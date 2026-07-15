"""Resolve one existence-claim evidence requirement boundary.

This resolver records one EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY object
only. It reads declared Markdown basis files only: the preserved contaminated
descendant-body derivation event file, the upstream negative seam case, and the
governing evidence-requirement boundary specification.

It does not scan the repository, enforce the future evidence requirement, create
a checker, create tests, repair the affected file, validate unsupported
existence claims, or create descendant bodies, derivation, standing, relation,
crossing, FIELD machinery, runtime, authority, currentness, output, action,
derivative reception, synchronization, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class ExistenceClaimEvidenceRequirementBoundaryV0MinError(RuntimeError):
    """Bounded resolver error for request/path handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_existence_claim_evidence_requirement_boundary_v0_min"

OUTCOME_RECORDED = "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_existence_claim_evidence_requirement_"
    "boundary_v0_min"
)

BOUNDARY_TYPE = "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY"
BOUNDARY_SCOPE = "UNSUPPORTED_EXISTENCE_CLAIM_CLASS_REQUIREMENT_ONLY"
SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)

INTENT_RECORD = "RECORD_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY"
INTENT_BLOCK = "BLOCK_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_BOUNDARY_ID = "existence_claim_evidence_requirement_boundary_001"
DEFAULT_QUESTION = (
    "Given one preserved negative seam case marking "
    "spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md as "
    "contaminated for unsupported existence claims, and one governing "
    "existence-claim evidence requirement boundary spec, may one "
    "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY be recorded that preserves "
    "the requirement that future existence-shaped true claims identify "
    "separately supported evidence before those claims may be treated as "
    "standing or clean basis, without repairing the affected file, validating "
    "unsupported claims, creating checker machinery, creating tests, creating "
    "terminal summary, scanning the repository, creating descendant bodies, "
    "recording derivation, creating standing, creating relation, authorizing "
    "crossing, creating FIELD machinery, creating runtime, creating authority, "
    "creating currentness, authorizing output, authorizing action, authorizing "
    "derivative reception, authorizing synchronization, or authorizing "
    "follow-on work?"
)

DEFAULT_AFFECTED_FILE_PATH = (
    "spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md"
)
DEFAULT_SEAM_CASE_PATH = (
    "spec/SEAM_CASE_LAW__CO_AGENCY_AUTHORIZATION_UNSUPPORTED_EXISTENCE_CLAIM_V0.md"
)
DEFAULT_EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_PATH = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_V0_MIN_SPEC.md"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "evidence_checker_created",
    "checker_created",
    "resolver_created",
    "test_created",
    "artifact_created",
    "scanner_created",
    "repository_scan_performed",
    "validation_performed",
    "evidence_requirement_enforced",
    "affected_file_repaired",
    "affected_file_edited",
    "affected_file_deleted",
    "affected_file_overwritten",
    "affected_file_invalidated_by_replacement",
    "seam_case_replaced",
    "seam_case_treated_as_repair",
    "unsupported_existence_claims_validated",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_basis_candidate_a_created",
    "descendant_body_basis_candidate_b_created",
    "valid_derivation_event_recorded",
    "body_division_performed",
    "body_copy_performed",
    "body_distinction_created",
    "separate_lineage_receipt_created",
    "separate_sealing_created",
    "descendant_standing_check_performed",
    "standing_descendant_created",
    "first_crossing_authorized",
    "relation_created",
    "field_machinery_created",
    "iammai_system_continuation_reopened",
    "field_handoff_reversed",
    "runtime_created",
    "api_created",
    "machinery_created",
    "currentness_created",
    "authority_created",
    "standing_created",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "follow_on_work_authorized",
    "repo_presence_treated_as_standing",
    "codex_execution_treated_as_truth",
    "operator_authorization_treated_as_sole_authorship",
    "derivative_rendering_treated_as_standing_evidence",
    "later_recognition_treated_as_upstream_validity",
    "contaminated_lineage_treated_as_clean_basis",
    "hidden_repair_performed",
    "silent_overwrite_performed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "existence_claim_evidence_requirement_boundary_recorded",
    "unsupported_existence_claim_class_preserved",
    "future_existence_claims_require_evidence",
    "affected_file_contamination_preserved",
    "affected_file_basis_preserved",
    "seam_case_basis_preserved",
    "evidence_requirement_boundary_spec_basis_preserved",
    "future_checker_or_resolver_may_be_considered",
    "repo_presence_not_standing_preserved",
    "codex_execution_not_truth_preserved",
    "operator_authorization_not_sole_authorship_preserved",
    "later_recognition_not_upstream_validity_preserved",
    "result_level_non_claims_canonical_false",
    "existence_shape_created_claim_targeted",
    "existence_shape_recorded_claim_targeted",
    "existence_shape_performed_claim_targeted",
    "existence_shape_authorized_claim_targeted",
    "existence_shape_occurred_claim_targeted",
    "existence_shape_exists_claim_targeted",
    "existence_shape_standing_created_claim_targeted",
    "existence_shape_currentness_created_claim_targeted",
    "existence_shape_authority_created_claim_targeted",
)

