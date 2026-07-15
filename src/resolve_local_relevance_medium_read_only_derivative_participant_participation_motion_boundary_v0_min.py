"""Minimal resolver for the local read-only derivative participant boundary."""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class LocalRelevanceMediumReadOnlyDerivativeParticipantParticipationMotionBoundaryV0MinError(
    Exception
):
    """Raised when this resolver is asked to emit an unsupported boundary."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_derivative_participant_"
    "participation_motion_boundary_v0_min"
)
BOUNDARY_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_"
    "PARTICIPATION_MOTION_BOUNDARY"
)
BOUNDARY_SCOPE = "SELECTED_PARTICIPATION_MOTION_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_"
    "PARTICIPATION_MOTION_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_"
    "PARTICIPATION_MOTION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_"
    "PARTICIPATION_MOTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_"
    "PARTICIPATION_MOTION_BOUNDARY_BLOCKED"
)

ROLE_ADMISSION_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_RECORDED"
)
CONTINUATION_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_RECORDED"
ROLE_OBJECT = "local_relevance_medium_read_only_derivative_participant_role_admission"
ROLE_STATEMENT = (
    "local_relevance_medium_read_only_derivative_participant_role_admission_statement"
)
ROLE_SUMMARY = (
    "local_relevance_medium_read_only_derivative_participant_role_admission_summary"
)
ROLE_NON_MEANING = (
    "local_relevance_medium_read_only_derivative_participant_role_admission_non_meaning"
)
ROLE_METADATA = (
    "local_relevance_medium_read_only_derivative_participant_role_admission_metadata"
)
CONTINUATION_OBJECT = "local_relevance_medium_read_only_continuation"
CONTINUATION_STATEMENT = "local_relevance_medium_read_only_continuation_statement"
CONTINUATION_SUMMARY = "local_relevance_medium_read_only_continuation_summary"
CONTINUATION_NON_MEANING = "local_relevance_medium_read_only_continuation_non_meaning"
CONTINUATION_METADATA = "local_relevance_medium_read_only_continuation_metadata"

DEFAULT_BOUNDARY_ID = (
    "local_relevance_medium_read_only_derivative_participant_"
    "participation_motion_boundary_001"
)
DEFAULT_ROLE_ADMISSION_TERMINAL_SUMMARY = (
    "spec/LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_"
    "ROLE_ADMISSION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_ROLE_ADMISSION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "derivative_participant_role_admission_v0_min_v2/"
    "local_relevance_medium_read_only_derivative_participant_role_admission_001__"
    "local_relevance_medium_read_only_derivative_participant_role_admission_"
    "v0_min_v2_result.json"
)
DEFAULT_CONTINUATION_TERMINAL_SUMMARY = (
    "spec/LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_CONTINUATION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "continuation_v0_min/"
    "local_relevance_medium_read_only_continuation_reference_review_001__"
    "local_relevance_medium_read_only_continuation_v0_min_result.json"
)
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "derivative_participant_participation_motion_boundary_v0_min"
)

INTENT_RECORD = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_"
    "PARTICIPATION_MOTION_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_"
    "PARTICIPATION_MOTION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_"
    "PARTICIPATION_MOTION_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

BOUNDARY_QUESTION = (
    "Given one clean local relevance medium read-only derivative participant "
    "role-admission artifact and one clean selected local relevance medium "
    "read-only continuation artifact for selected command state, may one local "
    "read-only derivative participant participation-motion boundary be recorded "
    "only so a future bounded participation-motion step may be considered?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "participation_motion_created",
    "participant_output_authorized",
    "action_authorization_created",
    "participant_reentry_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "third_operation_created",
    "unbounded_operation_sequence_created",
    "reusable_operation_permission_created",
    "general_operation_permission_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
    "unsupported_lookup_keys_permitted",
    "new_lookup_entry_created",
    "new_signal_accepted",
    "new_entry_accepted",
    "new_relevance_object_created",
    "new_index_entry_created",
    "filesystem_discovery_performed",
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "registry_created",
    "search_surface_created",
    "query_surface_created",
    "ranking_surface_created",
    "scoring_surface_created",
    "priority_surface_created",
    "validity_judgment_created",
    "truth_judgment_created",
    "authority_judgment_created",
    "currentness_judgment_created",
    "received_derivative_participation_authority_imported",
    "received_derivative_action_authority_imported",
    "bounded_derivative_vessel_authority_imported",
    "derivative_vessel_relation_authority_imported",
    "role_admission_treated_as_participation_permission",
    "artifact_existence_treated_as_participation_motion_authority",
    "latest_file_posture_treated_as_participation_motion_authority",
    "repo_local_availability_treated_as_participation_motion_authority",
    "hidden_repo_state_used_as_participation_motion_content",
    "hidden_repo_state_used_as_participation_motion_authority",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "synchronization_created",
    "deployment_created",
    "public_release_created",
    "broader_reusable_permission_created",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "continuation_v1_failure_repaired",
    "continuation_v1_failure_hidden",
    "continuation_v1_failure_claimed_passed",
    "role_admission_v1_failure_repaired",
    "role_admission_v1_failure_hidden",
    "role_admission_v1_failure_claimed_passed",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ROLE_TRUE_FIELDS = (
    "local_relevance_medium_read_only_derivative_participant_role_admission_recorded",
    "derivative_participant_role_admission_created",
    "bounded_derivative_participant_role_admitted",
    "role_admission_local_only",
    "role_admission_read_only",
    "role_admission_selected_state_only",
    "role_admission_basis_reference_only",
    "role_admission_inside_continuation_body",
    "role_admission_from_continuation_only",
)
CONTINUATION_TRUE_FIELDS = (
    "selected_continuation_recorded",
    "continuation_created",
    "continuation_local_only",
    "continuation_read_only",
    "continuation_basis_reference_only",
    "continuation_selected_state_only",
    "continuation_from_second_operation",
    "continuation_sequence_count_is_2",
)
BOUNDARY_TRUE_FIELDS = (
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_recorded",
    "future_participation_motion_may_be_considered",
    "participation_motion_boundary_created",
    "participation_motion_boundary_local_only",
    "participation_motion_boundary_read_only",
    "participation_motion_boundary_selected_state_only",
    "participation_motion_boundary_basis_reference_only",
)
EVIDENCE_TRUE_FIELDS = (
    "continuation_v1_failure_evidence_preserved",
    "role_admission_v1_failure_evidence_preserved",
    "predecessor_failure_evidence_preserved",
)

ADDITIONAL_BASIS_CODES = {
    "ROLE_ADMISSION_TERMINAL_SUMMARY_PATH_MISSING",
    "ROLE_ADMISSION_ARTIFACT_PATH_MISSING",
    "ROLE_ADMISSION_ARTIFACT_UNREADABLE",
    "ROLE_ADMISSION_ARTIFACT_NOT_JSON_OBJECT",
    "ROLE_ADMISSION_ARTIFACT_NOT_RECORDED",
    "ROLE_ADMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "ROLE_ADMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    "CONTINUATION_TERMINAL_SUMMARY_PATH_MISSING",
    "CONTINUATION_ARTIFACT_PATH_MISSING",
    "CONTINUATION_ARTIFACT_UNREADABLE",
    "CONTINUATION_ARTIFACT_NOT_JSON_OBJECT",
    "CONTINUATION_ARTIFACT_NOT_RECORDED",
    "CONTINUATION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "CONTINUATION_ARTIFACT_VERSION_NOT_0_1_0",
}

BLOCK_CODES = ADDITIONAL_BASIS_CODES | {
    "PARTICIPATION_MOTION_BOUNDARY_QUESTION_UNDECLARED",
    "PARTICIPATION_MOTION_BOUNDARY_INTENT_UNSUPPORTED",
    "PARTICIPATION_MOTION_BOUNDARY_BLOCK_REQUESTED",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SELECTED_PARTICIPATION_MOTION_CONSIDERATION_ONLY",
    "ROLE_ADMISSION_NOT_RECORDED",
    "DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_NOT_CREATED",
    "BOUNDED_DERIVATIVE_PARTICIPANT_ROLE_NOT_ADMITTED",
    "ROLE_ADMISSION_LOCAL_ONLY_NOT_TRUE",
    "ROLE_ADMISSION_READ_ONLY_NOT_TRUE",
    "ROLE_ADMISSION_SELECTED_STATE_ONLY_NOT_TRUE",
    "ROLE_ADMISSION_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "ROLE_ADMISSION_NOT_INSIDE_CONTINUATION_BODY",
    "ROLE_ADMISSION_NOT_FROM_CONTINUATION_ONLY",
    "SELECTED_CONTINUATION_NOT_RECORDED",
    "CONTINUATION_NOT_CREATED",
    "CONTINUATION_LOCAL_ONLY_NOT_TRUE",
    "CONTINUATION_READ_ONLY_NOT_TRUE",
    "CONTINUATION_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "CONTINUATION_SELECTED_STATE_ONLY_NOT_TRUE",
    "CONTINUATION_FROM_SECOND_OPERATION_NOT_TRUE",
    "CONTINUATION_SEQUENCE_COUNT_NOT_2",
    "CONTINUATION_OPERATION_SEQUENCE_COUNT_NOT_2",
    "PARTICIPATION_MOTION_BOUNDARY_NOT_RECORDED",
    "FUTURE_PARTICIPATION_MOTION_MAY_NOT_BE_CONSIDERED",
    "PARTICIPATION_MOTION_BOUNDARY_NOT_CREATED",
    "PARTICIPATION_MOTION_BOUNDARY_LOCAL_ONLY_NOT_TRUE",
    "PARTICIPATION_MOTION_BOUNDARY_READ_ONLY_NOT_TRUE",
    "PARTICIPATION_MOTION_BOUNDARY_SELECTED_STATE_ONLY_NOT_TRUE",
    "PARTICIPATION_MOTION_BOUNDARY_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "CONTINUATION_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
    "ROLE_ADMISSION_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
    "PREDECESSOR_FAILURE_EVIDENCE_NOT_PRESERVED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_PARTICIPATION_MOTION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_PARTICIPATION_MOTION_BOUNDARY_REQUEST_UNREADABLE",
} | {key.upper() for key in REQUIRED_FALSE_NON_CLAIMS}

ROLE_FIELD_CODES = {
    "local_relevance_medium_read_only_derivative_participant_role_admission_recorded": (
        "ROLE_ADMISSION_NOT_RECORDED"
    ),
    "derivative_participant_role_admission_created": (
        "DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_NOT_CREATED"
    ),
    "bounded_derivative_participant_role_admitted": (
        "BOUNDED_DERIVATIVE_PARTICIPANT_ROLE_NOT_ADMITTED"
    ),
    "role_admission_local_only": "ROLE_ADMISSION_LOCAL_ONLY_NOT_TRUE",
    "role_admission_read_only": "ROLE_ADMISSION_READ_ONLY_NOT_TRUE",
    "role_admission_selected_state_only": "ROLE_ADMISSION_SELECTED_STATE_ONLY_NOT_TRUE",
    "role_admission_basis_reference_only": "ROLE_ADMISSION_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "role_admission_inside_continuation_body": (
        "ROLE_ADMISSION_NOT_INSIDE_CONTINUATION_BODY"
    ),
    "role_admission_from_continuation_only": "ROLE_ADMISSION_NOT_FROM_CONTINUATION_ONLY",
}
CONTINUATION_FIELD_CODES = {
    "selected_continuation_recorded": "SELECTED_CONTINUATION_NOT_RECORDED",
    "continuation_created": "CONTINUATION_NOT_CREATED",
    "continuation_local_only": "CONTINUATION_LOCAL_ONLY_NOT_TRUE",
    "continuation_read_only": "CONTINUATION_READ_ONLY_NOT_TRUE",
    "continuation_basis_reference_only": "CONTINUATION_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "continuation_selected_state_only": "CONTINUATION_SELECTED_STATE_ONLY_NOT_TRUE",
    "continuation_from_second_operation": "CONTINUATION_FROM_SECOND_OPERATION_NOT_TRUE",
    "continuation_sequence_count_is_2": "CONTINUATION_SEQUENCE_COUNT_NOT_2",
}
BOUNDARY_FIELD_CODES = {
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_recorded": (
        "PARTICIPATION_MOTION_BOUNDARY_NOT_RECORDED"
    ),
    "future_participation_motion_may_be_considered": (
        "FUTURE_PARTICIPATION_MOTION_MAY_NOT_BE_CONSIDERED"
    ),
    "participation_motion_boundary_created": "PARTICIPATION_MOTION_BOUNDARY_NOT_CREATED",
    "participation_motion_boundary_local_only": (
        "PARTICIPATION_MOTION_BOUNDARY_LOCAL_ONLY_NOT_TRUE"
    ),
    "participation_motion_boundary_read_only": (
        "PARTICIPATION_MOTION_BOUNDARY_READ_ONLY_NOT_TRUE"
    ),
    "participation_motion_boundary_selected_state_only": (
        "PARTICIPATION_MOTION_BOUNDARY_SELECTED_STATE_ONLY_NOT_TRUE"
    ),
    "participation_motion_boundary_basis_reference_only": (
        "PARTICIPATION_MOTION_BOUNDARY_BASIS_REFERENCE_ONLY_NOT_TRUE"
    ),
}
EVIDENCE_FIELD_CODES = {
    "continuation_v1_failure_evidence_preserved": (
        "CONTINUATION_V1_FAILURE_EVIDENCE_NOT_PRESERVED"
    ),
    "role_admission_v1_failure_evidence_preserved": (
        "ROLE_ADMISSION_V1_FAILURE_EVIDENCE_NOT_PRESERVED"
    ),
    "predecessor_failure_evidence_preserved": "PREDECESSOR_FAILURE_EVIDENCE_NOT_PRESERVED",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _path_text(value: Any) -> str:
    if isinstance(value, Path):
        return str(value)
    return value.strip() if isinstance(value, str) else ""


def _redact(value: Any, key: str = "") -> Any:
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        lowered = key.lower()
        if (
            lowered.startswith("raw_")
            or lowered.endswith("_body")
            or "hidden_repo_state" in lowered
            or "authorization_token" in lowered
            or "RAW_" in value
            or "HIDDEN_REPO_STATE" in value
        ):
            return "[REDACTED]"
        return value
    if isinstance(value, Mapping):
        return {str(k): _redact(v, str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_redact(item, key) for item in value]
    return str(value)


def _read_json_object(
    path_value: Any, missing: str, unreadable: str, not_object: str
) -> tuple[dict[str, Any] | None, str | None]:
    path_text = _path_text(path_value)
    if not path_text:
        return None, missing
    try:
        with Path(path_text).open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        return None, unreadable
    if not isinstance(loaded, Mapping):
        return None, not_object
    return dict(loaded), None


def _section(artifact: Mapping[str, Any] | None, key: str) -> Mapping[str, Any]:
    return _mapping(artifact.get(key) if artifact else None)


def _checks(artifact: Mapping[str, Any] | None, key: str) -> list[Mapping[str, Any]]:
    value = artifact.get(key) if artifact else None
    return [item for item in value if isinstance(item, Mapping)] if isinstance(value, list) else []


def _first(sections: Iterable[Mapping[str, Any]], key: str) -> Any:
    for section in sections:
        if key in section:
            return section[key]
    return None


def _bool(sections: Iterable[Mapping[str, Any]], key: str) -> bool | None:
    value = _first(sections, key)
    return value if isinstance(value, bool) else None


def _int(value: Any) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _role_sections(artifact: Mapping[str, Any] | None) -> tuple[Mapping[str, Any], ...]:
    return (
        _section(artifact, ROLE_OBJECT),
        _section(artifact, ROLE_STATEMENT),
        _section(artifact, ROLE_SUMMARY),
        _section(artifact, ROLE_NON_MEANING),
    )


def _continuation_sections(
    artifact: Mapping[str, Any] | None,
) -> tuple[Mapping[str, Any], ...]:
    return (
        _section(artifact, CONTINUATION_OBJECT),
        _section(artifact, CONTINUATION_STATEMENT),
        _section(artifact, CONTINUATION_SUMMARY),
        _section(artifact, CONTINUATION_NON_MEANING),
    )


def _artifact_outcome(artifact: Mapping[str, Any] | None, summary_key: str) -> str | None:
    if not artifact:
        return None
    for section in (artifact, _section(artifact, summary_key)):
        value = section.get("outcome")
        if isinstance(value, str):
            return value
    return None


def _artifact_version(
    artifact: Mapping[str, Any] | None,
    object_key: str,
    summary_key: str,
    metadata_key: str,
    version_keys: tuple[str, ...],
) -> str | None:
    if not artifact:
        return None
    for section in (
        artifact,
        _section(artifact, summary_key),
        _section(artifact, metadata_key),
        _section(artifact, object_key),
    ):
        for key in ("result_version",) + version_keys:
            value = section.get(key)
            if isinstance(value, str):
                return value
    return None


def _failed_count(
    artifact: Mapping[str, Any] | None, summary_key: str, checks_key: str
) -> int | None:
    if not artifact:
        return None
    for section in (artifact, _section(artifact, summary_key)):
        for key in ("failed_check_count", "failed_checks_count"):
            count = _int(section.get(key))
            if count is not None:
                return count
    checks = _checks(artifact, checks_key)
    return len([check for check in checks if check.get("passed") is False]) if checks else None


def _passed_count(
    artifact: Mapping[str, Any] | None, summary_key: str, checks_key: str
) -> int | None:
    if not artifact:
        return None
    for section in (artifact, _section(artifact, summary_key)):
        count = _int(section.get("passed_check_count"))
        if count is not None:
            return count
    checks = _checks(artifact, checks_key)
    return len([check for check in checks if check.get("passed") is True]) if checks else None


def _clean_role(artifact: Mapping[str, Any] | None) -> bool:
    return (
        _artifact_outcome(artifact, ROLE_SUMMARY) == ROLE_ADMISSION_OUTCOME
        and _artifact_version(
            artifact,
            ROLE_OBJECT,
            ROLE_SUMMARY,
            ROLE_METADATA,
            (
                "local_relevance_medium_read_only_derivative_participant_role_admission_version",
                "role_admission_version",
            ),
        )
        == RESULT_VERSION
        and _failed_count(
            artifact,
            ROLE_SUMMARY,
            "local_relevance_medium_read_only_derivative_participant_role_admission_checks",
        )
        == 0
        and bool(_section(artifact, ROLE_OBJECT))
    )


def _clean_continuation(artifact: Mapping[str, Any] | None) -> bool:
    return (
        _artifact_outcome(artifact, CONTINUATION_SUMMARY) == CONTINUATION_OUTCOME
        and _artifact_version(
            artifact,
            CONTINUATION_OBJECT,
            CONTINUATION_SUMMARY,
            CONTINUATION_METADATA,
            ("local_relevance_medium_read_only_continuation_version", "continuation_version"),
        )
        == RESULT_VERSION
        and _failed_count(
            artifact,
            CONTINUATION_SUMMARY,
            "local_relevance_medium_read_only_continuation_checks",
        )
        == 0
        and bool(_section(artifact, CONTINUATION_OBJECT))
    )


def _role_value(artifact: Mapping[str, Any] | None, key: str, clean: bool) -> bool:
    value = _bool(_role_sections(artifact), key)
    if value is not None:
        return value
    if key == "local_relevance_medium_read_only_derivative_participant_role_admission_recorded":
        alias_value = _bool(_role_sections(artifact), "role_admission_recorded")
        return alias_value if alias_value is not None else clean
    return False


def _continuation_value(artifact: Mapping[str, Any] | None, key: str, clean: bool) -> bool:
    value = _bool(_continuation_sections(artifact), key)
    if value is not None:
        return value
    if key == "selected_continuation_recorded":
        alias_value = _bool(
            _continuation_sections(artifact),
            "local_relevance_medium_read_only_continuation_recorded",
        )
        return alias_value if alias_value is not None else clean
    if key == "continuation_sequence_count_is_2":
        return _first(_continuation_sections(artifact), "continuation_operation_sequence_count") == 2
    return False


def _continuation_count(artifact: Mapping[str, Any] | None, clean: bool) -> int | None:
    count = _int(_first(_continuation_sections(artifact), "continuation_operation_sequence_count"))
    return count if count is not None else (2 if clean else None)


def _forbidden_value(
    role_artifact: Mapping[str, Any] | None,
    continuation_artifact: Mapping[str, Any] | None,
    key: str,
) -> bool:
    sections = (
        _role_sections(role_artifact)
        + _continuation_sections(continuation_artifact)
        + (
            _mapping(role_artifact.get("non_claims") if role_artifact else None),
            _mapping(continuation_artifact.get("non_claims") if continuation_artifact else None),
        )
    )
    for section in sections:
        value = section.get(key)
        if value is True:
            return True
    return False


def _evidence(
    role_artifact: Mapping[str, Any] | None,
    continuation_artifact: Mapping[str, Any] | None,
    key: str,
) -> bool:
    value = _bool(_role_sections(role_artifact) + _continuation_sections(continuation_artifact), key)
    if value is not None:
        return value
    if key == "role_admission_v1_failure_evidence_preserved":
        return _clean_role(role_artifact)
    return False


def _role_basis(
    artifact: Mapping[str, Any] | None, error: str | None
) -> dict[str, Any]:
    clean = _clean_role(artifact) and error is None
    basis = {key: _role_value(artifact, key, clean) for key in ROLE_TRUE_FIELDS}
    basis.update(
        {
            "outcome": _artifact_outcome(artifact, ROLE_SUMMARY),
            "result_version": _artifact_version(
                artifact,
                ROLE_OBJECT,
                ROLE_SUMMARY,
                ROLE_METADATA,
                (
                    "local_relevance_medium_read_only_derivative_participant_role_admission_version",
                    "role_admission_version",
                ),
            ),
            "failed_check_count": _failed_count(
                artifact,
                ROLE_SUMMARY,
                "local_relevance_medium_read_only_derivative_participant_role_admission_checks",
            ),
            "passed_check_count": _passed_count(
                artifact,
                ROLE_SUMMARY,
                "local_relevance_medium_read_only_derivative_participant_role_admission_checks",
            ),
            "clean": clean,
            "read_error": error,
        }
    )
    return basis


def _continuation_basis(
    artifact: Mapping[str, Any] | None, error: str | None
) -> dict[str, Any]:
    clean = _clean_continuation(artifact) and error is None
    basis = {key: _continuation_value(artifact, key, clean) for key in CONTINUATION_TRUE_FIELDS}
    basis.update(
        {
            "continuation_operation_sequence_count": _continuation_count(artifact, clean),
            "outcome": _artifact_outcome(artifact, CONTINUATION_SUMMARY),
            "result_version": _artifact_version(
                artifact,
                CONTINUATION_OBJECT,
                CONTINUATION_SUMMARY,
                CONTINUATION_METADATA,
                ("local_relevance_medium_read_only_continuation_version", "continuation_version"),
            ),
            "failed_check_count": _failed_count(
                artifact,
                CONTINUATION_SUMMARY,
                "local_relevance_medium_read_only_continuation_checks",
            ),
            "passed_check_count": _passed_count(
                artifact,
                CONTINUATION_SUMMARY,
                "local_relevance_medium_read_only_continuation_checks",
            ),
            "clean": clean,
            "read_error": error,
        }
    )
    return basis


def _declared_non_claims_ok(request: Mapping[str, Any]) -> bool:
    declared = request.get("declared_non_claims")
    return isinstance(declared, Mapping) and all(
        declared.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
    )


def _required_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _add_check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str,
) -> None:
    if code not in BLOCK_CODES:
        raise LocalRelevanceMediumReadOnlyDerivativeParticipantParticipationMotionBoundaryV0MinError(
            f"Unsupported block code: {code}"
        )
    checks.append(
        {
            "check_name": name,
            "passed": bool(passed),
            "expected_posture": _redact(expected, name),
            "actual_posture": _redact(actual, name),
            "block_code": None if passed else code,
            "failure_code": None if passed else code,
        }
    )


def _failed_checks(checks: Iterable[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if check.get("passed") is False]


def _first_failed_code(checks: Iterable[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            return code if isinstance(code, str) else None
    return None


def _boundary_object(
    request: Mapping[str, Any],
    role_artifact: Mapping[str, Any] | None,
    continuation_artifact: Mapping[str, Any] | None,
    role_basis: Mapping[str, Any],
    continuation_basis: Mapping[str, Any],
    record: bool,
) -> dict[str, Any]:
    command = request.get("selected_command")
    boundary: dict[str, Any] = {
        "boundary_id": request.get(
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id",
            DEFAULT_BOUNDARY_ID,
        ),
        "boundary_type": request.get("boundary_type"),
        "boundary_scope": request.get("boundary_scope"),
        "boundary_version": RESULT_VERSION,
        "basis_role_admission_terminal_summary_path": request.get(
            "selected_role_admission_terminal_summary_path"
        ),
        "basis_role_admission_artifact": request.get("selected_role_admission_artifact"),
        "basis_role_admission_outcome": role_basis.get("outcome"),
        "basis_role_admission_result_version": role_basis.get("result_version"),
        "basis_role_admission_failed_check_count": role_basis.get("failed_check_count"),
        "basis_continuation_terminal_summary_path": request.get(
            "selected_continuation_terminal_summary_path"
        ),
        "basis_continuation_artifact": request.get("selected_continuation_artifact"),
        "basis_continuation_outcome": continuation_basis.get("outcome"),
        "basis_continuation_result_version": continuation_basis.get("result_version"),
        "basis_continuation_failed_check_count": continuation_basis.get("failed_check_count"),
        "selected_command": command,
        "selected_command_is_state": command == SELECTED_COMMAND,
        "selected_command_preserved": command == SELECTED_COMMAND,
    }
    for key in ROLE_TRUE_FIELDS:
        boundary[key] = bool(role_basis.get(key))
    for key in CONTINUATION_TRUE_FIELDS:
        boundary[key] = bool(continuation_basis.get(key))
    boundary["continuation_operation_sequence_count"] = continuation_basis.get(
        "continuation_operation_sequence_count"
    )
    for key in BOUNDARY_TRUE_FIELDS:
        boundary[key] = bool(record)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        boundary[key] = _forbidden_value(role_artifact, continuation_artifact, key)
    for key in EVIDENCE_TRUE_FIELDS:
        boundary[key] = _evidence(role_artifact, continuation_artifact, key)
    boundary["result_level_non_claims_canonical_false"] = True
    return boundary


def _checks_for(
    request: Mapping[str, Any],
    request_error: str | None,
    role_error: str | None,
    continuation_error: str | None,
    role_basis: Mapping[str, Any],
    continuation_basis: Mapping[str, Any],
    boundary: Mapping[str, Any],
    declared_non_claims_ok: bool,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if request_error is not None:
        _add_check(checks, "declared_request_readable_object", False, None, request_error, request_error)

    question = request.get(
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_question"
    )
    intent = request.get(
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent"
    )
    command = request.get("selected_command")
    boundary_type = request.get("boundary_type")
    boundary_scope = request.get("boundary_scope")

    _add_check(
        checks,
        "boundary_question_declared",
        isinstance(question, str) and bool(question.strip()),
        "declared question",
        question,
        "PARTICIPATION_MOTION_BOUNDARY_QUESTION_UNDECLARED",
    )
    _add_check(
        checks,
        "boundary_intent_supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "PARTICIPATION_MOTION_BOUNDARY_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _add_check(
            checks,
            "boundary_block_not_requested",
            False,
            "record or do-not-record intent",
            intent,
            "PARTICIPATION_MOTION_BOUNDARY_BLOCK_REQUESTED",
        )
    _add_check(checks, "selected_command_declared", command is not None, SELECTED_COMMAND, command, "SELECTED_COMMAND_MISSING")
    _add_check(checks, "selected_command_exactly_state", command == SELECTED_COMMAND, SELECTED_COMMAND, command, "SELECTED_COMMAND_NOT_STATE")
    _add_check(checks, "boundary_type_declared", boundary_type is not None, BOUNDARY_TYPE, boundary_type, "BOUNDARY_TYPE_MISSING")
    _add_check(
        checks,
        "boundary_type_exact",
        boundary_type == BOUNDARY_TYPE,
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY",
    )
    _add_check(checks, "boundary_scope_declared", boundary_scope is not None, BOUNDARY_SCOPE, boundary_scope, "BOUNDARY_SCOPE_MISSING")
    _add_check(
        checks,
        "boundary_scope_exact",
        boundary_scope == BOUNDARY_SCOPE,
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_NOT_SELECTED_PARTICIPATION_MOTION_CONSIDERATION_ONLY",
    )

    role_summary = _path_text(request.get("selected_role_admission_terminal_summary_path"))
    role_path = _path_text(request.get("selected_role_admission_artifact"))
    cont_summary = _path_text(request.get("selected_continuation_terminal_summary_path"))
    cont_path = _path_text(request.get("selected_continuation_artifact"))
    _add_check(checks, "role_admission_terminal_summary_path_declared", bool(role_summary), "declared path", role_summary, "ROLE_ADMISSION_TERMINAL_SUMMARY_PATH_MISSING")
    _add_check(checks, "role_admission_artifact_path_declared", bool(role_path), "declared path", role_path, "ROLE_ADMISSION_ARTIFACT_PATH_MISSING")
    _add_check(checks, "role_admission_artifact_readable", role_error != "ROLE_ADMISSION_ARTIFACT_UNREADABLE", "readable", role_error, "ROLE_ADMISSION_ARTIFACT_UNREADABLE")
    _add_check(checks, "role_admission_artifact_object_shaped", role_error is None, "JSON object", role_error, "ROLE_ADMISSION_ARTIFACT_NOT_JSON_OBJECT")
    _add_check(checks, "role_admission_artifact_outcome_recorded", role_basis.get("outcome") == ROLE_ADMISSION_OUTCOME, ROLE_ADMISSION_OUTCOME, role_basis.get("outcome"), "ROLE_ADMISSION_ARTIFACT_NOT_RECORDED")
    _add_check(checks, "role_admission_artifact_result_version_0_1_0", role_basis.get("result_version") == RESULT_VERSION, RESULT_VERSION, role_basis.get("result_version"), "ROLE_ADMISSION_ARTIFACT_VERSION_NOT_0_1_0")
    _add_check(checks, "role_admission_artifact_failed_check_count_zero", role_basis.get("failed_check_count") == 0, 0, role_basis.get("failed_check_count"), "ROLE_ADMISSION_ARTIFACT_FAILED_CHECKS_PRESENT")

    for key in ROLE_TRUE_FIELDS:
        _add_check(checks, key, boundary.get(key) is True, True, boundary.get(key), ROLE_FIELD_CODES[key])

    _add_check(checks, "continuation_terminal_summary_path_declared", bool(cont_summary), "declared path", cont_summary, "CONTINUATION_TERMINAL_SUMMARY_PATH_MISSING")
    _add_check(checks, "continuation_artifact_path_declared", bool(cont_path), "declared path", cont_path, "CONTINUATION_ARTIFACT_PATH_MISSING")
    _add_check(checks, "continuation_artifact_readable", continuation_error != "CONTINUATION_ARTIFACT_UNREADABLE", "readable", continuation_error, "CONTINUATION_ARTIFACT_UNREADABLE")
    _add_check(checks, "continuation_artifact_object_shaped", continuation_error is None, "JSON object", continuation_error, "CONTINUATION_ARTIFACT_NOT_JSON_OBJECT")
    _add_check(checks, "continuation_artifact_outcome_recorded", continuation_basis.get("outcome") == CONTINUATION_OUTCOME, CONTINUATION_OUTCOME, continuation_basis.get("outcome"), "CONTINUATION_ARTIFACT_NOT_RECORDED")
    _add_check(checks, "continuation_artifact_result_version_0_1_0", continuation_basis.get("result_version") == RESULT_VERSION, RESULT_VERSION, continuation_basis.get("result_version"), "CONTINUATION_ARTIFACT_VERSION_NOT_0_1_0")
    _add_check(checks, "continuation_artifact_failed_check_count_zero", continuation_basis.get("failed_check_count") == 0, 0, continuation_basis.get("failed_check_count"), "CONTINUATION_ARTIFACT_FAILED_CHECKS_PRESENT")

    for key in CONTINUATION_TRUE_FIELDS:
        _add_check(
            checks,
            key,
            boundary.get(key) is True,
            True,
            boundary.get(key),
            CONTINUATION_FIELD_CODES[key],
        )
    _add_check(
        checks,
        "continuation_operation_sequence_count_is_2",
        boundary.get("continuation_operation_sequence_count") == 2,
        2,
        boundary.get("continuation_operation_sequence_count"),
        "CONTINUATION_OPERATION_SEQUENCE_COUNT_NOT_2",
    )

    if intent == INTENT_RECORD:
        for key in BOUNDARY_TRUE_FIELDS:
            _add_check(checks, key, boundary.get(key) is True, True, boundary.get(key), BOUNDARY_FIELD_CODES[key])

    for key in REQUIRED_FALSE_NON_CLAIMS:
        _add_check(checks, key, boundary.get(key) is False, False, boundary.get(key), key.upper())
    for key in EVIDENCE_TRUE_FIELDS:
        _add_check(checks, key, boundary.get(key) is True, True, boundary.get(key), EVIDENCE_FIELD_CODES[key])
    _add_check(
        checks,
        "declared_required_non_claims_false",
        declared_non_claims_ok,
        "all required declared non-claims false",
        "canonical false" if declared_non_claims_ok else "missing or flipped",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _add_check(
        checks,
        "result_level_required_false_non_claims_canonical_false",
        boundary.get("result_level_non_claims_canonical_false") is True,
        True,
        boundary.get("result_level_non_claims_canonical_false"),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return checks


def build_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    boundary = _mapping(
        result.get(
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary"
        )
    )
    checks = result.get(
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_checks",
        [],
    )
    checks_list = checks if isinstance(checks, list) else []
    block = _mapping(result.get("block"))
    return _redact(
        {
            "outcome": result.get("outcome"),
            "block_code": block.get("block_code") or block.get("code"),
            "boundary_id": boundary.get("boundary_id"),
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "selected_command": boundary.get("selected_command"),
            "passed_check_count": len(
                [check for check in checks_list if isinstance(check, Mapping) and check.get("passed") is True]
            ),
            "failed_check_count": len(
                [check for check in checks_list if isinstance(check, Mapping) and check.get("passed") is False]
            ),
            "participation_motion_boundary_recorded": boundary.get(
                "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_recorded"
            ),
            "future_participation_motion_may_be_considered": boundary.get(
                "future_participation_motion_may_be_considered"
            ),
            "role_admission_not_treated_as_participation_permission": boundary.get(
                "role_admission_treated_as_participation_permission"
            )
            is False,
            "preserved_ancestor_derivative_surfaces_not_imported_as_authority": all(
                boundary.get(key) is False
                for key in (
                    "received_derivative_participation_authority_imported",
                    "received_derivative_action_authority_imported",
                    "bounded_derivative_vessel_authority_imported",
                    "derivative_vessel_relation_authority_imported",
                )
            ),
            "raw_state_body_not_embedded": boundary.get("raw_state_body_embedded") is False,
            "state_mutation_not_performed": boundary.get("state_mutation_performed") is False,
            "state_update_not_performed": boundary.get("state_update_performed") is False,
            "result_level_non_claims_canonical_false": boundary.get(
                "result_level_non_claims_canonical_false"
            ),
        }
    )


def resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min(
    declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary: Mapping[
        str, Any
    ]
    | None = None,
) -> dict[str, Any]:
    if declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary is None:
        request: Mapping[str, Any] = (
            build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_request()
        )
        request_error = None
    elif not isinstance(
        declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary,
        Mapping,
    ):
        request = {}
        request_error = "DECLARED_PARTICIPATION_MOTION_BOUNDARY_REQUEST_MALFORMED"
    else:
        request = declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary
        code = request.get("_request_error_code")
        request_error = code if isinstance(code, str) and code in BLOCK_CODES else None

    role_artifact, role_error = _read_json_object(
        request.get("selected_role_admission_artifact"),
        "ROLE_ADMISSION_ARTIFACT_PATH_MISSING",
        "ROLE_ADMISSION_ARTIFACT_UNREADABLE",
        "ROLE_ADMISSION_ARTIFACT_NOT_JSON_OBJECT",
    )
    continuation_artifact, continuation_error = _read_json_object(
        request.get("selected_continuation_artifact"),
        "CONTINUATION_ARTIFACT_PATH_MISSING",
        "CONTINUATION_ARTIFACT_UNREADABLE",
        "CONTINUATION_ARTIFACT_NOT_JSON_OBJECT",
    )
    role_basis = _role_basis(role_artifact, role_error)
    continuation_basis = _continuation_basis(continuation_artifact, continuation_error)
    declared_non_claims_ok = _declared_non_claims_ok(request)
    forbidden_clear = all(
        _forbidden_value(role_artifact, continuation_artifact, key) is False
        for key in REQUIRED_FALSE_NON_CLAIMS
    )
    evidence_clear = all(
        _evidence(role_artifact, continuation_artifact, key) is True
        for key in EVIDENCE_TRUE_FIELDS
    )
    basis_ready = (
        request_error is None
        and request.get(
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent"
        )
        == INTENT_RECORD
        and request.get("selected_command") == SELECTED_COMMAND
        and request.get("boundary_type") == BOUNDARY_TYPE
        and request.get("boundary_scope") == BOUNDARY_SCOPE
        and role_basis.get("clean") is True
        and continuation_basis.get("clean") is True
        and declared_non_claims_ok
        and forbidden_clear
        and evidence_clear
    )
    boundary = _boundary_object(
        request,
        role_artifact,
        continuation_artifact,
        role_basis,
        continuation_basis,
        bool(basis_ready),
    )
    checks = _checks_for(
        request,
        request_error,
        role_error,
        continuation_error,
        role_basis,
        continuation_basis,
        boundary,
        declared_non_claims_ok,
    )
    failed = _failed_checks(checks)
    first_code = _first_failed_code(checks)
    intent = request.get(
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent"
    )
    if intent == INTENT_BLOCK:
        outcome = OUTCOME_BLOCKED
        code = "PARTICIPATION_MOTION_BOUNDARY_BLOCK_REQUESTED"
    elif intent not in SUPPORTED_INTENTS:
        outcome = OUTCOME_BLOCKED
        code = "PARTICIPATION_MOTION_BOUNDARY_INTENT_UNSUPPORTED"
    elif request_error is not None:
        outcome = OUTCOME_BLOCKED
        code = request_error
    elif intent == INTENT_DO_NOT_RECORD and not failed:
        outcome = OUTCOME_NOT_RECORDED
        code = None
    elif failed:
        code = first_code
        outcome = (
            OUTCOME_REQUIRES_ADDITIONAL_BASIS
            if code in ADDITIONAL_BASIS_CODES
            else OUTCOME_BLOCKED
        )
    else:
        outcome = OUTCOME_RECORDED
        code = None

    result: dict[str, Any] = {
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_metadata": {
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id": boundary.get(
                "boundary_id"
            ),
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_type": BOUNDARY_TYPE,
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "intent": intent,
        },
        "declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_question": request.get(
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_question"
        ),
        "selected_role_admission_terminal_summary_basis": {
            "selected_role_admission_terminal_summary_path": request.get(
                "selected_role_admission_terminal_summary_path"
            ),
            "selected_role_admission_terminal_summary_path_declared": bool(
                _path_text(request.get("selected_role_admission_terminal_summary_path"))
            ),
        },
        "selected_role_admission_artifact_basis": {
            "selected_role_admission_artifact": request.get("selected_role_admission_artifact"),
            "selected_role_admission_artifact_read_error": role_error,
            **role_basis,
        },
        "selected_continuation_terminal_summary_basis": {
            "selected_continuation_terminal_summary_path": request.get(
                "selected_continuation_terminal_summary_path"
            ),
            "selected_continuation_terminal_summary_path_declared": bool(
                _path_text(request.get("selected_continuation_terminal_summary_path"))
            ),
        },
        "selected_continuation_artifact_basis": {
            "selected_continuation_artifact": request.get("selected_continuation_artifact"),
            "selected_continuation_artifact_read_error": continuation_error,
            **continuation_basis,
        },
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary": boundary,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_checks": checks,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_statement": copy.deepcopy(
            boundary
        ),
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_non_meaning": {
            "this_is_participation_motion_boundary_only": True,
            "this_is_not_participation_motion": True,
            "this_is_not_participant_output_authorization": True,
            "this_is_not_action_authorization": True,
            "this_is_not_participant_reentry": True,
            "this_is_not_derivative_reception": True,
            "this_is_not_vessel_relation": True,
            "this_is_not_runtime": True,
            "this_is_not_source": True,
            "this_is_not_authority": True,
            "this_is_not_currentness": True,
            "this_is_not_truth": True,
            "role_admission_requires_separate_participation_motion_to_participate": True,
            "preserved_ancestor_derivative_surfaces_not_imported_as_authority": True,
        },
        "additional_basis_required": [code]
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS and code
        else [],
        "not_recorded_basis": [INTENT_DO_NOT_RECORD] if outcome == OUTCOME_NOT_RECORDED else [],
        "what_remains_open": [
            "participation_motion",
            "participant_output_authorization",
            "action_authorization",
            "participant_reentry",
            "derivative_reception",
            "vessel_relation",
            "runtime_hosting",
            "runtime_loop",
            "daemon_behavior",
            "public_api",
            "participant_facing_interface",
            "distributed_network_behavior",
            "source",
            "authority",
            "currentness",
            "truth",
            "synchronization",
            "deployment",
            "public_release",
            "broader_reusable_permission",
            "adoption",
            "receiving_context_governance",
            "publication_flow",
            "follow_on_work",
        ],
        "non_claims": _required_false_non_claims(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code if outcome == OUTCOME_BLOCKED else None,
            "block_code": code if outcome == OUTCOME_BLOCKED else None,
            "reason": code if outcome == OUTCOME_BLOCKED else None,
        },
    }
    result[
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_summary"
    ] = build_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_summary(
        result
    )
    return _redact(result)


def resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_from_path(
    path: Path | str,
) -> dict[str, Any]:
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        request = (
            build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_request()
        )
        request["_request_error_code"] = (
            "DECLARED_PARTICIPATION_MOTION_BOUNDARY_REQUEST_UNREADABLE"
        )
        return resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min(
            request
        )
    if not isinstance(loaded, Mapping):
        request = (
            build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_request()
        )
        request["_request_error_code"] = (
            "DECLARED_PARTICIPATION_MOTION_BOUNDARY_REQUEST_MALFORMED"
        )
        return resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min(
            request
        )
    return resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min(
        loaded
    )


def _safe_filename(value: Any) -> str:
    text = str(value or DEFAULT_BOUNDARY_ID)
    safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in text)
    return safe.strip("._-") or DEFAULT_BOUNDARY_ID


def _dedupe_path(path: Path) -> Path:
    if not path.exists():
        return path
    index = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def write_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    boundary = _mapping(
        result.get(
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary"
        )
    )
    if output_path is None:
        path = OUTPUT_ROOT / (
            f"{_safe_filename(boundary.get('boundary_id', DEFAULT_BOUNDARY_ID))}__"
            "local_relevance_medium_read_only_derivative_participant_"
            "participation_motion_boundary_v0_min_result.json"
        )
    else:
        path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _dedupe_path(path)
    final_path.write_text(
        json.dumps(_redact(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_request(
    local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id: str = DEFAULT_BOUNDARY_ID,
    local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_question: str = BOUNDARY_QUESTION,
    local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent: str = INTENT_RECORD,
    selected_role_admission_terminal_summary_path: Path
    | str = DEFAULT_ROLE_ADMISSION_TERMINAL_SUMMARY,
    selected_role_admission_artifact: Path | str = DEFAULT_ROLE_ADMISSION_ARTIFACT,
    selected_continuation_terminal_summary_path: Path
    | str = DEFAULT_CONTINUATION_TERMINAL_SUMMARY,
    selected_continuation_artifact: Path | str = DEFAULT_CONTINUATION_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    declared_non_claims: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    non_claims = _required_false_non_claims()
    if declared_non_claims is not None:
        non_claims.update(copy.deepcopy(dict(declared_non_claims)))
    return {
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id": local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_question": local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_question,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent": local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent,
        "selected_role_admission_terminal_summary_path": str(
            selected_role_admission_terminal_summary_path
        ),
        "selected_role_admission_artifact": str(selected_role_admission_artifact),
        "selected_continuation_terminal_summary_path": str(
            selected_continuation_terminal_summary_path
        ),
        "selected_continuation_artifact": str(selected_continuation_artifact),
        "selected_command": selected_command,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "declared_non_claims": non_claims,
    }
