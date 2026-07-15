#!/usr/bin/env python3
"""
Small local seam check for seam_experiment_001.

This script automates only the already-proven manual seam behavior for one
witness artifact. It does not implement a wider handoff system.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict


SCRIPT_PATH = Path(__file__).resolve()
EXPERIMENT_ROOT = SCRIPT_PATH.parents[1]
REPO_ROOT = SCRIPT_PATH.parents[3]

SEAM_DIR = EXPERIMENT_ROOT / "seam"
INBOUND_DIR = SEAM_DIR / "inbound"
ACCEPTED_DIR = SEAM_DIR / "accepted"
REJECTED_DIR = SEAM_DIR / "rejected"
TRANSFER_LOG_DIR = SEAM_DIR / "transfer_log"
DERIVATIVE_DIR = EXPERIMENT_ROOT / "receiver_view" / "derivative"
LOCAL_REGISTRY_DIR = EXPERIMENT_ROOT / "receiver_view" / "local_registry"

REQUIRED_NON_CLAIMS = {
    "not_semantic_source",
    "not_final_authority",
    "not_governance_force",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the bounded witness-artifact seam check for seam_experiment_001."
    )
    parser.add_argument("artifact_path", help="Path to one source witness artifact JSON.")
    return parser.parse_args()


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def load_artifact(path: Path) -> Dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Artifact must be a JSON object.")
    return payload


def check_seam_conditions(artifact: Dict[str, Any]) -> Dict[str, bool]:
    source_legible = isinstance(artifact.get("surface_ref"), str) and bool(
        artifact["surface_ref"].strip()
    )
    artifact_type_legible = isinstance(artifact.get("witness_type"), str) and bool(
        artifact["witness_type"].strip()
    )
    non_claims = artifact.get("non_claims")
    no_silent_authority_transfer = isinstance(non_claims, list) and REQUIRED_NON_CLAIMS.issubset(
        {str(item) for item in non_claims}
    )

    # The destination treatment is bounded by this script itself: derivative copy
    # only, plus a derivative receipt note and no native standing claim.
    destination_treatment_bounded = True

    return {
        "source_legible": source_legible,
        "artifact_type_legible": artifact_type_legible,
        "no_silent_authority_transfer": no_silent_authority_transfer,
        "destination_treatment_bounded": destination_treatment_bounded,
    }


def next_transfer_number() -> int:
    pattern = re.compile(r"^TRANSFER_(\d{3})_(SUCCESS|REFUSAL)\.md$")
    numbers = []
    for path in TRANSFER_LOG_DIR.glob("TRANSFER_*.md"):
        match = pattern.match(path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def routed_artifact_name(stage: str, number: int) -> str:
    return f"WITNESS_ARTIFACT_{stage}_{number:03d}.json"


def copy_artifact(source: Path, destination: Path) -> None:
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {destination}")
    shutil.copy2(source, destination)


def write_success_log(number: int, artifact_name: str, source_path: str) -> Path:
    path = TRANSFER_LOG_DIR / f"TRANSFER_{number:03d}_SUCCESS.md"
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    content = (
        f"# Transfer {number:03d} Success\n\n"
        f"- artifact name: `{artifact_name}`\n"
        f"- source path: `{source_path}`\n"
        f"- decision: accepted\n"
        f"- reason:\n"
        f"  - source legible\n"
        f"  - type legible\n"
        f"  - no silent authority transfer\n"
        f"  - destination treatment bounded\n\n"
        f"Source canon remains at source.\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def write_receipt(number: int, artifact_name: str, source_path: str) -> Path:
    path = LOCAL_REGISTRY_DIR / f"RECEIPT_{number:03d}.md"
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    content = (
        f"# Receipt {number:03d}\n\n"
        f"- received: `{artifact_name}`\n"
        f"- source path: `{source_path}`\n"
        f"- received as:\n"
        f"  - derivative artifact\n"
        f"  - not native standing\n"
        f"  - not truth by default\n"
        f"  - not authority by default\n\n"
        f"Destination receipt does not rewrite source origin.\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def write_refusal_log(number: int, artifact_name: str, source_path: str) -> Path:
    path = TRANSFER_LOG_DIR / f"TRANSFER_{number:03d}_REFUSAL.md"
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    content = (
        f"# Transfer {number:03d} Refusal\n\n"
        f"- artifact name: `{artifact_name}`\n"
        f"- source path: `{source_path}`\n"
        f"- decision: rejected\n"
        f"- refusal reason:\n"
        f"  - source legibility failed\n"
        f"  - artifact not admitted across seam\n\n"
        f"No destination receipt was created and no continuity was claimed.\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    args = parse_args()

    source_path = Path(args.artifact_path)
    if not source_path.is_absolute():
        source_path = (REPO_ROOT / source_path).resolve()

    if not source_path.exists():
        raise FileNotFoundError(f"Source artifact does not exist: {source_path}")

    transfer_number = next_transfer_number()
    source_path_label = repo_relative(source_path)
    source_artifact_name = source_path.name

    inbound_path = INBOUND_DIR / routed_artifact_name("INBOUND", transfer_number)
    copy_artifact(source_path, inbound_path)

    artifact = load_artifact(inbound_path)
    conditions = check_seam_conditions(artifact)

    if not conditions["artifact_type_legible"]:
        raise RuntimeError("Unsupported artifact: witness type is missing or unclear.")
    if not conditions["no_silent_authority_transfer"]:
        raise RuntimeError(
            "Unsupported artifact: silent authority transfer protection is unclear."
        )
    if not conditions["destination_treatment_bounded"]:
        raise RuntimeError("Unsupported destination treatment.")

    if not conditions["source_legible"]:
        rejected_name = routed_artifact_name("REJECTED", transfer_number)
        rejected_path = REJECTED_DIR / rejected_name
        copy_artifact(inbound_path, rejected_path)
        refusal_log = write_refusal_log(
            transfer_number, rejected_name, source_path_label
        )
        print(f"rejected: {repo_relative(rejected_path)}")
        print(f"log: {repo_relative(refusal_log)}")
        return 0

    accepted_path = ACCEPTED_DIR / routed_artifact_name("ACCEPTED", transfer_number)
    derivative_path = DERIVATIVE_DIR / routed_artifact_name("DERIVATIVE", transfer_number)
    copy_artifact(inbound_path, accepted_path)
    copy_artifact(inbound_path, derivative_path)

    success_log = write_success_log(
        transfer_number, source_artifact_name, source_path_label
    )
    receipt = write_receipt(
        transfer_number, source_artifact_name, source_path_label
    )

    print(f"accepted: {repo_relative(accepted_path)}")
    print(f"derivative: {repo_relative(derivative_path)}")
    print(f"log: {repo_relative(success_log)}")
    print(f"receipt: {repo_relative(receipt)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # keep failure visible and bounded
        print(f"seam check failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
