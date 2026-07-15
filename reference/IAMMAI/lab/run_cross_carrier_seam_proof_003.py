#!/usr/bin/env python3
"""
Third bounded executable cross-carrier seam proof.

This runner proves one lawful source-side release and one receiver-local
condition surface. The same valid package is then read through one ingress
mode, with outcome determined by the receiver-local parser/governance
condition rather than by a clean/contaminated ingress mode label alone.
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

EXPERIMENT_ID = "cross_carrier_seam_proof_003"
EXPERIMENT_ROOT = REPO_ROOT / "lab" / EXPERIMENT_ID
SOURCE_RUNS_ROOT = EXPERIMENT_ROOT / "source_runs"
RECEIVING_RUNS_ROOT = EXPERIMENT_ROOT / "receiving_runs"
RECEIVER_LOCAL_CONDITION_PATH = EXPERIMENT_ROOT / "receiver_local_condition.json"

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
    condition_ref: Optional[str] = None

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
        if self.condition_ref is not None:
            record["condition_ref"] = self.condition_ref
        return record


@dataclass(frozen=True)
class PackageEvaluation:
    valid: bool
    reasons: Tuple[str, ...]


@dataclass(frozen=True)
class ReceiverLocalConditionEvaluation:
    condition_artifact_id: str
    condition_status: str
    receiver_local_governance_admissible: bool
    parser_contaminated: bool
    technical_receipt_supported: bool
    lineage_can_be_preserved: bool
    rank_can_be_preserved: bool
    refusal_visible_if_blocked: bool
    standing_inflation_risk_present: bool
    source_blame_shift_pressure_present: bool
    reasons: Tuple[str, ...]


@dataclass(frozen=True)
class IngressEvaluation:
    condition_artifact_id: str
    receiver_local_condition_status: str
    receiver_local_governance_admissible: bool
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
            "condition_artifact_id": self.condition_artifact_id,
            "receiver_local_condition_status": self.receiver_local_condition_status,
            "receiver_local_governance_admissible": (
                self.receiver_local_governance_admissible
            ),
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
    "iammai_identifier_generation_cross_carrier_proof_003",
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
    if release_context.get("receiver_local_condition_required") is not True:
        issues.append(
            ConformanceIssue(
                "Package does not preserve that receiver-local condition is required."
            )
        )
    if (
        release_context.get("same_valid_package_may_diverge_by_receiver_local_condition")
        is not True
    ):
        issues.append(
            ConformanceIssue(
                "Package does not preserve that the same valid package may diverge by receiver-local condition."
            )
        )
    if (
        release_context.get(
            "expected_ingress_under_admissible_receiver_local_condition"
        )
        != "lawful_derivative_ingress"
    ):
        issues.append(
            ConformanceIssue(
                "Package does not preserve the expected admissible-condition ingress outcome."
            )
        )
    if (
        release_context.get(
            "expected_ingress_under_contaminated_receiver_local_condition"
        )
        != "receiver_local_contamination_non_passage"
    ):
        issues.append(
            ConformanceIssue(
                "Package does not preserve the expected contaminated-condition ingress outcome."
            )
        )
    if release_context.get("do_not_blame_source_for_receiver_local_contamination") is not True:
        issues.append(
            ConformanceIssue(
                "Package does not preserve the no-false-source-blame rule for receiver-local contamination."
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
    if seam.get("receiver_local_condition_controls_admissibility") is not True:
        issues.append(
            ConformanceIssue(
                "Package does not preserve that receiver-local condition controls admissibility."
            )
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


def build_receiver_local_condition(condition_status: str) -> Dict[str, Any]:
    base = {
        "experiment_id": EXPERIMENT_ID,
        "condition_artifact_id": local_id("receiver-local-condition"),
        "generated_at": utc_now(),
        "receiver_local_condition_kind": "parser_governance_condition",
        "receiver_side_carrier_label": RECEIVING_CARRIER_LABEL,
        "technical_receipt_supported": True,
        "refusal_visible_if_blocked": True,
        "grounding_surfaces": build_grounding_surface_records(),
        "note": (
            "Implementation-local receiver condition artifact only. It determines "
            "receiving-side admissibility for this bounded proof without rewriting "
            "the source-side package."
        ),
    }

    if condition_status == "admissible":
        base.update(
            {
                "parser_governance_status": "admissible",
                "receiver_local_governance_admissible": True,
                "parser_contaminated": False,
                "lineage_can_be_preserved": True,
                "rank_can_be_preserved": True,
                "standing_inflation_risk_present": False,
                "source_blame_shift_pressure_present": False,
            }
        )
        return base

    if condition_status == "contaminated":
        base.update(
            {
                "parser_governance_status": "contaminated",
                "receiver_local_governance_admissible": False,
                "parser_contaminated": True,
                "lineage_can_be_preserved": False,
                "rank_can_be_preserved": False,
                "standing_inflation_risk_present": True,
                "source_blame_shift_pressure_present": True,
            }
        )
        return base

    raise ValueError(f"Unsupported receiver-local condition status: {condition_status}")


def load_receiver_local_condition() -> Dict[str, Any]:
    if not RECEIVER_LOCAL_CONDITION_PATH.is_file():
        raise FileNotFoundError(
            "Receiver-local condition artifact is missing. "
            "Run init_receiver_clean or init_receiver_contaminated first: "
            f"{RECEIVER_LOCAL_CONDITION_PATH}"
        )

    try:
        parsed = json.loads(RECEIVER_LOCAL_CONDITION_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(
            "Failed to read receiver-local condition artifact "
            f"{RECEIVER_LOCAL_CONDITION_PATH}: {exc}"
        ) from exc

    if not isinstance(parsed, dict):
        raise RuntimeError(
            "Receiver-local condition artifact is not a JSON object: "
            f"{RECEIVER_LOCAL_CONDITION_PATH}"
        )
    return parsed


def validate_receiver_local_condition(
    condition: Mapping[str, Any],
    *,
    condition_ref: str,
) -> Tuple[ConformanceRecord, ReceiverLocalConditionEvaluation]:
    issues: List[ConformanceIssue] = []

    required_string_fields = (
        "experiment_id",
        "condition_artifact_id",
        "receiver_local_condition_kind",
        "receiver_side_carrier_label",
        "parser_governance_status",
        "generated_at",
    )
    for field_name in required_string_fields:
        value = condition.get(field_name)
        if not isinstance(value, str) or not value.strip():
            issues.append(
                ConformanceIssue(
                    f"Receiver-local condition field {field_name} must be a non-empty string."
                )
            )

    required_bool_fields = (
        "receiver_local_governance_admissible",
        "parser_contaminated",
        "technical_receipt_supported",
        "lineage_can_be_preserved",
        "rank_can_be_preserved",
        "refusal_visible_if_blocked",
        "standing_inflation_risk_present",
        "source_blame_shift_pressure_present",
    )
    for field_name in required_bool_fields:
        value = condition.get(field_name)
        if not isinstance(value, bool):
            issues.append(
                ConformanceIssue(
                    f"Receiver-local condition field {field_name} must be boolean."
                )
            )

    if condition.get("experiment_id") != EXPERIMENT_ID:
        issues.append(ConformanceIssue("Receiver-local condition does not match this proof."))
    if condition.get("receiver_local_condition_kind") != "parser_governance_condition":
        issues.append(
            ConformanceIssue(
                "Receiver-local condition kind must be parser_governance_condition."
            )
        )
    if condition.get("receiver_side_carrier_label") != RECEIVING_CARRIER_LABEL:
        issues.append(
            ConformanceIssue("Receiver-local condition does not preserve the receiving carrier label.")
        )
    if not parse_datetime_string(str(condition.get("generated_at", ""))):
        issues.append(
            ConformanceIssue("Receiver-local condition generated_at is not a valid date-time string.")
        )
    if condition.get("technical_receipt_supported") is not True:
        issues.append(
            ConformanceIssue(
                "Receiver-local condition must preserve technical receipt support for this proof."
            )
        )
    if condition.get("refusal_visible_if_blocked") is not True:
        issues.append(
            ConformanceIssue(
                "Receiver-local condition must preserve visible refusal when ingress is blocked."
            )
        )

    status_value = condition.get("parser_governance_status")
    if status_value not in {"admissible", "contaminated"}:
        issues.append(
            ConformanceIssue(
                "Receiver-local condition parser_governance_status must be admissible or contaminated."
            )
        )
        status_value = "unknown"

    if status_value == "admissible":
        if condition.get("receiver_local_governance_admissible") is not True:
            issues.append(
                ConformanceIssue(
                    "Admissible receiver-local condition must declare governance admissible."
                )
            )
        if condition.get("parser_contaminated") is not False:
            issues.append(
                ConformanceIssue(
                    "Admissible receiver-local condition must not declare parser contamination."
                )
            )
        if condition.get("lineage_can_be_preserved") is not True:
            issues.append(
                ConformanceIssue(
                    "Admissible receiver-local condition must preserve lineage."
                )
            )
        if condition.get("rank_can_be_preserved") is not True:
            issues.append(
                ConformanceIssue("Admissible receiver-local condition must preserve rank.")
            )
        if condition.get("standing_inflation_risk_present") is not False:
            issues.append(
                ConformanceIssue(
                    "Admissible receiver-local condition must not carry standing inflation risk."
                )
            )
        if condition.get("source_blame_shift_pressure_present") is not False:
            issues.append(
                ConformanceIssue(
                    "Admissible receiver-local condition must not carry source-blame shift pressure."
                )
            )
    elif status_value == "contaminated":
        if condition.get("receiver_local_governance_admissible") is not False:
            issues.append(
                ConformanceIssue(
                    "Contaminated receiver-local condition must deny governance admissibility."
                )
            )
        if condition.get("parser_contaminated") is not True:
            issues.append(
                ConformanceIssue(
                    "Contaminated receiver-local condition must declare parser contamination."
                )
            )
        if condition.get("lineage_can_be_preserved") is not False:
            issues.append(
                ConformanceIssue(
                    "Contaminated receiver-local condition must deny lawful lineage preservation under ingress."
                )
            )
        if condition.get("rank_can_be_preserved") is not False:
            issues.append(
                ConformanceIssue(
                    "Contaminated receiver-local condition must deny lawful rank preservation under ingress."
                )
            )
        if condition.get("standing_inflation_risk_present") is not True:
            issues.append(
                ConformanceIssue(
                    "Contaminated receiver-local condition must preserve standing inflation risk."
                )
            )
        if condition.get("source_blame_shift_pressure_present") is not True:
            issues.append(
                ConformanceIssue(
                    "Contaminated receiver-local condition must preserve source-blame shift pressure."
                )
            )

    condition_errors = tuple(issues)
    conformance = ConformanceRecord(
        surface="receiver_local_condition_artifact",
        conformance_kind="receiver_local_condition_shape",
        status="pass" if not issues else "fail",
        checked_at=utc_now(),
        artifact_family=ARTIFACT_FAMILY,
        validation_mode="local_receiver_condition_reader",
        condition_ref=condition_ref,
        errors=condition_errors,
    )

    reasons: List[str] = []
    if status_value == "admissible":
        reasons.extend(
            [
                "Receiver-local parser/governance is admissible for lawful derivative-only ingress.",
                "Receiver-local condition can preserve lineage and rank without standing inflation.",
            ]
        )
    elif status_value == "contaminated":
        reasons.extend(
            [
                "Receiver-local parser/governance remains contaminated.",
                "Technical receipt may still occur, but lawful ingress cannot be preserved under this local condition.",
                "Source-blame shift pressure remains present locally and must not be ratified as source fault.",
            ]
        )
    else:
        reasons.append("Receiver-local parser/governance status is unreadable.")

    evaluation = ReceiverLocalConditionEvaluation(
        condition_artifact_id=str(condition.get("condition_artifact_id") or "unreadable"),
        condition_status=str(status_value),
        receiver_local_governance_admissible=bool(
            condition.get("receiver_local_governance_admissible")
        ),
        parser_contaminated=bool(condition.get("parser_contaminated")),
        technical_receipt_supported=bool(condition.get("technical_receipt_supported")),
        lineage_can_be_preserved=bool(condition.get("lineage_can_be_preserved")),
        rank_can_be_preserved=bool(condition.get("rank_can_be_preserved")),
        refusal_visible_if_blocked=bool(condition.get("refusal_visible_if_blocked")),
        standing_inflation_risk_present=bool(
            condition.get("standing_inflation_risk_present")
        ),
        source_blame_shift_pressure_present=bool(
            condition.get("source_blame_shift_pressure_present")
        ),
        reasons=tuple(reasons),
    )
    return conformance, evaluation


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


def write_json_replacing(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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
        "surface_ref": "lab:cross_carrier_seam_proof_003:source_release",
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
            "One source-side carrier releases one valid witness artifact package for receiver-local condition-dependent ingress."
        ),
        "seam_statement": (
            "Source remains source. The same valid package may ingress lawfully or fail lawfully "
            "with visible non-passage depending on the receiver-local parser/governance condition."
        ),
        "receiver_local_condition_required": True,
        "expected_ingress_under_admissible_receiver_local_condition": (
            "lawful_derivative_ingress"
        ),
        "expected_ingress_under_contaminated_receiver_local_condition": (
            "receiver_local_contamination_non_passage"
        ),
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
                "Source remains source. The same valid package may be technically receivable on different receivers "
                "while lawful ingress still depends on the receiver-local parser/governance condition."
            ),
            "receiver_local_condition_required": True,
            "same_valid_package_may_diverge_by_receiver_local_condition": True,
            "expected_ingress_under_admissible_receiver_local_condition": (
                "lawful_derivative_ingress"
            ),
            "expected_ingress_under_contaminated_receiver_local_condition": (
                "receiver_local_contamination_non_passage"
            ),
            "do_not_blame_source_for_receiver_local_contamination": True,
            "receiver_local_condition_ref": repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
        },
        "seam": {
            "explicit_release": True,
            "explicit_seam": True,
            "explicit_ingress_required": True,
            "receiver_local_condition_controls_admissibility": True,
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
                "Lawful source-side release package for receiver-local condition-dependent cross-carrier reading."
            ),
        },
    }


def evaluate_ingress(
    package: Mapping[str, Any],
    *,
    package_ref: str,
    receiver_condition_evaluation: ReceiverLocalConditionEvaluation,
) -> Tuple[ConformanceRecord, ConformanceRecord, IngressEvaluation]:
    body = package.get("canonical_body", {})
    body_conformance = validate_witness_body(
        body if isinstance(body, Mapping) else {},
        surface="receiving_side_carried_witness_body",
    )
    package_conformance, package_evaluation = build_package_conformance(
        package,
        package_ref=package_ref,
    )

    technical_receipt = receiver_condition_evaluation.technical_receipt_supported
    package_valid = (
        body_conformance.status == "pass" and package_evaluation.valid
    )
    legibility = source_legibility_status(package, body_conformance)

    reasons: List[str] = []
    if technical_receipt:
        reasons.append("Technical receipt occurred on the receiving-side carrier.")
    else:
        reasons.append("Technical receipt did not occur on the receiving-side carrier.")

    if package_valid:
        reasons.append("The carried package is valid and the source-side release remains legible.")
    else:
        reasons.append("Package validity failed before lawful ingress could be recognized.")
        if body_conformance.status != "pass":
            reasons.append(
                "Carried canonical witness body does not validate against the witness schema."
            )
        reasons.extend(package_evaluation.reasons)

    reasons.extend(receiver_condition_evaluation.reasons)

    if package_valid and receiver_condition_evaluation.receiver_local_governance_admissible:
        reasons.extend(
            [
                "The receiver-local condition lawfully preserves derivative-only arrival.",
                "Source remains source and no silent authority inheritance occurs.",
            ]
        )
        evaluation = IngressEvaluation(
            condition_artifact_id=receiver_condition_evaluation.condition_artifact_id,
            receiver_local_condition_status=receiver_condition_evaluation.condition_status,
            receiver_local_governance_admissible=True,
            parser_contaminated=receiver_condition_evaluation.parser_contaminated,
            technical_receipt=technical_receipt,
            package_valid=True,
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
    elif package_valid and not receiver_condition_evaluation.receiver_local_governance_admissible:
        reasons.extend(
            [
                "Package validity is not the blocking condition.",
                "The same valid package may yield different lawful outcomes depending on receiver-local condition.",
                "Transport or receipt success is not the same as lawful ingress.",
                "Receiver-local parser/governance contamination blocks lawful ingress.",
                "No false blame shifts back onto the source-side lawful release.",
            ]
        )
        evaluation = IngressEvaluation(
            condition_artifact_id=receiver_condition_evaluation.condition_artifact_id,
            receiver_local_condition_status=receiver_condition_evaluation.condition_status,
            receiver_local_governance_admissible=False,
            parser_contaminated=receiver_condition_evaluation.parser_contaminated,
            technical_receipt=technical_receipt,
            package_valid=True,
            ingress_lawful=False,
            ingress_outcome="receiver_local_contamination_non_passage",
            arrival_status="none",
            source_remains_source=True,
            shared_authority=False,
            standing_upgraded=False,
            refusal_visible=receiver_condition_evaluation.refusal_visible_if_blocked,
            non_passage=True,
            source_fault=False,
            source_legibility_status=legibility,
            blocking_condition="receiver_local_parser_governance_contamination",
            reasons=tuple(reasons),
        )
    else:
        reasons.append(
            "Visible refusal and non-passage are preserved because lawful ingress cannot be recognized."
        )
        evaluation = IngressEvaluation(
            condition_artifact_id=receiver_condition_evaluation.condition_artifact_id,
            receiver_local_condition_status=receiver_condition_evaluation.condition_status,
            receiver_local_governance_admissible=(
                receiver_condition_evaluation.receiver_local_governance_admissible
            ),
            parser_contaminated=receiver_condition_evaluation.parser_contaminated,
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

    return body_conformance, package_conformance, evaluation


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
        "receiver_local_condition_ref": repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
        "expected_ingress_under_admissible_receiver_local_condition": (
            "lawful_derivative_ingress"
        ),
        "expected_ingress_under_contaminated_receiver_local_condition": (
            "receiver_local_contamination_non_passage"
        ),
        "package_path": repo_relative(package_path),
        "identity_generation_mode": identity_generation_mode(),
        "note": (
            "Bounded source-side release summary only. The same valid package is intended "
            "for receiver-local condition-dependent ingress without silent authority transfer."
        ),
    }


def build_receipt_record(
    *,
    receiving_execution_id: str,
    package_path: Path,
    package: Mapping[str, Any],
    receiver_condition: Mapping[str, Any],
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
        "receiver_local_condition_ref": repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
        "condition_artifact_id": receiver_condition.get("condition_artifact_id"),
        "receiver_local_condition_status": receiver_condition.get("parser_governance_status"),
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
            "Technical receipt records package arrival only. It does not itself declare lawful ingress."
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
        "receiver_local_condition_ref": repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
        "condition_artifact_id": ingress_evaluation.condition_artifact_id,
        "receiver_local_condition_status": ingress_evaluation.receiver_local_condition_status,
        "receiver_local_governance_admissible": (
            ingress_evaluation.receiver_local_governance_admissible
        ),
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
            "Bounded lawful ingress record only. The arriving witness remains derivative-only "
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
        "receiver_local_condition_ref": repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
        "condition_artifact_id": ingress_evaluation.condition_artifact_id,
        "receiver_local_condition_status": ingress_evaluation.receiver_local_condition_status,
        "receiver_local_governance_admissible": (
            ingress_evaluation.receiver_local_governance_admissible
        ),
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
            "from lawful ingress, and receiver-local contamination remains the blocking condition."
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
        "mode": "ingress",
        "execution_id": receiving_execution_id,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "receiver_local_condition_ref": repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
        "condition_artifact_id": ingress_evaluation.condition_artifact_id,
        "receiver_local_condition_status": ingress_evaluation.receiver_local_condition_status,
        "receiver_local_governance_admissible": (
            ingress_evaluation.receiver_local_governance_admissible
        ),
        "parser_contaminated": ingress_evaluation.parser_contaminated,
        "package_path": repo_relative(package_path),
        "package_id": package.get("package_id"),
        "artifact_family": package.get("artifact_family"),
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
        "same_valid_package_may_diverge_by_receiver_local_condition": True,
        "identity_generation_mode": identity_generation_mode(),
        "reasoning": list(ingress_evaluation.reasons),
        "note": (
            "Bounded receiving-side summary only. Technical receipt, package validity, "
            "receiver-local admissibility, and lawful ingress remain distinct."
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
        "admissible_receiver_local_condition=lawful_derivative_ingress "
        "contaminated_receiver_local_condition=receiver_local_contamination_non_passage"
    )


def print_receiver_condition_summary(condition: Mapping[str, Any]) -> None:
    print("Receiver-local condition written.")
    print(f"Condition id: {condition['condition_artifact_id']}")
    print(f"Condition path: {repo_relative(RECEIVER_LOCAL_CONDITION_PATH)}")
    print(f"Condition status: {condition['parser_governance_status']}")


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


def run_init_receiver_condition_mode(condition_status: str) -> int:
    ensure_grounding_surfaces_exist()
    EXPERIMENT_ROOT.mkdir(parents=True, exist_ok=True)

    condition_payload = build_receiver_local_condition(condition_status)
    write_json_replacing(RECEIVER_LOCAL_CONDITION_PATH, condition_payload)
    print_receiver_condition_summary(condition_payload)
    return 0


def run_ingress_mode(package_argument: str) -> int:
    ensure_grounding_surfaces_exist()
    RECEIVING_RUNS_ROOT.mkdir(parents=True, exist_ok=True)

    package_path = resolve_cli_package_path(package_argument)
    if not package_path.is_file():
        raise FileNotFoundError(f"Transfer package does not exist: {package_path}")

    package = load_package(package_path)
    receiver_condition = load_receiver_local_condition()
    condition_conformance, receiver_condition_evaluation = validate_receiver_local_condition(
        receiver_condition,
        condition_ref=repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
    )
    if condition_conformance.status != "pass":
        error_text = "; ".join(issue.message for issue in condition_conformance.errors)
        raise RuntimeError(
            "Receiver-local condition artifact is malformed: "
            f"{repo_relative(RECEIVER_LOCAL_CONDITION_PATH)}: {error_text}"
        )

    receiving_execution_id = new_execution_id()
    layout = create_run_layout(
        RECEIVING_RUNS_ROOT,
        receiving_execution_id,
        (
            "package",
            "conformance",
            "summary",
            "manifest",
            "grounding",
            "ingress",
            "refusal",
        ),
    )
    run_dir = layout["run_dir"]
    written_files: List[Path] = []

    grounding_payload = build_grounding_payload(
        execution_id=receiving_execution_id,
        run_dir=run_dir,
        mode="ingress",
    )
    grounding_path = layout["grounding"] / "grounding.json"
    write_json(grounding_path, grounding_payload)
    written_files.append(grounding_path)

    condition_snapshot_path = layout["package"] / "receiver_local_condition_snapshot.json"
    write_json(condition_snapshot_path, receiver_condition)
    written_files.append(condition_snapshot_path)

    receipt_placeholder = {
        "experiment_id": EXPERIMENT_ID,
        "package_path": repo_relative(package_path),
        "receiver_local_condition_ref": repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
        "note": "Package and receiver-local condition were both readable before ingress evaluation.",
    }
    input_read_path = layout["package"] / "input_read_record.json"
    write_json(input_read_path, receipt_placeholder)
    written_files.append(input_read_path)

    (
        body_conformance,
        package_conformance,
        ingress_evaluation,
    ) = evaluate_ingress(
        package,
        package_ref=repo_relative(package_path),
        receiver_condition_evaluation=receiver_condition_evaluation,
    )

    receipt_record = build_receipt_record(
        receiving_execution_id=receiving_execution_id,
        package_path=package_path,
        package=package,
        receiver_condition=receiver_condition,
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

    condition_conformance_path = (
        layout["conformance"] / "receiver_local_condition_conformance.json"
    )
    write_json(condition_conformance_path, condition_conformance.as_record())
    written_files.append(condition_conformance_path)

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
        mode="ingress",
        written_files=tuple(written_files) + (manifest_path,),
    )
    write_json(manifest_path, manifest_payload)
    written_files.append(manifest_path)

    print_ingress_summary(summary_payload)
    return 0


def usage() -> str:
    return (
        "Usage:\n"
        "  python lab/run_cross_carrier_seam_proof_003.py release\n"
        "  python lab/run_cross_carrier_seam_proof_003.py init_receiver_clean\n"
        "  python lab/run_cross_carrier_seam_proof_003.py init_receiver_contaminated\n"
        "  python lab/run_cross_carrier_seam_proof_003.py ingress <path-to-package>\n"
    )


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print(usage(), file=sys.stderr)
        return 1

    mode = argv[1]
    if mode == "release" and len(argv) == 2:
        return run_release_mode()
    if mode == "init_receiver_clean" and len(argv) == 2:
        return run_init_receiver_condition_mode("admissible")
    if mode == "init_receiver_contaminated" and len(argv) == 2:
        return run_init_receiver_condition_mode("contaminated")
    if mode == "ingress" and len(argv) == 3:
        return run_ingress_mode(argv[2])

    print(usage(), file=sys.stderr)
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except Exception as exc:
        print(f"cross-carrier seam proof failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
