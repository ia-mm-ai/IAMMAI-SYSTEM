"""v3 resolver for the local read-only derivative participant boundary.

This successor preserves the v2 public surface while rebuilding emitted
boundary posture from canonical values. Incoming illegal true posture can block
the result and appear in check evidence, but it is never echoed into the final
boundary object, statement, or result-level non-claims.
"""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3"
)
BOUNDARY_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY"
)
BOUNDARY_SCOPE = "SELECTED_PARTICIPATION_MOTION_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3"
)
DEFAULT_BOUNDARY_ID = (
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_001"
)
DEFAULT_ROLE_ADMISSION_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2/"
    "local_relevance_medium_read_only_derivative_participant_role_admission_001__"
    "local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_result.json"
)
DEFAULT_CONTINUATION_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_continuation_v0_min/"
    "local_relevance_medium_read_only_continuation_reference_review_001__"
    "local_relevance_medium_read_only_continuation_v0_min_result.json"
)

SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)

ROLE_ADMISSION_OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_RECORDED"
)
CONTINUATION_OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_RECORDED"

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

ROLE_POSITIVE_FIELDS = (
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
CONTINUATION_POSITIVE_FIELDS = (
    "selected_continuation_recorded",
    "continuation_created",
    "continuation_local_only",
    "continuation_read_only",
    "continuation_basis_reference_only",
    "continuation_selected_state_only",
    "continuation_from_second_operation",
    "continuation_sequence_count_is_2",
)
BOUNDARY_POSITIVE_FIELDS = (
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_recorded",
    "future_participation_motion_may_be_considered",
    "participation_motion_boundary_created",
    "participation_motion_boundary_local_only",
    "participation_motion_boundary_read_only",
    "participation_motion_boundary_selected_state_only",
    "participation_motion_boundary_basis_reference_only",
)
EVIDENCE_FIELDS = (
    "continuation_v1_failure_evidence_preserved",
    "role_admission_v1_failure_evidence_preserved",
    "predecessor_failure_evidence_preserved",
)
ALLOWED_TRUE_RECORDED_FIELDS = (
    "selected_command_is_state",
    "selected_command_preserved",
    "result_level_non_claims_canonical_false",
    "local_relevance_medium_read_only_continuation_recorded",
    "role_admission_recorded",
    *ROLE_POSITIVE_FIELDS,
    *CONTINUATION_POSITIVE_FIELDS,
    *BOUNDARY_POSITIVE_FIELDS,
    *EVIDENCE_FIELDS,
)

FALSE_FIELD_BLOCK_CODES = {key: key.upper() for key in REQUIRED_FALSE_NON_CLAIMS}
_BASE_BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "REQUEST_PATH_MISSING",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "REQUEST_JSON_NOT_MAPPING",
    "EXPLICIT_BLOCK_INTENT",
    "UNSUPPORTED_INTENT",
    "SELECTED_COMMAND_NOT_STATE",
    "BOUNDARY_TYPE_UNSUPPORTED",
    "BOUNDARY_SCOPE_UNSUPPORTED",
    "DECLARED_NON_CLAIMS_NOT_MAPPING",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "ROLE_ARTIFACT_PATH_MISSING",
    "ROLE_ARTIFACT_UNREADABLE",
    "ROLE_ARTIFACT_JSON_INVALID",
    "ROLE_ARTIFACT_NOT_MAPPING",
    "ROLE_OUTCOME_NOT_RECORDED",
    "ROLE_RESULT_VERSION_UNSUPPORTED",
    "ROLE_FAILED_CHECKS_PRESENT",
    "ROLE_ADMISSION_BASIS_MISSING_OR_FALSE",
    "CONTINUATION_ARTIFACT_PATH_MISSING",
    "CONTINUATION_ARTIFACT_UNREADABLE",
    "CONTINUATION_ARTIFACT_JSON_INVALID",
    "CONTINUATION_ARTIFACT_NOT_MAPPING",
    "CONTINUATION_OUTCOME_NOT_RECORDED",
    "CONTINUATION_RESULT_VERSION_UNSUPPORTED",
    "CONTINUATION_FAILED_CHECKS_PRESENT",
    "CONTINUATION_BASIS_MISSING_OR_FALSE",
    "EVIDENCE_NOT_PRESERVED",
    "BOUNDARY_VALIDATION_FAILED",
)
BLOCK_CODES = tuple(dict.fromkeys((*_BASE_BLOCK_CODES, *FALSE_FIELD_BLOCK_CODES.values())))

_RECORD_INTENT = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY"
)
_BLOCK_INTENT = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY"
)
_MISSING = object()


