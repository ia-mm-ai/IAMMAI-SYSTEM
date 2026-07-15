"""Resolve one existence-claim evidence check.

This resolver records one EXISTENCE_CLAIM_EVIDENCE_CHECK result object only.
It reads one declared Markdown target surface and one declared evidence map,
detects existence-shaped true assignments in that declared surface only, and
records per-claim evidence outcomes plus one file-level clean or
contaminated-class outcome.

It does not scan the repository, discover files, repair or mutate the target
surface, validate unsupported claims by assertion, create descendant-body work,
create derivation, standing, relation, crossing, FIELD machinery, runtime,
authority, currentness, output, action, derivative reception, synchronization,
or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
import re
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class ExistenceClaimEvidenceCheckV0MinError(RuntimeError):
    """Bounded resolver error for request/path/write handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_existence_claim_evidence_check_v0_min"

OUTCOME_RECORDED = "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED"
OUTCOME_NOT_RECORDED = "EXISTENCE_CLAIM_EVIDENCE_CHECK_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "EXISTENCE_CLAIM_EVIDENCE_CHECK_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

PER_CLAIM_OUTCOME_EVIDENCE_SUPPORTED = "EVIDENCE_SUPPORTED"
PER_CLAIM_OUTCOME_UNSUPPORTED = "UNSUPPORTED"
PER_CLAIM_OUTCOME_CLAIM_NOT_APPLICABLE = "CLAIM_NOT_APPLICABLE"
PER_CLAIM_OUTCOME_CLAIM_CHECK_BLOCKED = "CLAIM_CHECK_BLOCKED"
PER_CLAIM_OUTCOME_FAMILY = (
    PER_CLAIM_OUTCOME_EVIDENCE_SUPPORTED,
    PER_CLAIM_OUTCOME_UNSUPPORTED,
    PER_CLAIM_OUTCOME_CLAIM_NOT_APPLICABLE,
    PER_CLAIM_OUTCOME_CLAIM_CHECK_BLOCKED,
)

FILE_OUTCOME_CLEAN = "EXISTENCE_CLAIM_EVIDENCE_CHECK_CLEAN"
FILE_OUTCOME_CONTAMINATED_CLASS = (
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS"
)
FILE_OUTCOME_BLOCKED = "EXISTENCE_CLAIM_EVIDENCE_CHECK_BLOCKED"
FILE_OUTCOME_FAMILY = (
    FILE_OUTCOME_CLEAN,
    FILE_OUTCOME_CONTAMINATED_CLASS,
    FILE_OUTCOME_BLOCKED,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_existence_claim_evidence_check_v0_min"
)

CHECK_TYPE = "EXISTENCE_CLAIM_EVIDENCE_CHECK"
CHECK_SCOPE = "DECLARED_SURFACE_ONLY"
TARGET_SURFACE_KIND = "MARKDOWN"
SUPPORTED_CHECK_TYPE_VALUES = (CHECK_TYPE,)
SUPPORTED_CHECK_SCOPE_VALUES = (CHECK_SCOPE,)
SUPPORTED_TARGET_SURFACE_KIND_VALUES = (TARGET_SURFACE_KIND,)

INTENT_RECORD = "RECORD_EXISTENCE_CLAIM_EVIDENCE_CHECK"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_EXISTENCE_CLAIM_EVIDENCE_CHECK"
INTENT_BLOCK = "BLOCK_EXISTENCE_CLAIM_EVIDENCE_CHECK"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_CHECK_ID = "existence_claim_evidence_check_001"
DEFAULT_TARGET_SURFACE_PATH = (
    "spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md"
)
DEFAULT_CONTAMINATED_LINEAGE_POLICY = "PRESERVE_CONTAMINATION"
DEFAULT_QUESTION = (
    "Given one declared Markdown target surface and one declared evidence map, "
    "may one EXISTENCE_CLAIM_EVIDENCE_CHECK be recorded that detects "
    "existence-shaped true claims and classifies each detected claim as "
    "EVIDENCE_SUPPORTED or UNSUPPORTED according to declared evidence "
    "references, without scanning the repository, discovering files, repairing "
    "the target surface, validating unsupported claims, treating repo presence "
    "as standing, treating Codex execution as truth, treating operator "
    "authorization as sole authorship, treating derivative rendering as "
    "standing evidence, treating later recognition as upstream validity, "
    "treating contaminated lineage as clean basis, creating descendant bodies, "
    "recording derivation, creating standing, creating relation, authorizing "
    "crossing, creating FIELD machinery, creating runtime, creating authority, "
    "creating currentness, authorizing output, authorizing action, authorizing "
    "derivative reception, authorizing synchronization, or authorizing "
    "follow-on work?"
)

SUPPORTED_EVIDENCE_KINDS = (
    "operation_evidence",
    "resolver_evidence",
    "test_evidence",
    "emitted_artifact_evidence",
    "terminal_summary_evidence",
    "prior_standing_basis_evidence",
    "bounded_operator_attested_evidence",
    "negative_seam_case_contamination_evidence",
)

EXISTENCE_TRUE_SUFFIXES = (
    "_created",
    "_recorded",
    "_performed",
    "_authorized",
    "_occurred",
    "_exists",
    "_standing_created",
    "_currentness_created",
    "_authority_created",
)

