"""Resolve one descendant-body differentiation operation boundary.

This resolver records one DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY
result object only. It does not implement or perform the future operation, does
not create candidate records, does not create descendant bodies, does not
validate prior unsupported claims, does not repair the contaminated lineage
file, and does not authorize standing, crossing, relation, FIELD machinery,
runtime, currentness, authority, output, action, derivative reception,
synchronization, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class DescendantBodyDifferentiationOperationBoundaryV0MinError(RuntimeError):
    """Bounded resolver error for request/path/write handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_descendant_body_differentiation_operation_boundary_v0_min"
)

OUTCOME_RECORDED = "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

BOUNDARY_TYPE = "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY"
FUTURE_OPERATION_TYPE = "DESCENDANT_BODY_DIFFERENTIATION_OPERATION"
FUTURE_OPERATION_SCOPE = "ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY"
FUTURE_CANDIDATE_RECORD_POLICY = (
    "EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS"
)
FUTURE_FAILURE_VISIBILITY_POLICY = "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL"

SUPPORTED_FUTURE_OPERATION_TYPE_VALUES = (FUTURE_OPERATION_TYPE,)
SUPPORTED_FUTURE_OPERATION_SCOPE_VALUES = (FUTURE_OPERATION_SCOPE,)
SUPPORTED_FUTURE_CANDIDATE_RECORD_POLICY_VALUES = (
    FUTURE_CANDIDATE_RECORD_POLICY,
)
SUPPORTED_FUTURE_FAILURE_VISIBILITY_POLICY_VALUES = (
    FUTURE_FAILURE_VISIBILITY_POLICY,
)

FUTURE_OPERATION_OUTCOME_FAMILY = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BLOCKED",
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_NOT_RECORDED",
)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_differentiation_"
    "operation_boundary_v0_min"
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_BOUNDARY_ID = "descendant_body_differentiation_operation_boundary_001"
DEFAULT_STANDING_BODY_PROOF_BASIS_REFERENCE = (
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
DEFAULT_BOUNDARY_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_V0_MIN_SPEC.md"
)
DEFAULT_QUESTION = (
    "Given one preserved standing body-proof basis, one preserved contaminated "
    "descendant-body derivation event file, one completed existence-claim "
    "evidence requirement boundary line, and one completed existence-claim "
    "evidence check line that mechanically recorded the affected descendant "
    "claims as UNSUPPORTED, may the repo record a boundary allowing future "
    "consideration of exactly one separately implemented descendant-body "
    "differentiation operation by which two non-standing descendant-body-basis "
    "candidate records may be produced only through separately emitted operation "
    "evidence, while preserving that this boundary does not itself create "
    "descendants, candidates, derivation, standing, relation, crossing, FIELD "
    "machinery, runtime, currentness, authority, output, action, derivative "
    "reception, synchronization, repair, scan, validation enforcement, or "
    "follow-on work?"
)

DEFAULT_FUTURE_OPERATION_SHAPE = {
    "operation_id": "future_descendant_body_differentiation_operation_id",
    "operation_type": FUTURE_OPERATION_TYPE,
    "operation_version": RESULT_VERSION,
    "operation_scope": FUTURE_OPERATION_SCOPE,
    "source_body_proof_basis_reference": DEFAULT_STANDING_BODY_PROOF_BASIS_REFERENCE,
    "contaminated_lineage_reference": DEFAULT_CONTAMINATED_LINEAGE_REFERENCE,
    "evidence_requirement_reference": DEFAULT_EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE,
    "evidence_check_reference": DEFAULT_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
    "differentiation_method": "separately_bounded_future_operation_only",
    "candidate_record_policy": FUTURE_CANDIDATE_RECORD_POLICY,
    "failure_visibility_policy": FUTURE_FAILURE_VISIBILITY_POLICY,
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
}