class LocalRelevanceMediumReadOnlyDerivativeParticipantParticipationMotionBoundaryV0MinV3Error(
    Exception
):
    """Bounded resolver error for invalid direct write or path operations."""


def build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3_request(
    selected_role_admission_artifact: Path | str | None = None,
    selected_continuation_artifact: Path | str | None = None,
    selected_command: str = SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    declared_non_claims: Mapping[str, Any] | None = None,
    local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id: str = DEFAULT_BOUNDARY_ID,
    intent: str = _RECORD_INTENT,
) -> dict[str, Any]:
    """Build the bounded request mapping consumed by the v3 resolver."""

    non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))
    return {
        "request_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent": intent,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id": local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id,
        "selected_role_admission_artifact": _path_to_request_value(
            selected_role_admission_artifact, DEFAULT_ROLE_ADMISSION_ARTIFACT
        ),
        "selected_continuation_artifact": _path_to_request_value(
            selected_continuation_artifact, DEFAULT_CONTINUATION_ARTIFACT
        ),
        "selected_command": selected_command,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "declared_non_claims": non_claims,
    }


def resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3_from_path(
    declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_path: Path
    | str,
) -> dict[str, Any]:
    """Resolve a declared request JSON file without leaking raw file material."""

    checks: list[dict[str, Any]] = []
    if declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_path in (
        None,
        "",
    ):
        _add_check(
            checks,
            "request_path_present",
            False,
            "REQUEST_PATH_MISSING",
            expected="path",
            actual=_MISSING,
        )
        return _result_from_parts({}, None, None, checks)

    path = _resolve_path(
        declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_path
    )
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except FileNotFoundError:
        _add_check(
            checks,
            "request_path_readable",
            False,
            "REQUEST_PATH_UNREADABLE",
            expected="readable_json_mapping",
            actual="missing",
        )
        return _result_from_parts({}, None, None, checks)
    except json.JSONDecodeError:
        _add_check(
            checks,
            "request_json_valid",
            False,
            "REQUEST_JSON_INVALID",
            expected="json_mapping",
            actual="invalid_json",
        )
        return _result_from_parts({}, None, None, checks)
    except OSError:
        _add_check(
            checks,
            "request_path_readable",
            False,
            "REQUEST_PATH_UNREADABLE",
            expected="readable_json_mapping",
            actual="unreadable",
        )
        return _result_from_parts({}, None, None, checks)

    if not isinstance(loaded, Mapping):
        _add_check(
            checks,
            "request_json_mapping",
            False,
            "REQUEST_JSON_NOT_MAPPING",
            expected="mapping",
            actual=loaded,
        )
        return _result_from_parts({}, None, None, checks)
    _add_check(checks, "request_json_mapping", True, expected="mapping", actual="mapping")
    return resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3(
        loaded,
        _pre_checks=checks,
    )


def resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3(
    declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary: Mapping[
        str, Any
    ]
    | None = None,
    *,
    _pre_checks: Sequence[Mapping[str, Any]] = (),
) -> dict[str, Any]:
    """Resolve the selected participation-motion boundary from declared basis."""

    checks = [dict(check) for check in _pre_checks]
    if declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary is None:
        request: dict[str, Any] = (
            build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3_request()
        )
        _add_check(checks, "request_mapping", True, expected="mapping", actual="mapping")
    elif isinstance(
        declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary,
        Mapping,
    ):
        request = dict(
            declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary
        )
        _add_check(checks, "request_mapping", True, expected="mapping", actual="mapping")
    else:
        request = {}
        _add_check(
            checks,
            "request_mapping",
            False,
            "REQUEST_NOT_MAPPING",
            expected="mapping",
            actual=declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary,
        )

    intent = request.get(
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent"
    )
    if intent == _BLOCK_INTENT:
        _add_check(
            checks,
            "request_intent_not_block",
            False,
            "EXPLICIT_BLOCK_INTENT",
            expected=_RECORD_INTENT,
            actual=intent,
        )
    elif intent not in (None, "", _RECORD_INTENT):
        _add_check(
            checks,
            "request_intent_supported",
            False,
            "UNSUPPORTED_INTENT",
            expected=_RECORD_INTENT,
            actual=intent,
        )
    else:
        _add_check(checks, "request_intent_supported", True, expected=_RECORD_INTENT, actual=intent)

    selected_command = request.get("selected_command")
    command_ok = selected_command == SELECTED_COMMAND
    _add_check(
        checks,
        "selected_command_is_state",
        command_ok,
        None if command_ok else "SELECTED_COMMAND_NOT_STATE",
        expected=SELECTED_COMMAND,
        actual=selected_command,
    )

    boundary_type = request.get("boundary_type")
    type_ok = boundary_type == BOUNDARY_TYPE
    _add_check(
        checks,
        "boundary_type_supported",
        type_ok,
        None if type_ok else "BOUNDARY_TYPE_UNSUPPORTED",
        expected=BOUNDARY_TYPE,
        actual=boundary_type,
    )

    boundary_scope = request.get("boundary_scope")
    scope_ok = boundary_scope == BOUNDARY_SCOPE
    _add_check(
        checks,
        "boundary_scope_supported",
        scope_ok,
        None if scope_ok else "BOUNDARY_SCOPE_UNSUPPORTED",
        expected=BOUNDARY_SCOPE,
        actual=boundary_scope,
    )

    declared_non_claims = request.get("declared_non_claims")
    declared_non_claims_ok = isinstance(declared_non_claims, Mapping)
    _add_check(
        checks,
        "declared_non_claims_mapping",
        declared_non_claims_ok,
        None if declared_non_claims_ok else "DECLARED_NON_CLAIMS_NOT_MAPPING",
        expected="mapping",
        actual="mapping" if declared_non_claims_ok else declared_non_claims,
    )
    if not declared_non_claims_ok:
        declared_non_claims = {}

    role_artifact, role_path = _load_artifact(
        request.get("selected_role_admission_artifact"), "role", checks
    )
    continuation_artifact, continuation_path = _load_artifact(
        request.get("selected_continuation_artifact"), "continuation", checks
    )

    role_sections = _role_sections(role_artifact)
    continuation_sections = _continuation_sections(continuation_artifact)

    _validate_artifact_header(
        checks,
        role_sections,
        ROLE_ADMISSION_OUTCOME_RECORDED,
        "role",
        "ROLE_OUTCOME_NOT_RECORDED",
        "ROLE_RESULT_VERSION_UNSUPPORTED",
        "ROLE_FAILED_CHECKS_PRESENT",
    )
    _validate_artifact_header(
        checks,
        continuation_sections,
        CONTINUATION_OUTCOME_RECORDED,
        "continuation",
        "CONTINUATION_OUTCOME_NOT_RECORDED",
        "CONTINUATION_RESULT_VERSION_UNSUPPORTED",
        "CONTINUATION_FAILED_CHECKS_PRESENT",
    )

    role_positive = _validate_role_basis(checks, role_sections)
    continuation_positive = _validate_continuation_basis(checks, continuation_sections)
    evidence_positive = _validate_evidence_basis(checks, role_sections, continuation_sections)

    request_sections = [request]
    if isinstance(declared_non_claims, Mapping):
        request_sections.append(declared_non_claims)
    _validate_false_posture(
        checks,
        declared_non_claims if isinstance(declared_non_claims, Mapping) else {},
        request_sections,
        role_sections,
        continuation_sections,
    )

    failed_checks = [check for check in checks if check.get("passed") is False]
    outcome = OUTCOME_RECORDED if not failed_checks else OUTCOME_BLOCKED
    clean_recorded = outcome == OUTCOME_RECORDED
    boundary = _build_boundary(
        request,
        role_artifact,
        continuation_artifact,
        role_path,
        continuation_path,
        selected_command=selected_command,
        role_positive=role_positive,
        continuation_positive=continuation_positive,
        evidence_positive=evidence_positive,
        clean_recorded=clean_recorded,
    )
    statement = _build_statement(boundary)
    return _result_from_parts(request, boundary, statement, checks, outcome=outcome)


