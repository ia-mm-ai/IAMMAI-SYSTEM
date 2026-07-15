"""V2 successor for bounded authored declaration metadata-only receipt.

V1 remains preserved lineage. V2 retains its metadata-only receipt behavior
and blocks any incoming top-level claim that a required-false posture already
exists. Result-level non-claims remain canonical false on every outcome.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min as _v1


class DescendantBodyCandidateAuthoredScopeDivisionDeclarationReceiptOperationV0MinV2Error(Exception):
    """Raised for bounded v2 receipt-operation result writing failures."""


RESULT_VERSION = "0.2.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2"

OPERATION_ID = _v1.OPERATION_ID
OPERATION_TYPE = _v1.OPERATION_TYPE
OPERATION_VERSION = _v1.OPERATION_VERSION
OPERATION_SCOPE = _v1.OPERATION_SCOPE
UPSTREAM_BOUNDARY_TYPE = _v1.UPSTREAM_BOUNDARY_TYPE
UPSTREAM_BOUNDARY_OUTCOME_REQUIRED = _v1.UPSTREAM_BOUNDARY_OUTCOME_REQUIRED
ADMISSIBLE_FUTURE_ROUTE = _v1.ADMISSIBLE_FUTURE_ROUTE
RECEIVED_MATERIAL_TYPE = _v1.RECEIVED_MATERIAL_TYPE
RECEIVED_MATERIAL_EXPECTED_FILENAME = _v1.RECEIVED_MATERIAL_EXPECTED_FILENAME
RECEIVED_MATERIAL_EXPECTED_TITLE = _v1.RECEIVED_MATERIAL_EXPECTED_TITLE
RECEIVED_MATERIAL_EXPECTED_VERSION = _v1.RECEIVED_MATERIAL_EXPECTED_VERSION
RECEIVED_MATERIAL_EXPECTED_DATE = _v1.RECEIVED_MATERIAL_EXPECTED_DATE
RECEIVED_MATERIAL_EXPECTED_AUTHOR = _v1.RECEIVED_MATERIAL_EXPECTED_AUTHOR
RECEIVED_MATERIAL_EXPECTED_SIGNATURE_PRESENT = _v1.RECEIVED_MATERIAL_EXPECTED_SIGNATURE_PRESENT
RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE = _v1.RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE
RECEIVED_MATERIAL_EXPECTED_PREDECESSOR = _v1.RECEIVED_MATERIAL_EXPECTED_PREDECESSOR
RECEIVED_MATERIAL_PREDECESSOR_ROLE = _v1.RECEIVED_MATERIAL_PREDECESSOR_ROLE

OUTCOME_RECORDED = _v1.OUTCOME_RECORDED
OUTCOME_BLOCKED = _v1.OUTCOME_BLOCKED
OUTCOME_NOT_RECORDED = _v1.OUTCOME_NOT_RECORDED
OUTCOME_FAMILY = _v1.OUTCOME_FAMILY

INTENT_RECORD = _v1.INTENT_RECORD
INTENT_DO_NOT_RECORD = _v1.INTENT_DO_NOT_RECORD
INTENT_BLOCK = _v1.INTENT_BLOCK
SUPPORTED_INTENTS = _v1.SUPPORTED_INTENTS

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_"
    "division_declaration_receipt_operation_v0_min_v2"
)
DETERMINISTIC_FILENAME = (
    "descendant_body_candidate_authored_scope_division_declaration_receipt_operation_001"
    "__authored_scope_division_declaration_receipt_operation_v0_min_v2_result.json"
)

DEFAULT_OPERATION_SPEC_REFERENCE = _v1.DEFAULT_OPERATION_SPEC_REFERENCE
DEFAULT_RECEIPT_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = _v1.DEFAULT_RECEIPT_BOUNDARY_TERMINAL_SUMMARY_REFERENCE
DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE
)
DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE
)
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE
)
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE
)
DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE
)

REQUIRED_FALSE_NON_CLAIMS = _v1.REQUIRED_FALSE_NON_CLAIMS
ALLOWED_TRUE_RECORDED_FIELDS = _v1.ALLOWED_TRUE_RECORDED_FIELDS
PROHIBITED_REQUEST_FLAGS = _v1.PROHIBITED_REQUEST_FLAGS
UPSTREAM_REQUIREMENTS = _v1.UPSTREAM_REQUIREMENTS
CUSTODY_POSTURES = _v1.CUSTODY_POSTURES
TEXT_EXTRACTION_POSTURES = _v1.TEXT_EXTRACTION_POSTURES
DIGEST_SCOPE = _v1.DIGEST_SCOPE

PROHIBITED_TOP_LEVEL_POSTURE_REQUESTED = "PROHIBITED_TOP_LEVEL_POSTURE_REQUESTED"
BLOCK_CODES = tuple(dict.fromkeys((*_v1.BLOCK_CODES, PROHIBITED_TOP_LEVEL_POSTURE_REQUESTED)))


def _top_level_true_postures(request: Mapping[str, Any]) -> tuple[str, ...]:
    """Return required-false keys pre-claimed as true by the incoming request."""

    return tuple(key for key in REQUIRED_FALSE_NON_CLAIMS if request.get(key) is True)


def _upgrade_result(result: Mapping[str, Any]) -> dict[str, Any]:
    """Retag a v1-shaped result as the v2 successor without changing posture."""

    upgraded = copy.deepcopy(dict(result))
    metadata = upgraded.get("authored_scope_division_declaration_receipt_operation_metadata")
    if isinstance(metadata, dict):
        metadata["result_version"] = RESULT_VERSION
        metadata["resolver_module"] = RESOLVER_MODULE
    summary = _v1.build_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_summary(upgraded)
    summary["result_version"] = RESULT_VERSION
    summary["resolver_module"] = RESOLVER_MODULE
    upgraded["authored_scope_division_declaration_receipt_operation_summary"] = summary
    return upgraded


def _blocked_top_level_posture_result(request: Mapping[str, Any], keys: tuple[str, ...]) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    for key in keys:
        _v1._add_check(
            checks,
            f"top-level required false posture {key} not pre-claimed",
            False,
            False,
            True,
            PROHIBITED_TOP_LEVEL_POSTURE_REQUESTED,
        )
    result = _v1._blocked_result(
        request,
        checks,
        PROHIBITED_TOP_LEVEL_POSTURE_REQUESTED,
        "incoming request pre-claims one or more required-false postures",
    )
    return _upgrade_result(result)


def build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build a v2 request with v1 metadata-only defaults and no pre-claims."""

    return _v1.build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_request(
        **overrides
    )


def resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(
    declared_authored_scope_division_declaration_receipt_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve metadata-only receipt while rejecting top-level false-posture claims."""

    if declared_authored_scope_division_declaration_receipt_operation is None:
        base_result = _v1.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min()
        return _upgrade_result(base_result)
    if not isinstance(declared_authored_scope_division_declaration_receipt_operation, Mapping):
        base_result = _v1.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(
            declared_authored_scope_division_declaration_receipt_operation
        )
        return _upgrade_result(base_result)

    request = copy.deepcopy(dict(declared_authored_scope_division_declaration_receipt_operation))
    illegal_keys = _top_level_true_postures(request)
    if illegal_keys:
        return _blocked_top_level_posture_result(request, illegal_keys)
    base_result = _v1.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(
        request
    )
    return _upgrade_result(base_result)


def resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_from_path(
    declared_authored_scope_division_declaration_receipt_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one request object and apply v2 top-level posture validation."""

    path = Path(declared_authored_scope_division_declaration_receipt_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError):
        base_result = _v1.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_from_path(
            path
        )
        return _upgrade_result(base_result)
    return resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)


def build_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the v2 compact result summary without raw material content."""

    return _upgrade_result(result)[
        "authored_scope_division_declaration_receipt_operation_summary"
    ]


def write_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write v2 result JSON without silent overwrite or source-material writes."""

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
            json.dump(_v1._json_ready(result), handle, ensure_ascii=True, indent=2, sort_keys=True)
            handle.write("\n")
        return final_path
    except OSError as exc:
        raise DescendantBodyCandidateAuthoredScopeDivisionDeclarationReceiptOperationV0MinV2Error(
            f"WRITE_REFUSED: {exc}"
        ) from exc
