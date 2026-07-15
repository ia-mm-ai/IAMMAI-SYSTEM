"""
Bounded shared v1 implementation-local conformance helper.

This module provides one additive shared surface for schema loading, canonical
body validation, bounded relation-level conformance checks, and expectation-
aware result shaping for future proof-slice runners.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_DIR = REPO_ROOT / "v1" / "schemas"

ORDINARY_SCHEMA_NAMES: Tuple[str, ...] = (
    "validation_artifact",
    "witness_artifact",
    "governance_action",
    "transition_record",
    "state_record",
)
CONTINUITY_SCHEMA_NAME = "continuity_turn"
DEFAULT_SCHEMA_NAMES: Tuple[str, ...] = ORDINARY_SCHEMA_NAMES + (CONTINUITY_SCHEMA_NAME,)


@dataclass(frozen=True)
class SchemaSpec:
    schema_name: str
    artifact_family: str
    filename: str


@dataclass(frozen=True)
class LoadedSchema:
    spec: SchemaSpec
    path: Path
    schema: Dict[str, Any]
    validator: Any


@dataclass(frozen=True)
class ConformanceIssue:
    message: str
    validator: Optional[str] = None
    instance_path: Tuple[Any, ...] = ()
    schema_path: Tuple[Any, ...] = ()

    def as_record(self) -> Dict[str, Any]:
        record: Dict[str, Any] = {"message": self.message}
        if self.validator is not None:
            record["validator"] = self.validator
        if self.instance_path:
            record["instance_path"] = list(self.instance_path)
        if self.schema_path:
            record["schema_path"] = list(self.schema_path)
        return record


@dataclass(frozen=True)
class ConformanceResult:
    surface: str
    artifact_family: str
    conformance_kind: str
    status: str
    expected_status: str
    matched_expectation: bool
    checked_at: str
    fixture_classification: Optional[str] = None
    schema_name: Optional[str] = None
    schema_ref: Optional[str] = None
    references: Dict[str, str] = field(default_factory=dict)
    errors: Tuple[ConformanceIssue, ...] = ()

    def as_record(self) -> Dict[str, Any]:
        record: Dict[str, Any] = {
            "surface": self.surface,
            "artifact_family": self.artifact_family,
            "conformance_kind": self.conformance_kind,
            "expected_status": self.expected_status,
            "status": self.status,
            "matched_expectation": self.matched_expectation,
            "checked_at": self.checked_at,
            "errors": [issue.as_record() for issue in self.errors],
        }
        if self.fixture_classification is not None:
            record["fixture_classification"] = self.fixture_classification
        if self.schema_name is not None:
            record["schema_name"] = self.schema_name
        if self.schema_ref is not None:
            record["schema_ref"] = self.schema_ref
        for key, value in sorted(self.references.items()):
            record[key] = value
        return record


@dataclass(frozen=True)
class SchemaCatalog:
    loaded_schemas: Dict[str, LoadedSchema]

    def get(self, schema_name: str) -> LoadedSchema:
        if schema_name not in self.loaded_schemas:
            raise UnknownSchemaError(
                f"Unknown schema {schema_name!r}. "
                f"Known schemas are: {', '.join(sorted(self.loaded_schemas))}."
            )
        return self.loaded_schemas[schema_name]


SCHEMA_SPECS: Dict[str, SchemaSpec] = {
    "validation_artifact": SchemaSpec(
        schema_name="validation_artifact",
        artifact_family="validation_artifact",
        filename="validation_artifact.schema.json",
    ),
    "witness_artifact": SchemaSpec(
        schema_name="witness_artifact",
        artifact_family="witness_artifact",
        filename="witness_artifact.schema.json",
    ),
    "governance_action": SchemaSpec(
        schema_name="governance_action",
        artifact_family="governance_action",
        filename="governance_action.schema.json",
    ),
    "transition_record": SchemaSpec(
        schema_name="transition_record",
        artifact_family="transition_record",
        filename="transition_record.schema.json",
    ),
    "state_record": SchemaSpec(
        schema_name="state_record",
        artifact_family="state_record",
        filename="state_record.schema.json",
    ),
    "continuity_turn": SchemaSpec(
        schema_name="continuity_turn",
        artifact_family="continuity_turn",
        filename="continuity_turn.schema.json",
    ),
}


class ConformanceChecksError(RuntimeError):
    """Base error for the bounded shared conformance surface."""


class MissingJsonSchemaDependency(ConformanceChecksError):
    """Raised when jsonschema is unavailable for schema validation."""


class SchemaLoadError(ConformanceChecksError):
    """Raised when a requested schema cannot be loaded or compiled."""


class UnknownSchemaError(ConformanceChecksError):
    """Raised when a caller requests an unsupported schema name."""


class InvalidExpectedStatusError(ConformanceChecksError):
    """Raised when expectation handling receives an unsupported status."""


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def repo_relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def load_schema_catalog(
    schema_names: Optional[Sequence[str]] = None,
) -> SchemaCatalog:
    """
    Load and compile the bounded v1 schemas needed by proof-slice runners.

    When `schema_names` is omitted, all ordinary and continuity schemas are
    loaded. This function raises clearly if `jsonschema` is unavailable or if
    any selected schema file cannot be read or compiled.
    """

    validator_for, format_checker_class = _load_validator_tools()
    selected_names = _selected_schema_names(schema_names)
    loaded_schemas: Dict[str, LoadedSchema] = {}

    for schema_name in selected_names:
        spec = SCHEMA_SPECS[schema_name]
        schema_path = SCHEMA_DIR / spec.filename
        if not schema_path.is_file():
            raise SchemaLoadError(
                "Missing schema file for "
                f"{schema_name!r} at {repo_relative(schema_path)}."
            )

        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SchemaLoadError(
                "Failed to read schema "
                f"{schema_name!r} at {repo_relative(schema_path)}: {exc}"
            ) from exc

        try:
            validator_class = validator_for(schema)
            validator_class.check_schema(schema)
            validator = validator_class(
                schema,
                format_checker=format_checker_class(),
            )
        except Exception as exc:  # pragma: no cover - depends on schema correctness
            raise SchemaLoadError(
                "Failed to compile schema "
                f"{schema_name!r} at {repo_relative(schema_path)}: {exc}"
            ) from exc

        loaded_schemas[schema_name] = LoadedSchema(
            spec=spec,
            path=schema_path,
            schema=schema,
            validator=validator,
        )

    return SchemaCatalog(loaded_schemas=loaded_schemas)


def validate_body(
    schema_catalog: SchemaCatalog,
    schema_name: str,
    body: Mapping[str, Any],
    *,
    body_ref: Optional[str | Path] = None,
    fixture_classification: Optional[str] = None,
    expected_status: str = "pass",
) -> ConformanceResult:
    """
    Validate one canonical body against one bounded v1 schema.

    This helper supports both the five ordinary canonical body families and the
    continuity turn body. Surface naming remains explicit rather than flattening
    ordinary and continuity body validation into one undifferentiated claim.
    """

    loaded_schema = schema_catalog.get(schema_name)
    errors = sorted(
        loaded_schema.validator.iter_errors(body),
        key=lambda error: list(error.path),
    )
    issues = tuple(_issue_from_jsonschema_error(error) for error in errors)

    return _build_result(
        surface=_body_surface_for_schema(schema_name),
        artifact_family=loaded_schema.spec.artifact_family,
        conformance_kind="schema_validation",
        expected_status=expected_status,
        fixture_classification=fixture_classification,
        schema_name=loaded_schema.spec.schema_name,
        schema_path=loaded_schema.path,
        references={"body_ref": body_ref},
        issues=issues,
    )


def validate_ordinary_body(
    schema_catalog: SchemaCatalog,
    artifact_family: str,
    body: Mapping[str, Any],
    *,
    body_ref: Optional[str | Path] = None,
    fixture_classification: Optional[str] = None,
    expected_status: str = "pass",
) -> ConformanceResult:
    """Validate one ordinary canonical body against its v1 schema."""

    if artifact_family not in ORDINARY_SCHEMA_NAMES:
        raise UnknownSchemaError(
            f"{artifact_family!r} is not an ordinary artifact schema. "
            f"Known ordinary schemas are: {', '.join(ORDINARY_SCHEMA_NAMES)}."
        )
    return validate_body(
        schema_catalog,
        artifact_family,
        body,
        body_ref=body_ref,
        fixture_classification=fixture_classification,
        expected_status=expected_status,
    )


def validate_continuity_body(
    schema_catalog: SchemaCatalog,
    body: Mapping[str, Any],
    *,
    body_ref: Optional[str | Path] = None,
    fixture_classification: Optional[str] = None,
    expected_status: str = "pass",
) -> ConformanceResult:
    """Validate one canonical continuity turn body against the v1 schema."""

    return validate_body(
        schema_catalog,
        CONTINUITY_SCHEMA_NAME,
        body,
        body_ref=body_ref,
        fixture_classification=fixture_classification,
        expected_status=expected_status,
    )


def check_envelope_bearing_conformance(
    artifact_family: str,
    envelope_object: Mapping[str, Any],
    canonical_body: Mapping[str, Any],
    *,
    execution_identity: str,
    canonical_body_ref: str | Path,
    envelope_ref: Optional[str | Path] = None,
    fixture_classification: Optional[str] = None,
    expected_status: str = "pass",
) -> ConformanceResult:
    """
    Check bounded ordinary envelope-bearing conformance.

    This validates the explicit distinction between carried canonical body and
    execution-bearing envelope without pretending the combined object is itself
    canonical body validation.
    """

    expected_body_ref = _normalize_reference(canonical_body_ref)
    issues = []

    envelope = envelope_object.get("envelope")
    carried_body = envelope_object.get("body")

    if not isinstance(envelope, dict):
        issues.append(ConformanceIssue(message="Missing explicit envelope object."))
    if not isinstance(carried_body, dict):
        issues.append(ConformanceIssue(message="Missing explicit carried body object."))

    if isinstance(envelope, dict):
        if envelope.get("execution_id") != execution_identity:
            issues.append(
                ConformanceIssue(
                    message="Envelope execution identity does not match the expected execution identity."
                )
            )
        if envelope.get("artifact_family") != artifact_family:
            issues.append(
                ConformanceIssue(
                    message="Envelope artifact family does not match the carried family."
                )
            )
        if envelope.get("canonical_body_ref") != expected_body_ref:
            issues.append(
                ConformanceIssue(
                    message="Envelope canonical_body_ref does not point to the preserved canonical body."
                )
            )

    if isinstance(carried_body, dict):
        if carried_body != canonical_body:
            issues.append(
                ConformanceIssue(
                    message="Envelope body does not match the preserved canonical body."
                )
            )
        if "run_id" in carried_body or "execution_id" in carried_body:
            issues.append(
                ConformanceIssue(
                    message="Carried body illegally contains execution identity inside canonical body content."
                )
            )

    return _build_result(
        surface="envelope_bearing_conformance",
        artifact_family=artifact_family,
        conformance_kind="relation_check",
        expected_status=expected_status,
        fixture_classification=fixture_classification,
        references={
            "envelope_ref": envelope_ref,
            "canonical_body_ref": expected_body_ref,
        },
        issues=tuple(issues),
    )


def check_execution_relation_conformance(
    execution_relation: Mapping[str, Any],
    *,
    execution_identity: str,
    continuity_turn_identity: str,
    continuity_body_ref: str | Path,
    execution_relation_ref: Optional[str | Path] = None,
    anchor_source_run_ref: Optional[str | Path] = None,
    predecessor_source_run_ref: Optional[str | Path] = None,
    predecessor_turn_ref: Optional[str] = None,
    fixture_classification: Optional[str] = None,
    expected_status: str = "pass",
) -> ConformanceResult:
    """
    Check bounded continuity execution-relation conformance.

    This validates explicit execution relation as execution relation rather than
    continuity body, and preserves anchor and predecessor checks only where the
    caller says they are relevant to the current continuity slice.
    """

    expected_body_ref = _normalize_reference(continuity_body_ref)
    normalized_anchor_run_ref = _normalize_optional_reference(anchor_source_run_ref)
    normalized_predecessor_source_run_ref = _normalize_optional_reference(
        predecessor_source_run_ref
    )
    issues = []

    if execution_relation.get("relation_type") != "continuity_execution_relation":
        issues.append(
            ConformanceIssue(message="Execution relation type is missing or incorrect.")
        )
    if execution_relation.get("execution_identity") != execution_identity:
        issues.append(
            ConformanceIssue(
                message="Execution relation does not preserve the expected execution identity."
            )
        )
    if execution_relation.get("continuity_turn_identity") != continuity_turn_identity:
        issues.append(
            ConformanceIssue(
                message="Execution relation does not point to the expected continuity turn identity."
            )
        )
    if execution_relation.get("continuity_body_ref") != expected_body_ref:
        issues.append(
            ConformanceIssue(
                message="Execution relation does not point to the preserved continuity body."
            )
        )
    if (
        normalized_anchor_run_ref is not None
        and execution_relation.get("anchor_source_run_ref") != normalized_anchor_run_ref
    ):
        issues.append(
            ConformanceIssue(
                message="Execution relation does not preserve the expected ordinary anchor run."
            )
        )
    if (
        normalized_predecessor_source_run_ref is not None
        and execution_relation.get("predecessor_source_run_ref")
        != normalized_predecessor_source_run_ref
    ):
        issues.append(
            ConformanceIssue(
                message="Execution relation does not preserve the expected predecessor continuity run."
            )
        )
    if (
        predecessor_turn_ref is not None
        and execution_relation.get("predecessor_turn_ref") != predecessor_turn_ref
    ):
        issues.append(
            ConformanceIssue(
                message="Execution relation does not preserve the expected predecessor continuity turn."
            )
        )
    if "body" in execution_relation or "continuity_body" in execution_relation:
        issues.append(
            ConformanceIssue(
                message="Execution relation must not embed the continuity body inline."
            )
        )

    return _build_result(
        surface="execution_relation_conformance",
        artifact_family="continuity_turn",
        conformance_kind="relation_check",
        expected_status=expected_status,
        fixture_classification=fixture_classification,
        references={
            "execution_relation_ref": execution_relation_ref,
            "continuity_body_ref": expected_body_ref,
            "anchor_source_run_ref": normalized_anchor_run_ref,
            "predecessor_source_run_ref": normalized_predecessor_source_run_ref,
            "predecessor_turn_ref": predecessor_turn_ref,
        },
        issues=tuple(issues),
    )


def _load_validator_tools() -> Tuple[Any, Any]:
    try:
        from jsonschema import FormatChecker
        from jsonschema.validators import validator_for
    except ImportError as exc:  # pragma: no cover - dependency posture only
        raise MissingJsonSchemaDependency(
            "This helper requires the 'jsonschema' package. "
            "Install it with 'python -m pip install jsonschema' and rerun."
        ) from exc

    return validator_for, FormatChecker


def _selected_schema_names(schema_names: Optional[Sequence[str]]) -> Tuple[str, ...]:
    if schema_names is None:
        return DEFAULT_SCHEMA_NAMES

    ordered_names = []
    seen = set()
    for schema_name in schema_names:
        if schema_name in seen:
            continue
        if schema_name not in SCHEMA_SPECS:
            raise UnknownSchemaError(
                f"Unknown schema {schema_name!r}. "
                f"Known schemas are: {', '.join(sorted(SCHEMA_SPECS))}."
            )
        ordered_names.append(schema_name)
        seen.add(schema_name)
    return tuple(ordered_names)


def _body_surface_for_schema(schema_name: str) -> str:
    if schema_name == CONTINUITY_SCHEMA_NAME:
        return "continuity_body_conformance"
    return "canonical_body_conformance"


def _issue_from_jsonschema_error(error: Any) -> ConformanceIssue:
    return ConformanceIssue(
        message=error.message,
        validator=getattr(error, "validator", None),
        instance_path=tuple(getattr(error, "path", ())),
        schema_path=tuple(getattr(error, "schema_path", ())),
    )


def _build_result(
    *,
    surface: str,
    artifact_family: str,
    conformance_kind: str,
    expected_status: str,
    fixture_classification: Optional[str],
    issues: Tuple[ConformanceIssue, ...],
    schema_name: Optional[str] = None,
    schema_path: Optional[Path] = None,
    references: Optional[Mapping[str, Optional[str | Path]]] = None,
) -> ConformanceResult:
    normalized_expected_status = _normalize_expected_status(expected_status)
    status = "pass" if not issues else "fail"
    normalized_references = _normalize_references(references or {})

    return ConformanceResult(
        surface=surface,
        artifact_family=artifact_family,
        conformance_kind=conformance_kind,
        status=status,
        expected_status=normalized_expected_status,
        matched_expectation=status == normalized_expected_status,
        checked_at=utc_now(),
        fixture_classification=fixture_classification,
        schema_name=schema_name,
        schema_ref=repo_relative(schema_path) if schema_path is not None else None,
        references=normalized_references,
        errors=issues,
    )


def _normalize_expected_status(expected_status: str) -> str:
    if expected_status not in {"pass", "fail"}:
        raise InvalidExpectedStatusError(
            f"Unsupported expected status {expected_status!r}. "
            "Expected status must be either 'pass' or 'fail'."
        )
    return expected_status


def _normalize_references(
    references: Mapping[str, Optional[str | Path]],
) -> Dict[str, str]:
    normalized: Dict[str, str] = {}
    for key, value in references.items():
        if value is None:
            continue
        normalized[key] = _normalize_reference(value)
    return normalized


def _normalize_optional_reference(value: Optional[str | Path]) -> Optional[str]:
    if value is None:
        return None
    return _normalize_reference(value)


def _normalize_reference(value: str | Path) -> str:
    if isinstance(value, Path):
        return repo_relative(value)
    return value


__all__ = [
    "CONTINUITY_SCHEMA_NAME",
    "DEFAULT_SCHEMA_NAMES",
    "ORDINARY_SCHEMA_NAMES",
    "ConformanceChecksError",
    "ConformanceIssue",
    "ConformanceResult",
    "InvalidExpectedStatusError",
    "LoadedSchema",
    "MissingJsonSchemaDependency",
    "SchemaCatalog",
    "SchemaLoadError",
    "SchemaSpec",
    "UnknownSchemaError",
    "check_envelope_bearing_conformance",
    "check_execution_relation_conformance",
    "load_schema_catalog",
    "repo_relative",
    "utc_now",
    "validate_body",
    "validate_continuity_body",
    "validate_ordinary_body",
]