def write_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a stable JSON result without overwriting an existing artifact."""

    if not isinstance(result, Mapping):
        raise LocalRelevanceMediumReadOnlyDerivativeParticipantParticipationMotionBoundaryV0MinV3Error(
            "result must be a mapping"
        )
    boundary = result.get(
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary"
    )
    if not isinstance(boundary, Mapping):
        raise LocalRelevanceMediumReadOnlyDerivativeParticipantParticipationMotionBoundaryV0MinV3Error(
            "result does not contain a boundary mapping"
        )
    boundary_id = str(boundary.get("boundary_id") or DEFAULT_BOUNDARY_ID)
    filename = (
        f"{boundary_id}__"
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3_result.json"
    )

    if output_path is None:
        target = OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
        if path.suffix:
            target = path
        else:
            target = path / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _dedupe_path(target)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(dict(result), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def build_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the compact public summary for a v3 result mapping."""

    if not isinstance(result, Mapping):
        raise LocalRelevanceMediumReadOnlyDerivativeParticipantParticipationMotionBoundaryV0MinV3Error(
            "result must be a mapping"
        )
    checks = result.get(
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_checks",
        (),
    )
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes)):
        checks = ()
    failed = sum(
        1
        for check in checks
        if isinstance(check, Mapping) and check.get("passed") is False
    )
    passed = sum(
        1
        for check in checks
        if isinstance(check, Mapping) and check.get("passed") is True
    )
    boundary = result.get(
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary"
    )
    if not isinstance(boundary, Mapping):
        boundary = {}
    summary = {
        "result_version": result.get("result_version", RESULT_VERSION),
        "resolver_module": result.get("resolver_module", RESOLVER_MODULE),
        "outcome": result.get("outcome", OUTCOME_BLOCKED),
        "failed_check_count": failed,
        "passed_check_count": passed,
        "boundary_id": boundary.get("boundary_id", DEFAULT_BOUNDARY_ID),
        "boundary_type": boundary.get("boundary_type", BOUNDARY_TYPE),
        "boundary_scope": boundary.get("boundary_scope", BOUNDARY_SCOPE),
    }
    for key in (
        *BOUNDARY_POSITIVE_FIELDS,
        *ROLE_POSITIVE_FIELDS,
        *CONTINUATION_POSITIVE_FIELDS,
        *EVIDENCE_FIELDS,
        "result_level_non_claims_canonical_false",
    ):
        summary[key] = bool(boundary.get(key) is True)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        summary[key] = False
    return summary


def _result_from_parts(
    request: Mapping[str, Any],
    boundary: Mapping[str, Any] | None,
    statement: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    *,
    outcome: str | None = None,
) -> dict[str, Any]:
    safe_checks = [dict(check) for check in checks]
    failed = [check for check in safe_checks if check.get("passed") is False]
    final_outcome = outcome or (OUTCOME_BLOCKED if failed else OUTCOME_RECORDED)
    final_boundary = dict(boundary) if isinstance(boundary, Mapping) else _build_boundary({}, None, None, None, None)
    final_statement = dict(statement) if isinstance(statement, Mapping) else _build_statement(final_boundary)
    canonical_non_claims = _canonical_false_non_claims()
    for key in REQUIRED_FALSE_NON_CLAIMS:
        final_boundary[key] = False
        final_statement[key] = False
        canonical_non_claims[key] = False

    block_code = failed[0].get("block_code") if failed else None
    block = {
        "blocked": bool(failed),
        "code": block_code,
        "block_code": block_code,
        "reason": failed[0].get("check_name") if failed else None,
    }
    summary = build_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v3_summary(
        {
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "outcome": final_outcome,
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary": final_boundary,
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_checks": safe_checks,
        }
    )
    additional_basis_required = [
        check["check_name"]
        for check in failed
        if str(check.get("block_code", "")).endswith("MISSING_OR_FALSE")
        or str(check.get("block_code", "")).endswith("UNSUPPORTED")
        or str(check.get("block_code", "")).endswith("UNREADABLE")
    ]
    not_recorded_basis = [
        check["check_name"]
        for check in failed
        if "OUTCOME" in str(check.get("block_code", ""))
        or "FAILED_CHECKS" in str(check.get("block_code", ""))
    ]

    return {
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_metadata": {
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_scope": BOUNDARY_SCOPE,
            "selected_command": SELECTED_COMMAND,
            "predecessor_v1_preserved_as_evidence_only": True,
            "predecessor_v2_preserved_as_evidence_only": True,
        },
        "declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_question": _safe_declared_question(
            request
        ),
        "selected_role_admission_terminal_summary_basis": _terminal_basis(
            final_boundary, "role_admission"
        ),
        "selected_role_admission_artifact_basis": _artifact_basis(
            final_boundary, "role_admission"
        ),
        "selected_continuation_terminal_summary_basis": _terminal_basis(
            final_boundary, "continuation"
        ),
        "selected_continuation_artifact_basis": _artifact_basis(
            final_boundary, "continuation"
        ),
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary": final_boundary,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_checks": safe_checks,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_statement": final_statement,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": [
            "future_participation_motion_requires_a_separate_authorized_request",
            "participant_output_requires_a_separate_authorized_boundary",
            "action_authorization_requires_a_separate_authorized_boundary",
        ],
        "non_claims": canonical_non_claims,
        "outcome": final_outcome,
        "block": block,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_summary": summary,
    }