BLOCK_CODES = (
    "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_QUESTION_UNDECLARED",
    "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_INTENT_UNSUPPORTED",
    "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_BLOCK_REQUESTED",
    "AFFECTED_FILE_PATH_MISSING",
    "AFFECTED_FILE_UNREADABLE",
    "AFFECTED_FILE_UNSUPPORTED_CLAIM_A_MISSING",
    "AFFECTED_FILE_UNSUPPORTED_CLAIM_B_MISSING",
    "AFFECTED_FILE_DERIVATION_EVENT_RECORDED_CLAIM_MISSING",
    "SEAM_CASE_PATH_MISSING",
    "SEAM_CASE_UNREADABLE",
    "SEAM_CASE_UNSUPPORTED_EXISTENCE_CLAIM_CLASS_MISSING",
    "SEAM_CASE_REPO_PRESENCE_NOT_STANDING_MISSING",
    "SEAM_CASE_CODEX_EXECUTION_NOT_TRUTH_MISSING",
    "SEAM_CASE_OPERATOR_AUTHORIZATION_NOT_SOLE_AUTHORSHIP_MISSING",
    "SEAM_CASE_LATER_RECOGNITION_NOT_UPSTREAM_VALIDITY_MISSING",
    "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_PATH_MISSING",
    "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_UNREADABLE",
    "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_TITLE_MISSING",
    "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_NO_MACHINERY_POSTURE_MISSING",
    "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_NOT_ENFORCED_POSTURE_MISSING",
    "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_EVIDENCE_REQUIREMENT_POSTURE_MISSING",
    "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_OPEN_RESOLVER_CHECKER_MISSING",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_UNSUPPORTED_EXISTENCE_CLAIM_CLASS_REQUIREMENT_ONLY",
    "CHECKER_CREATED",
    "RESOLVER_CREATED",
    "TEST_CREATED",
    "ARTIFACT_CREATED",
    "SCANNER_CREATED",
    "REPOSITORY_SCAN_PERFORMED",
    "VALIDATION_PERFORMED",
    "EVIDENCE_REQUIREMENT_ENFORCED",
    "AFFECTED_FILE_REPAIRED",
    "AFFECTED_FILE_EDITED",
    "AFFECTED_FILE_DELETED",
    "AFFECTED_FILE_OVERWRITTEN",
    "AFFECTED_FILE_INVALIDATED_BY_REPLACEMENT",
    "SEAM_CASE_REPLACED",
    "SEAM_CASE_TREATED_AS_REPAIR",
    "UNSUPPORTED_EXISTENCE_CLAIMS_VALIDATED",
    "DESCENDANT_BODY_A_CREATED",
    "DESCENDANT_BODY_B_CREATED",
    "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED",
    "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED",
    "VALID_DERIVATION_EVENT_RECORDED",
    "BODY_DIVISION_PERFORMED",
    "BODY_COPY_PERFORMED",
    "BODY_DISTINCTION_CREATED",
    "SEPARATE_LINEAGE_RECEIPT_CREATED",
    "SEPARATE_SEALING_CREATED",
    "DESCENDANT_STANDING_CHECK_PERFORMED",
    "STANDING_DESCENDANT_CREATED",
    "FIRST_CROSSING_AUTHORIZED",
    "RELATION_CREATED",
    "FIELD_MACHINERY_CREATED",
    "IAMMAI_SYSTEM_CONTINUATION_REOPENED",
    "FIELD_HANDOFF_REVERSED",
    "RUNTIME_CREATED",
    "API_CREATED",
    "MACHINERY_CREATED",
    "CURRENTNESS_CREATED",
    "AUTHORITY_CREATED",
    "STANDING_CREATED",
    "OUTPUT_AUTHORIZED",
    "ACTION_AUTHORIZED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "SYNCHRONIZATION_AUTHORIZED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "REPO_PRESENCE_TREATED_AS_STANDING",
    "CODEX_EXECUTION_TREATED_AS_TRUTH",
    "OPERATOR_AUTHORIZATION_TREATED_AS_SOLE_AUTHORSHIP",
    "DERIVATIVE_RENDERING_TREATED_AS_STANDING_EVIDENCE",
    "LATER_RECOGNITION_TREATED_AS_UPSTREAM_VALIDITY",
    "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
    "HIDDEN_REPAIR_PERFORMED",
    "SILENT_OVERWRITE_PERFORMED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_REQUEST_UNREADABLE",
)

