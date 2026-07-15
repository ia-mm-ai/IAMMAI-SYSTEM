#!/usr/bin/env python3
"""
First mechanical intake checker for one accession candidate package.

This script performs bounded first-receipt checks only. It does not prove,
admit, or operationalize the candidate slice.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Sequence


DECLARATION_FILENAME = "candidate_declaration.json"
RESULT_FILENAME = "accession_intake_result.json"

STATUS_ACCEPTED = "accepted_for_candidate_review"
STATUS_INSUFFICIENT = "insufficient_package_grounding"
STATUS_OUT_OF_SCOPE = "package_out_of_scope"
STATUS_REFUSED = "refused"

WHOLE_SYSTEM_PATTERN = re.compile(
    r"^\s*(?:all|everything|whole\s+system|entire\s+system|entire\s+platform)\s*$",
    re.IGNORECASE,
)
SLICE_ID_PATTERN = re.compile(r"^[A-Za-z0-9._:-]+$")
SLICE_TYPE_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9._:-]*$")

STRING_FIELD_MAX_LENGTHS: Dict[str, int] = {
    "external_system_name": 200,
    "candidate_slice_name": 200,
    "candidate_slice_id": 128,
    "slice_type": 128,
    "source_description": 2000,
    "export_description": 2000,
    "display_only_description": 2000,
    "proof_question": 2000,
}

ARRAY_ITEM_MAX_LENGTHS: Dict[str, int] = {
    "included_scope": 300,
    "excluded_scope": 300,
    "source_object_paths": 1000,
    "export_slice_paths": 1000,
    "clean_case_paths": 1000,
    "blocked_case_paths": 1000,
}

REQUIRED_STRING_FIELDS = (
    "external_system_name",
    "candidate_slice_name",
    "candidate_slice_id",
    "slice_type",
    "source_description",
    "export_description",
    "display_only_description",
    "proof_question",
)

REQUIRED_ARRAY_FIELDS = (
    "included_scope",
    "excluded_scope",
    "source_object_paths",
    "export_slice_paths",
    "clean_case_paths",
    "blocked_case_paths",
)

EXPECTED_DECLARATION_KEYS = set(REQUIRED_STRING_FIELDS) | set(REQUIRED_ARRAY_FIELDS)

EXPECTED_PATH_GROUPS = {
    "source_object_paths": "source",
    "export_slice_paths": "export",
    "clean_case_paths": "cases/clean",
    "blocked_case_paths": "cases/blocked",
}

EXPECTED_PACKAGE_DIRECTORIES = (
    "source",
    "export",
    "cases/clean",
    "cases/blocked",
)


@dataclass
class IssueBuckets:
    insufficient: list[str] = field(default_factory=list)
    out_of_scope: list[str] = field(default_factory=list)
    refused: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checked_paths: list[str] = field(default_factory=list)
    missing_paths: list[str] = field(default_factory=list)

    def status(self) -> str:
        if self.refused:
            return STATUS_REFUSED
        if self.out_of_scope:
            return STATUS_OUT_OF_SCOPE
        if self.insufficient:
            return STATUS_INSUFFICIENT
        return STATUS_ACCEPTED

    def issue_list(self) -> list[str]:
        issues: list[str] = []
        issues.extend(f"refused: {message}" for message in self.refused)
        issues.extend(f"package_out_of_scope: {message}" for message in self.out_of_scope)
        issues.extend(
            f"insufficient_package_grounding: {message}" for message in self.insufficient
        )
        return issues


@dataclass
class ValidationState:
    package_root: Path
    issues: IssueBuckets = field(default_factory=IssueBuckets)
    candidate_slice_id: Optional[str] = None
    candidate_slice_name: Optional[str] = None
    validated_arrays: dict[str, list[str]] = field(default_factory=dict)


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def print_usage() -> None:
    print(
        "Usage:\n"
        "  python3 accession/intake/check_candidate_package.py /path/to/candidate_package",
        file=sys.stderr,
    )


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def path_display(package_root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(package_root))
    except ValueError:
        return str(path)


def add_unique(items: list[str], value: str) -> None:
    if value not in items:
        items.append(value)


def load_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_declaration_shape(declaration: Any, state: ValidationState) -> None:
    if not isinstance(declaration, dict):
        state.issues.insufficient.append(
            f"{DECLARATION_FILENAME} must contain a JSON object at the top level."
        )
        return

    extra_keys = sorted(set(declaration.keys()) - EXPECTED_DECLARATION_KEYS)
    if extra_keys:
        state.issues.insufficient.append(
            "Unexpected declaration keys are not allowed: " + ", ".join(extra_keys)
        )

    raw_slice_id = declaration.get("candidate_slice_id")
    if is_non_empty_string(raw_slice_id):
        state.candidate_slice_id = raw_slice_id.strip()

    raw_slice_name = declaration.get("candidate_slice_name")
    if is_non_empty_string(raw_slice_name):
        state.candidate_slice_name = raw_slice_name.strip()

    for field_name in REQUIRED_STRING_FIELDS:
        validate_required_string_field(declaration, field_name, state)

    for field_name in REQUIRED_ARRAY_FIELDS:
        values = validate_required_string_array(declaration, field_name, state)
        if values is not None:
            state.validated_arrays[field_name] = values


def validate_required_string_field(
    declaration: dict[str, Any],
    field_name: str,
    state: ValidationState,
) -> None:
    if field_name not in declaration:
        state.issues.insufficient.append(f"Missing required declaration field: {field_name}")
        return

    value = declaration[field_name]
    if not isinstance(value, str):
        state.issues.insufficient.append(f"{field_name} must be a string.")
        return

    if not value.strip():
        state.issues.insufficient.append(f"{field_name} must be a non-empty string.")
        return

    max_length = STRING_FIELD_MAX_LENGTHS[field_name]
    if len(value) > max_length:
        state.issues.insufficient.append(
            f"{field_name} exceeds its maximum length of {max_length} characters."
        )

    if field_name == "candidate_slice_id" and not SLICE_ID_PATTERN.fullmatch(value):
        state.issues.insufficient.append(
            "candidate_slice_id must match ^[A-Za-z0-9._:-]+$."
        )

    if field_name == "slice_type" and not SLICE_TYPE_PATTERN.fullmatch(value):
        state.issues.insufficient.append(
            "slice_type must match ^[A-Za-z][A-Za-z0-9._:-]*$."
        )

    if field_name == "candidate_slice_name" and WHOLE_SYSTEM_PATTERN.fullmatch(value):
        state.issues.out_of_scope.append(
            "candidate_slice_name attempts a whole-system or everything-style submission."
        )


def validate_required_string_array(
    declaration: dict[str, Any],
    field_name: str,
    state: ValidationState,
) -> Optional[list[str]]:
    if field_name not in declaration:
        state.issues.insufficient.append(f"Missing required declaration field: {field_name}")
        return None

    value = declaration[field_name]
    if not isinstance(value, list):
        state.issues.insufficient.append(f"{field_name} must be an array.")
        return None

    if not value:
        state.issues.insufficient.append(f"{field_name} must contain at least one item.")
        return None

    max_length = ARRAY_ITEM_MAX_LENGTHS[field_name]
    validated: list[str] = []
    seen: set[str] = set()

    for index, item in enumerate(value):
        item_label = f"{field_name}[{index}]"
        if not isinstance(item, str):
            state.issues.insufficient.append(f"{item_label} must be a string.")
            continue
        if not item.strip():
            state.issues.insufficient.append(f"{item_label} must be a non-empty string.")
            continue
        if len(item) > max_length:
            state.issues.insufficient.append(
                f"{item_label} exceeds its maximum length of {max_length} characters."
            )
        if item in seen:
            state.issues.insufficient.append(
                f"{field_name} contains a duplicate item: {item!r}."
            )
        seen.add(item)
        if field_name in {"included_scope", "excluded_scope"} and WHOLE_SYSTEM_PATTERN.fullmatch(item):
            state.issues.out_of_scope.append(
                f"{item_label} attempts a whole-system or everything-style scope."
            )
        validated.append(item)

    return validated


def check_package_directories(state: ValidationState) -> None:
    for relative_dir in EXPECTED_PACKAGE_DIRECTORIES:
        path = state.package_root / relative_dir
        if not path.exists():
            state.issues.insufficient.append(
                f"Expected package directory is missing: {relative_dir}"
            )
            continue
        if not path.is_dir():
            state.issues.insufficient.append(
                f"Expected package directory is not a directory: {relative_dir}"
            )

    display_dir = state.package_root / "display"
    if display_dir.exists():
        if display_dir.is_dir():
            state.issues.warnings.append(
                "display/ is present and treated as optional non-authoritative material."
            )
        else:
            state.issues.insufficient.append("display exists but is not a directory.")


def resolve_declared_path(package_root: Path, raw_path: str) -> tuple[Optional[Path], Optional[str]]:
    candidate = Path(raw_path)
    if not candidate.is_absolute():
        candidate = package_root / candidate

    try:
        resolved = candidate.resolve(strict=False)
    except OSError as exc:
        return None, f"Declared path could not be resolved: {raw_path} ({exc})"

    try:
        resolved.relative_to(package_root)
    except ValueError:
        return None, f"Declared path escapes the candidate package root: {raw_path}"

    return resolved, None


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def check_declared_paths(state: ValidationState) -> dict[str, set[Path]]:
    resolved_groups: dict[str, set[Path]] = {}
    display_dir = (state.package_root / "display").resolve(strict=False)

    for field_name, expected_root_name in EXPECTED_PATH_GROUPS.items():
        raw_paths = state.validated_arrays.get(field_name)
        if raw_paths is None:
            continue

        expected_root = (state.package_root / expected_root_name).resolve(strict=False)
        resolved_group: set[Path] = set()

        for raw_path in raw_paths:
            resolved_path, error = resolve_declared_path(state.package_root, raw_path)
            if error is not None:
                state.issues.refused.append(error)
                continue

            if is_within(resolved_path, display_dir):
                state.issues.refused.append(
                    f"{field_name} points into display/, which is optional and non-authoritative: {raw_path}"
                )
                continue

            if not is_within(resolved_path, expected_root):
                state.issues.refused.append(
                    f"{field_name} must stay within {expected_root_name}/: {raw_path}"
                )
                continue

            if not resolved_path.exists():
                state.issues.insufficient.append(
                    f"{field_name} path does not exist: {raw_path}"
                )
                add_unique(state.issues.missing_paths, path_display(state.package_root, resolved_path))
                continue

            resolved_group.add(resolved_path)
            add_unique(state.issues.checked_paths, path_display(state.package_root, resolved_path))

        resolved_groups[field_name] = resolved_group

    return resolved_groups


def check_distinctions(state: ValidationState, resolved_groups: dict[str, set[Path]]) -> None:
    source_paths = resolved_groups.get("source_object_paths", set())
    export_paths = resolved_groups.get("export_slice_paths", set())
    clean_paths = resolved_groups.get("clean_case_paths", set())
    blocked_paths = resolved_groups.get("blocked_case_paths", set())

    if source_paths and export_paths and source_paths == export_paths:
        state.issues.refused.append(
            "source_object_paths and export_slice_paths are identical, so source/export distinction is not real."
        )
    elif source_paths and export_paths and source_paths.intersection(export_paths):
        state.issues.warnings.append(
            "source_object_paths and export_slice_paths overlap; inspect source/export distinction carefully."
        )

    if clean_paths and blocked_paths and clean_paths == blocked_paths:
        state.issues.refused.append(
            "clean_case_paths and blocked_case_paths are identical, so case distinction is not real."
        )
    elif clean_paths and blocked_paths and clean_paths.intersection(blocked_paths):
        state.issues.warnings.append(
            "clean_case_paths and blocked_case_paths overlap; inspect case distinction carefully."
        )


def build_result_payload(state: ValidationState) -> dict[str, Any]:
    return {
        "checked_at": utc_timestamp(),
        "checker_path": str(Path(__file__).resolve()),
        "package_root": str(state.package_root),
        "status": state.issues.status(),
        "candidate_slice_id": state.candidate_slice_id,
        "candidate_slice_name": state.candidate_slice_name,
        "issues": state.issues.issue_list(),
        "warnings": list(state.issues.warnings),
        "checked_paths": list(state.issues.checked_paths),
        "missing_paths": list(state.issues.missing_paths),
    }


def write_result_artifact(package_root: Path, payload: dict[str, Any]) -> Path:
    artifact_path = package_root / RESULT_FILENAME
    artifact_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return artifact_path


def print_summary(
    state: ValidationState,
    artifact_path: Path,
) -> None:
    slice_name = state.candidate_slice_name or "<unknown-slice>"
    slice_id = state.candidate_slice_id or "<unknown-id>"
    issue_count = len(state.issues.issue_list())
    print(
        f"slice={slice_name} id={slice_id} status={state.issues.status()} "
        f"issues={issue_count} artifact={artifact_path}"
    )


def check_candidate_package(package_root_arg: str) -> int:
    package_root_path = Path(package_root_arg).expanduser()
    try:
        package_root = package_root_path.resolve(strict=True)
    except FileNotFoundError:
        print(f"Candidate package path does not exist: {package_root_path}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"Candidate package path is unreadable: {package_root_path} ({exc})", file=sys.stderr)
        return 2

    if not package_root.is_dir():
        print(f"Candidate package path is not a directory: {package_root}", file=sys.stderr)
        return 2

    declaration_path = package_root / DECLARATION_FILENAME
    state = ValidationState(package_root=package_root)

    check_package_directories(state)

    declaration: Any = None
    if not declaration_path.exists():
        state.issues.insufficient.append(
            f"Missing required declaration file: {DECLARATION_FILENAME}"
        )
    else:
        add_unique(state.issues.checked_paths, DECLARATION_FILENAME)
        try:
            declaration = load_json_file(declaration_path)
        except json.JSONDecodeError as exc:
            state.issues.insufficient.append(
                f"{DECLARATION_FILENAME} is not valid JSON: {exc}"
            )
        except OSError as exc:
            state.issues.insufficient.append(
                f"{DECLARATION_FILENAME} could not be read: {exc}"
            )

    if declaration is not None:
        validate_declaration_shape(declaration, state)
        resolved_groups = check_declared_paths(state)
        check_distinctions(state, resolved_groups)

    payload = build_result_payload(state)

    try:
        artifact_path = write_result_artifact(package_root, payload)
    except OSError as exc:
        print(
            f"Unable to write intake result artifact inside {package_root}: {exc}",
            file=sys.stderr,
        )
        return 2

    print_summary(state, artifact_path)

    return 0 if state.issues.status() == STATUS_ACCEPTED else 1


def main(argv: Sequence[str]) -> int:
    if len(argv) != 2:
        print_usage()
        return 2
    return check_candidate_package(argv[1])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
