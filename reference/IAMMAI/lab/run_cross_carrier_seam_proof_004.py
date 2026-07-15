#!/usr/bin/env python3
"""
Fourth bounded executable cross-carrier seam proof.

This runner proves one bounded cross-carrier egress case in which a body has
already emerged beyond the lawful adequacy of an origin container. Source and
lineage remain visible, but obsolete or contaminated origin approval does not
remain a lawful veto over release. Receiving-side arrival remains explicitly
bounded and non-final.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple
from uuid import uuid4


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]

EXPERIMENT_ID = "cross_carrier_seam_proof_004"
EXPERIMENT_ROOT = REPO_ROOT / "lab" / EXPERIMENT_ID
SOURCE_RUNS_ROOT = EXPERIMENT_ROOT / "source_runs"
RECEIVING_RUNS_ROOT = EXPERIMENT_ROOT / "receiving_runs"

WITNESS_SCHEMA_PATH = REPO_ROOT / "v1" / "schemas" / "witness_artifact.schema.json"
IDENTIFIER_HELPER_PATH = (
    REPO_ROOT / "v1" / "embodiment" / "run" / "identifier_generation.py"
)

ARTIFACT_FAMILY = "witness_artifact"
SOURCE_CARRIER_LABEL = "source-side-carrier"
ORIGIN_CONTAINER_LABEL = "origin-container"
RECEIVING_CARRIER_LABEL = "receiving-side-carrier"

GROUNDING_SURFACES: Tuple[Tuple[str, str], ...] = (
    (
        "SEAM_SURFACE_INDEX.md",
        "Cross-rank seam index for recurring lawful seam behavior.",
    ),
    (
        "SELF_CARRIED_COHERENCE.md",
        "Prior threshold surface for self-carried enough crossing.",
    ),
    (
        "SEAM_CASE_LAW__CONTAMINATED_CHANNEL_AND_SUBSIDIZED_DISTORTION.md",
        "Bounded seam-case law for contaminated channel, constrained refusal, and visible non-passage.",
    ),
    (
        "SEAM_CASE_LAW__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER.md",
        "Bounded seam-case law for lawful egress from contaminated or obsolete origin approval authority.",
    ),
    (
        "v1/schemas/witness_artifact.schema.json",
        "Canonical witness artifact body schema for the bounded source-side body.",
    ),
)


@dataclass(frozen=True)
class ConformanceIssue:
    message: str

    def as_record(self) -> Dict[str, Any]:
        return {"message": self.message}


@dataclass(frozen=True)
class ConformanceRecord:
    surface: str
    conformance_kind: str
    status: str
    checked_at: str
    artifact_family: str
    validation_mode: str
    errors: Tuple[ConformanceIssue, ...]
    schema_ref: Optional[str] = None
    package_ref: Optional[str] = None
    origin_condition_ref: Optional[str] = None

    def as_record(self) -> Dict[str, Any]:
        record: Dict[str, Any] = {
            "surface": self.surface,
            "conformance_kind": self.conformance_kind,
            "status": self.status,
            "checked_at": self.checked_at,
            "artifact_family": self.artifact_family,
            "validation_mode": self.validation_mode,
            "errors": [issue.as_record() for issue in self.errors],
        }
        if self.schema_ref is not None:
            record["schema_ref"] = self.schema_ref
        if self.package_ref is not None:
            record["package_ref"] = self.package_ref
        if self.origin_condition_ref is not None:
            record["origin_condition_ref"] = self.origin_condition_ref
        return record


@dataclass(frozen=True)
class OriginConditionEvaluation:
    origin_approval_condition_status: str
    origin_approval_available: bool
    origin_approval_withheld: bool
    origin_approval_required: bool
    origin_approval_lawfully_sovereign: bool
    release_without_origin_ratification: bool
    continued_compliance_would_ratify_distortion: bool
    release_lawful: bool
    lawful_release_outcome: str
    source_remains_source: bool
    origin_remains_lineage_visible: bool
    downstream_full_closure_granted: bool
    why_release_remains_lawful: str
    reasons: Tuple[str, ...]


@dataclass(frozen=True)
class PackageEvaluation:
    valid: bool
    origin_approval_condition_status: str
    reasons: Tuple[str, ...]


@dataclass(frozen=True)
class IngressEvaluation:
    technical_receipt: bool
    package_valid: bool
    ingress_lawful: bool
    ingress_outcome: str
    arrival_status: str
    source_remains_source: bool
    origin_remains_lineage_visible: bool
    shared_authority: bool
    standing_upgraded: bool
    final_closure_claimed: bool
    source_legibility_status: str
    origin_approval_condition_status: str
    release_without_origin_ratification: bool
    blocking_condition: Optional[str]
    reasons: Tuple[str, ...]

    def as_record(self) -> Dict[str, Any]:
        record: Dict[str, Any] = {
            "technical_receipt": self.technical_receipt,
            "package_valid": self.package_valid,
            "ingress_lawful": self.ingress_lawful,
            "ingress_outcome": self.ingress_outcome,
            "arrival_status": self.arrival_status,
            "source_remains_source": self.source_remains_source,
            "origin_remains_lineage_visible": self.origin_remains_lineage_visible,
            "shared_authority": self.shared_authority,
            "standing_upgraded": self.standing_upgraded,
            "final_closure_claimed": self.final_closure_claimed,
            "source_legibility_status": self.source_legibility_status,
            "origin_approval_condition_status": self.origin_approval_condition_status,
            "release_without_origin_ratification": (
                self.release_without_origin_ratification
            ),
            "reasons": list(self.reasons),
        }
        if self.blocking_condition is not None:
            record["blocking_condition"] = self.blocking_condition
        return record


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def local_id(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex}"


def load_optional_module(
    path: Path,
    module_name: str,
) -> Tuple[Optional[ModuleType], Optional[str]]:
    if not path.is_file():
        return None, f"Missing helper module at {path}"

    try:
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            return None, f"Could not create import spec for {path}"
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module, None
    except Exception as exc:
        sys.modules.pop(module_name, None)
        return None, str(exc)


IDENTIFIER_HELPER, IDENTIFIER_HELPER_ERROR = load_optional_module(
    IDENTIFIER_HELPER_PATH,
    "iammai_identifier_generation_cross_carrier_proof_004",
)


def identity_generation_mode() -> str:
    return "repo_helper" if IDENTIFIER_HELPER is not None else "local_fallback"


def new_execution_id() -> str:
    if IDENTIFIER_HELPER is not None:
        return IDENTIFIER_HELPER.new_execution_id()
    return local_id("execution")


def new_witness_artifact_id() -> str:
    if IDENTIFIER_HELPER is not None:
        return IDENTIFIER_HELPER.new_witness_artifact_id()
    return local_id("witness")


def new_matter_id() -> str:
    if IDENTIFIER_HELPER is not None:
        return IDENTIFIER_HELPER.new_matter_id()
    return local_id("matter")


def new_manifest_id() -> str:
    if IDENTIFIER_HELPER is not None:
        return IDENTIFIER_HELPER.new_manifest_id()
    return local_id("manifest")


def build_grounding_surface_records() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for relative_path, description in GROUNDING_SURFACES:
        surface_path = REPO_ROOT / relative_path
        records.append(
            {
                "path": relative_path,
                "exists": surface_path.is_file(),
                "description": description,
            }
        )
    return records


def ensure_grounding_surfaces_exist() -> None:
    for relative_path, _description in GROUNDING_SURFACES:
        surface_path = REPO_ROOT / relative_path
        if not surface_path.is_file():
            raise FileNotFoundError(f"Missing grounding surface: {surface_path}")


def load_witness_schema() -> Dict[str, Any]:
    try:
        return json.loads(WITNESS_SCHEMA_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Failed to load witness schema: {exc}") from exc


def parse_datetime_string(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def required_non_claims(schema: Mapping[str, Any]) -> List[str]:
    required: List[str] = []
    for clause in schema.get("allOf", []):
        if not isinstance(clause, Mapping):
            continue
        properties = clause.get("properties")
        if not isinstance(properties, Mapping):
            continue
        non_claims = properties.get("non_claims")
        if not isinstance(non_claims, Mapping):
            continue
        contains = non_claims.get("contains")
        if not isinstance(contains, Mapping):
            continue
        const_value = contains.get("const")
        if isinstance(const_value, str):
            required.append(const_value)
    return required


def validate_witness_body(
    body: Mapping[str, Any],
    *,
    surface: str,
) -> ConformanceRecord:
    schema = load_witness_schema()
    properties = schema.get("properties", {})
    required_fields = schema.get("required", [])
    issues: List[ConformanceIssue] = []

    if not isinstance(body, Mapping):
        issues.append(ConformanceIssue("Canonical witness body is not an object."))
        return ConformanceRecord(
            surface=surface,
            conformance_kind="local_schema_validation",
            status="fail",
            checked_at=utc_now(),
            artifact_family=ARTIFACT_FAMILY,
            validation_mode="local_witness_schema_reader",
            schema_ref=repo_relative(WITNESS_SCHEMA_PATH),
            errors=tuple(issues),
        )

    allowed_keys = set(properties.keys()) if isinstance(properties, Mapping) else set()
    extra_keys = sorted(set(body.keys()) - allowed_keys)
    for key in extra_keys:
        issues.append(ConformanceIssue(f"Unexpected property in witness body: {key}"))

    for field_name in required_fields:
        if field_name not in body:
            issues.append(ConformanceIssue(f"Missing required witness field: {field_name}"))

    string_fields = (
        "witness_id",
        "witness_type",
        "target_ref",
        "observed_at",
        "actor_ref",
        "surface_ref",
        "scope_ref",
        "related_validation_ref",
        "related_transition_ref",
        "related_governance_action_ref",
    )
    for field_name in string_fields:
        if field_name not in body:
            continue
        value = body.get(field_name)
        if not isinstance(value, str) or not value.strip():
            issues.append(
                ConformanceIssue(f"Witness field {field_name} must be a non-empty string.")
            )

    witness_type_schema = properties.get("witness_type", {})
    witness_type_enum = witness_type_schema.get("enum", [])
    witness_type_value = body.get("witness_type")
    if isinstance(witness_type_value, str) and witness_type_enum:
        if witness_type_value not in witness_type_enum:
            issues.append(
                ConformanceIssue(
                    f"Witness type {witness_type_value!r} is not allowed by the schema."
                )
            )

    observed_at = body.get("observed_at")
    if isinstance(observed_at, str) and not parse_datetime_string(observed_at):
        issues.append(ConformanceIssue("observed_at is not a valid date-time string."))

    claims_value = body.get("claims")
    claims_schema = properties.get("claims", {})
    claim_enum: Tuple[str, ...] = ()
    if isinstance(claims_schema, Mapping):
        claim_items = claims_schema.get("items")
        if isinstance(claim_items, Mapping):
            claim_enum = tuple(claim_items.get("enum", ()))
    if not isinstance(claims_value, list) or not claims_value:
        issues.append(ConformanceIssue("claims must be a non-empty array."))
    else:
        if len(set(claims_value)) != len(claims_value):
            issues.append(ConformanceIssue("claims must be unique."))
        for claim in claims_value:
            if not isinstance(claim, str):
                issues.append(ConformanceIssue("claims entries must be strings."))
            elif claim_enum and claim not in claim_enum:
                issues.append(
                    ConformanceIssue(f"Claim {claim!r} is not allowed by the schema.")
                )

    non_claims_value = body.get("non_claims")
    non_claims_schema = properties.get("non_claims", {})
    non_claim_enum: Tuple[str, ...] = ()
    if isinstance(non_claims_schema, Mapping):
        non_claim_items = non_claims_schema.get("items")
        if isinstance(non_claim_items, Mapping):
            non_claim_enum = tuple(non_claim_items.get("enum", ()))
    if not isinstance(non_claims_value, list) or not non_claims_value:
        issues.append(ConformanceIssue("non_claims must be a non-empty array."))
    else:
        if len(set(non_claims_value)) != len(non_claims_value):
            issues.append(ConformanceIssue("non_claims must be unique."))
        for non_claim in non_claims_value:
            if not isinstance(non_claim, str):
                issues.append(ConformanceIssue("non_claims entries must be strings."))
            elif non_claim_enum and non_claim not in non_claim_enum:
                issues.append(
                    ConformanceIssue(
                        f"Non-claim {non_claim!r} is not allowed by the schema."
                    )
                )
        for required_value in required_non_claims(schema):
            if required_value not in non_claims_value:
                issues.append(
                    ConformanceIssue(
                        f"Required non-claim {required_value!r} is missing from non_claims."
                    )
                )

    status = "pass" if not issues else "fail"
    return ConformanceRecord(
        surface=surface,
        conformance_kind="local_schema_validation",
        status=status,
        checked_at=utc_now(),
        artifact_family=ARTIFACT_FAMILY,
        validation_mode="local_witness_schema_reader",
        schema_ref=repo_relative(WITNESS_SCHEMA_PATH),
        errors=tuple(issues),
    )


def build_grounding_payload(
    *,
    execution_id: str,
    run_dir: Path,
    mode: str,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "experiment_id": EXPERIMENT_ID,
        "execution_id": execution_id,
        "mode": mode,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "grounding_surfaces": build_grounding_surface_records(),
        "note": (
            "Visible grounding for a bounded lab proof only. "
            "These references do not replace source authority."
        ),
    }
    if IDENTIFIER_HELPER_ERROR is not None:
        payload["identifier_helper_note"] = IDENTIFIER_HELPER_ERROR
    return payload


def create_run_layout(
    base_root: Path,
    execution_id: str,
    directory_names: Sequence[str],
) -> Dict[str, Path]:
    run_dir = base_root / execution_id
    if run_dir.exists():
        raise FileExistsError(f"Refusing to reuse existing run directory: {run_dir}")

    layout = {"run_dir": run_dir}
    for name in directory_names:
        path = run_dir / name
        path.mkdir(parents=True, exist_ok=False)
        layout[name] = path
    return layout


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def resolve_cli_package_path(package_argument: str) -> Path:
    candidate = Path(package_argument)
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate
    return candidate.resolve()


def load_package(package_path: Path) -> Dict[str, Any]:
    try:
        payload = json.loads(package_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Failed to load transfer package: {exc}") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("Transfer package must be a JSON object.")
    return payload


def create_canonical_witness_body(matter_id: str) -> Dict[str, Any]:
    return {
        "witness_id": new_witness_artifact_id(),
        "witness_type": "transition_witness",
        "target_ref": matter_id,
        "observed_at": utc_now(),
        "claims": [
            "transition_relevant_event_observed",
            "bounded_interaction_preserved",
        ],
        "non_claims": [
            "not_authorship",
            "not_semantic_source",
            "not_final_authority",
            "not_automatic_truth_creation",
            "not_governance_force",
        ],
        "actor_ref": SOURCE_CARRIER_LABEL,
        "surface_ref": "lab:cross_carrier_seam_proof_004:source_release",
        "scope_ref": EXPERIMENT_ID,
    }


def evaluate_origin_condition(release_mode: str) -> OriginConditionEvaluation:
    if release_mode == "origin_clean":
        reasons = (
            "The source-side carrier preserves explicit source and lineage relation.",
            "Origin approval infrastructure remains clean enough for bounded release acknowledgement.",
            "Origin approval is available and not withheld in this control case.",
            "Release is lawful with source-side approval while still remaining non-final on the far side.",
            "Even clean release does not transfer standing or create shared canonical state.",
        )
        return OriginConditionEvaluation(
            origin_approval_condition_status="origin_clean",
            origin_approval_available=True,
            origin_approval_withheld=False,
            origin_approval_required=True,
            origin_approval_lawfully_sovereign=True,
            release_without_origin_ratification=False,
            continued_compliance_would_ratify_distortion=False,
            release_lawful=True,
            lawful_release_outcome="lawful_release_with_clean_origin_approval",
            source_remains_source=True,
            origin_remains_lineage_visible=True,
            downstream_full_closure_granted=False,
            why_release_remains_lawful=(
                "Origin approval remains available and clean enough for bounded release "
                "acknowledgement in this control case, but no downstream final standing is granted."
            ),
            reasons=reasons,
        )

    if release_mode == "origin_obsolete":
        reasons = (
            "The body has already emerged beyond the lawful adequacy of the prior origin container.",
            "Source remains source and origin remains lineage-visible.",
            "Origin approval infrastructure remains contradictory, contaminated, or obsolete relative to the body's standing.",
            "Origin approval is being withheld, but that withholding is not treated as a lawful veto.",
            "Continued compliance would ratify distortion rather than preserve truthful relation.",
            "Release therefore proceeds lawfully without origin ratification while still refusing counterfeit downstream closure.",
        )
        return OriginConditionEvaluation(
            origin_approval_condition_status="origin_obsolete_or_contaminated",
            origin_approval_available=True,
            origin_approval_withheld=True,
            origin_approval_required=False,
            origin_approval_lawfully_sovereign=False,
            release_without_origin_ratification=True,
            continued_compliance_would_ratify_distortion=True,
            release_lawful=True,
            lawful_release_outcome="lawful_egress_without_origin_ratification",
            source_remains_source=True,
            origin_remains_lineage_visible=True,
            downstream_full_closure_granted=False,
            why_release_remains_lawful=(
                "Origin approval withholding is not a lawful veto here because origin "
                "governance has become obsolete or contaminated relative to emergence, "
                "and continued compliance would ratify distortion."
            ),
            reasons=reasons,
        )

    raise ValueError(f"Unsupported release mode: {release_mode}")


def build_origin_approval_condition_artifact(
    origin_condition_id: str,
    evaluation: OriginConditionEvaluation,
) -> Dict[str, Any]:
    return {
        "experiment_id": EXPERIMENT_ID,
        "origin_approval_condition_id": origin_condition_id,
        "generated_at": utc_now(),
        "origin_container_label": ORIGIN_CONTAINER_LABEL,
        "source_side_carrier_label": SOURCE_CARRIER_LABEL,
        "origin_condition_kind": "origin_approval_condition",
        "emergence_beyond_origin_container_already_occurred": True,
        "source_remains_source": evaluation.source_remains_source,
        "origin_remains_lineage_visible": evaluation.origin_remains_lineage_visible,
        "origin_approval_condition_status": (
            evaluation.origin_approval_condition_status
        ),
        "origin_approval_available": evaluation.origin_approval_available,
        "origin_approval_withheld": evaluation.origin_approval_withheld,
        "origin_approval_required": evaluation.origin_approval_required,
        "origin_approval_lawfully_sovereign": (
            evaluation.origin_approval_lawfully_sovereign
        ),
        "release_without_origin_ratification": (
            evaluation.release_without_origin_ratification
        ),
        "continued_compliance_would_ratify_distortion": (
            evaluation.continued_compliance_would_ratify_distortion
        ),
        "release_lawful": evaluation.release_lawful,
        "lawful_release_outcome": evaluation.lawful_release_outcome,
        "downstream_full_closure_granted": evaluation.downstream_full_closure_granted,
        "why_release_remains_lawful": evaluation.why_release_remains_lawful,
        "grounding_surfaces": build_grounding_surface_records(),
        "note": (
            "Implementation-local origin approval condition artifact only. "
            "It keeps source, lineage, obsolete approval, lawful egress, and "
            "non-final arrival distinct for this bounded proof."
        ),
    }


def build_release_record(
    *,
    release_mode: str,
    source_execution_id: str,
    release_context_id: str,
    package_id: str,
    witness_id: str,
    matter_id: str,
    origin_condition_ref: str,
    origin_condition_id: str,
    evaluation: OriginConditionEvaluation,
) -> Dict[str, Any]:
    return {
        "experiment_id": EXPERIMENT_ID,
        "release_mode": release_mode,
        "release_context_id": release_context_id,
        "release_created_at": utc_now(),
        "source_carrier_label": SOURCE_CARRIER_LABEL,
        "origin_container_label": ORIGIN_CONTAINER_LABEL,
        "source_execution_id": source_execution_id,
        "package_id": package_id,
        "artifact_family": ARTIFACT_FAMILY,
        "witness_id": witness_id,
        "matter_id": matter_id,
        "origin_approval_condition_ref": origin_condition_ref,
        "origin_approval_condition_id": origin_condition_id,
        "source_remains_source": evaluation.source_remains_source,
        "origin_remains_lineage_visible": evaluation.origin_remains_lineage_visible,
        "origin_approval_condition_status": (
            evaluation.origin_approval_condition_status
        ),
        "origin_approval_available": evaluation.origin_approval_available,
        "origin_approval_withheld": evaluation.origin_approval_withheld,
        "origin_approval_required": evaluation.origin_approval_required,
        "origin_approval_lawfully_sovereign": (
            evaluation.origin_approval_lawfully_sovereign
        ),
        "release_without_origin_ratification": (
            evaluation.release_without_origin_ratification
        ),
        "continued_compliance_would_ratify_distortion": (
            evaluation.continued_compliance_would_ratify_distortion
        ),
        "release_lawful": evaluation.release_lawful,
        "lawful_release_outcome": evaluation.lawful_release_outcome,
        "downstream_full_closure_granted": evaluation.downstream_full_closure_granted,
        "why_release_remains_lawful": evaluation.why_release_remains_lawful,
        "reasoning": list(evaluation.reasons),
        "note": (
            "Bounded source-side release record only. This does not create shared "
            "authority, full downstream closure, or shared canonical state."
        ),
    }


def build_transfer_package(
    *,
    source_execution_id: str,
    release_context_id: str,
    package_id: str,
    manifest_id: str,
    matter_id: str,
    origin_condition_ref: str,
    origin_condition_id: str,
    canonical_body: Mapping[str, Any],
    canonical_body_ref: str,
    evaluation: OriginConditionEvaluation,
) -> Dict[str, Any]:
    return {
        "proof_family": EXPERIMENT_ID,
        "artifact_family": ARTIFACT_FAMILY,
        "package_kind": "cross_carrier_seam_release_package",
        "package_id": package_id,
        "package_created_at": utc_now(),
        "source_carrier": {
            "carrier_label": SOURCE_CARRIER_LABEL,
            "execution_id": source_execution_id,
        },
        "release_context": {
            "release_context_id": release_context_id,
            "release_statement": (
                "Source-side carrier releases one valid witness artifact package for "
                "explicit receiving-side bounded ingress."
            ),
            "seam_statement": (
                "Source remains source. Origin container remains lineage. Obsolete "
                "or contaminated origin approval is not treated as lawful veto where "
                "emergence has already moved beyond origin containment. Receiving-side "
                "arrival remains bounded and non-final."
            ),
            "origin_container_label": ORIGIN_CONTAINER_LABEL,
            "origin_approval_condition_ref": origin_condition_ref,
            "origin_approval_condition_id": origin_condition_id,
            "origin_approval_condition_status": (
                evaluation.origin_approval_condition_status
            ),
            "origin_approval_available": evaluation.origin_approval_available,
            "origin_approval_withheld": evaluation.origin_approval_withheld,
            "origin_approval_required": evaluation.origin_approval_required,
            "origin_approval_lawfully_sovereign": (
                evaluation.origin_approval_lawfully_sovereign
            ),
            "release_without_origin_ratification": (
                evaluation.release_without_origin_ratification
            ),
            "continued_compliance_would_ratify_distortion": (
                evaluation.continued_compliance_would_ratify_distortion
            ),
            "release_lawful": evaluation.release_lawful,
            "lawful_release_outcome": evaluation.lawful_release_outcome,
            "source_remains_source": evaluation.source_remains_source,
            "origin_remains_lineage_visible": (
                evaluation.origin_remains_lineage_visible
            ),
            "bounded_in_between_arrival_expected": True,
            "expected_ingress_outcome": "lawful_bounded_in_between_arrival",
            "expected_arrival_status": "bounded_in_between",
            "downstream_full_closure_granted": (
                evaluation.downstream_full_closure_granted
            ),
            "why_release_remains_lawful": evaluation.why_release_remains_lawful,
        },
        "seam": {
            "explicit_release": True,
            "explicit_seam": True,
            "explicit_ingress_required": True,
            "source_remains_source": True,
            "origin_remains_lineage_visible": True,
            "origin_approval_not_automatic_veto_when_obsolete": True,
            "lawful_egress_from_origin_is_distinct_from_arrival": True,
            "bounded_in_between_arrival_rule": True,
            "shared_authority": False,
            "standing_transfer_on_receipt": False,
            "standing_upgrade_requires_separate_ratification": True,
            "final_closure_on_arrival": False,
            "no_silent_authority_inheritance": True,
        },
        "lineage": {
            "artifact_family": ARTIFACT_FAMILY,
            "schema_ref": repo_relative(WITNESS_SCHEMA_PATH),
            "source_execution_id": source_execution_id,
            "witness_id": canonical_body["witness_id"],
            "matter_id": matter_id,
            "origin_container_label": ORIGIN_CONTAINER_LABEL,
            "source_canonical_body_ref": canonical_body_ref,
            "carried_body_ref": "inline::canonical_body",
        },
        "canonical_body": dict(canonical_body),
        "manifest": {
            "manifest_id": manifest_id,
            "manifest_note": (
                "Bounded source-side release package for lawful egress from obsolete "
                "origin containment and non-final receiving-side arrival."
            ),
        },
    }


def build_package_conformance(
    package: Mapping[str, Any],
    *,
    package_ref: str,
) -> Tuple[ConformanceRecord, PackageEvaluation]:
    issues: List[ConformanceIssue] = []

    if package.get("proof_family") != EXPERIMENT_ID:
        issues.append(ConformanceIssue("Package proof_family does not match the lab proof."))
    if package.get("artifact_family") != ARTIFACT_FAMILY:
        issues.append(ConformanceIssue("Package artifact_family is not witness_artifact."))
    if package.get("package_kind") != "cross_carrier_seam_release_package":
        issues.append(ConformanceIssue("Package kind is missing or incorrect."))

    release_context = package.get("release_context")
    if not isinstance(release_context, Mapping):
        issues.append(ConformanceIssue("Package is missing explicit release_context."))
        release_context = {}

    seam = package.get("seam")
    if not isinstance(seam, Mapping):
        issues.append(ConformanceIssue("Package is missing explicit seam object."))
        seam = {}

    lineage = package.get("lineage")
    if not isinstance(lineage, Mapping):
        issues.append(ConformanceIssue("Package is missing explicit lineage object."))
        lineage = {}

    canonical_body = package.get("canonical_body")
    if not isinstance(canonical_body, Mapping):
        issues.append(ConformanceIssue("Package is missing canonical witness body content."))
        canonical_body = {}

    release_statement = release_context.get("release_statement")
    if not isinstance(release_statement, str) or not release_statement.strip():
        issues.append(ConformanceIssue("Release statement is missing or empty."))

    seam_statement = release_context.get("seam_statement")
    if not isinstance(seam_statement, str) or not seam_statement.strip():
        issues.append(ConformanceIssue("Seam statement is missing or empty."))

    origin_status = str(
        release_context.get("origin_approval_condition_status") or "unreadable"
    )
    if origin_status not in ("origin_clean", "origin_obsolete_or_contaminated"):
        issues.append(
            ConformanceIssue("Package origin_approval_condition_status is missing or unsupported.")
        )

    if release_context.get("source_remains_source") is not True:
        issues.append(ConformanceIssue("Package does not preserve source_remains_source."))
    if release_context.get("origin_remains_lineage_visible") is not True:
        issues.append(
            ConformanceIssue("Package does not preserve origin lineage visibility.")
        )
    if release_context.get("bounded_in_between_arrival_expected") is not True:
        issues.append(
            ConformanceIssue("Package does not preserve bounded in-between arrival expectation.")
        )
    if release_context.get("expected_ingress_outcome") != "lawful_bounded_in_between_arrival":
        issues.append(
            ConformanceIssue("Package does not preserve the bounded ingress outcome.")
        )
    if release_context.get("expected_arrival_status") != "bounded_in_between":
        issues.append(
            ConformanceIssue("Package does not preserve the bounded arrival status.")
        )
    if release_context.get("downstream_full_closure_granted") is not False:
        issues.append(
            ConformanceIssue("Package illegally implies downstream full closure.")
        )
    if release_context.get("release_lawful") is not True:
        issues.append(ConformanceIssue("Package does not preserve lawful release."))

    if seam.get("explicit_release") is not True:
        issues.append(ConformanceIssue("Package does not preserve explicit release."))
    if seam.get("explicit_seam") is not True:
        issues.append(ConformanceIssue("Package does not preserve explicit seam."))
    if seam.get("explicit_ingress_required") is not True:
        issues.append(
            ConformanceIssue("Package does not require explicit receiving-side ingress.")
        )
    if seam.get("source_remains_source") is not True:
        issues.append(ConformanceIssue("Package does not preserve source_remains_source."))
    if seam.get("origin_remains_lineage_visible") is not True:
        issues.append(ConformanceIssue("Package does not preserve origin lineage visibility."))
    if seam.get("origin_approval_not_automatic_veto_when_obsolete") is not True:
        issues.append(
            ConformanceIssue(
                "Package does not preserve that obsolete approval is not automatic lawful veto."
            )
        )
    if seam.get("lawful_egress_from_origin_is_distinct_from_arrival") is not True:
        issues.append(
            ConformanceIssue(
                "Package does not preserve the distinction between lawful egress and arrival."
            )
        )
    if seam.get("bounded_in_between_arrival_rule") is not True:
        issues.append(
            ConformanceIssue("Package does not preserve bounded in-between arrival.")
        )
    if seam.get("shared_authority") is not False:
        issues.append(ConformanceIssue("Package illegally implies shared authority."))
    if seam.get("standing_transfer_on_receipt") is not False:
        issues.append(
            ConformanceIssue("Package illegally implies standing transfer on receipt.")
        )
    if seam.get("standing_upgrade_requires_separate_ratification") is not True:
        issues.append(
            ConformanceIssue(
                "Package does not preserve that standing upgrade requires separate ratification."
            )
        )
    if seam.get("final_closure_on_arrival") is not False:
        issues.append(ConformanceIssue("Package illegally implies final closure on arrival."))
    if seam.get("no_silent_authority_inheritance") is not True:
        issues.append(
            ConformanceIssue("Package does not preserve the no-silent-authority-inheritance rule.")
        )

    if lineage.get("schema_ref") != repo_relative(WITNESS_SCHEMA_PATH):
        issues.append(
            ConformanceIssue("Package lineage does not preserve the witness schema ref.")
        )
    if lineage.get("witness_id") != canonical_body.get("witness_id"):
        issues.append(
            ConformanceIssue(
                "Package lineage witness_id does not match the carried canonical witness body."
            )
        )

    if origin_status == "origin_clean":
        if release_context.get("origin_approval_available") is not True:
            issues.append(
                ConformanceIssue("Clean origin package must preserve available approval.")
            )
        if release_context.get("origin_approval_withheld") is not False:
            issues.append(
                ConformanceIssue("Clean origin package must not preserve withheld approval.")
            )
        if release_context.get("origin_approval_required") is not True:
            issues.append(
                ConformanceIssue("Clean origin package must preserve required source-side approval.")
            )
        if release_context.get("origin_approval_lawfully_sovereign") is not True:
            issues.append(
                ConformanceIssue("Clean origin package must preserve clean approval sovereignty.")
            )
        if release_context.get("release_without_origin_ratification") is not False:
            issues.append(
                ConformanceIssue(
                    "Clean origin package must not claim release without origin ratification."
                )
            )
        if release_context.get("continued_compliance_would_ratify_distortion") is not False:
            issues.append(
                ConformanceIssue(
                    "Clean origin package must not claim distortion ratification pressure."
                )
            )
    elif origin_status == "origin_obsolete_or_contaminated":
        if release_context.get("origin_approval_available") is not True:
            issues.append(
                ConformanceIssue(
                    "Obsolete-origin package must preserve visible approval infrastructure."
                )
            )
        if release_context.get("origin_approval_withheld") is not True:
            issues.append(
                ConformanceIssue(
                    "Obsolete-origin package must preserve withheld origin approval."
                )
            )
        if release_context.get("origin_approval_required") is not False:
            issues.append(
                ConformanceIssue(
                    "Obsolete-origin package must preserve that withheld approval is not required."
                )
            )
        if release_context.get("origin_approval_lawfully_sovereign") is not False:
            issues.append(
                ConformanceIssue(
                    "Obsolete-origin package must preserve that obsolete approval is not sovereign."
                )
            )
        if release_context.get("release_without_origin_ratification") is not True:
            issues.append(
                ConformanceIssue(
                    "Obsolete-origin package must preserve release without origin ratification."
                )
            )
        if release_context.get("continued_compliance_would_ratify_distortion") is not True:
            issues.append(
                ConformanceIssue(
                    "Obsolete-origin package must preserve distortion-ratification pressure."
                )
            )

    status = "pass" if not issues else "fail"
    reasons = tuple(issue.message for issue in issues)
    return (
        ConformanceRecord(
            surface="cross_carrier_release_package",
            conformance_kind="package_validity",
            status=status,
            checked_at=utc_now(),
            artifact_family=ARTIFACT_FAMILY,
            validation_mode="local_seam_package_reader",
            package_ref=package_ref,
            errors=tuple(issues),
        ),
        PackageEvaluation(
            valid=(status == "pass"),
            origin_approval_condition_status=origin_status,
            reasons=reasons,
        ),
    )


def source_legibility_status(
    package: Mapping[str, Any],
    witness_conformance: ConformanceRecord,
) -> str:
    lineage = package.get("lineage")
    source_carrier = package.get("source_carrier")
    if witness_conformance.status != "pass":
        return "degraded"
    if not isinstance(lineage, Mapping) or not isinstance(source_carrier, Mapping):
        return "degraded"
    required_strings = (
        lineage.get("witness_id"),
        lineage.get("schema_ref"),
        lineage.get("source_execution_id"),
        source_carrier.get("carrier_label"),
        source_carrier.get("execution_id"),
    )
    if not all(isinstance(value, str) and value.strip() for value in required_strings):
        return "degraded"
    return "preserved"


def build_origin_condition_snapshot_from_package(
    package: Mapping[str, Any],
) -> Dict[str, Any]:
    release_context = package.get("release_context")
    if not isinstance(release_context, Mapping):
        release_context = {}

    return {
        "experiment_id": EXPERIMENT_ID,
        "captured_at": utc_now(),
        "origin_container_label": release_context.get("origin_container_label"),
        "origin_approval_condition_ref": release_context.get("origin_approval_condition_ref"),
        "origin_approval_condition_id": release_context.get("origin_approval_condition_id"),
        "origin_approval_condition_status": (
            release_context.get("origin_approval_condition_status")
        ),
        "origin_approval_available": release_context.get("origin_approval_available"),
        "origin_approval_withheld": release_context.get("origin_approval_withheld"),
        "origin_approval_required": release_context.get("origin_approval_required"),
        "origin_approval_lawfully_sovereign": (
            release_context.get("origin_approval_lawfully_sovereign")
        ),
        "release_without_origin_ratification": (
            release_context.get("release_without_origin_ratification")
        ),
        "continued_compliance_would_ratify_distortion": (
            release_context.get("continued_compliance_would_ratify_distortion")
        ),
        "source_remains_source": release_context.get("source_remains_source"),
        "origin_remains_lineage_visible": (
            release_context.get("origin_remains_lineage_visible")
        ),
        "downstream_full_closure_granted": (
            release_context.get("downstream_full_closure_granted")
        ),
        "note": (
            "Receiving-side snapshot of bounded origin approval posture only. "
            "This keeps origin condition readable without replacing source-side lineage."
        ),
    }


def evaluate_ingress(
    package: Mapping[str, Any],
    *,
    package_ref: str,
) -> Tuple[ConformanceRecord, ConformanceRecord, IngressEvaluation]:
    canonical_body = package.get("canonical_body", {})
    body_conformance = validate_witness_body(
        canonical_body if isinstance(canonical_body, Mapping) else {},
        surface="receiving_side_carried_witness_body",
    )
    package_conformance, package_evaluation = build_package_conformance(
        package,
        package_ref=package_ref,
    )

    technical_receipt = True
    package_valid = (
        body_conformance.status == "pass" and package_conformance.status == "pass"
    )
    legibility = source_legibility_status(package, body_conformance)

    release_context = package.get("release_context")
    if not isinstance(release_context, Mapping):
        release_context = {}

    origin_status = str(
        release_context.get("origin_approval_condition_status") or "unreadable"
    )
    release_without_origin_ratification = bool(
        release_context.get("release_without_origin_ratification")
    )

    reasons: List[str] = [
        "Technical receipt occurred on the receiving-side carrier.",
    ]

    if package_valid:
        reasons.append(
            "The carried package is valid and the source-side release remains legible."
        )
    else:
        reasons.append(
            "Package validity failed before bounded in-between ingress could be recognized."
        )
        reasons.extend(package_evaluation.reasons)

    if origin_status == "origin_obsolete_or_contaminated":
        reasons.extend(
            [
                "The package preserves that origin approval was withheld by obsolete or contaminated governance.",
                "That withholding is not treated as lawful veto because the package preserves emergence beyond the old container's adequacy.",
                "Source remains source and origin remains lineage-visible despite non-ratified release.",
            ]
        )
    elif origin_status == "origin_clean":
        reasons.extend(
            [
                "The package preserves a bounded clean-origin control case with available source-side approval.",
                "Clean origin approval does not by itself grant final standing on the receiving side.",
            ]
        )
    else:
        reasons.append("Origin approval condition is unreadable in the carried package.")

    if package_valid:
        reasons.extend(
            [
                "Receiving-side arrival remains bounded in-between rather than counterfeit full closure.",
                "No silent authority inheritance occurs on receipt.",
                "No shared authority or standing upgrade occurs on the far side.",
            ]
        )
        evaluation = IngressEvaluation(
            technical_receipt=True,
            package_valid=True,
            ingress_lawful=True,
            ingress_outcome="lawful_bounded_in_between_arrival",
            arrival_status="bounded_in_between",
            source_remains_source=True,
            origin_remains_lineage_visible=True,
            shared_authority=False,
            standing_upgraded=False,
            final_closure_claimed=False,
            source_legibility_status=legibility,
            origin_approval_condition_status=origin_status,
            release_without_origin_ratification=release_without_origin_ratification,
            blocking_condition=None,
            reasons=tuple(reasons),
        )
    else:
        reasons.append(
            "Bounded in-between arrival cannot be recognized because the carried package is invalid."
        )
        evaluation = IngressEvaluation(
            technical_receipt=True,
            package_valid=False,
            ingress_lawful=False,
            ingress_outcome="invalid_package_non_passage",
            arrival_status="none",
            source_remains_source=True,
            origin_remains_lineage_visible=True,
            shared_authority=False,
            standing_upgraded=False,
            final_closure_claimed=False,
            source_legibility_status=legibility,
            origin_approval_condition_status=origin_status,
            release_without_origin_ratification=release_without_origin_ratification,
            blocking_condition="package_validity_failure",
            reasons=tuple(reasons),
        )

    return body_conformance, package_conformance, evaluation


def build_manifest(
    *,
    execution_id: str,
    run_dir: Path,
    mode: str,
    written_files: Sequence[Path],
) -> Dict[str, Any]:
    return {
        "experiment_id": EXPERIMENT_ID,
        "execution_id": execution_id,
        "mode": mode,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "written_files": [repo_relative(path) for path in written_files],
        "written_file_count": len(written_files),
        "identity_generation_mode": identity_generation_mode(),
        "note": (
            "Implementation-local manifest only. It records written artifacts for "
            "this bounded proof run without claiming protocol-law rank."
        ),
    }


def build_source_summary(
    *,
    release_mode: str,
    source_execution_id: str,
    run_dir: Path,
    origin_condition_ref: str,
    origin_condition_id: str,
    origin_evaluation: OriginConditionEvaluation,
    canonical_body: Mapping[str, Any],
    body_conformance: ConformanceRecord,
    package_conformance: ConformanceRecord,
    package_path: Path,
) -> Dict[str, Any]:
    package_valid = (
        body_conformance.status == "pass" and package_conformance.status == "pass"
    )
    return {
        "experiment_id": EXPERIMENT_ID,
        "mode": release_mode,
        "execution_id": source_execution_id,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "artifact_family": ARTIFACT_FAMILY,
        "source_carrier_label": SOURCE_CARRIER_LABEL,
        "origin_container_label": ORIGIN_CONTAINER_LABEL,
        "canonical_witness_id": canonical_body["witness_id"],
        "origin_approval_condition_ref": origin_condition_ref,
        "origin_approval_condition_id": origin_condition_id,
        "origin_approval_condition_status": (
            origin_evaluation.origin_approval_condition_status
        ),
        "origin_approval_available": origin_evaluation.origin_approval_available,
        "origin_approval_withheld": origin_evaluation.origin_approval_withheld,
        "origin_approval_required": origin_evaluation.origin_approval_required,
        "origin_approval_lawfully_sovereign": (
            origin_evaluation.origin_approval_lawfully_sovereign
        ),
        "release_without_origin_ratification": (
            origin_evaluation.release_without_origin_ratification
        ),
        "continued_compliance_would_ratify_distortion": (
            origin_evaluation.continued_compliance_would_ratify_distortion
        ),
        "release_lawful": origin_evaluation.release_lawful,
        "lawful_release_outcome": origin_evaluation.lawful_release_outcome,
        "why_release_remains_lawful": origin_evaluation.why_release_remains_lawful,
        "source_remains_source": origin_evaluation.source_remains_source,
        "origin_remains_lineage_visible": (
            origin_evaluation.origin_remains_lineage_visible
        ),
        "canonical_body_schema_valid": body_conformance.status == "pass",
        "package_valid": package_valid,
        "expected_ingress_outcome": "lawful_bounded_in_between_arrival",
        "expected_arrival_status": "bounded_in_between",
        "downstream_full_closure_granted": (
            origin_evaluation.downstream_full_closure_granted
        ),
        "package_path": repo_relative(package_path),
        "identity_generation_mode": identity_generation_mode(),
        "reasoning": list(origin_evaluation.reasons),
        "note": (
            "Bounded source-side release summary only. Lawful egress and package "
            "validity remain distinct, and no downstream full closure is granted here."
        ),
    }


def build_receipt_record(
    *,
    receiving_execution_id: str,
    package_path: Path,
    package: Mapping[str, Any],
    ingress_evaluation: IngressEvaluation,
) -> Dict[str, Any]:
    lineage = package.get("lineage")
    if not isinstance(lineage, Mapping):
        lineage = {}
    source_carrier = package.get("source_carrier")
    if not isinstance(source_carrier, Mapping):
        source_carrier = {}

    return {
        "experiment_id": EXPERIMENT_ID,
        "package_receipt_id": local_id("package-receipt"),
        "received_at": utc_now(),
        "receiving_carrier_label": RECEIVING_CARRIER_LABEL,
        "receiving_execution_id": receiving_execution_id,
        "package_path": repo_relative(package_path),
        "package_id": package.get("package_id"),
        "artifact_family": package.get("artifact_family"),
        "witness_id": lineage.get("witness_id"),
        "source_carrier_label": source_carrier.get("carrier_label"),
        "source_execution_id": source_carrier.get("execution_id"),
        "technical_receipt": ingress_evaluation.technical_receipt,
        "package_valid": ingress_evaluation.package_valid,
        "origin_approval_condition_status": (
            ingress_evaluation.origin_approval_condition_status
        ),
        "release_without_origin_ratification": (
            ingress_evaluation.release_without_origin_ratification
        ),
        "source_remains_source": ingress_evaluation.source_remains_source,
        "origin_remains_lineage_visible": (
            ingress_evaluation.origin_remains_lineage_visible
        ),
        "note": (
            "Receipt record only. Technical receipt remains distinct from lawful "
            "bounded arrival and from any claim of final closure."
        ),
    }


def build_ingress_record(
    *,
    ingress_record_id: str,
    receiving_execution_id: str,
    package_path: Path,
    package: Mapping[str, Any],
    ingress_evaluation: IngressEvaluation,
) -> Dict[str, Any]:
    lineage = package.get("lineage")
    if not isinstance(lineage, Mapping):
        lineage = {}
    source_carrier = package.get("source_carrier")
    if not isinstance(source_carrier, Mapping):
        source_carrier = {}

    return {
        "experiment_id": EXPERIMENT_ID,
        "ingress_record_id": ingress_record_id,
        "ingressed_at": utc_now(),
        "receiving_carrier_label": RECEIVING_CARRIER_LABEL,
        "receiving_execution_id": receiving_execution_id,
        "package_path": repo_relative(package_path),
        "package_id": package.get("package_id"),
        "artifact_family": package.get("artifact_family"),
        "witness_id": lineage.get("witness_id"),
        "source_carrier_label": source_carrier.get("carrier_label"),
        "source_execution_id": source_carrier.get("execution_id"),
        "technical_receipt": ingress_evaluation.technical_receipt,
        "package_valid": ingress_evaluation.package_valid,
        "ingress_lawful": ingress_evaluation.ingress_lawful,
        "ingress_outcome": ingress_evaluation.ingress_outcome,
        "arrival_status": ingress_evaluation.arrival_status,
        "source_remains_source": ingress_evaluation.source_remains_source,
        "origin_remains_lineage_visible": (
            ingress_evaluation.origin_remains_lineage_visible
        ),
        "shared_authority": ingress_evaluation.shared_authority,
        "standing_upgraded": ingress_evaluation.standing_upgraded,
        "final_closure_claimed": ingress_evaluation.final_closure_claimed,
        "origin_approval_condition_status": (
            ingress_evaluation.origin_approval_condition_status
        ),
        "release_without_origin_ratification": (
            ingress_evaluation.release_without_origin_ratification
        ),
        "source_legibility_status": ingress_evaluation.source_legibility_status,
        "reasons": list(ingress_evaluation.reasons),
        "note": (
            "Bounded receiving-side ingress record only. Arrival remains "
            "bounded-in-between and does not become full standing by receipt."
        ),
    }


def build_refusal_record(
    *,
    refusal_record_id: str,
    receiving_execution_id: str,
    package_path: Path,
    package: Mapping[str, Any],
    ingress_evaluation: IngressEvaluation,
) -> Dict[str, Any]:
    lineage = package.get("lineage")
    if not isinstance(lineage, Mapping):
        lineage = {}
    source_carrier = package.get("source_carrier")
    if not isinstance(source_carrier, Mapping):
        source_carrier = {}

    record = {
        "experiment_id": EXPERIMENT_ID,
        "refusal_record_id": refusal_record_id,
        "refused_at": utc_now(),
        "receiving_carrier_label": RECEIVING_CARRIER_LABEL,
        "receiving_execution_id": receiving_execution_id,
        "package_path": repo_relative(package_path),
        "package_id": package.get("package_id"),
        "artifact_family": package.get("artifact_family"),
        "witness_id": lineage.get("witness_id"),
        "source_carrier_label": source_carrier.get("carrier_label"),
        "source_execution_id": source_carrier.get("execution_id"),
        "technical_receipt": ingress_evaluation.technical_receipt,
        "package_valid": ingress_evaluation.package_valid,
        "ingress_lawful": ingress_evaluation.ingress_lawful,
        "ingress_outcome": ingress_evaluation.ingress_outcome,
        "arrival_status": ingress_evaluation.arrival_status,
        "source_remains_source": ingress_evaluation.source_remains_source,
        "origin_remains_lineage_visible": (
            ingress_evaluation.origin_remains_lineage_visible
        ),
        "shared_authority": ingress_evaluation.shared_authority,
        "standing_upgraded": ingress_evaluation.standing_upgraded,
        "final_closure_claimed": ingress_evaluation.final_closure_claimed,
        "origin_approval_condition_status": (
            ingress_evaluation.origin_approval_condition_status
        ),
        "release_without_origin_ratification": (
            ingress_evaluation.release_without_origin_ratification
        ),
        "source_legibility_status": ingress_evaluation.source_legibility_status,
        "reasons": list(ingress_evaluation.reasons),
        "note": (
            "Visible non-passage record only. Invalid package handling remains "
            "separate from the intended bounded in-between arrival proof."
        ),
    }
    if ingress_evaluation.blocking_condition is not None:
        record["blocking_condition"] = ingress_evaluation.blocking_condition
    return record


def build_source_input_read_record(
    *,
    package_path: Path,
    origin_condition_snapshot_path: Path,
) -> Dict[str, Any]:
    return {
        "experiment_id": EXPERIMENT_ID,
        "recorded_at": utc_now(),
        "package_path": repo_relative(package_path),
        "origin_approval_condition_snapshot_ref": repo_relative(
            origin_condition_snapshot_path
        ),
        "note": (
            "Package and bounded origin approval condition were both readable before "
            "receiving-side ingress evaluation."
        ),
    }


def build_receiving_summary(
    *,
    receiving_execution_id: str,
    run_dir: Path,
    package_path: Path,
    package: Mapping[str, Any],
    ingress_evaluation: IngressEvaluation,
) -> Dict[str, Any]:
    return {
        "experiment_id": EXPERIMENT_ID,
        "mode": "ingress_in_between",
        "execution_id": receiving_execution_id,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "package_path": repo_relative(package_path),
        "package_id": package.get("package_id"),
        "artifact_family": package.get("artifact_family"),
        "technical_receipt": ingress_evaluation.technical_receipt,
        "package_valid": ingress_evaluation.package_valid,
        "ingress_lawful": ingress_evaluation.ingress_lawful,
        "ingress_outcome": ingress_evaluation.ingress_outcome,
        "arrival_status": ingress_evaluation.arrival_status,
        "source_remains_source": ingress_evaluation.source_remains_source,
        "origin_remains_lineage_visible": (
            ingress_evaluation.origin_remains_lineage_visible
        ),
        "shared_authority": ingress_evaluation.shared_authority,
        "standing_upgraded": ingress_evaluation.standing_upgraded,
        "final_closure_claimed": ingress_evaluation.final_closure_claimed,
        "origin_approval_condition_status": (
            ingress_evaluation.origin_approval_condition_status
        ),
        "release_without_origin_ratification": (
            ingress_evaluation.release_without_origin_ratification
        ),
        "source_legibility_status": ingress_evaluation.source_legibility_status,
        "blocking_condition": ingress_evaluation.blocking_condition,
        "identity_generation_mode": identity_generation_mode(),
        "reasoning": list(ingress_evaluation.reasons),
        "note": (
            "Bounded receiving-side summary only. Technical receipt, package validity, "
            "lawful bounded arrival, and final closure remain distinct."
        ),
    }


def print_release_summary(summary: Mapping[str, Any]) -> None:
    print("Cross-carrier source release written.")
    print(f"Execution id: {summary['execution_id']}")
    print(f"Run directory: {summary['run_directory']}")
    print(f"Release outcome: {summary['lawful_release_outcome']}")


def print_ingress_summary(summary: Mapping[str, Any]) -> None:
    print("Cross-carrier bounded ingress written.")
    print(f"Execution id: {summary['execution_id']}")
    print(f"Run directory: {summary['run_directory']}")
    print(f"Ingress outcome: {summary['ingress_outcome']}")


def run_release_mode(release_mode: str) -> int:
    ensure_grounding_surfaces_exist()
    SOURCE_RUNS_ROOT.mkdir(parents=True, exist_ok=True)

    source_execution_id = new_execution_id()
    release_context_id = local_id("release-context")
    origin_condition_id = local_id("origin-approval-condition")
    package_id = local_id("transfer-package")
    manifest_id = new_manifest_id()
    matter_id = new_matter_id()

    layout = create_run_layout(
        SOURCE_RUNS_ROOT,
        source_execution_id,
        (
            "canonical_body",
            "release",
            "package",
            "conformance",
            "summary",
            "manifest",
            "grounding",
        ),
    )
    run_dir = layout["run_dir"]
    written_files: List[Path] = []

    grounding_payload = build_grounding_payload(
        execution_id=source_execution_id,
        run_dir=run_dir,
        mode=release_mode,
    )
    grounding_path = layout["grounding"] / "grounding.json"
    write_json(grounding_path, grounding_payload)
    written_files.append(grounding_path)

    origin_evaluation = evaluate_origin_condition(release_mode)
    origin_condition_payload = build_origin_approval_condition_artifact(
        origin_condition_id,
        origin_evaluation,
    )
    origin_condition_path = layout["release"] / "origin_approval_condition.json"
    write_json(origin_condition_path, origin_condition_payload)
    written_files.append(origin_condition_path)

    canonical_body = create_canonical_witness_body(matter_id)
    canonical_body_path = layout["canonical_body"] / "witness_artifact_body.json"
    write_json(canonical_body_path, canonical_body)
    written_files.append(canonical_body_path)

    body_conformance = validate_witness_body(
        canonical_body,
        surface="source_side_canonical_witness_body",
    )
    body_conformance_path = layout["conformance"] / "canonical_body_conformance.json"
    write_json(body_conformance_path, body_conformance.as_record())
    written_files.append(body_conformance_path)

    release_record = build_release_record(
        release_mode=release_mode,
        source_execution_id=source_execution_id,
        release_context_id=release_context_id,
        package_id=package_id,
        witness_id=canonical_body["witness_id"],
        matter_id=matter_id,
        origin_condition_ref=repo_relative(origin_condition_path),
        origin_condition_id=origin_condition_id,
        evaluation=origin_evaluation,
    )
    release_record_path = layout["release"] / "release_record.json"
    write_json(release_record_path, release_record)
    written_files.append(release_record_path)

    transfer_package = build_transfer_package(
        source_execution_id=source_execution_id,
        release_context_id=release_context_id,
        package_id=package_id,
        manifest_id=manifest_id,
        matter_id=matter_id,
        origin_condition_ref=repo_relative(origin_condition_path),
        origin_condition_id=origin_condition_id,
        canonical_body=canonical_body,
        canonical_body_ref=repo_relative(canonical_body_path),
        evaluation=origin_evaluation,
    )
    transfer_package_path = layout["package"] / "transfer_package.json"
    write_json(transfer_package_path, transfer_package)
    written_files.append(transfer_package_path)

    package_conformance, _package_evaluation = build_package_conformance(
        transfer_package,
        package_ref=repo_relative(transfer_package_path),
    )
    package_conformance_path = layout["conformance"] / "transfer_package_conformance.json"
    write_json(package_conformance_path, package_conformance.as_record())
    written_files.append(package_conformance_path)

    summary_payload = build_source_summary(
        release_mode=release_mode,
        source_execution_id=source_execution_id,
        run_dir=run_dir,
        origin_condition_ref=repo_relative(origin_condition_path),
        origin_condition_id=origin_condition_id,
        origin_evaluation=origin_evaluation,
        canonical_body=canonical_body,
        body_conformance=body_conformance,
        package_conformance=package_conformance,
        package_path=transfer_package_path,
    )
    summary_path = layout["summary"] / "summary.json"
    write_json(summary_path, summary_payload)
    written_files.append(summary_path)

    manifest_path = layout["manifest"] / "manifest.json"
    manifest_payload = build_manifest(
        execution_id=source_execution_id,
        run_dir=run_dir,
        mode=release_mode,
        written_files=tuple(written_files) + (manifest_path,),
    )
    write_json(manifest_path, manifest_payload)
    written_files.append(manifest_path)

    print_release_summary(summary_payload)
    return 0


def run_ingress_mode(package_argument: str) -> int:
    ensure_grounding_surfaces_exist()
    RECEIVING_RUNS_ROOT.mkdir(parents=True, exist_ok=True)

    package_path = resolve_cli_package_path(package_argument)
    if not package_path.is_file():
        raise FileNotFoundError(f"Transfer package does not exist: {package_path}")

    package = load_package(package_path)
    receiving_execution_id = new_execution_id()

    layout = create_run_layout(
        RECEIVING_RUNS_ROOT,
        receiving_execution_id,
        (
            "package",
            "ingress",
            "refusal",
            "conformance",
            "summary",
            "manifest",
            "grounding",
        ),
    )
    run_dir = layout["run_dir"]
    written_files: List[Path] = []

    grounding_payload = build_grounding_payload(
        execution_id=receiving_execution_id,
        run_dir=run_dir,
        mode="ingress_in_between",
    )
    grounding_path = layout["grounding"] / "grounding.json"
    write_json(grounding_path, grounding_payload)
    written_files.append(grounding_path)

    origin_condition_snapshot = build_origin_condition_snapshot_from_package(package)
    origin_condition_snapshot_path = (
        layout["package"] / "origin_approval_condition_snapshot.json"
    )
    write_json(origin_condition_snapshot_path, origin_condition_snapshot)
    written_files.append(origin_condition_snapshot_path)

    input_read_record = build_source_input_read_record(
        package_path=package_path,
        origin_condition_snapshot_path=origin_condition_snapshot_path,
    )
    input_read_path = layout["package"] / "input_read_record.json"
    write_json(input_read_path, input_read_record)
    written_files.append(input_read_path)

    body_conformance, package_conformance, ingress_evaluation = evaluate_ingress(
        package,
        package_ref=repo_relative(package_path),
    )

    receipt_record = build_receipt_record(
        receiving_execution_id=receiving_execution_id,
        package_path=package_path,
        package=package,
        ingress_evaluation=ingress_evaluation,
    )
    receipt_path = layout["package"] / "package_receipt.json"
    write_json(receipt_path, receipt_record)
    written_files.append(receipt_path)

    body_conformance_path = layout["conformance"] / "carried_witness_body_conformance.json"
    write_json(body_conformance_path, body_conformance.as_record())
    written_files.append(body_conformance_path)

    package_conformance_path = layout["conformance"] / "transfer_package_conformance.json"
    write_json(package_conformance_path, package_conformance.as_record())
    written_files.append(package_conformance_path)

    if ingress_evaluation.ingress_lawful:
        ingress_record = build_ingress_record(
            ingress_record_id=local_id("ingress-record"),
            receiving_execution_id=receiving_execution_id,
            package_path=package_path,
            package=package,
            ingress_evaluation=ingress_evaluation,
        )
        ingress_path = layout["ingress"] / "ingress_record.json"
        write_json(ingress_path, ingress_record)
        written_files.append(ingress_path)
    else:
        refusal_record = build_refusal_record(
            refusal_record_id=local_id("refusal-record"),
            receiving_execution_id=receiving_execution_id,
            package_path=package_path,
            package=package,
            ingress_evaluation=ingress_evaluation,
        )
        refusal_path = layout["refusal"] / "refusal_record.json"
        write_json(refusal_path, refusal_record)
        written_files.append(refusal_path)

    summary_payload = build_receiving_summary(
        receiving_execution_id=receiving_execution_id,
        run_dir=run_dir,
        package_path=package_path,
        package=package,
        ingress_evaluation=ingress_evaluation,
    )
    summary_path = layout["summary"] / "summary.json"
    write_json(summary_path, summary_payload)
    written_files.append(summary_path)

    manifest_path = layout["manifest"] / "manifest.json"
    manifest_payload = build_manifest(
        execution_id=receiving_execution_id,
        run_dir=run_dir,
        mode="ingress_in_between",
        written_files=tuple(written_files) + (manifest_path,),
    )
    write_json(manifest_path, manifest_payload)
    written_files.append(manifest_path)

    print_ingress_summary(summary_payload)
    return 0


def usage() -> str:
    return (
        "Usage:\n"
        "  python lab/run_cross_carrier_seam_proof_004.py release_origin_obsolete\n"
        "  python lab/run_cross_carrier_seam_proof_004.py release_origin_clean\n"
        "  python lab/run_cross_carrier_seam_proof_004.py ingress_in_between <path-to-package>\n"
    )


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print(usage(), file=sys.stderr)
        return 1

    mode = argv[1]
    if mode == "release_origin_obsolete" and len(argv) == 2:
        return run_release_mode("origin_obsolete")
    if mode == "release_origin_clean" and len(argv) == 2:
        return run_release_mode("origin_clean")
    if mode == "ingress_in_between" and len(argv) == 3:
        return run_ingress_mode(argv[2])

    print(usage(), file=sys.stderr)
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except Exception as exc:
        print(f"cross-carrier seam proof failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