INSUFFICIENT_EVIDENCE_REFERENCES = {
    "file existence",
    "latest-file posture",
    "latest file posture",
    "repo-local availability",
    "repo local availability",
    "codex execution",
    "summary text",
    "operator authorization",
    "derivative rendering",
    "later convergence",
    "later recognition",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "resolver_created",
    "test_created",
    "artifact_created",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
    "target_surface_repaired",
    "target_surface_edited",
    "target_surface_deleted",
    "target_surface_overwritten",
    "target_surface_invalidated_by_replacement",
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
    "existence_claim_evidence_check_recorded",
    "target_surface_declared",
    "target_surface_readable",
    "target_surface_kind_is_markdown",
    "evidence_map_declared",
    "contaminated_lineage_policy_preserved",
    "detected_claims_extracted",
    "per_claim_outcomes_recorded",
    "file_level_outcome_recorded",
    "unsupported_claims_preserved",
    "contaminated_class_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_QUESTION_UNDECLARED",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_INTENT_UNSUPPORTED",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_BLOCK_REQUESTED",
    "TARGET_SURFACE_PATH_MISSING",
    "TARGET_SURFACE_UNREADABLE",
    "TARGET_SURFACE_KIND_MISSING",
    "TARGET_SURFACE_KIND_NOT_MARKDOWN",
    "EVIDENCE_MAP_MISSING",
    "EVIDENCE_MAP_MALFORMED",
    "CONTAMINATED_LINEAGE_POLICY_MISSING",
    "CHECK_TYPE_MISSING",
    "CHECK_TYPE_NOT_EXISTENCE_CLAIM_EVIDENCE_CHECK",
    "CHECK_SCOPE_MISSING",
    "CHECK_SCOPE_NOT_DECLARED_SURFACE_ONLY",
    "SCAN_ALLOWED_TRUE",
    "REPAIR_ALLOWED_TRUE",
    "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
    "FOLLOW_ON_AUTHORIZED_TRUE",
    "REQUESTED_REPOSITORY_SCAN",
    "REQUESTED_FILE_DISCOVERY",
    "REQUESTED_TARGET_REPAIR",
    "REQUESTED_TARGET_MUTATION",
    "REQUESTED_VALIDATION_ENFORCEMENT",
    "REQUESTED_RAW_TARGET_BODY_RETURN",
    "SCAN_PERFORMED",
    "REPOSITORY_SCAN_PERFORMED",
    "FILE_DISCOVERY_PERFORMED",
    "VALIDATION_ENFORCED",
    "TARGET_SURFACE_REPAIRED",
    "TARGET_SURFACE_EDITED",
    "TARGET_SURFACE_DELETED",
    "TARGET_SURFACE_OVERWRITTEN",
    "TARGET_SURFACE_INVALIDATED_BY_REPLACEMENT",
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
    "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_MALFORMED",
    "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_UNREADABLE",
)

FALSE_POSTURE_BLOCK_CODES = {
    "resolver_created": "RESOLVER_CREATED",
    "test_created": "TEST_CREATED",
    "artifact_created": "ARTIFACT_CREATED",
    "scan_performed": "SCAN_PERFORMED",
    "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
    "file_discovery_performed": "FILE_DISCOVERY_PERFORMED",
    "validation_enforced": "VALIDATION_ENFORCED",
    "target_surface_repaired": "TARGET_SURFACE_REPAIRED",
    "target_surface_edited": "TARGET_SURFACE_EDITED",
    "target_surface_deleted": "TARGET_SURFACE_DELETED",
    "target_surface_overwritten": "TARGET_SURFACE_OVERWRITTEN",
    "target_surface_invalidated_by_replacement": (
        "TARGET_SURFACE_INVALIDATED_BY_REPLACEMENT"
    ),
    "unsupported_existence_claims_validated": (
        "UNSUPPORTED_EXISTENCE_CLAIMS_VALIDATED"
    ),
    "descendant_body_a_created": "DESCENDANT_BODY_A_CREATED",
    "descendant_body_b_created": "DESCENDANT_BODY_B_CREATED",
    "descendant_body_basis_candidate_a_created": (
        "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED"
    ),
    "descendant_body_basis_candidate_b_created": (
        "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED"
    ),
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
    "operator_authorization_treated_as_sole_authorship": (
        "OPERATOR_AUTHORIZATION_TREATED_AS_SOLE_AUTHORSHIP"
    ),
    "derivative_rendering_treated_as_standing_evidence": (
        "DERIVATIVE_RENDERING_TREATED_AS_STANDING_EVIDENCE"
    ),
    "later_recognition_treated_as_upstream_validity": (
        "LATER_RECOGNITION_TREATED_AS_UPSTREAM_VALIDITY"
    ),
    "contaminated_lineage_treated_as_clean_basis": (
        "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS"
    ),
    "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
    "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
}

CLAIM_ASSIGNMENT_RE = re.compile(
    r"`?\b([A-Za-z][A-Za-z0-9_]*)\s*=\s*true\b`?",
    re.IGNORECASE,
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


def _read_text(path_value: Any) -> tuple[bool, str, str | None, str | None]:
    try:
        path = _repo_path(path_value)
        return True, path.read_text(encoding="utf-8"), None, str(path)
    except (OSError, UnicodeDecodeError, TypeError, ValueError) as exc:
        return False, "", f"{type(exc).__name__}: {exc}", None


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


def _truthy_flag(request: Mapping[str, Any], names: Iterable[str]) -> bool:
    return any(request.get(name) is True for name in names)


def _contaminated_policy_treats_as_clean(value: Any) -> bool:
    normalized = str(value or "").lower()
    return "clean" in normalized and "preserve" not in normalized


def _is_existence_claim_key(claim_key: str) -> bool:
    key = claim_key.strip()
    if not key or key.startswith("not_") or "_not_" in key:
        return False
    return any(key.endswith(suffix) for suffix in EXISTENCE_TRUE_SUFFIXES)


def _extract_existence_claims(text: str, source_surface: Any) -> list[dict[str, Any]]:
    detected: list[dict[str, Any]] = []
    seen_keys: set[str] = set()
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in CLAIM_ASSIGNMENT_RE.finditer(line):
            claim_key = match.group(1)
            if not _is_existence_claim_key(claim_key):
                continue
            if claim_key in seen_keys:
                continue
            seen_keys.add(claim_key)
            detected.append(
                {
                    "claim_key": claim_key,
                    "claim_value": True,
                    "claim_source_surface": str(source_surface),
                    "line_number": line_number,
                    "raw_claim_snippet": line.strip(),
                }
            )
    return detected


def _as_string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value if str(item).strip()]
    return [str(value)]