def _build_boundary(
    request: Mapping[str, Any],
    role_artifact: Mapping[str, Any] | None,
    continuation_artifact: Mapping[str, Any] | None,
    role_path: Path | None,
    continuation_path: Path | None,
    *,
    selected_command: Any = None,
    role_positive: Mapping[str, bool] | None = None,
    continuation_positive: Mapping[str, bool] | None = None,
    evidence_positive: Mapping[str, bool] | None = None,
    clean_recorded: bool = False,
) -> dict[str, Any]:
    role_positive = dict(role_positive or {})
    continuation_positive = dict(continuation_positive or {})
    evidence_positive = dict(evidence_positive or {})
    boundary_id = str(
        request.get(
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id",
            DEFAULT_BOUNDARY_ID,
        )
        or DEFAULT_BOUNDARY_ID
    )
    boundary = {
        "boundary_id": boundary_id,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "selected_command": selected_command if selected_command == SELECTED_COMMAND else SELECTED_COMMAND,
        "selected_command_is_state": selected_command == SELECTED_COMMAND,
        "selected_command_preserved": selected_command == SELECTED_COMMAND,
        "basis_role_admission_artifact": _display_path(role_path),
        "basis_role_admission_outcome": _first_value(
            _role_sections(role_artifact), "outcome", ROLE_ADMISSION_OUTCOME_RECORDED
        ),
        "basis_role_admission_result_version": _first_value(
            _role_sections(role_artifact), "result_version", RESULT_VERSION
        ),
        "basis_role_admission_failed_check_count": _first_value(
            _role_sections(role_artifact), "failed_check_count", 0
        ),
        "basis_continuation_artifact": _display_path(continuation_path),
        "basis_continuation_outcome": _first_value(
            _continuation_sections(continuation_artifact),
            "outcome",
            CONTINUATION_OUTCOME_RECORDED,
        ),
        "basis_continuation_result_version": _first_value(
            _continuation_sections(continuation_artifact), "result_version", RESULT_VERSION
        ),
        "basis_continuation_failed_check_count": _first_value(
            _continuation_sections(continuation_artifact), "failed_check_count", 0
        ),
        "result_level_non_claims_canonical_false": True,
    }
    for key in ROLE_POSITIVE_FIELDS:
        boundary[key] = bool(role_positive.get(key))
    for key in CONTINUATION_POSITIVE_FIELDS:
        boundary[key] = bool(continuation_positive.get(key))
    for key in BOUNDARY_POSITIVE_FIELDS:
        boundary[key] = clean_recorded
    for key in EVIDENCE_FIELDS:
        boundary[key] = bool(evidence_positive.get(key))
    for key in REQUIRED_FALSE_NON_CLAIMS:
        boundary[key] = False
    return boundary


def _build_statement(boundary: Mapping[str, Any]) -> dict[str, Any]:
    statement = {
        "statement_version": RESULT_VERSION,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_scope": BOUNDARY_SCOPE,
        "selected_command": SELECTED_COMMAND,
        "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_recorded": bool(
            boundary.get(
                "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_recorded"
            )
            is True
        ),
        "future_participation_motion_may_be_considered": bool(
            boundary.get("future_participation_motion_may_be_considered") is True
        ),
        "result_level_non_claims_canonical_false": True,
        "predecessor_v1_preserved_as_evidence_only": True,
        "predecessor_v2_preserved_as_evidence_only": True,
    }
    for key in (*ROLE_POSITIVE_FIELDS, *CONTINUATION_POSITIVE_FIELDS, *EVIDENCE_FIELDS):
        statement[key] = bool(boundary.get(key) is True)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        statement[key] = False
    return statement


def _validate_artifact_header(
    checks: list[dict[str, Any]],
    sections: Sequence[Mapping[str, Any]],
    expected_outcome: str,
    prefix: str,
    outcome_code: str,
    version_code: str,
    failed_checks_code: str,
) -> None:
    outcome = _first_value(sections, "outcome", _MISSING)
    outcome_ok = outcome == expected_outcome
    _add_check(
        checks,
        f"{prefix}_outcome_recorded",
        outcome_ok,
        None if outcome_ok else outcome_code,
        expected=expected_outcome,
        actual=outcome,
    )
    version = _first_value(sections, "result_version", _MISSING)
    version_ok = version == RESULT_VERSION
    _add_check(
        checks,
        f"{prefix}_result_version_supported",
        version_ok,
        None if version_ok else version_code,
        expected=RESULT_VERSION,
        actual=version,
    )
    failed_count = _first_value(sections, "failed_check_count", _MISSING)
    failed_count_ok = failed_count == 0
    _add_check(
        checks,
        f"{prefix}_failed_check_count_zero",
        failed_count_ok,
        None if failed_count_ok else failed_checks_code,
        expected=0,
        actual=failed_count,
    )


