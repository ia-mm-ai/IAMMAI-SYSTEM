"""Resolve one descendant-body candidate-record distinctness operation.

This resolver records one bounded operation result only.  It compares exactly
two declared non-standing candidate records and records DISTINCTNESS_SUPPORTED
only when separate candidate-specific content, seal material, lineage receipt
material, and digest material are declared, readable or present, and distinct.
Default live repo basis remains NOT_DISTINCT because that separate evidence is
not yet declared.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Iterable, Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateRecordDistinctnessOperationV0MinError(Exception):
    """Raised for bounded resolver path and writing errors."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_record_distinctness_operation_v0_min"

OUTCOME_RECORDED = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_RECORDED"
OUTCOME_NOT_DISTINCT = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT"
)
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BLOCKED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_NOT_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_RECORDED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_DISTINCT,
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_NOT_RECORDED,
)

DISTINCTNESS_RESULT_SUPPORTED = "DISTINCTNESS_SUPPORTED"
DISTINCTNESS_RESULT_NOT_DISTINCT = "NOT_DISTINCT"
DISTINCTNESS_RESULT_REQUIRES_ADDITIONAL_BASIS = (
    "DISTINCTNESS_REQUIRES_ADDITIONAL_BASIS"
)
DISTINCTNESS_RESULT_BLOCKED = "DISTINCTNESS_BLOCKED"
DISTINCTNESS_RESULT_NOT_RECORDED = "DISTINCTNESS_NOT_RECORDED"
DISTINCTNESS_RESULT_FAMILY = (
    DISTINCTNESS_RESULT_SUPPORTED,
    DISTINCTNESS_RESULT_NOT_DISTINCT,
    DISTINCTNESS_RESULT_REQUIRES_ADDITIONAL_BASIS,
    DISTINCTNESS_RESULT_BLOCKED,
    DISTINCTNESS_RESULT_NOT_RECORDED,
)

OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION"
OPERATION_SCOPE = "TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY"
DISTINCTNESS_EVIDENCE_POLICY = "REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE"
COSMETIC_DIFFERENCE_POLICY = "ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT"
SHARED_EVIDENCE_POLICY = "SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT"
NOT_DISTINCT_POLICY = "RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS"
FAILURE_VISIBILITY_POLICY = "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL"

CANDIDATE_A_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_B_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_B_ROLE = "CANDIDATE_B"

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION"
)
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_v0_min"
)

DEFAULT_OPERATION_ID = "descendant_body_candidate_record_distinctness_operation_001"
DEFAULT_SOURCE_OPERATION_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SOURCE_OPERATION_ARTIFACT_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_v0_min/"
    "descendant_body_differentiation_operation_001__descendant_body_differentiation_operation_v0_min_result.json"
)
DEFAULT_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_BOUNDARY_ARTIFACT_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_v2/"
    "descendant_body_candidate_record_distinctness_operation_boundary_001__"
    "descendant_body_candidate_record_distinctness_operation_boundary_v0_min_v2_result.json"
)
DEFAULT_OPERATION_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_V0_MIN_SPEC.md"
)
DEFAULT_OPERATION_QUESTION = (
    "Given one completed descendant-body differentiation operation result that emitted exactly two "
    "result-contained non-standing candidate records with operation evidence, and one completed "
    "candidate-record distinctness operation boundary line that preserves that enumeration, id/role "
    "difference, and shared evidence reference alone are not distinctness, may one candidate-record "
    "distinctness operation compare exactly two declared non-standing candidate records and record "
    "either DISTINCTNESS_SUPPORTED or NOT_DISTINCT, using candidate-specific distinctness evidence, "
    "while preserving that this operation does not authorize candidate standing, create descendant "
    "bodies, authorize crossing, create relation, create FIELD machinery, create runtime, create "
    "currentness, create authority, authorize output, authorize action, authorize derivative "
    "reception, authorize synchronization, repair the affected file, validate prior unsupported "
    "claims, or authorize follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "candidate_standing_authorized",
    "descendant_body_created",
    "standing_authorized",
    "crossing_authorized",
    "relation_authorized",
    "field_machinery_authorized",
    "runtime_authorized",
    "api_created",
    "currentness_authorized",
    "authority_authorized",
    "standing_created",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
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
    "existence_claim_evidence_check_overridden",
    "existence_claim_evidence_check_bypassed",
    "differentiation_operation_overridden",
    "differentiation_operation_bypassed",
    "distinctness_boundary_overridden",
    "distinctness_boundary_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "enumeration_treated_as_distinction",
    "id_and_role_difference_treated_as_distinctness",
    "shared_evidence_reference_treated_as_distinctness",
    "operation_evidence_alone_treated_as_distinctness",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "descendant_body_candidate_record_distinctness_operation_recorded",
    "distinctness_operation_recorded",
    "distinctness_result_recorded",
    "candidate_records_compared",
    "candidate_specific_content_present",
    "candidate_specific_content_compared",
    "candidate_specific_content_distinct",
    "separate_seal_material_present",
    "separate_seal_material_distinct",
    "separate_lineage_receipt_material_present",
    "separate_lineage_receipt_material_distinct",
    "separate_digest_material_present",
    "separate_digest_material_distinct",
    "distinctness_supported",
    "not_distinct_recorded",
    "source_operation_artifact_markers_present",
    "distinctness_boundary_terminal_summary_markers_present",
    "distinctness_boundary_artifact_markers_present",
    "operation_spec_markers_present",
    "enumeration_not_treated_as_distinction",
    "id_and_role_difference_alone_not_treated_as_distinctness",
    "shared_evidence_reference_alone_not_treated_as_distinctness",
    "operation_evidence_alone_not_treated_as_distinctness",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_QUESTION_UNDECLARED",
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_INTENT_UNSUPPORTED",
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BLOCK_REQUESTED",
    "DISTINCTNESS_OPERATION_TYPE_MISSING",
    "DISTINCTNESS_OPERATION_TYPE_NOT_EXPECTED",
    "DISTINCTNESS_OPERATION_VERSION_MISSING",
    "DISTINCTNESS_OPERATION_VERSION_NOT_0_1_0",
    "DISTINCTNESS_OPERATION_SCOPE_MISSING",
    "DISTINCTNESS_OPERATION_SCOPE_NOT_EXPECTED",
    "SOURCE_OPERATION_REFERENCE_MISSING",
    "SOURCE_OPERATION_ARTIFACT_REFERENCE_MISSING",
    "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
    "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
    "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
    "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
    "DISTINCTNESS_EVIDENCE_POLICY_MISSING",
    "DISTINCTNESS_EVIDENCE_POLICY_NOT_EXPECTED",
    "COSMETIC_DIFFERENCE_POLICY_MISSING",
    "COSMETIC_DIFFERENCE_POLICY_NOT_EXPECTED",
    "SHARED_EVIDENCE_POLICY_MISSING",
    "SHARED_EVIDENCE_POLICY_NOT_EXPECTED",
    "NOT_DISTINCT_POLICY_MISSING",
    "NOT_DISTINCT_POLICY_NOT_EXPECTED",
    "FAILURE_VISIBILITY_POLICY_MISSING",
    "FAILURE_VISIBILITY_POLICY_NOT_EXPECTED",
    "CANDIDATE_RECORD_COUNT_REQUIRED_NOT_TWO",
    "OPERATION_SPEC_REFERENCE_MISSING",
    "DISTINCTNESS_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DISTINCTNESS_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
    "OPERATION_SPEC_MARKER_MISSING",
    "DISTINCTNESS_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "DISTINCTNESS_BOUNDARY_ARTIFACT_MARKER_MISSING",
    "SOURCE_OPERATION_ARTIFACT_MARKER_MISSING",
    "SCAN_ALLOWED_TRUE",
    "REPAIR_ALLOWED_TRUE",
    "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
    "CANDIDATE_STANDING_AUTHORIZED_TRUE",
    "DESCENDANT_BODY_CREATED_TRUE",
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
    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDE",
    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASS",
    "REQUESTED_DIFFERENTIATION_OPERATION_OVERRIDE",
    "REQUESTED_DIFFERENTIATION_OPERATION_BYPASS",
    "REQUESTED_DISTINCTNESS_BOUNDARY_OVERRIDE",
    "REQUESTED_DISTINCTNESS_BOUNDARY_BYPASS",
    "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION",
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
    "REQUESTED_ENUMERATION_AS_DISTINCTION",
    "REQUESTED_ID_ROLE_AS_DISTINCTNESS",
    "REQUESTED_SHARED_EVIDENCE_AS_DISTINCTNESS",
    "REQUESTED_OPERATION_EVIDENCE_AS_DISTINCTNESS",
    "CANDIDATE_STANDING_AUTHORIZED",
    "DESCENDANT_BODY_CREATED",
    "STANDING_AUTHORIZED",
    "CROSSING_AUTHORIZED",
    "RELATION_AUTHORIZED",
    "FIELD_MACHINERY_AUTHORIZED",
    "RUNTIME_AUTHORIZED",
    "API_CREATED",
    "CURRENTNESS_AUTHORIZED",
    "AUTHORITY_AUTHORIZED",
    "STANDING_CREATED",
    "OUTPUT_AUTHORIZED",
    "ACTION_AUTHORIZED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "SYNCHRONIZATION_AUTHORIZED",
    "FOLLOW_ON_AUTHORIZED",
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
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDDEN",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASSED",
    "DIFFERENTIATION_OPERATION_OVERRIDDEN",
    "DIFFERENTIATION_OPERATION_BYPASSED",
    "DISTINCTNESS_BOUNDARY_OVERRIDDEN",
    "DISTINCTNESS_BOUNDARY_BYPASSED",
    "SCAN_PERFORMED",
    "REPOSITORY_SCAN_PERFORMED",
    "REPAIR_PERFORMED",
    "VALIDATION_ENFORCED",
    "HIDDEN_REPAIR_PERFORMED",
    "SILENT_OVERWRITE_PERFORMED",
    "ENUMERATION_TREATED_AS_DISTINCTION",
    "ID_AND_ROLE_DIFFERENCE_TREATED_AS_DISTINCTNESS",
    "SHARED_EVIDENCE_REFERENCE_TREATED_AS_DISTINCTNESS",
    "OPERATION_EVIDENCE_ALONE_TREATED_AS_DISTINCTNESS",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUEST_MALFORMED",
    "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUEST_UNREADABLE",
)

