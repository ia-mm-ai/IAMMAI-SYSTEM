"""Portable source-body verification output capture v2 resolver.

This additive successor preserves the v1 output-capture law and corrects only
the v1 returned/written-result containment failure: v1 could produce a clean
in-memory result while leaving frozenset values inside check expected_posture,
which prevented JSON writing. V2 keeps v1 visible as predecessor failure
evidence and returns a recursively JSON-safe result without inventing output
content or creating report, result, success, authority, currentness, final
completion, continuation, reusable permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

import resolve_portable_source_body_verification_output_capture as _v1


class PortableSourceBodyVerificationOutputCaptureV2Error(Exception):
    """Raised for impossible output-capture v2 containment failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_output_capture_v2"
RESULT_VERSION = "0.2.0"
RESULT_TYPE = _v1.RESULT_TYPE
SUCCESSOR_OF = "resolve_portable_source_body_verification_output_capture"
SUCCESSOR_REASON = (
    "v1 produced clean in-memory output-capture resolution but failed JSON "
    "writing because expected_posture contained frozenset"
)

PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_V2_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_output_capture_v2"
)
OUTPUT_ROOT = PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_V2_ROOT

CORE_OUTPUT_CAPTURE_QUESTION = _v1.CORE_OUTPUT_CAPTURE_QUESTION

INTENT_RECORD = _v1.INTENT_RECORD
INTENT_DO_NOT_RECORD = _v1.INTENT_DO_NOT_RECORD
INTENT_BLOCK = _v1.INTENT_BLOCK
SUPPORTED_INTENTS = _v1.SUPPORTED_INTENTS

OUTCOME_RECORDED = _v1.OUTCOME_RECORDED
OUTCOME_NOT_RECORDED = _v1.OUTCOME_NOT_RECORDED
OUTCOME_REQUIRES_ADDITIONAL_BASIS = _v1.OUTCOME_REQUIRES_ADDITIONAL_BASIS
OUTCOME_BLOCKED = _v1.OUTCOME_BLOCKED
OUTPUT_CAPTURE_OUTCOME = _v1.OUTPUT_CAPTURE_OUTCOME
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_CAPTURE_BOUNDARY_OUTCOME = _v1.OUTPUT_CAPTURE_BOUNDARY_OUTCOME
COMMAND_OUTPUT_OUTCOME = _v1.COMMAND_OUTPUT_OUTCOME
COMMAND_OUTPUT_BOUNDARY_OUTCOME = _v1.COMMAND_OUTPUT_BOUNDARY_OUTCOME
COMMAND_OUTPUT_CONTAINMENT_OUTCOME = _v1.COMMAND_OUTPUT_CONTAINMENT_OUTCOME
POST_INVOCATION_COMMAND_EXECUTION_OUTCOME = _v1.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME
COMMAND_INVOCATION_OUTCOME = _v1.COMMAND_INVOCATION_OUTCOME
COMMAND_EXECUTION_REVIEW_OUTCOME = _v1.COMMAND_EXECUTION_REVIEW_OUTCOME
REQUEST_CONSUMPTION_OUTCOME = _v1.REQUEST_CONSUMPTION_OUTCOME
V2_ADMITTED_REQUEST_OUTCOME = _v1.V2_ADMITTED_REQUEST_OUTCOME
V2_ADMITTED_REQUEST_VERSION = _v1.V2_ADMITTED_REQUEST_VERSION

SUPPORTED_OUTPUT_CAPTURE_SCOPE = _v1.SUPPORTED_OUTPUT_CAPTURE_SCOPE
REQUIRED_FALSE_NON_CLAIMS = _v1.REQUIRED_FALSE_NON_CLAIMS
ALLOWED_TRUE_RECORDED_FIELDS = _v1.ALLOWED_TRUE_RECORDED_FIELDS
ALLOWED_FALSE_RECORDED_FIELDS = _v1.ALLOWED_FALSE_RECORDED_FIELDS
SELECTED_BASIS_KEYS = _v1.SELECTED_BASIS_KEYS
POSTURE_KEYS = _v1.POSTURE_KEYS


def _json_sort_key(value: Any) -> str:
    return str(value)


def _json_safe(value: Any) -> Any:
    """Return a recursively JSON-safe copy without dropping check content."""

    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (set, frozenset)):
        return [_json_safe(item) for item in sorted(value, key=_json_sort_key)]
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return copy.deepcopy(value)
    return str(value)


def _successor_metadata() -> dict[str, Any]:
    return {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "portable_source_body_verification_output_capture_result_version": RESULT_VERSION,
        "successor_of": SUCCESSOR_OF,
        "successor_reason": SUCCESSOR_REASON,
        "v1_predecessor_failure_preserved": True,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
        "v2_successor_does_not_erase_v1": True,
        "returned_result_containment_preserved": True,
    }