FALSE_POSTURE_BLOCK_CODES = {
    "evidence_checker_created": "CHECKER_CREATED",
    "checker_created": "CHECKER_CREATED",
    "resolver_created": "RESOLVER_CREATED",
    "test_created": "TEST_CREATED",
    "artifact_created": "ARTIFACT_CREATED",
    "scanner_created": "SCANNER_CREATED",
    "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
    "validation_performed": "VALIDATION_PERFORMED",
    "evidence_requirement_enforced": "EVIDENCE_REQUIREMENT_ENFORCED",
    "affected_file_repaired": "AFFECTED_FILE_REPAIRED",
    "affected_file_edited": "AFFECTED_FILE_EDITED",
    "affected_file_deleted": "AFFECTED_FILE_DELETED",
    "affected_file_overwritten": "AFFECTED_FILE_OVERWRITTEN",
    "affected_file_invalidated_by_replacement": "AFFECTED_FILE_INVALIDATED_BY_REPLACEMENT",
    "seam_case_replaced": "SEAM_CASE_REPLACED",
    "seam_case_treated_as_repair": "SEAM_CASE_TREATED_AS_REPAIR",
    "unsupported_existence_claims_validated": "UNSUPPORTED_EXISTENCE_CLAIMS_VALIDATED",
    "descendant_body_a_created": "DESCENDANT_BODY_A_CREATED",
    "descendant_body_b_created": "DESCENDANT_BODY_B_CREATED",
    "descendant_body_basis_candidate_a_created": "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED",
    "descendant_body_basis_candidate_b_created": "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED",
    "valid_derivation_event_recorded": "VALID_DERIVATION_EVENT_RECORDED",
    "body_division_performed": "BODY_DIVISION_PERFORMED",
    "body_copy_performed": "BODY_COPY_PERFORMED",
    "body_distinction_created": "BODY_DISTINCTION_CREATED",
    "separate_lineage_receipt_created": "SEPARATE_LINEAGE_RECEIPT_CREATED",
    "separate_sealing_created": "SEPARATE_SEALING_CREATED",
    "descendant_standing_check_performed": "DESCENDANT_STANDING_CHECK_PERFORMED",
    "standing_descendant_created": "STANDING_DESCENDANT_CREATED",
    "first_crossing_authorized": "FIRST_CROSSING_AUTHORIZED",
    "relation_created": "RELATION_CREATED",
    "field_machinery_created": "FIELD_MACHINERY_CREATED",
    "iammai_system_continuation_reopened": "IAMMAI_SYSTEM_CONTINUATION_REOPENED",
    "field_handoff_reversed": "FIELD_HANDOFF_REVERSED",
    "runtime_created": "RUNTIME_CREATED",
    "api_created": "API_CREATED",
    "machinery_created": "MACHINERY_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "standing_created": "STANDING_CREATED",
    "output_authorized": "OUTPUT_AUTHORIZED",
    "action_authorized": "ACTION_AUTHORIZED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "synchronization_authorized": "SYNCHRONIZATION_AUTHORIZED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "repo_presence_treated_as_standing": "REPO_PRESENCE_TREATED_AS_STANDING",
    "codex_execution_treated_as_truth": "CODEX_EXECUTION_TREATED_AS_TRUTH",
    "operator_authorization_treated_as_sole_authorship": "OPERATOR_AUTHORIZATION_TREATED_AS_SOLE_AUTHORSHIP",
    "derivative_rendering_treated_as_standing_evidence": "DERIVATIVE_RENDERING_TREATED_AS_STANDING_EVIDENCE",
    "later_recognition_treated_as_upstream_validity": "LATER_RECOGNITION_TREATED_AS_UPSTREAM_VALIDITY",
    "contaminated_lineage_treated_as_clean_basis": "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
    "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
    "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
}

AFFECTED_FILE_MARKERS = (
    (
        "affected_file_contains_candidate_a_created_claim",
        "descendant_body_basis_candidate_a_created = true",
        "AFFECTED_FILE_UNSUPPORTED_CLAIM_A_MISSING",
    ),
    (
        "affected_file_contains_candidate_b_created_claim",
        "descendant_body_basis_candidate_b_created = true",
        "AFFECTED_FILE_UNSUPPORTED_CLAIM_B_MISSING",
    ),
    (
        "affected_file_contains_derivation_event_recorded_claim",
        "descendant_body_basis_derivation_event_recorded = true",
        "AFFECTED_FILE_DERIVATION_EVENT_RECORDED_CLAIM_MISSING",
    ),
)

SEAM_CASE_MARKERS = (
    (
        "seam_case_contains_unsupported_existence_claim_class",
        "contaminated for the unsupported existence-claim class",
        "SEAM_CASE_UNSUPPORTED_EXISTENCE_CLAIM_CLASS_MISSING",
    ),
    (
        "seam_case_contains_repo_presence_not_standing",
        "Repo presence is not standing",
        "SEAM_CASE_REPO_PRESENCE_NOT_STANDING_MISSING",
    ),
    (
        "seam_case_contains_codex_execution_not_truth",
        "Codex execution is not truth",
        "SEAM_CASE_CODEX_EXECUTION_NOT_TRUTH_MISSING",
    ),
    (
        "seam_case_contains_operator_authorization_not_sole_authorship",
        "Operator authorization is not sole authorship",
        "SEAM_CASE_OPERATOR_AUTHORIZATION_NOT_SOLE_AUTHORSHIP_MISSING",
    ),
    (
        "seam_case_contains_later_recognition_not_upstream_validity",
        "Later recognition is not proof of upstream validity",
        "SEAM_CASE_LATER_RECOGNITION_NOT_UPSTREAM_VALIDITY_MISSING",
    ),
)

