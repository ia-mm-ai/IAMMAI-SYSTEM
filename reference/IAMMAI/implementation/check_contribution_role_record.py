#!/usr/bin/env python3
"""
First bounded checker for first-pass contribution-role records.

This script validates one JSON file as one contribution-role record object
against the visible first-pass contribution-role schema lane. It also checks
clearly file-like refs carried by that object where the schema and examples
already justify that. It does not implement generic JSON Schema support,
infer runtime status, derive identity, or act as a governance mechanism.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Pattern, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]

ID_PATTERN = re.compile(r"^[A-Za-z0-9._:-]+$")

ROLE_TYPES = frozenset(
    {
        "ORIGIN",
        "ELICITATION",
        "FORMALIZATION",
        "AUTHORIZATION",
        "RENDERING",
        "TRANSMISSION",
    }
)

REQUIRED_FIELDS = {
    "contribution_role_record_id",
    "recorded_at",
    "role_type",
    "matter_ref",
}

OPTIONAL_FIELDS = {
    "actor_ref",
    "artifact_ref",
    "related_governance_action_ref",
}

EXPECTED_FIELDS = REQUIRED_FIELDS | OPTIONAL_FIELDS

CLEAR_FILE_SUFFIXES = frozenset(
    {
        ".md",
        ".json",
        ".jsonl",
        ".pdf",
        ".py",
        ".toml",
        ".txt",
        ".yaml",
        ".yml",
    }
)


@dataclass
class CheckResult:
    record_path: Path
    field_errors: list[str] = field(default_factory=list)
    ref_errors: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.field_errors and not self.ref_errors


def usage() -> str:
    return (
        "Usage:\n"
        "  python3 implementation/check_contribution_role_record.py "
        "/path/to/contribution_role_record.json"
    )


def load_record(record_path: Path) -> Any:
    with record_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def check_required_and_unexpected_keys(
    data: dict[str, Any],
    result: CheckResult,
) -> None:
    missing = sorted(REQUIRED_FIELDS - set(data))
    for field_name in missing:
        result.field_errors.append(f"Missing required field: {field_name}")

    unexpected = sorted(set(data) - EXPECTED_FIELDS)
    for field_name in unexpected:
        result.field_errors.append(f"Unexpected field: {field_name}")


def validate_string_field(
    data: dict[str, Any],
    field_name: str,
    result: CheckResult,
    *,
    max_length: int,
    pattern: Pattern[str] | None = None,
) -> str | None:
    if field_name not in data:
        return None

    value = data[field_name]
    if not isinstance(value, str):
        result.field_errors.append(f"{field_name} must be a string.")
        return None
    if not value.strip():
        result.field_errors.append(f"{field_name} must be a non-empty string.")
        return None
    if len(value) > max_length:
        result.field_errors.append(
            f"{field_name} exceeds the first-pass maximum length of {max_length}."
        )
        return None
    if pattern is not None and not pattern.fullmatch(value):
        result.field_errors.append(f"{field_name} has an invalid first-pass format.")
        return None
    return value


def validate_role_type(
    data: dict[str, Any],
    result: CheckResult,
) -> str | None:
    role_type = validate_string_field(data, "role_type", result, max_length=64)
    if role_type is None:
        return None
    if role_type not in ROLE_TYPES:
        allowed = ", ".join(sorted(ROLE_TYPES))
        result.field_errors.append(
            f"role_type must be one of the visible first-pass values: {allowed}."
        )
        return None
    return role_type


def is_clearly_file_like_ref(ref_value: str) -> bool:
    candidate = Path(ref_value)

    if candidate.is_absolute():
        return True
    if ref_value.startswith("./") or ref_value.startswith("../"):
        return True

    return candidate.suffix.lower() in CLEAR_FILE_SUFFIXES


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
        return None, "points outside repository root"

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


def check_optional_file_like_ref(
    field_name: str,
    ref_value: str | None,
    result: CheckResult,
) -> None:
    if ref_value is None:
        return
    if is_clearly_file_like_ref(ref_value):
        check_file_ref(field_name, ref_value, result)


def validate_contribution_role_record(
    data: dict[str, Any],
    result: CheckResult,
) -> None:
    check_required_and_unexpected_keys(data, result)

    validate_string_field(
        data,
        "contribution_role_record_id",
        result,
        max_length=128,
        pattern=ID_PATTERN,
    )
    validate_string_field(data, "recorded_at", result, max_length=128)
    validate_role_type(data, result)
    validate_string_field(data, "matter_ref", result, max_length=1000)

    validate_string_field(data, "actor_ref", result, max_length=1000)
    artifact_ref = validate_string_field(data, "artifact_ref", result, max_length=1000)
    related_governance_action_ref = validate_string_field(
        data,
        "related_governance_action_ref",
        result,
        max_length=1000,
    )

    check_optional_file_like_ref("artifact_ref", artifact_ref, result)
    check_optional_file_like_ref(
        "related_governance_action_ref",
        related_governance_action_ref,
        result,
    )


def print_result(result: CheckResult) -> None:
    status = "PASS" if result.passed else "FAIL"
    print(
        f"record={result.record_path} "
        f"type=contribution_role_record "
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
        print(
            f"Unable to read contribution-role record: {record_path} (missing)",
            file=sys.stderr,
        )
        return 2
    except OSError as exc:
        print(
            f"Unable to read contribution-role record: {record_path} ({exc})",
            file=sys.stderr,
        )
        return 2

    if not resolved_record_path.is_file():
        print(
            f"Unable to read contribution-role record: {resolved_record_path} (not a file)",
            file=sys.stderr,
        )
        return 2

    try:
        raw_record = load_record(resolved_record_path)
    except json.JSONDecodeError as exc:
        print(f"Malformed JSON in {resolved_record_path}: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(
            f"Unable to read contribution-role record: {resolved_record_path} ({exc})",
            file=sys.stderr,
        )
        return 2

    result = CheckResult(record_path=resolved_record_path)

    if not isinstance(raw_record, dict):
        result.field_errors.append("Top-level JSON value must be an object.")
        print_result(result)
        return 1

    validate_contribution_role_record(raw_record, result)
    print_result(result)
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