def _validate_role_basis(
    checks: list[dict[str, Any]], sections: Sequence[Mapping[str, Any]]
) -> dict[str, bool]:
    fields: dict[str, tuple[str, ...]] = {
        "local_relevance_medium_read_only_derivative_participant_role_admission_recorded": (
            "local_relevance_medium_read_only_derivative_participant_role_admission_recorded",
            "role_admission_recorded",
        ),
        "derivative_participant_role_admission_created": (
            "derivative_participant_role_admission_created",
        ),
        "bounded_derivative_participant_role_admitted": (
            "bounded_derivative_participant_role_admitted",
        ),
        "role_admission_local_only": ("role_admission_local_only",),
        "role_admission_read_only": ("role_admission_read_only",),
        "role_admission_selected_state_only": ("role_admission_selected_state_only",),
        "role_admission_basis_reference_only": ("role_admission_basis_reference_only",),
        "role_admission_inside_continuation_body": (
            "role_admission_inside_continuation_body",
        ),
        "role_admission_from_continuation_only": ("role_admission_from_continuation_only",),
    }
    return _validate_positive_fields(
        checks, sections, fields, "role", "ROLE_ADMISSION_BASIS_MISSING_OR_FALSE"
    )


def _validate_continuation_basis(
    checks: list[dict[str, Any]], sections: Sequence[Mapping[str, Any]]
) -> dict[str, bool]:
    fields: dict[str, tuple[str, ...]] = {
        "selected_continuation_recorded": (
            "selected_continuation_recorded",
            "local_relevance_medium_read_only_continuation_recorded",
        ),
        "continuation_created": ("continuation_created",),
        "continuation_local_only": ("continuation_local_only",),
        "continuation_read_only": ("continuation_read_only",),
        "continuation_basis_reference_only": ("continuation_basis_reference_only",),
        "continuation_selected_state_only": ("continuation_selected_state_only",),
        "continuation_from_second_operation": ("continuation_from_second_operation",),
    }
    positives = _validate_positive_fields(
        checks, sections, fields, "continuation", "CONTINUATION_BASIS_MISSING_OR_FALSE"
    )
    sequence_ok, actual = _continuation_sequence_count_is_2(sections)
    positives["continuation_sequence_count_is_2"] = sequence_ok
    _add_check(
        checks,
        "continuation_sequence_count_is_2",
        sequence_ok,
        None if sequence_ok else "CONTINUATION_BASIS_MISSING_OR_FALSE",
        expected=True,
        actual=actual,
    )
    return positives


def _validate_evidence_basis(
    checks: list[dict[str, Any]],
    role_sections: Sequence[Mapping[str, Any]],
    continuation_sections: Sequence[Mapping[str, Any]],
) -> dict[str, bool]:
    sections = [*role_sections, *continuation_sections]
    fields = {key: (key,) for key in EVIDENCE_FIELDS}
    return _validate_positive_fields(checks, sections, fields, "evidence", "EVIDENCE_NOT_PRESERVED")


def _validate_positive_fields(
    checks: list[dict[str, Any]],
    sections: Sequence[Mapping[str, Any]],
    fields: Mapping[str, Sequence[str]],
    prefix: str,
    code: str,
) -> dict[str, bool]:
    positives: dict[str, bool] = {}
    for canonical_key, aliases in fields.items():
        ok, actual_key, actual = _first_explicit_bool(sections, aliases)
        positives[canonical_key] = ok
        _add_check(
            checks,
            f"{prefix}_{canonical_key}",
            ok,
            None if ok else code,
            expected=True,
            actual=actual,
            source=actual_key,
        )
    return positives


def _validate_false_posture(
    checks: list[dict[str, Any]],
    declared_non_claims: Mapping[str, Any],
    request_sections: Sequence[Mapping[str, Any]],
    role_sections: Sequence[Mapping[str, Any]],
    continuation_sections: Sequence[Mapping[str, Any]],
) -> None:
    incoming_sections = [*request_sections, *role_sections, *continuation_sections]
    for key in REQUIRED_FALSE_NON_CLAIMS:
        declared_value = declared_non_claims.get(key, _MISSING)
        declared_ok = declared_value is False
        _add_check(
            checks,
            f"declared_non_claim_{key}_is_false",
            declared_ok,
            None if declared_ok else "NON_CLAIM_MISSING_OR_FLIPPED",
            expected=False,
            actual=declared_value,
            source="declared_non_claims",
        )

        found_true, source = _contains_exact_true(incoming_sections, key)
        _add_check(
            checks,
            f"forbidden_posture_{key}_not_true",
            not found_true,
            None if not found_true else FALSE_FIELD_BLOCK_CODES[key],
            expected=False,
            actual=True if found_true else False,
            source=source,
        )


