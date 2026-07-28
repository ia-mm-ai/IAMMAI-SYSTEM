"""V3 successor for one bounded eight-dimension candidate-evaluation operation.

V3 preserves the V2 operation contract and derives ``what_remains_open`` from
the emitted result branch so completed evaluation work is not reported open.
"""

from __future__ import annotations

import contextlib
import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

import resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2 as _v2


RESULT_VERSION = "0.2.0"
RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3"
REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3"
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_candidate_evaluation_operation_001__"
    "receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result.json"
)


for _name in dir(_v2):
    if _name.isupper() and _name not in {
        "OUTPUT_FILENAME",
        "OUTPUT_ROOT",
        "REPO_ROOT",
        "RESOLVER_MODULE",
        "RESULT_VERSION",
        "WHAT_REMAINS_OPEN",
    }:
        globals()[_name] = getattr(_v2, _name)


class ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
    _v2.ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error
):
    """Raised when a bounded V3 operation result cannot be written."""


_DOWNSTREAM_OPEN = (
    "candidate-sufficiency boundary, if separately selected",
    "receiver-attestation boundary, only after later lawful basis",
    "receiver-answerable-receipt boundary, only after later lawful basis",
    "presence re-evaluation, only after later lawful basis",
    "identity",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "authority",
    "standing",
    "output",
    "action",
    "synchronization",
    "follow-on work",
)

_WAITING_OPEN = (
    "separately supplied eight-dimension evaluation basis",
    "actual candidate evaluation",
    "dimension-specific derived results",
    "candidate-sufficiency boundary, if separately selected after completed evaluation",
    *_DOWNSTREAM_OPEN[1:],
)


@contextlib.contextmanager
def _v2_execution_context() -> Any:
    """Apply V3 runtime configuration while V2 executes its unchanged logic."""
    synchronized = {
        "REPO_ROOT": REPO_ROOT,
        "RESULT_VERSION": RESULT_VERSION,
        "RESOLVER_MODULE": RESOLVER_MODULE,
        "MAX_BASIS_ITEMS_PER_DIMENSION": MAX_BASIS_ITEMS_PER_DIMENSION,
        "MAX_BASIS_REFERENCES_PER_DIMENSION": MAX_BASIS_REFERENCES_PER_DIMENSION,
        "MAX_SERIALIZED_DIMENSION_BASIS_RECORD_SIZE": MAX_SERIALIZED_DIMENSION_BASIS_RECORD_SIZE,
        "MAX_SERIALIZED_EVALUATION_REQUEST_SIZE": MAX_SERIALIZED_EVALUATION_REQUEST_SIZE,
    }
    original = {name: getattr(_v2, name) for name in synchronized}
    try:
        for name, value in synchronized.items():
            setattr(_v2, name, value)
        yield
    finally:
        for name, value in original.items():
            setattr(_v2, name, value)


def _build_what_remains_open(
    *,
    outcome: str,
    operation_result: str,
    atomic_gate: Mapping[str, Any],
    dimension_results: Mapping[str, Any],
    aggregate_postures: Mapping[str, Any],
    operation_exhausted: bool,
    missing_evaluation_basis: Sequence[Any],
) -> list[str]:
    """Return only work unresolved downstream of the final result branch."""
    candidate_evaluated = (
        aggregate_postures.get("receiver_side_answerable_basis_candidate_evaluated") is True
    )
    completed_dimensions = (
        len(dimension_results) == len(EVALUATION_DIMENSION_IDS)
        and all(
            result in {
                DIMENSION_RESULT_SATISFIED,
                DIMENSION_RESULT_NOT_SATISFIED,
                DIMENSION_RESULT_INDETERMINATE,
            }
            for result in dimension_results.values()
        )
    )
    complete_branch = (
        outcome == OUTCOME_RECORDED
        and operation_result
        in {OPERATION_RESULT_EVALUATED, OPERATION_RESULT_INDETERMINATE}
        and atomic_gate.get("all_dimension_basis_records_admissible") is True
        and candidate_evaluated
        and completed_dimensions
        and operation_exhausted
    )
    if complete_branch:
        return list(_DOWNSTREAM_OPEN)

    waiting_branch = (
        outcome == OUTCOME_REQUIRES_EVALUATION_BASIS
        and operation_result == OPERATION_RESULT_REQUIRES_EVALUATION_BASIS
        and not candidate_evaluated
        and not operation_exhausted
    )
    if waiting_branch or outcome == OUTCOME_NOT_RECORDED:
        return list(_WAITING_OPEN)

    if outcome == OUTCOME_BLOCKED:
        branch_open = ["corrected bounded operation request requirements, if separately selected"]
        if missing_evaluation_basis:
            branch_open.extend(
                "unresolved bounded evaluation-basis input: " + str(item)
                for item in missing_evaluation_basis
            )
        branch_open.extend(_DOWNSTREAM_OPEN)
        return branch_open

    return list(_WAITING_OPEN)


