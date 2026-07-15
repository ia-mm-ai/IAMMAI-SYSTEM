"""Resolve the v2 safe-sanitized digest/custody operation result.

This narrow successor preserves the v1 digest/custody resolver's validation,
material streaming, and blocking behavior.  It repairs only v1 result
sanitization so scalar posture values remain scalars in results and writes.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min as _v1


class DescendantBodyCandidateAuthoredScopeDivisionDeclarationDigestCustodyOperationV0MinV2Error(Exception):
    """Raised when a v2 result cannot be written safely."""


DescendantBodyCandidateAuthoredScopeDivisionDeclarationDigestCustodyOperationV0MinError = (
    _v1.DescendantBodyCandidateAuthoredScopeDivisionDeclarationDigestCustodyOperationV0MinError
)


RESULT_VERSION = "0.2.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2"

OPERATION_ID = _v1.OPERATION_ID
OPERATION_TYPE = _v1.OPERATION_TYPE
OPERATION_VERSION = _v1.OPERATION_VERSION
OPERATION_SCOPE = _v1.OPERATION_SCOPE
UPSTREAM_RECEIPT_OPERATION_TYPE = _v1.UPSTREAM_RECEIPT_OPERATION_TYPE
UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED = _v1.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED
UPSTREAM_RECEIPT_STATUS_REQUIRED = _v1.UPSTREAM_RECEIPT_STATUS_REQUIRED
UPSTREAM_AUDIT_OPERATION_TYPE = _v1.UPSTREAM_AUDIT_OPERATION_TYPE
UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED = _v1.UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED
UPSTREAM_AUDIT_RESULT_REQUIRED = _v1.UPSTREAM_AUDIT_RESULT_REQUIRED
UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED = _v1.UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED
TARGET_PRIMARY_MATERIAL_FILENAME = _v1.TARGET_PRIMARY_MATERIAL_FILENAME
TARGET_PRIMARY_MATERIAL_VERSION = _v1.TARGET_PRIMARY_MATERIAL_VERSION
TARGET_PRIMARY_MATERIAL_DATE = _v1.TARGET_PRIMARY_MATERIAL_DATE
TARGET_PRIMARY_MATERIAL_AUTHOR = _v1.TARGET_PRIMARY_MATERIAL_AUTHOR
TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE = _v1.TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE
TARGET_PREDECESSOR_MATERIAL_FILENAME = _v1.TARGET_PREDECESSOR_MATERIAL_FILENAME
TARGET_PREDECESSOR_MATERIAL_ROLE = _v1.TARGET_PREDECESSOR_MATERIAL_ROLE
DIGEST_ALGORITHM_ALLOWED = _v1.DIGEST_ALGORITHM_ALLOWED
CUSTODY_POSTURE_SCOPE = _v1.CUSTODY_POSTURE_SCOPE
ADMISSIBLE_FUTURE_ROUTE = _v1.ADMISSIBLE_FUTURE_ROUTE

OUTCOME_RECORDED = _v1.OUTCOME_RECORDED
OUTCOME_REQUIRES_MATERIAL = _v1.OUTCOME_REQUIRES_MATERIAL
OUTCOME_BLOCKED = _v1.OUTCOME_BLOCKED
OUTCOME_NOT_RECORDED = _v1.OUTCOME_NOT_RECORDED
OUTCOME_FAMILY = _v1.OUTCOME_FAMILY

INTENT_RECORD = _v1.INTENT_RECORD
INTENT_DO_NOT_RECORD = _v1.INTENT_DO_NOT_RECORD
INTENT_BLOCK = _v1.INTENT_BLOCK
SUPPORTED_INTENTS = _v1.SUPPORTED_INTENTS
CUSTODY_POSTURES = _v1.CUSTODY_POSTURES
ALLOWED_TRUE_RECORDED_FIELDS = _v1.ALLOWED_TRUE_RECORDED_FIELDS
REQUIRED_FALSE_NON_CLAIMS = _v1.REQUIRED_FALSE_NON_CLAIMS
BLOCK_CODES = _v1.BLOCK_CODES
PROHIBITED_REQUEST_FLAGS = _v1.PROHIBITED_REQUEST_FLAGS
SENSITIVE_BODY_KEYS = _v1.SENSITIVE_BODY_KEYS
OPERATION_SPEC_MARKER_CLASSES = _v1.OPERATION_SPEC_MARKER_CLASSES
UPSTREAM_REQUIREMENTS = _v1.UPSTREAM_REQUIREMENTS
WHAT_REMAINS_OPEN = _v1.WHAT_REMAINS_OPEN

DEFAULT_OPERATION_SPEC_REFERENCE = _v1.DEFAULT_OPERATION_SPEC_REFERENCE
DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE = _v1.DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE
DEFAULT_AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE = _v1.DEFAULT_AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE
DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = _v1.DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = _v1.DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = _v1.DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = _v1.DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE
DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = _v1.DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE

REPO_ROOT = _v1.REPO_ROOT
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2")
DETERMINISTIC_FILENAME = "descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_001__authored_scope_division_declaration_digest_custody_operation_v0_min_v2_result.json"

OPERATION_OBJECT_KEY = "descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation"
METADATA_KEY = "authored_scope_division_declaration_digest_custody_operation_metadata"
DECLARED_BASIS_KEY = "declared_authored_scope_division_declaration_digest_custody_operation_basis"
CHECKS_KEY = "authored_scope_division_declaration_digest_custody_operation_checks"
SUMMARY_KEY = "authored_scope_division_declaration_digest_custody_operation_summary"

EXPLICIT_BODY_CONTENT_KEYS = frozenset(
    {
        "raw_pdf",
        "raw_pdf_body",
        "raw_material_body",
        "raw_extracted_text",
        "extracted_text",
        "full_text",
        "full_body",
        "source_body",
        "pdf_bytes",
        "file_bytes",
        "binary",
        "payload",
        "pdf_content",
        "file_content",
        "content",
        "text",
        "body",
    }
)
EXTRA_FALSE_ROUTE_KEYS = (
    "raw_pdf_return_route",
    "raw_extracted_text_return_route",
    "copy_pdf_into_repo_route",
)
OPERATION_WRAPPER_FIELDS = frozenset(
    {
        "outcome",
        "block",
        CHECKS_KEY,
        "non_claims",
        SUMMARY_KEY,
        METADATA_KEY,
    }
)


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_explicit_body_content_key(key: str) -> bool:
    return key.lower() in EXPLICIT_BODY_CONTENT_KEYS


def _safe_sanitize(value: Any, key: str = "") -> Any:
    """Redact actual body content while preserving all scalar postures."""

    if isinstance(value, (bytes, bytearray, memoryview)):
        return "[REDACTED_BINARY_CONTENT]"
    if isinstance(value, Mapping):
        return {str(item_key): _safe_sanitize(item, str(item_key)) for item_key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_safe_sanitize(item, key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (bool, int, float)) or value is None:
        return value
    if isinstance(value, str):
        if _is_explicit_body_content_key(key) and value.strip():
            return "[REDACTED_SENSITIVE_BODY]"
        if len(value) > 4096:
            return f"{value[:4096]}...[truncated]"
        return value
    return str(value)


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _safe_mapping(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _normalized_operation(value: Any) -> dict[str, Any]:
    operation = _safe_mapping(value)
    for key in OPERATION_WRAPPER_FIELDS:
        operation.pop(key, None)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        operation[key] = False
    for key in EXTRA_FALSE_ROUTE_KEYS:
        operation[key] = False
    return _safe_sanitize(operation)


def _count_checks(value: Any, passed: bool) -> int:
    if not isinstance(value, list):
        return 0
    return sum(1 for check in value if isinstance(check, Mapping) and check.get("passed") is passed)


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get(OPERATION_OBJECT_KEY)
    op = operation if isinstance(operation, Mapping) else {}
    checks = result.get(CHECKS_KEY)
    upstream = result.get("upstream_basis")
    upstream_map = upstream if isinstance(upstream, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": _count_checks(checks, False),
        "passed_check_count": _count_checks(checks, True),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_id": op.get("operation_id"),
        "operation_type": op.get("operation_type"),
        "operation_version": op.get("operation_version"),
        "operation_scope": op.get("operation_scope"),
        "upstream_receipt_operation_type": op.get("upstream_receipt_operation_type"),
        "upstream_receipt_operation_outcome_required": op.get("upstream_receipt_operation_outcome_required"),
        "upstream_receipt_status_required": op.get("upstream_receipt_status_required"),
        "upstream_audit_operation_type": op.get("upstream_audit_operation_type"),
        "upstream_audit_operation_outcome_required": op.get("upstream_audit_operation_outcome_required"),
        "upstream_audit_result_required": op.get("upstream_audit_result_required"),
        "selected_target_spec_path": upstream_map.get("operation_spec_reference"),
        "completed_receipt_operation_terminal_summary_path": upstream_map.get("receipt_operation_terminal_summary_reference"),
        "completed_audit_operation_terminal_summary_path": upstream_map.get("audit_operation_terminal_summary_reference"),
        "result_level_non_claims_canonical_false": all(
            isinstance(result.get("non_claims"), Mapping)
            and result["non_claims"].get(key) is False
            for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }
    operation_fields = (
        "target_primary_material_filename",
        "target_primary_material_version",
        "target_primary_material_date",
        "target_primary_material_author",
        "target_primary_material_signature_role",
        "target_predecessor_material_filename",
        "target_predecessor_material_role",
        "digest_algorithm",
        "digest_custody_operation_recorded",
        "digest_computed",
        "digest_recorded",
        "custody_posture_recorded",
        "primary_material_digest_recorded",
        "predecessor_material_digest_recorded",
        "primary_material_custody_recorded",
        "predecessor_material_custody_recorded",
        "primary_material_digest_sha256",
        "predecessor_material_digest_sha256",
        "primary_material_custody_posture",
        "predecessor_material_custody_posture",
        *REQUIRED_FALSE_NON_CLAIMS,
        *EXTRA_FALSE_ROUTE_KEYS,
        "target_digest_custody_operation_spec_markers_present",
        *[flag for *_, flag in UPSTREAM_REQUIREMENTS],
    )
    for field in operation_fields:
        summary[field] = op.get(field)
    return _safe_sanitize(summary)


def _normalize_result(core_result: Mapping[str, Any], declared_request: Mapping[str, Any] | None) -> dict[str, Any]:
    result = _safe_mapping(core_result)
    metadata = _safe_mapping(result.get(METADATA_KEY))
    metadata["operation_id"] = OPERATION_ID
    metadata["result_version"] = RESULT_VERSION
    metadata["resolver_module"] = RESOLVER_MODULE
    result[METADATA_KEY] = _safe_sanitize(metadata)
    result["result_version"] = RESULT_VERSION
    result["resolver_module"] = RESOLVER_MODULE

    if declared_request is not None:
        result[DECLARED_BASIS_KEY] = _safe_sanitize(_safe_mapping(declared_request))
    else:
        result[DECLARED_BASIS_KEY] = _safe_sanitize(result.get(DECLARED_BASIS_KEY, {}))

    result[OPERATION_OBJECT_KEY] = _normalized_operation(result.get(OPERATION_OBJECT_KEY))
    result["non_claims"] = _canonical_non_claims()
    for field in (
        "upstream_basis",
        CHECKS_KEY,
        "authored_scope_division_declaration_digest_custody_operation_statement",
        "authored_scope_division_declaration_digest_custody_operation_non_meaning",
        "material_identity",
        "digest_custody_result_detail",
        "permitted_future_route",
        "blocked_routes",
        "what_remains_open",
        "block",
    ):
        if field in result:
            result[field] = _safe_sanitize(result[field])
    result[SUMMARY_KEY] = _build_summary(result)
    return result


def build_declared_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_request(**overrides: Any) -> dict[str, Any]:
    """Build the unchanged bounded v1 request shape for v2 resolution."""

    return _v1.build_declared_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_request(**overrides)


def resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(
    declared_authored_scope_division_declaration_digest_custody_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve v1 semantics and emit only the v2 scalar-preserving result."""

    if declared_authored_scope_division_declaration_digest_custody_operation is None:
        declared_request = build_declared_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_request()
        core_result = _v1.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min(declared_request)
        return _normalize_result(core_result, declared_request)
    if isinstance(declared_authored_scope_division_declaration_digest_custody_operation, Mapping):
        declared_request = _safe_mapping(declared_authored_scope_division_declaration_digest_custody_operation)
        core_result = _v1.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min(declared_request)
        return _normalize_result(core_result, declared_request)
    core_result = _v1.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min(
        declared_authored_scope_division_declaration_digest_custody_operation
    )
    return _normalize_result(core_result, None)


def resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_from_path(
    declared_authored_scope_division_declaration_digest_custody_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one explicit JSON request and resolve it with v2 normalization."""

    path = Path(declared_authored_scope_division_declaration_digest_custody_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            declared_request = json.load(handle)
    except (OSError, json.JSONDecodeError):
        core_result = _v1.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_from_path(path)
        return _normalize_result(core_result, None)
    return resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(declared_request)


def build_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a v2 compact summary with literal boolean false postures."""

    return _build_summary(_normalize_result(result, None))


def write_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_result(
    result: Mapping[str, Any], output_path: Path | str | None = None,
) -> Path:
    """Write normalized v2 JSON without silent overwrite or PDF copying."""

    normalized = _normalize_result(result, None)
    if output_path is None:
        path = REPO_ROOT / OUTPUT_ROOT / DETERMINISTIC_FILENAME
    else:
        candidate = Path(output_path)
        base = candidate if candidate.is_absolute() else REPO_ROOT / candidate
        path = base if base.suffix else base / DETERMINISTIC_FILENAME
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        final_path = path
        suffix = 1
        while final_path.exists():
            final_path = path.with_name(f"{path.stem}_{suffix:03d}{path.suffix}")
            suffix += 1
        with final_path.open("w", encoding="utf-8") as handle:
            json.dump(_json_ready(normalized), handle, ensure_ascii=True, indent=2, sort_keys=True)
            handle.write("\n")
        return final_path
    except OSError as exc:
        raise DescendantBodyCandidateAuthoredScopeDivisionDeclarationDigestCustodyOperationV0MinV2Error(
            f"WRITE_REFUSED: {exc}"
        ) from exc