def _load_artifact(
    value: Any, label: str, checks: list[dict[str, Any]]
) -> tuple[dict[str, Any] | None, Path | None]:
    path = _path_from_value(value)
    code_prefix = "ROLE" if label == "role" else "CONTINUATION"
    if path is None:
        _add_check(
            checks,
            f"{label}_artifact_path_present",
            False,
            f"{code_prefix}_ARTIFACT_PATH_MISSING",
            expected="path",
            actual=value,
        )
        return None, None
    _add_check(checks, f"{label}_artifact_path_present", True, expected="path", actual="path")
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except FileNotFoundError:
        _add_check(
            checks,
            f"{label}_artifact_readable",
            False,
            f"{code_prefix}_ARTIFACT_UNREADABLE",
            expected="readable_json_mapping",
            actual="missing",
        )
        return None, path
    except json.JSONDecodeError:
        _add_check(
            checks,
            f"{label}_artifact_json_valid",
            False,
            f"{code_prefix}_ARTIFACT_JSON_INVALID",
            expected="json_mapping",
            actual="invalid_json",
        )
        return None, path
    except OSError:
        _add_check(
            checks,
            f"{label}_artifact_readable",
            False,
            f"{code_prefix}_ARTIFACT_UNREADABLE",
            expected="readable_json_mapping",
            actual="unreadable",
        )
        return None, path
    if not isinstance(loaded, Mapping):
        _add_check(
            checks,
            f"{label}_artifact_mapping",
            False,
            f"{code_prefix}_ARTIFACT_NOT_MAPPING",
            expected="mapping",
            actual=loaded,
        )
        return None, path
    _add_check(checks, f"{label}_artifact_mapping", True, expected="mapping", actual="mapping")
    return dict(loaded), path


def _role_sections(artifact: Mapping[str, Any] | None) -> list[Mapping[str, Any]]:
    return _sections(
        artifact,
        (
            "local_relevance_medium_read_only_derivative_participant_role_admission",
            "local_relevance_medium_read_only_derivative_participant_role_admission_statement",
            "local_relevance_medium_read_only_derivative_participant_role_admission_summary",
            "local_relevance_medium_read_only_derivative_participant_role_admission_non_meaning",
            "non_claims",
        ),
    )


def _continuation_sections(artifact: Mapping[str, Any] | None) -> list[Mapping[str, Any]]:
    return _sections(
        artifact,
        (
            "local_relevance_medium_read_only_continuation",
            "local_relevance_medium_read_only_continuation_statement",
            "local_relevance_medium_read_only_continuation_summary",
            "local_relevance_medium_read_only_continuation_non_meaning",
            "non_claims",
        ),
    )


def _sections(
    artifact: Mapping[str, Any] | None, section_names: Sequence[str]
) -> list[Mapping[str, Any]]:
    if not isinstance(artifact, Mapping):
        return []
    sections: list[Mapping[str, Any]] = [artifact]
    for name in section_names:
        value = artifact.get(name)
        if isinstance(value, Mapping):
            sections.append(value)
    return sections


def _first_value(
    sections: Sequence[Mapping[str, Any]], key: str, default: Any = _MISSING
) -> Any:
    for section in sections:
        if key in section:
            return section[key]
    return default


def _first_explicit_bool(
    sections: Sequence[Mapping[str, Any]], keys: Sequence[str]
) -> tuple[bool, str | None, Any]:
    for section in sections:
        for key in keys:
            if key in section:
                value = section[key]
                if value is True:
                    return True, key, True
                return False, key, value
    return False, keys[0] if keys else None, _MISSING


def _continuation_sequence_count_is_2(
    sections: Sequence[Mapping[str, Any]]
) -> tuple[bool, Any]:
    for section in sections:
        if "continuation_sequence_count_is_2" in section:
            value = section["continuation_sequence_count_is_2"]
            if value is True:
                return True, True
            return False, value
        if "continuation_operation_sequence_count" in section:
            value = section["continuation_operation_sequence_count"]
            return value == 2, value
    return False, _MISSING


def _contains_exact_true(
    sections: Sequence[Mapping[str, Any]], key: str
) -> tuple[bool, str | None]:
    for index, section in enumerate(sections):
        if section.get(key) is True:
            return True, f"section_{index}.{key}"
    return False, None


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    code: str | None = None,
    *,
    expected: Any = _MISSING,
    actual: Any = _MISSING,
    source: str | None = None,
) -> None:
    public_code = code
    if public_code is not None and public_code not in BLOCK_CODES:
        public_code = "BOUNDARY_VALIDATION_FAILED"
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
    }
    if expected is not _MISSING:
        record["expected"] = _safe_actual(expected)
    if actual is not _MISSING:
        record["actual"] = _safe_actual(actual)
    if source:
        record["source"] = source
    if not passed:
        record["block_code"] = public_code or "BOUNDARY_VALIDATION_FAILED"
        record["failure_code"] = public_code or "BOUNDARY_VALIDATION_FAILED"
    checks.append(record)


