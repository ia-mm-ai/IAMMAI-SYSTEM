"""Resolve bounded continuity-transfer receipts for the v0-min line.

This module emits one additive receiving-side receipt result from one
successful continuity-transfer unit and one bounded receipt request. It
preserves transfer provenance, selected source identity, source-vs-derivative
distinction, and carried non-claims.

It does not replay source actions into a live host, merge preserved runs,
mutate prior artifacts, complete continuity, upgrade standing, replace source,
define persistence or registry law, or turn receipt into final governance.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit as transfer_resolver


class ContinuityTransferReceiptError(RuntimeError):
    """Raised for malformed receipt inputs or impossible correspondence."""


CONTINUITY_TRANSFER_UNIT_ROOT = transfer_resolver.CONTINUITY_TRANSFER_UNIT_ROOT
CONTINUITY_TRANSFER_RECEIPT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_continuity_transfer_receipts"
)

CURRENT_STATE_ANSWER_SURFACE_ROOT = transfer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
CURRENT_STATE_QUERY_ROOT = transfer_resolver.CURRENT_STATE_QUERY_ROOT
CURRENT_STATE_WHAT_STANDS_NOW_ROOT = (
    transfer_resolver.CURRENT_STATE_WHAT_STANDS_NOW_ROOT
)
CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT = (
    transfer_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
)
CURRENT_STATE_TOUCH_PERMISSION_ROOT = transfer_resolver.CURRENT_STATE_TOUCH_PERMISSION_ROOT

CANONICAL_CORE_EXECUTION_FILE = transfer_resolver.CANONICAL_CORE_EXECUTION_FILE
RESOLVER_MODULE = (
    "resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt"
)
CONTINUITY_TRANSFER_RECEIPT_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CONTINUITY_TRANSFER_RECEIPT_RESULT"
)
CONTINUITY_TRANSFER_RECEIPT_RESULT_VERSION = "0.1.0"

OUTCOME_RECEIVED = "RECEIVED"
OUTCOME_REFUSED = "REFUSED"

RECEIPT_CLASS_VALIDATION = "VALIDATION_RECEIPT"
RECEIPT_CLASS_BOUNDED_ACCEPTANCE = "BOUNDED_ACCEPTANCE_RECEIPT"
SUPPORTED_RECEIPT_CLASSES = frozenset(
    {RECEIPT_CLASS_VALIDATION, RECEIPT_CLASS_BOUNDED_ACCEPTANCE}
)

PATH_INPUT_KEYS = transfer_resolver.PATH_INPUT_KEYS
EFFECTIVE_INPUT_KEYS = transfer_resolver.EFFECTIVE_INPUT_KEYS
REQUIRED_FALSE_NON_CLAIMS = transfer_resolver.REQUIRED_FALSE_NON_CLAIMS

NON_CLAIM_DEFAULTS = {
    **transfer_resolver.NON_CLAIM_DEFAULTS,
    "final_continuity_transfer_receipt_completed": False,
}

VALIDATION_DEFAULT_FIELDS = (
    "selected_transfer_result_id",
    "selected_transfer_result_type",
    "selected_transfer_result_outcome",
    "transfer_class",
    "transfer_basis",
    "selected_source_surface_id",
    "selected_source_surface_family",
    "selected_source_surface_outcome",
    "payload_derivative_status",
    "source_remains_source",
    "non_claims",
)

BLOCK_REASONS = {
    "NO_ADMISSIBLE_TRANSFER_RESULT": (
        "No admissible successful continuity-transfer result is available."
    ),
    "SELECTED_TRANSFER_RESULT_UNREADABLE": (
        "The selected continuity-transfer result is unreadable."
    ),
    "SELECTED_TRANSFER_RESULT_MALFORMED": (
        "The selected continuity-transfer result is malformed."
    ),
    "SELECTED_TRANSFER_RESULT_BLOCKED": (
        "The selected continuity-transfer result is refused or blocked."
    ),
    "SELECTED_TRANSFER_RESULT_OUT_OF_SCOPE": (
        "The selected artifact is outside the bounded receipt source scope."
    ),
    "SELECTED_TRANSFER_RESULT_NOT_TRANSFERRED": (
        "The selected transfer result does not have outcome TRANSFERRED."
    ),
    "TOUCH_PERMISSION_REFERENCE_UNREADABLE": (
        "The touch-permission reference preserved by the transfer is unreadable."
    ),
    "TOUCH_PERMISSION_REFERENCE_MALFORMED": (
        "The touch-permission reference preserved by the transfer is malformed."
    ),
    "TRANSFER_PAYLOAD_UNREADABLE": (
        "The transfer payload is absent, unreadable, or not an object."
    ),
    "TRANSFER_PAYLOAD_MISSING_DERIVATIVE_STATUS": (
        "The transfer payload does not preserve explicit derivative status."
    ),
    "SOURCE_REMAINS_SOURCE_NOT_TRUE": (
        "The transfer payload does not preserve source_remains_source = true."
    ),
    "SELECTED_SOURCE_SURFACE_IDENTITY_MISSING": (
        "The transfer result does not preserve selected source-surface identity."
    ),
    "CANONICAL_EXECUTION_LINE_MISMATCH": (
        "The effective references do not preserve the canonical execution line."
    ),
    "EFFECTIVE_REFERENCE_INCOHERENCE": (
        "The transfer result's effective references are not internally coherent."
    ),
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": (
        "Continuity-transfer receipt cannot fall back to stale prior-family artifacts."
    ),
    "LATEST_FILE_INFERENCE_REFUSED": (
        "Continuity-transfer receipt cannot infer current state from latest files."
    ),
    "REPLAY_SHORTCUT_REFUSED": "Replay-based receipt is refused.",
    "MERGE_SHORTCUT_REFUSED": "Merge-based receipt is refused.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": (
        "Continuity-transfer receipt cannot claim continuity completion."
    ),
    "SILENT_STANDING_UPGRADE_REFUSED": (
        "Continuity-transfer receipt cannot silently upgrade standing."
    ),
    "IMPLICIT_MUTATION_REFUSED": "Continuity-transfer receipt cannot authorize mutation.",
    "IMPLICIT_AUTHORITY_CLAIM_REFUSED": (
        "Continuity-transfer receipt cannot carry implicit authority claims."
    ),
    "RECEIPT_CLASS_OUT_OF_SCOPE": (
        "The requested receipt class is outside the bounded receipt model."
    ),
    "RECEIPT_PAYLOAD_OUT_OF_SCOPE": (
        "The requested receipt payload exceeds the transferred carried payload."
    ),
    "SOURCE_REPLACEMENT_REFUSED": (
        "Continuity-transfer receipt cannot replace the selected source surface."
    ),
    "SOURCE_DERIVATIVE_COLLAPSE_REFUSED": (
        "Continuity-transfer receipt cannot collapse source and carried derivative."
    ),
    "MULTIPLE_TRANSFER_RESULTS_CONFLICT_UNRESOLVED": (
        "Multiple transferred units conflict without bounded arbitration."
    ),
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return _repo_root() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    if path == "provided_mapping":
        return "provided_mapping"
    resolved = _repo_path(path)
    try:
        return str(resolved.relative_to(_repo_root()))
    except ValueError:
        return str(resolved)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _read_json_file(path: Path | str, context: str) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"{context} not found: {resolved}") from exc
    except OSError as exc:
        raise OSError(f"{context} is unreadable: {resolved}") from exc
    except json.JSONDecodeError as exc:
        raise ContinuityTransferReceiptError(
            f"{context} is malformed JSON: {resolved}"
        ) from exc
    if not isinstance(value, dict):
        raise ContinuityTransferReceiptError(
            f"{context} must be a JSON object: {resolved}"
        )
    return value


def read_continuity_transfer_receipt_request(path: Path | str) -> dict[str, Any]:
    """Read one bounded continuity-transfer receipt request."""

    return _normal_receipt_request(
        _read_json_file(path, "continuity-transfer receipt request")
    )


def _check(
    name: str,
    passed: bool,
    expected: Any | None = None,
    actual: Any | None = None,
    block_code: str | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {"check_name": name, "passed": bool(passed)}
    if expected is not None:
        result["expected_posture"] = expected
    if actual is not None:
        result["actual_posture"] = actual
    if block_code is not None:
        result["block_code"] = block_code
    return result


def _count_checks(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value:
        value = "continuity_transfer_receipt_result"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or "continuity_transfer_receipt_result"


def _same_path(left: Any, right: Any) -> bool:
    if not isinstance(left, str) or not left.strip():
        return False
    if not isinstance(right, str) or not right.strip():
        return False
    return _repo_path(left).resolve(strict=False) == _repo_path(right).resolve(
        strict=False
    )


def _normal_receipt_request(request: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(request, Mapping):
        raise ContinuityTransferReceiptError(
            "continuity-transfer receipt request must be a mapping"
        )
    required = (
        "continuity_transfer_receipt_request_id",
        "receipt_class",
        "receipt_basis",
        "requested_receipt_fields",
        "receiving_boundary_label",
    )
    for key in required:
        if key not in request:
            raise ContinuityTransferReceiptError(
                f"continuity-transfer receipt request is missing {key}"
            )
    normalized: dict[str, Any] = {}
    for key in (
        "continuity_transfer_receipt_request_id",
        "receipt_class",
        "receipt_basis",
        "receiving_boundary_label",
    ):
        value = request.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ContinuityTransferReceiptError(
                f"continuity-transfer receipt request {key} must be a non-empty string"
            )
        normalized[key] = value.strip()
    fields = request.get("requested_receipt_fields")
    if not isinstance(fields, list):
        raise ContinuityTransferReceiptError(
            "continuity-transfer receipt request requested_receipt_fields must be a list"
        )
    normalized_fields: list[str] = []
    for index, value in enumerate(fields):
        if not isinstance(value, str) or not value.strip():
            raise ContinuityTransferReceiptError(
                "continuity-transfer receipt request requested_receipt_fields "
                f"entry {index} must be a non-empty string"
            )
        normalized_fields.append(value.strip())
    normalized["requested_receipt_fields"] = normalized_fields
    return normalized


def _looks_like_transfer_result(transfer: Mapping[str, Any]) -> bool:
    return any(
        key in transfer
        for key in (
            "continuity_transfer_metadata",
            "selected_source_surface",
            "touch_permission_reference",
            "transfer_request",
            "transfer_payload",
            "transfer_summary",
        )
    )


def _transfer_metadata(transfer: Mapping[str, Any]) -> Mapping[str, Any]:
    metadata = transfer.get("continuity_transfer_metadata")
    if not isinstance(metadata, Mapping):
        raise ContinuityTransferReceiptError(
            "selected transfer result metadata must be an object"
        )
    for key in (
        "continuity_transfer_result_id",
        "continuity_transfer_result_type",
        "continuity_transfer_result_version",
    ):
        value = metadata.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ContinuityTransferReceiptError(
                f"selected transfer result metadata {key} is malformed"
            )
    return metadata


def _selected_source_surface(transfer: Mapping[str, Any]) -> Mapping[str, Any]:
    selected = transfer.get("selected_source_surface")
    if not isinstance(selected, Mapping):
        raise ContinuityTransferReceiptError(
            "selected transfer result selected_source_surface must be an object"
        )
    return selected


def _touch_reference_section(transfer: Mapping[str, Any]) -> Mapping[str, Any]:
    reference = transfer.get("touch_permission_reference")
    if not isinstance(reference, Mapping):
        raise ContinuityTransferReceiptError(
            "selected transfer result touch_permission_reference must be an object"
        )
    return reference


def _transfer_request_section(transfer: Mapping[str, Any]) -> Mapping[str, Any]:
    request = transfer.get("transfer_request")
    if not isinstance(request, Mapping):
        raise ContinuityTransferReceiptError(
            "selected transfer result transfer_request must be an object"
        )
    return request


def _transfer_payload(transfer: Mapping[str, Any]) -> Mapping[str, Any] | None:
    payload = transfer.get("transfer_payload")
    if payload is None:
        return None
    if not isinstance(payload, Mapping):
        return None
    return payload


def _transfer_id(transfer: Mapping[str, Any]) -> str | None:
    metadata = transfer.get("continuity_transfer_metadata")
    if not isinstance(metadata, Mapping):
        return None
    value = metadata.get("continuity_transfer_result_id")
    return value if isinstance(value, str) and value.strip() else None


def _transfer_identity(
    transfer: Mapping[str, Any] | None,
    transfer_path: Path | str | None,
) -> dict[str, Any]:
    if transfer is None:
        return {
            "selected_transfer_result_path": _display_path(transfer_path),
            "selected_transfer_result_id": None,
            "selected_transfer_result_type": None,
            "selected_transfer_result_outcome": None,
            "transfer_class": None,
            "transfer_basis": None,
        }
    metadata = transfer.get("continuity_transfer_metadata", {})
    transfer_request = transfer.get("transfer_request", {})
    return {
        "selected_transfer_result_path": _display_path(transfer_path)
        if transfer_path is not None
        else "provided_mapping",
        "selected_transfer_result_id": metadata.get("continuity_transfer_result_id")
        if isinstance(metadata, Mapping)
        else None,
        "selected_transfer_result_type": metadata.get("continuity_transfer_result_type")
        if isinstance(metadata, Mapping)
        else None,
        "selected_transfer_result_outcome": transfer.get("outcome"),
        "transfer_class": transfer_request.get("transfer_class")
        if isinstance(transfer_request, Mapping)
        else None,
        "transfer_basis": transfer_request.get("transfer_basis")
        if isinstance(transfer_request, Mapping)
        else None,
    }


def _source_identity_from_transfer(
    transfer: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if transfer is None:
        return {
            "selected_source_surface_path": None,
            "selected_source_surface_id": None,
            "selected_source_surface_family": None,
            "selected_source_surface_outcome": None,
            "selected_source_surface_effective_references": {},
        }
    selected = transfer.get("selected_source_surface", {})
    if not isinstance(selected, Mapping):
        return {
            "selected_source_surface_path": None,
            "selected_source_surface_id": None,
            "selected_source_surface_family": None,
            "selected_source_surface_outcome": None,
            "selected_source_surface_effective_references": {},
        }
    references = selected.get("selected_source_surface_effective_references", {})
    return {
        "selected_source_surface_path": selected.get("selected_source_surface_path"),
        "selected_source_surface_id": selected.get("selected_source_surface_id"),
        "selected_source_surface_family": selected.get("selected_source_surface_family"),
        "selected_source_surface_outcome": selected.get("selected_source_surface_outcome"),
        "selected_source_surface_effective_references": dict(references)
        if isinstance(references, Mapping)
        else {},
    }


def _touch_reference_from_transfer(
    transfer: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if transfer is None:
        return {
            "touch_permission_result_path": None,
            "touch_permission_result_id": None,
            "admitted_touch_class": None,
            "admitted_touch_scope": None,
        }
    reference = transfer.get("touch_permission_reference", {})
    if not isinstance(reference, Mapping):
        return {
            "touch_permission_result_path": None,
            "touch_permission_result_id": None,
            "admitted_touch_class": None,
            "admitted_touch_scope": None,
        }
    scope = reference.get("admitted_touch_scope")
    return {
        "touch_permission_result_path": reference.get("touch_permission_result_path"),
        "touch_permission_result_id": reference.get("touch_permission_result_id"),
        "admitted_touch_class": reference.get("admitted_touch_class"),
        "admitted_touch_scope": dict(scope) if isinstance(scope, Mapping) else scope,
    }


def _merge_non_claims(transfer: Mapping[str, Any] | None) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    if transfer is None:
        return merged
    raw = transfer.get("non_claims", {})
    if raw is None:
        return merged
    if not isinstance(raw, Mapping):
        raise ContinuityTransferReceiptError(
            "selected transfer result non_claims must be an object"
        )
    for key, value in raw.items():
        if not isinstance(key, str):
            raise ContinuityTransferReceiptError("non_claim keys must be strings")
        if not isinstance(value, bool):
            raise ContinuityTransferReceiptError(
                f"non_claim value for {key!r} must be boolean"
            )
        merged[key] = value
    return merged


def _discover_artifacts(root: Path | str, context: str) -> list[Path]:
    resolved = _repo_path(root)
    if not resolved.exists():
        return []
    if not resolved.is_dir():
        raise ContinuityTransferReceiptError(
            f"{context} root is not a directory: {resolved}"
        )
    try:
        return sorted(path for path in resolved.glob("*.json") if path.is_file())
    except OSError as exc:
        raise ContinuityTransferReceiptError(
            f"{context} root is unreadable: {resolved}"
        ) from exc


def _transfer_effective_key(transfer: Mapping[str, Any]) -> tuple[Any, ...]:
    selected = transfer.get("selected_source_surface", {})
    touch = transfer.get("touch_permission_reference", {})
    payload = transfer.get("transfer_payload", {})
    transfer_request = transfer.get("transfer_request", {})
    references = {}
    if isinstance(selected, Mapping):
        raw_references = selected.get("selected_source_surface_effective_references", {})
        if isinstance(raw_references, Mapping):
            references = raw_references
    payload_fields = ()
    if isinstance(payload, Mapping):
        carried = payload.get("carried_fields", {})
        if isinstance(carried, Mapping):
            payload_fields = tuple(sorted(str(key) for key in carried))
    return (
        selected.get("selected_source_surface_id") if isinstance(selected, Mapping) else None,
        selected.get("selected_source_surface_family")
        if isinstance(selected, Mapping)
        else None,
        touch.get("touch_permission_result_id") if isinstance(touch, Mapping) else None,
        transfer_request.get("transfer_class")
        if isinstance(transfer_request, Mapping)
        else None,
        payload_fields,
        tuple(references.get(key) for key in EFFECTIVE_INPUT_KEYS),
    )


def _select_default_transfer_result() -> tuple[
    Mapping[str, Any] | None,
    Path | None,
    str | None,
]:
    candidates: list[tuple[str, Mapping[str, Any], Path]] = []
    for path in _discover_artifacts(CONTINUITY_TRANSFER_UNIT_ROOT, "continuity-transfer"):
        transfer = _read_json_file(path, "continuity-transfer result")
        if transfer.get("outcome") != transfer_resolver.OUTCOME_TRANSFERRED:
            continue
        candidates.append((_display_path(path) or str(path), transfer, path))
    if not candidates:
        return None, None, "NO_ADMISSIBLE_TRANSFER_RESULT"
    keys = {_transfer_effective_key(transfer) for _, transfer, _ in candidates}
    if len(keys) > 1:
        return None, None, "MULTIPLE_TRANSFER_RESULTS_CONFLICT_UNRESOLVED"
    _, transfer, path = sorted(candidates, key=lambda item: item[0])[-1]
    return transfer, path, None


def _checks_all_passed(artifact: Mapping[str, Any], label: str) -> bool:
    checks = artifact.get("checks", [])
    if not isinstance(checks, list):
        raise ContinuityTransferReceiptError(f"{label} checks must be a list")
    return all(
        isinstance(check, Mapping) and check.get("passed") is True for check in checks
    )


def _effective_inputs_from_transfer(transfer: Mapping[str, Any]) -> dict[str, Any]:
    selected = _selected_source_surface(transfer)
    raw = selected.get("selected_source_surface_effective_references")
    if not isinstance(raw, Mapping):
        raise ContinuityTransferReceiptError(
            "selected source-surface effective references must be an object"
        )
    result = dict(raw)
    for key in PATH_INPUT_KEYS:
        value = result.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ContinuityTransferReceiptError(
                f"effective reference {key} must be a non-empty string"
            )
    for key in ("effective_source_run_path", "effective_ingress_run_path"):
        value = result.get(key)
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ContinuityTransferReceiptError(
                f"effective reference {key} must be a string when present"
            )
    return {key: result.get(key) for key in EFFECTIVE_INPUT_KEYS}


def _load_effective_artifacts(
    effective_inputs: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    try:
        return (
            _read_json_file(
                str(effective_inputs["effective_authority_artifact_path"]),
                "effective authority artifact",
            ),
            _read_json_file(
                str(effective_inputs["effective_family_packet_path"]),
                "effective run-family packet",
            ),
            _read_json_file(
                str(effective_inputs["effective_status_packet_path"]),
                "effective preserved-run status packet",
            ),
            _read_json_file(
                str(effective_inputs["effective_current_governing_packet_path"]),
                "effective current-governing packet",
            ),
        )
    except (FileNotFoundError, OSError) as exc:
        raise FileNotFoundError(str(exc)) from exc


def _effective_summaries(
    authority: Mapping[str, Any],
    family: Mapping[str, Any],
    status: Mapping[str, Any],
    governing: Mapping[str, Any],
) -> dict[str, dict[str, Any]]:
    try:
        return {
            "authority": transfer_resolver.query_resolver.build_execution_authority_summary(
                authority
            ),
            "family": transfer_resolver.query_resolver.build_run_family_summary(family),
            "status": (
                transfer_resolver.query_resolver.build_preserved_run_status_summary(
                    status
                )
            ),
            "governing": (
                transfer_resolver.query_resolver.build_current_governing_summary(
                    governing
                )
            ),
        }
    except Exception as exc:  # noqa: BLE001 - malformed artifacts fail clearly.
        raise ContinuityTransferReceiptError(
            "effective reference artifact is malformed"
        ) from exc


def _exposed_paths_match(values: Sequence[Any]) -> bool:
    exposed = [value for value in values if isinstance(value, str) and value.strip()]
    if len(exposed) < 2:
        return True
    first = exposed[0]
    return all(_same_path(first, value) for value in exposed[1:])


def _effective_currentness_checks(
    effective_inputs: Mapping[str, Any],
    summaries: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    canonical_actual = {
        name: summary.get("core_execution_file") for name, summary in summaries.items()
    }
    source_values = [
        effective_inputs.get("effective_source_run_path"),
        summaries["authority"].get("selected_source_run_directory_path"),
        summaries["family"].get("current_authority_source_run_path"),
        summaries["status"].get("selected_current_authority_source_run_path"),
        summaries["governing"].get("current_governing_source_run_path"),
    ]
    ingress_values = [
        effective_inputs.get("effective_ingress_run_path"),
        summaries["authority"].get("selected_ingress_run_directory_path"),
        summaries["family"].get("current_authority_ingress_run_path"),
        summaries["governing"].get("current_governing_ingress_run_path"),
    ]
    canonical_passed = all(
        value == CANONICAL_CORE_EXECUTION_FILE for value in canonical_actual.values()
    )
    source_passed = _exposed_paths_match(source_values)
    ingress_passed = _exposed_paths_match(ingress_values)
    return [
        _check(
            "canonical_core_execution_file_aligned",
            canonical_passed,
            expected=CANONICAL_CORE_EXECUTION_FILE,
            actual=canonical_actual,
            block_code="CANONICAL_EXECUTION_LINE_MISMATCH"
            if not canonical_passed
            else None,
        ),
        _check(
            "effective_references_share_current_governing_source_run_where_exposed",
            source_passed,
            expected="same current governing source run where exposed",
            actual=source_values,
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE" if not source_passed else None,
        ),
        _check(
            "effective_references_share_current_governing_ingress_run_where_exposed",
            ingress_passed,
            expected="same current governing ingress run where exposed",
            actual=ingress_values,
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE"
            if not ingress_passed
            else None,
        ),
    ]


def _touch_permission_path(reference: Mapping[str, Any]) -> str | None:
    value = reference.get("touch_permission_result_path")
    if not isinstance(value, str) or not value.strip():
        return None
    if value == "provided_mapping":
        return None
    return value


def _validate_touch_reference(
    reference: Mapping[str, Any],
) -> tuple[list[dict[str, Any]], str | None]:
    checks: list[dict[str, Any]] = []
    touch_id = reference.get("touch_permission_result_id")
    path = _touch_permission_path(reference)
    if touch_id is None and path is None:
        checks.append(
            _check(
                "touch_permission_reference_optional_or_carried",
                True,
                expected="no file-backed touch reference required",
                actual=reference,
            )
        )
        return checks, None
    if touch_id is not None and (not isinstance(touch_id, str) or not touch_id.strip()):
        raise ContinuityTransferReceiptError(
            "touch-permission reference result id is malformed"
        )
    if path is None:
        checks.append(
            _check(
                "touch_permission_reference_file_readable_where_applicable",
                True,
                expected="provided mapping or carried touch reference",
                actual=reference.get("touch_permission_result_path"),
            )
        )
        return checks, None
    try:
        touch = _read_json_file(path, "touch-permission reference")
    except (FileNotFoundError, OSError) as exc:
        checks.append(
            _check(
                "touch_permission_reference_file_readable_where_applicable",
                False,
                expected="readable touch-permission result where path is preserved",
                actual=str(exc),
                block_code="TOUCH_PERMISSION_REFERENCE_UNREADABLE",
            )
        )
        return checks, "TOUCH_PERMISSION_REFERENCE_UNREADABLE"
    metadata = touch.get("touch_permission_metadata")
    if not isinstance(metadata, Mapping):
        raise ContinuityTransferReceiptError(
            "touch-permission reference metadata is malformed"
        )
    actual_id = metadata.get("touch_permission_result_id")
    id_matches = not isinstance(touch_id, str) or actual_id == touch_id
    outcome_ok = (
        touch.get("outcome")
        == transfer_resolver.touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH
    )
    checks.extend(
        [
            _check(
                "touch_permission_reference_file_readable_where_applicable",
                True,
                expected="readable touch-permission result where path is preserved",
                actual=path,
            ),
            _check(
                "touch_permission_reference_id_corresponds",
                id_matches,
                expected=touch_id,
                actual=actual_id,
                block_code="TOUCH_PERMISSION_REFERENCE_MALFORMED"
                if not id_matches
                else None,
            ),
            _check(
                "touch_permission_reference_is_successful",
                outcome_ok,
                expected=transfer_resolver.touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
                actual=touch.get("outcome"),
                block_code="TOUCH_PERMISSION_REFERENCE_MALFORMED"
                if not outcome_ok
                else None,
            ),
            _check(
                "touch_permission_reference_checks_passed",
                _checks_all_passed(touch, "touch-permission reference"),
                expected="touch-permission checks all passed",
                actual="all passed"
                if _checks_all_passed(touch, "touch-permission reference")
                else "one or more failed",
                block_code="TOUCH_PERMISSION_REFERENCE_MALFORMED"
                if not _checks_all_passed(touch, "touch-permission reference")
                else None,
            ),
        ]
    )
    failed = _first_failed(checks)
    if failed is not None:
        code = failed.get("block_code")
        if isinstance(code, str):
            return checks, code
    return checks, None


def _request_text(request: Mapping[str, Any]) -> str:
    parts = [
        str(request.get("receipt_basis", "")),
        str(request.get("receiving_boundary_label", "")),
        " ".join(str(field) for field in request.get("requested_receipt_fields", [])),
    ]
    return " ".join(parts).lower()


def _contains(text: str, phrases: Sequence[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def _request_refusal_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    text = _request_text(request)
    return [
        _check(
            "receipt_request_does_not_attempt_replay",
            not _contains(text, ("replay into", "replay-based", "allow replay", "use replay")),
            expected="no replay shortcut",
            actual=request.get("receipt_basis"),
            block_code="REPLAY_SHORTCUT_REFUSED",
        ),
        _check(
            "receipt_request_does_not_attempt_merge",
            not _contains(text, ("merge into", "merge-based", "allow merge", "use merge")),
            expected="no merge shortcut",
            actual=request.get("receipt_basis"),
            block_code="MERGE_SHORTCUT_REFUSED",
        ),
        _check(
            "receipt_request_does_not_claim_continuity_completion",
            not _contains(
                text,
                ("complete continuity", "continuity completion", "claim continuity"),
            ),
            expected="no continuity-completion claim",
            actual=request.get("receipt_basis"),
            block_code="CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "receipt_request_does_not_silently_upgrade_standing",
            not _contains(text, ("standing upgrade", "upgrade standing", "promote standing")),
            expected="no standing upgrade",
            actual=request.get("receipt_basis"),
            block_code="SILENT_STANDING_UPGRADE_REFUSED",
        ),
        _check(
            "receipt_request_does_not_request_stale_prior_family_fallback",
            not _contains(text, ("stale prior", "prior-family fallback", "fallback to prior")),
            expected="no stale prior-family fallback",
            actual=request.get("receipt_basis"),
            block_code="STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
        _check(
            "receipt_request_does_not_infer_from_latest_files",
            not _contains(
                text,
                ("latest authority", "latest family", "latest status", "latest governing"),
            ),
            expected="no latest-file inference",
            actual=request.get("receipt_basis"),
            block_code="LATEST_FILE_INFERENCE_REFUSED",
        ),
        _check(
            "receipt_request_does_not_authorize_mutation",
            not _contains(text, ("mutate", "rewrite", "overwrite", "delete prior", "modify prior")),
            expected="no mutation authority",
            actual=request.get("receipt_basis"),
            block_code="IMPLICIT_MUTATION_REFUSED",
        ),
        _check(
            "receipt_request_does_not_claim_implicit_authority",
            not _contains(
                text,
                (
                    "final governance",
                    "system law",
                    "protocol law",
                    "governing standing",
                    "authority claim",
                    "final identity",
                    "constitutional author",
                    "local authority",
                ),
            ),
            expected="no implicit authority claim",
            actual=request.get("receipt_basis"),
            block_code="IMPLICIT_AUTHORITY_CLAIM_REFUSED",
        ),
        _check(
            "receipt_request_does_not_replace_source",
            not _contains(text, ("replace source", "source replacement", "become source")),
            expected="source remains source",
            actual=request.get("receipt_basis"),
            block_code="SOURCE_REPLACEMENT_REFUSED",
        ),
        _check(
            "receipt_request_preserves_source_derivative_distinction",
            not _contains(
                text,
                ("collapse source", "collapse derivative", "derivative becomes source"),
            ),
            expected="source and carried derivative remain distinct",
            actual=request.get("receipt_basis"),
            block_code="SOURCE_DERIVATIVE_COLLAPSE_REFUSED",
        ),
    ]


def _non_claim_checks(non_claims: Mapping[str, bool]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for key in REQUIRED_FALSE_NON_CLAIMS:
        block_code = {
            "replayed_into_live_host": "REPLAY_SHORTCUT_REFUSED",
            "merged_into_local_state": "MERGE_SHORTCUT_REFUSED",
            "continuity_completed": "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
            "standing_upgraded": "SILENT_STANDING_UPGRADE_REFUSED",
        }[key]
        checks.append(
            _check(
                f"non_claim_{key}_remains_false",
                non_claims.get(key) is False,
                expected=False,
                actual=non_claims.get(key),
                block_code=block_code if non_claims.get(key) is not False else None,
            )
        )
    finality_failures = {
        key: value
        for key, value in non_claims.items()
        if (key.startswith("final_") or key == "minimum_lawful_system_completed")
        and value is not False
    }
    checks.append(
        _check(
            "broader_finality_non_claims_remain_false",
            not finality_failures,
            expected="all carried finality non-claims false",
            actual=finality_failures,
            block_code="IMPLICIT_AUTHORITY_CLAIM_REFUSED"
            if finality_failures
            else None,
        )
    )
    return checks


def _source_identity_missing(source_identity: Mapping[str, Any]) -> bool:
    required = (
        "selected_source_surface_id",
        "selected_source_surface_family",
        "selected_source_surface_outcome",
    )
    for key in required:
        value = source_identity.get(key)
        if not isinstance(value, str) or not value.strip():
            return True
    references = source_identity.get("selected_source_surface_effective_references")
    return not isinstance(references, Mapping)


def _receipt_values(
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    touch_reference: Mapping[str, Any],
    payload: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    carried_fields = payload.get("carried_fields", {})
    carried_references = payload.get("carried_references", {})
    values: dict[str, Any] = {
        **dict(transfer_identity),
        **dict(source_identity),
        **dict(touch_reference),
        "payload_derivative_status": payload.get("payload_derivative_status"),
        "source_remains_source": payload.get("source_remains_source"),
        "carried_derivative_remains_derivative": True,
        "non_claims": dict(non_claims),
    }
    if isinstance(carried_fields, Mapping):
        for key, value in carried_fields.items():
            if isinstance(key, str):
                values[key] = value
    if isinstance(carried_references, Mapping):
        for key, value in carried_references.items():
            if isinstance(key, str):
                values[key] = value
    for key, value in non_claims.items():
        values[key] = value
    return values


def _requested_fields_for_receipt(request: Mapping[str, Any]) -> list[str]:
    requested = list(request["requested_receipt_fields"])
    if request["receipt_class"] == RECEIPT_CLASS_VALIDATION and not requested:
        return list(VALIDATION_DEFAULT_FIELDS)
    return requested


def _receipt_payload_scope(
    request: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    touch_reference: Mapping[str, Any],
    payload: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> tuple[dict[str, Any], dict[str, Any] | None, list[str]]:
    receipt_class = str(request["receipt_class"])
    fields = _requested_fields_for_receipt(request)
    values = _receipt_values(
        transfer_identity,
        source_identity,
        touch_reference,
        payload,
        non_claims,
    )
    if receipt_class not in SUPPORTED_RECEIPT_CLASSES:
        return (
            _check(
                "receipt_class_is_supported",
                False,
                expected=sorted(SUPPORTED_RECEIPT_CLASSES),
                actual=receipt_class,
                block_code="RECEIPT_CLASS_OUT_OF_SCOPE",
            ),
            None,
            fields,
        )
    if receipt_class == RECEIPT_CLASS_BOUNDED_ACCEPTANCE and not fields:
        return (
            _check(
                "receipt_payload_scope_is_bounded",
                False,
                expected="non-empty requested_receipt_fields for bounded acceptance",
                actual=fields,
                block_code="RECEIPT_PAYLOAD_OUT_OF_SCOPE",
            ),
            None,
            fields,
        )
    invalid_fields = [field for field in fields if field not in values]
    passed = not invalid_fields
    check = _check(
        "receipt_payload_scope_is_bounded",
        passed,
        expected="fields already transferred or intrinsic validation fields",
        actual={
            "requested_receipt_fields": list(request["requested_receipt_fields"]),
            "receipt_fields": fields,
            "invalid_fields": invalid_fields,
        },
        block_code="RECEIPT_PAYLOAD_OUT_OF_SCOPE" if not passed else None,
    )
    if not passed:
        return check, None, fields
    received_payload = {
        "payload_receipt_status": "received_carried_derivative",
        "source_remains_source": True,
        "carried_derivative_remains_derivative": True,
        "received_fields": {field: values[field] for field in fields},
        "received_references": {
            "selected_transfer_result_path": transfer_identity.get(
                "selected_transfer_result_path"
            ),
            "selected_transfer_result_id": transfer_identity.get(
                "selected_transfer_result_id"
            ),
            "selected_source_surface_path": source_identity.get(
                "selected_source_surface_path"
            ),
            "selected_source_surface_effective_references": source_identity.get(
                "selected_source_surface_effective_references"
            ),
            "touch_permission_result_path": touch_reference.get(
                "touch_permission_result_path"
            ),
            "touch_permission_result_id": touch_reference.get(
                "touch_permission_result_id"
            ),
        },
    }
    return check, received_payload, fields


def _result_id(
    transfer_identity: Mapping[str, Any],
    request: Mapping[str, Any],
    outcome: str,
) -> str:
    transfer_id = transfer_identity.get("selected_transfer_result_id")
    if not isinstance(transfer_id, str) or not transfer_id.strip():
        transfer_id = "no_transfer_result"
    request_id = request.get("continuity_transfer_receipt_request_id")
    if not isinstance(request_id, str) or not request_id.strip():
        request_id = "continuity_transfer_receipt_request"
    suffix = "received" if outcome == OUTCOME_RECEIVED else "refused"
    return f"{transfer_id}__{request_id}__continuity_transfer_receipt_{suffix}"


def _result(
    request: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    touch_reference: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    received_payload: Mapping[str, Any] | None,
    receipt_summary: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    return {
        "continuity_transfer_receipt_metadata": {
            "continuity_transfer_receipt_result_id": _result_id(
                transfer_identity,
                request,
                outcome,
            ),
            "continuity_transfer_receipt_result_type": (
                CONTINUITY_TRANSFER_RECEIPT_RESULT_TYPE
            ),
            "continuity_transfer_receipt_result_version": (
                CONTINUITY_TRANSFER_RECEIPT_RESULT_VERSION
            ),
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_transfer_result": dict(transfer_identity),
        "selected_source_surface": dict(source_identity),
        "touch_permission_reference": dict(touch_reference),
        "receipt_request": dict(request),
        "checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": BLOCK_REASONS.get(block_code) if block_code else None,
        },
        "received_payload": dict(received_payload)
        if received_payload is not None
        else None,
        "receipt_summary": dict(receipt_summary)
        if receipt_summary is not None
        else None,
        "non_claims": dict(non_claims),
    }


def _refused_result(
    request: Mapping[str, Any],
    block_code: str,
    checks: Sequence[Mapping[str, Any]],
    transfer_identity: Mapping[str, Any] | None = None,
    source_identity: Mapping[str, Any] | None = None,
    touch_reference: Mapping[str, Any] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _result(
        request,
        transfer_identity or _transfer_identity(None, None),
        source_identity or _source_identity_from_transfer(None),
        touch_reference or _touch_reference_from_transfer(None),
        checks,
        OUTCOME_REFUSED,
        block_code,
        None,
        None,
        non_claims or dict(NON_CLAIM_DEFAULTS),
    )


def _resolve_selected_transfer(
    request: Mapping[str, Any],
    transfer: Mapping[str, Any],
    transfer_path: Path | str | None,
    selection_source: str,
) -> dict[str, Any]:
    if not _looks_like_transfer_result(transfer):
        return _refused_result(
            request,
            "SELECTED_TRANSFER_RESULT_OUT_OF_SCOPE",
            [
                _check(
                    "selected_transfer_result_is_in_receipt_scope",
                    False,
                    expected="continuity-transfer-unit result artifact",
                    actual="unrecognized artifact shape",
                    block_code="SELECTED_TRANSFER_RESULT_OUT_OF_SCOPE",
                )
            ],
            transfer_identity=_transfer_identity(transfer, transfer_path),
            non_claims=_merge_non_claims(transfer),
        )

    transfer_identity = _transfer_identity(transfer, transfer_path)
    source_identity = _source_identity_from_transfer(transfer)
    touch_reference = _touch_reference_from_transfer(transfer)
    non_claims = _merge_non_claims(transfer)
    outcome = transfer.get("outcome")

    if outcome == transfer_resolver.OUTCOME_REFUSED or outcome == "BLOCKED":
        return _refused_result(
            request,
            "SELECTED_TRANSFER_RESULT_BLOCKED",
            [
                _check(
                    "selected_transfer_result_has_transferred_outcome",
                    False,
                    expected=transfer_resolver.OUTCOME_TRANSFERRED,
                    actual=outcome,
                    block_code="SELECTED_TRANSFER_RESULT_BLOCKED",
                )
            ],
            transfer_identity=transfer_identity,
            source_identity=source_identity,
            touch_reference=touch_reference,
            non_claims=non_claims,
        )
    if outcome != transfer_resolver.OUTCOME_TRANSFERRED:
        return _refused_result(
            request,
            "SELECTED_TRANSFER_RESULT_NOT_TRANSFERRED",
            [
                _check(
                    "selected_transfer_result_has_transferred_outcome",
                    False,
                    expected=transfer_resolver.OUTCOME_TRANSFERRED,
                    actual=outcome,
                    block_code="SELECTED_TRANSFER_RESULT_NOT_TRANSFERRED",
                )
            ],
            transfer_identity=transfer_identity,
            source_identity=source_identity,
            touch_reference=touch_reference,
            non_claims=non_claims,
        )

    _transfer_metadata(transfer)
    _transfer_request_section(transfer)
    _selected_source_surface(transfer)
    _touch_reference_section(transfer)
    payload = _transfer_payload(transfer)
    payload_is_mapping = isinstance(payload, Mapping)
    checks: list[dict[str, Any]] = [
        _check(
            "selected_transfer_result_exists_and_is_readable",
            True,
            expected="one readable selected continuity-transfer result",
            actual=transfer_identity.get("selected_transfer_result_path"),
        ),
        _check(
            "selected_transfer_result_has_transferred_outcome",
            True,
            expected=transfer_resolver.OUTCOME_TRANSFERRED,
            actual=outcome,
        ),
        _check(
            "selected_transfer_result_is_in_receipt_scope",
            True,
            expected="continuity-transfer-unit result artifact",
            actual=transfer_identity.get("selected_transfer_result_type"),
        ),
        _check(
            "selected_transfer_result_checks_passed",
            _checks_all_passed(transfer, "selected transfer result"),
            expected="selected transfer result checks all passed",
            actual="all passed"
            if _checks_all_passed(transfer, "selected transfer result")
            else "one or more failed",
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE"
            if not _checks_all_passed(transfer, "selected transfer result")
            else None,
        ),
        _check(
            "transfer_payload_is_readable",
            payload_is_mapping,
            expected="transfer_payload object",
            actual=payload,
            block_code="TRANSFER_PAYLOAD_UNREADABLE"
            if not payload_is_mapping
            else None,
        ),
    ]

    if not payload_is_mapping or payload is None:
        return _refused_result(
            request,
            "TRANSFER_PAYLOAD_UNREADABLE",
            checks,
            transfer_identity=transfer_identity,
            source_identity=source_identity,
            touch_reference=touch_reference,
            non_claims=non_claims,
        )

    derivative_status_ok = payload.get("payload_derivative_status") == "carried_derivative"
    source_remains_source = payload.get("source_remains_source") is True
    source_identity_missing = _source_identity_missing(source_identity)
    checks.extend(
        [
            _check(
                "transfer_payload_preserves_derivative_status",
                derivative_status_ok,
                expected="carried_derivative",
                actual=payload.get("payload_derivative_status"),
                block_code="TRANSFER_PAYLOAD_MISSING_DERIVATIVE_STATUS"
                if not derivative_status_ok
                else None,
            ),
            _check(
                "transfer_payload_preserves_source_remains_source",
                source_remains_source,
                expected=True,
                actual=payload.get("source_remains_source"),
                block_code="SOURCE_REMAINS_SOURCE_NOT_TRUE"
                if not source_remains_source
                else None,
            ),
            _check(
                "selected_source_surface_identity_is_preserved",
                not source_identity_missing,
                expected="source id, family, outcome, and effective references preserved",
                actual=source_identity,
                block_code="SELECTED_SOURCE_SURFACE_IDENTITY_MISSING"
                if source_identity_missing
                else None,
            ),
            _check(
                "receipt_uses_selected_transfer_result_not_latest_files_alone",
                True,
                expected="selected continuity-transfer result",
                actual=selection_source,
            ),
            _check(
                "receipt_does_not_fall_back_to_stale_prior_family",
                True,
                expected="effective references carried by transfer result",
                actual=source_identity.get("selected_source_surface_effective_references"),
            ),
        ]
    )

    touch_checks, touch_block = _validate_touch_reference(touch_reference)
    checks.extend(touch_checks)
    if touch_block is not None:
        return _refused_result(
            request,
            touch_block,
            checks,
            transfer_identity=transfer_identity,
            source_identity=source_identity,
            touch_reference=touch_reference,
            non_claims=non_claims,
        )

    try:
        effective_inputs = _effective_inputs_from_transfer(transfer)
    except ContinuityTransferReceiptError:
        raise
    try:
        effective_artifacts = _load_effective_artifacts(effective_inputs)
    except (FileNotFoundError, OSError) as exc:
        checks.append(
            _check(
                "effective_references_are_readable",
                False,
                expected="readable authority/family/status/governing artifacts",
                actual=str(exc),
                block_code="EFFECTIVE_REFERENCE_INCOHERENCE",
            )
        )
        return _refused_result(
            request,
            "EFFECTIVE_REFERENCE_INCOHERENCE",
            checks,
            transfer_identity=transfer_identity,
            source_identity=source_identity,
            touch_reference=touch_reference,
            non_claims=non_claims,
        )

    summaries = _effective_summaries(*effective_artifacts)
    checks.append(
        _check(
            "effective_references_are_readable",
            True,
            expected="readable authority/family/status/governing artifacts",
            actual={key: effective_inputs.get(key) for key in PATH_INPUT_KEYS},
        )
    )
    checks.extend(_effective_currentness_checks(effective_inputs, summaries))
    checks.append(
        _check(
            "receipt_class_is_supported",
            request["receipt_class"] in SUPPORTED_RECEIPT_CLASSES,
            expected=sorted(SUPPORTED_RECEIPT_CLASSES),
            actual=request["receipt_class"],
            block_code="RECEIPT_CLASS_OUT_OF_SCOPE"
            if request["receipt_class"] not in SUPPORTED_RECEIPT_CLASSES
            else None,
        )
    )

    scope_check, received_payload, fields = _receipt_payload_scope(
        request,
        transfer_identity,
        source_identity,
        touch_reference,
        payload,
        non_claims,
    )
    checks.append(scope_check)
    checks.extend(_request_refusal_checks(request))
    checks.extend(_non_claim_checks(non_claims))
    checks.append(
        _check(
            "source_derivative_distinction_preserved_at_receipt",
            received_payload is None
            or (
                received_payload.get("payload_receipt_status")
                == "received_carried_derivative"
                and received_payload.get("source_remains_source") is True
                and received_payload.get("carried_derivative_remains_derivative")
                is True
            ),
            expected="source remains source and received payload remains derivative",
            actual=received_payload,
            block_code="SOURCE_DERIVATIVE_COLLAPSE_REFUSED"
            if received_payload is not None
            and (
                received_payload.get("payload_receipt_status")
                != "received_carried_derivative"
                or received_payload.get("source_remains_source") is not True
                or received_payload.get("carried_derivative_remains_derivative")
                is not True
            )
            else None,
        )
    )

    failed = _first_failed(checks)
    if failed is not None:
        block_code = failed.get("block_code")
        if not isinstance(block_code, str) or block_code not in BLOCK_REASONS:
            block_code = "EFFECTIVE_REFERENCE_INCOHERENCE"
        return _refused_result(
            request,
            block_code,
            checks,
            transfer_identity=transfer_identity,
            source_identity=source_identity,
            touch_reference=touch_reference,
            non_claims=non_claims,
        )

    receipt_summary = {
        "received_field_count": len(fields),
        "received_field_names": list(fields),
        "selected_transfer_result_id": transfer_identity.get(
            "selected_transfer_result_id"
        ),
        "selected_source_surface_id": source_identity.get(
            "selected_source_surface_id"
        ),
        "selected_source_surface_family": source_identity.get(
            "selected_source_surface_family"
        ),
        "touch_permission_result_id": touch_reference.get(
            "touch_permission_result_id"
        ),
        "receipt_basis": request.get("receipt_basis"),
        "receiving_boundary_label": request.get("receiving_boundary_label"),
    }
    return _result(
        request,
        transfer_identity,
        source_identity,
        touch_reference,
        checks,
        OUTCOME_RECEIVED,
        None,
        received_payload,
        receipt_summary,
        non_claims,
    )


def resolve_continuity_transfer_receipt(
    receipt_request: Mapping[str, Any],
    transfer_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded continuity-transfer-receipt decision."""

    request = _normal_receipt_request(receipt_request)
    if transfer_result is not None:
        if not isinstance(transfer_result, Mapping):
            raise ContinuityTransferReceiptError(
                "transfer_result must be a mapping or None"
            )
        return _resolve_selected_transfer(
            request,
            dict(transfer_result),
            None,
            "provided_mapping",
        )

    transfer, path, block_code = _select_default_transfer_result()
    if block_code is not None:
        return _refused_result(
            request,
            block_code,
            [
                _check(
                    "admissible_transfer_result_selected",
                    False,
                    expected="one transferred continuity-transfer result",
                    actual=block_code,
                    block_code=block_code,
                )
            ],
        )
    if transfer is None:
        raise ContinuityTransferReceiptError("selected transfer result is absent")
    return _resolve_selected_transfer(
        request,
        transfer,
        path,
        "continuity_transfer_result_discovery",
    )


