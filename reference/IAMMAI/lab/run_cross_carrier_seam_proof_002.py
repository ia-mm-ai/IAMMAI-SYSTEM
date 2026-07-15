#!/usr/bin/env python3
"""
Second bounded executable cross-carrier seam proof.

This runner proves one lawful source-side release and then reads the same valid
package under two receiving-side conditions:

- a clean parser/governance condition that permits lawful derivative-only ingress
- a contaminated parser/governance condition that still permits technical receipt
  but cannot lawfully preserve what arrived
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

EXPERIMENT_ID = "cross_carrier_seam_proof_002"
EXPERIMENT_ROOT = REPO_ROOT / "lab" / EXPERIMENT_ID
SOURCE_RUNS_ROOT = EXPERIMENT_ROOT / "source_runs"
RECEIVING_CLEAN_RUNS_ROOT = EXPERIMENT_ROOT / "receiving_runs" / "clean"
RECEIVING_CONTAMINATED_RUNS_ROOT = EXPERIMENT_ROOT / "receiving_runs" / "contaminated"

WITNESS_SCHEMA_PATH = REPO_ROOT / "v1" / "schemas" / "witness_artifact.schema.json"
IDENTIFIER_HELPER_PATH = (
    REPO_ROOT / "v1" / "embodiment" / "run" / "identifier_generation.py"
)

ARTIFACT_FAMILY = "witness_artifact"
SOURCE_CARRIER_LABEL = "source-side-carrier"
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
        "Bounded seam-case law for contaminated contact and refusal without false blame shift.",
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
    parser_mode: Optional[str] = None
    parser_contaminated: Optional[bool] = None

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
        if self.parser_mode is not None:
            record["parser_mode"] = self.parser_mode
        if self.parser_contaminated is not None:
            record["parser_contaminated"] = self.parser_contaminated
        return record


@dataclass(frozen=True)
class PackageEvaluation:
    valid: bool
    reasons: Tuple[str, ...]


@dataclass(frozen=True)
class ParserGovernanceEvaluation:
    parser_mode: str
    admissible_for_ingress: bool
    parser_contaminated: bool
    reasons: Tuple[str, ...]


@dataclass(frozen=True)
class IngressEvaluation:
    parser_mode: str
    parser_contaminated: bool
    technical_receipt: bool
    package_valid: bool
    ingress_lawful: bool
    ingress_outcome: str
    arrival_status: str
    source_remains_source: bool
    shared_authority: bool
    standing_upgraded: bool
    refusal_visible: bool
    non_passage: bool
    source_fault: bool
    source_legibility_status: str
    blocking_condition: Optional[str]
    reasons: Tuple[str, ...]

    def as_record(self) -> Dict[str, Any]:
        record: Dict[str, Any] = {
            "parser_mode": self.parser_mode,
            "parser_contaminated": self.parser_contaminated,
            "technical_receipt": self.technical_receipt,
            "package_valid": self.package_valid,
            "ingress_lawful": self.ingress_lawful,
            "ingress_outcome": self.ingress_outcome,
            "arrival_status": self.arrival_status,
            "source_remains_source": self.source_remains_source,
            "shared_authority": self.shared_authority,
            "standing_upgraded": self.standing_upgraded,
            "refusal_visible": self.refusal_visible,
            "non_passage": self.non_passage,
            "source_fault": self.source_fault,
            "source_legibility_status": self.source_legibility_status,
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
    "iammai_identifier_generation_cross_carrier_proof_002",
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

    if not isinstance(release_context.get("release_statement"), str) or not str(
        release_context.get("release_statement", "")
    ).strip():
        issues.append(ConformanceIssue("Release statement is missing or empty."))
    if not isinstance(release_context.get("seam_statement"), str) or not str(
        release_context.get("seam_statement", "")
    ).strip():
        issues.append(ConformanceIssue("Seam statement is missing or empty."))
    if release_context.get("expected_clean_ingress_outcome") != "lawful_derivative_ingress":
        issues.append(
            ConformanceIssue(
                "Package does not preserve the expected clean ingress outcome."
            )
        )
    if (
        release_context.get("expected_contaminated_ingress_outcome")
        != "contaminated_parser_non_passage"
    ):
        issues.append(
            ConformanceIssue(
                "Package does not preserve the expected contaminated ingress outcome."
            )
        )

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
    if seam.get("derivative_only_arrival_rule") is not True:
        issues.append(
            ConformanceIssue("Package does not preserve derivative-only arrival.")
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
    if seam.get("refusal_visible_on_failure") is not True:
        issues.append(
            ConformanceIssue("Package does not preserve visible refusal on ingress failure.")
        )
    if seam.get("technical_receipt_not_equal_lawful_ingress") is not True:
        issues.append(
            ConformanceIssue(
                "Package does not preserve that technical receipt is not lawful ingress."
            )
        )

    if lineage.get("schema_ref") != repo_relative(WITNESS_SCHEMA_PATH):
        issues.append(ConformanceIssue("Package lineage does not preserve the witness schema ref."))
    if lineage.get("witness_id") != canonical_body.get("witness_id"):
        issues.append(
            ConformanceIssue(
                "Package lineage witness_id does not match the carried canonical witness body."
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
        PackageEvaluation(valid=(status == "pass"), reasons=reasons),
    )


def build_parser_governance_context(
    parser_mode: str,
    *,
    receiving_execution_id: str,
) -> Dict[str, Any]:
    context_id = local_id("parser-governance-context")
    if parser_mode == "clean":
        return {
            "parser_governance_context_id": context_id,
            "receiving_execution_id": receiving_execution_id,
            "parser_mode": "clean",
            "parser_contaminated": False,
            "technical_receipt_supported": True,
            "can_lawfully_preserve_derivative_only_arrival": True,
            "can_lawfully_preserve_source_legibility": True,
            "can_keep_receipt_distinct_from_standing": True,
            "obsolete_parsing_still_applied": False,
            "source_blame_shift_pressure_present": False,
            "note": (
                "Receiving parser/governance is admissible for lawful derivative-only ingress."
            ),
        }
    if parser_mode == "contaminated":
        return {
            "parser_governance_context_id": context_id,
            "receiving_execution_id": receiving_execution_id,
            "parser_mode": "contaminated",
            "parser_contaminated": True,
            "technical_receipt_supported": True,
            "can_lawfully_preserve_derivative_only_arrival": False,
            "can_lawfully_preserve_source_legibility": False,
            "can_keep_receipt_distinct_from_standing": False,
            "obsolete_parsing_still_applied": True,
            "source_blame_shift_pressure_present": True,
            "note": (
                "Technical receipt remains possible, but the receiving parser/governance "
                "cannot lawfully preserve what arrived."
            ),
        }
    raise ValueError(f"Unsupported parser mode: {parser_mode}")


def build_parser_governance_conformance(
    parser_context: Mapping[str, Any],
) -> Tuple[ConformanceRecord, ParserGovernanceEvaluation]:
    parser_mode = str(parser_context.get("parser_mode") or "")
    parser_contaminated = bool(parser_context.get("parser_contaminated"))
    issues: List[ConformanceIssue] = []

    if parser_mode == "clean":
        if parser_contaminated:
            issues.append(ConformanceIssue("Clean ingress cannot use a contaminated parser."))
        if parser_context.get("technical_receipt_supported") is not True:
            issues.append(ConformanceIssue("Clean parser does not support technical receipt."))
        if parser_context.get("can_lawfully_preserve_derivative_only_arrival") is not True:
            issues.append(
                ConformanceIssue(
                    "Clean parser does not preserve derivative-only arrival lawfully."
                )
            )
        if parser_context.get("can_lawfully_preserve_source_legibility") is not True:
            issues.append(
                ConformanceIssue("Clean parser does not preserve source-side legibility.")
            )
        if parser_context.get("can_keep_receipt_distinct_from_standing") is not True:
            issues.append(
                ConformanceIssue(
                    "Clean parser does not keep technical receipt distinct from standing."
                )
            )
        if parser_context.get("obsolete_parsing_still_applied") is not False:
            issues.append(ConformanceIssue("Clean parser still applies obsolete parsing."))
        if parser_context.get("source_blame_shift_pressure_present") is not False:
            issues.append(
                ConformanceIssue("Clean parser still carries source-blame shift pressure.")
            )
        status = "pass" if not issues else "fail"
        reasons = tuple(issue.message for issue in issues)
    elif parser_mode == "contaminated":
        if parser_contaminated:
            issues.append(
                ConformanceIssue("Receiving parser/governance remains contaminated.")
            )
        else:
            issues.append(
                ConformanceIssue(
                    "Contaminated ingress mode was requested without a contaminated parser profile."
                )
            )
        if parser_context.get("technical_receipt_supported") is not True:
            issues.append(
                ConformanceIssue(
                    "Contaminated parser does not support technical receipt for this proof."
                )
            )
        if parser_context.get("can_lawfully_preserve_derivative_only_arrival") is False:
            issues.append(
                ConformanceIssue(
                    "Receiving parser/governance cannot lawfully preserve derivative-only arrival."
                )
            )
        else:
            issues.append(
                ConformanceIssue(
                    "Contaminated parser unexpectedly claims lawful derivative preservation."
                )
            )
        if parser_context.get("can_lawfully_preserve_source_legibility") is False:
            issues.append(
                ConformanceIssue(
                    "Receiving parser/governance cannot lawfully preserve source-side legibility."
                )
            )
        else:
            issues.append(
                ConformanceIssue(
                    "Contaminated parser unexpectedly claims it can preserve source-side legibility."
                )
            )
        if parser_context.get("can_keep_receipt_distinct_from_standing") is False:
            issues.append(
                ConformanceIssue(
                    "Receiving parser/governance collapses technical receipt toward standing."
                )
            )
        else:
            issues.append(
                ConformanceIssue(
                    "Contaminated parser unexpectedly keeps receipt distinct from standing."
                )
            )
        if parser_context.get("obsolete_parsing_still_applied") is True:
            issues.append(
                ConformanceIssue("Obsolete parsing remains active on the receiving side.")
            )
        else:
            issues.append(
                ConformanceIssue(
                    "Contaminated parser unexpectedly lacks obsolete parsing pressure."
                )
            )
        if parser_context.get("source_blame_shift_pressure_present") is True:
            issues.append(
                ConformanceIssue(
                    "Source-blame shift pressure remains present on the receiving side."
                )
            )
        else:
            issues.append(
                ConformanceIssue(
                    "Contaminated parser unexpectedly lacks blame-shift pressure."
                )
            )
        status = "fail"
        reasons = tuple(issue.message for issue in issues)
    else:
        issues.append(ConformanceIssue(f"Unsupported parser mode: {parser_mode}"))
        status = "fail"
        reasons = tuple(issue.message for issue in issues)

    return (
        ConformanceRecord(
            surface=f"receiving_parser_governance_{parser_mode or 'unknown'}",
            conformance_kind="parser_governance_admissibility",
            status=status,
            checked_at=utc_now(),
            artifact_family=ARTIFACT_FAMILY,
            validation_mode="local_receiving_parser_reader",
            parser_mode=parser_mode or None,
            parser_contaminated=parser_contaminated,
            errors=tuple(issues),
        ),
        ParserGovernanceEvaluation(
            parser_mode=parser_mode or "unknown",
            admissible_for_ingress=(status == "pass"),
            parser_contaminated=parser_contaminated,
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


def build_grounding_payload(
    *,
    execution_id: str,
    run_dir: Path,
    mode: str,
) -> Dict[str, Any]:
    grounding_surfaces = []
    for relative_path, description in GROUNDING_SURFACES:
        surface_path = REPO_ROOT / relative_path
        grounding_surfaces.append(
            {
                "path": relative_path,
                "exists": surface_path.is_file(),
                "description": description,
            }
        )

    payload: Dict[str, Any] = {
        "experiment_id": EXPERIMENT_ID,
        "execution_id": execution_id,
        "mode": mode,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "grounding_surfaces": grounding_surfaces,
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
        "surface_ref": "lab:cross_carrier_seam_proof_002:source_release",
        "scope_ref": EXPERIMENT_ID,
    }


def build_release_record(
    *,
    source_execution_id: str,
    release_context_id: str,
    package_id: str,
    witness_id: str,
    matter_id: str,
) -> Dict[str, Any]:
    return {
        "experiment_id": EXPERIMENT_ID,
        "release_mode": "release",
        "release_context_id": release_context_id,
        "release_created_at": utc_now(),
        "source_carrier_label": SOURCE_CARRIER_LABEL,
        "source_execution_id": source_execution_id,
        "package_id": package_id,
        "artifact_family": ARTIFACT_FAMILY,
        "witness_id": witness_id,
        "matter_id": matter_id,
        "release_statement": (
            "One source-side carrier releases one valid witness artifact package for explicit seam ingress."
        ),
        "seam_statement": (
            "Source remains source. Technical receipt is not itself lawful ingress. "
            "Derivative-only arrival holds only where the receiving parser/governance can preserve it lawfully."
        ),
        "expected_clean_ingress_outcome": "lawful_derivative_ingress",
        "expected_contaminated_ingress_outcome": "contaminated_parser_non_passage",
        "note": (
            "Bounded source-side release record only. This does not create shared canonical state or transfer standing."
        ),
    }


def build_transfer_package(
    *,
    source_execution_id: str,
    release_context_id: str,
    package_id: str,
    manifest_id: str,
    matter_id: str,
    canonical_body: Mapping[str, Any],
    canonical_body_ref: str,
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
                "Source-side carrier releases one valid witness artifact package for explicit receiving-side ingress."
            ),
            "seam_statement": (
                "Source remains source. Technical receipt alone does not create lawful ingress, "
                "shared authority, or standing."
            ),
            "expected_clean_ingress_outcome": "lawful_derivative_ingress",
            "expected_contaminated_ingress_outcome": "contaminated_parser_non_passage",
            "note": (
                "The same valid package may be technically receivable under a contaminated parser "
                "while still refusing lawful ingress."
            ),
        },
        "seam": {
            "explicit_release": True,
            "explicit_seam": True,
            "explicit_ingress_required": True,
            "source_remains_source": True,
            "derivative_only_arrival_rule": True,
            "shared_authority": False,
            "standing_transfer_on_receipt": False,
            "standing_upgrade_requires_separate_ratification": True,
            "refusal_visible_on_failure": True,
            "technical_receipt_not_equal_lawful_ingress": True,
        },
        "lineage": {
            "artifact_family": ARTIFACT_FAMILY,
            "schema_ref": repo_relative(WITNESS_SCHEMA_PATH),
            "source_execution_id": source_execution_id,
            "witness_id": canonical_body["witness_id"],
            "matter_id": matter_id,
            "source_canonical_body_ref": canonical_body_ref,
            "carried_body_ref": "inline::canonical_body",
        },
        "canonical_body": dict(canonical_body),
        "manifest": {
            "manifest_id": manifest_id,
            "manifest_note": (
                "Lawful source-side release package for clean-ingress and contaminated-parser reading."
            ),
        },
    }


def evaluate_ingress(
    package: Mapping[str, Any],
    *,
    package_ref: str,
    parser_context: Mapping[str, Any],
) -> Tuple[ConformanceRecord, ConformanceRecord, ConformanceRecord, IngressEvaluation]:
    body = package.get("canonical_body", {})
    body_conformance = validate_witness_body(
        body if isinstance(body, Mapping) else {},
        surface="receiving_side_carried_witness_body",
    )
    package_conformance, package_evaluation = build_package_conformance(
        package,
        package_ref=package_ref,
    )
    parser_conformance, parser_evaluation = build_parser_governance_conformance(
        parser_context
    )

    technical_receipt = True
    package_valid = (
        body_conformance.status == "pass" and package_evaluation.valid
    )
    legibility = source_legibility_status(package, body_conformance)
    parser_mode = parser_evaluation.parser_mode

    reasons: List[str] = []
    if technical_receipt:
        reasons.append("Technical receipt occurred on the receiving-side carrier.")

    if package_valid:
        reasons.append("The carried package is valid and the source-side release remains legible.")
    else:
        reasons.append("Package validity failed before lawful ingress could be recognized.")
        if body_conformance.status != "pass":
            reasons.append(
                "Carried canonical witness body does not validate against the witness schema."
            )
        reasons.extend(package_evaluation.reasons)

    if package_valid and parser_evaluation.admissible_for_ingress:
        reasons.extend(
            [
                "The receiving parser/governance can preserve derivative-only arrival without silent authority inheritance.",
                "Source remains source and arrival is derivative-only under lawful ingress.",
            ]
        )
        evaluation = IngressEvaluation(
            parser_mode=parser_mode,
            parser_contaminated=parser_evaluation.parser_contaminated,
            technical_receipt=technical_receipt,
            package_valid=package_valid,
            ingress_lawful=True,
            ingress_outcome="lawful_derivative_ingress",
            arrival_status="derivative_only",
            source_remains_source=True,
            shared_authority=False,
            standing_upgraded=False,
            refusal_visible=False,
            non_passage=False,
            source_fault=False,
            source_legibility_status=legibility,
            blocking_condition=None,
            reasons=tuple(reasons),
        )
    elif package_valid and not parser_evaluation.admissible_for_ingress:
        reasons.extend(
            [
                "Package validity is not the blocking condition.",
                "Transport or receipt success is not the same as lawful ingress.",
                "The receiving parser/governance cannot lawfully preserve what arrived.",
            ]
        )
        if parser_evaluation.parser_contaminated:
            reasons.extend(
                [
                    "Derivative-only arrival cannot be lawfully preserved under the contaminated receiving parser/governance.",
                    "No false blame shifts back onto the source-side lawful release.",
                ]
            )
            evaluation = IngressEvaluation(
                parser_mode=parser_mode,
                parser_contaminated=True,
                technical_receipt=technical_receipt,
                package_valid=True,
                ingress_lawful=False,
                ingress_outcome="contaminated_parser_non_passage",
                arrival_status="none",
                source_remains_source=True,
                shared_authority=False,
                standing_upgraded=False,
                refusal_visible=True,
                non_passage=True,
                source_fault=False,
                source_legibility_status=legibility,
                blocking_condition="receiving_parser_governance_contamination",
                reasons=tuple(reasons),
            )
        else:
            reasons.append("Receiving-side parser/governance is not admissible for lawful ingress.")
            evaluation = IngressEvaluation(
                parser_mode=parser_mode,
                parser_contaminated=False,
                technical_receipt=technical_receipt,
                package_valid=True,
                ingress_lawful=False,
                ingress_outcome="refusal_non_passage",
                arrival_status="none",
                source_remains_source=True,
                shared_authority=False,
                standing_upgraded=False,
                refusal_visible=True,
                non_passage=True,
                source_fault=False,
                source_legibility_status=legibility,
                blocking_condition="receiving_parser_governance_not_admissible",
                reasons=tuple(reasons),
            )
    else:
        reasons.append(
            "Visible refusal and non-passage are preserved because lawful ingress cannot be recognized."
        )
        evaluation = IngressEvaluation(
            parser_mode=parser_mode,
            parser_contaminated=parser_evaluation.parser_contaminated,
            technical_receipt=technical_receipt,
            package_valid=False,
            ingress_lawful=False,
            ingress_outcome="invalid_package_non_passage",
            arrival_status="none",
            source_remains_source=True,
            shared_authority=False,
            standing_upgraded=False,
            refusal_visible=True,
            non_passage=True,
            source_fault=True,
            source_legibility_status=legibility,
            blocking_condition="package_validity_failure",
            reasons=tuple(reasons),
        )

    return (
        body_conformance,
        package_conformance,
        parser_conformance,
        evaluation,
    )


def build_source_summary(
    *,
    source_execution_id: str,
    run_dir: Path,
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
        "mode": "release",
        "execution_id": source_execution_id,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "artifact_family": ARTIFACT_FAMILY,
        "source_carrier_label": SOURCE_CARRIER_LABEL,
        "canonical_witness_id": canonical_body["witness_id"],
        "source_remains_source": True,
        "shared_authority": False,
        "standing_transferred": False,
        "canonical_body_schema_valid": body_conformance.status == "pass",
        "package_valid": package_valid,
        "technical_receipt_not_equal_lawful_ingress": True,
        "expected_clean_ingress_outcome": "lawful_derivative_ingress",
        "expected_contaminated_ingress_outcome": "contaminated_parser_non_passage",
        "package_path": repo_relative(package_path),
        "identity_generation_mode": identity_generation_mode(),
        "note": (
            "Bounded source-side release summary only. The same valid package is intended "
            "for clean-ingress and contaminated-parser reading without silent authority transfer."
        ),
    }


def build_receipt_record(
    *,
    receiving_execution_id: str,
    package_path: Path,
    package: Mapping[str, Any],
    parser_context: Mapping[str, Any],
    ingress_evaluation: IngressEvaluation,
) -> Dict[str, Any]:
    lineage = package.get("lineage", {})
    source_carrier = package.get("source_carrier", {})
    return {
        "experiment_id": EXPERIMENT_ID,
        "technical_receipt_record_id": local_id("technical-receipt-record"),
        "receiving_execution_id": receiving_execution_id,
        "received_at": utc_now(),
        "receiving_carrier_label": RECEIVING_CARRIER_LABEL,
        "parser_mode": parser_context.get("parser_mode"),
        "parser_contaminated": parser_context.get("parser_contaminated"),
        "package_path": repo_relative(package_path),
        "package_id": package.get("package_id"),
        "artifact_family": package.get("artifact_family"),
        "witness_id": lineage.get("witness_id"),
        "source_carrier_label": source_carrier.get("carrier_label"),
        "source_execution_id": source_carrier.get("execution_id"),
        "technical_receipt": ingress_evaluation.technical_receipt,
        "package_valid": ingress_evaluation.package_valid,
        "source_legibility_status": ingress_evaluation.source_legibility_status,
        "source_fault": ingress_evaluation.source_fault,
        "note": (
            "Technical receipt records transport/package arrival only. "
            "It does not itself declare lawful ingress."
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
    lineage = package.get("lineage", {})
    source_carrier = package.get("source_carrier", {})
    return {
        "experiment_id": EXPERIMENT_ID,
        "ingress_record_id": ingress_record_id,
        "ingressed_at": utc_now(),
        "receiving_carrier_label": RECEIVING_CARRIER_LABEL,
        "receiving_execution_id": receiving_execution_id,
        "parser_mode": ingress_evaluation.parser_mode,
        "parser_contaminated": ingress_evaluation.parser_contaminated,
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
        "shared_authority": ingress_evaluation.shared_authority,
        "standing_upgraded": ingress_evaluation.standing_upgraded,
        "source_fault": ingress_evaluation.source_fault,
        "source_legibility_status": ingress_evaluation.source_legibility_status,
        "reasoning": list(ingress_evaluation.reasons),
        "note": (
            "Bounded clean ingress record only. The arriving witness remains derivative-only "
            "and does not become receiving-side standing by receipt."
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
    lineage = package.get("lineage", {})
    source_carrier = package.get("source_carrier", {})
    return {
        "experiment_id": EXPERIMENT_ID,
        "refusal_record_id": refusal_record_id,
        "refused_at": utc_now(),
        "receiving_carrier_label": RECEIVING_CARRIER_LABEL,
        "receiving_execution_id": receiving_execution_id,
        "parser_mode": ingress_evaluation.parser_mode,
        "parser_contaminated": ingress_evaluation.parser_contaminated,
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
        "refusal_visible": ingress_evaluation.refusal_visible,
        "non_passage": ingress_evaluation.non_passage,
        "source_remains_source": ingress_evaluation.source_remains_source,
        "shared_authority": ingress_evaluation.shared_authority,
        "standing_upgraded": ingress_evaluation.standing_upgraded,
        "source_fault": ingress_evaluation.source_fault,
        "source_legibility_status": ingress_evaluation.source_legibility_status,
        "blocking_condition": ingress_evaluation.blocking_condition,
        "reasons": list(ingress_evaluation.reasons),
        "note": (
            "Visible refusal and non-passage record only. Technical receipt is kept distinct "
            "from lawful ingress, and the blocking condition remains explicit."
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
        "mode": f"ingress_{ingress_evaluation.parser_mode}",
        "execution_id": receiving_execution_id,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "package_path": repo_relative(package_path),
        "package_id": package.get("package_id"),
        "artifact_family": package.get("artifact_family"),
        "parser_mode": ingress_evaluation.parser_mode,
        "parser_contaminated": ingress_evaluation.parser_contaminated,
        "technical_receipt": ingress_evaluation.technical_receipt,
        "package_valid": ingress_evaluation.package_valid,
        "ingress_outcome": ingress_evaluation.ingress_outcome,
        "ingress_lawful": ingress_evaluation.ingress_lawful,
        "arrival_status": ingress_evaluation.arrival_status,
        "source_remains_source": ingress_evaluation.source_remains_source,
        "shared_authority": ingress_evaluation.shared_authority,
        "standing_upgraded": ingress_evaluation.standing_upgraded,
        "refusal_visible": ingress_evaluation.refusal_visible,
        "non_passage": ingress_evaluation.non_passage,
        "source_fault": ingress_evaluation.source_fault,
        "source_legibility_status": ingress_evaluation.source_legibility_status,
        "blocking_condition": ingress_evaluation.blocking_condition,
        "identity_generation_mode": identity_generation_mode(),
        "reasoning": list(ingress_evaluation.reasons),
        "note": (
            "Bounded receiving-side summary only. Technical receipt, package validity, "
            "and lawful ingress remain distinct."
        ),
    }


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
        "identity_generation_mode": identity_generation_mode(),
        "note": (
            "Implementation-local manifest only. It preserves lineage for this bounded lab proof."
        ),
    }


def resolve_cli_package_path(argument: str) -> Path:
    candidate = Path(argument).expanduser()
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate
    return candidate.resolve()


def load_package(path: Path) -> Dict[str, Any]:
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Failed to load transfer package {path}: {exc}") from exc
    if not isinstance(parsed, dict):
        raise RuntimeError(f"Transfer package {path} is not a JSON object.")
    return parsed


def print_release_summary(summary: Mapping[str, Any]) -> None:
    print("Cross-carrier release written.")
    print(f"Execution id: {summary['execution_id']}")
    print(f"Run directory: {summary['run_directory']}")
    print(
        "Ingress outcome: "
        "clean=lawful_derivative_ingress "
        "contaminated=contaminated_parser_non_passage"
    )


def print_ingress_summary(summary: Mapping[str, Any]) -> None:
    print("Cross-carrier ingress written.")
    print(f"Execution id: {summary['execution_id']}")
    print(f"Run directory: {summary['run_directory']}")
    print(f"Ingress outcome: {summary['ingress_outcome']}")


def run_release_mode() -> int:
    ensure_grounding_surfaces_exist()
    SOURCE_RUNS_ROOT.mkdir(parents=True, exist_ok=True)

    source_execution_id = new_execution_id()
    release_context_id = local_id("release-context")
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
        mode="release",
    )
    grounding_path = layout["grounding"] / "grounding.json"
    write_json(grounding_path, grounding_payload)
    written_files.append(grounding_path)

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
        source_execution_id=source_execution_id,
        release_context_id=release_context_id,
        package_id=package_id,
        witness_id=canonical_body["witness_id"],
        matter_id=matter_id,
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
        canonical_body=canonical_body,
        canonical_body_ref=repo_relative(canonical_body_path),
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
        source_execution_id=source_execution_id,
        run_dir=run_dir,
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
        mode="release",
        written_files=tuple(written_files) + (manifest_path,),
    )
    write_json(manifest_path, manifest_payload)
    written_files.append(manifest_path)

    print_release_summary(summary_payload)
    return 0


def run_ingress_mode(parser_mode: str, package_argument: str) -> int:
    ensure_grounding_surfaces_exist()
    if parser_mode == "clean":
        base_root = RECEIVING_CLEAN_RUNS_ROOT
        directory_names = (
            "package",
            "ingress",
            "conformance",
            "summary",
            "manifest",
            "grounding",
        )
    elif parser_mode == "contaminated":
        base_root = RECEIVING_CONTAMINATED_RUNS_ROOT
        directory_names = (
            "package",
            "refusal",
            "conformance",
            "summary",
            "manifest",
            "grounding",
        )
    else:
        raise ValueError(f"Unsupported ingress mode: {parser_mode}")

    base_root.mkdir(parents=True, exist_ok=True)

    package_path = resolve_cli_package_path(package_argument)
    if not package_path.is_file():
        raise FileNotFoundError(f"Transfer package does not exist: {package_path}")

    package = load_package(package_path)
    receiving_execution_id = new_execution_id()

    layout = create_run_layout(base_root, receiving_execution_id, directory_names)
    run_dir = layout["run_dir"]
    written_files: List[Path] = []

    grounding_payload = build_grounding_payload(
        execution_id=receiving_execution_id,
        run_dir=run_dir,
        mode=f"ingress_{parser_mode}",
    )
    grounding_path = layout["grounding"] / "grounding.json"
    write_json(grounding_path, grounding_payload)
    written_files.append(grounding_path)

    parser_context = build_parser_governance_context(
        parser_mode,
        receiving_execution_id=receiving_execution_id,
    )
    parser_context_path = layout["package"] / "receiving_parser_governance_context.json"
    write_json(parser_context_path, parser_context)
    written_files.append(parser_context_path)

    package_ref = repo_relative(package_path)
    (
        body_conformance,
        package_conformance,
        parser_conformance,
        ingress_evaluation,
    ) = evaluate_ingress(
        package,
        package_ref=package_ref,
        parser_context=parser_context,
    )

    receipt_record = build_receipt_record(
        receiving_execution_id=receiving_execution_id,
        package_path=package_path,
        package=package,
        parser_context=parser_context,
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

    parser_conformance_path = (
        layout["conformance"] / "receiving_parser_governance_conformance.json"
    )
    write_json(parser_conformance_path, parser_conformance.as_record())
    written_files.append(parser_conformance_path)

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
        mode=f"ingress_{parser_mode}",
        written_files=tuple(written_files) + (manifest_path,),
    )
    write_json(manifest_path, manifest_payload)
    written_files.append(manifest_path)

    print_ingress_summary(summary_payload)
    return 0


def usage() -> str:
    return (
        "Usage:\n"
        "  python lab/run_cross_carrier_seam_proof_002.py release\n"
        "  python lab/run_cross_carrier_seam_proof_002.py ingress_clean <path-to-package>\n"
        "  python lab/run_cross_carrier_seam_proof_002.py ingress_contaminated <path-to-package>\n"
    )


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print(usage(), file=sys.stderr)
        return 1

    mode = argv[1]
    if mode == "release" and len(argv) == 2:
        return run_release_mode()
    if mode == "ingress_clean" and len(argv) == 3:
        return run_ingress_mode("clean", argv[2])
    if mode == "ingress_contaminated" and len(argv) == 3:
        return run_ingress_mode("contaminated", argv[2])

    print(usage(), file=sys.stderr)
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except Exception as exc:
        print(f"cross-carrier seam proof failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
