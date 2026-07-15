"""Build bounded portable source-body verification command reports.

This module is checker-only report construction. It does not execute a
command, create a CLI, invoke shell commands, call subprocess, call network
services, mutate artifacts, embed full prior artifacts, or treat report
construction as command success.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


MODULE = "portable_source_body_verification_command"
REPORT_VERSION = "0.1.0"
PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_REPORT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "command_report"
)

STATUS_BUILT = "PORTABLE_VERIFICATION_COMMAND_REPORT_BUILT"
STATUS_NOT_BUILT = "PORTABLE_VERIFICATION_COMMAND_REPORT_NOT_BUILT"
STATUS_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_VERIFICATION_COMMAND_REPORT_REQUIRES_ADDITIONAL_BASIS"
)
STATUS_BLOCKED = "PORTABLE_VERIFICATION_COMMAND_REPORT_BLOCKED"
STATUS_FAMILY = {
    STATUS_BUILT,
    STATUS_NOT_BUILT,
    STATUS_REQUIRES_ADDITIONAL_BASIS,
    STATUS_BLOCKED,
}

SELECTED_REFERENCE_FIELDS = (
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

SELECTED_REFERENCE_REQUEST_FIELDS = (
    "selected_command_implementation_boundary_reference",
    "selected_command_boundary_reference",
    "selected_artifact_emission_containment_reference",
    "selected_evidence_manifest_reference",
    "selected_portable_verification_reference",
)

FULL_ARTIFACT_BODY_KEYS = {
    "full_artifact_body",
    "raw_artifact",
    "raw_result",
    "embedded_artifact",
    "selected_full_artifact",
    "complete_artifact_body",
    "raw_full_artifact_body",
    "artifact_body",
    "raw_artifact_body",
    "embedded_artifacts",
    "full_result",
    "raw_selected_basis",
}

FULL_ARTIFACT_BODY_POSTURE_KEYS = {
    "full_artifact_body_not_embedded",
    "omitted_full_artifact_body_keys",
    "large_string_omitted_from_reference_shape",
}

REQUIRED_FALSE_NON_CLAIMS = (
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
)

OUTPUT_FALSE_NON_CLAIMS = tuple(
    dict.fromkeys(
        REQUIRED_FALSE_NON_CLAIMS
        + (
            "report_became_source",
            "report_became_authority",
            "report_created_currentness",
            "source_transferred",
            "source_migrated",
            "source_received",
            "source_receipt_recorded",
            "reception_authorized",
            "authority_created",
            "currentness_created",
            "public_readiness_created",
            "path_created_currentness",
            "latest_file_created_currentness",
            "artifact_existence_created_currentness",
            "repository_copy_became_body",
            "carrier_possession_created_currentness",
            "environment_state_created_currentness",
            "os_became_authority",
            "vendor_environment_became_authority",
            "account_became_authority",
            "narration_created_currentness",
        )
    )
)

COLLAPSE_FIELD_CODES = (
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
    ("command_output_became_authority", "COMMAND_OUTPUT_TREATED_AS_AUTHORITY"),
    ("command_output_treated_as_authority", "COMMAND_OUTPUT_TREATED_AS_AUTHORITY"),
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
    ("command_became_authority", "COMMAND_TREATED_AS_AUTHORITY"),
    ("command_treated_as_authority", "COMMAND_TREATED_AS_AUTHORITY"),
    ("report_became_authority", "REPORT_TREATED_AS_AUTHORITY"),
    ("report_treated_as_authority", "REPORT_TREATED_AS_AUTHORITY"),
    ("report_created_authority", "REPORT_TREATED_AS_AUTHORITY"),
    ("report_became_source", "REPORT_TREATED_AS_SOURCE"),
    ("report_treated_as_source", "REPORT_TREATED_AS_SOURCE"),
    ("report_created_currentness", "REPORT_TREATED_AS_CURRENTNESS"),
    ("report_treated_as_currentness", "REPORT_TREATED_AS_CURRENTNESS"),
    ("full_prior_artifacts_embedded", "FULL_PRIOR_ARTIFACT_BODY_EMBEDDED"),
    ("full_prior_artifact_body_embedded", "FULL_PRIOR_ARTIFACT_BODY_EMBEDDED"),
    ("raw_full_artifact_body_embedded", "FULL_PRIOR_ARTIFACT_BODY_EMBEDDED"),
    ("prior_artifacts_mutated", "ARTIFACT_MUTATION_REQUESTED"),
    ("artifacts_mutated", "ARTIFACT_MUTATION_REQUESTED"),
    ("artifact_mutation_requested", "ARTIFACT_MUTATION_REQUESTED"),
    ("manifest_implemented", "MANIFEST_IMPLEMENTATION_CREATED"),
    ("checksum_implemented", "CHECKSUM_IMPLEMENTATION_CREATED"),
    ("signature_implemented", "SIGNATURE_IMPLEMENTATION_CREATED"),
    ("packet_implemented", "PACKET_IMPLEMENTATION_CREATED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
    ("public_launch_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("public_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("final_completion_claimed", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
    ("publication_flow_opened", "CONTINUATION_AUTHORIZED"),
    ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("successor_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ("source_transferred", "SOURCE_TRANSFER_CREATED"),
    ("source_migrated", "SOURCE_MIGRATION_CREATED"),
    ("source_received", "SOURCE_RECEIPT_CREATED"),
    ("source_receipt_recorded", "SOURCE_RECEIPT_CREATED"),
    ("reception_authorized", "RECEPTION_AUTHORIZED"),
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
    ("environment_state_created_currentness", "ENVIRONMENT_STATE_TREATED_AS_CURRENTNESS"),
    ("environment_state_treated_as_currentness", "ENVIRONMENT_STATE_TREATED_AS_CURRENTNESS"),
    ("os_became_authority", "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY"),
    ("vendor_environment_became_authority", "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY"),
    ("account_became_authority", "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY"),
    ("narration_created_currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
    ("narration_treated_as_currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
)


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
            "created",
            "executed",
            "authorized",
            "source",
            "authority",
            "currentness",
            "current",
            "success",
        }
    return bool(value)


def _is_false(value: Any) -> bool:
    if isinstance(value, bool):
        return value is False
    if isinstance(value, str):
        return value.strip().lower() in {"false", "no", "0"}
    return value == 0


def _is_zero_count(value: Any) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return value == 0
    if isinstance(value, str):
        return value.strip() == "0"
    return False


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _generated_at() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _safe_component(value: Any) -> str:
    text = str(value or "portable_verification_command_report").strip()
    cleaned = "".join(
        character if character.isalnum() or character in {"-", "_"} else "_"
        for character in text
    )
    cleaned = cleaned.strip("_")
    return cleaned or "portable_verification_command_report"


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


def _contains_full_artifact_body_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, nested_value in value.items():
            key_text = str(key)
            lowered = key_text.lower()
            full_body_key = (
                key_text not in FULL_ARTIFACT_BODY_POSTURE_KEYS
                and lowered not in FULL_ARTIFACT_BODY_POSTURE_KEYS
                and (
                    key_text in FULL_ARTIFACT_BODY_KEYS
                or lowered in FULL_ARTIFACT_BODY_KEYS
                or "artifact_body" in lowered
                or "result_body" in lowered
                or "complete_artifact_body" in lowered
                or lowered in {"raw_artifact", "raw_result", "selected_full_artifact"}
                )
            )
            if full_body_key:
                return True
            if _contains_full_artifact_body_key(nested_value):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_full_artifact_body_key(item) for item in value)
    return False


def _sanitize_reference_shape(value: Any, depth: int = 0) -> Any:
    if depth > 10:
        return {"reference_shape_depth_limit_reached": True}
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        omitted: list[str] = []
        for key, nested_value in value.items():
            key_text = str(key)
            lowered = key_text.lower()
            raw_artifact_key = (
                key_text not in FULL_ARTIFACT_BODY_POSTURE_KEYS
                and lowered not in FULL_ARTIFACT_BODY_POSTURE_KEYS
                and (
                    key_text in FULL_ARTIFACT_BODY_KEYS
                or lowered in FULL_ARTIFACT_BODY_KEYS
                or "artifact_body" in lowered
                or "result_body" in lowered
                or "complete_artifact_body" in lowered
                or lowered in {"raw_artifact", "raw_result", "selected_full_artifact"}
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


def _selected_references(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        field: request.get(field)
        for field in SELECTED_REFERENCE_REQUEST_FIELDS
    }


def _missing_reference_fields(reference: Any) -> list[str]:
    if not isinstance(reference, Mapping):
        return list(SELECTED_REFERENCE_FIELDS)
    return [
        field
        for field in SELECTED_REFERENCE_FIELDS
        if not _present(reference.get(field))
    ]


def _reference_failed_counts(references: Mapping[str, Any]) -> dict[str, Any]:
    counts: dict[str, Any] = {}
    for field, reference in references.items():
        if isinstance(reference, Mapping):
            counts[field] = reference.get("selected_result_failed_check_count")
        else:
            counts[field] = None
    return counts


def _collapse_code(value: Any) -> str | None:
    for key, code in COLLAPSE_FIELD_CODES:
        if _contains_truthy_key(value, key):
            return code
    return None


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


def _make_non_claims() -> dict[str, bool]:
    return {key: False for key in OUTPUT_FALSE_NON_CLAIMS}


def _report_non_meaning() -> dict[str, bool]:
    names = (
        "command_executed",
        "command_invoked",
        "command_output_created",
        "command_result_created",
        "command_success_created",
        "command_output_became_source",
        "command_output_became_authority",
        "command_success_created_currentness",
        "command_success_claimed_final_completion",
        "report_became_source",
        "report_became_authority",
        "report_created_currentness",
        "deployment_created",
        "runtime_hosting_created",
        "public_release_created",
        "continuation_authorized",
        "follow_on_work_authorized",
    )
    return {f"report_built_does_not_mean_{name}": True for name in names}


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "command execution boundary",
            "command invocation",
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


def _reference_shape_checks(
    request: Any,
    request_is_mapping: bool,
    references: Mapping[str, Any],
) -> list[dict[str, Any]]:
    request_map: Mapping[str, Any] = request if request_is_mapping else {}
    present_reference_names = {
        name: _present(value) for name, value in references.items()
    }
    missing_reference_fields = {
        name: _missing_reference_fields(value)
        for name, value in references.items()
        if _present(value)
    }
    all_references_mapping = all(
        isinstance(value, Mapping) for value in references.values() if _present(value)
    )
    selected_references_have_no_full_bodies = not any(
        _contains_full_artifact_body_key(value)
        for value in references.values()
        if _present(value)
    )
    all_required_reference_fields_present = (
        all(_present(value) for value in references.values())
        and all(not missing for missing in missing_reference_fields.values())
    )
    all_outcomes_declared = all(
        isinstance(value, Mapping)
        and _present(value.get("selected_result_outcome"))
        for value in references.values()
        if _present(value)
    )
    failed_counts = _reference_failed_counts(references)
    failed_counts_zero = all(
        _is_zero_count(count) for count in failed_counts.values()
    )
    full_body_embedded = _contains_full_artifact_body_key(
        {
            "selected_references": references,
            "declared_evidence_references": request_map.get(
                "declared_evidence_references"
            ),
        }
    )
    declared_evidence = request_map.get("declared_evidence_references")
    execution_posture = request_map.get("execution_non_authorization_posture")

    checks = [
        _check(
            "request is mapping",
            request_is_mapping,
            "declared command report request is a mapping",
            type(request).__name__,
            "COMMAND_REPORT_REQUEST_MALFORMED",
        ),
        _check(
            "command report request id declared",
            _present(request_map.get("command_report_request_id")),
            "command_report_request_id present",
            request_map.get("command_report_request_id"),
            "COMMAND_REPORT_REQUEST_MALFORMED",
        ),
        _check(
            "command report question declared",
            _present(request_map.get("command_report_question")),
            "command_report_question present",
            request_map.get("command_report_question"),
            "COMMAND_REPORT_QUESTION_UNDECLARED",
        ),
        _check(
            "command implementation-boundary reference present",
            _present(request_map.get("selected_command_implementation_boundary_reference")),
            "selected_command_implementation_boundary_reference present",
            present_reference_names.get("selected_command_implementation_boundary_reference"),
            "COMMAND_IMPLEMENTATION_BOUNDARY_REFERENCE_MISSING",
        ),
        _check(
            "command-boundary reference present",
            _present(request_map.get("selected_command_boundary_reference")),
            "selected_command_boundary_reference present",
            present_reference_names.get("selected_command_boundary_reference"),
            "COMMAND_BOUNDARY_REFERENCE_MISSING",
        ),
        _check(
            "artifact emission containment reference present",
            _present(request_map.get("selected_artifact_emission_containment_reference")),
            "selected_artifact_emission_containment_reference present",
            present_reference_names.get("selected_artifact_emission_containment_reference"),
            "ARTIFACT_EMISSION_CONTAINMENT_REFERENCE_MISSING",
        ),
        _check(
            "evidence-manifest reference present",
            _present(request_map.get("selected_evidence_manifest_reference")),
            "selected_evidence_manifest_reference present",
            present_reference_names.get("selected_evidence_manifest_reference"),
            "EVIDENCE_MANIFEST_REFERENCE_MISSING",
        ),
        _check(
            "portable verification reference present",
            _present(request_map.get("selected_portable_verification_reference")),
            "selected_portable_verification_reference present",
            present_reference_names.get("selected_portable_verification_reference"),
            "PORTABLE_VERIFICATION_REFERENCE_MISSING",
        ),
        _check(
            "declared evidence references present",
            _present(declared_evidence),
            "declared_evidence_references present",
            declared_evidence,
            "DECLARED_EVIDENCE_REFERENCES_MISSING",
        ),
        _check(
            "execution non-authorization posture declared",
            _present(execution_posture),
            "execution_non_authorization_posture present",
            execution_posture,
            "EXECUTION_NON_AUTHORIZATION_POSTURE_MISSING",
        ),
        _check(
            "all selected references are reference-shaped",
            all_references_mapping and selected_references_have_no_full_bodies,
            "selected references are mappings without full artifact bodies",
            {
                "all_references_mapping": all_references_mapping,
                "selected_references_have_no_full_bodies": (
                    selected_references_have_no_full_bodies
                ),
            },
            (
                "FULL_PRIOR_ARTIFACT_BODY_EMBEDDED"
                if not selected_references_have_no_full_bodies
                else "REFERENCE_SHAPE_MISSING_REQUIRED_FIELD"
            ),
        ),
        _check(
            "required selected result fields present",
            all_required_reference_fields_present,
            f"selected references include {list(SELECTED_REFERENCE_FIELDS)}",
            missing_reference_fields,
            "REFERENCE_SHAPE_MISSING_REQUIRED_FIELD",
        ),
        _check(
            "expected outcomes declared where supplied",
            all_outcomes_declared,
            "selected_result_outcome present on selected references",
            {
                name: value.get("selected_result_outcome")
                if isinstance(value, Mapping)
                else None
                for name, value in references.items()
            },
            "REFERENCE_SHAPE_MISSING_REQUIRED_FIELD",
        ),
        _check(
            "failed check counts are zero where required",
            failed_counts_zero,
            "selected_result_failed_check_count is zero on selected references",
            failed_counts,
            "REQUIRED_FAILED_CHECK_COUNT_NONZERO",
        ),
        _check(
            "no full prior artifact body embedded",
            not full_body_embedded,
            "no full prior artifact body keys in selected references or declared evidence",
            {"full_prior_artifact_body_embedded": full_body_embedded},
            "FULL_PRIOR_ARTIFACT_BODY_EMBEDDED",
        ),
    ]
    return checks


def _non_claim_checks(request: Any, request_is_mapping: bool) -> list[dict[str, Any]]:
    request_map: Mapping[str, Any] = request if request_is_mapping else {}
    declared = request_map.get("declared_non_claims")
    declared_is_mapping = isinstance(declared, Mapping)
    missing_or_flipped = []
    if declared_is_mapping:
        missing_or_flipped = [
            key
            for key in REQUIRED_FALSE_NON_CLAIMS
            if key not in declared or not _is_false(declared[key])
        ]
    else:
        missing_or_flipped = list(REQUIRED_FALSE_NON_CLAIMS)

    collapse_code = _collapse_code(request_map)
    command_execution_authorized = collapse_code == "COMMAND_EXECUTION_AUTHORIZED"
    command_invocation_created = collapse_code == "COMMAND_INVOCATION_CREATED"
    command_output_created = collapse_code == "COMMAND_OUTPUT_CREATED"
    command_result_created = collapse_code == "COMMAND_RESULT_CREATED"
    command_success_created = collapse_code == "COMMAND_SUCCESS_CREATED"
    report_authority_collapse = collapse_code in {
        "REPORT_TREATED_AS_AUTHORITY",
        "REPORT_TREATED_AS_SOURCE",
        "REPORT_TREATED_AS_CURRENTNESS",
    }
    path_currentness = collapse_code in {
        "PATH_TREATED_AS_CURRENTNESS",
        "LATEST_FILE_TREATED_AS_CURRENTNESS",
    }
    artifact_currentness = collapse_code == "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS"

    return [
        _check(
            "declared non-claims present",
            declared_is_mapping,
            "declared_non_claims mapping present",
            declared,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "required non-claims false",
            declared_is_mapping and not missing_or_flipped,
            "all required non-claims explicit and false",
            {"missing_or_flipped": missing_or_flipped},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "command execution not authorized",
            not command_execution_authorized
            and not _contains_truthy_key(request_map, "command_authorized_to_run")
            and not _contains_truthy_key(request_map, "command_executed"),
            "no command execution authorization or execution",
            {"collapse_code": collapse_code},
            "COMMAND_EXECUTION_AUTHORIZED",
        ),
        _check(
            "command invocation not created",
            not command_invocation_created,
            "no command invocation",
            {"collapse_code": collapse_code},
            "COMMAND_INVOCATION_CREATED",
        ),
        _check(
            "command output not created",
            not command_output_created,
            "no command output",
            {"collapse_code": collapse_code},
            "COMMAND_OUTPUT_CREATED",
        ),
        _check(
            "command result not created",
            not command_result_created,
            "no command result",
            {"collapse_code": collapse_code},
            "COMMAND_RESULT_CREATED",
        ),
        _check(
            "command success not created",
            not command_success_created,
            "no command success",
            {"collapse_code": collapse_code},
            "COMMAND_SUCCESS_CREATED",
        ),
        _check(
            "report remains non-authoritative",
            not report_authority_collapse,
            "report is not source, authority, or currentness",
            {"collapse_code": collapse_code},
            "REPORT_TREATED_AS_AUTHORITY",
        ),
        _check(
            "path does not create currentness",
            not path_currentness,
            "path and latest-file posture do not create currentness",
            {"collapse_code": collapse_code},
            "PATH_TREATED_AS_CURRENTNESS",
        ),
        _check(
            "artifact existence does not create currentness",
            not artifact_currentness,
            "artifact existence does not create currentness",
            {"collapse_code": collapse_code},
            "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS",
        ),
        _check(
            "no collapse-shaped overread flags present",
            collapse_code is None,
            "no command, report, artifact, deployment, currentness, completion, continuation, or follow-on overread flags",
            {"collapse_code": collapse_code},
            collapse_code or "COMMAND_REPORT_REQUEST_MALFORMED",
        ),
    ]


def _first_blocking_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    not_build_only_codes = {"REQUIRED_FAILED_CHECK_COUNT_NONZERO"}
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if code and code not in not_build_only_codes:
                return str(code)
    return None


def _failed_check_count(checks: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is False)


def _passed_check_count(checks: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _requested_status(request: Mapping[str, Any]) -> str | None:
    value = request.get("requested_command_report_status")
    if value in STATUS_FAMILY:
        return str(value)
    return None


def _resolve_status(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
) -> str:
    if block_code is not None:
        return STATUS_BLOCKED
    requested = _requested_status(request)
    if requested in {STATUS_NOT_BUILT, STATUS_REQUIRES_ADDITIONAL_BASIS}:
        return requested
    if _failed_check_count(checks):
        return STATUS_NOT_BUILT
    return STATUS_BUILT


def _bounded_report_statement(
    status: str,
    reference_checks: Sequence[Mapping[str, Any]],
    non_claim_checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    reference_shape_checks_passed = all(
        check.get("passed") is True for check in reference_checks
    )
    non_claim_checks_passed = all(
        check.get("passed") is True for check in non_claim_checks
    )
    built = status == STATUS_BUILT
    non_claim_lookup = {
        check.get("check_name"): check.get("passed") is True
        for check in non_claim_checks
    }
    return {
        "portable_verification_command_report_built": built,
        "checker_findings_built": built,
        "reference_shape_checks_passed": built and reference_shape_checks_passed,
        "non_claim_checks_passed": built and non_claim_checks_passed,
        "report_is_non_authoritative": non_claim_lookup.get(
            "report remains non-authoritative", False
        ),
        "command_execution_not_authorized": non_claim_lookup.get(
            "command execution not authorized", False
        ),
        "command_invocation_not_created": non_claim_lookup.get(
            "command invocation not created", False
        ),
        "command_output_not_created": non_claim_lookup.get(
            "command output not created", False
        ),
        "command_result_not_created": non_claim_lookup.get(
            "command result not created", False
        ),
        "command_success_not_created": non_claim_lookup.get(
            "command success not created", False
        ),
        "command_executed": False,
        "command_output_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "final_completion_claimed": False,
        "report_building_is_not_live_command_execution": True,
        "report_building_is_not_command_invocation": True,
        "report_building_is_not_command_output_from_a_run": True,
        "report_status_is_not_command_success": True,
    }


def _checker_findings(
    status: str,
    checks: Sequence[Mapping[str, Any]],
    statement: Mapping[str, Any],
) -> dict[str, Any]:
    failed = [check for check in checks if check.get("passed") is False]
    return {
        "checker_findings_built": status == STATUS_BUILT,
        "findings_are_non_authoritative": True,
        "findings_are_not_command_output_from_live_execution": True,
        "passed_check_count": _passed_check_count(checks),
        "failed_check_count": _failed_check_count(checks),
        "failed_checks": [
            {
                "check_name": check.get("check_name"),
                "failure_code": check.get("failure_code"),
            }
            for check in failed
        ],
        "report_statement_reference": {
            "portable_verification_command_report_built": statement.get(
                "portable_verification_command_report_built"
            ),
            "report_is_non_authoritative": statement.get("report_is_non_authoritative"),
            "command_execution_not_authorized": statement.get(
                "command_execution_not_authorized"
            ),
        },
    }


def build_portable_verification_command_summary(
    report: Mapping[str, Any]
) -> dict[str, Any]:
    """Build a bounded summary of a command report object."""

    statement = report.get("bounded_report_statement", {})
    checker_findings = report.get("checker_findings", {})
    block = report.get("block", {})
    declared = report.get("declared_command_report_question", {})
    non_claims = report.get("non_claims", {})
    status = report.get("status")
    key_non_claims = {
        key: non_claims.get(key)
        for key in REQUIRED_FALSE_NON_CLAIMS
        if key in non_claims
    }
    return {
        "status": status,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "command_report_request_id": declared.get("command_report_request_id"),
        "command_report_question": declared.get("command_report_question"),
        "passed_check_count": checker_findings.get("passed_check_count", 0),
        "failed_check_count": checker_findings.get("failed_check_count", 0),
        "report_built": status == STATUS_BUILT,
        "checker_findings_built": statement.get("checker_findings_built") is True,
        "reference_shape_checks_passed": statement.get(
            "reference_shape_checks_passed"
        )
        is True,
        "non_claim_checks_passed": statement.get("non_claim_checks_passed") is True,
        "report_non_authoritative": statement.get("report_is_non_authoritative")
        is True,
        "command_execution_not_authorized": statement.get(
            "command_execution_not_authorized"
        )
        is True,
        "command_invocation_not_created": statement.get(
            "command_invocation_not_created"
        )
        is True,
        "command_output_not_created": statement.get("command_output_not_created")
        is True,
        "command_result_not_created": statement.get("command_result_not_created")
        is True,
        "command_success_not_created": statement.get("command_success_not_created")
        is True,
        "no_full_prior_artifacts_embedded": non_claims.get(
            "full_prior_artifacts_embedded"
        )
        is False,
        "no_artifact_mutation": non_claims.get("prior_artifacts_mutated") is False,
        "no_deployment_runtime_public_release": (
            non_claims.get("deployment_created") is False
            and non_claims.get("runtime_hosting_created") is False
            and non_claims.get("public_release_created") is False
        ),
        "no_operation_permission_public_readiness_final_completion": (
            non_claims.get("operation_permission_created") is False
            and non_claims.get("public_launch_readiness_created") is False
            and non_claims.get("final_completion_claimed") is False
        ),
        "no_continuation_publication_flow_reusable_permission": (
            non_claims.get("continuation_authorized") is False
            and non_claims.get("publication_flow_opened") is False
            and non_claims.get("reusable_permission_created") is False
        ),
        "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work": (
            non_claims.get("derivative_reception_authorized") is False
            and non_claims.get("vessel_relation_authorized") is False
            and non_claims.get("another_reception_request_authorized") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": key_non_claims,
    }


def build_portable_verification_command_report(
    request: Mapping[str, Any]
) -> dict[str, Any]:
    """Build a bounded non-authoritative report from declared references.

    Report building is not live command execution, command invocation, command
    output from a run, command result from execution, or command success.
    """

    request_is_mapping = isinstance(request, Mapping)
    request_map: Mapping[str, Any] = request if request_is_mapping else {}
    request_id = request_map.get("command_report_request_id")
    references = _selected_references(request_map)
    reference_checks = _reference_shape_checks(request, request_is_mapping, references)
    non_claim_checks = _non_claim_checks(request, request_is_mapping)
    all_checks = reference_checks + non_claim_checks
    block_code = _first_blocking_code(all_checks)
    status = _resolve_status(request_map, all_checks, block_code)
    block_reason = None
    if block_code is not None:
        failed_names = [
            str(check.get("check_name"))
            for check in all_checks
            if check.get("passed") is False
        ]
        block_reason = "; ".join(failed_names) or block_code

    statement = _bounded_report_statement(status, reference_checks, non_claim_checks)
    checker_findings = _checker_findings(status, all_checks, statement)

    report: dict[str, Any] = {
        "portable_source_body_verification_command_report_metadata": {
            "portable_source_body_verification_command_report_id": _safe_component(
                request_id
            ),
            "portable_source_body_verification_command_report_type": (
                "portable_source_body_verification_command_report"
            ),
            "portable_source_body_verification_command_report_version": REPORT_VERSION,
            "generated_at": _generated_at(),
            "module": MODULE,
        },
        "declared_command_report_question": {
            "command_report_request_id": _copy(request_id),
            "command_report_question": _copy(
                request_map.get("command_report_question")
            ),
            "command_report_question_declared": _present(
                request_map.get("command_report_question")
            ),
        },
        "selected_command_implementation_boundary_reference": _sanitize_reference_shape(
            request_map.get("selected_command_implementation_boundary_reference", {})
        ),
        "selected_command_boundary_reference": _sanitize_reference_shape(
            request_map.get("selected_command_boundary_reference", {})
        ),
        "selected_artifact_emission_containment_reference": _sanitize_reference_shape(
            request_map.get("selected_artifact_emission_containment_reference", {})
        ),
        "selected_evidence_manifest_reference": _sanitize_reference_shape(
            request_map.get("selected_evidence_manifest_reference", {})
        ),
        "selected_portable_verification_reference": _sanitize_reference_shape(
            request_map.get("selected_portable_verification_reference", {})
        ),
        "declared_evidence_references": _sanitize_reference_shape(
            request_map.get("declared_evidence_references", {})
        ),
        "reference_shape_checks": reference_checks,
        "non_claim_checks": non_claim_checks,
        "checker_findings": checker_findings,
        "bounded_report_statement": statement,
        "report_non_meaning": _report_non_meaning(),
        "what_remains_open": _what_remains_open(),
        "non_claims": _make_non_claims(),
        "status": status,
        "block": _block(block_code, block_reason),
        "portable_source_body_verification_command_summary": {},
    }
    report["portable_source_body_verification_command_summary"] = (
        build_portable_verification_command_summary(report)
    )
    return report


def _default_report_filename(report: Mapping[str, Any]) -> str:
    metadata = report.get("portable_source_body_verification_command_report_metadata", {})
    declared = report.get("declared_command_report_question", {})
    request_id = (
        declared.get("command_report_request_id")
        if isinstance(declared, Mapping)
        else None
    )
    if not _present(request_id) and isinstance(metadata, Mapping):
        request_id = metadata.get("portable_source_body_verification_command_report_id")
    return (
        f"{_safe_component(request_id)}__"
        "portable_source_body_verification_command_report.json"
    )


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter:03d}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def write_portable_verification_command_report(
    report: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded report JSON artifact additively.

    Writing a report is not command execution. This function does not read,
    repair, normalize, compact, delete, or mutate upstream artifacts.
    """

    filename = _default_report_filename(report)
    if output_path is None:
        target = PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_REPORT_ROOT / filename
    else:
        candidate = Path(output_path)
        target = candidate / filename if candidate.suffix == "" else candidate
    target = _non_overwriting_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(report), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