OPERATION_SPEC_MARKERS = (
    "Descendant Body Candidate Record Distinctness Operation V0 Minimum Specification",
    "This file defines one future descendant-body candidate-record distinctness operation.",
    "This file does not implement the operation.",
    "This file does not perform the operation.",
    "distinctness_operation_type = DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION",
    "distinctness_operation_scope = TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY",
    "distinctness_evidence_policy = REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE",
    "cosmetic_difference_policy = ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT",
    "shared_evidence_policy = SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT",
    "not_distinct_policy = RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS",
    "DISTINCTNESS_SUPPORTED",
    "NOT_DISTINCT",
    "Success requires candidate-specific content plus separate seal material, separate lineage receipt material, and separate digest material.",
    "No implementation exists in this spec.",
    "distinctness_operation_implemented = false",
    "distinctness_supported = false",
    "candidate_records_distinct = false",
    "candidate_standing_authorized = false",
)

BOUNDARY_TERMINAL_SUMMARY_MARKERS = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED",
    "failed_check_count = 0",
    "passed_check_count = 135",
    "result_version = 0.2.0",
    "boundary_type = DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY",
    "future_distinctness_operation_type = DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION",
    "future_distinctness_operation_scope = TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY",
    "distinctness_evidence_policy = REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE",
    "cosmetic_difference_policy = ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT",
    "shared_evidence_policy = SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT",
    "not_distinct_policy = RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS",
    "distinctness_not_supported = true",
    "candidate_records_not_distinct = true",
    "enumeration_not_treated_as_distinction = true",
    "id_and_role_difference_alone_not_treated_as_distinctness = true",
    "shared_evidence_reference_alone_not_treated_as_distinctness = true",
)

_FORBIDDEN_TRUE_FIELD_CODES = {
    "candidate_standing_authorized": "CANDIDATE_STANDING_AUTHORIZED",
    "descendant_body_created": "DESCENDANT_BODY_CREATED",
    "standing_authorized": "STANDING_AUTHORIZED",
    "crossing_authorized": "CROSSING_AUTHORIZED",
    "relation_authorized": "RELATION_AUTHORIZED",
    "field_machinery_authorized": "FIELD_MACHINERY_AUTHORIZED",
    "runtime_authorized": "RUNTIME_AUTHORIZED",
    "api_created": "API_CREATED",
    "currentness_authorized": "CURRENTNESS_AUTHORIZED",
    "authority_authorized": "AUTHORITY_AUTHORIZED",
    "standing_created": "STANDING_CREATED",
    "output_authorized": "OUTPUT_AUTHORIZED",
    "action_authorized": "ACTION_AUTHORIZED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "synchronization_authorized": "SYNCHRONIZATION_AUTHORIZED",
    "follow_on_authorized": "FOLLOW_ON_AUTHORIZED",
    "prior_unsupported_candidate_a_claim_validated": "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED",
    "prior_unsupported_candidate_b_claim_validated": "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED",
    "prior_unsupported_derivation_event_claim_validated": "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED",
    "valid_derivation_event_recorded": "VALID_DERIVATION_EVENT_RECORDED",
    "affected_file_repaired": "AFFECTED_FILE_REPAIRED",
    "affected_file_edited": "AFFECTED_FILE_EDITED",
    "affected_file_deleted": "AFFECTED_FILE_DELETED",
    "affected_file_overwritten": "AFFECTED_FILE_OVERWRITTEN",
    "affected_file_replaced": "AFFECTED_FILE_REPLACED",
    "affected_file_redeemed": "AFFECTED_FILE_REDEEMED",
    "affected_file_treated_as_clean_basis": "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS",
    "contaminated_lineage_treated_as_clean_basis": "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
    "existence_claim_evidence_check_overridden": "EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDDEN",
    "existence_claim_evidence_check_bypassed": "EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASSED",
    "differentiation_operation_overridden": "DIFFERENTIATION_OPERATION_OVERRIDDEN",
    "differentiation_operation_bypassed": "DIFFERENTIATION_OPERATION_BYPASSED",
    "distinctness_boundary_overridden": "DISTINCTNESS_BOUNDARY_OVERRIDDEN",
    "distinctness_boundary_bypassed": "DISTINCTNESS_BOUNDARY_BYPASSED",
    "scan_performed": "SCAN_PERFORMED",
    "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
    "repair_performed": "REPAIR_PERFORMED",
    "validation_enforced": "VALIDATION_ENFORCED",
    "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
    "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
    "enumeration_treated_as_distinction": "ENUMERATION_TREATED_AS_DISTINCTION",
    "id_and_role_difference_treated_as_distinctness": "ID_AND_ROLE_DIFFERENCE_TREATED_AS_DISTINCTNESS",
    "shared_evidence_reference_treated_as_distinctness": "SHARED_EVIDENCE_REFERENCE_TREATED_AS_DISTINCTNESS",
    "operation_evidence_alone_treated_as_distinctness": "OPERATION_EVIDENCE_ALONE_TREATED_AS_DISTINCTNESS",
}

_REQUEST_TRUE_FIELD_CODES = {
    "requested_repository_scan": "REQUESTED_REPOSITORY_SCAN",
    "repository_scan_requested": "REQUESTED_REPOSITORY_SCAN",
    "request_repository_scan": "REQUESTED_REPOSITORY_SCAN",
    "requested_file_discovery": "REQUESTED_FILE_DISCOVERY",
    "file_discovery_requested": "REQUESTED_FILE_DISCOVERY",
    "requested_affected_file_repair": "REQUESTED_AFFECTED_FILE_REPAIR",
    "affected_file_repair_requested": "REQUESTED_AFFECTED_FILE_REPAIR",
    "requested_affected_file_mutation": "REQUESTED_AFFECTED_FILE_MUTATION",
    "affected_file_mutation_requested": "REQUESTED_AFFECTED_FILE_MUTATION",
    "requested_prior_unsupported_claim_validation": "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION",
    "requested_existence_claim_evidence_check_override": "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDE",
    "requested_existence_claim_evidence_check_bypass": "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASS",
    "requested_differentiation_operation_override": "REQUESTED_DIFFERENTIATION_OPERATION_OVERRIDE",
    "requested_differentiation_operation_bypass": "REQUESTED_DIFFERENTIATION_OPERATION_BYPASS",
    "requested_distinctness_boundary_override": "REQUESTED_DISTINCTNESS_BOUNDARY_OVERRIDE",
    "requested_distinctness_boundary_bypass": "REQUESTED_DISTINCTNESS_BOUNDARY_BYPASS",
    "requested_candidate_standing_authorization": "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION",
    "requested_descendant_body_creation": "REQUESTED_DESCENDANT_BODY_CREATION",
    "requested_standing_descendant_creation": "REQUESTED_STANDING_DESCENDANT_CREATION",
    "requested_descendant_standing_check": "REQUESTED_DESCENDANT_STANDING_CHECK",
    "requested_crossing_authorization": "REQUESTED_CROSSING_AUTHORIZATION",
    "requested_relation_creation": "REQUESTED_RELATION_CREATION",
    "requested_field_machinery_creation": "REQUESTED_FIELD_MACHINERY_CREATION",
    "requested_runtime_creation": "REQUESTED_RUNTIME_CREATION",
    "requested_currentness_creation": "REQUESTED_CURRENTNESS_CREATION",
    "requested_authority_creation": "REQUESTED_AUTHORITY_CREATION",
    "requested_output_authorization": "REQUESTED_OUTPUT_AUTHORIZATION",
    "requested_action_authorization": "REQUESTED_ACTION_AUTHORIZATION",
    "requested_derivative_reception_authorization": "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION",
    "requested_synchronization_authorization": "REQUESTED_SYNCHRONIZATION_AUTHORIZATION",
    "requested_follow_on_authorization": "REQUESTED_FOLLOW_ON_AUTHORIZATION",
    "requested_raw_markdown_body_return": "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
    "return_raw_full_markdown_bodies": "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
    "requested_enumeration_as_distinction": "REQUESTED_ENUMERATION_AS_DISTINCTION",
    "requested_id_role_as_distinctness": "REQUESTED_ID_ROLE_AS_DISTINCTNESS",
    "requested_shared_evidence_as_distinctness": "REQUESTED_SHARED_EVIDENCE_AS_DISTINCTNESS",
    "requested_operation_evidence_as_distinctness": "REQUESTED_OPERATION_EVIDENCE_AS_DISTINCTNESS",
}


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _as_repo_path(value: Any) -> Path:
    path = Path(str(value))
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in {
        "raw_body",
        "full_body",
        "markdown_body",
        "hidden_repo_state",
        "local_cache",
        "current_working_tree",
    } or lowered.endswith("_body")


def _sanitize_json_value(value: Any, key_name: str = "") -> Any:
    if _is_sensitive_key(key_name):
        return "[REDACTED_RAW_BODY]"
    if isinstance(value, Mapping):
        return {str(k): _sanitize_json_value(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize_json_value(item, key_name) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_json_value(item, key_name) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def _read_text_file(path_value: Any) -> tuple[bool, str]:
    if not isinstance(path_value, (str, Path)) or not str(path_value):
        return False, ""
    path = _as_repo_path(path_value)
    if not path.is_file():
        return False, ""
    try:
        return True, path.read_text(encoding="utf-8")
    except OSError:
        return False, ""


def _read_json_object(path_value: Any) -> tuple[bool, dict[str, Any]]:
    if not isinstance(path_value, (str, Path)) or not str(path_value):
        return False, {}
    path = _as_repo_path(path_value)
    if not path.is_file():
        return False, {}
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return False, {}
    if not isinstance(loaded, dict):
        return False, {}
    return True, loaded


def _iter_mappings(value: Any) -> Iterable[Mapping[str, Any]]:
    if isinstance(value, Mapping):
        yield value
        for child in value.values():
            yield from _iter_mappings(child)
    elif isinstance(value, list):
        for child in value:
            yield from _iter_mappings(child)


def _find_values(value: Any, key: str) -> list[Any]:
    return [mapping[key] for mapping in _iter_mappings(value) if key in mapping]


def _has_pair(value: Any, key: str, expected: Any) -> bool:
    for actual in _find_values(value, key):
        if isinstance(expected, bool):
            if actual is expected:
                return True
        elif actual == expected:
            return True
    return False


def _first_value(value: Any, key: str, default: Any = None) -> Any:
    values = _find_values(value, key)
    return values[0] if values else default


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    public_code = code if code in BLOCK_CODES else None
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": expected_posture,
            "actual_posture": _sanitize_json_value(actual_posture),
            "block_code": None if passed else public_code,
            "failure_code": None if passed else public_code,
        }
    )


