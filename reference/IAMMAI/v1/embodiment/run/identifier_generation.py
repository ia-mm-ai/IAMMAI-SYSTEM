"""
Bounded shared v1 implementation-local identifier-generation helper.

This module provides one additive shared surface for generating bounded
implementation-local identities for future proof-slice runners without
rewriting earlier runners, mutating earlier outputs, or claiming final
protocol-law identifier syntax.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Mapping, Tuple
from uuid import uuid4


@dataclass(frozen=True)
class IdentitySpec:
    """
    Implementation-local identifier specification for one identity class.

    The prefix is an implementation-local class marker only. It exists to keep
    identity classes readable and distinct without claiming final protocol law.
    """

    identity_class: str
    prefix: str
    description: str

    def new_id(self) -> str:
        return f"{self.prefix}-{uuid4().hex}"


class IdentifierGenerationError(RuntimeError):
    """Base error for the bounded shared identifier-generation surface."""


class UnknownArtifactFamilyError(IdentifierGenerationError):
    """Raised when an unsupported ordinary artifact family is requested."""


class UnknownContextKindError(IdentifierGenerationError):
    """Raised when an unsupported context identity kind is requested."""


_EXECUTION_SPEC = IdentitySpec(
    identity_class="execution",
    prefix="execution",
    description="Execution-run identity for bounded runtime occurrence.",
)

_MATTER_SPEC = IdentitySpec(
    identity_class="matter",
    prefix="matter",
    description="Matter identity for bounded matter relation.",
)

_CONTINUITY_TURN_SPEC = IdentitySpec(
    identity_class="continuity_turn",
    prefix="continuity-turn",
    description="Canonical continuity-turn identity.",
)

_EXECUTION_RELATION_SPEC = IdentitySpec(
    identity_class="execution_relation",
    prefix="execution-relation",
    description="Explicit execution-relation identity.",
)

_ORDINARY_ARTIFACT_SPECS: Dict[str, IdentitySpec] = {
    "validation_artifact": IdentitySpec(
        identity_class="ordinary_artifact",
        prefix="validation",
        description="Canonical validation-artifact identity.",
    ),
    "witness_artifact": IdentitySpec(
        identity_class="ordinary_artifact",
        prefix="witness",
        description="Canonical witness-artifact identity.",
    ),
    "governance_action": IdentitySpec(
        identity_class="ordinary_artifact",
        prefix="governance_action",
        description="Canonical governance-action identity.",
    ),
    "transition_record": IdentitySpec(
        identity_class="ordinary_artifact",
        prefix="transition",
        description="Canonical transition-record identity.",
    ),
    "state_record": IdentitySpec(
        identity_class="ordinary_artifact",
        prefix="state",
        description="Canonical state-record identity.",
    ),
}

_ORDINARY_ARTIFACT_ALIASES: Dict[str, str] = {
    "validation": "validation_artifact",
    "validation_artifact": "validation_artifact",
    "witness": "witness_artifact",
    "witness_artifact": "witness_artifact",
    "governance_action": "governance_action",
    "transition": "transition_record",
    "transition_record": "transition_record",
    "state": "state_record",
    "state_record": "state_record",
}

_CONTEXT_SPECS: Dict[str, IdentitySpec] = {
    "preservation": IdentitySpec(
        identity_class="context",
        prefix="preservation",
        description="Preservation-context identity.",
    ),
    "source_note": IdentitySpec(
        identity_class="context",
        prefix="source-note",
        description="Structured source-note identity.",
    ),
    "manifest": IdentitySpec(
        identity_class="context",
        prefix="manifest",
        description="Preservation-manifest identity.",
    ),
    "anchor_source_note": IdentitySpec(
        identity_class="context",
        prefix="anchor-source-note",
        description="Anchor-source-note identity for bounded continuity context.",
    ),
    "state_preparation_threshold": IdentitySpec(
        identity_class="context",
        prefix="state-preparation-threshold",
        description="Bounded preparatory state reference for ordinary proof-slice work.",
    ),
}

_CONTEXT_ALIASES: Dict[str, str] = {
    "preservation": "preservation",
    "source_note": "source_note",
    "source-note": "source_note",
    "manifest": "manifest",
    "anchor_source_note": "anchor_source_note",
    "anchor-source-note": "anchor_source_note",
    "state_preparation_threshold": "state_preparation_threshold",
    "state-preparation-threshold": "state_preparation_threshold",
}

ORDINARY_ARTIFACT_FAMILIES: Tuple[str, ...] = (
    "validation_artifact",
    "witness_artifact",
    "governance_action",
    "transition_record",
    "state_record",
)

CONTEXT_KINDS: Tuple[str, ...] = (
    "preservation",
    "source_note",
    "manifest",
    "anchor_source_note",
    "state_preparation_threshold",
)


def new_execution_id() -> str:
    """Generate a new execution-run identity."""

    return _EXECUTION_SPEC.new_id()


def new_artifact_id(artifact_family: str) -> str:
    """
    Generate a new canonical ordinary-artifact identity.

    This is an implementation-local helper for the five ordinary v1 artifact
    families only. Continuity-turn identity remains continuity-specific.
    """

    return new_ordinary_artifact_id(artifact_family)


def new_ordinary_artifact_id(artifact_family: str) -> str:
    """Generate a new canonical ordinary-artifact identity by family."""

    return _ordinary_artifact_spec(artifact_family).new_id()


def new_validation_artifact_id() -> str:
    """Generate a new canonical validation-artifact identity."""

    return _ORDINARY_ARTIFACT_SPECS["validation_artifact"].new_id()


def new_witness_artifact_id() -> str:
    """Generate a new canonical witness-artifact identity."""

    return _ORDINARY_ARTIFACT_SPECS["witness_artifact"].new_id()


def new_governance_action_id() -> str:
    """Generate a new canonical governance-action identity."""

    return _ORDINARY_ARTIFACT_SPECS["governance_action"].new_id()


def new_transition_record_id() -> str:
    """Generate a new canonical transition-record identity."""

    return _ORDINARY_ARTIFACT_SPECS["transition_record"].new_id()


def new_state_record_id() -> str:
    """Generate a new canonical state-record identity."""

    return _ORDINARY_ARTIFACT_SPECS["state_record"].new_id()


def new_continuity_turn_id() -> str:
    """Generate a new canonical continuity-turn identity."""

    return _CONTINUITY_TURN_SPEC.new_id()


def new_matter_id() -> str:
    """Generate a new matter identity."""

    return _MATTER_SPEC.new_id()


def new_execution_relation_id() -> str:
    """Generate a new explicit execution-relation identity."""

    return _EXECUTION_RELATION_SPEC.new_id()


def new_preservation_id() -> str:
    """Generate a new preservation-context identity."""

    return _CONTEXT_SPECS["preservation"].new_id()


def new_source_note_id() -> str:
    """Generate a new source-note identity."""

    return _CONTEXT_SPECS["source_note"].new_id()


def new_manifest_id() -> str:
    """Generate a new manifest identity."""

    return _CONTEXT_SPECS["manifest"].new_id()


def new_context_id(kind: str) -> str:
    """
    Generate a new secondary context identity by supported kind.

    Context identities are useful for bounded implementation-local support
    objects such as manifests, source notes, and preparatory context records.
    They are not substitutes for canonical artifact, continuity, matter, or
    execution identities.
    """

    return _context_spec(kind).new_id()


def ordinary_artifact_specs() -> Mapping[str, IdentitySpec]:
    """Return the bounded ordinary-artifact identity specs by canonical family."""

    return dict(_ORDINARY_ARTIFACT_SPECS)


def context_specs() -> Mapping[str, IdentitySpec]:
    """Return the bounded secondary context-identity specs by canonical kind."""

    return dict(_CONTEXT_SPECS)


def _ordinary_artifact_spec(artifact_family: str) -> IdentitySpec:
    normalized_family = _normalize_key(artifact_family)
    if normalized_family is None or normalized_family not in _ORDINARY_ARTIFACT_ALIASES:
        raise UnknownArtifactFamilyError(
            f"Unknown ordinary artifact family {artifact_family!r}. "
            "Supported families are: "
            + ", ".join(ORDINARY_ARTIFACT_FAMILIES)
            + "."
        )
    canonical_family = _ORDINARY_ARTIFACT_ALIASES[normalized_family]
    return _ORDINARY_ARTIFACT_SPECS[canonical_family]


def _context_spec(kind: str) -> IdentitySpec:
    normalized_kind = _normalize_key(kind)
    if normalized_kind is None or normalized_kind not in _CONTEXT_ALIASES:
        raise UnknownContextKindError(
            f"Unknown context identity kind {kind!r}. "
            "Supported kinds are: "
            + ", ".join(CONTEXT_KINDS)
            + "."
        )
    canonical_kind = _CONTEXT_ALIASES[normalized_kind]
    return _CONTEXT_SPECS[canonical_kind]


def _normalize_key(value: str) -> str | None:
    stripped = value.strip()
    if not stripped:
        return None
    return stripped


__all__ = [
    "CONTEXT_KINDS",
    "ORDINARY_ARTIFACT_FAMILIES",
    "IdentifierGenerationError",
    "IdentitySpec",
    "UnknownArtifactFamilyError",
    "UnknownContextKindError",
    "context_specs",
    "new_artifact_id",
    "new_context_id",
    "new_continuity_turn_id",
    "new_execution_id",
    "new_execution_relation_id",
    "new_governance_action_id",
    "new_manifest_id",
    "new_matter_id",
    "new_ordinary_artifact_id",
    "new_preservation_id",
    "new_source_note_id",
    "new_state_record_id",
    "new_transition_record_id",
    "new_validation_artifact_id",
    "new_witness_artifact_id",
    "ordinary_artifact_specs",
]