EVIDENCE_REQUIREMENT_SPEC_MARKERS = (
    (
        "evidence_requirement_boundary_spec_contains_exact_title",
        "Existence Claim Evidence Requirement Boundary V0 Minimum Specification",
        "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_TITLE_MISSING",
    ),
    (
        "evidence_requirement_boundary_spec_states_no_machinery",
        "This boundary does not create evidence-checking machinery",
        "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_NO_MACHINERY_POSTURE_MISSING",
    ),
    (
        "evidence_requirement_boundary_spec_states_rule_not_enforced",
        "This rule is not enforced by this boundary",
        "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_NOT_ENFORCED_POSTURE_MISSING",
    ),
    (
        "evidence_requirement_boundary_spec_states_future_claims_require_evidence",
        "future existence-shaped true claims require separately supported evidence "
        "before they may be treated as standing or clean basis",
        "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_EVIDENCE_REQUIREMENT_POSTURE_MISSING",
    ),
    (
        "evidence_requirement_boundary_spec_leaves_resolver_checker_open",
        "evidence requirement resolver/checker",
        "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_OPEN_RESOLVER_CHECKER_MISSING",
    ),
    (
        "evidence_requirement_boundary_spec_mentions_follow_on_work",
        "follow-on work",
        "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_OPEN_RESOLVER_CHECKER_MISSING",
    ),
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


def _read_text_basis(path_value: Any) -> tuple[bool, str, str | None]:
    try:
        path = _repo_path(path_value)
        return True, path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeDecodeError, TypeError, ValueError) as exc:
        return False, "", f"{type(exc).__name__}: {exc}"


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
            if isinstance(code, str) and code in BLOCK_CODES:
                codes.append(code)
    return codes


def _first_failed_code(checks: Iterable[Mapping[str, Any]]) -> str | None:
    codes = _failed_codes(checks)
    return codes[0] if codes else None


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
        code = FALSE_POSTURE_BLOCK_CODES[key]
        _add_check(
            checks,
            f"top_level_{key}_not_true",
            value is not True,
            "not true",
            value,
            code,
        )


def _basis_from_text(
    *,
    path_value: Any,
    path_missing_code: str,
    unreadable_code: str,
    markers: Iterable[tuple[str, str, str]],
    checks: list[dict[str, Any]],
    section_name: str,
) -> dict[str, Any]:
    path_declared = isinstance(path_value, (str, Path)) and str(path_value).strip() != ""
    _add_check(
        checks,
        f"{section_name}_path_declared",
        path_declared,
        "non-empty path",
        path_value,
        path_missing_code,
    )

    basis: dict[str, Any] = {
        "path": str(path_value) if path_declared else None,
        "readable": False,
        "read_error": None,
    }
    text = ""
    if path_declared:
        readable, text, error = _read_text_basis(path_value)
        basis["readable"] = readable
        basis["read_error"] = error
        basis["resolved_path"] = str(_repo_path(path_value))
        _add_check(
            checks,
            f"{section_name}_readable",
            readable,
            "readable UTF-8 Markdown text",
            "readable" if readable else error,
            unreadable_code,
        )
    else:
        _add_check(
            checks,
            f"{section_name}_readable",
            False,
            "readable UTF-8 Markdown text",
            "path missing",
            unreadable_code,
        )

    for basis_key, marker, code in markers:
        contains = bool(text and marker in text)
        basis[basis_key] = contains
        _add_check(
            checks,
            basis_key,
            contains,
            f"contains marker: {marker}",
            contains,
            code,
        )

    basis["raw_markdown_body_returned"] = False
    return basis


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
    raise ExistenceClaimEvidenceRequirementBoundaryV0MinError(
        f"could not find available output path for {path}"
    )