def _safe_actual(value: Any) -> Any:
    if value is _MISSING:
        return "<missing>"
    if value is None or isinstance(value, bool):
        return value
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, str):
        allowed_strings = {
            RESULT_VERSION,
            RESOLVER_MODULE,
            BOUNDARY_TYPE,
            BOUNDARY_SCOPE,
            SELECTED_COMMAND,
            OUTCOME_RECORDED,
            OUTCOME_NOT_RECORDED,
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            OUTCOME_BLOCKED,
            ROLE_ADMISSION_OUTCOME_RECORDED,
            CONTINUATION_OUTCOME_RECORDED,
            _RECORD_INTENT,
            _BLOCK_INTENT,
            "mapping",
            "path",
            "missing",
            "invalid_json",
            "unreadable",
        }
        if value in allowed_strings:
            return value
        return f"<str:{len(value)}>"
    if isinstance(value, float):
        return value
    if isinstance(value, Mapping):
        return "<mapping>"
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return "<sequence>"
    return f"<{type(value).__name__}>"


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _safe_declared_question(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "boundary_type": BOUNDARY_TYPE,
        "boundary_scope": BOUNDARY_SCOPE,
        "selected_command": SELECTED_COMMAND,
        "selected_role_admission_artifact": _safe_actual(
            request.get("selected_role_admission_artifact", DEFAULT_ROLE_ADMISSION_ARTIFACT)
        ),
        "selected_continuation_artifact": _safe_actual(
            request.get("selected_continuation_artifact", DEFAULT_CONTINUATION_ARTIFACT)
        ),
        "declared_non_claims_canonicalized_in_result": True,
    }


def _terminal_basis(boundary: Mapping[str, Any], label: str) -> dict[str, Any]:
    if label == "role_admission":
        return {
            "outcome": boundary.get("basis_role_admission_outcome"),
            "result_version": boundary.get("basis_role_admission_result_version"),
            "failed_check_count": boundary.get("basis_role_admission_failed_check_count"),
            "role_admission_v1_failure_evidence_preserved": boundary.get(
                "role_admission_v1_failure_evidence_preserved"
            )
            is True,
        }
    return {
        "outcome": boundary.get("basis_continuation_outcome"),
        "result_version": boundary.get("basis_continuation_result_version"),
        "failed_check_count": boundary.get("basis_continuation_failed_check_count"),
        "continuation_v1_failure_evidence_preserved": boundary.get(
            "continuation_v1_failure_evidence_preserved"
        )
        is True,
    }


def _artifact_basis(boundary: Mapping[str, Any], label: str) -> dict[str, Any]:
    if label == "role_admission":
        return {
            "artifact": boundary.get("basis_role_admission_artifact"),
            "basis_reference_only": boundary.get("role_admission_basis_reference_only") is True,
            "local_only": boundary.get("role_admission_local_only") is True,
            "read_only": boundary.get("role_admission_read_only") is True,
        }
    return {
        "artifact": boundary.get("basis_continuation_artifact"),
        "basis_reference_only": boundary.get("continuation_basis_reference_only") is True,
        "local_only": boundary.get("continuation_local_only") is True,
        "read_only": boundary.get("continuation_read_only") is True,
    }


def _non_meaning() -> dict[str, Any]:
    return {
        "does_not_create_participation_motion": True,
        "does_not_authorize_participant_output": True,
        "does_not_authorize_action": True,
        "does_not_create_participant_reentry": True,
        "does_not_authorize_derivative_reception": True,
        "does_not_authorize_vessel_relation": True,
        "does_not_create_runtime_or_public_interface": True,
        "does_not_import_received_or_vessel_authority": True,
        "does_not_repair_hide_or_claim_passed_predecessor_failure": True,
    }


def _path_to_request_value(value: Path | str | None, default: str) -> str:
    if value is None:
        return default
    return str(value)


def _path_from_value(value: Any) -> Path | None:
    if value in (None, ""):
        return None
    if not isinstance(value, (str, Path)):
        return None
    path = Path(value)
    if not str(path):
        return None
    return _resolve_path(path)


def _resolve_path(value: Path | str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _display_path(path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _dedupe_path(path: Path) -> Path:
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
