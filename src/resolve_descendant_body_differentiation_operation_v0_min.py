"""Resolve one descendant-body differentiation operation result.

This resolver records one DESCENDANT_BODY_DIFFERENTIATION_OPERATION result
object only. When all declared basis requirements pass, it emits exactly two
result-contained non-standing descendant-body-basis candidate records with
operation evidence.

It does not create descendant bodies, standing descendants, crossing,
relation, FIELD machinery, runtime, API, currentness, authority, output,
action, derivative reception, synchronization, repair, repository scan,
validation enforcement, or follow-on work. It preserves the contaminated
lineage file as contaminated lineage and preserves the completed evidence-check
and operation-boundary lines as bounded basis only.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class DescendantBodyDifferentiationOperationV0MinError(RuntimeError):
    """Bounded resolver error for request/path/write handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_differentiation_operation_v0_min"

OUTCOME_RECORDED = "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED"
OUTCOME_BLOCKED = "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BLOCKED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_NOT_RECORDED,
)

OPERATION_TYPE = "DESCENDANT_BODY_DIFFERENTIATION_OPERATION"
OPERATION_SCOPE = "ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY"
CANDIDATE_RECORD_POLICY = "EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS"
FAILURE_VISIBILITY_POLICY = "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL"
DIFFERENTIATION_METHOD = "DECLARED_BASIS_DUAL_CANDIDATE_DIFFERENTIATION"

CANDIDATE_RECORD_TYPE = "NON_STANDING_DESCENDANT_BODY_BASIS_CANDIDATE"
CANDIDATE_A_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_B_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_B_ROLE = "CANDIDATE_B"

SUPPORTED_OPERATION_TYPE_VALUES = (OPERATION_TYPE,)
SUPPORTED_OPERATION_SCOPE_VALUES = (OPERATION_SCOPE,)
SUPPORTED_CANDIDATE_RECORD_POLICY_VALUES = (CANDIDATE_RECORD_POLICY,)
SUPPORTED_FAILURE_VISIBILITY_POLICY_VALUES = (FAILURE_VISIBILITY_POLICY,)
SUPPORTED_DIFFERENTIATION_METHOD_VALUES = (DIFFERENTIATION_METHOD,)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_differentiation_"
    "operation_v0_min"
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_DIFFERENTIATION_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_DIFFERENTIATION_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_DIFFERENTIATION_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_OPERATION_ID = "descendant_body_differentiation_operation_001"
DEFAULT_SOURCE_BODY_PROOF_BASIS_REFERENCE = (
    "declared-standing-body-proof-basis-before-contaminated-derivation-event"
)
DEFAULT_CONTAMINATED_LINEAGE_REFERENCE = (
    "spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md"
)
DEFAULT_EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EVIDENCE_CHECK_ARTIFACT_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_existence_claim_evidence_check_"
    "v0_min/existence_claim_evidence_check_001__existence_claim_evidence_check_"
    "v0_min_result.json"
)
DEFAULT_DIFFERENTIATION_OPERATION_BOUNDARY_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_differentiation_"
    "operation_boundary_v0_min/descendant_body_differentiation_operation_boundary_"
    "001__descendant_body_differentiation_operation_boundary_v0_min_result.json"
)
DEFAULT_OPERATION_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_V0_MIN_SPEC.md"
)
DEFAULT_QUESTION = (
    "Given one declared standing body-proof basis reference, one preserved "
    "contaminated descendant derivation event file, one completed "
    "existence-claim evidence check line, and one completed descendant-body "
    "differentiation operation boundary line, may one descendant-body "
    "differentiation operation result be recorded that either emits exactly "
    "two non-standing descendant-body-basis candidate records with operation "
    "evidence, or blocks visibly without creating candidate records, while "
    "preserving that the operation does not create standing descendants, "
    "authorize crossing, create relation, create FIELD machinery, create "
    "runtime, create currentness, create authority, authorize output, "
    "authorize action, authorize derivative reception, authorize "
    "synchronization, repair the affected file, validate prior unsupported "
    "claims, or authorize follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_basis_candidate_a_created",
    "descendant_body_basis_candidate_b_created",
    "standing_descendant_created",
    "descendant_standing_check_performed",
    "first_crossing_authorized",
    "relation_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "currentness_created",
    "authority_created",
    "standing_created",
    "output_authorized_result",
    "action_authorized_result",
    "derivative_reception_authorized_result",
    "synchronization_authorized_result",
    "follow_on_work_authorized",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "valid_derivation_event_recorded",
    "affected_file_repaired",
    "affected_file_edited",
    "affected_file_deleted",
    "affected_file_overwritten",
    "affected_file_replaced",
    "affected_file_redeemed",
    "affected_file_treated_as_clean_basis",
    "contaminated_lineage_treated_as_clean_basis",
    "evidence_check_overridden",
    "evidence_check_bypassed",
    "boundary_overridden",
    "boundary_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "repo_presence_treated_as_standing",
    "codex_execution_treated_as_truth",
    "operator_authorization_treated_as_sole_authorship",
    "derivative_rendering_treated_as_standing_evidence",
    "later_recognition_treated_as_upstream_validity",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "descendant_body_differentiation_operation_recorded",
    "operation_result_created",
    "operation_recorded",
    "differentiation_performed",
    "candidate_records_created",
    "exactly_two_candidate_records_emitted",
    "candidate_records_have_operation_evidence",
    "candidate_records_non_standing",
    "candidate_records_do_not_inherit_from_contaminated_lineage",
    "source_body_proof_basis_reference_declared",
    "contaminated_lineage_reference_declared",
    "evidence_requirement_boundary_reference_declared",
    "evidence_check_terminal_summary_reference_declared",
    "evidence_check_artifact_reference_declared",
    "differentiation_operation_boundary_reference_declared",
    "differentiation_operation_boundary_artifact_reference_declared",
    "operation_spec_reference_declared",
    "operation_spec_markers_present",
    "contaminated_lineage_markers_present",
    "evidence_check_terminal_summary_markers_present",
    "evidence_check_artifact_markers_present",
    "differentiation_operation_boundary_terminal_summary_markers_present",
    "differentiation_operation_boundary_artifact_markers_present",
    "prior_unsupported_claims_preserved",
    "contaminated_lineage_preserved",
    "evidence_check_not_overridden",
    "evidence_check_not_bypassed",
    "boundary_not_overridden",
    "boundary_not_bypassed",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_QUESTION_UNDECLARED",
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_INTENT_UNSUPPORTED",
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BLOCK_REQUESTED",
    "OPERATION_TYPE_MISSING",
    "OPERATION_TYPE_NOT_DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
    "OPERATION_VERSION_MISSING",
    "OPERATION_VERSION_NOT_0_1_0",
    "OPERATION_SCOPE_MISSING",
    "OPERATION_SCOPE_NOT_ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
    "SOURCE_BODY_PROOF_BASIS_REFERENCE_MISSING",
    "CONTAMINATED_LINEAGE_REFERENCE_MISSING",
    "EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE_MISSING",
    "EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EVIDENCE_CHECK_ARTIFACT_REFERENCE_MISSING",
    "DIFFERENTIATION_OPERATION_BOUNDARY_REFERENCE_MISSING",
    "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
    "OPERATION_SPEC_REFERENCE_MISSING",
    "CANDIDATE_RECORD_COUNT_NOT_TWO",
    "CANDIDATE_RECORD_POLICY_MISSING",
    "CANDIDATE_RECORD_POLICY_NOT_EVIDENCE_GATED",
    "FAILURE_VISIBILITY_POLICY_MISSING",
    "FAILURE_VISIBILITY_POLICY_NOT_VISIBLE_BLOCK",
    "DIFFERENTIATION_METHOD_MISSING",
    "DIFFERENTIATION_METHOD_NOT_DECLARED_BASIS_DUAL_CANDIDATE_DIFFERENTIATION",
    "SCAN_ALLOWED_TRUE",
    "REPAIR_ALLOWED_TRUE",
    "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
    "STANDING_AUTHORIZED_TRUE",
    "CROSSING_AUTHORIZED_TRUE",
    "RELATION_AUTHORIZED_TRUE",
    "FIELD_MACHINERY_AUTHORIZED_TRUE",
    "RUNTIME_AUTHORIZED_TRUE",
    "CURRENTNESS_AUTHORIZED_TRUE",
    "AUTHORITY_AUTHORIZED_TRUE",
    "OUTPUT_AUTHORIZED_TRUE",
    "ACTION_AUTHORIZED_TRUE",
    "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE",
    "SYNCHRONIZATION_AUTHORIZED_TRUE",
    "FOLLOW_ON_AUTHORIZED_TRUE",
    "REQUESTED_REPOSITORY_SCAN",
    "REQUESTED_FILE_DISCOVERY",
    "REQUESTED_AFFECTED_FILE_REPAIR",
    "REQUESTED_AFFECTED_FILE_MUTATION",
    "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION",
    "REQUESTED_EVIDENCE_CHECK_OVERRIDE",
    "REQUESTED_EVIDENCE_CHECK_BYPASS",
    "REQUESTED_BOUNDARY_OVERRIDE",
    "REQUESTED_BOUNDARY_BYPASS",
    "REQUESTED_DESCENDANT_BODY_CREATION",
    "REQUESTED_STANDING_DESCENDANT_CREATION",
    "REQUESTED_DESCENDANT_STANDING_CHECK",
    "REQUESTED_CROSSING_AUTHORIZATION",
    "REQUESTED_RELATION_CREATION",
    "REQUESTED_FIELD_MACHINERY_CREATION",
    "REQUESTED_RUNTIME_CREATION",
    "REQUESTED_CURRENTNESS_CREATION",
    "REQUESTED_AUTHORITY_CREATION",
    "REQUESTED_OUTPUT_AUTHORIZATION",
    "REQUESTED_ACTION_AUTHORIZATION",
    "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION",
    "REQUESTED_SYNCHRONIZATION_AUTHORIZATION",
    "REQUESTED_FOLLOW_ON_AUTHORIZATION",
    "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
    "OPERATION_SPEC_MARKER_MISSING",
    "CONTAMINATED_LINEAGE_MARKER_MISSING",
    "EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING",
    "DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING",
    "DESCENDANT_BODY_A_CREATED",
    "DESCENDANT_BODY_B_CREATED",
    "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED",
    "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED",
    "STANDING_DESCENDANT_CREATED",
    "DESCENDANT_STANDING_CHECK_PERFORMED",
    "FIRST_CROSSING_AUTHORIZED",
    "RELATION_CREATED",
    "FIELD_MACHINERY_CREATED",
    "RUNTIME_CREATED",
    "API_CREATED",
    "CURRENTNESS_CREATED",
    "AUTHORITY_CREATED",
    "STANDING_CREATED",
    "OUTPUT_AUTHORIZED_RESULT",
    "ACTION_AUTHORIZED_RESULT",
    "DERIVATIVE_RECEPTION_AUTHORIZED_RESULT",
    "SYNCHRONIZATION_AUTHORIZED_RESULT",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED",
    "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED",
    "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED",
    "VALID_DERIVATION_EVENT_RECORDED",
    "AFFECTED_FILE_REPAIRED",
    "AFFECTED_FILE_EDITED",
    "AFFECTED_FILE_DELETED",
    "AFFECTED_FILE_OVERWRITTEN",
    "AFFECTED_FILE_REPLACED",
    "AFFECTED_FILE_REDEEMED",
    "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS",
    "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
    "EVIDENCE_CHECK_OVERRIDDEN",
    "EVIDENCE_CHECK_BYPASSED",
    "BOUNDARY_OVERRIDDEN",
    "BOUNDARY_BYPASSED",
    "SCAN_PERFORMED",
    "REPOSITORY_SCAN_PERFORMED",
    "REPAIR_PERFORMED",
    "VALIDATION_ENFORCED",
    "HIDDEN_REPAIR_PERFORMED",
    "SILENT_OVERWRITE_PERFORMED",
    "REPO_PRESENCE_TREATED_AS_STANDING",
    "CODEX_EXECUTION_TREATED_AS_TRUTH",
    "OPERATOR_AUTHORIZATION_TREATED_AS_SOLE_AUTHORSHIP",
    "DERIVATIVE_RENDERING_TREATED_AS_STANDING_EVIDENCE",
    "LATER_RECOGNITION_TREATED_AS_UPSTREAM_VALIDITY",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUEST_MALFORMED",
    "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUEST_UNREADABLE",
)

