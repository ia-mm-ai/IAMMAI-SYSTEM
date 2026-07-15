#!/usr/bin/env python3
"""
Bounded v1 runner for the second ordinary proof slice.

This script forms canonical bodies for the five ordinary v1 artifact families,
validates them against the v1 schemas, carries them in explicitly separable
execution-bearing envelopes, and preserves the result through the shared
implementation-local preservation layout under v1/registry/runs/.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence, Tuple
from uuid import uuid4

try:
    from preservation_layout import (
        PreservationLayoutError,
        RunLayout,
        RUNS_DIR as LAYOUT_RUNS_DIR,
        WrittenOutput,
        build_manifest_payload,
        create_ordinary_run_layout,
        write_fixture,
        write_json,
        write_manifest,
        write_summary,
    )
except ImportError:  # pragma: no cover - package import fallback
    from v1.embodiment.run.preservation_layout import (  # type: ignore
        PreservationLayoutError,
        RunLayout,
        RUNS_DIR as LAYOUT_RUNS_DIR,
        WrittenOutput,
        build_manifest_payload,
        create_ordinary_run_layout,
        write_fixture,
        write_json,
        write_manifest,
        write_summary,
    )


REPO_ROOT = Path(__file__).resolve().parents[3]
V1_DIR = REPO_ROOT / "v1"
SCHEMA_DIR = V1_DIR / "schemas"
RUNS_DIR = V1_DIR / "registry" / "runs"

CONDITION_SET_REF = "condition-set-v1-second-proof-slice-threshold-validation"
ACTOR_REF = "actor-v1-local-operator"
LEGITIMACY_BASIS_REF = "legitimacy-basis-v1-second-proof-slice"
SURFACE_REF = "surface-v1-local-proof-slice"


@dataclass(frozen=True)
class FamilySpec:
    name: str
    schema_filename: str
    id_field: str
    body_filename: str


FAMILY_SPECS: Tuple[FamilySpec, ...] = (
    FamilySpec(
        name="validation_artifact",
        schema_filename="validation_artifact.schema.json",
        id_field="validation_id",
        body_filename="validation_artifact.body.json",
    ),
    FamilySpec(
        name="witness_artifact",
        schema_filename="witness_artifact.schema.json",
        id_field="witness_id",
        body_filename="witness_artifact.body.json",
    ),
    FamilySpec(
        name="governance_action",
        schema_filename="governance_action.schema.json",
        id_field="governance_action_id",
        body_filename="governance_action.body.json",
    ),
    FamilySpec(
        name="transition_record",
        schema_filename="transition_record.schema.json",
        id_field="transition_id",
        body_filename="transition_record.body.json",
    ),
    FamilySpec(
        name="state_record",
        schema_filename="state_record.schema.json",
        id_field="state_id",
        body_filename="state_record.body.json",
    ),
)


class MissingJsonSchemaDependency(RuntimeError):
    """Raised when jsonschema is unavailable for the bounded proof slice."""


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def repo_relative(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def generate_identity(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex}"


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_validator_tools() -> Tuple[Any, Any]:
    try:
        from jsonschema import FormatChecker
        from jsonschema.validators import validator_for
    except ImportError as exc:  # pragma: no cover - dependency posture only
        raise MissingJsonSchemaDependency(
            "This runner requires the 'jsonschema' package. "
            "Install it with 'python -m pip install jsonschema' and rerun."
        ) from exc

    return validator_for, FormatChecker


def load_schema_validators() -> Dict[str, Dict[str, Any]]:
    validator_for, format_checker_class = load_validator_tools()
    validators: Dict[str, Dict[str, Any]] = {}

    for spec in FAMILY_SPECS:
        schema_path = SCHEMA_DIR / spec.schema_filename
        schema = read_json(schema_path)
        validator_class = validator_for(schema)
        validator_class.check_schema(schema)
        validators[spec.name] = {
            "schema": schema,
            "schema_path": schema_path,
            "validator": validator_class(schema, format_checker=format_checker_class()),
        }

    return validators


def track_output(
    written_outputs: List[WrittenOutput],
    output: WrittenOutput,
) -> WrittenOutput:
    written_outputs.append(output)
    return output


def build_positive_bodies(
    matter_id: str,
    threshold_state_ref: str,
    artifact_ids: Mapping[str, str],
    recorded_at: str,
) -> Dict[str, Dict[str, Any]]:
    validation = {
        "validation_id": artifact_ids["validation_artifact"],
        "validation_type": "threshold_validation",
        "target_ref": matter_id,
        "condition_set_ref": CONDITION_SET_REF,
        "outcome": "pass",
        "checked_at": recorded_at,
        "reason_refs": [
            "reason-v1-bounded-input-present",
            "reason-v1-bounded-threshold-satisfied",
        ],
        "related_witness_ref": artifact_ids["witness_artifact"],
    }

    witness = {
        "witness_id": artifact_ids["witness_artifact"],
        "witness_type": "validation_witness",
        "target_ref": matter_id,
        "observed_at": recorded_at,
        "claims": [
            "contact_occurred",
            "bounded_interaction_preserved",
            "validation_event_observed",
        ],
        "non_claims": [
            "not_authorship",
            "not_semantic_source",
            "not_final_authority",
            "not_automatic_truth_creation",
            "not_governance_force",
        ],
        "surface_ref": SURFACE_REF,
        "related_validation_ref": artifact_ids["validation_artifact"],
    }

    governance = {
        "governance_action_id": artifact_ids["governance_action"],
        "action_type": "authorize",
        "authority_class": "local_operator_governor",
        "actor_ref": ACTOR_REF,
        "legitimacy_basis_ref": LEGITIMACY_BASIS_REF,
        "matter_ref": matter_id,
        "acted_at": recorded_at,
        "related_validation_ref": artifact_ids["validation_artifact"],
        "related_witness_ref": artifact_ids["witness_artifact"],
    }

    transition = {
        "transition_id": artifact_ids["transition_record"],
        "matter_ref": matter_id,
        "source_ref": threshold_state_ref,
        "target_ref": artifact_ids["state_record"],
        "transition_type": "truth_formation",
        "occurred_at": recorded_at,
        "related_validation_ref": artifact_ids["validation_artifact"],
        "related_witness_ref": artifact_ids["witness_artifact"],
        "related_governance_action_ref": artifact_ids["governance_action"],
    }

    state = {
        "state_id": artifact_ids["state_record"],
        "matter_ref": matter_id,
        "state_family": "standing",
        "state_type": "truth",
        "recorded_at": recorded_at,
        "predecessor_ref": threshold_state_ref,
        "related_transition_ref": artifact_ids["transition_record"],
        "related_governance_action_ref": artifact_ids["governance_action"],
        "related_validation_ref": artifact_ids["validation_artifact"],
        "related_witness_ref": artifact_ids["witness_artifact"],
    }

    return {
        "validation_artifact": validation,
        "witness_artifact": witness,
        "governance_action": governance,
        "transition_record": transition,
        "state_record": state,
    }


def build_negative_validation_fixture(
    matter_id: str,
    recorded_at: str,
) -> Dict[str, Any]:
    return {
        "validation_id": generate_identity("validation"),
        "validation_type": "threshold_validation",
        "target_ref": matter_id,
        "outcome": "pass",
        "checked_at": recorded_at,
    }


def validate_body(
    family_name: str,
    body: Mapping[str, Any],
    body_path: Path,
    schema_entry: Mapping[str, Any],
    fixture_classification: str,
    expected_status: str,
) -> Dict[str, Any]:
    validator = schema_entry["validator"]
    schema_path: Path = schema_entry["schema_path"]
    errors = sorted(validator.iter_errors(body), key=lambda error: list(error.path))
    error_items = [
        {
            "message": error.message,
            "validator": error.validator,
            "instance_path": list(error.path),
            "schema_path": list(error.schema_path),
        }
        for error in errors
    ]
    status = "pass" if not error_items else "fail"

    return {
        "surface": "canonical_body_conformance",
        "artifact_family": family_name,
        "fixture_classification": fixture_classification,
        "expected_status": expected_status,
        "status": status,
        "matched_expectation": status == expected_status,
        "checked_at": utc_now(),
        "schema_ref": repo_relative(schema_path),
        "body_ref": repo_relative(body_path),
        "errors": error_items,
    }


def build_envelope(
    family_name: str,
    body: Mapping[str, Any],
    execution_id: str,
    body_ref: str,
    emitted_at: str,
) -> Dict[str, Any]:
    return {
        "envelope": {
            "execution_id": execution_id,
            "artifact_family": family_name,
            "emitted_at": emitted_at,
            "canonical_body_ref": body_ref,
        },
        "body": dict(body),
    }


def validate_envelope(
    family_name: str,
    envelope_object: Mapping[str, Any],
    body: Mapping[str, Any],
    execution_id: str,
    expected_body_ref: str,
    envelope_path: Path,
) -> Dict[str, Any]:
    errors: List[Dict[str, Any]] = []
    envelope = envelope_object.get("envelope")
    carried_body = envelope_object.get("body")

    if not isinstance(envelope, dict):
        errors.append({"message": "Missing explicit envelope object."})
    if not isinstance(carried_body, dict):
        errors.append({"message": "Missing explicit carried body object."})

    if isinstance(envelope, dict):
        if envelope.get("execution_id") != execution_id:
            errors.append(
                {
                    "message": "Envelope execution identity does not match run execution identity."
                }
            )
        if envelope.get("artifact_family") != family_name:
            errors.append(
                {
                    "message": "Envelope artifact family does not match the carried family."
                }
            )
        if envelope.get("canonical_body_ref") != expected_body_ref:
            errors.append(
                {
                    "message": "Envelope canonical_body_ref does not point to the preserved canonical body."
                }
            )

    if isinstance(carried_body, dict):
        if carried_body != body:
            errors.append(
                {"message": "Envelope body does not match the preserved canonical body."}
            )
        if "run_id" in carried_body or "execution_id" in carried_body:
            errors.append(
                {
                    "message": "Carried body illegally contains execution identity inside canonical body content."
                }
            )

    return {
        "surface": "envelope_bearing_conformance",
        "artifact_family": family_name,
        "status": "pass" if not errors else "fail",
        "checked_at": utc_now(),
        "envelope_ref": repo_relative(envelope_path),
        "canonical_body_ref": expected_body_ref,
        "errors": errors,
    }


def evaluate_preservation_conformance(
    layout: RunLayout,
    written_outputs: Sequence[WrittenOutput],
) -> Dict[str, Any]:
    checks: List[Dict[str, Any]] = []

    def add_check(name: str, condition: bool, message: str) -> None:
        checks.append(
            {
                "name": name,
                "status": "pass" if condition else "fail",
                "message": message,
            }
        )

    add_check(
        "written_files_exist",
        all(output.path.exists() for output in written_outputs),
        "All preserved files recorded before preservation conformance must exist.",
    )
    add_check(
        "canonical_bodies_separate_from_envelopes",
        sum(1 for output in written_outputs if output.layer == "canonical_body")
        == len(FAMILY_SPECS)
        and sum(1 for output in written_outputs if output.layer == "envelope")
        == len(FAMILY_SPECS),
        "Canonical bodies and envelope-bearing emissions must both be preserved separately.",
    )
    add_check(
        "conformance_layer_present",
        any(output.layer == "conformance" for output in written_outputs),
        "Conformance material must remain explicitly preserved as its own readable layer.",
    )
    add_check(
        "negative_fixture_separated",
        any(output.layer == "fixtures" for output in written_outputs)
        and all(
            "/fixture_outputs/negative/" in repo_relative(output.path)
            for output in written_outputs
            if output.layer == "fixtures"
        ),
        "Negative fixture material must remain under an explicitly separate negative fixture branch.",
    )
    add_check(
        "continuity_not_emitted",
        layout.kind == "ordinary"
        and all("/continuity/" not in repo_relative(output.path) for output in written_outputs),
        "Continuity remains out of scope for the bounded ordinary proof slice.",
    )
    add_check(
        "shared_layout_surface_used",
        layout.kind == "ordinary"
        and layout.naming_posture == "implementation_local_default",
        "The bounded ordinary proof slice must preserve outputs through the shared implementation-local layout surface.",
    )
    add_check(
        "run_directory_bounded_to_v1_registry",
        layout.root_dir.parent == RUNS_DIR,
        "The local preservation surface must remain bounded to v1/registry/runs/<execution-identity>/.",
    )

    errors = [check for check in checks if check["status"] == "fail"]
    return {
        "surface": "preservation_conformance",
        "status": "pass" if not errors else "fail",
        "checked_at": utc_now(),
        "run_directory": repo_relative(layout.root_dir),
        "preservation_layout": layout.as_record(),
        "checks": checks,
    }


def build_run_summary(
    execution_id: str,
    matter_id: str,
    layout: RunLayout,
    body_results: Mapping[str, Dict[str, Any]],
    envelope_results: Mapping[str, Dict[str, Any]],
    negative_result: Mapping[str, Any],
    fixture_classification_ref: str,
    preservation_result_ref: str,
    preservation_status: str,
) -> Dict[str, Any]:
    return {
        "summary_type": "v1_second_proof_slice_summary",
        "execution_identity": execution_id,
        "matter_identity": matter_id,
        "run_directory": repo_relative(layout.root_dir),
        "preservation_layout": layout.as_record(),
        "scope": {
            "artifact_families": [spec.name for spec in FAMILY_SPECS],
            "continuity_emitted": False,
            "note": "This bounded runner implements the ordinary proof slice only.",
        },
        "layer_outcomes": {
            "body_conformance": {
                "positive": [
                    {
                        "artifact_family": family_name,
                        "status": result["status"],
                        "matched_expectation": result["matched_expectation"],
                        "result_ref": result["result_ref"],
                    }
                    for family_name, result in body_results.items()
                ],
                "negative": [
                    {
                        "artifact_family": negative_result["artifact_family"],
                        "status": negative_result["status"],
                        "matched_expectation": negative_result["matched_expectation"],
                        "result_ref": negative_result["result_ref"],
                    }
                ],
            },
            "envelope_bearing_conformance": {
                "positive": [
                    {
                        "artifact_family": family_name,
                        "status": result["status"],
                        "result_ref": result["result_ref"],
                    }
                    for family_name, result in envelope_results.items()
                ]
            },
            "preservation_write_outcome": {
                "status": preservation_status,
                "result_ref": preservation_result_ref,
            },
            "fixture_classification": {
                "negative": [
                    {
                        "fixture_class": "conformance_failure",
                        "classification_ref": fixture_classification_ref,
                    }
                ]
            },
        },
        "reading_posture": {
            "positive_path": "read by body, envelope, and preservation layers",
            "negative_fixture": "read as an expected conformance failure, not as accidental architectural incoherence",
        },
    }


def main() -> int:
    try:
        schema_validators = load_schema_validators()
    except MissingJsonSchemaDependency as exc:
        print(str(exc), file=sys.stderr)
        return 1

    execution_id = generate_identity("execution")
    matter_id = generate_identity("matter")
    threshold_state_ref = generate_identity("state-preparation-threshold")
    recorded_at = utc_now()

    artifact_ids = {
        spec.name: generate_identity(spec.id_field.removesuffix("_id"))
        for spec in FAMILY_SPECS
    }
    positive_bodies = build_positive_bodies(
        matter_id=matter_id,
        threshold_state_ref=threshold_state_ref,
        artifact_ids=artifact_ids,
        recorded_at=recorded_at,
    )

    try:
        layout = create_ordinary_run_layout(
            execution_id,
            LAYOUT_RUNS_DIR,
            exist_ok=False,
        )
        written_outputs: List[WrittenOutput] = []
        body_results: Dict[str, Dict[str, Any]] = {}
        envelope_results: Dict[str, Dict[str, Any]] = {}

        for spec in FAMILY_SPECS:
            body = positive_bodies[spec.name]
            body_output = track_output(
                written_outputs,
                write_json(layout, "canonical_body", spec.body_filename, body),
            )

            body_result = validate_body(
                family_name=spec.name,
                body=body,
                body_path=body_output.path,
                schema_entry=schema_validators[spec.name],
                fixture_classification="positive_fixture",
                expected_status="pass",
            )
            body_result_output = track_output(
                written_outputs,
                write_json(
                    layout,
                    "conformance",
                    f"body/positive/{spec.name}.json",
                    body_result,
                ),
            )
            body_result["result_ref"] = repo_relative(body_result_output.path)
            body_results[spec.name] = body_result

            envelope = build_envelope(
                family_name=spec.name,
                body=body,
                execution_id=execution_id,
                body_ref=repo_relative(body_output.path),
                emitted_at=utc_now(),
            )
            envelope_output = track_output(
                written_outputs,
                write_json(layout, "envelope", f"positive/{spec.name}.json", envelope),
            )

            envelope_result = validate_envelope(
                family_name=spec.name,
                envelope_object=envelope,
                body=body,
                execution_id=execution_id,
                expected_body_ref=repo_relative(body_output.path),
                envelope_path=envelope_output.path,
            )
            envelope_result_output = track_output(
                written_outputs,
                write_json(
                    layout,
                    "conformance",
                    f"envelope/positive/{spec.name}.json",
                    envelope_result,
                ),
            )
            envelope_result["result_ref"] = repo_relative(envelope_result_output.path)
            envelope_results[spec.name] = envelope_result

        negative_body = build_negative_validation_fixture(
            matter_id=matter_id,
            recorded_at=utc_now(),
        )
        negative_body_output = track_output(
            written_outputs,
            write_fixture(
                layout,
                "negative/body/invalid_validation_artifact.body.json",
                negative_body,
            ),
        )

        negative_classification = {
            "fixture_class": "conformance_failure",
            "scope": "ordinary_proof_slice",
            "artifact_family": "validation_artifact",
            "expected_surface": "canonical_body_conformance",
            "expected_status": "fail",
            "body_ref": repo_relative(negative_body_output.path),
            "note": "This fixture fails because required bounded validation basis was omitted from canonical body content.",
        }
        negative_classification_output = track_output(
            written_outputs,
            write_fixture(layout, "negative/classification.json", negative_classification),
        )

        negative_result = validate_body(
            family_name="validation_artifact",
            body=negative_body,
            body_path=negative_body_output.path,
            schema_entry=schema_validators["validation_artifact"],
            fixture_classification="conformance_failure",
            expected_status="fail",
        )
        negative_result_output = track_output(
            written_outputs,
            write_json(
                layout,
                "conformance",
                "body/negative/invalid_validation_artifact.json",
                negative_result,
            ),
        )
        negative_result["result_ref"] = repo_relative(negative_result_output.path)

        preservation_result = evaluate_preservation_conformance(
            layout=layout,
            written_outputs=written_outputs,
        )
        preservation_result_output = track_output(
            written_outputs,
            write_json(
                layout,
                "conformance",
                "preservation/run_write_outcome.json",
                preservation_result,
            ),
        )

        summary = build_run_summary(
            execution_id=execution_id,
            matter_id=matter_id,
            layout=layout,
            body_results=body_results,
            envelope_results=envelope_results,
            negative_result=negative_result,
            fixture_classification_ref=repo_relative(negative_classification_output.path),
            preservation_result_ref=repo_relative(preservation_result_output.path),
            preservation_status=preservation_result["status"],
        )
        summary_output = track_output(written_outputs, write_summary(layout, summary))

        manifest_payload = build_manifest_payload(
            layout,
            written_outputs,
            manifest_type="v1_second_proof_slice_preservation_manifest",
            extra={
                "matter_identity": matter_id,
                "continuity_emitted": False,
                "preservation_result_ref": repo_relative(preservation_result_output.path),
                "summary_ref": repo_relative(summary_output.path),
            },
        )
        track_output(written_outputs, write_manifest(layout, manifest_payload))
    except PreservationLayoutError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    positive_body_failures = [
        family_name
        for family_name, result in body_results.items()
        if result["status"] != "pass"
    ]
    positive_envelope_failures = [
        family_name
        for family_name, result in envelope_results.items()
        if result["status"] != "pass"
    ]
    unexpected_negative_status = negative_result["status"] != "fail"
    preservation_failed = preservation_result["status"] != "pass"

    print("Bounded v1 second ordinary proof slice completed.")
    print(f"Run directory: {repo_relative(layout.root_dir)}")
    print(
        "Positive body conformance: "
        f"{len(FAMILY_SPECS) - len(positive_body_failures)}/{len(FAMILY_SPECS)} passed."
    )
    print(
        "Positive envelope conformance: "
        f"{len(FAMILY_SPECS) - len(positive_envelope_failures)}/{len(FAMILY_SPECS)} passed."
    )
    print(
        "Negative fixture body conformance: "
        f"{negative_result['status']} (expected fail)."
    )
    print(f"Preservation conformance: {preservation_result['status']}.")

    if (
        positive_body_failures
        or positive_envelope_failures
        or unexpected_negative_status
        or preservation_failed
    ):
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