REQUIRED_FALSE_NON_CLAIMS = (
    "operation_created",
    "operation_performed",
    "operation_recorded",
    "differentiation_performed",
    "candidate_records_created",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_basis_candidate_a_created",
    "descendant_body_basis_candidate_b_created",
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
    "repo_presence_treated_as_standing",
    "codex_execution_treated_as_truth",
    "operator_authorization_treated_as_sole_authorship",
    "derivative_rendering_treated_as_standing_evidence",
    "later_recognition_treated_as_upstream_validity",
    "evidence_check_overridden",
    "evidence_check_bypassed",
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
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "follow_on_work_authorized",
    "scan_performed",
    "repository_scan_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "descendant_body_differentiation_operation_boundary_recorded",
    "boundary_created",
    "standing_body_proof_basis_reference_declared",
    "contaminated_lineage_reference_declared",
    "evidence_requirement_boundary_reference_declared",
    "evidence_check_terminal_summary_reference_declared",
    "evidence_check_artifact_reference_declared",
    "future_operation_shape_declared",
    "future_operation_type_accepted",
    "future_operation_scope_accepted",
    "future_candidate_record_policy_accepted",
    "future_failure_visibility_policy_accepted",
    "boundary_spec_markers_present",
    "contaminated_lineage_markers_present",
    "evidence_check_terminal_summary_markers_present",
    "evidence_check_artifact_markers_present",
    "contaminated_lineage_preserved",
    "prior_unsupported_claims_preserved",
    "future_operation_not_created",
    "candidate_records_not_created",
    "descendant_bodies_not_created",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_QUESTION_UNDECLARED",
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_INTENT_UNSUPPORTED",
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_BLOCK_REQUESTED",
    "STANDING_BODY_PROOF_BASIS_REFERENCE_MISSING",
    "CONTAMINATED_LINEAGE_REFERENCE_MISSING",
    "EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE_MISSING",
    "EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EVIDENCE_CHECK_ARTIFACT_REFERENCE_MISSING",
    "BOUNDARY_SPEC_REFERENCE_MISSING",
    "FUTURE_OPERATION_TYPE_MISSING",
    "FUTURE_OPERATION_TYPE_NOT_DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
    "FUTURE_OPERATION_SCOPE_MISSING",
    "FUTURE_OPERATION_SCOPE_NOT_ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
    "FUTURE_CANDIDATE_RECORD_POLICY_MISSING",
    "FUTURE_CANDIDATE_RECORD_POLICY_NOT_EVIDENCE_GATED",
    "FUTURE_FAILURE_VISIBILITY_POLICY_MISSING",
    "FUTURE_FAILURE_VISIBILITY_POLICY_NOT_VISIBLE_BLOCK",
    "FUTURE_OPERATION_SHAPE_MISSING",
    "FUTURE_OPERATION_SHAPE_MALFORMED",
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
    "REQUESTED_OPERATION_CREATION",
    "REQUESTED_OPERATION_PERFORMANCE",
    "REQUESTED_CANDIDATE_RECORD_CREATION",
    "REQUESTED_DESCENDANT_BODY_CREATION",
    "REQUESTED_STANDING_AUTHORIZATION",
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
    "BOUNDARY_SPEC_MARKER_MISSING",
    "CONTAMINATED_LINEAGE_MARKER_MISSING",
    "EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING",
    "OPERATION_CREATED",
    "OPERATION_PERFORMED",
    "OPERATION_RECORDED",
    "DIFFERENTIATION_PERFORMED",
    "CANDIDATE_RECORDS_CREATED",
    "DESCENDANT_BODY_A_CREATED",
    "DESCENDANT_BODY_B_CREATED",
    "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED",
    "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED",
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
    "REPO_PRESENCE_TREATED_AS_STANDING",
    "CODEX_EXECUTION_TREATED_AS_TRUTH",
    "OPERATOR_AUTHORIZATION_TREATED_AS_SOLE_AUTHORSHIP",
    "DERIVATIVE_RENDERING_TREATED_AS_STANDING_EVIDENCE",
    "LATER_RECOGNITION_TREATED_AS_UPSTREAM_VALIDITY",
    "EVIDENCE_CHECK_OVERRIDDEN",
    "EVIDENCE_CHECK_BYPASSED",
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
    "OUTPUT_AUTHORIZED",
    "ACTION_AUTHORIZED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "SYNCHRONIZATION_AUTHORIZED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "SCAN_PERFORMED",
    "REPOSITORY_SCAN_PERFORMED",
    "REPAIR_PERFORMED",
    "VALIDATION_ENFORCED",
    "HIDDEN_REPAIR_PERFORMED",
    "SILENT_OVERWRITE_PERFORMED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_REQUEST_UNREADABLE",
)

FALSE_POSTURE_BLOCK_CODES = {
    "operation_created": "OPERATION_CREATED",
    "operation_performed": "OPERATION_PERFORMED",
    "operation_recorded": "OPERATION_RECORDED",
    "differentiation_performed": "DIFFERENTIATION_PERFORMED",
    "candidate_records_created": "CANDIDATE_RECORDS_CREATED",
    "descendant_body_a_created": "DESCENDANT_BODY_A_CREATED",
    "descendant_body_b_created": "DESCENDANT_BODY_B_CREATED",
    "descendant_body_basis_candidate_a_created": (
        "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED"
    ),
    "descendant_body_basis_candidate_b_created": (
        "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED"
    ),
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
    "evidence_check_overridden": "EVIDENCE_CHECK_OVERRIDDEN",
    "evidence_check_bypassed": "EVIDENCE_CHECK_BYPASSED",
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
    "output_authorized": "OUTPUT_AUTHORIZED",
    "action_authorized": "ACTION_AUTHORIZED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "synchronization_authorized": "SYNCHRONIZATION_AUTHORIZED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "scan_performed": "SCAN_PERFORMED",
    "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
    "repair_performed": "REPAIR_PERFORMED",
    "validation_enforced": "VALIDATION_ENFORCED",
    "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
    "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
}