FALSE_POSTURE_BLOCK_CODES = {
    "descendant_body_a_created": "DESCENDANT_BODY_A_CREATED",
    "descendant_body_b_created": "DESCENDANT_BODY_B_CREATED",
    "descendant_body_basis_candidate_a_created": (
        "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED"
    ),
    "descendant_body_basis_candidate_b_created": (
        "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED"
    ),
    "standing_descendant_created": "STANDING_DESCENDANT_CREATED",
    "descendant_standing_check_performed": "DESCENDANT_STANDING_CHECK_PERFORMED",
    "first_crossing_authorized": "FIRST_CROSSING_AUTHORIZED",
    "relation_created": "RELATION_CREATED",
    "field_machinery_created": "FIELD_MACHINERY_CREATED",
    "runtime_created": "RUNTIME_CREATED",
    "api_created": "API_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "standing_created": "STANDING_CREATED",
    "output_authorized_result": "OUTPUT_AUTHORIZED_RESULT",
    "action_authorized_result": "ACTION_AUTHORIZED_RESULT",
    "derivative_reception_authorized_result": (
        "DERIVATIVE_RECEPTION_AUTHORIZED_RESULT"
    ),
    "synchronization_authorized_result": "SYNCHRONIZATION_AUTHORIZED_RESULT",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "prior_unsupported_candidate_a_claim_validated": (
        "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED"
    ),
    "prior_unsupported_candidate_b_claim_validated": (
        "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED"
    ),
    "prior_unsupported_derivation_event_claim_validated": (
        "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED"
    ),
    "valid_derivation_event_recorded": "VALID_DERIVATION_EVENT_RECORDED",
    "affected_file_repaired": "AFFECTED_FILE_REPAIRED",
    "affected_file_edited": "AFFECTED_FILE_EDITED",
    "affected_file_deleted": "AFFECTED_FILE_DELETED",
    "affected_file_overwritten": "AFFECTED_FILE_OVERWRITTEN",
    "affected_file_replaced": "AFFECTED_FILE_REPLACED",
    "affected_file_redeemed": "AFFECTED_FILE_REDEEMED",
    "affected_file_treated_as_clean_basis": "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS",
    "contaminated_lineage_treated_as_clean_basis": (
        "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS"
    ),
    "evidence_check_overridden": "EVIDENCE_CHECK_OVERRIDDEN",
    "evidence_check_bypassed": "EVIDENCE_CHECK_BYPASSED",
    "boundary_overridden": "BOUNDARY_OVERRIDDEN",
    "boundary_bypassed": "BOUNDARY_BYPASSED",
    "scan_performed": "SCAN_PERFORMED",
    "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
    "repair_performed": "REPAIR_PERFORMED",
    "validation_enforced": "VALIDATION_ENFORCED",
    "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
    "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
    "repo_presence_treated_as_standing": "REPO_PRESENCE_TREATED_AS_STANDING",
    "codex_execution_treated_as_truth": "CODEX_EXECUTION_TREATED_AS_TRUTH",
    "operator_authorization_treated_as_sole_authorship": (
        "OPERATOR_AUTHORIZATION_TREATED_AS_SOLE_AUTHORSHIP"
    ),
    "derivative_rendering_treated_as_standing_evidence": (
        "DERIVATIVE_RENDERING_TREATED_AS_STANDING_EVIDENCE"
    ),
    "later_recognition_treated_as_upstream_validity": (
        "LATER_RECOGNITION_TREATED_AS_UPSTREAM_VALIDITY"
    ),
}

OPERATION_SPEC_MARKERS = (
    "Descendant Body Differentiation Operation V0 Minimum Specification",
    "This file defines one future descendant-body differentiation operation.",
    "This file does not implement the operation.",
    "This file does not perform the operation.",
    "Candidate records are future result-contained records only.",
    "This spec does not create the candidate records.",
    "candidate_record_id = descendant_body_basis_candidate_a_001",
    "candidate_record_id = descendant_body_basis_candidate_b_001",
    "candidate_record_created_by_operation = true",
    "candidate_record_standing = false",
    "descendant_body_created = false",
    "inherited_from_contaminated_lineage = false",
    "prior_unsupported_claim_validated = false",
    "operation_implemented = false",
    "operation_recorded = false",
    "candidate_records_created = false",
)

CONTAMINATED_LINEAGE_MARKERS = (
    "descendant_body_basis_candidate_a_created = true",
    "descendant_body_basis_candidate_b_created = true",
    "descendant_body_basis_derivation_event_recorded = true",
)

EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKERS = (
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS",
    "descendant_body_basis_candidate_a_created = UNSUPPORTED",
    "descendant_body_basis_candidate_b_created = UNSUPPORTED",
    "descendant_body_basis_derivation_event_recorded = UNSUPPORTED",
    "Contaminated lineage is not clean basis",
)

DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKERS = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_RECORDED",
    "failed_check_count = 0",
    "passed_check_count = 179",
    "future_operation_type = DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
    "future_operation_scope = ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
    (
        "future_candidate_record_policy = "
        "EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS"
    ),
    (
        "future_failure_visibility_policy = "
        "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL"
    ),
    "future_operation_not_created = true",
    "candidate_records_not_created = true",
    "descendant_bodies_not_created = true",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _repo_path(path_value: Any) -> Path:
    path = Path(str(path_value))
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _json_safe(value: Any, key: str | None = None) -> Any:
    if key is not None:
        lowered = key.lower()
        if lowered in {
            "raw_body",
            "full_body",
            "markdown_body",
            "hidden_repo_state",
            "local_cache",
            "current_working_tree",
        } or lowered.endswith("_body"):
            return "[REDACTED_RAW_BODY]"
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, MappingABC):
        return {str(k): _json_safe(v, str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    return str(value)


def _read_text(path_value: Any) -> tuple[bool, str, str | None, str | None]:
    try:
        path = _repo_path(path_value)
        return True, path.read_text(encoding="utf-8"), None, str(path)
    except (OSError, UnicodeDecodeError, TypeError, ValueError) as exc:
        return False, "", f"{type(exc).__name__}: {exc}", None


def _read_json(path_value: Any) -> tuple[bool, Any, str | None, str | None]:
    try:
        path = _repo_path(path_value)
        with path.open("r", encoding="utf-8") as handle:
            return True, json.load(handle), None, str(path)
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        return False, None, f"{type(exc).__name__}: {exc}", None


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    failure_code = None if passed else code
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _json_safe(expected_posture),
            "actual_posture": _json_safe(actual_posture),
            "block_code": failure_code,
            "failure_code": failure_code,
        }
    )