def _build_boundary_object(
    request: Mapping[str, Any],
    affected_file_basis: Mapping[str, Any],
    seam_case_basis: Mapping[str, Any],
    evidence_requirement_boundary_spec_basis: Mapping[str, Any],
    recorded: bool,
) -> dict[str, Any]:
    boundary: dict[str, Any] = {
        "boundary_id": _json_safe(
            request.get("existence_claim_evidence_requirement_boundary_id")
            or DEFAULT_BOUNDARY_ID
        ),
        "boundary_type": _json_safe(request.get("boundary_type") or BOUNDARY_TYPE),
        "boundary_version": RESULT_VERSION,
        "boundary_scope": _json_safe(request.get("boundary_scope") or BOUNDARY_SCOPE),
        "affected_file_path": _json_safe(request.get("affected_file_path")),
        "seam_case_path": _json_safe(request.get("seam_case_path")),
        "evidence_requirement_boundary_spec_path": _json_safe(
            request.get("evidence_requirement_boundary_spec_path")
        ),
        "affected_file_contains_candidate_a_created_claim": bool(
            affected_file_basis.get("affected_file_contains_candidate_a_created_claim")
        ),
        "affected_file_contains_candidate_b_created_claim": bool(
            affected_file_basis.get("affected_file_contains_candidate_b_created_claim")
        ),
        "affected_file_contains_derivation_event_recorded_claim": bool(
            affected_file_basis.get(
                "affected_file_contains_derivation_event_recorded_claim"
            )
        ),
        "existence_claim_evidence_requirement_boundary_recorded": recorded,
        "unsupported_existence_claim_class_preserved": recorded,
        "future_existence_claims_require_evidence": recorded,
        "affected_file_contamination_preserved": recorded,
        "affected_file_basis_preserved": recorded,
        "seam_case_basis_preserved": recorded,
        "evidence_requirement_boundary_spec_basis_preserved": recorded,
        "future_checker_or_resolver_may_be_considered": recorded,
        "repo_presence_not_standing_preserved": recorded,
        "codex_execution_not_truth_preserved": recorded,
        "operator_authorization_not_sole_authorship_preserved": recorded,
        "later_recognition_not_upstream_validity_preserved": recorded,
        "existence_shape_created_claim_targeted": recorded,
        "existence_shape_recorded_claim_targeted": recorded,
        "existence_shape_performed_claim_targeted": recorded,
        "existence_shape_authorized_claim_targeted": recorded,
        "existence_shape_occurred_claim_targeted": recorded,
        "existence_shape_exists_claim_targeted": recorded,
        "existence_shape_standing_created_claim_targeted": recorded,
        "existence_shape_currentness_created_claim_targeted": recorded,
        "existence_shape_authority_created_claim_targeted": recorded,
    }
    boundary.update(_canonical_non_claims())
    return boundary