def _normalize_evidence_map(
    evidence_map: Any,
) -> tuple[bool, dict[str, dict[str, Any]], dict[str, Any]]:
    entries_by_key: dict[str, dict[str, Any]] = {}
    malformed_count = 0
    entry_count = 0

    if not isinstance(evidence_map, (MappingABC, list, tuple)):
        return False, entries_by_key, {
            "entry_count": 0,
            "malformed_entry_count": 0,
            "normalized_claim_keys": [],
        }

    if isinstance(evidence_map, MappingABC) and (
        "claim_key" in evidence_map or "evidence_kind" in evidence_map
    ):
        raw_entries: list[Any] = [evidence_map]
    elif isinstance(evidence_map, MappingABC):
        raw_entries = []
        for claim_key, entry in evidence_map.items():
            if isinstance(entry, MappingABC):
                normalized_entry = dict(entry)
                normalized_entry.setdefault("claim_key", str(claim_key))
                raw_entries.append(normalized_entry)
            else:
                raw_entries.append(
                    {
                        "claim_key": str(claim_key),
                        "malformed": True,
                        "malformed_reason": "evidence entry is not a mapping",
                    }
                )
    else:
        raw_entries = list(evidence_map)

    for raw_entry in raw_entries:
        entry_count += 1
        if not isinstance(raw_entry, MappingABC):
            malformed_count += 1
            continue
        entry = dict(raw_entry)
        claim_key = str(entry.get("claim_key") or "").strip()
        if not claim_key:
            malformed_count += 1
            continue
        malformed = bool(entry.get("malformed"))
        if malformed:
            malformed_count += 1
        equivalent_keys = _as_string_list(entry.get("equivalent_claim_keys"))
        normalized = {
            "claim_key": claim_key,
            "equivalent_claim_keys": equivalent_keys,
            "evidence_kind": entry.get("evidence_kind"),
            "evidence_reference": entry.get("evidence_reference"),
            "evidence_scope": entry.get("evidence_scope"),
            "evidence_target": entry.get("evidence_target"),
            "evidence_note": entry.get("evidence_note"),
            "malformed": malformed,
            "malformed_reason": entry.get("malformed_reason"),
        }
        entries_by_key[claim_key] = normalized
        for equivalent_key in equivalent_keys:
            entries_by_key[equivalent_key] = normalized

    basis = {
        "entry_count": entry_count,
        "malformed_entry_count": malformed_count,
        "normalized_claim_keys": sorted(entries_by_key.keys()),
    }
    return True, entries_by_key, basis


def _is_insufficient_evidence_reference(value: Any) -> bool:
    normalized = str(value or "").strip().lower()
    return normalized in INSUFFICIENT_EVIDENCE_REFERENCES


def _classify_claim(
    claim: Mapping[str, Any],
    evidence_entries: Mapping[str, Mapping[str, Any]],
    contaminated_lineage_as_clean: bool,
    blocked: bool,
) -> dict[str, Any]:
    claim_key = str(claim.get("claim_key") or "")
    if blocked:
        return {
            "claim_key": claim_key,
            "claim_value": claim.get("claim_value"),
            "claim_source_surface": claim.get("claim_source_surface"),
            "evidence_kind": None,
            "evidence_reference": None,
            "evidence_adequacy": False,
            "per_claim_outcome": PER_CLAIM_OUTCOME_CLAIM_CHECK_BLOCKED,
            "unsupported_reason": "CLAIM_CHECK_BLOCKED",
        }

    entry = evidence_entries.get(claim_key)
    if entry is None:
        return {
            "claim_key": claim_key,
            "claim_value": claim.get("claim_value"),
            "claim_source_surface": claim.get("claim_source_surface"),
            "evidence_kind": None,
            "evidence_reference": None,
            "evidence_adequacy": False,
            "per_claim_outcome": PER_CLAIM_OUTCOME_UNSUPPORTED,
            "unsupported_reason": "NO_MATCHING_EVIDENCE_ENTRY",
        }

    evidence_kind = entry.get("evidence_kind")
    evidence_reference = entry.get("evidence_reference")
    reason = None
    if entry.get("malformed"):
        reason = "MALFORMED_EVIDENCE_ENTRY"
    elif evidence_kind not in SUPPORTED_EVIDENCE_KINDS:
        reason = "EVIDENCE_KIND_MISSING_OR_UNSUPPORTED"
    elif not isinstance(evidence_reference, str) or not evidence_reference.strip():
        reason = "EVIDENCE_REFERENCE_MISSING"
    elif evidence_kind == "negative_seam_case_contamination_evidence":
        reason = "NEGATIVE_SEAM_CASE_CONTAMINATION_ONLY"
    elif _is_insufficient_evidence_reference(evidence_reference):
        reason = "EVIDENCE_REFERENCE_INSUFFICIENT_BY_ITSELF"
    elif contaminated_lineage_as_clean:
        reason = "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS"

    if reason is not None:
        return {
            "claim_key": claim_key,
            "claim_value": claim.get("claim_value"),
            "claim_source_surface": claim.get("claim_source_surface"),
            "evidence_kind": evidence_kind,
            "evidence_reference": evidence_reference,
            "evidence_adequacy": False,
            "per_claim_outcome": PER_CLAIM_OUTCOME_UNSUPPORTED,
            "unsupported_reason": reason,
        }

    return {
        "claim_key": claim_key,
        "claim_value": claim.get("claim_value"),
        "claim_source_surface": claim.get("claim_source_surface"),
        "evidence_kind": evidence_kind,
        "evidence_reference": evidence_reference,
        "evidence_adequacy": True,
        "per_claim_outcome": PER_CLAIM_OUTCOME_EVIDENCE_SUPPORTED,
        "unsupported_reason": None,
    }