def _with_v2_successor_posture(result: Mapping[str, Any]) -> dict[str, Any]:
    contained = _json_safe(result)
    metadata = contained.setdefault("portable_source_body_verification_output_capture_metadata", {})
    if not isinstance(metadata, dict):
        metadata = {}
        contained["portable_source_body_verification_output_capture_metadata"] = metadata
    metadata.update(_successor_metadata())
    metadata["short_resolver_filename"] = (
        "resolve_portable_source_body_verification_output_capture_v2.py"
    )

    contained["portable_source_body_verification_output_capture_v2_successor_posture"] = {
        "successor_of": SUCCESSOR_OF,
        "successor_reason": SUCCESSOR_REASON,
        "v1_predecessor_failure_preserved": True,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
        "v2_successor_does_not_erase_v1": True,
        "returned_result_containment_preserved": True,
        "same_output_capture_law_preserved": True,
        "json_safe_returned_result_preserved": True,
        "stdout_content_invented": False,
        "stderr_content_invented": False,
        "process_output_content_invented": False,
        "raw_output_body_content_invented": False,
        "command_output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
    }
    contained["portable_source_body_verification_output_capture_summary"] = (
        build_portable_source_body_verification_output_capture_v2_summary(contained)
    )
    try:
        json.dumps(contained, sort_keys=True, ensure_ascii=False)
    except TypeError as exc:
        raise PortableSourceBodyVerificationOutputCaptureV2Error(
            "v2 output-capture result must be JSON-safe"
        ) from exc
    return contained


def _safe_filename_part(value: Any) -> str:
    text = str(value or "output_capture_request").strip()
    safe = "".join(char if char.isalnum() or char in {"-", "_", "."} else "_" for char in text)
    return safe or "output_capture_request"


def _with_suffix_if_exists(path: Path) -> Path:
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


def resolve_portable_source_body_verification_output_capture_v2(
    declared_output_capture_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    result = _v1.resolve_portable_source_body_verification_output_capture(
        declared_output_capture_request=declared_output_capture_request
    )
    return _with_v2_successor_posture(result)


def resolve_portable_source_body_verification_output_capture_v2_from_path(
    declared_output_capture_request_path: Path | str,
) -> dict[str, Any]:
    result = _v1.resolve_portable_source_body_verification_output_capture_from_path(
        declared_output_capture_request_path
    )
    return _with_v2_successor_posture(result)


def build_portable_source_body_verification_output_capture_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    summary = _json_safe(_v1.build_portable_source_body_verification_output_capture_summary(result))
    summary.update(
        {
            "resolver_module": RESOLVER_MODULE,
            "result_version": RESULT_VERSION,
            "successor_of": SUCCESSOR_OF,
            "successor_reason": SUCCESSOR_REASON,
            "v1_predecessor_failure_preserved": True,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
            "v2_successor_does_not_erase_v1": True,
            "returned_result_containment_preserved": True,
            "json_safe_result": True,
            "output_capture_law_preserved_from_v1": True,
            "stdout_content_invented": False,
            "stderr_content_invented": False,
            "process_output_content_invented": False,
            "raw_output_body_content_invented": False,
            "command_output_report_artifact_created": False,
            "command_result_created": False,
            "command_success_created": False,
            "authority_created": False,
            "currentness_created": False,
            "final_completion_claimed": False,
            "follow_on_work_authorized": False,
        }
    )
    return summary


def write_portable_source_body_verification_output_capture_v2_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    contained = _with_v2_successor_posture(result)
    if output_path is None:
        declared = contained.get("declared_output_capture_question", {})
        request_id = None
        if isinstance(declared, Mapping):
            request_id = declared.get("output_capture_request_id")
        filename = (
            f"{_safe_filename_part(request_id)}"
            "__portable_source_body_verification_output_capture_v2_result.json"
        )
        path = OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _with_suffix_if_exists(path)
    final_path.write_text(
        json.dumps(contained, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_portable_source_body_verification_output_capture_v2_request(
    output_capture_request_id: str,
    *,
    output_capture_question: str = CORE_OUTPUT_CAPTURE_QUESTION,
    output_capture_intent: str = INTENT_RECORD,
    output_capture_scope: Sequence[str] = SUPPORTED_OUTPUT_CAPTURE_SCOPE,
    requested_output_capture_outcome: str = OUTCOME_RECORDED,
    declared_non_claims: Mapping[str, Any] | None = None,
    **selected_basis_and_posture: Any,
) -> dict[str, Any]:
    request = _v1.build_declared_portable_source_body_verification_output_capture_request(
        output_capture_request_id,
        output_capture_question=output_capture_question,
        output_capture_intent=output_capture_intent,
        output_capture_scope=output_capture_scope,
        requested_output_capture_outcome=requested_output_capture_outcome,
        declared_non_claims=declared_non_claims,
        **selected_basis_and_posture,
    )
    return _json_safe(request)