def _open_items() -> list[str]:
    return [
        "evidence requirement resolver/checker boundary",
        "evidence requirement resolver/checker",
        "evidence requirement test",
        "evidence requirement artifact",
        "evidence requirement terminal summary",
        "automated repository scan, if ever separately bounded",
        "repair or successor handling of the affected file",
        "descendant-body derivation successor, if ever separately bounded",
        "descendant standing checks",
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


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    affected_file_basis: Mapping[str, Any],
    seam_case_basis: Mapping[str, Any],
    evidence_requirement_boundary_spec_basis: Mapping[str, Any],
    outcome: str,
    recorded: bool,
) -> dict[str, Any]:
    boundary = _build_boundary_object(
        request,
        affected_file_basis,
        seam_case_basis,
        evidence_requirement_boundary_spec_basis,
        recorded,
    )
    failed_code = _first_failed_code(checks)
    failed_checks = [check for check in checks if check.get("passed") is False]
    passed_checks = [check for check in checks if check.get("passed") is True]
    non_claims = _canonical_non_claims()
    statement = {
        "existence_claim_evidence_requirement_boundary_recorded": recorded,
        "unsupported_existence_claim_class_preserved": recorded,
        "future_existence_claims_require_evidence": recorded,
        "affected_file_contamination_preserved": recorded,
        "affected_file_basis_preserved": recorded,
        "seam_case_basis_preserved": recorded,
        "evidence_requirement_boundary_spec_basis_preserved": recorded,
        "future_checker_or_resolver_may_be_considered": recorded,
        "repo_presence_not_standing_preserved": recorded,
        "codex_execution_not_truth_preserved": recorded,
        "operator_authorization_not_sole_authorship_preserved": recorded,
        "later_recognition_not_upstream_validity_preserved": recorded,
        "result_level_non_claims_canonical_false": all(
            value is False for value in non_claims.values()
        ),
    }
    statement.update(non_claims)
    result: dict[str, Any] = {
        "existence_claim_evidence_requirement_boundary_metadata": {
            "existence_claim_evidence_requirement_boundary_id": boundary["boundary_id"],
            "existence_claim_evidence_requirement_boundary_type": BOUNDARY_TYPE,
            "existence_claim_evidence_requirement_boundary_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_existence_claim_evidence_requirement_boundary_question": {
            "existence_claim_evidence_requirement_boundary_id": _json_safe(
                request.get("existence_claim_evidence_requirement_boundary_id")
            ),
            "existence_claim_evidence_requirement_boundary_question": _json_safe(
                request.get("existence_claim_evidence_requirement_boundary_question")
            ),
            "existence_claim_evidence_requirement_boundary_intent": _json_safe(
                request.get("existence_claim_evidence_requirement_boundary_intent")
            ),
            "boundary_type": _json_safe(request.get("boundary_type")),
            "boundary_scope": _json_safe(request.get("boundary_scope")),
            "affected_file_path": _json_safe(request.get("affected_file_path")),
            "seam_case_path": _json_safe(request.get("seam_case_path")),
            "evidence_requirement_boundary_spec_path": _json_safe(
                request.get("evidence_requirement_boundary_spec_path")
            ),
        },
        "affected_file_basis": dict(affected_file_basis),
        "seam_case_basis": dict(seam_case_basis),
        "evidence_requirement_boundary_spec_basis": dict(
            evidence_requirement_boundary_spec_basis
        ),
        "existence_claim_evidence_requirement_boundary": boundary,
        "existence_claim_evidence_requirement_boundary_checks": checks,
        "existence_claim_evidence_requirement_boundary_statement": statement,
        "existence_claim_evidence_requirement_boundary_non_meaning": {
            "not_evidence_checking_machinery": True,
            "not_checker": True,
            "not_repository_scan": True,
            "not_validation": True,
            "not_repair": True,
            "not_descendant_body_work": True,
            "not_runtime": True,
            "not_authority": True,
            "not_currentness": True,
            "not_follow_on_work": True,
        },
        "additional_basis_required": [
            check["check_name"]
            for check in failed_checks
            if str(check.get("failure_code", "")).endswith("MISSING")
            or str(check.get("failure_code", "")).endswith("UNREADABLE")
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
    result["existence_claim_evidence_requirement_boundary_summary"] = (
        build_existence_claim_evidence_requirement_boundary_v0_min_summary(result)
    )
    result["existence_claim_evidence_requirement_boundary_summary"][
        "passed_check_count"
    ] = len(passed_checks)
    result["existence_claim_evidence_requirement_boundary_summary"][
        "failed_check_count"
    ] = len(failed_checks)
    return result


def build_declared_existence_claim_evidence_requirement_boundary_v0_min_request(
    existence_claim_evidence_requirement_boundary_id: str = DEFAULT_BOUNDARY_ID,
    existence_claim_evidence_requirement_boundary_question: str = DEFAULT_QUESTION,
    existence_claim_evidence_requirement_boundary_intent: str = INTENT_RECORD,
    affected_file_path: Path | str = DEFAULT_AFFECTED_FILE_PATH,
    seam_case_path: Path | str = DEFAULT_SEAM_CASE_PATH,
    evidence_requirement_boundary_spec_path: Path | str = (
        DEFAULT_EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_PATH
    ),
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    declared_non_claims: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a bounded default request for this resolver."""

    return {
        "existence_claim_evidence_requirement_boundary_id": (
            existence_claim_evidence_requirement_boundary_id
        ),
        "existence_claim_evidence_requirement_boundary_question": (
            existence_claim_evidence_requirement_boundary_question
        ),
        "existence_claim_evidence_requirement_boundary_intent": (
            existence_claim_evidence_requirement_boundary_intent
        ),
        "affected_file_path": str(affected_file_path),
        "seam_case_path": str(seam_case_path),
        "evidence_requirement_boundary_spec_path": str(
            evidence_requirement_boundary_spec_path
        ),
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "declared_non_claims": (
            dict(declared_non_claims)
            if declared_non_claims is not None
            else _canonical_non_claims()
        ),
    }


def resolve_existence_claim_evidence_requirement_boundary_v0_min(
    declared_existence_claim_evidence_requirement_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one existence-claim evidence requirement boundary request."""

    if declared_existence_claim_evidence_requirement_boundary is None:
        request: dict[str, Any] = (
            build_declared_existence_claim_evidence_requirement_boundary_v0_min_request()
        )
    elif isinstance(declared_existence_claim_evidence_requirement_boundary, MappingABC):
        request = copy.deepcopy(dict(declared_existence_claim_evidence_requirement_boundary))
    else:
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_is_mapping",
            False,
            "mapping",
            type(declared_existence_claim_evidence_requirement_boundary).__name__,
            "DECLARED_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_REQUEST_MALFORMED",
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

    question = request.get("existence_claim_evidence_requirement_boundary_question")
    _add_check(
        checks,
        "boundary_question_declared",
        isinstance(question, str) and question.strip() != "",
        "non-empty boundary question",
        question,
        "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get("existence_claim_evidence_requirement_boundary_intent")
    intent_supported = intent in SUPPORTED_INTENTS
    _add_check(
        checks,
        "boundary_intent_supported",
        intent_supported,
        SUPPORTED_INTENTS,
        intent,
        "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _add_check(
        checks,
        "boundary_block_not_requested",
        intent != INTENT_BLOCK,
        f"intent is not {INTENT_BLOCK}",
        intent,
        "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_BLOCK_REQUESTED",
    )

    affected_file_basis = _basis_from_text(
        path_value=request.get("affected_file_path"),
        path_missing_code="AFFECTED_FILE_PATH_MISSING",
        unreadable_code="AFFECTED_FILE_UNREADABLE",
        markers=AFFECTED_FILE_MARKERS,
        checks=checks,
        section_name="affected_file",
    )
    seam_case_basis = _basis_from_text(
        path_value=request.get("seam_case_path"),
        path_missing_code="SEAM_CASE_PATH_MISSING",
        unreadable_code="SEAM_CASE_UNREADABLE",
        markers=SEAM_CASE_MARKERS,
        checks=checks,
        section_name="seam_case",
    )
    evidence_requirement_boundary_spec_basis = _basis_from_text(
        path_value=request.get("evidence_requirement_boundary_spec_path"),
        path_missing_code="EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_PATH_MISSING",
        unreadable_code="EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_UNREADABLE",
        markers=EVIDENCE_REQUIREMENT_SPEC_MARKERS,
        checks=checks,
        section_name="evidence_requirement_boundary_spec",
    )

    boundary_type = request.get("boundary_type")
    _add_check(
        checks,
        "boundary_type_declared",
        isinstance(boundary_type, str) and boundary_type.strip() != "",
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_MISSING",
    )
    _add_check(
        checks,
        "boundary_type_exact",
        boundary_type == BOUNDARY_TYPE,
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_NOT_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY",
    )

    boundary_scope = request.get("boundary_scope")
    _add_check(
        checks,
        "boundary_scope_declared",
        isinstance(boundary_scope, str) and boundary_scope.strip() != "",
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "boundary_scope_exact",
        boundary_scope == BOUNDARY_SCOPE,
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_NOT_UNSUPPORTED_EXISTENCE_CLAIM_CLASS_REQUIREMENT_ONLY",
    )

    declared_non_claims_ok = _check_declared_non_claims(request, checks)
    _check_top_level_false_postures(request, checks)

    blocking_code_before_positive = _first_failed_code(checks)
    recorded = (
        intent == INTENT_RECORD
        and blocking_code_before_positive is None
        and declared_non_claims_ok
    )
    expected_positive = recorded
    positive_postures = {
        "existence_claim_evidence_requirement_boundary_recorded": recorded,
        "unsupported_existence_claim_class_preserved": recorded,
        "future_existence_claims_require_evidence": recorded,
        "affected_file_contamination_preserved": recorded,
        "affected_file_basis_preserved": recorded,
        "seam_case_basis_preserved": recorded,
        "evidence_requirement_boundary_spec_basis_preserved": recorded,
        "future_checker_or_resolver_may_be_considered": recorded,
    }
    positive_failure_code = blocking_code_before_positive or (
        "DECLARED_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_REQUEST_MALFORMED"
    )
    for posture_name, actual in positive_postures.items():
        _add_check(
            checks,
            posture_name,
            actual is expected_positive,
            expected_positive,
            actual,
            positive_failure_code,
        )

    for key in REQUIRED_FALSE_NON_CLAIMS:
        _add_check(
            checks,
            f"boundary_preserves_{key}_false",
            True,
            False,
            False,
            FALSE_POSTURE_BLOCK_CODES[key],
        )

    canonical_false = all(value is False for value in _canonical_non_claims().values())
    _add_check(
        checks,
        "result_level_required_false_non_claims_canonical_false",
        canonical_false,
        True,
        canonical_false,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _add_check(
        checks,
        "required_non_claims_false",
        declared_non_claims_ok,
        True,
        declared_non_claims_ok,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

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
        affected_file_basis,
        seam_case_basis,
        evidence_requirement_boundary_spec_basis,
        outcome,
        recorded,
    )


def resolve_existence_claim_evidence_requirement_boundary_v0_min_from_path(
    declared_existence_claim_evidence_requirement_boundary_path: Path | str,
) -> dict[str, Any]:
    """Resolve from one declared JSON request path."""

    try:
        path = _repo_path(declared_existence_claim_evidence_requirement_boundary_path)
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
            "DECLARED_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_REQUEST_UNREADABLE",
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
            "DECLARED_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_REQUEST_MALFORMED",
        )
        return _build_result({}, checks, {}, {}, {}, OUTCOME_BLOCKED, False)

    return resolve_existence_claim_evidence_requirement_boundary_v0_min(payload)


def build_existence_claim_evidence_requirement_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a bounded summary without embedding raw Markdown bodies."""

    boundary = result.get("existence_claim_evidence_requirement_boundary")
    if not isinstance(boundary, MappingABC):
        boundary = {}
    checks = result.get("existence_claim_evidence_requirement_boundary_checks")
    if not isinstance(checks, list):
        checks = []
    block = result.get("block")
    if not isinstance(block, MappingABC):
        block = {}
    failed_check_count = sum(1 for check in checks if check.get("passed") is False)
    passed_check_count = sum(1 for check in checks if check.get("passed") is True)
    non_claims = result.get("non_claims")
    non_claims_canonical = isinstance(non_claims, MappingABC) and all(
        non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
    )

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "boundary_id": boundary.get("boundary_id"),
        "question": (
            result.get("declared_existence_claim_evidence_requirement_boundary_question")
            or {}
        ).get("existence_claim_evidence_requirement_boundary_question"),
        "intent": (
            result.get("declared_existence_claim_evidence_requirement_boundary_question")
            or {}
        ).get("existence_claim_evidence_requirement_boundary_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_recorded": boundary.get(
            "existence_claim_evidence_requirement_boundary_recorded", False
        ),
        "affected_file_path": boundary.get("affected_file_path"),
        "seam_case_path": boundary.get("seam_case_path"),
        "evidence_requirement_boundary_spec_path": boundary.get(
            "evidence_requirement_boundary_spec_path"
        ),
        "unsupported_existence_claim_class_preserved": boundary.get(
            "unsupported_existence_claim_class_preserved", False
        ),
        "future_existence_claims_require_evidence": boundary.get(
            "future_existence_claims_require_evidence", False
        ),
        "future_checker_or_resolver_may_be_considered": boundary.get(
            "future_checker_or_resolver_may_be_considered", False
        ),
        "affected_file_contamination_preserved": boundary.get(
            "affected_file_contamination_preserved", False
        ),
        "seam_case_basis_preserved": boundary.get("seam_case_basis_preserved", False),
        "evidence_requirement_boundary_spec_basis_preserved": boundary.get(
            "evidence_requirement_boundary_spec_basis_preserved", False
        ),
        "checker_not_created": boundary.get("checker_created") is False,
        "resolver_not_created": boundary.get("resolver_created") is False,
        "test_not_created": boundary.get("test_created") is False,
        "artifact_not_created": boundary.get("artifact_created") is False,
        "scanner_not_created": boundary.get("scanner_created") is False,
        "repository_scan_not_performed": boundary.get("repository_scan_performed")
        is False,
        "validation_not_performed": boundary.get("validation_performed") is False,
        "evidence_requirement_not_enforced": boundary.get(
            "evidence_requirement_enforced"
        )
        is False,
        "affected_file_not_repaired": boundary.get("affected_file_repaired") is False,
        "affected_file_not_edited": boundary.get("affected_file_edited") is False,
        "affected_file_not_deleted": boundary.get("affected_file_deleted") is False,
        "affected_file_not_overwritten": boundary.get("affected_file_overwritten")
        is False,
        "unsupported_existence_claims_not_validated": boundary.get(
            "unsupported_existence_claims_validated"
        )
        is False,
        "descendant_body_or_candidate_not_created": (
            boundary.get("descendant_body_a_created") is False
            and boundary.get("descendant_body_b_created") is False
            and boundary.get("descendant_body_basis_candidate_a_created") is False
            and boundary.get("descendant_body_basis_candidate_b_created") is False
        ),
        "valid_derivation_event_not_recorded": boundary.get(
            "valid_derivation_event_recorded"
        )
        is False,
        "standing_relation_crossing_runtime_authority_currentness_follow_on_not_created": (
            boundary.get("standing_created") is False
            and boundary.get("relation_created") is False
            and boundary.get("first_crossing_authorized") is False
            and boundary.get("runtime_created") is False
            and boundary.get("authority_created") is False
            and boundary.get("currentness_created") is False
            and boundary.get("follow_on_work_authorized") is False
        ),
        "repo_presence_not_treated_as_standing": boundary.get(
            "repo_presence_treated_as_standing"
        )
        is False,
        "codex_execution_not_treated_as_truth": boundary.get(
            "codex_execution_treated_as_truth"
        )
        is False,
        "operator_authorization_not_treated_as_sole_authorship": boundary.get(
            "operator_authorization_treated_as_sole_authorship"
        )
        is False,
        "derivative_rendering_not_treated_as_standing_evidence": boundary.get(
            "derivative_rendering_treated_as_standing_evidence"
        )
        is False,
        "later_recognition_not_treated_as_upstream_validity": boundary.get(
            "later_recognition_treated_as_upstream_validity"
        )
        is False,
        "contaminated_lineage_not_treated_as_clean_basis": boundary.get(
            "contaminated_lineage_treated_as_clean_basis"
        )
        is False,
        "hidden_repair_not_performed": boundary.get("hidden_repair_performed")
        is False,
        "silent_overwrite_not_performed": boundary.get("silent_overwrite_performed")
        is False,
        "result_level_non_claims_canonical_false": non_claims_canonical,
    }


def write_existence_claim_evidence_requirement_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a stable JSON result without overwriting an existing file."""

    boundary = result.get("existence_claim_evidence_requirement_boundary")
    if not isinstance(boundary, MappingABC):
        boundary_id = DEFAULT_BOUNDARY_ID
    else:
        boundary_id = boundary.get("boundary_id") or DEFAULT_BOUNDARY_ID

    filename = (
        f"{_sanitize_filename(boundary_id)}"
        "__existence_claim_evidence_requirement_boundary_v0_min_result.json"
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
        json.dump(_json_safe(result), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path