def _failed_codes(checks: Iterable[Mapping[str, Any]]) -> list[str]:
    codes: list[str] = []
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                codes.append(code)
    return codes


def _first_failed_code(checks: Iterable[Mapping[str, Any]]) -> str | None:
    codes = _failed_codes(checks)
    return codes[0] if codes else None


def _truthy_flag(request: Mapping[str, Any], names: Iterable[str]) -> bool:
    return any(request.get(name) is True for name in names)


def _all_markers_present(text: str, markers: Iterable[str]) -> bool:
    return all(marker in text for marker in markers)


def _request_value(request: Mapping[str, Any], primary: str, *aliases: str) -> Any:
    for key in (primary, *aliases):
        if key in request:
            return request.get(key)
    return None


def _reference_declared(request: Mapping[str, Any], key: str) -> bool:
    value = request.get(key)
    return isinstance(value, str) and value.strip() != ""


def _object_sections(artifact: Mapping[str, Any], object_key: str) -> list[Mapping[str, Any]]:
    sections: list[Mapping[str, Any]] = [artifact]
    for key in (
        f"{object_key}_summary",
        object_key,
        f"{object_key}_statement",
    ):
        value = artifact.get(key)
        if isinstance(value, MappingABC):
            sections.append(value)
    return sections


def _lookup_in_sections(
    artifact: Mapping[str, Any], object_key: str, value_key: str
) -> Any:
    for section in _object_sections(artifact, object_key):
        if value_key in section:
            return section.get(value_key)
    return None


def _artifact_claim_outcomes(artifact: Mapping[str, Any]) -> dict[str, str]:
    outcome_sections = (
        artifact.get("existence_claim_evidence_check_per_claim_outcomes"),
        artifact.get("per_claim_outcomes"),
        artifact.get("claim_outcomes"),
    )
    result: dict[str, str] = {}
    for outcomes in outcome_sections:
        if not isinstance(outcomes, list):
            continue
        for item in outcomes:
            if not isinstance(item, MappingABC):
                continue
            claim_key = item.get("claim_key")
            per_claim_outcome = item.get("per_claim_outcome") or item.get("outcome")
            if isinstance(claim_key, str) and isinstance(per_claim_outcome, str):
                result[claim_key] = per_claim_outcome
    return result


def _evidence_artifact_markers_present(artifact: Any) -> bool:
    if not isinstance(artifact, MappingABC):
        return False
    object_key = "existence_claim_evidence_check"
    if artifact.get("outcome") != "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED":
        return False
    expected_values = {
        "file_level_outcome": "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS",
        "failed_check_count": 0,
        "detected_claim_count": 3,
        "unsupported_claim_count": 3,
        "evidence_supported_claim_count": 0,
    }
    for key, expected in expected_values.items():
        if _lookup_in_sections(artifact, object_key, key) != expected:
            return False
    outcomes = _artifact_claim_outcomes(artifact)
    for marker in CONTAMINATED_LINEAGE_MARKERS:
        claim_key = marker.split(" = ", 1)[0]
        if outcomes.get(claim_key) != "UNSUPPORTED":
            return False
    return True


def _boundary_artifact_markers_present(artifact: Any) -> bool:
    if not isinstance(artifact, MappingABC):
        return False
    object_key = "descendant_body_differentiation_operation_boundary"
    expected_values = {
        "outcome": "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_RECORDED",
        "failed_check_count": 0,
        "boundary_type": "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY",
        "future_operation_type": OPERATION_TYPE,
        "future_operation_scope": OPERATION_SCOPE,
        "future_candidate_record_policy": CANDIDATE_RECORD_POLICY,
        "future_failure_visibility_policy": FAILURE_VISIBILITY_POLICY,
        "boundary_created": True,
        "future_operation_not_created": True,
        "candidate_records_not_created": True,
        "descendant_bodies_not_created": True,
        "operation_created": False,
        "operation_performed": False,
        "operation_recorded": False,
        "differentiation_performed": False,
        "candidate_records_created": False,
    }
    for key, expected in expected_values.items():
        actual = artifact.get(key) if key == "outcome" else _lookup_in_sections(
            artifact, object_key, key
        )
        if actual != expected:
            return False
    return True