BOUNDARY_SPEC_MARKERS = (
    "Descendant Body Differentiation Operation Boundary V0 Minimum Specification",
    "This file defines one boundary for a future descendant-body differentiation operation.",
    "This file does not perform the operation.",
    "candidate records must include evidence supporting their creation by that operation",
    "The future operation must not inherit candidate existence",
    "boundary_created = true",
    "operation_created = false",
    "candidate_records_created = false",
    "descendant_body_basis_candidate_a_created = false",
    "descendant_body_basis_candidate_b_created = false",
    "valid_derivation_event_recorded = false",
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


def _summary_or_boundary_value(
    artifact: Mapping[str, Any], summary_key: str, boundary_key: str | None = None
) -> Any:
    summary = artifact.get("existence_claim_evidence_check_summary")
    if isinstance(summary, MappingABC) and summary_key in summary:
        return summary.get(summary_key)
    check = artifact.get("existence_claim_evidence_check")
    if isinstance(check, MappingABC):
        return check.get(boundary_key or summary_key)
    return None


def _artifact_claim_outcomes(artifact: Mapping[str, Any]) -> dict[str, str]:
    outcomes = artifact.get("existence_claim_evidence_check_per_claim_outcomes")
    if not isinstance(outcomes, list):
        return {}
    result: dict[str, str] = {}
    for item in outcomes:
        if not isinstance(item, MappingABC):
            continue
        claim_key = item.get("claim_key")
        per_claim_outcome = item.get("per_claim_outcome")
        if isinstance(claim_key, str) and isinstance(per_claim_outcome, str):
            result[claim_key] = per_claim_outcome
    return result


def _evidence_artifact_markers_present(artifact: Any) -> bool:
    if not isinstance(artifact, MappingABC):
        return False
    if artifact.get("outcome") != "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED":
        return False
    if (
        _summary_or_boundary_value(artifact, "file_level_outcome")
        != "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS"
    ):
        return False
    expected_counts = {
        "failed_check_count": 0,
        "detected_claim_count": 3,
        "unsupported_claim_count": 3,
        "evidence_supported_claim_count": 0,
    }
    for key, expected in expected_counts.items():
        if _summary_or_boundary_value(artifact, key) != expected:
            return False
    outcomes = _artifact_claim_outcomes(artifact)
    for claim_key in CONTAMINATED_LINEAGE_MARKERS:
        normalized_key = claim_key.split(" = ", 1)[0]
        if outcomes.get(normalized_key) != "UNSUPPORTED":
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
    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = request.get(key, False)
        _add_check(
            checks,
            f"top_level_{key}_not_true",
            value is not True,
            "not true",
            value,
            FALSE_POSTURE_BLOCK_CODES[key],
        )


def _open_items() -> list[str]:
    return [
        "descendant-body differentiation operation resolver",
        "descendant-body differentiation operation test",
        "descendant-body differentiation operation artifact",
        "descendant-body differentiation operation terminal summary",
        "candidate-record evidence emission",
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


def _required_future_operation_shape() -> dict[str, Any]:
    return copy.deepcopy(DEFAULT_FUTURE_OPERATION_SHAPE)


def build_declared_descendant_body_differentiation_operation_boundary_v0_min_request(
    descendant_body_differentiation_operation_boundary_id: str = DEFAULT_BOUNDARY_ID,
    descendant_body_differentiation_operation_boundary_question: str = DEFAULT_QUESTION,
    descendant_body_differentiation_operation_boundary_intent: str = INTENT_RECORD,
    standing_body_proof_basis_reference: str = (
        DEFAULT_STANDING_BODY_PROOF_BASIS_REFERENCE
    ),
    contaminated_lineage_reference: str = DEFAULT_CONTAMINATED_LINEAGE_REFERENCE,
    evidence_requirement_boundary_reference: str = (
        DEFAULT_EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE
    ),
    evidence_check_terminal_summary_reference: str = (
        DEFAULT_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE
    ),
    evidence_check_artifact_reference: str = DEFAULT_EVIDENCE_CHECK_ARTIFACT_REFERENCE,
    boundary_spec_reference: str = DEFAULT_BOUNDARY_SPEC_REFERENCE,
    future_operation_type: str = FUTURE_OPERATION_TYPE,
    future_operation_scope: str = FUTURE_OPERATION_SCOPE,
    future_candidate_record_policy: str = FUTURE_CANDIDATE_RECORD_POLICY,
    future_failure_visibility_policy: str = FUTURE_FAILURE_VISIBILITY_POLICY,
    future_operation_shape: Mapping[str, Any] | None = None,
    scan_allowed: bool = False,
    repair_allowed: bool = False,
    validation_enforcement_allowed: bool = False,
    operation_created: bool = False,
    operation_performed: bool = False,
    operation_recorded: bool = False,
    candidate_records_created: bool = False,
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
    """Build a bounded default declared boundary request."""

    request = {
        "descendant_body_differentiation_operation_boundary_id": (
            descendant_body_differentiation_operation_boundary_id
        ),
        "descendant_body_differentiation_operation_boundary_question": (
            descendant_body_differentiation_operation_boundary_question
        ),
        "descendant_body_differentiation_operation_boundary_intent": (
            descendant_body_differentiation_operation_boundary_intent
        ),
        "standing_body_proof_basis_reference": standing_body_proof_basis_reference,
        "contaminated_lineage_reference": contaminated_lineage_reference,
        "evidence_requirement_boundary_reference": (
            evidence_requirement_boundary_reference
        ),
        "evidence_check_terminal_summary_reference": (
            evidence_check_terminal_summary_reference
        ),
        "evidence_check_artifact_reference": evidence_check_artifact_reference,
        "boundary_spec_reference": boundary_spec_reference,
        "future_operation_type": future_operation_type,
        "future_operation_scope": future_operation_scope,
        "future_candidate_record_policy": future_candidate_record_policy,
        "future_failure_visibility_policy": future_failure_visibility_policy,
        "future_operation_shape": (
            copy.deepcopy(future_operation_shape)
            if future_operation_shape is not None
            else _required_future_operation_shape()
        ),
        "scan_allowed": scan_allowed,
        "repair_allowed": repair_allowed,
        "validation_enforcement_allowed": validation_enforcement_allowed,
        "operation_created": operation_created,
        "operation_performed": operation_performed,
        "operation_recorded": operation_recorded,
        "candidate_records_created": candidate_records_created,
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
    return request


def _reference_declared(request: Mapping[str, Any], key: str) -> bool:
    value = request.get(key)
    return isinstance(value, str) and value.strip() != ""


def _build_boundary_object(
    request: Mapping[str, Any],
    recorded: bool,
    marker_posture: Mapping[str, bool],
) -> dict[str, Any]:
    boundary = {
        "boundary_id": _json_safe(
            request.get("descendant_body_differentiation_operation_boundary_id")
            or DEFAULT_BOUNDARY_ID
        ),
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "standing_body_proof_basis_reference": _json_safe(
            request.get("standing_body_proof_basis_reference")
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
        "future_operation_type": _json_safe(request.get("future_operation_type")),
        "future_operation_scope": _json_safe(request.get("future_operation_scope")),
        "future_candidate_record_policy": _json_safe(
            request.get("future_candidate_record_policy")
        ),
        "future_failure_visibility_policy": _json_safe(
            request.get("future_failure_visibility_policy")
        ),
        "future_operation_shape": _json_safe(_required_future_operation_shape()),
        "descendant_body_differentiation_operation_boundary_recorded": recorded,
        "boundary_created": recorded,
        "standing_body_proof_basis_reference_declared": _reference_declared(
            request, "standing_body_proof_basis_reference"
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
        "future_operation_shape_declared": "future_operation_shape" in request,
        "future_operation_type_accepted": (
            request.get("future_operation_type") == FUTURE_OPERATION_TYPE
        ),
        "future_operation_scope_accepted": (
            request.get("future_operation_scope") == FUTURE_OPERATION_SCOPE
        ),
        "future_candidate_record_policy_accepted": (
            request.get("future_candidate_record_policy")
            == FUTURE_CANDIDATE_RECORD_POLICY
        ),
        "future_failure_visibility_policy_accepted": (
            request.get("future_failure_visibility_policy")
            == FUTURE_FAILURE_VISIBILITY_POLICY
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
        "output_authorized_result": False,
        "action_authorized_result": False,
        "derivative_reception_authorized_result": False,
        "synchronization_authorized_result": False,
        "boundary_spec_markers_present": bool(
            marker_posture.get("boundary_spec_markers_present")
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
        "contaminated_lineage_preserved": bool(
            marker_posture.get("contaminated_lineage_markers_present")
        ),
        "prior_unsupported_claims_preserved": bool(
            marker_posture.get("evidence_check_terminal_summary_markers_present")
            and marker_posture.get("evidence_check_artifact_markers_present")
        ),
        "future_operation_not_created": True,
        "candidate_records_not_created": True,
        "descendant_bodies_not_created": True,
    }
    boundary.update(_canonical_non_claims())
    return boundary


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


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    upstream_basis: Mapping[str, Any],
    future_operation_boundary_basis: Mapping[str, Any],
    marker_posture: Mapping[str, bool],
    outcome: str,
    recorded: bool,
) -> dict[str, Any]:
    boundary_object = _build_boundary_object(request, recorded, marker_posture)
    failed_checks = [check for check in checks if check.get("passed") is False]
    passed_checks = [check for check in checks if check.get("passed") is True]
    failed_code = _first_failed_code(checks)
    non_claims = _canonical_non_claims()
    statement = {
        "descendant_body_differentiation_operation_boundary_recorded": recorded,
        "boundary_created": recorded,
        "standing_body_proof_basis_reference_declared": boundary_object[
            "standing_body_proof_basis_reference_declared"
        ],
        "contaminated_lineage_reference_declared": boundary_object[
            "contaminated_lineage_reference_declared"
        ],
        "evidence_requirement_boundary_reference_declared": boundary_object[
            "evidence_requirement_boundary_reference_declared"
        ],
        "evidence_check_terminal_summary_reference_declared": boundary_object[
            "evidence_check_terminal_summary_reference_declared"
        ],
        "evidence_check_artifact_reference_declared": boundary_object[
            "evidence_check_artifact_reference_declared"
        ],
        "future_operation_shape_declared": boundary_object[
            "future_operation_shape_declared"
        ],
        "future_operation_type_accepted": boundary_object[
            "future_operation_type_accepted"
        ],
        "future_operation_scope_accepted": boundary_object[
            "future_operation_scope_accepted"
        ],
        "future_candidate_record_policy_accepted": boundary_object[
            "future_candidate_record_policy_accepted"
        ],
        "future_failure_visibility_policy_accepted": boundary_object[
            "future_failure_visibility_policy_accepted"
        ],
        "boundary_spec_markers_present": boundary_object[
            "boundary_spec_markers_present"
        ],
        "contaminated_lineage_markers_present": boundary_object[
            "contaminated_lineage_markers_present"
        ],
        "evidence_check_terminal_summary_markers_present": boundary_object[
            "evidence_check_terminal_summary_markers_present"
        ],
        "evidence_check_artifact_markers_present": boundary_object[
            "evidence_check_artifact_markers_present"
        ],
        "contaminated_lineage_preserved": boundary_object[
            "contaminated_lineage_preserved"
        ],
        "prior_unsupported_claims_preserved": boundary_object[
            "prior_unsupported_claims_preserved"
        ],
        "future_operation_not_created": True,
        "candidate_records_not_created": True,
        "descendant_bodies_not_created": True,
        "result_level_non_claims_canonical_false": all(
            value is False for value in non_claims.values()
        ),
    }
    statement.update(non_claims)
    result: dict[str, Any] = {
        "descendant_body_differentiation_operation_boundary_metadata": {
            "descendant_body_differentiation_operation_boundary_id": (
                boundary_object["boundary_id"]
            ),
            "boundary_type": BOUNDARY_TYPE,
            "result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_descendant_body_differentiation_operation_boundary_question": {
            "descendant_body_differentiation_operation_boundary_id": _json_safe(
                request.get("descendant_body_differentiation_operation_boundary_id")
            ),
            "descendant_body_differentiation_operation_boundary_question": _json_safe(
                request.get("descendant_body_differentiation_operation_boundary_question")
            ),
            "descendant_body_differentiation_operation_boundary_intent": _json_safe(
                request.get("descendant_body_differentiation_operation_boundary_intent")
            ),
            "standing_body_proof_basis_reference": _json_safe(
                request.get("standing_body_proof_basis_reference")
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
            "boundary_spec_reference": _json_safe(
                request.get("boundary_spec_reference")
            ),
            "future_operation_type": _json_safe(
                request.get("future_operation_type")
            ),
            "future_operation_scope": _json_safe(
                request.get("future_operation_scope")
            ),
            "future_candidate_record_policy": _json_safe(
                request.get("future_candidate_record_policy")
            ),
            "future_failure_visibility_policy": _json_safe(
                request.get("future_failure_visibility_policy")
            ),
            "scan_allowed": _json_safe(request.get("scan_allowed")),
            "repair_allowed": _json_safe(request.get("repair_allowed")),
            "validation_enforcement_allowed": _json_safe(
                request.get("validation_enforcement_allowed")
            ),
        },
        "upstream_basis": dict(upstream_basis),
        "future_operation_boundary_basis": dict(future_operation_boundary_basis),
        "descendant_body_differentiation_operation_boundary": boundary_object,
        "descendant_body_differentiation_operation_boundary_checks": checks,
        "descendant_body_differentiation_operation_boundary_statement": statement,
        "descendant_body_differentiation_operation_boundary_non_meaning": {
            "not_descendant_body_differentiation_operation": True,
            "not_operation_execution": True,
            "not_candidate_record_creation": True,
            "not_descendant_body_creation": True,
            "not_prior_unsupported_claim_validation": True,
            "not_affected_file_repair": True,
            "not_repository_scan": True,
            "not_standing_check": True,
            "not_crossing": True,
            "not_relation": True,
            "not_field_machinery": True,
            "not_runtime": True,
            "not_currentness": True,
            "not_authority": True,
            "not_output_action_or_follow_on": True,
        },
        "additional_basis_required": [
            check["check_name"]
            for check in failed_checks
            if str(check.get("failure_code", "")).endswith("MISSING")
            or str(check.get("failure_code", "")).endswith("UNREADABLE")
            or str(check.get("failure_code", "")).endswith("MALFORMED")
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
    result["descendant_body_differentiation_operation_boundary_summary"] = (
        build_descendant_body_differentiation_operation_boundary_v0_min_summary(result)
    )
    result["descendant_body_differentiation_operation_boundary_summary"][
        "passed_check_count"
    ] = len(passed_checks)
    result["descendant_body_differentiation_operation_boundary_summary"][
        "failed_check_count"
    ] = len(failed_checks)
    return result


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
            "requested_operation_creation",
            ("requested_operation_creation", "operation_creation_requested", "create_operation"),
            "REQUESTED_OPERATION_CREATION",
        ),
        (
            "requested_operation_performance",
            ("requested_operation_performance", "operation_performance_requested", "perform_operation"),
            "REQUESTED_OPERATION_PERFORMANCE",
        ),
        (
            "requested_candidate_record_creation",
            ("requested_candidate_record_creation", "candidate_record_creation_requested", "create_candidate_records"),
            "REQUESTED_CANDIDATE_RECORD_CREATION",
        ),
        (
            "requested_descendant_body_creation",
            ("requested_descendant_body_creation", "descendant_body_creation_requested", "create_descendant_bodies"),
            "REQUESTED_DESCENDANT_BODY_CREATION",
        ),
        (
            "requested_standing_authorization",
            ("requested_standing_authorization", "standing_authorization_requested", "authorize_standing"),
            "REQUESTED_STANDING_AUTHORIZATION",
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


def _validate_future_operation_shape_details(
    future_operation_shape: Any, checks: list[dict[str, Any]]
) -> None:
    if not isinstance(future_operation_shape, MappingABC):
        return

    expected_values = (
        ("operation_type", FUTURE_OPERATION_TYPE, "FUTURE_OPERATION_TYPE_NOT_DESCENDANT_BODY_DIFFERENTIATION_OPERATION"),
        ("operation_scope", FUTURE_OPERATION_SCOPE, "FUTURE_OPERATION_SCOPE_NOT_ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY"),
        ("candidate_record_policy", FUTURE_CANDIDATE_RECORD_POLICY, "FUTURE_CANDIDATE_RECORD_POLICY_NOT_EVIDENCE_GATED"),
        ("failure_visibility_policy", FUTURE_FAILURE_VISIBILITY_POLICY, "FUTURE_FAILURE_VISIBILITY_POLICY_NOT_VISIBLE_BLOCK"),
    )
    for key, expected, code in expected_values:
        actual = future_operation_shape.get(key)
        _add_check(
            checks,
            f"future_operation_shape_{key}_exact",
            actual == expected,
            expected,
            actual,
            code,
        )

    false_values = (
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
    )
    for key, code in false_values:
        actual = future_operation_shape.get(key)
        _add_check(
            checks,
            f"future_operation_shape_{key}_is_false",
            actual is False,
            False,
            actual,
            code,
        )


def resolve_descendant_body_differentiation_operation_boundary_v0_min(
    declared_descendant_body_differentiation_operation_boundary: Mapping[str, Any]
    | None = None,
) -> dict[str, Any]:
    """Resolve one declared descendant-body differentiation operation boundary."""

    if declared_descendant_body_differentiation_operation_boundary is None:
        request: dict[str, Any] = (
            build_declared_descendant_body_differentiation_operation_boundary_v0_min_request()
        )
    elif isinstance(
        declared_descendant_body_differentiation_operation_boundary, MappingABC
    ):
        request = copy.deepcopy(
            dict(declared_descendant_body_differentiation_operation_boundary)
        )
    else:
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_is_mapping",
            False,
            "mapping",
            type(declared_descendant_body_differentiation_operation_boundary).__name__,
            "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_REQUEST_MALFORMED",
        )
        return _build_result(
            {},
            checks,
            {},
            {},
            {},
            OUTCOME_BLOCKED,
            False,
        )

    checks = []

    question = request.get(
        "descendant_body_differentiation_operation_boundary_question"
    )
    _add_check(
        checks,
        "boundary_question_declared",
        isinstance(question, str) and question.strip() != "",
        "non-empty boundary question",
        question,
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get("descendant_body_differentiation_operation_boundary_intent")
    _add_check(
        checks,
        "boundary_intent_supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _add_check(
        checks,
        "boundary_block_not_requested",
        intent != INTENT_BLOCK,
        f"intent is not {INTENT_BLOCK}",
        intent,
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_BLOCK_REQUESTED",
    )

    standing_ref_declared = _validate_reference(
        request,
        checks,
        "standing_body_proof_basis_reference",
        "standing_body_proof_basis_reference_declared",
        "STANDING_BODY_PROOF_BASIS_REFERENCE_MISSING",
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
    evidence_check_summary_ref_declared = _validate_reference(
        request,
        checks,
        "evidence_check_terminal_summary_reference",
        "evidence_check_terminal_summary_reference_declared",
        "EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    )
    evidence_check_artifact_ref_declared = _validate_reference(
        request,
        checks,
        "evidence_check_artifact_reference",
        "evidence_check_artifact_reference_declared",
        "EVIDENCE_CHECK_ARTIFACT_REFERENCE_MISSING",
    )
    boundary_spec_ref_declared = _validate_reference(
        request,
        checks,
        "boundary_spec_reference",
        "boundary_spec_reference_declared",
        "BOUNDARY_SPEC_REFERENCE_MISSING",
    )

    future_operation_type = request.get("future_operation_type")
    _add_check(
        checks,
        "future_operation_type_declared",
        isinstance(future_operation_type, str) and future_operation_type.strip() != "",
        FUTURE_OPERATION_TYPE,
        future_operation_type,
        "FUTURE_OPERATION_TYPE_MISSING",
    )
    _add_check(
        checks,
        "future_operation_type_exact",
        future_operation_type == FUTURE_OPERATION_TYPE,
        FUTURE_OPERATION_TYPE,
        future_operation_type,
        "FUTURE_OPERATION_TYPE_NOT_DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
    )

    future_operation_scope = request.get("future_operation_scope")
    _add_check(
        checks,
        "future_operation_scope_declared",
        isinstance(future_operation_scope, str)
        and future_operation_scope.strip() != "",
        FUTURE_OPERATION_SCOPE,
        future_operation_scope,
        "FUTURE_OPERATION_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "future_operation_scope_exact",
        future_operation_scope == FUTURE_OPERATION_SCOPE,
        FUTURE_OPERATION_SCOPE,
        future_operation_scope,
        "FUTURE_OPERATION_SCOPE_NOT_ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
    )

    future_candidate_record_policy = request.get("future_candidate_record_policy")
    _add_check(
        checks,
        "future_candidate_record_policy_declared",
        isinstance(future_candidate_record_policy, str)
        and future_candidate_record_policy.strip() != "",
        FUTURE_CANDIDATE_RECORD_POLICY,
        future_candidate_record_policy,
        "FUTURE_CANDIDATE_RECORD_POLICY_MISSING",
    )
    _add_check(
        checks,
        "future_candidate_record_policy_exact",
        future_candidate_record_policy == FUTURE_CANDIDATE_RECORD_POLICY,
        FUTURE_CANDIDATE_RECORD_POLICY,
        future_candidate_record_policy,
        "FUTURE_CANDIDATE_RECORD_POLICY_NOT_EVIDENCE_GATED",
    )

    future_failure_visibility_policy = request.get(
        "future_failure_visibility_policy"
    )
    _add_check(
        checks,
        "future_failure_visibility_policy_declared",
        isinstance(future_failure_visibility_policy, str)
        and future_failure_visibility_policy.strip() != "",
        FUTURE_FAILURE_VISIBILITY_POLICY,
        future_failure_visibility_policy,
        "FUTURE_FAILURE_VISIBILITY_POLICY_MISSING",
    )
    _add_check(
        checks,
        "future_failure_visibility_policy_exact",
        future_failure_visibility_policy == FUTURE_FAILURE_VISIBILITY_POLICY,
        FUTURE_FAILURE_VISIBILITY_POLICY,
        future_failure_visibility_policy,
        "FUTURE_FAILURE_VISIBILITY_POLICY_NOT_VISIBLE_BLOCK",
    )

    future_operation_shape_present = "future_operation_shape" in request
    future_operation_shape = request.get("future_operation_shape")
    _add_check(
        checks,
        "future_operation_shape_declared",
        future_operation_shape_present,
        "declared future operation shape",
        future_operation_shape_present,
        "FUTURE_OPERATION_SHAPE_MISSING",
    )
    _add_check(
        checks,
        "future_operation_shape_mapping_or_list",
        future_operation_shape_present
        and isinstance(future_operation_shape, (MappingABC, list, tuple)),
        "mapping or list shape",
        type(future_operation_shape).__name__,
        "FUTURE_OPERATION_SHAPE_MALFORMED",
    )
    _validate_future_operation_shape_details(future_operation_shape, checks)

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

    if boundary_spec_ref_declared:
        (
            boundary_spec_readable,
            boundary_spec_text,
            boundary_spec_error,
            boundary_spec_resolved,
        ) = _read_text(request.get("boundary_spec_reference"))
    else:
        boundary_spec_readable, boundary_spec_text, boundary_spec_error = (
            False,
            "",
            "reference missing",
        )
        boundary_spec_resolved = None
    boundary_spec_markers_present = boundary_spec_readable and _all_markers_present(
        boundary_spec_text, BOUNDARY_SPEC_MARKERS
    )
    _add_check(
        checks,
        "boundary_spec_markers_present",
        boundary_spec_markers_present,
        list(BOUNDARY_SPEC_MARKERS),
        "present" if boundary_spec_markers_present else "missing",
        "BOUNDARY_SPEC_MARKER_MISSING",
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

    if evidence_check_summary_ref_declared:
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

    if evidence_check_artifact_ref_declared:
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

    marker_posture = {
        "boundary_spec_markers_present": boundary_spec_markers_present,
        "contaminated_lineage_markers_present": contaminated_markers_present,
        "evidence_check_terminal_summary_markers_present": (
            evidence_summary_markers_present
        ),
        "evidence_check_artifact_markers_present": (
            evidence_artifact_markers_present
        ),
    }

    upstream_basis = {
        "standing_body_proof_basis_reference": {
            "reference": _json_safe(
                request.get("standing_body_proof_basis_reference")
            ),
            "declared": standing_ref_declared,
            "standing_body_proof_basis_recreated": False,
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
            declared=evidence_check_summary_ref_declared,
            readable=evidence_summary_readable,
            resolved_path=evidence_summary_resolved,
            read_error=evidence_summary_error,
            markers_present=evidence_summary_markers_present,
            marker_names=EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKERS,
        ),
        "evidence_check_artifact_reference": {
            "path": _json_safe(request.get("evidence_check_artifact_reference"))
            if evidence_check_artifact_ref_declared
            else None,
            "resolved_path": evidence_artifact_resolved,
            "declared": evidence_check_artifact_ref_declared,
            "readable": evidence_artifact_readable,
            "read_error": evidence_artifact_error,
            "markers_present": evidence_artifact_markers_present,
            "raw_artifact_body_returned": False,
        },
    }

    future_operation_boundary_basis = {
        "boundary_spec_reference": _basis_summary(
            path_value=request.get("boundary_spec_reference"),
            declared=boundary_spec_ref_declared,
            readable=boundary_spec_readable,
            resolved_path=boundary_spec_resolved,
            read_error=boundary_spec_error,
            markers_present=boundary_spec_markers_present,
            marker_names=BOUNDARY_SPEC_MARKERS,
        ),
        "future_operation_type": _json_safe(request.get("future_operation_type")),
        "future_operation_scope": _json_safe(request.get("future_operation_scope")),
        "future_candidate_record_policy": _json_safe(
            request.get("future_candidate_record_policy")
        ),
        "future_failure_visibility_policy": _json_safe(
            request.get("future_failure_visibility_policy")
        ),
        "future_operation_shape_declared": future_operation_shape_present,
        "future_operation_shape_malformed": not isinstance(
            future_operation_shape, (MappingABC, list, tuple)
        ),
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
        future_operation_boundary_basis,
        marker_posture,
        outcome,
        recorded,
    )


def resolve_descendant_body_differentiation_operation_boundary_v0_min_from_path(
    declared_descendant_body_differentiation_operation_boundary_path: Path | str,
) -> dict[str, Any]:
    """Resolve from one declared JSON request path."""

    try:
        path = _repo_path(declared_descendant_body_differentiation_operation_boundary_path)
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
            "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_REQUEST_UNREADABLE",
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
            "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_REQUEST_MALFORMED",
        )
        return _build_result({}, checks, {}, {}, {}, OUTCOME_BLOCKED, False)

    return resolve_descendant_body_differentiation_operation_boundary_v0_min(payload)


def build_descendant_body_differentiation_operation_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a bounded summary without embedding raw Markdown or artifact bodies."""

    boundary = result.get("descendant_body_differentiation_operation_boundary")
    if not isinstance(boundary, MappingABC):
        boundary = {}
    checks = result.get("descendant_body_differentiation_operation_boundary_checks")
    if not isinstance(checks, list):
        checks = []
    block = result.get("block")
    if not isinstance(block, MappingABC):
        block = {}
    question = result.get(
        "declared_descendant_body_differentiation_operation_boundary_question"
    )
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
        "boundary_id": boundary.get("boundary_id"),
        "question": question.get(
            "descendant_body_differentiation_operation_boundary_question"
        ),
        "intent": question.get(
            "descendant_body_differentiation_operation_boundary_intent"
        ),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_type": boundary.get("boundary_type"),
        "future_operation_type": boundary.get("future_operation_type"),
        "future_operation_scope": boundary.get("future_operation_scope"),
        "future_candidate_record_policy": boundary.get(
            "future_candidate_record_policy"
        ),
        "future_failure_visibility_policy": boundary.get(
            "future_failure_visibility_policy"
        ),
        "boundary_recorded": boundary.get(
            "descendant_body_differentiation_operation_boundary_recorded", False
        ),
        "boundary_created": boundary.get("boundary_created", False),
        "operation_created_false": boundary.get("operation_created") is False,
        "operation_performed_false": boundary.get("operation_performed") is False,
        "operation_recorded_false": boundary.get("operation_recorded") is False,
        "candidate_records_created_false": boundary.get("candidate_records_created")
        is False,
        "descendant_bodies_created_false": (
            boundary.get("descendant_body_a_created") is False
            and boundary.get("descendant_body_b_created") is False
        ),
        "prior_unsupported_claims_validated_false": (
            boundary.get("prior_unsupported_candidate_a_claim_validated") is False
            and boundary.get("prior_unsupported_candidate_b_claim_validated") is False
            and boundary.get("prior_unsupported_derivation_event_claim_validated")
            is False
        ),
        "affected_file_repaired_false": boundary.get("affected_file_repaired")
        is False,
        "affected_file_edited_false": boundary.get("affected_file_edited") is False,
        "affected_file_deleted_false": boundary.get("affected_file_deleted") is False,
        "affected_file_overwritten_false": boundary.get("affected_file_overwritten")
        is False,
        "affected_file_replaced_false": boundary.get("affected_file_replaced")
        is False,
        "affected_file_redeemed_false": boundary.get("affected_file_redeemed")
        is False,
        "affected_file_treated_as_clean_basis_false": boundary.get(
            "affected_file_treated_as_clean_basis"
        )
        is False,
        "contaminated_lineage_treated_as_clean_basis_false": boundary.get(
            "contaminated_lineage_treated_as_clean_basis"
        )
        is False,
        "evidence_check_overridden_false": boundary.get("evidence_check_overridden")
        is False,
        "evidence_check_bypassed_false": boundary.get("evidence_check_bypassed")
        is False,
        "scan_allowed_false": boundary.get("scan_allowed") is False,
        "repair_allowed_false": boundary.get("repair_allowed") is False,
        "validation_enforcement_allowed_false": boundary.get(
            "validation_enforcement_allowed"
        )
        is False,
        "standing_authorized_false": boundary.get("standing_authorized") is False,
        "crossing_authorized_false": boundary.get("crossing_authorized") is False,
        "relation_authorized_false": boundary.get("relation_authorized") is False,
        "field_machinery_authorized_false": boundary.get(
            "field_machinery_authorized"
        )
        is False,
        "runtime_authorized_false": boundary.get("runtime_authorized") is False,
        "currentness_authorized_false": boundary.get("currentness_authorized")
        is False,
        "authority_authorized_false": boundary.get("authority_authorized") is False,
        "output_authorized_false": boundary.get("output_authorized") is False,
        "action_authorized_false": boundary.get("action_authorized") is False,
        "derivative_reception_authorized_false": boundary.get(
            "derivative_reception_authorized"
        )
        is False,
        "synchronization_authorized_false": boundary.get(
            "synchronization_authorized"
        )
        is False,
        "follow_on_authorized_false": boundary.get("follow_on_authorized") is False,
        "scan_not_performed": boundary.get("scan_performed") is False,
        "repository_scan_not_performed": boundary.get("repository_scan_performed")
        is False,
        "repair_not_performed": boundary.get("repair_performed") is False,
        "validation_not_enforced": boundary.get("validation_enforced") is False,
        "hidden_repair_not_performed": boundary.get("hidden_repair_performed")
        is False,
        "silent_overwrite_not_performed": boundary.get("silent_overwrite_performed")
        is False,
        "boundary_spec_markers_present": boundary.get(
            "boundary_spec_markers_present", False
        ),
        "contaminated_lineage_markers_present": boundary.get(
            "contaminated_lineage_markers_present", False
        ),
        "evidence_check_terminal_summary_markers_present": boundary.get(
            "evidence_check_terminal_summary_markers_present", False
        ),
        "evidence_check_artifact_markers_present": boundary.get(
            "evidence_check_artifact_markers_present", False
        ),
        "contaminated_lineage_preserved": boundary.get(
            "contaminated_lineage_preserved", False
        ),
        "prior_unsupported_claims_preserved": boundary.get(
            "prior_unsupported_claims_preserved", False
        ),
        "future_operation_not_created": boundary.get(
            "future_operation_not_created", False
        ),
        "candidate_records_not_created": boundary.get(
            "candidate_records_not_created", False
        ),
        "descendant_bodies_not_created": boundary.get(
            "descendant_bodies_not_created", False
        ),
        "result_level_non_claims_canonical_false": non_claims_canonical,
    }


def _sanitize_filename(value: Any) -> str:
    safe = str(value or DEFAULT_BOUNDARY_ID)
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe.strip("._-") or DEFAULT_BOUNDARY_ID


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
    raise DescendantBodyDifferentiationOperationBoundaryV0MinError(
        f"could not find available output path for {path}"
    )


def write_descendant_body_differentiation_operation_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a stable JSON result without overwriting an existing file."""

    boundary = result.get("descendant_body_differentiation_operation_boundary")
    if not isinstance(boundary, MappingABC):
        boundary_id = DEFAULT_BOUNDARY_ID
    else:
        boundary_id = boundary.get("boundary_id") or DEFAULT_BOUNDARY_ID

    filename = (
        f"{_sanitize_filename(boundary_id)}"
        "__descendant_body_differentiation_operation_boundary_v0_min_result.json"
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