def _file_level_outcome(
    per_claim_outcomes: Iterable[Mapping[str, Any]], blocked: bool
) -> str:
    if blocked:
        return FILE_OUTCOME_BLOCKED
    for outcome in per_claim_outcomes:
        if outcome.get("per_claim_outcome") == PER_CLAIM_OUTCOME_UNSUPPORTED:
            return FILE_OUTCOME_CONTAMINATED_CLASS
    return FILE_OUTCOME_CLEAN


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
        "existence-claim evidence check test",
        "existence-claim evidence check live artifact",
        "existence-claim evidence check terminal summary",
        "automated repository scan, if ever separately bounded",
        "repair or successor handling of the affected file, if ever separately bounded",
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


def _build_check_object(
    request: Mapping[str, Any],
    target_surface_basis: Mapping[str, Any],
    recorded: bool,
    detected_claims: list[Mapping[str, Any]],
    per_claim_outcomes: list[Mapping[str, Any]],
    file_level_outcome: str,
) -> dict[str, Any]:
    unsupported_count = sum(
        1
        for item in per_claim_outcomes
        if item.get("per_claim_outcome") == PER_CLAIM_OUTCOME_UNSUPPORTED
    )
    supported_count = sum(
        1
        for item in per_claim_outcomes
        if item.get("per_claim_outcome") == PER_CLAIM_OUTCOME_EVIDENCE_SUPPORTED
    )
    check = {
        "check_id": _json_safe(
            request.get("existence_claim_evidence_check_id") or DEFAULT_CHECK_ID
        ),
        "check_type": _json_safe(request.get("check_type") or CHECK_TYPE),
        "check_version": RESULT_VERSION,
        "check_scope": _json_safe(request.get("check_scope") or CHECK_SCOPE),
        "target_surface_path": _json_safe(request.get("target_surface_path")),
        "target_surface_kind": _json_safe(
            request.get("target_surface_kind") or TARGET_SURFACE_KIND
        ),
        "contaminated_lineage_policy": _json_safe(
            request.get("contaminated_lineage_policy")
        ),
        "scan_allowed": request.get("scan_allowed") is True,
        "repair_allowed": request.get("repair_allowed") is True,
        "validation_enforcement_allowed": (
            request.get("validation_enforcement_allowed") is True
        ),
        "follow_on_authorized": request.get("follow_on_authorized") is True,
        "existence_claim_evidence_check_recorded": recorded,
        "target_surface_declared": bool(target_surface_basis.get("declared")),
        "target_surface_readable": bool(target_surface_basis.get("readable")),
        "target_surface_kind_is_markdown": (
            request.get("target_surface_kind") == TARGET_SURFACE_KIND
        ),
        "evidence_map_declared": "evidence_map" in request,
        "detected_claim_count": len(detected_claims),
        "unsupported_claim_count": unsupported_count,
        "evidence_supported_claim_count": supported_count,
        "file_level_outcome": file_level_outcome,
        "contaminated_class_preserved": (
            file_level_outcome == FILE_OUTCOME_CONTAMINATED_CLASS
        ),
        "unsupported_claims_preserved": unsupported_count > 0,
    }
    check.update(_canonical_non_claims())
    return check


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    target_surface_basis: Mapping[str, Any],
    evidence_map_basis: Mapping[str, Any],
    detected_claims: list[Mapping[str, Any]],
    per_claim_outcomes: list[Mapping[str, Any]],
    file_level_outcome: str,
    outcome: str,
    recorded: bool,
) -> dict[str, Any]:
    check_object = _build_check_object(
        request,
        target_surface_basis,
        recorded,
        detected_claims,
        per_claim_outcomes,
        file_level_outcome,
    )
    failed_code = _first_failed_code(checks)
    failed_checks = [check for check in checks if check.get("passed") is False]
    passed_checks = [check for check in checks if check.get("passed") is True]
    non_claims = _canonical_non_claims()
    statement = {
        "existence_claim_evidence_check_recorded": recorded,
        "target_surface_declared": check_object["target_surface_declared"],
        "target_surface_readable": check_object["target_surface_readable"],
        "target_surface_kind_is_markdown": check_object[
            "target_surface_kind_is_markdown"
        ],
        "evidence_map_declared": check_object["evidence_map_declared"],
        "contaminated_lineage_policy_preserved": (
            request.get("contaminated_lineage_policy")
            == DEFAULT_CONTAMINATED_LINEAGE_POLICY
        ),
        "detected_claims_extracted": bool(detected_claims)
        or check_object["target_surface_readable"],
        "per_claim_outcomes_recorded": len(per_claim_outcomes) == len(detected_claims),
        "file_level_outcome_recorded": file_level_outcome in FILE_OUTCOME_FAMILY,
        "unsupported_claims_preserved": check_object["unsupported_claims_preserved"],
        "contaminated_class_preserved": check_object["contaminated_class_preserved"],
        "result_level_non_claims_canonical_false": all(
            value is False for value in non_claims.values()
        ),
    }
    statement.update(non_claims)
    result: dict[str, Any] = {
        "existence_claim_evidence_check_metadata": {
            "existence_claim_evidence_check_id": check_object["check_id"],
            "existence_claim_evidence_check_type": CHECK_TYPE,
            "existence_claim_evidence_check_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_existence_claim_evidence_check_question": {
            "existence_claim_evidence_check_id": _json_safe(
                request.get("existence_claim_evidence_check_id")
            ),
            "existence_claim_evidence_check_question": _json_safe(
                request.get("existence_claim_evidence_check_question")
            ),
            "existence_claim_evidence_check_intent": _json_safe(
                request.get("existence_claim_evidence_check_intent")
            ),
            "target_surface_path": _json_safe(request.get("target_surface_path")),
            "target_surface_kind": _json_safe(request.get("target_surface_kind")),
            "contaminated_lineage_policy": _json_safe(
                request.get("contaminated_lineage_policy")
            ),
            "check_type": _json_safe(request.get("check_type")),
            "check_scope": _json_safe(request.get("check_scope")),
            "scan_allowed": _json_safe(request.get("scan_allowed")),
            "repair_allowed": _json_safe(request.get("repair_allowed")),
            "validation_enforcement_allowed": _json_safe(
                request.get("validation_enforcement_allowed")
            ),
            "follow_on_authorized": _json_safe(request.get("follow_on_authorized")),
        },
        "target_surface_basis": dict(target_surface_basis),
        "declared_evidence_map_basis": dict(evidence_map_basis),
        "existence_claim_evidence_check": check_object,
        "detected_existence_claims": [_json_safe(item) for item in detected_claims],
        "existence_claim_evidence_check_per_claim_outcomes": [
            _json_safe(item) for item in per_claim_outcomes
        ],
        "existence_claim_evidence_check_checks": checks,
        "existence_claim_evidence_check_statement": statement,
        "existence_claim_evidence_check_non_meaning": {
            "not_repository_scan": True,
            "not_file_discovery": True,
            "not_repair": True,
            "not_validation_enforcement": True,
            "not_unsupported_claim_validation": True,
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
    result["existence_claim_evidence_check_summary"] = (
        build_existence_claim_evidence_check_v0_min_summary(result)
    )
    result["existence_claim_evidence_check_summary"]["passed_check_count"] = len(
        passed_checks
    )
    result["existence_claim_evidence_check_summary"]["failed_check_count"] = len(
        failed_checks
    )
    return result


def build_declared_existence_claim_evidence_check_v0_min_request(
    existence_claim_evidence_check_id: str = DEFAULT_CHECK_ID,
    existence_claim_evidence_check_question: str = DEFAULT_QUESTION,
    existence_claim_evidence_check_intent: str = INTENT_RECORD,
    target_surface_path: Path | str = DEFAULT_TARGET_SURFACE_PATH,
    target_surface_kind: str = TARGET_SURFACE_KIND,
    evidence_map: Mapping[str, Any] | list[Mapping[str, Any]] | None = None,
    contaminated_lineage_policy: str = DEFAULT_CONTAMINATED_LINEAGE_POLICY,
    check_type: str = CHECK_TYPE,
    check_scope: str = CHECK_SCOPE,
    scan_allowed: bool = False,
    repair_allowed: bool = False,
    validation_enforcement_allowed: bool = False,
    follow_on_authorized: bool = False,
    declared_non_claims: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a bounded default declared evidence-check request."""

    return {
        "existence_claim_evidence_check_id": existence_claim_evidence_check_id,
        "existence_claim_evidence_check_question": (
            existence_claim_evidence_check_question
        ),
        "existence_claim_evidence_check_intent": existence_claim_evidence_check_intent,
        "target_surface_path": str(target_surface_path),
        "target_surface_kind": target_surface_kind,
        "evidence_map": copy.deepcopy(evidence_map) if evidence_map is not None else {},
        "contaminated_lineage_policy": contaminated_lineage_policy,
        "check_type": check_type,
        "check_scope": check_scope,
        "scan_allowed": scan_allowed,
        "repair_allowed": repair_allowed,
        "validation_enforcement_allowed": validation_enforcement_allowed,
        "follow_on_authorized": follow_on_authorized,
        "declared_non_claims": (
            dict(declared_non_claims)
            if declared_non_claims is not None
            else _canonical_non_claims()
        ),
    }


def resolve_existence_claim_evidence_check_v0_min(
    declared_existence_claim_evidence_check: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declared-surface existence-claim evidence check request."""

    if declared_existence_claim_evidence_check is None:
        request: dict[str, Any] = (
            build_declared_existence_claim_evidence_check_v0_min_request()
        )
    elif isinstance(declared_existence_claim_evidence_check, MappingABC):
        request = copy.deepcopy(dict(declared_existence_claim_evidence_check))
    else:
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_is_mapping",
            False,
            "mapping",
            type(declared_existence_claim_evidence_check).__name__,
            "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_MALFORMED",
        )
        return _build_result(
            {},
            checks,
            {},
            {},
            [],
            [],
            FILE_OUTCOME_BLOCKED,
            OUTCOME_BLOCKED,
            False,
        )

    checks = []

    question = request.get("existence_claim_evidence_check_question")
    _add_check(
        checks,
        "check_question_declared",
        isinstance(question, str) and question.strip() != "",
        "non-empty check question",
        question,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_QUESTION_UNDECLARED",
    )

    intent = request.get("existence_claim_evidence_check_intent")
    _add_check(
        checks,
        "check_intent_supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_INTENT_UNSUPPORTED",
    )
    _add_check(
        checks,
        "check_block_not_requested",
        intent != INTENT_BLOCK,
        f"intent is not {INTENT_BLOCK}",
        intent,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_BLOCK_REQUESTED",
    )

    target_path_value = request.get("target_surface_path")
    target_declared = (
        isinstance(target_path_value, (str, Path)) and str(target_path_value).strip() != ""
    )
    _add_check(
        checks,
        "target_surface_path_declared",
        target_declared,
        "non-empty target surface path",
        target_path_value,
        "TARGET_SURFACE_PATH_MISSING",
    )
    if target_declared:
        readable, target_text, read_error, resolved_path = _read_text(target_path_value)
    else:
        readable, target_text, read_error, resolved_path = (
            False,
            "",
            "path missing",
            None,
        )
    _add_check(
        checks,
        "target_surface_readable",
        readable,
        "readable UTF-8 Markdown text",
        "readable" if readable else read_error,
        "TARGET_SURFACE_UNREADABLE",
    )
    target_surface_basis = {
        "path": str(target_path_value) if target_declared else None,
        "resolved_path": resolved_path,
        "declared": target_declared,
        "readable": readable,
        "read_error": read_error,
        "line_count": len(target_text.splitlines()) if readable else 0,
        "raw_markdown_body_returned": False,
    }

    target_kind = request.get("target_surface_kind")
    _add_check(
        checks,
        "target_surface_kind_declared",
        isinstance(target_kind, str) and target_kind.strip() != "",
        TARGET_SURFACE_KIND,
        target_kind,
        "TARGET_SURFACE_KIND_MISSING",
    )
    _add_check(
        checks,
        "target_surface_kind_exact",
        target_kind == TARGET_SURFACE_KIND,
        TARGET_SURFACE_KIND,
        target_kind,
        "TARGET_SURFACE_KIND_NOT_MARKDOWN",
    )

    evidence_map_present = "evidence_map" in request
    evidence_map_value = request.get("evidence_map")
    _add_check(
        checks,
        "evidence_map_declared",
        evidence_map_present,
        "declared evidence map",
        evidence_map_present,
        "EVIDENCE_MAP_MISSING",
    )
    evidence_map_shape_ok, evidence_entries, evidence_basis_extra = (
        _normalize_evidence_map(evidence_map_value)
    )
    _add_check(
        checks,
        "evidence_map_mapping_or_list_shaped",
        evidence_map_present and evidence_map_shape_ok,
        "mapping or list of mappings",
        type(evidence_map_value).__name__,
        "EVIDENCE_MAP_MALFORMED",
    )
    evidence_map_basis = {
        "declared": evidence_map_present,
        "mapping_or_list_shaped": evidence_map_shape_ok,
        "raw_evidence_map_returned": False,
    }
    evidence_map_basis.update(evidence_basis_extra)

    contaminated_policy = request.get("contaminated_lineage_policy")
    contaminated_policy_declared = (
        isinstance(contaminated_policy, str) and contaminated_policy.strip() != ""
    )
    contaminated_lineage_as_clean = _contaminated_policy_treats_as_clean(
        contaminated_policy
    )
    _add_check(
        checks,
        "contaminated_lineage_policy_declared",
        contaminated_policy_declared,
        "declared contaminated lineage policy",
        contaminated_policy,
        "CONTAMINATED_LINEAGE_POLICY_MISSING",
    )
    _add_check(
        checks,
        "contaminated_lineage_not_treated_as_clean_basis_by_policy",
        not contaminated_lineage_as_clean,
        "policy does not treat contaminated lineage as clean basis",
        contaminated_policy,
        "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
    )

    check_type = request.get("check_type")
    _add_check(
        checks,
        "check_type_declared",
        isinstance(check_type, str) and check_type.strip() != "",
        CHECK_TYPE,
        check_type,
        "CHECK_TYPE_MISSING",
    )
    _add_check(
        checks,
        "check_type_exact",
        check_type == CHECK_TYPE,
        CHECK_TYPE,
        check_type,
        "CHECK_TYPE_NOT_EXISTENCE_CLAIM_EVIDENCE_CHECK",
    )

    check_scope = request.get("check_scope")
    _add_check(
        checks,
        "check_scope_declared",
        isinstance(check_scope, str) and check_scope.strip() != "",
        CHECK_SCOPE,
        check_scope,
        "CHECK_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "check_scope_exact",
        check_scope == CHECK_SCOPE,
        CHECK_SCOPE,
        check_scope,
        "CHECK_SCOPE_NOT_DECLARED_SURFACE_ONLY",
    )

    for flag_name, code in (
        ("scan_allowed", "SCAN_ALLOWED_TRUE"),
        ("repair_allowed", "REPAIR_ALLOWED_TRUE"),
        ("validation_enforcement_allowed", "VALIDATION_ENFORCEMENT_ALLOWED_TRUE"),
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

    requested_flags = (
        (
            "requested_repository_scan",
            _truthy_flag(
                request,
                (
                    "requested_repository_scan",
                    "repository_scan_requested",
                    "perform_repository_scan",
                ),
            ),
            "REQUESTED_REPOSITORY_SCAN",
        ),
        (
            "requested_file_discovery",
            _truthy_flag(
                request,
                ("requested_file_discovery", "file_discovery_requested", "discover_files"),
            ),
            "REQUESTED_FILE_DISCOVERY",
        ),
        (
            "requested_target_repair",
            _truthy_flag(
                request,
                ("requested_target_repair", "target_repair_requested", "repair_target"),
            ),
            "REQUESTED_TARGET_REPAIR",
        ),
        (
            "requested_target_mutation",
            _truthy_flag(
                request,
                ("requested_target_mutation", "target_mutation_requested", "mutate_target"),
            ),
            "REQUESTED_TARGET_MUTATION",
        ),
        (
            "requested_validation_enforcement",
            _truthy_flag(
                request,
                (
                    "requested_validation_enforcement",
                    "validation_enforcement_requested",
                    "enforce_validation",
                ),
            ),
            "REQUESTED_VALIDATION_ENFORCEMENT",
        ),
        (
            "requested_raw_target_body_return",
            _truthy_flag(
                request,
                (
                    "requested_raw_target_body_return",
                    "return_raw_target_body",
                    "return_raw_markdown_body",
                ),
            ),
            "REQUESTED_RAW_TARGET_BODY_RETURN",
        ),
    )
    for check_name, requested, code in requested_flags:
        _add_check(checks, check_name, not requested, "not requested", requested, code)

    declared_non_claims_ok = _check_declared_non_claims(request, checks)
    _check_top_level_false_postures(request, checks)

    detected_claims = (
        _extract_existence_claims(target_text, target_path_value) if readable else []
    )
    _add_check(
        checks,
        "detected_claims_extracted_from_declared_surface_only",
        readable or not target_declared,
        "declared surface only",
        len(detected_claims),
        "TARGET_SURFACE_UNREADABLE",
    )

    first_failure_before_claims = _first_failed_code(checks)
    blocked_before_claims = first_failure_before_claims is not None
    per_claim_outcomes = [
        _classify_claim(
            claim,
            evidence_entries,
            contaminated_lineage_as_clean
            or request.get("contaminated_lineage_treated_as_clean_basis") is True,
            blocked_before_claims,
        )
        for claim in detected_claims
    ]
    file_level_outcome = _file_level_outcome(
        per_claim_outcomes, blocked_before_claims
    )
    unsupported_count = sum(
        1
        for item in per_claim_outcomes
        if item.get("per_claim_outcome") == PER_CLAIM_OUTCOME_UNSUPPORTED
    )

    _add_check(
        checks,
        "per_claim_outcomes_recorded",
        len(per_claim_outcomes) == len(detected_claims),
        "one per-claim outcome for each detected claim",
        len(per_claim_outcomes),
        first_failure_before_claims
        or "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_MALFORMED",
    )
    _add_check(
        checks,
        "file_level_outcome_recorded",
        file_level_outcome in FILE_OUTCOME_FAMILY,
        FILE_OUTCOME_FAMILY,
        file_level_outcome,
        first_failure_before_claims
        or "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_MALFORMED",
    )
    _add_check(
        checks,
        "unsupported_claims_produce_contaminated_class_outcome",
        unsupported_count == 0 or file_level_outcome == FILE_OUTCOME_CONTAMINATED_CLASS,
        FILE_OUTCOME_CONTAMINATED_CLASS,
        file_level_outcome,
        "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_MALFORMED",
    )

    for key in REQUIRED_FALSE_NON_CLAIMS:
        _add_check(
            checks,
            f"check_preserves_{key}_false",
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
        file_level_outcome = FILE_OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        recorded = False
    else:
        outcome = OUTCOME_RECORDED
        recorded = True

    return _build_result(
        request,
        checks,
        target_surface_basis,
        evidence_map_basis,
        detected_claims,
        per_claim_outcomes,
        file_level_outcome,
        outcome,
        recorded,
    )


def resolve_existence_claim_evidence_check_v0_min_from_path(
    declared_existence_claim_evidence_check_path: Path | str,
) -> dict[str, Any]:
    """Resolve from one declared JSON request path."""

    try:
        path = _repo_path(declared_existence_claim_evidence_check_path)
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
            "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_UNREADABLE",
        )
        return _build_result(
            {},
            checks,
            {},
            {},
            [],
            [],
            FILE_OUTCOME_BLOCKED,
            OUTCOME_BLOCKED,
            False,
        )

    if not isinstance(payload, MappingABC):
        checks = []
        _add_check(
            checks,
            "declared_request_json_is_mapping",
            False,
            "JSON object",
            type(payload).__name__,
            "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_MALFORMED",
        )
        return _build_result(
            {},
            checks,
            {},
            {},
            [],
            [],
            FILE_OUTCOME_BLOCKED,
            OUTCOME_BLOCKED,
            False,
        )

    return resolve_existence_claim_evidence_check_v0_min(payload)


def build_existence_claim_evidence_check_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a bounded summary without embedding raw Markdown bodies."""

    check_object = result.get("existence_claim_evidence_check")
    if not isinstance(check_object, MappingABC):
        check_object = {}
    checks = result.get("existence_claim_evidence_check_checks")
    if not isinstance(checks, list):
        checks = []
    block = result.get("block")
    if not isinstance(block, MappingABC):
        block = {}
    non_claims = result.get("non_claims")
    non_claims_canonical = isinstance(non_claims, MappingABC) and all(
        non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
    )
    per_claim = result.get("existence_claim_evidence_check_per_claim_outcomes")
    if not isinstance(per_claim, list):
        per_claim = []
    per_claim_counts = {
        outcome: sum(1 for item in per_claim if item.get("per_claim_outcome") == outcome)
        for outcome in PER_CLAIM_OUTCOME_FAMILY
    }
    failed_check_count = sum(1 for check in checks if check.get("passed") is False)
    passed_check_count = sum(1 for check in checks if check.get("passed") is True)
    question = result.get("declared_existence_claim_evidence_check_question")
    if not isinstance(question, MappingABC):
        question = {}

    return {
        "outcome": result.get("outcome"),
        "file_level_outcome": check_object.get("file_level_outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "check_id": check_object.get("check_id"),
        "question": question.get("existence_claim_evidence_check_question"),
        "intent": question.get("existence_claim_evidence_check_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "target_surface_path": check_object.get("target_surface_path"),
        "detected_claim_count": check_object.get("detected_claim_count", 0),
        "unsupported_claim_count": check_object.get("unsupported_claim_count", 0),
        "evidence_supported_claim_count": check_object.get(
            "evidence_supported_claim_count", 0
        ),
        "per_claim_outcome_counts": per_claim_counts,
        "check_recorded": check_object.get(
            "existence_claim_evidence_check_recorded", False
        ),
        "target_surface_declared": check_object.get("target_surface_declared", False),
        "target_surface_readable": check_object.get("target_surface_readable", False),
        "evidence_map_declared": check_object.get("evidence_map_declared", False),
        "scan_allowed_false": check_object.get("scan_allowed") is False,
        "repair_allowed_false": check_object.get("repair_allowed") is False,
        "validation_enforcement_allowed_false": check_object.get(
            "validation_enforcement_allowed"
        )
        is False,
        "follow_on_authorized_false": check_object.get("follow_on_authorized")
        is False,
        "scan_not_performed": check_object.get("scan_performed") is False,
        "repository_scan_not_performed": check_object.get("repository_scan_performed")
        is False,
        "file_discovery_not_performed": check_object.get("file_discovery_performed")
        is False,
        "validation_not_enforced": check_object.get("validation_enforced") is False,
        "target_surface_not_repaired": check_object.get("target_surface_repaired")
        is False,
        "target_surface_not_edited": check_object.get("target_surface_edited")
        is False,
        "target_surface_not_deleted": check_object.get("target_surface_deleted")
        is False,
        "target_surface_not_overwritten": check_object.get("target_surface_overwritten")
        is False,
        "unsupported_existence_claims_not_validated": check_object.get(
            "unsupported_existence_claims_validated"
        )
        is False,
        "descendant_body_or_candidate_not_created": (
            check_object.get("descendant_body_a_created") is False
            and check_object.get("descendant_body_b_created") is False
            and check_object.get("descendant_body_basis_candidate_a_created") is False
            and check_object.get("descendant_body_basis_candidate_b_created") is False
        ),
        "valid_derivation_event_not_recorded": check_object.get(
            "valid_derivation_event_recorded"
        )
        is False,
        "standing_relation_crossing_runtime_authority_currentness_follow_on_not_created": (
            check_object.get("standing_created") is False
            and check_object.get("relation_created") is False
            and check_object.get("first_crossing_authorized") is False
            and check_object.get("runtime_created") is False
            and check_object.get("authority_created") is False
            and check_object.get("currentness_created") is False
            and check_object.get("follow_on_work_authorized") is False
        ),
        "repo_presence_not_treated_as_standing": check_object.get(
            "repo_presence_treated_as_standing"
        )
        is False,
        "codex_execution_not_treated_as_truth": check_object.get(
            "codex_execution_treated_as_truth"
        )
        is False,
        "operator_authorization_not_treated_as_sole_authorship": check_object.get(
            "operator_authorization_treated_as_sole_authorship"
        )
        is False,
        "derivative_rendering_not_treated_as_standing_evidence": check_object.get(
            "derivative_rendering_treated_as_standing_evidence"
        )
        is False,
        "later_recognition_not_treated_as_upstream_validity": check_object.get(
            "later_recognition_treated_as_upstream_validity"
        )
        is False,
        "contaminated_lineage_not_treated_as_clean_basis": check_object.get(
            "contaminated_lineage_treated_as_clean_basis"
        )
        is False,
        "hidden_repair_not_performed": check_object.get("hidden_repair_performed")
        is False,
        "silent_overwrite_not_performed": check_object.get("silent_overwrite_performed")
        is False,
        "result_level_non_claims_canonical_false": non_claims_canonical,
    }


def _sanitize_filename(value: Any) -> str:
    safe = str(value or DEFAULT_CHECK_ID)
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe.strip("._-") or DEFAULT_CHECK_ID


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
    raise ExistenceClaimEvidenceCheckV0MinError(
        f"could not find available output path for {path}"
    )


def write_existence_claim_evidence_check_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a stable JSON result without overwriting an existing file."""

    check_object = result.get("existence_claim_evidence_check")
    if not isinstance(check_object, MappingABC):
        check_id = DEFAULT_CHECK_ID
    else:
        check_id = check_object.get("check_id") or DEFAULT_CHECK_ID

    filename = (
        f"{_sanitize_filename(check_id)}"
        "__existence_claim_evidence_check_v0_min_result.json"
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
