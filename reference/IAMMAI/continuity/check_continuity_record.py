#!/usr/bin/env python3
"""
First bounded checker for first-pass continuity records.

This script validates one JSON file as either a lineage record or a
currentness record, then checks the file-like refs that record carries.
It does not compute continuity, derive missing structure, or mutate input.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]

LINEAGE = "lineage"
CURRENTNESS = "currentness"

ID_PATTERN = re.compile(r"^[A-Za-z0-9._:-]+$")
TOKEN_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9._:-]*$")

LINEAGE_REQUIRED_KEYS = {
    "lineage_record_id",
    "recorded_at",
    "from_ref",
    "to_ref",
    "relation_type",
    "preserves",
    "changes",
}

CURRENTNESS_REQUIRED_KEYS = {
    "currentness_record_id",
    "recorded_at",
    "scope_ref",
    "current_ref",
    "current_posture",
    "basis_refs",
    "non_current_refs",
}


@dataclass
class CheckResult:
    record_path: Path
    record_type: str | None = None
    field_errors: list[str] = field(default_factory=list)
    ref_errors: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return self.record_type is not None and not self.field_errors and not self.ref_errors


def usage() -> str:
    return (
        "Usage:\n"
        "  python3 continuity/check_continuity_record.py /path/to/continuity_record.json"
    )


def load_record(record_path: Path) -> Any:
    with record_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_non_empty_string(
    data: dict[str, Any],
    field_name: str,
    result: CheckResult,
    *,
    pattern: re.Pattern[str] | None = None,
) -> str | None:
    value = data.get(field_name)
    if not isinstance(value, str):
        result.field_errors.append(f"{field_name} must be a string.")
        return None
    if not value.strip():
        result.field_errors.append(f"{field_name} must be a non-empty string.")
        return None
    if pattern is not None and not pattern.fullmatch(value):
        result.field_errors.append(f"{field_name} has an invalid first-pass format.")
        return None
    return value


def validate_string_array(
    data: dict[str, Any],
    field_name: str,
    result: CheckResult,
) -> list[str] | None:
    value = data.get(field_name)
    if not isinstance(value, list):
        result.field_errors.append(f"{field_name} must be an array.")
        return None
    if not value:
        result.field_errors.append(f"{field_name} must contain at least one item.")
        return None

    validated: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(value):
        label = f"{field_name}[{index}]"
        if not isinstance(item, str):
            result.field_errors.append(f"{label} must be a string.")
            continue
        if not item.strip():
            result.field_errors.append(f"{label} must be a non-empty string.")
            continue
        if item in seen:
            result.field_errors.append(f"{label} duplicates an earlier item in {field_name}.")
            continue
        seen.add(item)
        validated.append(item)

    return validated if validated else None


def check_required_and_unexpected_keys(
    data: dict[str, Any],
    required_keys: set[str],
    result: CheckResult,
) -> None:
    missing = sorted(required_keys - set(data))
    for field_name in missing:
        result.field_errors.append(f"Missing required field: {field_name}")

    unexpected = sorted(set(data) - required_keys)
    for field_name in unexpected:
        result.field_errors.append(f"Unexpected field for {result.record_type} record: {field_name}")


def resolve_repo_ref(ref_value: str) -> tuple[Path | None, str | None]:
    candidate = Path(ref_value)
    candidate = candidate if candidate.is_absolute() else REPO_ROOT / candidate

    try:
        resolved = candidate.resolve(strict=False)
    except OSError as exc:
        return None, f"could not be resolved ({exc})"

    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError:
        return None, "escapes repository root"

    return resolved, None


def check_file_ref(field_name: str, ref_value: str, result: CheckResult) -> None:
    resolved, resolution_error = resolve_repo_ref(ref_value)
    if resolution_error is not None:
        result.ref_errors.append(f"{field_name}: {ref_value} ({resolution_error})")
        return

    if resolved is None or not resolved.exists():
        result.ref_errors.append(f"{field_name}: {ref_value} (missing)")
        return

    if not resolved.is_file():
        result.ref_errors.append(f"{field_name}: {ref_value} (not a file)")


def detect_record_type(data: dict[str, Any], result: CheckResult) -> str | None:
    has_lineage = "lineage_record_id" in data
    has_currentness = "currentness_record_id" in data

    if has_lineage and has_currentness:
        result.field_errors.append(
            "Record cannot contain both lineage_record_id and currentness_record_id."
        )
        return None
    if not has_lineage and not has_currentness:
        result.field_errors.append(
            "Record must contain either lineage_record_id or currentness_record_id."
        )
        return None

    return LINEAGE if has_lineage else CURRENTNESS


def validate_lineage_record(data: dict[str, Any], result: CheckResult) -> None:
    check_required_and_unexpected_keys(data, LINEAGE_REQUIRED_KEYS, result)

    validate_non_empty_string(data, "lineage_record_id", result, pattern=ID_PATTERN)
    validate_non_empty_string(data, "recorded_at", result)
    from_ref = validate_non_empty_string(data, "from_ref", result)
    to_ref = validate_non_empty_string(data, "to_ref", result)
    validate_non_empty_string(data, "relation_type", result, pattern=TOKEN_PATTERN)
    validate_string_array(data, "preserves", result)
    validate_string_array(data, "changes", result)

    if from_ref is not None:
        check_file_ref("from_ref", from_ref, result)
    if to_ref is not None:
        check_file_ref("to_ref", to_ref, result)


def validate_currentness_record(data: dict[str, Any], result: CheckResult) -> None:
    check_required_and_unexpected_keys(data, CURRENTNESS_REQUIRED_KEYS, result)

    validate_non_empty_string(data, "currentness_record_id", result, pattern=ID_PATTERN)
    validate_non_empty_string(data, "recorded_at", result)
    validate_non_empty_string(data, "scope_ref", result)
    current_ref = validate_non_empty_string(data, "current_ref", result)
    validate_non_empty_string(data, "current_posture", result, pattern=TOKEN_PATTERN)
    basis_refs = validate_string_array(data, "basis_refs", result)
    non_current_refs = validate_string_array(data, "non_current_refs", result)

    if current_ref is not None:
        check_file_ref("current_ref", current_ref, result)
    if basis_refs is not None:
        for index, ref_value in enumerate(basis_refs):
            check_file_ref(f"basis_refs[{index}]", ref_value, result)
    if non_current_refs is not None:
        for index, ref_value in enumerate(non_current_refs):
            check_file_ref(f"non_current_refs[{index}]", ref_value, result)


def print_result(result: CheckResult) -> None:
    status = "PASS" if result.passed else "FAIL"
    detected_type = result.record_type or "unknown"
    print(
        f"record={result.record_path} "
        f"type={detected_type} "
        f"status={status} "
        f"field_issues={len(result.field_errors)} "
        f"ref_issues={len(result.ref_errors)}"
    )

    for issue in result.field_errors:
        print(f"field: {issue}")
    for issue in result.ref_errors:
        print(f"ref: {issue}")


def main(argv: Sequence[str]) -> int:
    if len(argv) != 2:
        print(usage(), file=sys.stderr)
        return 2

    record_path = Path(argv[1]).expanduser()
    try:
        resolved_record_path = record_path.resolve(strict=True)
    except FileNotFoundError:
        print(f"Unable to read continuity record: {record_path} (missing)", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"Unable to read continuity record: {record_path} ({exc})", file=sys.stderr)
        return 2

    if not resolved_record_path.is_file():
        print(
            f"Unable to read continuity record: {resolved_record_path} (not a file)",
            file=sys.stderr,
        )
        return 2

    try:
        raw_record = load_record(resolved_record_path)
    except json.JSONDecodeError as exc:
        print(f"Malformed JSON in {resolved_record_path}: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Unable to read continuity record: {resolved_record_path} ({exc})", file=sys.stderr)
        return 2

    result = CheckResult(record_path=resolved_record_path)

    if not isinstance(raw_record, dict):
        result.field_errors.append("Top-level JSON value must be an object.")
        print_result(result)
        return 1

    result.record_type = detect_record_type(raw_record, result)

    if result.record_type == LINEAGE:
        validate_lineage_record(raw_record, result)
    elif result.record_type == CURRENTNESS:
        validate_currentness_record(raw_record, result)

    print_result(result)
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