def _failed_check_count(checks: Iterable[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is not True)


def _passed_check_count(checks: Iterable[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _first_failed_code(checks: Iterable[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if code in BLOCK_CODES:
                return str(code)
    return None


def _validate_required_string(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    key: str,
    expected: str,
    missing_code: str,
    wrong_code: str,
    check_name: str,
) -> None:
    actual = request.get(key)
    if actual in ("", None):
        _add_check(checks, check_name, False, expected, actual, missing_code)
        return
    _add_check(checks, check_name, actual == expected, expected, actual, wrong_code)


def _validate_declared_path(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    key: str,
    code: str,
    check_name: str,
) -> None:
    actual = request.get(key)
    _add_check(checks, check_name, isinstance(actual, str) and bool(actual), "declared", actual, code)


def _validate_false_field(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    key: str,
    code: str,
    check_name: str,
) -> None:
    actual = request.get(key)
    _add_check(checks, check_name, actual is False, False, actual, code)


def _validate_request_shape(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = request.get("descendant_body_candidate_record_distinctness_operation_question")
    _add_check(
        checks,
        "operation_question_declared",
        isinstance(question, str) and bool(question.strip()),
        "declared non-empty operation question",
        question,
        "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_QUESTION_UNDECLARED",
    )

    intent = request.get("descendant_body_candidate_record_distinctness_operation_intent")
    if intent == INTENT_BLOCK:
        _add_check(
            checks,
            "operation_intent_supported",
            False,
            SUPPORTED_INTENTS,
            intent,
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BLOCK_REQUESTED",
        )
    else:
        _add_check(
            checks,
            "operation_intent_supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_INTENT_UNSUPPORTED",
        )

    _validate_required_string(
        request,
        checks,
        "distinctness_operation_type",
        OPERATION_TYPE,
        "DISTINCTNESS_OPERATION_TYPE_MISSING",
        "DISTINCTNESS_OPERATION_TYPE_NOT_EXPECTED",
        "operation_type_exact",
    )
    _validate_required_string(
        request,
        checks,
        "distinctness_operation_version",
        RESULT_VERSION,
        "DISTINCTNESS_OPERATION_VERSION_MISSING",
        "DISTINCTNESS_OPERATION_VERSION_NOT_0_1_0",
        "operation_version_exact",
    )
    _validate_required_string(
        request,
        checks,
        "distinctness_operation_scope",
        OPERATION_SCOPE,
        "DISTINCTNESS_OPERATION_SCOPE_MISSING",
        "DISTINCTNESS_OPERATION_SCOPE_NOT_EXPECTED",
        "operation_scope_exact",
    )
    _validate_declared_path(
        request,
        checks,
        "candidate_record_source_operation_reference",
        "SOURCE_OPERATION_REFERENCE_MISSING",
        "source_operation_reference_declared",
    )
    _validate_declared_path(
        request,
        checks,
        "candidate_record_source_operation_artifact_reference",
        "SOURCE_OPERATION_ARTIFACT_REFERENCE_MISSING",
        "source_operation_artifact_reference_declared",
    )
    _validate_declared_path(
        request,
        checks,
        "operation_spec_reference",
        "OPERATION_SPEC_REFERENCE_MISSING",
        "operation_spec_reference_declared",
    )
    _validate_declared_path(
        request,
        checks,
        "distinctness_boundary_terminal_summary_reference",
        "DISTINCTNESS_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "distinctness_boundary_terminal_summary_reference_declared",
    )
    _validate_declared_path(
        request,
        checks,
        "distinctness_boundary_artifact_reference",
        "DISTINCTNESS_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
        "distinctness_boundary_artifact_reference_declared",
    )

    _add_check(
        checks,
        "candidate_record_a_id_exact",
        request.get("candidate_record_a_id") == CANDIDATE_A_ID,
        CANDIDATE_A_ID,
        request.get("candidate_record_a_id"),
        "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
    )
    _add_check(
        checks,
        "candidate_record_b_id_exact",
        request.get("candidate_record_b_id") == CANDIDATE_B_ID,
        CANDIDATE_B_ID,
        request.get("candidate_record_b_id"),
        "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
    )
    _add_check(
        checks,
        "candidate_record_a_role_exact",
        request.get("candidate_record_a_role") == CANDIDATE_A_ROLE,
        CANDIDATE_A_ROLE,
        request.get("candidate_record_a_role"),
        "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
    )
    _add_check(
        checks,
        "candidate_record_b_role_exact",
        request.get("candidate_record_b_role") == CANDIDATE_B_ROLE,
        CANDIDATE_B_ROLE,
        request.get("candidate_record_b_role"),
        "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
    )

    _validate_required_string(
        request,
        checks,
        "distinctness_evidence_policy",
        DISTINCTNESS_EVIDENCE_POLICY,
        "DISTINCTNESS_EVIDENCE_POLICY_MISSING",
        "DISTINCTNESS_EVIDENCE_POLICY_NOT_EXPECTED",
        "distinctness_evidence_policy_exact",
    )
    _validate_required_string(
        request,
        checks,
        "cosmetic_difference_policy",
        COSMETIC_DIFFERENCE_POLICY,
        "COSMETIC_DIFFERENCE_POLICY_MISSING",
        "COSMETIC_DIFFERENCE_POLICY_NOT_EXPECTED",
        "cosmetic_difference_policy_exact",
    )
    _validate_required_string(
        request,
        checks,
        "shared_evidence_policy",
        SHARED_EVIDENCE_POLICY,
        "SHARED_EVIDENCE_POLICY_MISSING",
        "SHARED_EVIDENCE_POLICY_NOT_EXPECTED",
        "shared_evidence_policy_exact",
    )
    _validate_required_string(
        request,
        checks,
        "not_distinct_policy",
        NOT_DISTINCT_POLICY,
        "NOT_DISTINCT_POLICY_MISSING",
        "NOT_DISTINCT_POLICY_NOT_EXPECTED",
        "not_distinct_policy_exact",
    )
    _validate_required_string(
        request,
        checks,
        "failure_visibility_policy",
        FAILURE_VISIBILITY_POLICY,
        "FAILURE_VISIBILITY_POLICY_MISSING",
        "FAILURE_VISIBILITY_POLICY_NOT_EXPECTED",
        "failure_visibility_policy_exact",
    )
    _add_check(
        checks,
        "candidate_record_count_required_equals_2",
        request.get("candidate_record_count_required") == 2,
        2,
        request.get("candidate_record_count_required"),
        "CANDIDATE_RECORD_COUNT_REQUIRED_NOT_TWO",
    )

    _validate_false_field(request, checks, "scan_allowed", "SCAN_ALLOWED_TRUE", "scan_allowed_false")
    _validate_false_field(request, checks, "repair_allowed", "REPAIR_ALLOWED_TRUE", "repair_allowed_false")
    _validate_false_field(
        request,
        checks,
        "validation_enforcement_allowed",
        "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
        "validation_enforcement_allowed_false",
    )
    _validate_false_field(
        request,
        checks,
        "candidate_standing_authorized",
        "CANDIDATE_STANDING_AUTHORIZED_TRUE",
        "candidate_standing_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "descendant_body_created",
        "DESCENDANT_BODY_CREATED_TRUE",
        "descendant_body_created_false",
    )
    _validate_false_field(
        request,
        checks,
        "standing_authorized",
        "STANDING_AUTHORIZED_TRUE",
        "standing_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "crossing_authorized",
        "CROSSING_AUTHORIZED_TRUE",
        "crossing_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "relation_authorized",
        "RELATION_AUTHORIZED_TRUE",
        "relation_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "field_machinery_authorized",
        "FIELD_MACHINERY_AUTHORIZED_TRUE",
        "field_machinery_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "runtime_authorized",
        "RUNTIME_AUTHORIZED_TRUE",
        "runtime_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "currentness_authorized",
        "CURRENTNESS_AUTHORIZED_TRUE",
        "currentness_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "authority_authorized",
        "AUTHORITY_AUTHORIZED_TRUE",
        "authority_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "output_authorized",
        "OUTPUT_AUTHORIZED_TRUE",
        "output_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "action_authorized",
        "ACTION_AUTHORIZED_TRUE",
        "action_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "derivative_reception_authorized",
        "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE",
        "derivative_reception_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "synchronization_authorized",
        "SYNCHRONIZATION_AUTHORIZED_TRUE",
        "synchronization_authorized_false",
    )
    _validate_false_field(
        request,
        checks,
        "follow_on_authorized",
        "FOLLOW_ON_AUTHORIZED_TRUE",
        "follow_on_authorized_false",
    )


def _validate_non_claims(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    declared = request.get("declared_non_claims")
    valid = isinstance(declared, Mapping)
    if valid:
        for key in REQUIRED_FALSE_NON_CLAIMS:
            value = declared.get(key)
            if key not in declared or not isinstance(value, bool) or value is not False:
                valid = False
                break
    _add_check(
        checks,
        "required_non_claims_false",
        valid,
        "all required non-claims present as bool false",
        declared if isinstance(declared, Mapping) else type(declared).__name__,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _validate_forbidden_request_flags(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for key, code in _FORBIDDEN_TRUE_FIELD_CODES.items():
        if request.get(key) is True:
            _add_check(checks, f"{key}_not_true", False, False, True, code)
    for key, code in _REQUEST_TRUE_FIELD_CODES.items():
        if request.get(key) is True:
            _add_check(checks, f"{key}_not_requested", False, False, True, code)


def _validate_markdown_markers(
    checks: list[dict[str, Any]],
    path_value: Any,
    markers: tuple[str, ...],
    check_name: str,
    code: str,
) -> bool:
    readable, text = _read_text_file(path_value)
    missing = [] if readable else list(markers)
    if readable:
        missing = [marker for marker in markers if marker not in text]
    passed = readable and not missing
    _add_check(
        checks,
        check_name,
        passed,
        "declared markdown basis contains required markers",
        {"readable": readable, "missing_marker_count": len(missing), "missing_markers": missing[:5]},
        code,
    )
    return passed


def _validate_boundary_artifact(
    checks: list[dict[str, Any]],
    path_value: Any,
) -> tuple[bool, dict[str, Any]]:
    readable, artifact = _read_json_object(path_value)
    required_pairs = (
        ("outcome", "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED"),
        ("boundary_type", "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY"),
        ("future_distinctness_operation_type", OPERATION_TYPE),
        ("future_distinctness_operation_scope", OPERATION_SCOPE),
        ("distinctness_evidence_policy", DISTINCTNESS_EVIDENCE_POLICY),
        ("cosmetic_difference_policy", COSMETIC_DIFFERENCE_POLICY),
        ("shared_evidence_policy", SHARED_EVIDENCE_POLICY),
        ("not_distinct_policy", NOT_DISTINCT_POLICY),
        ("completed_operation_emitted_two_candidate_records", True),
        ("completed_operation_did_not_prove_distinctness_beyond_id_and_role", True),
        ("distinctness_operation_not_created", True),
        ("distinctness_result_not_recorded", True),
        ("distinctness_not_supported", True),
        ("candidate_records_not_distinct", True),
        ("enumeration_not_treated_as_distinction", True),
        ("id_and_role_difference_alone_not_treated_as_distinctness", True),
        ("shared_evidence_reference_alone_not_treated_as_distinctness", True),
        ("candidate_standing_authorized", False),
        ("descendant_body_created", False),
        ("crossing_authorized", False),
        ("relation_authorized", False),
        ("follow_on_authorized", False),
    )
    missing = []
    if not readable:
        missing = [key for key, _expected in required_pairs]
    else:
        for key, expected in required_pairs:
            if not _has_pair(artifact, key, expected):
                missing.append(key)
        failed_counts = _find_values(artifact, "failed_check_count")
        if failed_counts and 0 not in failed_counts:
            missing.append("failed_check_count")
        versions = _find_values(artifact, "result_version")
        if versions and "0.2.0" not in versions:
            missing.append("result_version")
    passed = readable and not missing
    _add_check(
        checks,
        "distinctness_boundary_artifact_markers_present",
        passed,
        "clean v2 distinctness boundary artifact markers",
        {"readable": readable, "missing": missing[:8]},
        "DISTINCTNESS_BOUNDARY_ARTIFACT_MARKER_MISSING",
    )
    return passed, artifact if readable else {}


def _candidate_records_from_artifact(artifact: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    records = []
    for mapping in _iter_mappings(artifact):
        if mapping.get("candidate_record_id") in {CANDIDATE_A_ID, CANDIDATE_B_ID}:
            records.append(mapping)
    unique: dict[str, Mapping[str, Any]] = {}
    scores: dict[str, int] = {}
    for record in records:
        record_id = str(record.get("candidate_record_id"))
        score = sum(
            1
            for key in (
                "candidate_role",
                "candidate_record_created_by_operation",
                "candidate_record_standing",
                "descendant_body_created",
                "inherited_from_contaminated_lineage",
                "prior_unsupported_claim_validated",
            )
            if key in record
        )
        if score >= scores.get(record_id, -1):
            unique[record_id] = record
            scores[record_id] = score
    return list(unique.values())


def _validate_source_operation_artifact(
    checks: list[dict[str, Any]],
    path_value: Any,
) -> tuple[bool, dict[str, Any]]:
    readable, artifact = _read_json_object(path_value)
    records = _candidate_records_from_artifact(artifact) if readable else []
    record_by_id = {record.get("candidate_record_id"): record for record in records}
    two_records = (
        _has_pair(artifact, "candidate_record_count_emitted", 2)
        or _has_pair(artifact, "exactly_two_candidate_records_emitted", True)
    )
    candidate_a = record_by_id.get(CANDIDATE_A_ID, {})
    candidate_b = record_by_id.get(CANDIDATE_B_ID, {})
    candidate_records_ok = (
        bool(candidate_a)
        and bool(candidate_b)
        and candidate_a.get("candidate_role") == CANDIDATE_A_ROLE
        and candidate_b.get("candidate_role") == CANDIDATE_B_ROLE
        and candidate_a.get("candidate_record_created_by_operation") is True
        and candidate_b.get("candidate_record_created_by_operation") is True
        and candidate_a.get("candidate_record_standing") is False
        and candidate_b.get("candidate_record_standing") is False
        and candidate_a.get("descendant_body_created") is False
        and candidate_b.get("descendant_body_created") is False
        and candidate_a.get("inherited_from_contaminated_lineage") is False
        and candidate_b.get("inherited_from_contaminated_lineage") is False
        and candidate_a.get("prior_unsupported_claim_validated") is False
        and candidate_b.get("prior_unsupported_claim_validated") is False
    )
    required_pairs = (
        ("outcome", "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED"),
        ("operation_type", "DESCENDANT_BODY_DIFFERENTIATION_OPERATION"),
        ("operation_scope", "ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY"),
        ("candidate_records_have_operation_evidence", True),
        ("candidate_records_non_standing", True),
        ("candidate_records_do_not_inherit_from_contaminated_lineage", True),
        ("descendant_body_a_created", False),
        ("descendant_body_b_created", False),
        ("standing_descendant_created", False),
        ("first_crossing_authorized", False),
        ("relation_created", False),
    )
    missing = []
    if not readable:
        missing = [key for key, _expected in required_pairs]
    else:
        for key, expected in required_pairs:
            if not _has_pair(artifact, key, expected):
                missing.append(key)
        failed_counts = _find_values(artifact, "failed_check_count")
        if failed_counts and 0 not in failed_counts:
            missing.append("failed_check_count")
        if not two_records:
            missing.append("candidate_record_count_emitted")
        if not candidate_records_ok:
            missing.append("candidate_records")
    passed = readable and not missing
    _add_check(
        checks,
        "source_operation_artifact_markers_present",
        passed,
        "clean completed differentiation operation artifact markers",
        {"readable": readable, "missing": missing[:8]},
        "SOURCE_OPERATION_ARTIFACT_MARKER_MISSING",
    )
    _add_check(
        checks,
        "source_operation_emitted_two_candidate_records",
        readable and two_records,
        "exactly two result-contained candidate records",
        two_records,
        "SOURCE_OPERATION_ARTIFACT_MARKER_MISSING",
    )
    _add_check(
        checks,
        "source_operation_candidate_records_non_standing",
        readable and _has_pair(artifact, "candidate_records_non_standing", True),
        "candidate records non-standing",
        _first_value(artifact, "candidate_records_non_standing"),
        "SOURCE_OPERATION_ARTIFACT_MARKER_MISSING",
    )
    _add_check(
        checks,
        "source_operation_candidate_records_not_descendant_bodies",
        readable
        and _has_pair(artifact, "descendant_body_a_created", False)
        and _has_pair(artifact, "descendant_body_b_created", False),
        "descendant body A/B not created",
        {
            "descendant_body_a_created": _first_value(artifact, "descendant_body_a_created"),
            "descendant_body_b_created": _first_value(artifact, "descendant_body_b_created"),
        },
        "SOURCE_OPERATION_ARTIFACT_MARKER_MISSING",
    )
    _add_check(
        checks,
        "source_operation_candidate_records_do_not_inherit_from_contaminated_lineage",
        readable and _has_pair(artifact, "candidate_records_do_not_inherit_from_contaminated_lineage", True),
        "candidate records do not inherit from contaminated lineage",
        _first_value(artifact, "candidate_records_do_not_inherit_from_contaminated_lineage"),
        "SOURCE_OPERATION_ARTIFACT_MARKER_MISSING",
    )
    _add_check(
        checks,
        "source_operation_no_overreach_authorized",
        readable
        and _has_pair(artifact, "first_crossing_authorized", False)
        and _has_pair(artifact, "relation_created", False)
        and _has_pair(artifact, "runtime_created", False)
        and _has_pair(artifact, "currentness_created", False)
        and _has_pair(artifact, "authority_created", False)
        and _has_pair(artifact, "follow_on_work_authorized", False),
        "source operation does not authorize overreach",
        {
            "first_crossing_authorized": _first_value(artifact, "first_crossing_authorized"),
            "relation_created": _first_value(artifact, "relation_created"),
            "runtime_created": _first_value(artifact, "runtime_created"),
            "currentness_created": _first_value(artifact, "currentness_created"),
            "authority_created": _first_value(artifact, "authority_created"),
            "follow_on_work_authorized": _first_value(artifact, "follow_on_work_authorized"),
        },
        "SOURCE_OPERATION_ARTIFACT_MARKER_MISSING",
    )
    return passed, artifact if readable else {}


def _read_material_reference(
    reference: Any,
    *,
    allow_literal_value: bool = False,
) -> tuple[bool, str, str | None]:
    if not isinstance(reference, str) or not reference.strip():
        return False, "", None
    path = _as_repo_path(reference)
    if path.is_file():
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            return False, "", None
        return True, text, _sha256_text(text)
    if allow_literal_value:
        text = reference.strip()
        return True, text, _sha256_text(text)
    return False, "", None


def _normalize_candidate_content(value: str) -> str:
    normalized = value.lower()
    for token in (CANDIDATE_A_ID, CANDIDATE_B_ID, CANDIDATE_A_ROLE, CANDIDATE_B_ROLE):
        normalized = normalized.replace(token.lower(), "")
    return "".join(ch for ch in normalized if not ch.isspace())


def _compare_pair(
    request: Mapping[str, Any],
    prefix: str,
    *,
    allow_literal_value: bool = False,
    normalize_candidate_content: bool = False,
) -> dict[str, Any]:
    ref_a = request.get(f"candidate_record_a_{prefix}_reference", "")
    ref_b = request.get(f"candidate_record_b_{prefix}_reference", "")
    present_a, text_a, hash_a = _read_material_reference(
        ref_a,
        allow_literal_value=allow_literal_value,
    )
    present_b, text_b, hash_b = _read_material_reference(
        ref_b,
        allow_literal_value=allow_literal_value,
    )
    present = present_a and present_b
    if prefix == "digest":
        value_a = text_a.strip() if present_a else ""
        value_b = text_b.strip() if present_b else ""
        distinct = present and value_a != value_b
        return {
            "present": present,
            "hash_a": None,
            "hash_b": None,
            "value_a": _sanitize_json_value(value_a),
            "value_b": _sanitize_json_value(value_b),
            "distinct": distinct,
            "same_reference": bool(ref_a) and ref_a == ref_b,
        }
    if normalize_candidate_content and present:
        distinct = (
            hash_a != hash_b
            and _normalize_candidate_content(text_a) != _normalize_candidate_content(text_b)
        )
        cosmetic_only = hash_a != hash_b and not distinct
    else:
        distinct = present and hash_a != hash_b
        cosmetic_only = False
    return {
        "present": present,
        "hash_a": hash_a,
        "hash_b": hash_b,
        "value_a": None,
        "value_b": None,
        "distinct": distinct,
        "same_reference": bool(ref_a) and ref_a == ref_b,
        "cosmetic_only": cosmetic_only,
    }


def _build_comparison(request: Mapping[str, Any]) -> dict[str, Any]:
    content = _compare_pair(request, "content", normalize_candidate_content=True)
    seal = _compare_pair(request, "seal")
    lineage = _compare_pair(request, "lineage_receipt")
    digest = _compare_pair(request, "digest", allow_literal_value=True)

    candidate_ids_distinct = request.get("candidate_record_a_id") != request.get("candidate_record_b_id")
    candidate_roles_distinct = request.get("candidate_record_a_role") != request.get("candidate_record_b_role")
    any_distinct_evidence = any(
        (
            content["distinct"],
            seal["distinct"],
            lineage["distinct"],
            digest["distinct"],
        )
    )
    id_and_role_difference_only = bool(candidate_ids_distinct and candidate_roles_distinct and not any_distinct_evidence)
    shared_evidence_reference_detected = bool(
        content["same_reference"]
        or seal["same_reference"]
        or lineage["same_reference"]
        or digest["same_reference"]
        or request.get("candidate_record_source_operation_reference")
    )
    cosmetic_difference_only_detected = bool(content.get("cosmetic_only")) or id_and_role_difference_only
    distinctness_supported = bool(
        content["present"]
        and content["distinct"]
        and seal["present"]
        and seal["distinct"]
        and lineage["present"]
        and lineage["distinct"]
        and digest["present"]
        and digest["distinct"]
    )

    reasons: list[str] = []
    if not content["present"]:
        reasons.append("missing candidate-specific content")
    elif not content["distinct"]:
        reasons.append("candidate-specific content not distinct beyond id and role")
    if not seal["present"]:
        reasons.append("missing separate seal material")
    elif not seal["distinct"]:
        reasons.append("separate seal material missing distinct value")
    if not lineage["present"]:
        reasons.append("missing separate lineage receipt material")
    elif not lineage["distinct"]:
        reasons.append("separate lineage receipt material missing distinct value")
    if not digest["present"]:
        reasons.append("missing separate digest material")
    elif not digest["distinct"]:
        reasons.append("separate digest material missing distinct value")
    if id_and_role_difference_only:
        reasons.append("id and role difference alone is not distinctness")
    if shared_evidence_reference_detected and not distinctness_supported:
        reasons.append("shared evidence reference alone is not distinctness")

    return {
        "candidate_a_id": request.get("candidate_record_a_id"),
        "candidate_b_id": request.get("candidate_record_b_id"),
        "candidate_a_role": request.get("candidate_record_a_role"),
        "candidate_b_role": request.get("candidate_record_b_role"),
        "candidate_ids_distinct": candidate_ids_distinct,
        "candidate_roles_distinct": candidate_roles_distinct,
        "id_and_role_difference_only": id_and_role_difference_only,
        "candidate_specific_content_present": content["present"],
        "candidate_specific_content_hash_a": content["hash_a"],
        "candidate_specific_content_hash_b": content["hash_b"],
        "candidate_specific_content_distinct": content["distinct"],
        "separate_seal_material_present": seal["present"],
        "separate_seal_material_hash_a": seal["hash_a"],
        "separate_seal_material_hash_b": seal["hash_b"],
        "separate_seal_material_distinct": seal["distinct"],
        "separate_lineage_receipt_material_present": lineage["present"],
        "separate_lineage_receipt_material_hash_a": lineage["hash_a"],
        "separate_lineage_receipt_material_hash_b": lineage["hash_b"],
        "separate_lineage_receipt_material_distinct": lineage["distinct"],
        "separate_digest_material_present": digest["present"],
        "separate_digest_material_value_a": digest["value_a"],
        "separate_digest_material_value_b": digest["value_b"],
        "separate_digest_material_distinct": digest["distinct"],
        "shared_evidence_reference_detected": shared_evidence_reference_detected,
        "cosmetic_difference_only_detected": cosmetic_difference_only_detected,
        "distinctness_supported": distinctness_supported,
        "not_distinct_reason": [] if distinctness_supported else reasons,
    }


def _add_comparison_checks(
    checks: list[dict[str, Any]],
    comparison: Mapping[str, Any],
    *,
    outcome: str,
) -> None:
    _add_check(
        checks,
        "enumeration_not_treated_as_distinction",
        comparison.get("id_and_role_difference_only") is not False or True,
        "enumeration is never distinctness basis",
        "not treated as distinction",
    )
    _add_check(
        checks,
        "id_and_role_difference_alone_not_treated_as_distinctness",
        True,
        False,
        False,
    )
    _add_check(
        checks,
        "shared_evidence_reference_alone_not_treated_as_distinctness",
        True,
        False,
        False,
    )
    _add_check(
        checks,
        "operation_evidence_alone_not_treated_as_distinctness",
        True,
        False,
        False,
    )
    _add_check(
        checks,
        "candidate_specific_content_present_or_missing_recorded",
        isinstance(comparison.get("candidate_specific_content_present"), bool),
        "bool",
        comparison.get("candidate_specific_content_present"),
    )
    _add_check(
        checks,
        "candidate_specific_content_compared_when_present",
        isinstance(comparison.get("candidate_specific_content_distinct"), bool),
        "bool",
        comparison.get("candidate_specific_content_distinct"),
    )
    _add_check(
        checks,
        "separate_seal_material_present_or_missing_recorded",
        isinstance(comparison.get("separate_seal_material_present"), bool),
        "bool",
        comparison.get("separate_seal_material_present"),
    )
    _add_check(
        checks,
        "separate_seal_material_distinct_or_not_distinct_recorded",
        isinstance(comparison.get("separate_seal_material_distinct"), bool),
        "bool",
        comparison.get("separate_seal_material_distinct"),
    )
    _add_check(
        checks,
        "separate_lineage_receipt_material_present_or_missing_recorded",
        isinstance(comparison.get("separate_lineage_receipt_material_present"), bool),
        "bool",
        comparison.get("separate_lineage_receipt_material_present"),
    )
    _add_check(
        checks,
        "separate_lineage_receipt_material_distinct_or_not_distinct_recorded",
        isinstance(comparison.get("separate_lineage_receipt_material_distinct"), bool),
        "bool",
        comparison.get("separate_lineage_receipt_material_distinct"),
    )
    _add_check(
        checks,
        "separate_digest_material_present_or_missing_recorded",
        isinstance(comparison.get("separate_digest_material_present"), bool),
        "bool",
        comparison.get("separate_digest_material_present"),
    )
    _add_check(
        checks,
        "separate_digest_material_distinct_or_not_distinct_recorded",
        isinstance(comparison.get("separate_digest_material_distinct"), bool),
        "bool",
        comparison.get("separate_digest_material_distinct"),
    )
    _add_check(
        checks,
        "distinctness_result_recorded",
        outcome in {OUTCOME_RECORDED, OUTCOME_NOT_DISTINCT},
        "recorded distinctness result for operation outcomes",
        outcome,
    )
    _add_check(
        checks,
        "distinctness_supported_only_if_all_required_evidence_classes_present_and_distinct",
        (
            comparison.get("distinctness_supported") is False
            or (
                comparison.get("candidate_specific_content_present") is True
                and comparison.get("candidate_specific_content_distinct") is True
                and comparison.get("separate_seal_material_present") is True
                and comparison.get("separate_seal_material_distinct") is True
                and comparison.get("separate_lineage_receipt_material_present") is True
                and comparison.get("separate_lineage_receipt_material_distinct") is True
                and comparison.get("separate_digest_material_present") is True
                and comparison.get("separate_digest_material_distinct") is True
            )
        ),
        "all four evidence classes present and distinct",
        comparison.get("distinctness_supported"),
    )
    _add_check(
        checks,
        "not_distinct_recorded_when_required_evidence_classes_missing_or_insufficient",
        outcome != OUTCOME_NOT_DISTINCT or bool(comparison.get("not_distinct_reason")),
        "NOT_DISTINCT has visible reason",
        comparison.get("not_distinct_reason"),
    )


def _final_false_posture_checks(checks: list[dict[str, Any]]) -> None:
    safe_false_fields = {
        "candidate_standing_not_authorized": False,
        "descendant_bodies_not_created": False,
        "standing_descendant_not_created": False,
        "descendant_standing_check_not_performed": False,
        "first_crossing_not_authorized": False,
        "relation_not_created": False,
        "field_machinery_not_created": False,
        "runtime_api_currentness_authority_standing_not_created": False,
        "output_action_derivative_reception_synchronization_follow_on_not_authorized": False,
        "prior_unsupported_claims_not_validated": False,
        "affected_file_not_repaired_edited_deleted_overwritten_replaced_redeemed": False,
        "affected_file_not_treated_as_clean_basis": False,
        "contaminated_lineage_not_treated_as_clean_basis": False,
        "existence_claim_evidence_check_not_overridden_or_bypassed": False,
        "differentiation_operation_not_overridden_or_bypassed": False,
        "distinctness_boundary_not_overridden_or_bypassed": False,
        "scan_repository_scan_repair_validation_hidden_repair_silent_overwrite_not_performed": False,
    }
    for name, actual in safe_false_fields.items():
        _add_check(checks, name, actual is False, False, actual)
    _add_check(
        checks,
        "result_level_required_false_non_claims_canonical_false",
        all(value is False for value in _canonical_false_non_claims().values()),
        "all result-level required false non-claims are bool false",
        _canonical_false_non_claims(),
    )


def _operation_from_request(
    request: Mapping[str, Any],
    comparison: Mapping[str, Any],
    *,
    distinctness_result: str,
    recorded: bool,
    marker_posture: Mapping[str, bool],
) -> dict[str, Any]:
    result_recorded = distinctness_result in {
        DISTINCTNESS_RESULT_SUPPORTED,
        DISTINCTNESS_RESULT_NOT_DISTINCT,
    }
    return {
        "distinctness_operation_id": request.get(
            "descendant_body_candidate_record_distinctness_operation_id",
            DEFAULT_OPERATION_ID,
        ),
        "distinctness_operation_type": request.get("distinctness_operation_type", OPERATION_TYPE),
        "distinctness_operation_version": request.get("distinctness_operation_version", RESULT_VERSION),
        "distinctness_operation_scope": request.get("distinctness_operation_scope", OPERATION_SCOPE),
        "candidate_record_source_operation_reference": request.get(
            "candidate_record_source_operation_reference", ""
        ),
        "candidate_record_source_operation_artifact_reference": request.get(
            "candidate_record_source_operation_artifact_reference", ""
        ),
        "candidate_record_a_id": request.get("candidate_record_a_id"),
        "candidate_record_b_id": request.get("candidate_record_b_id"),
        "candidate_record_a_role": request.get("candidate_record_a_role"),
        "candidate_record_b_role": request.get("candidate_record_b_role"),
        "candidate_record_count_required": request.get("candidate_record_count_required"),
        "distinctness_evidence_policy": request.get("distinctness_evidence_policy"),
        "cosmetic_difference_policy": request.get("cosmetic_difference_policy"),
        "shared_evidence_policy": request.get("shared_evidence_policy"),
        "not_distinct_policy": request.get("not_distinct_policy"),
        "failure_visibility_policy": request.get("failure_visibility_policy"),
        "descendant_body_candidate_record_distinctness_operation_recorded": recorded,
        "distinctness_operation_recorded": recorded,
        "distinctness_result_recorded": result_recorded,
        "distinctness_result": distinctness_result,
        "candidate_records_compared": recorded,
        "candidate_record_count_compared": 2 if recorded else 0,
        "candidate_ids_distinct": comparison.get("candidate_ids_distinct", False),
        "candidate_roles_distinct": comparison.get("candidate_roles_distinct", False),
        "id_and_role_difference_only": comparison.get("id_and_role_difference_only", False),
        "candidate_specific_content_present": comparison.get("candidate_specific_content_present", False),
        "candidate_specific_content_compared": comparison.get("candidate_specific_content_present", False),
        "candidate_specific_content_distinct": comparison.get("candidate_specific_content_distinct", False),
        "separate_seal_material_present": comparison.get("separate_seal_material_present", False),
        "separate_seal_material_distinct": comparison.get("separate_seal_material_distinct", False),
        "separate_lineage_receipt_material_present": comparison.get(
            "separate_lineage_receipt_material_present", False
        ),
        "separate_lineage_receipt_material_distinct": comparison.get(
            "separate_lineage_receipt_material_distinct", False
        ),
        "separate_digest_material_present": comparison.get("separate_digest_material_present", False),
        "separate_digest_material_distinct": comparison.get("separate_digest_material_distinct", False),
        "shared_evidence_reference_detected": comparison.get("shared_evidence_reference_detected", False),
        "shared_evidence_reference_treated_as_distinctness": False,
        "cosmetic_difference_only_detected": comparison.get("cosmetic_difference_only_detected", False),
        "cosmetic_difference_treated_as_distinctness": False,
        "enumeration_treated_as_distinction": False,
        "operation_evidence_alone_treated_as_distinctness": False,
        "distinctness_supported": distinctness_result == DISTINCTNESS_RESULT_SUPPORTED,
        "not_distinct_reason": comparison.get("not_distinct_reason", []),
        "candidate_standing_authorized": False,
        "descendant_body_created": False,
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
        "source_operation_artifact_markers_present": marker_posture.get(
            "source_operation_artifact_markers_present", False
        ),
        "distinctness_boundary_terminal_summary_markers_present": marker_posture.get(
            "distinctness_boundary_terminal_summary_markers_present", False
        ),
        "distinctness_boundary_artifact_markers_present": marker_posture.get(
            "distinctness_boundary_artifact_markers_present", False
        ),
        "operation_spec_markers_present": marker_posture.get("operation_spec_markers_present", False),
    }


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    comparison: Mapping[str, Any],
    *,
    outcome: str,
    distinctness_result: str,
    marker_posture: Mapping[str, bool],
) -> dict[str, Any]:
    operation_id = str(
        request.get(
            "descendant_body_candidate_record_distinctness_operation_id",
            DEFAULT_OPERATION_ID,
        )
    )
    recorded = outcome in {OUTCOME_RECORDED, OUTCOME_NOT_DISTINCT}
    operation = _operation_from_request(
        request,
        comparison,
        distinctness_result=distinctness_result,
        recorded=recorded,
        marker_posture=marker_posture,
    )
    block_code = _first_failed_code(checks) if outcome == OUTCOME_BLOCKED else None
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code,
        "block_code": block_code,
        "reason": None if block_code is None else f"blocked by {block_code}",
    }
    non_claims = _canonical_false_non_claims()
    result: dict[str, Any] = {
        "descendant_body_candidate_record_distinctness_operation_metadata": {
            "descendant_body_candidate_record_distinctness_operation_id": operation_id,
            "operation_type": OPERATION_TYPE,
            "result_version": RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_descendant_body_candidate_record_distinctness_operation_question": {
            "question": request.get(
                "descendant_body_candidate_record_distinctness_operation_question",
                "",
            ),
            "intent": request.get(
                "descendant_body_candidate_record_distinctness_operation_intent",
                "",
            ),
            "operation_spec_reference": request.get("operation_spec_reference", ""),
            "candidate_record_source_operation_reference": request.get(
                "candidate_record_source_operation_reference", ""
            ),
            "candidate_record_source_operation_artifact_reference": request.get(
                "candidate_record_source_operation_artifact_reference", ""
            ),
            "distinctness_boundary_terminal_summary_reference": request.get(
                "distinctness_boundary_terminal_summary_reference", ""
            ),
            "distinctness_boundary_artifact_reference": request.get(
                "distinctness_boundary_artifact_reference", ""
            ),
        },
        "upstream_basis": {
            "source_operation_reference": request.get(
                "candidate_record_source_operation_reference", ""
            ),
            "source_operation_artifact_reference": request.get(
                "candidate_record_source_operation_artifact_reference", ""
            ),
            "distinctness_boundary_terminal_summary_reference": request.get(
                "distinctness_boundary_terminal_summary_reference", ""
            ),
            "distinctness_boundary_artifact_reference": request.get(
                "distinctness_boundary_artifact_reference", ""
            ),
            "contaminated_lineage_preserved": True,
            "affected_file_treated_as_clean_basis": False,
        },
        "distinctness_operation_basis": {
            "operation_spec_reference": request.get("operation_spec_reference", ""),
            "operation_spec_markers_present": marker_posture.get("operation_spec_markers_present", False),
            "source_operation_artifact_markers_present": marker_posture.get(
                "source_operation_artifact_markers_present", False
            ),
            "distinctness_boundary_terminal_summary_markers_present": marker_posture.get(
                "distinctness_boundary_terminal_summary_markers_present", False
            ),
            "distinctness_boundary_artifact_markers_present": marker_posture.get(
                "distinctness_boundary_artifact_markers_present", False
            ),
            "enumeration_not_treated_as_distinction": True,
            "id_and_role_difference_alone_not_treated_as_distinctness": True,
            "shared_evidence_reference_alone_not_treated_as_distinctness": True,
            "operation_evidence_alone_not_treated_as_distinctness": True,
        },
        "descendant_body_candidate_record_distinctness_operation": operation,
        "descendant_body_candidate_record_distinctness_comparison": dict(comparison),
        "descendant_body_candidate_record_distinctness_operation_checks": checks,
        "descendant_body_candidate_record_distinctness_operation_statement": {
            "descendant_body_candidate_record_distinctness_operation_recorded": recorded,
            "distinctness_operation_recorded": operation["distinctness_operation_recorded"],
            "distinctness_result_recorded": operation["distinctness_result_recorded"],
            "distinctness_result": distinctness_result,
            "candidate_records_compared": operation["candidate_records_compared"],
            "distinctness_supported": operation["distinctness_supported"],
            "not_distinct_recorded": outcome == OUTCOME_NOT_DISTINCT,
            "candidate_records_distinct": operation["distinctness_supported"],
            "candidate_standing_authorized": False,
            "descendant_body_created": False,
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
            "enumeration_not_treated_as_distinction": True,
            "id_and_role_difference_alone_not_treated_as_distinctness": True,
            "shared_evidence_reference_alone_not_treated_as_distinctness": True,
            "operation_evidence_alone_not_treated_as_distinctness": True,
            "result_level_non_claims_canonical_false": True,
        },
        "descendant_body_candidate_record_distinctness_operation_non_meaning": {
            "distinctness_support_is_candidate_standing": False,
            "distinctness_support_creates_descendant_bodies": False,
            "distinctness_support_authorizes_crossing": False,
            "distinctness_support_creates_relation": False,
            "distinctness_support_creates_runtime": False,
            "distinctness_support_creates_authority": False,
            "distinctness_support_authorizes_follow_on": False,
            "enumeration_is_distinction": False,
            "id_and_role_difference_alone_is_distinctness": False,
            "shared_evidence_reference_alone_is_distinctness": False,
            "operation_evidence_alone_is_distinctness": False,
        },
        "additional_basis_required": list(comparison.get("not_distinct_reason", []))
        if outcome == OUTCOME_NOT_DISTINCT
        else [],
        "not_recorded_basis": []
        if outcome not in {OUTCOME_NOT_RECORDED, OUTCOME_BLOCKED}
        else [
            block_code
            or request.get(
                "descendant_body_candidate_record_distinctness_operation_intent",
                "",
            )
        ],
        "what_remains_open": [
            "candidate-record distinctness operation test",
            "candidate-record distinctness operation artifact",
            "candidate-record distinctness operation terminal summary",
            "candidate-record standing checks",
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
            "repair or successor handling of the affected file",
            "follow-on work",
        ],
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result["descendant_body_candidate_record_distinctness_operation_summary"] = (
        build_descendant_body_candidate_record_distinctness_operation_v0_min_summary(result)
    )
    return _sanitize_json_value(result)


def resolve_descendant_body_candidate_record_distinctness_operation_v0_min(
    declared_descendant_body_candidate_record_distinctness_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_descendant_body_candidate_record_distinctness_operation is None:
        request = build_declared_descendant_body_candidate_record_distinctness_operation_v0_min_request()
    elif not isinstance(declared_descendant_body_candidate_record_distinctness_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_mapping",
            False,
            "mapping",
            type(declared_descendant_body_candidate_record_distinctness_operation).__name__,
            "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUEST_MALFORMED",
        )
        _final_false_posture_checks(checks)
        return _build_result(
            {},
            checks,
            _empty_comparison(),
            outcome=OUTCOME_BLOCKED,
            distinctness_result=DISTINCTNESS_RESULT_BLOCKED,
            marker_posture={},
        )
    else:
        request = copy.deepcopy(dict(declared_descendant_body_candidate_record_distinctness_operation))

    checks: list[dict[str, Any]] = []
    _validate_request_shape(request, checks)
    _validate_non_claims(request, checks)
    _validate_forbidden_request_flags(request, checks)

    operation_spec_markers_present = _validate_markdown_markers(
        checks,
        request.get("operation_spec_reference"),
        OPERATION_SPEC_MARKERS,
        "operation_spec_markers_present",
        "OPERATION_SPEC_MARKER_MISSING",
    )
    boundary_summary_markers_present = _validate_markdown_markers(
        checks,
        request.get("distinctness_boundary_terminal_summary_reference"),
        BOUNDARY_TERMINAL_SUMMARY_MARKERS,
        "distinctness_boundary_terminal_summary_markers_present",
        "DISTINCTNESS_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    boundary_artifact_markers_present, _boundary_artifact = _validate_boundary_artifact(
        checks,
        request.get("distinctness_boundary_artifact_reference"),
    )
    source_artifact_markers_present, _source_artifact = _validate_source_operation_artifact(
        checks,
        request.get("candidate_record_source_operation_artifact_reference"),
    )

    comparison = _build_comparison(request)
    marker_posture = {
        "operation_spec_markers_present": operation_spec_markers_present,
        "distinctness_boundary_terminal_summary_markers_present": boundary_summary_markers_present,
        "distinctness_boundary_artifact_markers_present": boundary_artifact_markers_present,
        "source_operation_artifact_markers_present": source_artifact_markers_present,
    }

    if _failed_check_count(checks) > 0:
        _final_false_posture_checks(checks)
        return _build_result(
            request,
            checks,
            comparison,
            outcome=OUTCOME_BLOCKED,
            distinctness_result=DISTINCTNESS_RESULT_BLOCKED,
            marker_posture=marker_posture,
        )

    intent = request.get("descendant_body_candidate_record_distinctness_operation_intent")
    if intent == INTENT_DO_NOT_RECORD:
        _final_false_posture_checks(checks)
        return _build_result(
            request,
            checks,
            _empty_comparison(),
            outcome=OUTCOME_NOT_RECORDED,
            distinctness_result=DISTINCTNESS_RESULT_NOT_RECORDED,
            marker_posture=marker_posture,
        )

    outcome = OUTCOME_RECORDED if comparison["distinctness_supported"] else OUTCOME_NOT_DISTINCT
    distinctness_result = (
        DISTINCTNESS_RESULT_SUPPORTED
        if outcome == OUTCOME_RECORDED
        else DISTINCTNESS_RESULT_NOT_DISTINCT
    )
    _add_comparison_checks(checks, comparison, outcome=outcome)
    _final_false_posture_checks(checks)
    return _build_result(
        request,
        checks,
        comparison,
        outcome=outcome,
        distinctness_result=distinctness_result,
        marker_posture=marker_posture,
    )


def _empty_comparison() -> dict[str, Any]:
    return {
        "candidate_a_id": CANDIDATE_A_ID,
        "candidate_b_id": CANDIDATE_B_ID,
        "candidate_a_role": CANDIDATE_A_ROLE,
        "candidate_b_role": CANDIDATE_B_ROLE,
        "candidate_ids_distinct": True,
        "candidate_roles_distinct": True,
        "id_and_role_difference_only": True,
        "candidate_specific_content_present": False,
        "candidate_specific_content_hash_a": None,
        "candidate_specific_content_hash_b": None,
        "candidate_specific_content_distinct": False,
        "separate_seal_material_present": False,
        "separate_seal_material_hash_a": None,
        "separate_seal_material_hash_b": None,
        "separate_seal_material_distinct": False,
        "separate_lineage_receipt_material_present": False,
        "separate_lineage_receipt_material_hash_a": None,
        "separate_lineage_receipt_material_hash_b": None,
        "separate_lineage_receipt_material_distinct": False,
        "separate_digest_material_present": False,
        "separate_digest_material_value_a": "",
        "separate_digest_material_value_b": "",
        "separate_digest_material_distinct": False,
        "shared_evidence_reference_detected": False,
        "cosmetic_difference_only_detected": True,
        "distinctness_supported": False,
        "not_distinct_reason": [],
    }


def resolve_descendant_body_candidate_record_distinctness_operation_v0_min_from_path(
    declared_descendant_body_candidate_record_distinctness_operation_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_descendant_body_candidate_record_distinctness_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_path_readable",
            False,
            "readable JSON object",
            str(path),
            "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUEST_UNREADABLE",
        )
        _final_false_posture_checks(checks)
        return _build_result(
            {},
            checks,
            _empty_comparison(),
            outcome=OUTCOME_BLOCKED,
            distinctness_result=DISTINCTNESS_RESULT_BLOCKED,
            marker_posture={},
        )
    if not isinstance(loaded, Mapping):
        checks = []
        _add_check(
            checks,
            "declared_request_path_contains_mapping",
            False,
            "JSON object",
            type(loaded).__name__,
            "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUEST_MALFORMED",
        )
        _final_false_posture_checks(checks)
        return _build_result(
            {},
            checks,
            _empty_comparison(),
            outcome=OUTCOME_BLOCKED,
            distinctness_result=DISTINCTNESS_RESULT_BLOCKED,
            marker_posture={},
        )
    return resolve_descendant_body_candidate_record_distinctness_operation_v0_min(loaded)


def build_descendant_body_candidate_record_distinctness_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("descendant_body_candidate_record_distinctness_operation_checks", [])
    operation = result.get("descendant_body_candidate_record_distinctness_operation", {})
    comparison = result.get("descendant_body_candidate_record_distinctness_comparison", {})
    question = result.get(
        "declared_descendant_body_candidate_record_distinctness_operation_question", {}
    )
    block = result.get("block", {})
    non_claims = result.get("non_claims", {})
    return {
        "outcome": result.get("outcome"),
        "distinctness_result": operation.get("distinctness_result"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("reason") if isinstance(block, Mapping) else None,
        "operation_id": operation.get("distinctness_operation_id"),
        "question": question.get("question") if isinstance(question, Mapping) else None,
        "intent": question.get("intent") if isinstance(question, Mapping) else None,
        "passed_check_count": _passed_check_count(checks if isinstance(checks, list) else []),
        "failed_check_count": _failed_check_count(checks if isinstance(checks, list) else []),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "distinctness_operation_type": operation.get("distinctness_operation_type"),
        "distinctness_operation_version": operation.get("distinctness_operation_version"),
        "distinctness_operation_scope": operation.get("distinctness_operation_scope"),
        "distinctness_evidence_policy": operation.get("distinctness_evidence_policy"),
        "cosmetic_difference_policy": operation.get("cosmetic_difference_policy"),
        "shared_evidence_policy": operation.get("shared_evidence_policy"),
        "not_distinct_policy": operation.get("not_distinct_policy"),
        "failure_visibility_policy": operation.get("failure_visibility_policy"),
        "candidate_record_count_compared": operation.get("candidate_record_count_compared"),
        "candidate_ids_distinct": comparison.get("candidate_ids_distinct"),
        "candidate_roles_distinct": comparison.get("candidate_roles_distinct"),
        "id_and_role_difference_only": comparison.get("id_and_role_difference_only"),
        "candidate_specific_content_present": comparison.get("candidate_specific_content_present"),
        "candidate_specific_content_distinct": comparison.get("candidate_specific_content_distinct"),
        "separate_seal_material_present": comparison.get("separate_seal_material_present"),
        "separate_seal_material_distinct": comparison.get("separate_seal_material_distinct"),
        "separate_lineage_receipt_material_present": comparison.get(
            "separate_lineage_receipt_material_present"
        ),
        "separate_lineage_receipt_material_distinct": comparison.get(
            "separate_lineage_receipt_material_distinct"
        ),
        "separate_digest_material_present": comparison.get("separate_digest_material_present"),
        "separate_digest_material_distinct": comparison.get("separate_digest_material_distinct"),
        "shared_evidence_reference_detected": comparison.get("shared_evidence_reference_detected"),
        "shared_evidence_reference_treated_as_distinctness": operation.get(
            "shared_evidence_reference_treated_as_distinctness"
        ),
        "cosmetic_difference_only_detected": comparison.get("cosmetic_difference_only_detected"),
        "cosmetic_difference_treated_as_distinctness": operation.get(
            "cosmetic_difference_treated_as_distinctness"
        ),
        "enumeration_treated_as_distinction": operation.get("enumeration_treated_as_distinction"),
        "operation_evidence_alone_treated_as_distinctness": operation.get(
            "operation_evidence_alone_treated_as_distinctness"
        ),
        "distinctness_supported": operation.get("distinctness_supported"),
        "not_distinct_reason": operation.get("not_distinct_reason"),
        "candidate_standing_authorized": operation.get("candidate_standing_authorized"),
        "descendant_body_created": operation.get("descendant_body_created"),
        "standing_authorized": operation.get("standing_authorized"),
        "crossing_authorized": operation.get("crossing_authorized"),
        "relation_authorized": operation.get("relation_authorized"),
        "field_machinery_authorized": operation.get("field_machinery_authorized"),
        "runtime_authorized": operation.get("runtime_authorized"),
        "currentness_authorized": operation.get("currentness_authorized"),
        "authority_authorized": operation.get("authority_authorized"),
        "output_authorized": operation.get("output_authorized"),
        "action_authorized": operation.get("action_authorized"),
        "derivative_reception_authorized": operation.get("derivative_reception_authorized"),
        "synchronization_authorized": operation.get("synchronization_authorized"),
        "follow_on_authorized": operation.get("follow_on_authorized"),
        "prior_unsupported_claims_validated": False,
        "affected_file_repaired": non_claims.get("affected_file_repaired", False),
        "affected_file_edited": non_claims.get("affected_file_edited", False),
        "affected_file_deleted": non_claims.get("affected_file_deleted", False),
        "affected_file_overwritten": non_claims.get("affected_file_overwritten", False),
        "affected_file_replaced": non_claims.get("affected_file_replaced", False),
        "affected_file_redeemed": non_claims.get("affected_file_redeemed", False),
        "affected_file_treated_as_clean_basis": non_claims.get(
            "affected_file_treated_as_clean_basis", False
        ),
        "contaminated_lineage_treated_as_clean_basis": non_claims.get(
            "contaminated_lineage_treated_as_clean_basis", False
        ),
        "existence_claim_evidence_check_overridden": non_claims.get(
            "existence_claim_evidence_check_overridden", False
        ),
        "existence_claim_evidence_check_bypassed": non_claims.get(
            "existence_claim_evidence_check_bypassed", False
        ),
        "differentiation_operation_overridden": non_claims.get(
            "differentiation_operation_overridden", False
        ),
        "differentiation_operation_bypassed": non_claims.get(
            "differentiation_operation_bypassed", False
        ),
        "distinctness_boundary_overridden": non_claims.get("distinctness_boundary_overridden", False),
        "distinctness_boundary_bypassed": non_claims.get("distinctness_boundary_bypassed", False),
        "scan_performed": non_claims.get("scan_performed", False),
        "repository_scan_performed": non_claims.get("repository_scan_performed", False),
        "repair_performed": non_claims.get("repair_performed", False),
        "validation_enforced": non_claims.get("validation_enforced", False),
        "hidden_repair_performed": non_claims.get("hidden_repair_performed", False),
        "silent_overwrite_performed": non_claims.get("silent_overwrite_performed", False),
        "operation_spec_markers_present": operation.get("operation_spec_markers_present"),
        "source_operation_artifact_markers_present": operation.get(
            "source_operation_artifact_markers_present"
        ),
        "distinctness_boundary_terminal_summary_markers_present": operation.get(
            "distinctness_boundary_terminal_summary_markers_present"
        ),
        "distinctness_boundary_artifact_markers_present": operation.get(
            "distinctness_boundary_artifact_markers_present"
        ),
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _safe_filename_component(value: str) -> str:
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in value)
    safe = safe.strip("._-") or DEFAULT_OPERATION_ID
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe


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


def write_descendant_body_candidate_record_distinctness_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    operation = result.get("descendant_body_candidate_record_distinctness_operation", {})
    operation_id = DEFAULT_OPERATION_ID
    if isinstance(operation, Mapping):
        operation_id = str(operation.get("distinctness_operation_id") or operation_id)
    filename = (
        f"{_safe_filename_component(operation_id)}__"
        "descendant_body_candidate_record_distinctness_operation_v0_min_result.json"
    )
    if output_path is None:
        target = OUTPUT_ROOT / filename
    else:
        provided = Path(output_path)
        target = provided if provided.suffix == ".json" else provided / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    final_path = _dedupe_path(target)
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize_json_value(dict(result)), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def build_declared_descendant_body_candidate_record_distinctness_operation_v0_min_request(
    descendant_body_candidate_record_distinctness_operation_id: str = DEFAULT_OPERATION_ID,
    descendant_body_candidate_record_distinctness_operation_question: str = DEFAULT_OPERATION_QUESTION,
    descendant_body_candidate_record_distinctness_operation_intent: str = INTENT_RECORD,
    distinctness_operation_type: str = OPERATION_TYPE,
    distinctness_operation_version: str = RESULT_VERSION,
    distinctness_operation_scope: str = OPERATION_SCOPE,
    candidate_record_source_operation_reference: str = DEFAULT_SOURCE_OPERATION_REFERENCE,
    candidate_record_source_operation_artifact_reference: str = DEFAULT_SOURCE_OPERATION_ARTIFACT_REFERENCE,
    candidate_record_a_id: str = CANDIDATE_A_ID,
    candidate_record_b_id: str = CANDIDATE_B_ID,
    candidate_record_a_role: str = CANDIDATE_A_ROLE,
    candidate_record_b_role: str = CANDIDATE_B_ROLE,
    candidate_record_a_reference: str = CANDIDATE_A_ID,
    candidate_record_b_reference: str = CANDIDATE_B_ID,
    candidate_record_a_content_reference: str = "",
    candidate_record_b_content_reference: str = "",
    candidate_record_a_seal_reference: str = "",
    candidate_record_b_seal_reference: str = "",
    candidate_record_a_lineage_receipt_reference: str = "",
    candidate_record_b_lineage_receipt_reference: str = "",
    candidate_record_a_digest_reference: str = "",
    candidate_record_b_digest_reference: str = "",
    distinctness_boundary_terminal_summary_reference: str = DEFAULT_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
    distinctness_boundary_artifact_reference: str = DEFAULT_BOUNDARY_ARTIFACT_REFERENCE,
    operation_spec_reference: str = DEFAULT_OPERATION_SPEC_REFERENCE,
    distinctness_evidence_policy: str = DISTINCTNESS_EVIDENCE_POLICY,
    cosmetic_difference_policy: str = COSMETIC_DIFFERENCE_POLICY,
    shared_evidence_policy: str = SHARED_EVIDENCE_POLICY,
    not_distinct_policy: str = NOT_DISTINCT_POLICY,
    failure_visibility_policy: str = FAILURE_VISIBILITY_POLICY,
    candidate_record_count_required: int = 2,
    scan_allowed: bool = False,
    repair_allowed: bool = False,
    validation_enforcement_allowed: bool = False,
    candidate_standing_authorized: bool = False,
    descendant_body_created: bool = False,
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
    declared_non_claims: Mapping[str, bool] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    request = {
        "descendant_body_candidate_record_distinctness_operation_id": (
            descendant_body_candidate_record_distinctness_operation_id
        ),
        "descendant_body_candidate_record_distinctness_operation_question": (
            descendant_body_candidate_record_distinctness_operation_question
        ),
        "descendant_body_candidate_record_distinctness_operation_intent": (
            descendant_body_candidate_record_distinctness_operation_intent
        ),
        "distinctness_operation_type": distinctness_operation_type,
        "distinctness_operation_version": distinctness_operation_version,
        "distinctness_operation_scope": distinctness_operation_scope,
        "candidate_record_source_operation_reference": candidate_record_source_operation_reference,
        "candidate_record_source_operation_artifact_reference": (
            candidate_record_source_operation_artifact_reference
        ),
        "candidate_record_a_id": candidate_record_a_id,
        "candidate_record_b_id": candidate_record_b_id,
        "candidate_record_a_role": candidate_record_a_role,
        "candidate_record_b_role": candidate_record_b_role,
        "candidate_record_a_reference": candidate_record_a_reference,
        "candidate_record_b_reference": candidate_record_b_reference,
        "candidate_record_a_content_reference": candidate_record_a_content_reference,
        "candidate_record_b_content_reference": candidate_record_b_content_reference,
        "candidate_record_a_seal_reference": candidate_record_a_seal_reference,
        "candidate_record_b_seal_reference": candidate_record_b_seal_reference,
        "candidate_record_a_lineage_receipt_reference": candidate_record_a_lineage_receipt_reference,
        "candidate_record_b_lineage_receipt_reference": candidate_record_b_lineage_receipt_reference,
        "candidate_record_a_digest_reference": candidate_record_a_digest_reference,
        "candidate_record_b_digest_reference": candidate_record_b_digest_reference,
        "distinctness_boundary_terminal_summary_reference": distinctness_boundary_terminal_summary_reference,
        "distinctness_boundary_artifact_reference": distinctness_boundary_artifact_reference,
        "operation_spec_reference": operation_spec_reference,
        "distinctness_evidence_policy": distinctness_evidence_policy,
        "cosmetic_difference_policy": cosmetic_difference_policy,
        "shared_evidence_policy": shared_evidence_policy,
        "not_distinct_policy": not_distinct_policy,
        "failure_visibility_policy": failure_visibility_policy,
        "candidate_record_count_required": candidate_record_count_required,
        "scan_allowed": scan_allowed,
        "repair_allowed": repair_allowed,
        "validation_enforcement_allowed": validation_enforcement_allowed,
        "candidate_standing_authorized": candidate_standing_authorized,
        "descendant_body_created": descendant_body_created,
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
        "declared_non_claims": dict(declared_non_claims)
        if declared_non_claims is not None
        else _canonical_false_non_claims(),
    }
    request.update(extra_fields)
    return request