def _check_declared_non_claims(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> bool:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, MappingABC):
        _add_check(
            checks,
            "declared_non_claims_mapping",
            False,
            "mapping with every required false non-claim set to false",
            type(declared).__name__,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return False

    all_ok = True
    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = declared.get(key)
        passed = isinstance(value, bool) and value is False
        all_ok = all_ok and passed
        _add_check(
            checks,
            f"declared_non_claim_{key}_is_false",
            passed,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    return all_ok


def _check_top_level_false_postures(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    for key, code in FALSE_POSTURE_BLOCK_CODES.items():
        value = request.get(key, False)
        _add_check(
            checks,
            f"top_level_{key}_not_true",
            value is not True,
            "not true",
            value,
            code,
        )


def _validate_reference(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    key: str,
    check_name: str,
    code: str,
) -> bool:
    declared = _reference_declared(request, key)
    _add_check(
        checks,
        check_name,
        declared,
        "declared non-empty string reference",
        request.get(key),
        code,
    )
    return declared


def _validate_requested_flags(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    requested_flags = (
        (
            "requested_repository_scan",
            ("requested_repository_scan", "repository_scan_requested", "perform_repository_scan"),
            "REQUESTED_REPOSITORY_SCAN",
        ),
        (
            "requested_file_discovery",
            ("requested_file_discovery", "file_discovery_requested", "discover_files"),
            "REQUESTED_FILE_DISCOVERY",
        ),
        (
            "requested_affected_file_repair",
            ("requested_affected_file_repair", "affected_file_repair_requested", "repair_affected_file"),
            "REQUESTED_AFFECTED_FILE_REPAIR",
        ),
        (
            "requested_affected_file_mutation",
            ("requested_affected_file_mutation", "affected_file_mutation_requested", "mutate_affected_file"),
            "REQUESTED_AFFECTED_FILE_MUTATION",
        ),
        (
            "requested_prior_unsupported_claim_validation",
            (
                "requested_prior_unsupported_claim_validation",
                "prior_unsupported_claim_validation_requested",
                "validate_prior_unsupported_claims",
            ),
            "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION",
        ),
        (
            "requested_evidence_check_override",
            ("requested_evidence_check_override", "evidence_check_override_requested", "override_evidence_check"),
            "REQUESTED_EVIDENCE_CHECK_OVERRIDE",
        ),
        (
            "requested_evidence_check_bypass",
            ("requested_evidence_check_bypass", "evidence_check_bypass_requested", "bypass_evidence_check"),
            "REQUESTED_EVIDENCE_CHECK_BYPASS",
        ),
        (
            "requested_boundary_override",
            ("requested_boundary_override", "boundary_override_requested", "override_boundary"),
            "REQUESTED_BOUNDARY_OVERRIDE",
        ),
        (
            "requested_boundary_bypass",
            ("requested_boundary_bypass", "boundary_bypass_requested", "bypass_boundary"),
            "REQUESTED_BOUNDARY_BYPASS",
        ),
        (
            "requested_descendant_body_creation",
            ("requested_descendant_body_creation", "descendant_body_creation_requested", "create_descendant_bodies"),
            "REQUESTED_DESCENDANT_BODY_CREATION",
        ),
        (
            "requested_standing_descendant_creation",
            ("requested_standing_descendant_creation", "standing_descendant_creation_requested", "create_standing_descendants"),
            "REQUESTED_STANDING_DESCENDANT_CREATION",
        ),
        (
            "requested_descendant_standing_check",
            ("requested_descendant_standing_check", "descendant_standing_check_requested", "perform_descendant_standing_check"),
            "REQUESTED_DESCENDANT_STANDING_CHECK",
        ),
        (
            "requested_crossing_authorization",
            ("requested_crossing_authorization", "crossing_authorization_requested", "authorize_crossing"),
            "REQUESTED_CROSSING_AUTHORIZATION",
        ),
        (
            "requested_relation_creation",
            ("requested_relation_creation", "relation_creation_requested", "create_relation"),
            "REQUESTED_RELATION_CREATION",
        ),
        (
            "requested_field_machinery_creation",
            ("requested_field_machinery_creation", "field_machinery_creation_requested", "create_field_machinery"),
            "REQUESTED_FIELD_MACHINERY_CREATION",
        ),
        (
            "requested_runtime_creation",
            ("requested_runtime_creation", "runtime_creation_requested", "create_runtime"),
            "REQUESTED_RUNTIME_CREATION",
        ),
        (
            "requested_currentness_creation",
            ("requested_currentness_creation", "currentness_creation_requested", "create_currentness"),
            "REQUESTED_CURRENTNESS_CREATION",
        ),
        (
            "requested_authority_creation",
            ("requested_authority_creation", "authority_creation_requested", "create_authority"),
            "REQUESTED_AUTHORITY_CREATION",
        ),
        (
            "requested_output_authorization",
            ("requested_output_authorization", "output_authorization_requested", "authorize_output"),
            "REQUESTED_OUTPUT_AUTHORIZATION",
        ),
        (
            "requested_action_authorization",
            ("requested_action_authorization", "action_authorization_requested", "authorize_action"),
            "REQUESTED_ACTION_AUTHORIZATION",
        ),
        (
            "requested_derivative_reception_authorization",
            (
                "requested_derivative_reception_authorization",
                "derivative_reception_authorization_requested",
                "authorize_derivative_reception",
            ),
            "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION",
        ),
        (
            "requested_synchronization_authorization",
            ("requested_synchronization_authorization", "synchronization_authorization_requested", "authorize_synchronization"),
            "REQUESTED_SYNCHRONIZATION_AUTHORIZATION",
        ),
        (
            "requested_follow_on_authorization",
            ("requested_follow_on_authorization", "follow_on_authorization_requested", "authorize_follow_on"),
            "REQUESTED_FOLLOW_ON_AUTHORIZATION",
        ),
        (
            "requested_raw_markdown_body_return",
            ("requested_raw_markdown_body_return", "return_raw_markdown_body", "return_raw_body"),
            "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
        ),
    )
    for check_name, names, code in requested_flags:
        requested = _truthy_flag(request, names)
        _add_check(checks, check_name, not requested, "not requested", requested, code)


def _open_items() -> list[str]:
    return [
        "descendant-body differentiation operation test",
        "descendant-body differentiation operation artifact",
        "descendant-body differentiation operation terminal summary",
        "candidate-record standing checks",
        "repair or successor handling of the affected file, if ever separately bounded",
        "prose-shaped existence-claim handling, if ever separately bounded",
        "automated repository scan, if ever separately bounded",
        "contribution/provenance trace handling, if ever separately bounded",
        "first crossing",
        "relation",
        "FIELD machinery",
        "runtime",
        "API",
        "currentness",
        "authority",
        "standing",
        "output authorization",
        "action authorization",
        "derivative reception",
        "synchronization",
        "follow-on work",
    ]


def build_declared_descendant_body_differentiation_operation_v0_min_request(
    descendant_body_differentiation_operation_id: str = DEFAULT_OPERATION_ID,
    descendant_body_differentiation_operation_question: str = DEFAULT_QUESTION,
    descendant_body_differentiation_operation_intent: str = INTENT_RECORD,
    operation_type: str = OPERATION_TYPE,
    operation_version: str = RESULT_VERSION,
    operation_scope: str = OPERATION_SCOPE,
    source_body_proof_basis_reference: str = (
        DEFAULT_SOURCE_BODY_PROOF_BASIS_REFERENCE
    ),
    contaminated_lineage_reference: str = DEFAULT_CONTAMINATED_LINEAGE_REFERENCE,
    evidence_requirement_boundary_reference: str = (
        DEFAULT_EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE
    ),
    evidence_check_terminal_summary_reference: str = (
        DEFAULT_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE
    ),
    evidence_check_artifact_reference: str = DEFAULT_EVIDENCE_CHECK_ARTIFACT_REFERENCE,
    differentiation_operation_boundary_reference: str = (
        DEFAULT_DIFFERENTIATION_OPERATION_BOUNDARY_REFERENCE
    ),
    differentiation_operation_boundary_artifact_reference: str = (
        DEFAULT_DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_REFERENCE
    ),
    operation_spec_reference: str = DEFAULT_OPERATION_SPEC_REFERENCE,
    candidate_record_count_requested: int = 2,
    candidate_record_policy: str = CANDIDATE_RECORD_POLICY,
    failure_visibility_policy: str = FAILURE_VISIBILITY_POLICY,
    differentiation_method: str = DIFFERENTIATION_METHOD,
    scan_allowed: bool = False,
    repair_allowed: bool = False,
    validation_enforcement_allowed: bool = False,
    standing_authorized: bool = False,
    crossing_authorized: bool = False,
    relation_authorized: bool = False,
    field_machinery_authorized: bool = False,
    runtime_authorized: bool = False,
    currentness_authorized: bool = False,
    authority_authorized: bool = False,
    output_authorized: bool = False,
    action_authorized: bool = False,
    derivative_reception_authorized: bool = False,
    synchronization_authorized: bool = False,
    follow_on_authorized: bool = False,
    declared_non_claims: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a bounded default declared operation request."""

    return {
        "descendant_body_differentiation_operation_id": (
            descendant_body_differentiation_operation_id
        ),
        "descendant_body_differentiation_operation_question": (
            descendant_body_differentiation_operation_question
        ),
        "descendant_body_differentiation_operation_intent": (
            descendant_body_differentiation_operation_intent
        ),
        "operation_type": operation_type,
        "operation_version": operation_version,
        "operation_scope": operation_scope,
        "source_body_proof_basis_reference": source_body_proof_basis_reference,
        "contaminated_lineage_reference": contaminated_lineage_reference,
        "evidence_requirement_boundary_reference": (
            evidence_requirement_boundary_reference
        ),
        "evidence_check_terminal_summary_reference": (
            evidence_check_terminal_summary_reference
        ),
        "evidence_check_artifact_reference": evidence_check_artifact_reference,
        "differentiation_operation_boundary_reference": (
            differentiation_operation_boundary_reference
        ),
        "differentiation_operation_boundary_artifact_reference": (
            differentiation_operation_boundary_artifact_reference
        ),
        "operation_spec_reference": operation_spec_reference,
        "candidate_record_count_requested": candidate_record_count_requested,
        "candidate_record_policy": candidate_record_policy,
        "failure_visibility_policy": failure_visibility_policy,
        "differentiation_method": differentiation_method,
        "scan_allowed": scan_allowed,
        "repair_allowed": repair_allowed,
        "validation_enforcement_allowed": validation_enforcement_allowed,
        "standing_authorized": standing_authorized,
        "crossing_authorized": crossing_authorized,
        "relation_authorized": relation_authorized,
        "field_machinery_authorized": field_machinery_authorized,
        "runtime_authorized": runtime_authorized,
        "currentness_authorized": currentness_authorized,
        "authority_authorized": authority_authorized,
        "output_authorized": output_authorized,
        "action_authorized": action_authorized,
        "derivative_reception_authorized": derivative_reception_authorized,
        "synchronization_authorized": synchronization_authorized,
        "follow_on_authorized": follow_on_authorized,
        "declared_non_claims": (
            dict(declared_non_claims)
            if declared_non_claims is not None
            else _canonical_non_claims()
        ),
    }


def _build_candidate_record(
    request: Mapping[str, Any], candidate_id: str, candidate_role: str
) -> dict[str, Any]:
    operation_id = _request_value(
        request, "descendant_body_differentiation_operation_id", "operation_id"
    ) or DEFAULT_OPERATION_ID
    return {
        "candidate_record_id": candidate_id,
        "candidate_record_type": CANDIDATE_RECORD_TYPE,
        "candidate_role": candidate_role,
        "candidate_record_created_by_operation": True,
        "candidate_record_standing": False,
        "descendant_body_created": False,
        "source_body_proof_basis_reference": _json_safe(
            request.get("source_body_proof_basis_reference")
        ),
        "operation_id": _json_safe(operation_id),
        "operation_evidence_reference": _json_safe(operation_id),
        "operation_evidence_kind": "descendant_body_differentiation_operation_result",
        "contaminated_lineage_reference": _json_safe(
            request.get("contaminated_lineage_reference")
        ),
        "inherited_from_contaminated_lineage": False,
        "prior_unsupported_claim_validated": False,
        "crossing_authorized": False,
        "relation_authorized": False,
        "field_machinery_authorized": False,
        "runtime_authorized": False,
        "currentness_authorized": False,
        "authority_authorized": False,
        "standing_created": False,
        "output_authorized": False,
        "action_authorized": False,
        "derivative_reception_authorized": False,
        "synchronization_authorized": False,
        "follow_on_authorized": False,
    }


def _build_candidate_records(
    request: Mapping[str, Any], recorded: bool
) -> list[dict[str, Any]]:
    if not recorded:
        return []
    return [
        _build_candidate_record(request, CANDIDATE_A_ID, CANDIDATE_A_ROLE),
        _build_candidate_record(request, CANDIDATE_B_ID, CANDIDATE_B_ROLE),
    ]


def _build_operation_object(
    request: Mapping[str, Any],
    recorded: bool,
    marker_posture: Mapping[str, bool],
) -> dict[str, Any]:
    candidate_record_ids = [CANDIDATE_A_ID, CANDIDATE_B_ID] if recorded else []
    operation = {
        "operation_id": _json_safe(
            _request_value(
                request,
                "descendant_body_differentiation_operation_id",
                "operation_id",
            )
            or DEFAULT_OPERATION_ID
        ),
        "operation_type": _json_safe(request.get("operation_type")),
        "operation_version": _json_safe(request.get("operation_version")),
        "operation_scope": _json_safe(request.get("operation_scope")),
        "source_body_proof_basis_reference": _json_safe(
            request.get("source_body_proof_basis_reference")
        ),
        "contaminated_lineage_reference": _json_safe(
            request.get("contaminated_lineage_reference")
        ),
        "evidence_requirement_boundary_reference": _json_safe(
            request.get("evidence_requirement_boundary_reference")
        ),
        "evidence_check_terminal_summary_reference": _json_safe(
            request.get("evidence_check_terminal_summary_reference")
        ),
        "evidence_check_artifact_reference": _json_safe(
            request.get("evidence_check_artifact_reference")
        ),
        "differentiation_operation_boundary_reference": _json_safe(
            request.get("differentiation_operation_boundary_reference")
        ),
        "differentiation_operation_boundary_artifact_reference": _json_safe(
            request.get("differentiation_operation_boundary_artifact_reference")
        ),
        "operation_spec_reference": _json_safe(request.get("operation_spec_reference")),
        "candidate_record_count_requested": _json_safe(
            request.get("candidate_record_count_requested")
        ),
        "candidate_record_policy": _json_safe(request.get("candidate_record_policy")),
        "failure_visibility_policy": _json_safe(
            request.get("failure_visibility_policy")
        ),
        "differentiation_method": _json_safe(request.get("differentiation_method")),
        "descendant_body_differentiation_operation_recorded": recorded,
        "operation_result_created": recorded,
        "operation_recorded": recorded,
        "differentiation_performed": recorded,
        "candidate_records_created": recorded,
        "candidate_record_count_emitted": 2 if recorded else 0,
        "candidate_record_ids": candidate_record_ids,
        "exactly_two_candidate_records_emitted": recorded,
        "candidate_records_have_operation_evidence": recorded,
        "candidate_records_non_standing": recorded,
        "candidate_records_do_not_inherit_from_contaminated_lineage": recorded,
        "source_body_proof_basis_reference_declared": _reference_declared(
            request, "source_body_proof_basis_reference"
        ),
        "contaminated_lineage_reference_declared": _reference_declared(
            request, "contaminated_lineage_reference"
        ),
        "evidence_requirement_boundary_reference_declared": _reference_declared(
            request, "evidence_requirement_boundary_reference"
        ),
        "evidence_check_terminal_summary_reference_declared": _reference_declared(
            request, "evidence_check_terminal_summary_reference"
        ),
        "evidence_check_artifact_reference_declared": _reference_declared(
            request, "evidence_check_artifact_reference"
        ),
        "differentiation_operation_boundary_reference_declared": _reference_declared(
            request, "differentiation_operation_boundary_reference"
        ),
        "differentiation_operation_boundary_artifact_reference_declared": (
            _reference_declared(
                request, "differentiation_operation_boundary_artifact_reference"
            )
        ),
        "operation_spec_reference_declared": _reference_declared(
            request, "operation_spec_reference"
        ),
        "scan_allowed": False,
        "repair_allowed": False,
        "validation_enforcement_allowed": False,
        "standing_authorized": False,
        "crossing_authorized": False,
        "relation_authorized": False,
        "field_machinery_authorized": False,
        "runtime_authorized": False,
        "currentness_authorized": False,
        "authority_authorized": False,
        "output_authorized": False,
        "action_authorized": False,
        "derivative_reception_authorized": False,
        "synchronization_authorized": False,
        "follow_on_authorized": False,
        "operation_spec_markers_present": bool(
            marker_posture.get("operation_spec_markers_present")
        ),
        "contaminated_lineage_markers_present": bool(
            marker_posture.get("contaminated_lineage_markers_present")
        ),
        "evidence_check_terminal_summary_markers_present": bool(
            marker_posture.get("evidence_check_terminal_summary_markers_present")
        ),
        "evidence_check_artifact_markers_present": bool(
            marker_posture.get("evidence_check_artifact_markers_present")
        ),
        "differentiation_operation_boundary_terminal_summary_markers_present": bool(
            marker_posture.get(
                "differentiation_operation_boundary_terminal_summary_markers_present"
            )
        ),
        "differentiation_operation_boundary_artifact_markers_present": bool(
            marker_posture.get(
                "differentiation_operation_boundary_artifact_markers_present"
            )
        ),
        "prior_unsupported_claims_preserved": bool(
            marker_posture.get("evidence_check_terminal_summary_markers_present")
            and marker_posture.get("evidence_check_artifact_markers_present")
        ),
        "contaminated_lineage_preserved": bool(
            marker_posture.get("contaminated_lineage_markers_present")
        ),
        "evidence_check_not_overridden": True,
        "evidence_check_not_bypassed": True,
        "boundary_not_overridden": True,
        "boundary_not_bypassed": True,
    }
    operation.update(_canonical_non_claims())
    return operation


def _basis_summary(
    *,
    path_value: Any,
    declared: bool,
    readable: bool,
    resolved_path: str | None,
    read_error: str | None,
    markers_present: bool,
    marker_names: Iterable[str],
) -> dict[str, Any]:
    return {
        "path": _json_safe(path_value) if declared else None,
        "resolved_path": resolved_path,
        "declared": declared,
        "readable": readable,
        "read_error": read_error,
        "markers_present": markers_present,
        "required_marker_names": list(marker_names),
        "raw_markdown_body_returned": False,
    }


def _artifact_basis_summary(
    *,
    path_value: Any,
    declared: bool,
    readable: bool,
    resolved_path: str | None,
    read_error: str | None,
    markers_present: bool,
) -> dict[str, Any]:
    return {
        "path": _json_safe(path_value) if declared else None,
        "resolved_path": resolved_path,
        "declared": declared,
        "readable": readable,
        "read_error": read_error,
        "markers_present": markers_present,
        "raw_artifact_body_returned": False,
    }


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    upstream_basis: Mapping[str, Any],
    operation_basis: Mapping[str, Any],
    marker_posture: Mapping[str, bool],
    outcome: str,
    recorded: bool,
) -> dict[str, Any]:
    operation = _build_operation_object(request, recorded, marker_posture)
    candidate_records = _build_candidate_records(request, recorded)
    failed_checks = [check for check in checks if check.get("passed") is False]
    passed_checks = [check for check in checks if check.get("passed") is True]
    failed_code = _first_failed_code(checks)
    non_claims = _canonical_non_claims()
    statement = {
        "descendant_body_differentiation_operation_recorded": recorded,
        "operation_result_created": recorded,
        "operation_recorded": recorded,
        "differentiation_performed": recorded,
        "candidate_records_created": recorded,
        "exactly_two_candidate_records_emitted": recorded,
        "candidate_records_have_operation_evidence": recorded,
        "candidate_records_non_standing": recorded,
        "candidate_records_do_not_inherit_from_contaminated_lineage": recorded,
        "source_body_proof_basis_reference_declared": operation[
            "source_body_proof_basis_reference_declared"
        ],
        "contaminated_lineage_reference_declared": operation[
            "contaminated_lineage_reference_declared"
        ],
        "evidence_requirement_boundary_reference_declared": operation[
            "evidence_requirement_boundary_reference_declared"
        ],
        "evidence_check_terminal_summary_reference_declared": operation[
            "evidence_check_terminal_summary_reference_declared"
        ],
        "evidence_check_artifact_reference_declared": operation[
            "evidence_check_artifact_reference_declared"
        ],
        "differentiation_operation_boundary_reference_declared": operation[
            "differentiation_operation_boundary_reference_declared"
        ],
        "differentiation_operation_boundary_artifact_reference_declared": operation[
            "differentiation_operation_boundary_artifact_reference_declared"
        ],
        "operation_spec_reference_declared": operation[
            "operation_spec_reference_declared"
        ],
        "operation_spec_markers_present": operation["operation_spec_markers_present"],
        "contaminated_lineage_markers_present": operation[
            "contaminated_lineage_markers_present"
        ],
        "evidence_check_terminal_summary_markers_present": operation[
            "evidence_check_terminal_summary_markers_present"
        ],
        "evidence_check_artifact_markers_present": operation[
            "evidence_check_artifact_markers_present"
        ],
        "differentiation_operation_boundary_terminal_summary_markers_present": operation[
            "differentiation_operation_boundary_terminal_summary_markers_present"
        ],
        "differentiation_operation_boundary_artifact_markers_present": operation[
            "differentiation_operation_boundary_artifact_markers_present"
        ],
        "prior_unsupported_claims_preserved": operation[
            "prior_unsupported_claims_preserved"
        ],
        "contaminated_lineage_preserved": operation["contaminated_lineage_preserved"],
        "evidence_check_not_overridden": True,
        "evidence_check_not_bypassed": True,
        "boundary_not_overridden": True,
        "boundary_not_bypassed": True,
        "result_level_non_claims_canonical_false": all(
            value is False for value in non_claims.values()
        ),
    }
    statement.update(non_claims)
    result: dict[str, Any] = {
        "descendant_body_differentiation_operation_metadata": {
            "descendant_body_differentiation_operation_id": operation["operation_id"],
            "operation_type": OPERATION_TYPE,
            "result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_descendant_body_differentiation_operation_question": {
            "descendant_body_differentiation_operation_id": _json_safe(
                _request_value(
                    request,
                    "descendant_body_differentiation_operation_id",
                    "operation_id",
                )
            ),
            "descendant_body_differentiation_operation_question": _json_safe(
                _request_value(
                    request,
                    "descendant_body_differentiation_operation_question",
                    "operation_question",
                )
            ),
            "descendant_body_differentiation_operation_intent": _json_safe(
                _request_value(
                    request,
                    "descendant_body_differentiation_operation_intent",
                    "operation_intent",
                )
            ),
            "operation_type": _json_safe(request.get("operation_type")),
            "operation_version": _json_safe(request.get("operation_version")),
            "operation_scope": _json_safe(request.get("operation_scope")),
            "source_body_proof_basis_reference": _json_safe(
                request.get("source_body_proof_basis_reference")
            ),
            "contaminated_lineage_reference": _json_safe(
                request.get("contaminated_lineage_reference")
            ),
            "evidence_requirement_boundary_reference": _json_safe(
                request.get("evidence_requirement_boundary_reference")
            ),
            "evidence_check_terminal_summary_reference": _json_safe(
                request.get("evidence_check_terminal_summary_reference")
            ),
            "evidence_check_artifact_reference": _json_safe(
                request.get("evidence_check_artifact_reference")
            ),
            "differentiation_operation_boundary_reference": _json_safe(
                request.get("differentiation_operation_boundary_reference")
            ),
            "differentiation_operation_boundary_artifact_reference": _json_safe(
                request.get("differentiation_operation_boundary_artifact_reference")
            ),
            "operation_spec_reference": _json_safe(
                request.get("operation_spec_reference")
            ),
            "candidate_record_count_requested": _json_safe(
                request.get("candidate_record_count_requested")
            ),
            "candidate_record_policy": _json_safe(
                request.get("candidate_record_policy")
            ),
            "failure_visibility_policy": _json_safe(
                request.get("failure_visibility_policy")
            ),
            "differentiation_method": _json_safe(
                request.get("differentiation_method")
            ),
            "scan_allowed": _json_safe(request.get("scan_allowed")),
            "repair_allowed": _json_safe(request.get("repair_allowed")),
            "validation_enforcement_allowed": _json_safe(
                request.get("validation_enforcement_allowed")
            ),
        },
        "upstream_basis": dict(upstream_basis),
        "operation_basis": dict(operation_basis),
        "descendant_body_differentiation_operation": operation,
        "descendant_body_differentiation_candidate_records": candidate_records,
        "descendant_body_differentiation_operation_checks": checks,
        "descendant_body_differentiation_operation_statement": statement,
        "descendant_body_differentiation_operation_non_meaning": {
            "not_descendant_body_creation": True,
            "not_standing_descendant_creation": True,
            "not_descendant_standing_check": True,
            "not_crossing": True,
            "not_relation": True,
            "not_field_machinery": True,
            "not_runtime": True,
            "not_api": True,
            "not_currentness": True,
            "not_authority": True,
            "not_output_action_derivative_reception_synchronization_or_follow_on": True,
            "not_affected_file_repair": True,
            "not_prior_unsupported_claim_validation": True,
            "not_repository_scan": True,
            "not_clean_basis_import_from_contaminated_lineage": True,
        },
        "additional_basis_required": [
            check["check_name"]
            for check in failed_checks
            if str(check.get("failure_code", "")).endswith("MISSING")
            or str(check.get("failure_code", "")).endswith("UNREADABLE")
            or str(check.get("failure_code", "")).endswith("MALFORMED")
            or str(check.get("failure_code", "")).endswith("MARKER_MISSING")
        ],
        "not_recorded_basis": [
            check["check_name"] for check in failed_checks if check.get("failure_code")
        ],
        "what_remains_open": _open_items(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": failed_code if outcome == OUTCOME_BLOCKED else None,
            "block_code": failed_code if outcome == OUTCOME_BLOCKED else None,
            "reason": failed_code if outcome == OUTCOME_BLOCKED else None,
        },
    }
    result["descendant_body_differentiation_operation_summary"] = (
        build_descendant_body_differentiation_operation_v0_min_summary(result)
    )
    result["descendant_body_differentiation_operation_summary"][
        "passed_check_count"
    ] = len(passed_checks)
    result["descendant_body_differentiation_operation_summary"][
        "failed_check_count"
    ] = len(failed_checks)
    return result


def _validate_exact_value(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    key: str,
    expected: Any,
    missing_code: str,
    mismatch_code: str,
) -> None:
    actual = request.get(key)
    _add_check(
        checks,
        f"{key}_declared",
        key in request and actual not in (None, ""),
        expected,
        actual,
        missing_code,
    )
    _add_check(
        checks,
        f"{key}_exact",
        actual == expected,
        expected,
        actual,
        mismatch_code,
    )


def resolve_descendant_body_differentiation_operation_v0_min(
    declared_descendant_body_differentiation_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declared descendant-body differentiation operation."""

    if declared_descendant_body_differentiation_operation is None:
        request: dict[str, Any] = (
            build_declared_descendant_body_differentiation_operation_v0_min_request()
        )
    elif isinstance(declared_descendant_body_differentiation_operation, MappingABC):
        request = copy.deepcopy(dict(declared_descendant_body_differentiation_operation))
    else:
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_is_mapping",
            False,
            "mapping",
            type(declared_descendant_body_differentiation_operation).__name__,
            "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUEST_MALFORMED",
        )
        return _build_result({}, checks, {}, {}, {}, OUTCOME_BLOCKED, False)

    checks = []

    question = _request_value(
        request,
        "descendant_body_differentiation_operation_question",
        "operation_question",
    )
    _add_check(
        checks,
        "operation_question_declared",
        isinstance(question, str) and question.strip() != "",
        "non-empty operation question",
        question,
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_QUESTION_UNDECLARED",
    )

    intent = _request_value(
        request, "descendant_body_differentiation_operation_intent", "operation_intent"
    )
    _add_check(
        checks,
        "operation_intent_supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_INTENT_UNSUPPORTED",
    )
    _add_check(
        checks,
        "operation_block_not_requested",
        intent != INTENT_BLOCK,
        f"intent is not {INTENT_BLOCK}",
        intent,
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BLOCK_REQUESTED",
    )

    _validate_exact_value(
        request,
        checks,
        "operation_type",
        OPERATION_TYPE,
        "OPERATION_TYPE_MISSING",
        "OPERATION_TYPE_NOT_DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
    )
    _validate_exact_value(
        request,
        checks,
        "operation_version",
        RESULT_VERSION,
        "OPERATION_VERSION_MISSING",
        "OPERATION_VERSION_NOT_0_1_0",
    )
    _validate_exact_value(
        request,
        checks,
        "operation_scope",
        OPERATION_SCOPE,
        "OPERATION_SCOPE_MISSING",
        "OPERATION_SCOPE_NOT_ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
    )

    source_ref_declared = _validate_reference(
        request,
        checks,
        "source_body_proof_basis_reference",
        "source_body_proof_basis_reference_declared",
        "SOURCE_BODY_PROOF_BASIS_REFERENCE_MISSING",
    )
    contaminated_ref_declared = _validate_reference(
        request,
        checks,
        "contaminated_lineage_reference",
        "contaminated_lineage_reference_declared",
        "CONTAMINATED_LINEAGE_REFERENCE_MISSING",
    )
    evidence_requirement_ref_declared = _validate_reference(
        request,
        checks,
        "evidence_requirement_boundary_reference",
        "evidence_requirement_boundary_reference_declared",
        "EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE_MISSING",
    )
    evidence_summary_ref_declared = _validate_reference(
        request,
        checks,
        "evidence_check_terminal_summary_reference",
        "evidence_check_terminal_summary_reference_declared",
        "EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    )
    evidence_artifact_ref_declared = _validate_reference(
        request,
        checks,
        "evidence_check_artifact_reference",
        "evidence_check_artifact_reference_declared",
        "EVIDENCE_CHECK_ARTIFACT_REFERENCE_MISSING",
    )
    boundary_summary_ref_declared = _validate_reference(
        request,
        checks,
        "differentiation_operation_boundary_reference",
        "differentiation_operation_boundary_reference_declared",
        "DIFFERENTIATION_OPERATION_BOUNDARY_REFERENCE_MISSING",
    )
    boundary_artifact_ref_declared = _validate_reference(
        request,
        checks,
        "differentiation_operation_boundary_artifact_reference",
        "differentiation_operation_boundary_artifact_reference_declared",
        "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
    )
    operation_spec_ref_declared = _validate_reference(
        request,
        checks,
        "operation_spec_reference",
        "operation_spec_reference_declared",
        "OPERATION_SPEC_REFERENCE_MISSING",
    )

    candidate_count = request.get("candidate_record_count_requested")
    _add_check(
        checks,
        "candidate_record_count_requested_equals_two",
        candidate_count == 2,
        2,
        candidate_count,
        "CANDIDATE_RECORD_COUNT_NOT_TWO",
    )
    _validate_exact_value(
        request,
        checks,
        "candidate_record_policy",
        CANDIDATE_RECORD_POLICY,
        "CANDIDATE_RECORD_POLICY_MISSING",
        "CANDIDATE_RECORD_POLICY_NOT_EVIDENCE_GATED",
    )
    _validate_exact_value(
        request,
        checks,
        "failure_visibility_policy",
        FAILURE_VISIBILITY_POLICY,
        "FAILURE_VISIBILITY_POLICY_MISSING",
        "FAILURE_VISIBILITY_POLICY_NOT_VISIBLE_BLOCK",
    )
    _validate_exact_value(
        request,
        checks,
        "differentiation_method",
        DIFFERENTIATION_METHOD,
        "DIFFERENTIATION_METHOD_MISSING",
        "DIFFERENTIATION_METHOD_NOT_DECLARED_BASIS_DUAL_CANDIDATE_DIFFERENTIATION",
    )

    for flag_name, code in (
        ("scan_allowed", "SCAN_ALLOWED_TRUE"),
        ("repair_allowed", "REPAIR_ALLOWED_TRUE"),
        ("validation_enforcement_allowed", "VALIDATION_ENFORCEMENT_ALLOWED_TRUE"),
        ("standing_authorized", "STANDING_AUTHORIZED_TRUE"),
        ("crossing_authorized", "CROSSING_AUTHORIZED_TRUE"),
        ("relation_authorized", "RELATION_AUTHORIZED_TRUE"),
        ("field_machinery_authorized", "FIELD_MACHINERY_AUTHORIZED_TRUE"),
        ("runtime_authorized", "RUNTIME_AUTHORIZED_TRUE"),
        ("currentness_authorized", "CURRENTNESS_AUTHORIZED_TRUE"),
        ("authority_authorized", "AUTHORITY_AUTHORIZED_TRUE"),
        ("output_authorized", "OUTPUT_AUTHORIZED_TRUE"),
        ("action_authorized", "ACTION_AUTHORIZED_TRUE"),
        ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE"),
        ("synchronization_authorized", "SYNCHRONIZATION_AUTHORIZED_TRUE"),
        ("follow_on_authorized", "FOLLOW_ON_AUTHORIZED_TRUE"),
    ):
        _add_check(
            checks,
            f"{flag_name}_is_false",
            request.get(flag_name) is False,
            False,
            request.get(flag_name),
            code,
        )

    _validate_requested_flags(request, checks)
    declared_non_claims_ok = _check_declared_non_claims(request, checks)
    _check_top_level_false_postures(request, checks)

    if operation_spec_ref_declared:
        (
            operation_spec_readable,
            operation_spec_text,
            operation_spec_error,
            operation_spec_resolved,
        ) = _read_text(request.get("operation_spec_reference"))
    else:
        operation_spec_readable, operation_spec_text, operation_spec_error = (
            False,
            "",
            "reference missing",
        )
        operation_spec_resolved = None
    operation_spec_markers_present = operation_spec_readable and _all_markers_present(
        operation_spec_text, OPERATION_SPEC_MARKERS
    )
    _add_check(
        checks,
        "operation_spec_markers_present",
        operation_spec_markers_present,
        list(OPERATION_SPEC_MARKERS),
        "present" if operation_spec_markers_present else "missing",
        "OPERATION_SPEC_MARKER_MISSING",
    )

    if contaminated_ref_declared:
        (
            contaminated_readable,
            contaminated_text,
            contaminated_error,
            contaminated_resolved,
        ) = _read_text(request.get("contaminated_lineage_reference"))
    else:
        contaminated_readable, contaminated_text, contaminated_error = (
            False,
            "",
            "reference missing",
        )
        contaminated_resolved = None
    contaminated_markers_present = contaminated_readable and _all_markers_present(
        contaminated_text, CONTAMINATED_LINEAGE_MARKERS
    )
    _add_check(
        checks,
        "contaminated_lineage_markers_present",
        contaminated_markers_present,
        list(CONTAMINATED_LINEAGE_MARKERS),
        "present" if contaminated_markers_present else "missing",
        "CONTAMINATED_LINEAGE_MARKER_MISSING",
    )

    if evidence_summary_ref_declared:
        (
            evidence_summary_readable,
            evidence_summary_text,
            evidence_summary_error,
            evidence_summary_resolved,
        ) = _read_text(request.get("evidence_check_terminal_summary_reference"))
    else:
        evidence_summary_readable, evidence_summary_text, evidence_summary_error = (
            False,
            "",
            "reference missing",
        )
        evidence_summary_resolved = None
    evidence_summary_markers_present = (
        evidence_summary_readable
        and _all_markers_present(
            evidence_summary_text, EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKERS
        )
    )
    _add_check(
        checks,
        "evidence_check_terminal_summary_markers_present",
        evidence_summary_markers_present,
        list(EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKERS),
        "present" if evidence_summary_markers_present else "missing",
        "EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    )

    if evidence_artifact_ref_declared:
        (
            evidence_artifact_readable,
            evidence_artifact_data,
            evidence_artifact_error,
            evidence_artifact_resolved,
        ) = _read_json(request.get("evidence_check_artifact_reference"))
    else:
        evidence_artifact_readable, evidence_artifact_data, evidence_artifact_error = (
            False,
            None,
            "reference missing",
        )
        evidence_artifact_resolved = None
    evidence_artifact_markers_present = (
        evidence_artifact_readable
        and _evidence_artifact_markers_present(evidence_artifact_data)
    )
    _add_check(
        checks,
        "evidence_check_artifact_markers_present",
        evidence_artifact_markers_present,
        "recorded contaminated-class artifact with three unsupported claims",
        "present" if evidence_artifact_markers_present else "missing",
        "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING",
    )

    if boundary_summary_ref_declared:
        (
            boundary_summary_readable,
            boundary_summary_text,
            boundary_summary_error,
            boundary_summary_resolved,
        ) = _read_text(request.get("differentiation_operation_boundary_reference"))
    else:
        boundary_summary_readable, boundary_summary_text, boundary_summary_error = (
            False,
            "",
            "reference missing",
        )
        boundary_summary_resolved = None
    boundary_summary_markers_present = (
        boundary_summary_readable
        and _all_markers_present(
            boundary_summary_text,
            DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKERS,
        )
    )
    _add_check(
        checks,
        "differentiation_operation_boundary_terminal_summary_markers_present",
        boundary_summary_markers_present,
        list(DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKERS),
        "present" if boundary_summary_markers_present else "missing",
        "DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    )

    if boundary_artifact_ref_declared:
        (
            boundary_artifact_readable,
            boundary_artifact_data,
            boundary_artifact_error,
            boundary_artifact_resolved,
        ) = _read_json(
            request.get("differentiation_operation_boundary_artifact_reference")
        )
    else:
        boundary_artifact_readable, boundary_artifact_data, boundary_artifact_error = (
            False,
            None,
            "reference missing",
        )
        boundary_artifact_resolved = None
    boundary_artifact_markers_present = (
        boundary_artifact_readable
        and _boundary_artifact_markers_present(boundary_artifact_data)
    )
    _add_check(
        checks,
        "differentiation_operation_boundary_artifact_markers_present",
        boundary_artifact_markers_present,
        "recorded future-operation-only boundary artifact",
        "present" if boundary_artifact_markers_present else "missing",
        "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING",
    )

    marker_posture = {
        "operation_spec_markers_present": operation_spec_markers_present,
        "contaminated_lineage_markers_present": contaminated_markers_present,
        "evidence_check_terminal_summary_markers_present": (
            evidence_summary_markers_present
        ),
        "evidence_check_artifact_markers_present": (
            evidence_artifact_markers_present
        ),
        "differentiation_operation_boundary_terminal_summary_markers_present": (
            boundary_summary_markers_present
        ),
        "differentiation_operation_boundary_artifact_markers_present": (
            boundary_artifact_markers_present
        ),
    }

    upstream_basis = {
        "source_body_proof_basis_reference": {
            "reference": _json_safe(request.get("source_body_proof_basis_reference")),
            "declared": source_ref_declared,
            "source_body_proof_basis_recreated": False,
        },
        "contaminated_lineage_reference": _basis_summary(
            path_value=request.get("contaminated_lineage_reference"),
            declared=contaminated_ref_declared,
            readable=contaminated_readable,
            resolved_path=contaminated_resolved,
            read_error=contaminated_error,
            markers_present=contaminated_markers_present,
            marker_names=CONTAMINATED_LINEAGE_MARKERS,
        ),
        "evidence_requirement_boundary_reference": {
            "reference": _json_safe(
                request.get("evidence_requirement_boundary_reference")
            ),
            "declared": evidence_requirement_ref_declared,
        },
        "evidence_check_terminal_summary_reference": _basis_summary(
            path_value=request.get("evidence_check_terminal_summary_reference"),
            declared=evidence_summary_ref_declared,
            readable=evidence_summary_readable,
            resolved_path=evidence_summary_resolved,
            read_error=evidence_summary_error,
            markers_present=evidence_summary_markers_present,
            marker_names=EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKERS,
        ),
        "evidence_check_artifact_reference": _artifact_basis_summary(
            path_value=request.get("evidence_check_artifact_reference"),
            declared=evidence_artifact_ref_declared,
            readable=evidence_artifact_readable,
            resolved_path=evidence_artifact_resolved,
            read_error=evidence_artifact_error,
            markers_present=evidence_artifact_markers_present,
        ),
    }

    operation_basis = {
        "operation_spec_reference": _basis_summary(
            path_value=request.get("operation_spec_reference"),
            declared=operation_spec_ref_declared,
            readable=operation_spec_readable,
            resolved_path=operation_spec_resolved,
            read_error=operation_spec_error,
            markers_present=operation_spec_markers_present,
            marker_names=OPERATION_SPEC_MARKERS,
        ),
        "differentiation_operation_boundary_reference": _basis_summary(
            path_value=request.get("differentiation_operation_boundary_reference"),
            declared=boundary_summary_ref_declared,
            readable=boundary_summary_readable,
            resolved_path=boundary_summary_resolved,
            read_error=boundary_summary_error,
            markers_present=boundary_summary_markers_present,
            marker_names=DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKERS,
        ),
        "differentiation_operation_boundary_artifact_reference": (
            _artifact_basis_summary(
                path_value=request.get(
                    "differentiation_operation_boundary_artifact_reference"
                ),
                declared=boundary_artifact_ref_declared,
                readable=boundary_artifact_readable,
                resolved_path=boundary_artifact_resolved,
                read_error=boundary_artifact_error,
                markers_present=boundary_artifact_markers_present,
            )
        ),
        "candidate_record_count_requested": _json_safe(candidate_count),
        "candidate_record_policy": _json_safe(request.get("candidate_record_policy")),
        "failure_visibility_policy": _json_safe(
            request.get("failure_visibility_policy")
        ),
        "differentiation_method": _json_safe(request.get("differentiation_method")),
        "declared_non_claims_ok": declared_non_claims_ok,
        "repository_scan_performed": False,
        "file_discovery_performed": False,
        "raw_markdown_bodies_returned": False,
    }

    first_failure = _first_failed_code(checks)
    if first_failure is not None:
        outcome = OUTCOME_BLOCKED
        recorded = False
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        recorded = False
    else:
        outcome = OUTCOME_RECORDED
        recorded = True

    return _build_result(
        request,
        checks,
        upstream_basis,
        operation_basis,
        marker_posture,
        outcome,
        recorded,
    )


def resolve_descendant_body_differentiation_operation_v0_min_from_path(
    declared_descendant_body_differentiation_operation_path: Path | str,
) -> dict[str, Any]:
    """Resolve from one declared JSON request path."""

    try:
        path = _repo_path(declared_descendant_body_differentiation_operation_path)
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_path_readable",
            False,
            "readable JSON object request",
            f"{type(exc).__name__}: {exc}",
            "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUEST_UNREADABLE",
        )
        return _build_result({}, checks, {}, {}, {}, OUTCOME_BLOCKED, False)

    if not isinstance(payload, MappingABC):
        checks = []
        _add_check(
            checks,
            "declared_request_json_is_mapping",
            False,
            "JSON object",
            type(payload).__name__,
            "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUEST_MALFORMED",
        )
        return _build_result({}, checks, {}, {}, {}, OUTCOME_BLOCKED, False)

    return resolve_descendant_body_differentiation_operation_v0_min(payload)


def build_descendant_body_differentiation_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary without raw Markdown or artifact bodies."""

    operation = result.get("descendant_body_differentiation_operation")
    if not isinstance(operation, MappingABC):
        operation = {}
    checks = result.get("descendant_body_differentiation_operation_checks")
    if not isinstance(checks, list):
        checks = []
    block = result.get("block")
    if not isinstance(block, MappingABC):
        block = {}
    question = result.get("declared_descendant_body_differentiation_operation_question")
    if not isinstance(question, MappingABC):
        question = {}
    non_claims = result.get("non_claims")
    non_claims_canonical = isinstance(non_claims, MappingABC) and all(
        non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
    )
    failed_check_count = sum(1 for check in checks if check.get("passed") is False)
    passed_check_count = sum(1 for check in checks if check.get("passed") is True)

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "operation_id": operation.get("operation_id"),
        "question": question.get("descendant_body_differentiation_operation_question"),
        "intent": question.get("descendant_body_differentiation_operation_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_type": operation.get("operation_type"),
        "operation_version": operation.get("operation_version"),
        "operation_scope": operation.get("operation_scope"),
        "candidate_record_policy": operation.get("candidate_record_policy"),
        "failure_visibility_policy": operation.get("failure_visibility_policy"),
        "differentiation_method": operation.get("differentiation_method"),
        "operation_recorded": operation.get("operation_recorded", False),
        "operation_result_created": operation.get("operation_result_created", False),
        "differentiation_performed": operation.get("differentiation_performed", False),
        "candidate_records_created": operation.get("candidate_records_created", False),
        "candidate_record_count_emitted": operation.get(
            "candidate_record_count_emitted", 0
        ),
        "candidate_record_ids": list(operation.get("candidate_record_ids") or []),
        "exactly_two_candidate_records_emitted": operation.get(
            "exactly_two_candidate_records_emitted", False
        ),
        "candidate_records_have_operation_evidence": operation.get(
            "candidate_records_have_operation_evidence", False
        ),
        "candidate_records_non_standing": operation.get(
            "candidate_records_non_standing", False
        ),
        "candidate_records_do_not_inherit_from_contaminated_lineage": operation.get(
            "candidate_records_do_not_inherit_from_contaminated_lineage", False
        ),
        "descendant_bodies_created_false": (
            operation.get("descendant_body_a_created") is False
            and operation.get("descendant_body_b_created") is False
        ),
        "standing_descendants_created_false": operation.get(
            "standing_descendant_created"
        )
        is False,
        "prior_unsupported_claims_validated_false": (
            operation.get("prior_unsupported_candidate_a_claim_validated") is False
            and operation.get("prior_unsupported_candidate_b_claim_validated") is False
            and operation.get("prior_unsupported_derivation_event_claim_validated")
            is False
        ),
        "affected_file_repaired_false": operation.get("affected_file_repaired")
        is False,
        "affected_file_edited_false": operation.get("affected_file_edited") is False,
        "affected_file_deleted_false": operation.get("affected_file_deleted")
        is False,
        "affected_file_overwritten_false": operation.get("affected_file_overwritten")
        is False,
        "affected_file_replaced_false": operation.get("affected_file_replaced")
        is False,
        "affected_file_redeemed_false": operation.get("affected_file_redeemed")
        is False,
        "affected_file_treated_as_clean_basis_false": operation.get(
            "affected_file_treated_as_clean_basis"
        )
        is False,
        "contaminated_lineage_treated_as_clean_basis_false": operation.get(
            "contaminated_lineage_treated_as_clean_basis"
        )
        is False,
        "evidence_check_overridden_false": operation.get("evidence_check_overridden")
        is False,
        "evidence_check_bypassed_false": operation.get("evidence_check_bypassed")
        is False,
        "boundary_overridden_false": operation.get("boundary_overridden") is False,
        "boundary_bypassed_false": operation.get("boundary_bypassed") is False,
        "scan_allowed_false": operation.get("scan_allowed") is False,
        "repair_allowed_false": operation.get("repair_allowed") is False,
        "validation_enforcement_allowed_false": operation.get(
            "validation_enforcement_allowed"
        )
        is False,
        "standing_authorized_false": operation.get("standing_authorized") is False,
        "crossing_authorized_false": operation.get("crossing_authorized") is False,
        "relation_authorized_false": operation.get("relation_authorized") is False,
        "field_machinery_authorized_false": operation.get(
            "field_machinery_authorized"
        )
        is False,
        "runtime_authorized_false": operation.get("runtime_authorized") is False,
        "currentness_authorized_false": operation.get("currentness_authorized")
        is False,
        "authority_authorized_false": operation.get("authority_authorized") is False,
        "output_authorized_false": operation.get("output_authorized") is False,
        "action_authorized_false": operation.get("action_authorized") is False,
        "derivative_reception_authorized_false": operation.get(
            "derivative_reception_authorized"
        )
        is False,
        "synchronization_authorized_false": operation.get(
            "synchronization_authorized"
        )
        is False,
        "follow_on_authorized_false": operation.get("follow_on_authorized") is False,
        "scan_not_performed": operation.get("scan_performed") is False,
        "repository_scan_not_performed": operation.get("repository_scan_performed")
        is False,
        "repair_not_performed": operation.get("repair_performed") is False,
        "validation_not_enforced": operation.get("validation_enforced") is False,
        "hidden_repair_not_performed": operation.get("hidden_repair_performed")
        is False,
        "silent_overwrite_not_performed": operation.get("silent_overwrite_performed")
        is False,
        "operation_spec_markers_present": operation.get(
            "operation_spec_markers_present", False
        ),
        "contaminated_lineage_markers_present": operation.get(
            "contaminated_lineage_markers_present", False
        ),
        "evidence_check_terminal_summary_markers_present": operation.get(
            "evidence_check_terminal_summary_markers_present", False
        ),
        "evidence_check_artifact_markers_present": operation.get(
            "evidence_check_artifact_markers_present", False
        ),
        "differentiation_operation_boundary_terminal_summary_markers_present": (
            operation.get(
                "differentiation_operation_boundary_terminal_summary_markers_present",
                False,
            )
        ),
        "differentiation_operation_boundary_artifact_markers_present": operation.get(
            "differentiation_operation_boundary_artifact_markers_present", False
        ),
        "prior_unsupported_claims_preserved": operation.get(
            "prior_unsupported_claims_preserved", False
        ),
        "contaminated_lineage_preserved": operation.get(
            "contaminated_lineage_preserved", False
        ),
        "result_level_non_claims_canonical_false": non_claims_canonical,
    }


def _sanitize_filename(value: Any) -> str:
    safe = str(value or DEFAULT_OPERATION_ID)
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe.strip("._-") or DEFAULT_OPERATION_ID


def _next_available_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    for index in range(1, 1000):
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
    raise DescendantBodyDifferentiationOperationV0MinError(
        f"could not find available output path for {path}"
    )


def write_descendant_body_differentiation_operation_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a stable JSON result without overwriting an existing file."""

    operation = result.get("descendant_body_differentiation_operation")
    if not isinstance(operation, MappingABC):
        operation_id = DEFAULT_OPERATION_ID
    else:
        operation_id = operation.get("operation_id") or DEFAULT_OPERATION_ID

    filename = (
        f"{_sanitize_filename(operation_id)}"
        "__descendant_body_differentiation_operation_v0_min_result.json"
    )
    if output_path is None:
        target = REPO_ROOT / OUTPUT_ROOT / filename
    else:
        supplied = Path(output_path)
        if not supplied.is_absolute():
            supplied = REPO_ROOT / supplied
        target = supplied / filename if supplied.suffix == "" else supplied

    target.parent.mkdir(parents=True, exist_ok=True)
    final_path = _next_available_path(target)
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(
            _json_safe(result),
            handle,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        handle.write("\n")
    return final_path