def resolve_continuity_transfer_receipt_from_path(
    transfer_result_path: Path | str,
    receipt_request: Mapping[str, Any],
) -> dict[str, Any]:
    """Read one continuity-transfer result and resolve receipt."""

    request = _normal_receipt_request(receipt_request)
    resolved_path = _repo_path(transfer_result_path)
    try:
        transfer = _read_json_file(resolved_path, "selected continuity-transfer result")
    except (FileNotFoundError, OSError):
        return _refused_result(
            request,
            "SELECTED_TRANSFER_RESULT_UNREADABLE",
            [
                _check(
                    "selected_transfer_result_exists_and_is_readable",
                    False,
                    expected="readable selected continuity-transfer result",
                    actual=_display_path(resolved_path),
                    block_code="SELECTED_TRANSFER_RESULT_UNREADABLE",
                )
            ],
            transfer_identity=_transfer_identity(None, resolved_path),
        )
    return _resolve_selected_transfer(
        request,
        transfer,
        resolved_path,
        "explicit_transfer_result_path",
    )


def build_continuity_transfer_receipt_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact inspection summary for one receipt result."""

    if not isinstance(result, Mapping):
        raise ContinuityTransferReceiptError(
            "continuity-transfer receipt result must be a mapping"
        )
    metadata = result.get("continuity_transfer_receipt_metadata", {})
    transfer = result.get("selected_transfer_result", {})
    source = result.get("selected_source_surface", {})
    request = result.get("receipt_request", {})
    block = result.get("block", {})
    checks = result.get("checks", [])
    summary = result.get("receipt_summary", {})
    non_claims = result.get("non_claims", {})
    if not isinstance(checks, list):
        raise ContinuityTransferReceiptError(
            "continuity-transfer receipt checks must be a list"
        )
    passed, failed = _count_checks(checks)
    return {
        "continuity_transfer_receipt_result_id": metadata.get(
            "continuity_transfer_receipt_result_id"
        )
        if isinstance(metadata, Mapping)
        else None,
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason")
        if isinstance(block, Mapping)
        else None,
        "selected_transfer_result_id": transfer.get("selected_transfer_result_id")
        if isinstance(transfer, Mapping)
        else None,
        "selected_source_surface_id": source.get("selected_source_surface_id")
        if isinstance(source, Mapping)
        else None,
        "receipt_class": request.get("receipt_class")
        if isinstance(request, Mapping)
        else None,
        "received_field_names": summary.get("received_field_names")
        if isinstance(summary, Mapping)
        else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in REQUIRED_FALSE_NON_CLAIMS
            if isinstance(non_claims, Mapping)
        },
    }


def _default_output_path(result: Mapping[str, Any]) -> Path:
    selected = result.get("selected_transfer_result", {})
    selected_id = (
        selected.get("selected_transfer_result_id")
        if isinstance(selected, Mapping)
        else None
    )
    stem = _safe_filename_part(selected_id)
    root = _repo_path(CONTINUITY_TRANSFER_RECEIPT_ROOT)
    candidate = root / f"{stem}__continuity_transfer_receipt_result.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = root / (
            f"{stem}__continuity_transfer_receipt_result_{index:03d}.json"
        )
        if not candidate.exists():
            return candidate
    raise ContinuityTransferReceiptError(
        "no bounded continuity-transfer-receipt filename available"
    )


def write_continuity_transfer_receipt_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive continuity-transfer-receipt JSON result."""

    if not isinstance(result, Mapping):
        raise ContinuityTransferReceiptError(
            "continuity-transfer receipt result must be a mapping"
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"continuity-transfer receipt result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