def _finalize_v3_result(v2_result: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(v2_result))
    operation = result.get("receiver_side_answerable_basis_candidate_evaluation_operation")
    dimensions = result.get("receiver_side_answerable_basis_candidate_evaluation_operation_dimensions")
    operation = operation if isinstance(operation, Mapping) else {}
    dimensions = dimensions if isinstance(dimensions, Mapping) else {}
    dimension_results = {
        dimension_id: entry.get("dimension_result")
        for dimension_id, entry in dimensions.items()
        if isinstance(entry, Mapping)
    }
    atomic_gate = {key: operation.get(key) for key in _v2._atomic_gate_keys()}
    aggregate_postures = {
        key: operation.get(key)
        for key in (
            "receiver_side_answerable_basis_candidate_evaluated",
            "receiver_side_answerable_basis_candidate_all_dimensions_satisfied",
            "receiver_side_answerable_basis_candidate_any_dimension_not_satisfied",
            "receiver_side_answerable_basis_candidate_any_dimension_indeterminate",
        )
    }
    result["what_remains_open"] = _build_what_remains_open(
        outcome=result.get("outcome"),
        operation_result=operation.get(
            "receiver_side_answerable_basis_candidate_evaluation_operation_result"
        ),
        atomic_gate=atomic_gate,
        dimension_results=dimension_results,
        aggregate_postures=aggregate_postures,
        operation_exhausted=operation.get("candidate_evaluation_operation_exhausted") is True,
        missing_evaluation_basis=result.get("missing_or_inconsistent_evaluation_basis", ()),
    )
    result["resolver_module"] = RESOLVER_MODULE
    result["result_version"] = RESULT_VERSION
    result["receiver_side_answerable_basis_candidate_evaluation_operation_summary"] = (
        _v2._summary_from_result(result)
    )
    return result


def build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build the unchanged bounded request shape; no basis is supplied by default."""
    return _v2.build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request(
        **overrides
    )


def build_declared_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build the declared V3 request using the unchanged bounded operation shape."""
    return build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_request(
        **overrides
    )


def resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3(
    declared_receiver_side_answerable_basis_candidate_evaluation_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded operation with branch-relative open-state reporting."""
    with _v2_execution_context():
        v2_result = _v2.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2(
            declared_receiver_side_answerable_basis_candidate_evaluation_operation
        )
    return _finalize_v3_result(v2_result)


def resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_from_path(
    declared_receiver_side_answerable_basis_candidate_evaluation_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one declared JSON request path and resolve it without discovery."""
    with _v2_execution_context():
        v2_result = _v2.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_from_path(
            declared_receiver_side_answerable_basis_candidate_evaluation_operation_path
        )
    return _finalize_v3_result(v2_result)


def build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return the unchanged compact summary shape for one V3 result."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _v2._summary_from_result(result)


def _as_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(path.stem + "_" + f"{index:03d}" + path.suffix)
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one valid material-omitting V3 result without silently overwriting."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
            "WRITE_REFUSED: result must be a mapping"
        )
    if result.get("resolver_module") != RESOLVER_MODULE or result.get("result_version") != RESULT_VERSION:
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
            "WRITE_REFUSED: incompatible result metadata"
        )
    if result.get("outcome") not in OUTCOME_FAMILY:
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
            "WRITE_REFUSED: unsupported result outcome"
        )
    if not _v2._declared_non_claims_valid(result.get("non_claims")):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
            "WRITE_REFUSED: non-claims are not canonical false"
        )
    if _v2._contains_copied_material(result):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
            "WRITE_REFUSED: copied candidate or complete basis material"
        )
    target = _as_path(output_path) if output_path is not None else OUTPUT_ROOT / OUTPUT_FILENAME
    if _v2._output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
            "WRITE_REFUSED: output path is forbidden"
        )
    target = _next_available_output_path(target)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(dict(result), handle, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False)
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target


def __getattr__(name: str) -> Any:
    """Expose unchanged V2 implementation constants not overridden by V3."""
    return getattr(_v2, name)
