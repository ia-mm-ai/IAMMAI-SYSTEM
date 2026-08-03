"""Resolve one bounded body-held integrity-condition evaluation boundary.

The resolver validates one frozen read contract and decides only whether a
separate heterogeneous ten-condition evaluation operation may be considered.
It does not evaluate a condition, read raw signal or archive bytes, populate a
condition ledger, or select a downstream operation result.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Mapping, Sequence
from datetime import datetime
from pathlib import Path
from typing import Any


RESOLVER_MODULE = (
    "resolve_body_held_receiver_answerable_basis_"
    "integrity_condition_evaluation_boundary_v0_min"
)
RESULT_VERSION = "0.1.0"

BOUNDARY_ID = (
    "body_held_receiver_answerable_basis_"
    "integrity_condition_evaluation_boundary_001"
)
BOUNDARY_TYPE = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_"
    "INTEGRITY_CONDITION_EVALUATION_BOUNDARY"
)
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "CONSIDER_ONE_HETEROGENEOUS_BODY_HELD_EVALUATION_OF_TEN_REMAINING_"
    "RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITIONS_ONLY"
)
SELECTED_MATTER_CLASS = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_REMAINING_TEN_"
    "INTEGRITY_CONDITIONS_ONLY"
)

INTENT_RECORD = (
    "RECORD_BODY_HELD_RECEIVER_ANSWERABLE_BASIS_"
    "INTEGRITY_CONDITION_EVALUATION_BOUNDARY"
)

OUTCOME_ALLOWED = BOUNDARY_TYPE + "_ALLOWED"
OUTCOME_NOT_ALLOWED = BOUNDARY_TYPE + "_NOT_ALLOWED"
OUTCOME_BLOCKED = BOUNDARY_TYPE + "_BLOCKED"
OUTCOME_FAMILY = (OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED, OUTCOME_BLOCKED)

RESULT_ALLOWED = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_CONSIDERATION_ALLOWED"
)
RESULT_NOT_ALLOWED = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_CONSIDERATION_NOT_ALLOWED"
)
RESULT_NOT_EVALUATED = "NOT_EVALUATED"
RESULT_FAMILY = (RESULT_ALLOWED, RESULT_NOT_ALLOWED, RESULT_NOT_EVALUATED)
BOUNDARY_RESULT_FAMILY = RESULT_FAMILY

ADMISSIBILITY_PASSED = "PASSED"
ADMISSIBILITY_NOT_EVALUATED = "NOT_EVALUATED"
ADMISSIBILITY_EVALUATION_FAMILY = (
    ADMISSIBILITY_PASSED,
    ADMISSIBILITY_NOT_EVALUATED,
)

ADMISSIBLE_FUTURE_ROUTE = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_"
    "BOUNDARY_THEN_SEPARATE_HETEROGENEOUS_TEN_CONDITION_EVALUATION_"
    "OPERATION_ONLY"
)

DECISION_CODE_ALLOWED = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_ALLOWED"
)
DECISION_REASON_ALLOWED = (
    "one exact frozen body-held basis admitted for one separate heterogeneous "
    "ten-condition evaluation consideration only"
)
DECISION_CODE_NOT_ALLOWED = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_NOT_ALLOWED"
)
DECISION_REASON_NOT_ALLOWED = (
    "canonical request lawfully declined the separate heterogeneous "
    "ten-condition evaluation consideration"
)

CONDITION_EVALUATION_FAMILY = (
    "SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS",
    "REQUIRES_BASIS",
    "INDETERMINATE",
    "NOT_EVALUATED",
)
REQUIRED_BASIS_CLASS_FAMILY = (
    "CUSTODY_DISTINCT_BASIS",
    "EXTERNAL_AUTHENTICITY_BASIS",
    "OTHER_EXACT_NAMED_BASIS",
    "NONE",
)
LATER_OPERATION_RESULT_FAMILY = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_OPERATION_RECORDED",
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_OPERATION_BLOCKED",
)

REQUIRED_CONDITIONS = (
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_controlled_by_declaring_side",
    "repo_local_execution_only",
    "operator_only_attestation",
    "derivative_rendering_attestation",
    "same_custody_countersignature",
    "automatic_acknowledgement",
    "generated_affirmation",
    "forged_receiver_attestation",
    "inadmissible_receiver_basis",
)
REQUIRED_CONDITION_VALUES = {
    condition: condition == "receiver_answerable_basis_custody_distinct"
    for condition in REQUIRED_CONDITIONS
}
EVIDENCE_CLASSES = (
    "CUSTODY_AND_CONTROL",
    "EXECUTION_AND_ATTESTATION_FORM",
    "ADVERSARIAL_INTEGRITY_AND_BOUNDED_ADMISSIBILITY",
)
EVIDENCE_CLASS_CONDITION_MAPPING = {
    "CUSTODY_AND_CONTROL": REQUIRED_CONDITIONS[0:2],
    "EXECUTION_AND_ATTESTATION_FORM": REQUIRED_CONDITIONS[2:8],
    "ADVERSARIAL_INTEGRITY_AND_BOUNDED_ADMISSIBILITY": REQUIRED_CONDITIONS[8:10],
}

HISTORICAL_CONDITION_MATRIX = {
    "receiver_attested": "SATISFIED",
    "receiver_answerable_receipt_present": "SATISFIED",
    "receiver_answerable_basis_custody_distinct": "REQUIRES_BASIS",
    "receiver_answerable_basis_controlled_by_declaring_side": "REQUIRES_BASIS",
    "receiver_answerable_basis_refusable": "REQUIRES_BASIS",
    "receiver_answerable_basis_could_have_been_withheld": "REQUIRES_BASIS",
    "repo_local_execution_only": "REQUIRES_BASIS",
    "operator_only_attestation": "REQUIRES_BASIS",
    "derivative_rendering_attestation": "REQUIRES_BASIS",
    "same_custody_countersignature": "REQUIRES_BASIS",
    "automatic_acknowledgement": "REQUIRES_BASIS",
    "generated_affirmation": "REQUIRES_BASIS",
    "forged_receiver_attestation": "REQUIRES_BASIS",
    "inadmissible_receiver_basis": "REQUIRES_BASIS",
}
HISTORICAL_REQUIRES_BASIS_CONDITIONS = (
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_controlled_by_declaring_side",
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
    "repo_local_execution_only",
    "operator_only_attestation",
    "derivative_rendering_attestation",
    "same_custody_countersignature",
    "automatic_acknowledgement",
    "generated_affirmation",
    "forged_receiver_attestation",
    "inadmissible_receiver_basis",
)

DEPENDENCY_CEILING_CONTRACT = (
    {
        "condition_id": "same_custody_countersignature",
        "ceiling": "MAY_NOT_OUTRUN_RECEIVER_ANSWERABLE_BASIS_CUSTODY_DISTINCT",
    },
    {
        "condition_id": "operator_only_attestation",
        "ceiling": "MAY_NOT_OUTRUN_RECEIVER_ORIGIN_AND_CUSTODY_RELATION_SUPPORT",
    },
    {
        "condition_id": "derivative_rendering_attestation",
        "ceiling": "ABSENCE_LIMITED_TO_ADMITTED_SOURCE_BODY_CONDUCT_AND_CARRIED_LINEAGE",
    },
    {
        "condition_id": "generated_affirmation",
        "ceiling": "ABSENCE_LIMITED_TO_ADMITTED_SOURCE_BODY_CONDUCT_AND_CARRIED_LINEAGE",
    },
    {
        "condition_id": "automatic_acknowledgement",
        "ceiling": "ABSENCE_LIMITED_TO_ADMITTED_MACHINERY_AND_CHRONOLOGY",
    },
    {
        "condition_id": "forged_receiver_attestation",
        "ceiling": (
            "MAY_NOT_OUTRUN_CUSTODY_ORIGIN_PRESERVATION_CORRESPONDENCE_"
            "AND_EXTERNAL_AUTHENTICITY_BASIS"
        ),
    },
    {
        "condition_id": "inadmissible_receiver_basis",
        "ceiling": "MAY_NOT_OUTRUN_EXACT_ADMITTED_RELATION_AND_MATTER_SCOPE",
    },
    {
        "condition_id": "ALL_NEGATIVE_FORM_CONDITIONS",
        "ceiling": "MAY_NOT_BECOME_UNIVERSAL_ABSENCE",
    },
    {
        "condition_id": "ALL_SIBLING_CONDITIONS",
        "ceiling": "NO_SUCCESSFUL_SIBLING_MAY_SILENTLY_STRENGTHEN_ANOTHER",
    },
    {
        "condition_id": "ALL_DEPENDENCIES",
        "ceiling": "NO_DEPENDENCY_MAY_BE_BYPASSED",
    },
)

CONDITION_LEDGER_SCHEMA_FIELDS = (
    "condition_id",
    "required_value",
    "prior_condition_posture",
    "evidence_class",
    "permitted_artifact_references",
    "supporting_fields_or_bytes",
    "support_proposition",
    "limitation",
    "dependency_conditions",
    "dependency_ceiling",
    "candidate_evidence_considered_but_not_admitted",
    "evaluation_posture",
    "required_basis_class",
    "compact_support_boolean",
    "successor_condition_posture",
    "prior_posture_preserved",
    "no_overwrite",
)

EXCLUDED_READ_IDENTIFIERS = (
    "RAW_SIGNAL_JSON",
    "ORIGINAL_ZIP_BYTES",
    "ARCHIVE_EXTRACTION",
    "COMPLETE_BOUNDED_CAPTURE_SIGNAL_BODY",
    "COMPLETE_CANDIDATE_BODY",
    "COMPLETE_CANDIDATE_EVALUATION_MATERIAL",
    "FILESYSTEM_PERMISSIONS",
    "ACL_DATA",
    "DEVICE_CONTROL_RECORDS",
    "PRIVATE_COMMUNICATIONS",
    "BROAD_GIT_HISTORY",
    "BROAD_PR_HISTORY",
    "SIBLING_DISCOVERY",
    "LATEST_FILE_SELECTION",
    "ALTERNATIVE_SOURCE_SEARCH",
    "SOURCE_RECONSTRUCTION",
    "GLOB",
    "RGLOB",
    "DIRECTORY_SCAN",
    "UNRELATED_RECEIVER_SIDE_MATERIAL",
)

RAW_SIGNAL_POSTURE = {
    "raw_signal_body_known_to_exist": True,
    "raw_signal_body_considered": True,
    "raw_signal_body_admitted": False,
    "raw_signal_body_read_authorized": False,
    "signal_morphology_evaluation_authorized": False,
    "authenticity_upgrade_from_signal_authorized": False,
}

KNOCK_GENERATED_AT = "2026-07-15T12:08:04Z"
RECEIVER_ATTESTATION_CONFIRMED_AT = "2026-07-28T06:37:56Z"
KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL_SECONDS = 1_103_392
KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL_COMPONENTS = {
    "days": 12,
    "hours": 18,
    "minutes": 29,
    "seconds": 52,
}
KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL = (
    "12 days, 18 hours, 29 minutes, 52 seconds"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/BODY_HELD_RECEIVER_ANSWERABLE_BASIS_"
    "INTEGRITY_CONDITION_EVALUATION_BOUNDARY_V0_MIN_SPEC.md"
)
PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_presence_re_evaluation_"
    "operation_v0_min/presence_re_evaluation_operation_001__"
    "presence_re_evaluation_operation_v0_min_result.json"
)
SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_originating_modal_"
    "fact_source_admissibility_boundary_v0_min/receiver_originating_modal_"
    "fact_source_admissibility_boundary_001__receiver_originating_modal_"
    "fact_source_admissibility_boundary_v0_min_result.json"
)
LATER_MODAL_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_originating_modal_"
    "fact_evaluation_operation_v0_min/receiver_originating_modal_fact_"
    "evaluation_operation_001__receiver_originating_modal_fact_evaluation_"
    "operation_v0_min_result.json"
)
MODAL_TERMINAL_SUMMARY_RELATIVE_PATH = Path(
    "spec/RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_"
    "OPERATION_V0_MIN_TERMINAL_SUMMARY.md"
)

GOVERNING_SPECIFICATION_PATH = REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_SPECIFICATION_PATH
GOVERNING_SPEC_RELATIVE_PATH = GOVERNING_SPECIFICATION_RELATIVE_PATH
PRIOR_PRESENCE_ARTIFACT_PATH = REPO_ROOT / PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH
SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_PATH = (
    REPO_ROOT / SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH
)
LATER_MODAL_ARTIFACT_PATH = REPO_ROOT / LATER_MODAL_ARTIFACT_RELATIVE_PATH
MODAL_TERMINAL_SUMMARY_PATH = REPO_ROOT / MODAL_TERMINAL_SUMMARY_RELATIVE_PATH

GOVERNING_SPECIFICATION_SHA256 = (
    "bc485e14b5da5d72f6702550b237311f367d44b3789c01fdddc45de38bdc3600"
)
PRIOR_PRESENCE_SHA256 = (
    "fa3f05965de18382b48a37d54abeb04ed4e3d4383b8e75c11ccaa1ca07c15776"
)
SOURCE_ADMISSIBILITY_BOUNDARY_SHA256 = (
    "f24795566eb369ad935e2212aba83ef68bfd1661363cc94da2f53498cc2935ac"
)
LATER_MODAL_SHA256 = (
    "5138294e3c9d5f776676afb580b786fc1d6a5518527add7808789be3a744ba57"
)
MODAL_TERMINAL_SUMMARY_SHA256 = (
    "7ec3f880174f6941340802e2af441aff2b5b163cef4c9efc81d4cb5c887b0682"
)

CANDIDATE_RECEPTION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_reception_operation_v0_min/receiver_side_answerable_basis_"
    "reception_operation_001__receiver_side_answerable_basis_reception_"
    "operation_v0_min_result_001.json"
)
CANDIDATE_EVALUATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_evaluation_operation_v0_min_v3/receiver_side_answerable_"
    "basis_candidate_evaluation_operation_001__receiver_side_answerable_basis_"
    "candidate_evaluation_operation_v0_min_v3_result.json"
)
CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_sufficiency_operation_v0_min/receiver_side_answerable_"
    "basis_candidate_sufficiency_operation_001__receiver_side_answerable_basis_"
    "candidate_sufficiency_operation_v0_min_result_001.json"
)
ATTESTATION_BASIS_DECLARATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_declaration_v0_min/receiver_"
    "side_answerable_basis_receiver_attestation_operation_basis_declaration_"
    "001__receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_v0_min_result.json"
)
ATTESTATION_BASIS_SUPPLY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_supply_v0_min/receiver_side_"
    "answerable_basis_receiver_attestation_operation_basis_supply_001__"
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "supply_v0_min_result.json"
)
RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_v0_min/receiver_side_answerable_"
    "basis_receiver_attestation_operation_001__receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min_result_001.json"
)
RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_answerable_receipt_operation_v0_min/receiver_side_"
    "answerable_basis_receiver_answerable_receipt_operation_001__receiver_"
    "side_answerable_basis_receiver_answerable_receipt_operation_v0_min_"
    "result.json"
)

CANDIDATE_RECEPTION_SHA256 = (
    "722cd329fe85d484bf6e626f42faa034ba23c3b7e9e6196519a2c4c7e609b315"
)
CANDIDATE_EVALUATION_SHA256 = (
    "952c08a4ca383f2506fa70ca93e086668511d224ee8c9fd51eb20b44e699fd1b"
)
CANDIDATE_SUFFICIENCY_SHA256 = (
    "7271d8cb62ce75fd4c5a42e09775d481edf62dae813790d16f8361c0e06509f4"
)
ATTESTATION_BASIS_DECLARATION_SHA256 = (
    "a60e496a4a53dd1019ab429e6b80fba2d20e1e2829b575fc56de9753ea885d37"
)
ATTESTATION_BASIS_SUPPLY_SHA256 = (
    "9d877d5ce48ec6aa484e649bc54928d692eed62feefe8383169d37f462228325"
)
RECEIVER_ATTESTATION_SHA256 = (
    "175821764f0f284311c21968994473ad6157148fae360102540a9e1a237533e9"
)
RECEIVER_ANSWERABLE_RECEIPT_SHA256 = (
    "a80c4d99b3b4d33f9b267989a4696e088e10f25845b536d0b188e1554973dfcb"
)

CARRIAGE_LINEAGE_RELATIVE_PATHS = (
    CANDIDATE_RECEPTION_ARTIFACT_RELATIVE_PATH,
    CANDIDATE_EVALUATION_ARTIFACT_RELATIVE_PATH,
    CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
    ATTESTATION_BASIS_DECLARATION_ARTIFACT_RELATIVE_PATH,
    ATTESTATION_BASIS_SUPPLY_ARTIFACT_RELATIVE_PATH,
    RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH,
    RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH,
)
CARRIAGE_LINEAGE_PATHS = tuple(REPO_ROOT / path for path in CARRIAGE_LINEAGE_RELATIVE_PATHS)
CANDIDATE_RECEPTION_ARTIFACT_PATH = CARRIAGE_LINEAGE_PATHS[0]
CANDIDATE_EVALUATION_ARTIFACT_PATH = CARRIAGE_LINEAGE_PATHS[1]
CANDIDATE_SUFFICIENCY_ARTIFACT_PATH = CARRIAGE_LINEAGE_PATHS[2]
ATTESTATION_BASIS_DECLARATION_ARTIFACT_PATH = CARRIAGE_LINEAGE_PATHS[3]
ATTESTATION_BASIS_SUPPLY_ARTIFACT_PATH = CARRIAGE_LINEAGE_PATHS[4]
RECEIVER_ATTESTATION_ARTIFACT_PATH = CARRIAGE_LINEAGE_PATHS[5]
RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH = CARRIAGE_LINEAGE_PATHS[6]

PACKET_TEXT_BASE = Path(
    "artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/"
    "extracted/receiver_attestation_001"
)
PACKET_TEXT_RELATIVE_PATHS = tuple(
    PACKET_TEXT_BASE / name
    for name in (
        "receiver_working_directory.txt",
        "capture_method.txt",
        "attested_at.txt",
        "attestation_statement.txt",
        "knock_reference.txt",
        "capture_only_statement.txt",
        "freely_given_statement.txt",
        "receiver_label.txt",
    )
)
PACKET_TEXT_PATHS = tuple(REPO_ROOT / path for path in PACKET_TEXT_RELATIVE_PATHS)

PACKET_TEXT_CONTENTS = (
    (
        "receiver_working_directory=/Users/sariomaric/workspace/IAMMAI-RECEIVER\n"
        "custody_note=This directory is the receiver's own custody. It is not "
        "part of, and is not controlled by, the source body repository.\n"
    ),
    (
        "capture_signal_file=knock_20260727_215052.json\n"
        "capture_signal_sha256=2650213b028f0cae851f27cc9fc941c13836818b1392809c86eecc633940e65d\n"
        "capture_tool_path=/Users/sariomaric/workspace/apple-silicon-accelerometer/record_knock.py\n"
        "capture_tool_sha256=61679438e363adb40a6ab501b05ef5cd50a7b5c53fa10030f306ce651c4d2fa1\n"
        "capture_tool_description=macimu-based reader of the Apple SPU accelerometer, "
        "5.0 s window, full rate\n"
        "capture_gesture=two knocks of the receiver's wrist on the MacBook palm rest\n"
        "capture_recorded_at=2026-07-27T21:50:57+02:00\n"
        "capture_declared_by_receiver=true\n"
    ),
    "attested_at=2026-07-28T06:37:56Z\n",
    "knock knock back",
    (
        "knock_result_path=artifacts/integrity_host_v0_min_coexistence_presence_"
        "operation_v0_min/presence_operation_001__presence_operation_v0_min_result.json\n"
        "knock_outcome=PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION\n"
        "knock_result_sha256=7cab32728cef1bf8de9d1ec544188f155c6564832678d74b501fdccb3e4111d3\n"
        "knock_generated_at=2026-07-15T12:08:04Z\n"
        "source_body_commit=ef640316263d8c8036946d75393df624185308a1\n"
        "knock_reference_note=This receipt answers exactly one knock: the presence "
        "operation identified above, and nothing else.\n"
    ),
    (
        "capture_only_statement=This is a receiver-side attestation receipt only. "
        "It is not authority, currentness, identity, coupling, standing, output "
        "authorization, action authorization, derivative reception, or follow-on "
        "authorization. It modifies nothing in the source body. It answers one "
        "knock only: presence_operation_001.\n"
    ),
    (
        "freely_given=true\n"
        "could_have_been_refused=true\n"
        "could_have_been_withheld=true\n"
        "prescribed_by_declaring_side=false\n"
        "attestation_words_authored_by_receiver_only=true\n"
        "confirmed_by_receiver_at=2026-07-28T06:37:56Z\n"
    ),
    "receiver_label=Mario\n",
)
PACKET_TEXT_SHA256 = (
    "7a8f21827b117955d81757a07be30696c9d106b5c01fc269962b04e421913d15",
    "0f13140914ce223133e65e5479fdf12686e649a300d812cba6cee9bad21f594c",
    "fa61245579600d0fb0d7c3a0d155eef62e5ea2c6c8f9f2dd7409bd32b29916e0",
    "d56475c29e47c2b50386869bf990fa1981931f65c242d8d1b9e1161628970f43",
    "27d34f694f53a5e678e91f913da5dc04a1ade0ae0bd060a957fe98aaf1c8964c",
    "8ae105abe3b09b5d49acd7ad46231a477ba0966b33fd74a681de5e339bc1c0ac",
    "9c1aeb888cd182fdbce789e1bb191f5778712f82483d7eca1334800dac4dd3eb",
    "ab6f94b1150fda466c8730de82064d915e8cf4b1dd54e7af2a16649fbca75d38",
)
PACKET_TEXT_BYTE_COUNTS = (203, 566, 33, 16, 518, 322, 207, 21)

PRESENCE_OPERATION_SPEC_RELATIVE_PATH = Path("spec/PRESENCE_OPERATION_V0_MIN_SPEC.md")
PRESENCE_OPERATION_RESOLVER_RELATIVE_PATH = Path("src/resolve_presence_operation_v0_min.py")
PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_presence_operation_v0_min/"
    "presence_operation_001__presence_operation_v0_min_result.json"
)
RECEPTION_BOUNDARY_SPEC_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_V0_MIN_SPEC.md"
)
RECEPTION_BOUNDARY_RESOLVER_RELATIVE_PATH = Path(
    "src/resolve_receiver_side_answerable_basis_reception_boundary_v0_min.py"
)
RECEPTION_BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_"
    "reception_boundary_v0_min_v2/receiver_side_answerable_basis_reception_"
    "boundary_001__receiver_side_answerable_basis_reception_boundary_v0_min_v2_"
    "result.json"
)
RECEPTION_OPERATION_SPEC_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_V0_MIN_SPEC.md"
)
RECEPTION_OPERATION_RESOLVER_RELATIVE_PATH = Path(
    "src/resolve_receiver_side_answerable_basis_reception_operation_v0_min.py"
)
RECEPTION_OPERATION_ARTIFACT_RELATIVE_PATH = CANDIDATE_RECEPTION_ARTIFACT_RELATIVE_PATH

SOURCE_BODY_CONDUCT_RELATIVE_PATHS = (
    PRESENCE_OPERATION_SPEC_RELATIVE_PATH,
    PRESENCE_OPERATION_RESOLVER_RELATIVE_PATH,
    PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH,
    RECEPTION_BOUNDARY_SPEC_RELATIVE_PATH,
    RECEPTION_BOUNDARY_RESOLVER_RELATIVE_PATH,
    RECEPTION_BOUNDARY_ARTIFACT_RELATIVE_PATH,
    RECEPTION_OPERATION_SPEC_RELATIVE_PATH,
    RECEPTION_OPERATION_RESOLVER_RELATIVE_PATH,
    RECEPTION_OPERATION_ARTIFACT_RELATIVE_PATH,
)
SOURCE_BODY_CONDUCT_PATHS = tuple(
    REPO_ROOT / path for path in SOURCE_BODY_CONDUCT_RELATIVE_PATHS
)
SOURCE_BODY_CONDUCT_SHA256 = (
    "58f75c47294d90dab10a2b6388dfd142f71181e1a1101bedf91c4fe3c1895ad6",
    "c8e8414938e806359c0256e1cd6b425fda0d3b3621b4bcf6c3deb20406cb876a",
    "7cab32728cef1bf8de9d1ec544188f155c6564832678d74b501fdccb3e4111d3",
    "fbb1fde665ac7f85d3224c3d2538a0b8586f61feb988ab87a9230708a1e890d5",
    "f4bf39090ad24afb33d366764eac2f03dd38a54dc0a9ce6a1a34b9d753779446",
    "3ac18bec045113cc58b02b0140cb2db3e550851fb0dd7c42463603517bbf5120",
    "7da57e73084210037f7ed86f7b8094c126549187dc43d89455bc5ddefd161444",
    "b7ff6c9b44083b97b801373ab0e0abd279069de2d725942cda1f372edae0d596",
    CANDIDATE_RECEPTION_SHA256,
)

CANONICAL_OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_body_held_receiver_answerable_"
    "basis_integrity_condition_evaluation_boundary_v0_min"
)
OUTPUT_ROOT = CANONICAL_OUTPUT_ROOT
OUTPUT_FILENAME = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "boundary_001__body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_boundary_v0_min_result.json"
)
DETERMINISTIC_FILENAME = OUTPUT_FILENAME

REQUIRED_FALSE_NON_CLAIMS = (
    "all_ten_conditions_established_as_reality_wide_facts",
    "custody_created",
    "custody_proven",
    "receiver_identity_established",
    "receiver_freedom_established",
    "provenance_created",
    "provenance_proven",
    "physical_validity_created",
    "physical_validity_proven",
    "receiver_attestation_non_forgery_established",
    "universal_automation_absence_established",
    "universal_generated_affirmation_absence_established",
    "universal_derivative_rendering_absence_established",
    "universal_same_custody_countersignature_absence_established",
    "global_receiver_basis_admissibility_established",
    "complete_receiver_answerable_basis_established",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "truth_created",
    "standing_created",
    "authority_created",
    "identity_created",
    "relation_created",
    "coupling_created",
    "field_machinery_created",
    "threshold_machinery_created",
    "truth_settlement_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "repeated_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_boundary_permission_created",
    "reusable_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_route_created",
    "same_body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "boundary_rerun_authorized",
    "automatic_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_boundary_retry_created",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "boundary_debt_created",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "boundary_obligation_created",
    "scheduled_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_created",
    "automatic_next_step_created",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "raw_signal_body_admitted",
    "raw_signal_body_read_authorized",
    "signal_morphology_evaluation_authorized",
    "authenticity_upgrade_from_signal_authorized",
    "condition_ledger_populated",
    "any_condition_evaluated",
    "later_operation_created",
    "later_operation_executed",
    "later_operation_result_selected",
    "prior_artifact_overwritten",
    "prior_condition_posture_overwritten",
    "source_naturalized",
    "jurisdiction_collapsed",
)

OMISSION_POSTURE_FIELDS = (
    "complete_upstream_artifact_bodies_omitted",
    "complete_candidate_body_omitted",
    "complete_candidate_evaluation_material_omitted",
    "raw_accelerometer_body_omitted",
    "original_zip_bytes_omitted",
    "archive_bytes_omitted",
    "filesystem_permissions_omitted",
    "acl_data_omitted",
    "device_control_data_omitted",
    "private_communications_omitted",
    "unrelated_receiver_side_material_omitted",
    "alternative_candidates_omitted",
    "alternative_declarations_omitted",
    "broad_git_history_omitted",
    "broad_pr_history_omitted",
    "excluded_evidence_bodies_omitted",
    "complete_material_omission_posture",
)

LINEAGE_PRESERVATION_FIELDS = (
    "prior_presence_result_preserved",
    "prior_twelve_condition_matrix_preserved",
    "later_two_source_supported_modal_evaluations_preserved",
    "both_modal_establishment_fields_remain_false",
    "ten_current_target_conditions_remain_unevaluated_in_later_modal_line",
    "source_admissibility_boundary_preserved",
    "receiver_originating_source_relation_preserved",
    "carried_arrival_remains_non_native",
    "source_not_naturalized",
    "jurisdiction_not_collapsed",
    "candidate_attestation_and_receipt_lineage_preserved",
    "no_prior_artifact_repaired_invalidated_superseded_normalized_replaced_or_overwritten",
    "contaminated_lineage_unchanged",
)

NON_MEANING_FIELDS = (
    "prior_requires_basis_standing_is_not_failure",
    "later_support_is_not_retroactive_overwrite",
    "boundary_is_not_operation",
    "record_existence_is_not_record_basis_admissibility",
    "record_basis_admissibility_is_not_evaluation",
    "evaluation_is_not_reality_wide_establishment",
    "custody_relation_is_not_custody_proof",
    "declared_provenance_is_not_proven_provenance",
    "receiver_label_is_not_receiver_identity",
    "admitted_record_relative_absence_is_not_universal_absence",
    "internal_consistency_is_not_non_forgery",
    "hashes_prove_preservation_not_authorship",
    "source_body_non_prescription_is_not_no_external_pressure",
    "source_body_non_generation_is_not_no_external_generation",
    "bounded_admissibility_is_not_global_admissibility",
    "supported_sibling_does_not_strengthen_another_condition_automatically",
    "dependency_ceiling_is_not_condition_denial",
    "considered_evidence_is_not_admitted_evidence",
    "raw_signal_existence_is_not_read_permission",
    "operation_recording_is_not_complete_receiver_answerable_basis",
    "complete_receiver_answerable_basis_is_not_presence",
    "boundary_exhaustion_is_not_standing",
    "open_does_not_mean_next",
)

BLOCKED_CONVERSIONS = (
    "PRIOR_REQUIRES_BASIS_TO_SUCCESSOR_CONDITION_RESULT",
    "LATER_TWO_CONDITION_SUPPORT_TO_SIBLING_CONDITION_SATISFACTION",
    "BODY_HELD_RECORD_EXISTENCE_TO_RECORD_BASIS_ADMISSIBILITY",
    "RECORD_BASIS_ADMISSIBILITY_TO_EVALUATION",
    "DECLARED_CUSTODY_TO_CUSTODY_PROOF_OR_RECEIVER_IDENTITY",
    "DECLARED_PROVENANCE_TO_PROVEN_PROVENANCE",
    "INTERNAL_CORRESPONDENCE_OR_HASH_TO_AUTHORSHIP_OR_NON_FORGERY",
    "ADMITTED_RECORD_RELATIVE_ABSENCE_TO_UNIVERSAL_ABSENCE",
    "BOUNDED_MATTER_ADMISSIBILITY_TO_GLOBAL_RECEIVER_BASIS_ADMISSIBILITY",
    "RAW_SIGNAL_EXISTENCE_TO_READ_MORPHOLOGY_OR_AUTHENTICITY_UPGRADE",
    "ONE_CONDITION_SUPPORT_TO_STRONGER_SIBLING_POSTURE",
    "BOUNDARY_RESULT_TO_OPERATION_COMPLETE_BASIS_PRESENCE_TRUTH_OR_AUTHORITY",
    "OPERATION_RECORDING_TO_COMPLETE_RECEIVER_ANSWERABLE_BASIS_OR_PRESENCE",
    "BOUNDARY_RESULT_TO_REPEAT_RETRY_DEBT_OBLIGATION_SCHEDULE_OR_AUTOMATIC_NEXT",
    "BOUNDARY_RESULT_TO_REPAIR_SCAN_DISCOVERY_VALIDATION_OR_RECONSTRUCTION",
)

WHAT_REMAINS_OPEN = (
    "boundary_tests",
    "boundary_request",
    "boundary_live_result",
    "boundary_terminal_summary",
    "separate_heterogeneous_ten_condition_operation_specification",
    "separate_heterogeneous_ten_condition_operation_resolver",
    "separate_heterogeneous_ten_condition_operation_tests",
    "separate_heterogeneous_ten_condition_operation_request",
    "separate_heterogeneous_ten_condition_operation_live_result",
    "separate_heterogeneous_ten_condition_operation_terminal_summary",
    "all_ten_actual_condition_evaluations",
    "external_authenticity_basis",
    "cryptographic_receiver_identity",
    "raw_signal_morphology_under_separate_admitting_surface",
    "complete_receiver_answerable_basis",
    "later_presence_re_evaluation",
    "presence_support_authorization_establishment_and_recording",
    "threshold_and_truth_settlement",
    "identity_custody_proof_provenance_proof_and_physical_validity",
    "authority_truth_standing_relation_and_coupling",
    "field_machinery_runtime_api_public_interface_and_public_intake",
    "output_action_derivative_reception_and_synchronization",
    "repair_validation_and_follow_on_work",
)

SPEC_REQUIRED_MARKERS = (
    ("title", "# Body-Held Receiver-Answerable-Basis Integrity-Condition Evaluation Boundary V0 Minimum Specification"),
    ("boundary_id", f"`body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_id = {BOUNDARY_ID}`"),
    ("boundary_type", f"`body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_type = {BOUNDARY_TYPE}`"),
    ("boundary_scope", f"`body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_scope = {BOUNDARY_SCOPE}`"),
    ("matter_class", f"`selected_matter_class = {SELECTED_MATTER_CLASS}`"),
    ("prior_digest", PRIOR_PRESENCE_SHA256),
    ("source_boundary_digest", SOURCE_ADMISSIBILITY_BOUNDARY_SHA256),
    ("later_modal_digest", LATER_MODAL_SHA256),
    ("condition_supported", "`SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS`"),
    ("condition_requires_basis", "`REQUIRES_BASIS`"),
    ("condition_indeterminate", "`INDETERMINATE`"),
    ("condition_not_evaluated", "`NOT_EVALUATED`"),
    ("basis_custody", "`CUSTODY_DISTINCT_BASIS`"),
    ("basis_external", "`EXTERNAL_AUTHENTICITY_BASIS`"),
    ("basis_other", "`OTHER_EXACT_NAMED_BASIS`"),
    ("basis_none", "`NONE`"),
    ("allowed", f"`{OUTCOME_ALLOWED}`"),
    ("not_allowed", f"`{OUTCOME_NOT_ALLOWED}`"),
    ("blocked", f"`{OUTCOME_BLOCKED}`"),
    ("future_route", f"`{ADMISSIBLE_FUTURE_ROUTE}`"),
    ("raw_known", "`raw_signal_body_known_to_exist = true`"),
    ("raw_admitted", "`raw_signal_body_admitted = false`"),
    ("interval", KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL),
    ("nonclaims", "## 18. Required False Non-Claims"),
    ("blocked_conversions", "## 19. Blocked Conversions"),
    ("closing_lock", "## 21. Closing Lock"),
)
SPEC_MARKERS = tuple(marker for _, marker in SPEC_REQUIRED_MARKERS)

PROHIBITED_DIRECT_REQUEST_FIELDS = frozenset(
    {
        *REQUIRED_CONDITIONS,
        "condition_evaluations",
        "condition_results",
        "condition_ledger",
        "operation_result",
        "later_operation_result",
        "successor_condition_posture",
        "compact_support_boolean",
        "semantic_payload",
        "raw_signal_body",
        "archive_bytes",
        "complete_candidate_body",
        "complete_upstream_artifact",
        "custody_proof",
        "receiver_identity",
        "provenance_proof",
        "non_forgery_result",
        "universal_absence",
        "global_admissibility",
        "complete_receiver_answerable_basis",
        "truth",
        "standing",
        "authority",
        "presence",
        "glob",
        "rglob",
        "scan",
        "discovery",
        "repair",
        "replacement",
        "normalization",
        "source_reconstruction",
        "latest_file_selection",
    }
)

BLOCK_CODES = frozenset(
    {
        "NOT_EXECUTED",
        "REQUEST_NOT_MAPPING",
        "REQUEST_JSON_INVALID",
        "REQUEST_FIELD_MISSING",
        "REQUEST_UNKNOWN_FIELD",
        "REQUEST_VALUE_MISMATCH",
        "REQUEST_BOOLEAN_REQUIRED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "RESULT_POSTURE_PRECLAIMED",
        "SPECIFICATION_MISSING_OR_UNREADABLE",
        "SPECIFICATION_DIGEST_MISMATCH",
        "SPECIFICATION_INVALID",
        "PRIOR_PRESENCE_ARTIFACT_MISSING_OR_UNREADABLE",
        "PRIOR_PRESENCE_ARTIFACT_DIGEST_MISMATCH",
        "PRIOR_PRESENCE_ARTIFACT_INVALID",
        "SOURCE_ADMISSIBILITY_ARTIFACT_MISSING_OR_UNREADABLE",
        "SOURCE_ADMISSIBILITY_ARTIFACT_DIGEST_MISMATCH",
        "SOURCE_ADMISSIBILITY_ARTIFACT_INVALID",
        "LATER_MODAL_ARTIFACT_MISSING_OR_UNREADABLE",
        "LATER_MODAL_ARTIFACT_DIGEST_MISMATCH",
        "LATER_MODAL_ARTIFACT_INVALID",
        "MODAL_TERMINAL_SUMMARY_MISSING_OR_UNREADABLE",
        "MODAL_TERMINAL_SUMMARY_DIGEST_MISMATCH",
        "MODAL_TERMINAL_SUMMARY_INVALID",
        "CARRIAGE_LINEAGE_ARTIFACT_MISSING_OR_UNREADABLE",
        "CARRIAGE_LINEAGE_ARTIFACT_DIGEST_MISMATCH",
        "CARRIAGE_LINEAGE_ARTIFACT_INVALID",
        "PACKET_TEXT_MISSING_OR_UNREADABLE",
        "PACKET_TEXT_DIGEST_MISMATCH",
        "PACKET_TEXT_INVALID",
        "SOURCE_BODY_CONDUCT_SURFACE_MISSING_OR_UNREADABLE",
        "SOURCE_BODY_CONDUCT_SURFACE_DIGEST_MISMATCH",
        "SOURCE_BODY_CONDUCT_SURFACE_INVALID",
        "READ_CONTRACT_INVALID",
        "MATTER_CONTRACT_INVALID",
        "DEPENDENCY_CEILING_INVALID",
        "RAW_SIGNAL_POSTURE_INVALID",
        "TEMPORAL_EVIDENCE_INVALID",
        "CONDITION_LEDGER_SCHEMA_INVALID",
        "ADMISSIBILITY_BLOCKED",
    }
)

BOUNDARY_KEY = "body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary"
CHECKS_KEY = BOUNDARY_KEY + "_checks"
SUMMARY_KEY = BOUNDARY_KEY + "_summary"
STATEMENT_KEY = BOUNDARY_KEY + "_statement"
NON_MEANING_KEY = BOUNDARY_KEY + "_non_meaning"
METADATA_KEY = BOUNDARY_KEY + "_metadata"
DECLARED_REQUEST_KEY = "declared_" + BOUNDARY_KEY + "_request"


class BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationBoundaryV0MinError(
    Exception
):
    """Raised when canonical result serialization is refused."""


class _DuplicateJsonKeyError(ValueError):
    pass


class _NonFiniteJsonNumberError(ValueError):
    pass


def _reject_duplicate_json_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def _reject_non_finite_json_number(value: str) -> Any:
    raise _NonFiniteJsonNumberError(value)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _as_repo_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_bytes(value: Path | str) -> tuple[bytes | None, str | None]:
    try:
        path = _as_repo_path(value)
        if not path.is_file():
            return None, "path is not a regular file"
        return path.read_bytes(), None
    except (OSError, RuntimeError, TypeError, ValueError) as exc:
        return None, type(exc).__name__


def _parse_json_bytes(payload: bytes) -> tuple[Any | None, str | None]:
    try:
        text = payload.decode("utf-8", errors="strict")
        value = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_json_keys,
            parse_constant=_reject_non_finite_json_number,
        )
        return value, None
    except (
        UnicodeDecodeError,
        json.JSONDecodeError,
        _DuplicateJsonKeyError,
        _NonFiniteJsonNumberError,
        RecursionError,
        TypeError,
        ValueError,
    ) as exc:
        return None, type(exc).__name__


def _read_json(value: Path | str) -> tuple[Any | None, bytes | None, str | None]:
    payload, error = _read_bytes(value)
    if error is not None or payload is None:
        return None, payload, error
    parsed, error = _parse_json_bytes(payload)
    return parsed, payload, error


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_omission_posture() -> dict[str, bool]:
    return {field: True for field in OMISSION_POSTURE_FIELDS}


def _canonical_lineage_posture() -> dict[str, bool]:
    return {field: True for field in LINEAGE_PRESERVATION_FIELDS}


def _canonical_non_meaning() -> dict[str, bool]:
    return {field: True for field in NON_MEANING_FIELDS}


def _exact_equal(actual: Any, expected: Any) -> bool:
    if type(expected) is bool:
        return type(actual) is bool and actual is expected
    if type(expected) is int:
        return type(actual) is int and actual == expected
    if isinstance(expected, Mapping):
        return (
            isinstance(actual, Mapping)
            and set(actual) == set(expected)
            and all(_exact_equal(actual[key], expected[key]) for key in expected)
        )
    if isinstance(expected, (tuple, list)):
        return (
            isinstance(actual, Sequence)
            and not isinstance(actual, (str, bytes, bytearray))
            and len(actual) == len(expected)
            and all(_exact_equal(a, e) for a, e in zip(actual, expected))
        )
    return type(actual) is type(expected) and actual == expected


def _canonical_false_mapping(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(type(value[field]) is bool and value[field] is False for field in value)
    )


def _check(
    check_id: str,
    passed: bool,
    *,
    code: str | None = None,
    expected: Any = None,
) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "passed": bool(passed),
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
        "expected": expected,
    }


def _add_check(
    checks: list[dict[str, Any]],
    check_id: str,
    passed: bool,
    code: str,
    *,
    expected: Any = None,
) -> bool:
    checks.append(_check(check_id, passed, code=code, expected=expected))
    return passed


def _first_failed_check(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for item in checks:
        if item.get("passed") is False:
            code = item.get("block_code")
            return str(code) if code in BLOCK_CODES else "ADMISSIBILITY_BLOCKED"
    return None


def _identity_request_values() -> dict[str, Any]:
    return {
        "intent": INTENT_RECORD,
        BOUNDARY_KEY + "_id": BOUNDARY_ID,
        BOUNDARY_KEY + "_type": BOUNDARY_TYPE,
        BOUNDARY_KEY + "_version": BOUNDARY_VERSION,
        BOUNDARY_KEY + "_scope": BOUNDARY_SCOPE,
        (
            "governing_body_held_receiver_answerable_basis_integrity_condition_"
            "evaluation_boundary_specification_path"
        ): str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "prior_presence_re_evaluation_operation_artifact_path": str(
            PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH
        ),
        "source_admissibility_boundary_artifact_path": str(
            SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_originating_modal_fact_evaluation_operation_artifact_path": str(
            LATER_MODAL_ARTIFACT_RELATIVE_PATH
        ),
        "receiver_originating_modal_fact_evaluation_terminal_summary_path": str(
            MODAL_TERMINAL_SUMMARY_RELATIVE_PATH
        ),
        "carriage_lineage_artifact_paths": [
            str(path) for path in CARRIAGE_LINEAGE_RELATIVE_PATHS
        ],
        "receiver_packet_text_paths": [
            str(path) for path in PACKET_TEXT_RELATIVE_PATHS
        ],
        "source_body_conduct_paths": [
            str(path) for path in SOURCE_BODY_CONDUCT_RELATIVE_PATHS
        ],
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "ordered_ten_condition_matter": list(REQUIRED_CONDITIONS),
        "required_condition_values": copy.deepcopy(REQUIRED_CONDITION_VALUES),
        "evidence_class_family": list(EVIDENCE_CLASSES),
        "evidence_class_condition_mapping": {
            key: list(value) for key, value in EVIDENCE_CLASS_CONDITION_MAPPING.items()
        },
        "condition_evaluation_family": list(CONDITION_EVALUATION_FAMILY),
        "required_basis_class_family": list(REQUIRED_BASIS_CLASS_FAMILY),
        "later_operation_result_family": list(LATER_OPERATION_RESULT_FAMILY),
        "dependency_ceiling_contract": copy.deepcopy(list(DEPENDENCY_CEILING_CONTRACT)),
        "condition_ledger_schema_fields": list(CONDITION_LEDGER_SCHEMA_FIELDS),
        "excluded_read_contract": list(EXCLUDED_READ_IDENTIFIERS),
        "raw_signal_considered_but_not_admitted_posture": copy.deepcopy(
            RAW_SIGNAL_POSTURE
        ),
        "temporal_evidence": {
            "knock_generated_at": KNOCK_GENERATED_AT,
            "receiver_attestation_confirmed_at": RECEIVER_ATTESTATION_CONFIRMED_AT,
            "knock_to_receiver_attestation_interval_seconds": (
                KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL_SECONDS
            ),
            "knock_to_receiver_attestation_interval_components": copy.deepcopy(
                KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL_COMPONENTS
            ),
            "knock_to_receiver_attestation_interval": (
                KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL
            ),
        },
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }


def _new_canonical_request(selected: bool = True) -> dict[str, Any]:
    return {
        **_identity_request_values(),
        (
            "body_held_receiver_answerable_basis_integrity_condition_"
            "evaluation_consideration_selected"
        ): selected,
        "declared_non_claims": _canonical_non_claims(),
    }


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_request(
) -> dict[str, Any]:
    """Return one fresh canonical selected boundary request."""
    return copy.deepcopy(_new_canonical_request())


def build_declared_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Return a canonical request while keeping explicit overrides visible."""
    request = _new_canonical_request()
    request.update(copy.deepcopy(overrides))
    return request


def _canonical_request_keys() -> set[str]:
    return {
        *_identity_request_values(),
        (
            "body_held_receiver_answerable_basis_integrity_condition_"
            "evaluation_consideration_selected"
        ),
        "declared_non_claims",
    }


def _validate_request(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None]:
    direct = set(request).intersection(PROHIBITED_DIRECT_REQUEST_FIELDS)
    if direct:
        _add_check(
            checks,
            "request.result_or_semantic_preclaim_absent",
            False,
            "RESULT_POSTURE_PRECLAIMED",
        )
        return "RESULT_POSTURE_PRECLAIMED", "request contains a prohibited preclaim"
    canonical = _canonical_request_keys()
    if canonical.difference(request):
        _add_check(checks, "request.schema", False, "REQUEST_FIELD_MISSING")
        return "REQUEST_FIELD_MISSING", "canonical request fields are missing"
    if set(request).difference(canonical):
        _add_check(checks, "request.schema", False, "REQUEST_UNKNOWN_FIELD")
        return "REQUEST_UNKNOWN_FIELD", "request contains unknown fields"
    _add_check(checks, "request.schema", True, "REQUEST_VALUE_MISMATCH")
    for field, expected in _identity_request_values().items():
        if not _add_check(
            checks,
            "request." + field,
            _exact_equal(request.get(field), expected),
            "REQUEST_VALUE_MISMATCH",
            expected=expected,
        ):
            return "REQUEST_VALUE_MISMATCH", field + " is not canonical"
    selected_field = (
        "body_held_receiver_answerable_basis_integrity_condition_"
        "evaluation_consideration_selected"
    )
    if not _add_check(
        checks,
        "request." + selected_field,
        type(request.get(selected_field)) is bool,
        "REQUEST_BOOLEAN_REQUIRED",
        expected="boolean",
    ):
        return "REQUEST_BOOLEAN_REQUIRED", "consideration selection must be Boolean"
    if not _add_check(
        checks,
        "request.declared_non_claims",
        _canonical_false_mapping(request.get("declared_non_claims")),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    ):
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared non-claims must be the exact canonical false mapping",
        )
    _add_check(
        checks,
        "request.result_or_semantic_preclaim_absent",
        True,
        "RESULT_POSTURE_PRECLAIMED",
    )
    return None, None


def _empty_specification_validation() -> dict[str, Any]:
    return {
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "expected_sha256": GOVERNING_SPECIFICATION_SHA256,
        "observed_sha256": None,
        "strict_utf8_validated": False,
        "marker_validation": {name: False for name, _ in SPEC_REQUIRED_MARKERS},
        "specification_validated": False,
    }


def _validate_specification(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_specification_validation()
    payload, error = _read_bytes(path)
    if error is not None or payload is None:
        _add_check(
            checks,
            "specification.readable",
            False,
            "SPECIFICATION_MISSING_OR_UNREADABLE",
        )
        return (
            "SPECIFICATION_MISSING_OR_UNREADABLE",
            "governing specification is missing or unreadable",
            validation,
        )
    observed = _sha256(payload)
    validation["observed_sha256"] = observed
    if not _add_check(
        checks,
        "specification.sha256",
        observed == GOVERNING_SPECIFICATION_SHA256,
        "SPECIFICATION_DIGEST_MISMATCH",
        expected=GOVERNING_SPECIFICATION_SHA256,
    ):
        return (
            "SPECIFICATION_DIGEST_MISMATCH",
            "governing specification digest mismatch",
            validation,
        )
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        _add_check(checks, "specification.utf8", False, "SPECIFICATION_INVALID")
        return "SPECIFICATION_INVALID", "specification is not strict UTF-8", validation
    validation["strict_utf8_validated"] = True
    markers = {name: marker in text for name, marker in SPEC_REQUIRED_MARKERS}
    validation["marker_validation"] = markers
    for name, present in markers.items():
        if not _add_check(
            checks,
            "specification.marker." + name,
            present,
            "SPECIFICATION_INVALID",
        ):
            return "SPECIFICATION_INVALID", "specification marker missing", validation
    validation["specification_validated"] = True
    return None, None, validation


def _empty_artifact_validation(relative_path: Path, digest: str) -> dict[str, Any]:
    return {
        "artifact_path": str(relative_path),
        "expected_sha256": digest,
        "observed_sha256": None,
        "strict_json_validated": False,
        "identity_validated": False,
        "result_validated": False,
        "completion_and_cardinality_validated": False,
        "false_locks_validated": False,
        "artifact_validated": False,
        "standing": {},
    }


def _load_pinned_json(
    *,
    path: Path | str,
    relative_path: Path,
    digest: str,
    prefix: str,
    code_prefix: str,
    checks: list[dict[str, Any]],
) -> tuple[Mapping[str, Any] | None, dict[str, Any], str | None, str | None]:
    validation = _empty_artifact_validation(relative_path, digest)
    value, payload, error = _read_json(path)
    missing_code = code_prefix + "_MISSING_OR_UNREADABLE"
    digest_code = code_prefix + "_DIGEST_MISMATCH"
    invalid_code = code_prefix + "_INVALID"
    if payload is None:
        _add_check(checks, prefix + ".readable_json", False, missing_code)
        return None, validation, missing_code, prefix + " is missing or unreadable"
    if error is not None:
        _add_check(checks, prefix + ".strict_json_mapping", False, invalid_code)
        return None, validation, invalid_code, prefix + " contains invalid JSON"
    observed = _sha256(payload)
    validation["observed_sha256"] = observed
    if not _add_check(
        checks,
        prefix + ".sha256",
        observed == digest,
        digest_code,
        expected=digest,
    ):
        return None, validation, digest_code, prefix + " digest mismatch"
    if not _add_check(
        checks,
        prefix + ".strict_json_mapping",
        isinstance(value, Mapping),
        invalid_code,
    ):
        return None, validation, invalid_code, prefix + " is not a JSON object"
    validation["strict_json_validated"] = True
    return value, validation, None, None


def _get_path(value: Any, path: tuple[str, ...]) -> Any:
    current = value
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return None
        current = current[key]
    return current


def _block_is_clear(value: Mapping[str, Any]) -> bool:
    block = value.get("block")
    return isinstance(block, Mapping) and block.get("blocked") is False


def _validate_prior_presence(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    value, validation, code, reason = _load_pinned_json(
        path=path,
        relative_path=PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH,
        digest=PRIOR_PRESENCE_SHA256,
        prefix="prior_presence",
        code_prefix="PRIOR_PRESENCE_ARTIFACT",
        checks=checks,
    )
    if code is not None or value is None:
        return code, reason, validation
    identity = _exact_equal(
        value.get("resolver_module"),
        "resolve_presence_re_evaluation_operation_v0_min",
    ) and _exact_equal(value.get("result_version"), "0.1.0")
    result_valid = (
        _exact_equal(
            value.get("outcome"),
            "PRESENCE_RE_EVALUATION_OPERATION_REQUIRES_RECEIVER_ANSWERABLE_BASIS",
        )
        and _exact_equal(
            value.get("presence_re_evaluation_operation_result"),
            "REQUIRES_RECEIVER_ANSWERABLE_BASIS",
        )
        and _exact_equal(
            value.get("successor_presence_result"),
            "REQUIRES_RECEIVER_ANSWERABLE_BASIS",
        )
        and _exact_equal(value.get("failed_check_count"), 0)
        and _exact_equal(value.get("passed_check_count"), 409)
        and _block_is_clear(value)
    )
    posture = value.get("operation_posture")
    completion = isinstance(posture, Mapping) and all(
        _exact_equal(posture.get(field), expected)
        for field, expected in {
            "operation_basis_admitted": True,
            "presence_re_evaluation_performed": True,
            "presence_re_evaluation_operation_exhausted": True,
            "completed_successor_result_posture_count": 1,
        }.items()
    ) and value.get("admissible_future_route") is None
    evaluations = value.get("condition_evaluations")
    matrix = (
        isinstance(evaluations, Mapping)
        and set(evaluations) == set(HISTORICAL_CONDITION_MATRIX)
        and all(
            isinstance(evaluations.get(condition), Mapping)
            and _exact_equal(evaluations[condition].get("evaluation"), expected)
            for condition, expected in HISTORICAL_CONDITION_MATRIX.items()
        )
    )
    operation = value.get("presence_re_evaluation_operation")
    false_locks = isinstance(operation, Mapping) and all(
        operation.get(field) is False
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        )
    )
    requirements = (
        ("identity", identity),
        ("result", result_valid),
        ("completion", completion),
        ("historical_condition_matrix", matrix),
        ("presence_false_locks", false_locks),
    )
    for name, valid in requirements:
        if not _add_check(
            checks,
            "prior_presence." + name,
            valid,
            "PRIOR_PRESENCE_ARTIFACT_INVALID",
        ):
            return (
                "PRIOR_PRESENCE_ARTIFACT_INVALID",
                "prior presence standing is invalid",
                validation,
            )
    validation.update(
        {
            "identity_validated": True,
            "result_validated": True,
            "completion_and_cardinality_validated": True,
            "false_locks_validated": True,
            "artifact_validated": True,
            "standing": {
                "outcome": value.get("outcome"),
                "operation_result": value.get("presence_re_evaluation_operation_result"),
                "successor_presence_result": value.get("successor_presence_result"),
                "passed_check_count": 409,
                "historical_condition_matrix": copy.deepcopy(HISTORICAL_CONDITION_MATRIX),
                "historical_requires_basis_conditions": list(
                    HISTORICAL_REQUIRES_BASIS_CONDITIONS
                ),
                "presence_supported": False,
                "presence_authorized": False,
                "presence_established": False,
                "presence_recorded": False,
                "admissible_future_route": None,
            },
        }
    )
    return None, None, validation


def _validate_source_admissibility(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    value, validation, code, reason = _load_pinned_json(
        path=path,
        relative_path=SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH,
        digest=SOURCE_ADMISSIBILITY_BOUNDARY_SHA256,
        prefix="source_admissibility",
        code_prefix="SOURCE_ADMISSIBILITY_ARTIFACT",
        checks=checks,
    )
    if code is not None or value is None:
        return code, reason, validation
    boundary = value.get("receiver_originating_modal_fact_source_admissibility_boundary")
    evaluations = value.get("admissibility_evaluations")
    lineage = value.get("lineage_preservation_posture")
    identity = _exact_equal(
        value.get("resolver_module"),
        "resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min",
    ) and _exact_equal(value.get("result_version"), "0.1.0")
    result_valid = (
        _exact_equal(
            value.get("outcome"),
            "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_ALLOWED",
        )
        and _exact_equal(
            value.get("boundary_result"),
            "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_CONSIDERATION_ALLOWED",
        )
        and _exact_equal(value.get("failed_check_count"), 0)
        and _exact_equal(value.get("passed_check_count"), 308)
        and _block_is_clear(value)
    )
    completion = isinstance(boundary, Mapping) and all(
        _exact_equal(boundary.get(field), expected)
        for field, expected in {
            "source_selection_recorded": True,
            "receiver_originating_modal_fact_source_admissibility_boundary_recorded": True,
            "receiver_originating_modal_fact_source_admissibility_boundary_result_recorded": True,
            "receiver_originating_modal_fact_source_admissibility_boundary_exhausted": True,
            "completed_consideration_posture_count": 1,
        }.items()
    )
    source = isinstance(boundary, Mapping) and all(
        _exact_equal(boundary.get(field), expected)
        for field, expected in {
            "selected_source_origin": "RECEIVER_ORIGINATING",
            "selected_source_arrival_posture": "CARRIED_ARRIVAL",
            "selected_source_native_standing": False,
            "jurisdiction_distinction_preserved": True,
        }.items()
    ) and isinstance(lineage, Mapping) and all(
        lineage.get(field) is True
        for field in (
            "selected_source_remains_receiver_originating",
            "source_relation_remains_legible",
            "carried_arrival_remains_non_native",
            "source_not_naturalized",
            "jurisdiction_not_collapsed",
        )
    )
    three = (
        isinstance(evaluations, Mapping)
        and set(evaluations)
        == {
            "source_admissibility_evaluation",
            "scope_and_matter_admissibility_evaluation",
            "transition_admissibility_evaluation",
        }
        and all(item == "PASSED" for item in evaluations.values())
    )
    future = value.get("admissible_future_route") == (
        "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_THEN_"
        "SEPARATE_RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_ONLY"
    )
    for name, valid in (
        ("identity", identity),
        ("result", result_valid),
        ("completion", completion),
        ("source_posture", source),
        ("three_part_admissibility", three),
        ("future_route", future),
    ):
        if not _add_check(
            checks,
            "source_admissibility." + name,
            valid,
            "SOURCE_ADMISSIBILITY_ARTIFACT_INVALID",
        ):
            return (
                "SOURCE_ADMISSIBILITY_ARTIFACT_INVALID",
                "source-admissibility standing is invalid",
                validation,
            )
    validation.update(
        {
            "identity_validated": True,
            "result_validated": True,
            "completion_and_cardinality_validated": True,
            "false_locks_validated": True,
            "artifact_validated": True,
            "standing": {
                "outcome": value.get("outcome"),
                "boundary_result": value.get("boundary_result"),
                "passed_check_count": 308,
                "source_selection_recorded": True,
                "receiver_origin_preserved": True,
                "carried_arrival": True,
                "selected_source_native_standing": False,
                "jurisdiction_distinction_preserved": True,
                "source_not_naturalized": True,
                "admissible_future_route": value.get("admissible_future_route"),
            },
        }
    )
    return None, None, validation


def _validate_later_modal(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    value, validation, code, reason = _load_pinned_json(
        path=path,
        relative_path=LATER_MODAL_ARTIFACT_RELATIVE_PATH,
        digest=LATER_MODAL_SHA256,
        prefix="later_modal",
        code_prefix="LATER_MODAL_ARTIFACT",
        checks=checks,
    )
    if code is not None or value is None:
        return code, reason, validation
    operation = value.get("receiver_originating_modal_fact_evaluation_operation")
    posture = value.get("operation_posture")
    excluded = value.get("excluded_condition_posture")
    lineage = value.get("lineage_preservation_posture")
    identity = _exact_equal(
        value.get("resolver_module"),
        "resolve_receiver_originating_modal_fact_evaluation_operation_v0_min",
    ) and _exact_equal(value.get("result_version"), "0.1.0")
    result_valid = (
        _exact_equal(
            value.get("outcome"),
            "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_SUPPORTED",
        )
        and _exact_equal(
            value.get("operation_result"),
            "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_SUPPORTED",
        )
        and _exact_equal(value.get("failed_check_count"), 0)
        and _exact_equal(value.get("passed_check_count"), 378)
        and _block_is_clear(value)
    )
    completion = isinstance(posture, Mapping) and all(
        _exact_equal(posture.get(field), expected)
        for field, expected in {
            "operation_basis_supplied": True,
            "operation_basis_admitted": True,
            "receiver_originating_modal_fact_evaluation_performed": True,
            "receiver_originating_modal_fact_evaluation_operation_exhausted": True,
            "completed_modal_fact_evaluation_result_posture_count": 1,
        }.items()
    ) and value.get("admissible_future_route") is None
    targets = isinstance(operation, Mapping) and all(
        _exact_equal(operation.get(field), expected)
        for field, expected in {
            "receiver_answerable_basis_refusable_evaluation": (
                "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE"
            ),
            "receiver_answerable_basis_could_have_been_withheld_evaluation": (
                "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE"
            ),
            "receiver_answerable_basis_refusable_supported": True,
            "receiver_answerable_basis_could_have_been_withheld_supported": True,
            "receiver_answerable_basis_refusable_established": False,
            "receiver_answerable_basis_could_have_been_withheld_established": False,
        }.items()
    )
    excluded_valid = (
        isinstance(excluded, Mapping)
        and excluded.get("excluded_condition_evaluation_performed") is False
        and excluded.get("excluded_conditions_not_evaluated") is True
        and _exact_equal(
            excluded.get("condition_evaluations"),
            {condition: "NOT_EVALUATED" for condition in REQUIRED_CONDITIONS},
        )
    )
    prior_preserved = isinstance(operation, Mapping) and all(
        operation.get(field) is False
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        )
    ) and isinstance(lineage, Mapping) and all(
        lineage.get(field) is True
        for field in (
            "prior_presence_requires_basis_result_preserved",
            "source_admissibility_boundary_result_preserved",
            "source_not_naturalized",
            "jurisdiction_not_collapsed",
            "contaminated_lineage_unchanged",
        )
    )
    for name, valid in (
        ("identity", identity),
        ("result", result_valid),
        ("completion", completion),
        ("target_support_without_establishment", targets),
        ("ten_conditions_not_evaluated", excluded_valid),
        ("prior_presence_false_locks", prior_preserved),
    ):
        if not _add_check(
            checks,
            "later_modal." + name,
            valid,
            "LATER_MODAL_ARTIFACT_INVALID",
        ):
            return (
                "LATER_MODAL_ARTIFACT_INVALID",
                "later modal standing is invalid",
                validation,
            )
    validation.update(
        {
            "identity_validated": True,
            "result_validated": True,
            "completion_and_cardinality_validated": True,
            "false_locks_validated": True,
            "artifact_validated": True,
            "standing": {
                "outcome": value.get("outcome"),
                "operation_result": value.get("operation_result"),
                "passed_check_count": 378,
                "receiver_answerable_basis_refusable_evaluation": (
                    "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE"
                ),
                "receiver_answerable_basis_could_have_been_withheld_evaluation": (
                    "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE"
                ),
                "receiver_answerable_basis_refusable_established": False,
                "receiver_answerable_basis_could_have_been_withheld_established": False,
                "ten_current_target_conditions": {
                    condition: "NOT_EVALUATED" for condition in REQUIRED_CONDITIONS
                },
                "admissible_future_route": None,
            },
        }
    )
    return None, None, validation


def _validate_modal_terminal_summary(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = {
        "terminal_summary_path": str(MODAL_TERMINAL_SUMMARY_RELATIVE_PATH),
        "expected_sha256": MODAL_TERMINAL_SUMMARY_SHA256,
        "observed_sha256": None,
        "strict_utf8_validated": False,
        "standing_markers_validated": False,
        "terminal_summary_validated": False,
    }
    payload, error = _read_bytes(path)
    if error is not None or payload is None:
        _add_check(
            checks,
            "modal_terminal_summary.readable",
            False,
            "MODAL_TERMINAL_SUMMARY_MISSING_OR_UNREADABLE",
        )
        return (
            "MODAL_TERMINAL_SUMMARY_MISSING_OR_UNREADABLE",
            "modal terminal summary is missing or unreadable",
            validation,
        )
    observed = _sha256(payload)
    validation["observed_sha256"] = observed
    if not _add_check(
        checks,
        "modal_terminal_summary.sha256",
        observed == MODAL_TERMINAL_SUMMARY_SHA256,
        "MODAL_TERMINAL_SUMMARY_DIGEST_MISMATCH",
        expected=MODAL_TERMINAL_SUMMARY_SHA256,
    ):
        return (
            "MODAL_TERMINAL_SUMMARY_DIGEST_MISMATCH",
            "modal terminal summary digest mismatch",
            validation,
        )
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        _add_check(
            checks,
            "modal_terminal_summary.utf8",
            False,
            "MODAL_TERMINAL_SUMMARY_INVALID",
        )
        return "MODAL_TERMINAL_SUMMARY_INVALID", "terminal summary is invalid", validation
    markers = (
        "# Receiver-Originating Modal Fact Evaluation Operation V0 Minimum Terminal Summary",
        "`outcome = RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_SUPPORTED`",
        "`failed_check_count = 0`",
        "`passed_check_count = 378`",
        "`receiver_answerable_basis_refusable_established = false`",
        "`receiver_answerable_basis_could_have_been_withheld_established = false`",
        "open does not mean next",
    )
    valid = all(marker in text for marker in markers)
    _add_check(
        checks,
        "modal_terminal_summary.standing_markers",
        valid,
        "MODAL_TERMINAL_SUMMARY_INVALID",
    )
    if not valid:
        return "MODAL_TERMINAL_SUMMARY_INVALID", "terminal summary marker missing", validation
    validation.update(
        {
            "strict_utf8_validated": True,
            "standing_markers_validated": True,
            "terminal_summary_validated": True,
        }
    )
    return None, None, validation


def _carriage_contracts() -> tuple[dict[str, Any], ...]:
    return (
        {
            "name": "candidate_reception",
            "relative_path": CANDIDATE_RECEPTION_ARTIFACT_RELATIVE_PATH,
            "path": CARRIAGE_LINEAGE_PATHS[0],
            "sha256": CANDIDATE_RECEPTION_SHA256,
            "resolver_module": "resolve_receiver_side_answerable_basis_reception_operation_v0_min",
            "result_version": "0.1.0",
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED",
            "passed_check_count": 105,
            "required_paths": (
                (("operation_result_detail", "result"), "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEIVED"),
                (("receiver_side_answerable_basis_reception_operation", "receiver_side_answerable_basis_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
                (("receiver_side_answerable_basis_reception_operation", "receiver_side_answerable_basis_reception_operation_result_recorded"), True),
            ),
        },
        {
            "name": "candidate_evaluation",
            "relative_path": CANDIDATE_EVALUATION_ARTIFACT_RELATIVE_PATH,
            "path": CARRIAGE_LINEAGE_PATHS[1],
            "sha256": CANDIDATE_EVALUATION_SHA256,
            "resolver_module": "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3",
            "result_version": "0.2.0",
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_RECORDED",
            "passed_check_count": 152,
            "required_paths": (
                (("operation_result_detail", "operation_result"), "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED"),
                (("operation_result_detail", "candidate_evaluation_operation_exhausted"), True),
                (("receiver_side_answerable_basis_candidate_evaluation_operation_basis", "candidate_structural_correspondence", "selected_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        },
        {
            "name": "candidate_sufficiency",
            "relative_path": CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
            "path": CARRIAGE_LINEAGE_PATHS[2],
            "sha256": CANDIDATE_SUFFICIENCY_SHA256,
            "resolver_module": "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min",
            "result_version": "0.1.0",
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_RECORDED",
            "passed_check_count": 140,
            "required_paths": (
                (("operation_result_detail", "operation_result"), "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"),
                (("receiver_side_answerable_basis_candidate_sufficiency_operation", "candidate_sufficiency_operation_exhausted"), True),
                (("receiver_side_answerable_basis_candidate_sufficiency_operation", "receiver_side_answerable_basis_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        },
        {
            "name": "receiver_attestation_operation_basis_declaration",
            "relative_path": ATTESTATION_BASIS_DECLARATION_ARTIFACT_RELATIVE_PATH,
            "path": CARRIAGE_LINEAGE_PATHS[3],
            "sha256": ATTESTATION_BASIS_DECLARATION_SHA256,
            "resolver_module": "resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min",
            "result_version": "0.1.0",
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_DECLARED",
            "passed_check_count": 55,
            "required_paths": (
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration", "declaration_result"), "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARED"),
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration", "declaration_exhausted"), True),
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration", "receiver_side_answerable_basis_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        },
        {
            "name": "receiver_attestation_operation_basis_supply",
            "relative_path": ATTESTATION_BASIS_SUPPLY_ARTIFACT_RELATIVE_PATH,
            "path": CARRIAGE_LINEAGE_PATHS[4],
            "sha256": ATTESTATION_BASIS_SUPPLY_SHA256,
            "resolver_module": "resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min",
            "result_version": "0.1.0",
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_SUPPLY_SUPPLIED",
            "passed_check_count": 101,
            "required_paths": (
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_supply", "supply_result"), "RECEIVER_ATTESTATION_OPERATION_BASIS_SUPPLIED"),
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_supply", "supply_exhausted"), True),
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_supply", "receiver_side_answerable_basis_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        },
        {
            "name": "receiver_attestation_operation",
            "relative_path": RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH,
            "path": CARRIAGE_LINEAGE_PATHS[5],
            "sha256": RECEIVER_ATTESTATION_SHA256,
            "resolver_module": "resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min",
            "result_version": "0.1.0",
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_RECORDED",
            "passed_check_count": 160,
            "required_paths": (
                (("operation_result_detail", "operation_result"), "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"),
                (("operation_result_detail", "completed_result_posture_count"), 1),
                (("operation_posture", "operation_exhausted"), True),
                (("selected_operation_and_candidate_identity", "selected_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        },
        {
            "name": "receiver_answerable_receipt_operation",
            "relative_path": RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH,
            "path": CARRIAGE_LINEAGE_PATHS[6],
            "sha256": RECEIVER_ANSWERABLE_RECEIPT_SHA256,
            "resolver_module": "resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min",
            "result_version": "0.1.0",
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RECORDED",
            "passed_check_count": 357,
            "required_paths": (
                (("operation_result",), "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_RECORDED"),
                (("operation_posture", "completed_result_posture_count"), 1),
                (("operation_posture", "receiver_answerable_receipt_operation_exhausted"), True),
                (("selected_operation_and_candidate_identity", "selected_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        },
    )


def _validate_carriage_lineage(
    paths: Sequence[Path | str], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, list[dict[str, Any]]]:
    validations: list[dict[str, Any]] = []
    contracts = _carriage_contracts()
    primary_keys = {
        "candidate_reception": "receiver_side_answerable_basis_reception_operation",
        "candidate_evaluation": "receiver_side_answerable_basis_candidate_evaluation_operation",
        "candidate_sufficiency": "receiver_side_answerable_basis_candidate_sufficiency_operation",
        "receiver_attestation_operation_basis_declaration": "receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration",
        "receiver_attestation_operation_basis_supply": "receiver_side_answerable_basis_receiver_attestation_operation_basis_supply",
        "receiver_attestation_operation": "receiver_side_answerable_basis_receiver_attestation_operation",
        "receiver_answerable_receipt_operation": "receiver_side_answerable_basis_receiver_answerable_receipt_operation",
    }
    required_false_locks = (
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "identity_created",
        "authority_created",
        "standing_created",
        "truth_created",
        "follow_on_work_authorized",
        "action_authorized",
        "output_authorized",
        "runtime_created",
        "api_created",
        "public_interface_created",
    )
    if len(paths) != len(contracts):
        _add_check(
            checks,
            "carriage_lineage.path_count",
            False,
            "READ_CONTRACT_INVALID",
        )
        return "READ_CONTRACT_INVALID", "carriage lineage path count is invalid", validations
    for supplied_path, contract in zip(paths, contracts):
        value, validation, code, reason = _load_pinned_json(
            path=supplied_path,
            relative_path=contract["relative_path"],
            digest=contract["sha256"],
            prefix="carriage_lineage." + contract["name"],
            code_prefix="CARRIAGE_LINEAGE_ARTIFACT",
            checks=checks,
        )
        validations.append(validation)
        if code is not None or value is None:
            return code, reason, validations
        identity = _exact_equal(
            value.get("resolver_module"), contract["resolver_module"]
        ) and _exact_equal(value.get("result_version"), contract["result_version"])
        result_valid = (
            _exact_equal(value.get("outcome"), contract["outcome"])
            and _exact_equal(value.get("failed_check_count"), 0)
            and _exact_equal(
                value.get("passed_check_count"), contract["passed_check_count"]
            )
            and _block_is_clear(value)
        )
        compact = all(
            _exact_equal(_get_path(value, field_path), expected)
            for field_path, expected in contract["required_paths"]
        )
        primary = value.get(primary_keys[contract["name"]])
        false_locks = isinstance(primary, Mapping) and all(
            primary.get(field) is False for field in required_false_locks
        )
        if contract["name"] == "candidate_reception":
            correspondence = (
                isinstance(primary, Mapping)
                and primary.get("candidate_source_provenance_reference_supplied")
                is True
                and primary.get("declared_source_provenance_reference_to_verified_provenance")
                is False
            )
        else:
            correspondence = True
        for name, valid in (
            ("identity", identity),
            ("result", result_valid),
            ("completion_correspondence_and_cardinality", compact),
            ("required_false_locks", false_locks),
            ("source_provenance_correspondence", correspondence),
        ):
            if not _add_check(
                checks,
                "carriage_lineage." + contract["name"] + "." + name,
                valid,
                "CARRIAGE_LINEAGE_ARTIFACT_INVALID",
            ):
                return (
                    "CARRIAGE_LINEAGE_ARTIFACT_INVALID",
                    contract["name"] + " standing is invalid",
                    validations,
                )
        validation.update(
            {
                "identity_validated": True,
                "result_validated": True,
                "completion_and_cardinality_validated": True,
                "false_locks_validated": false_locks,
                "artifact_validated": True,
                "standing": {
                    "lineage_surface": contract["name"],
                    "resolver_module": contract["resolver_module"],
                    "result_version": contract["result_version"],
                    "outcome": contract["outcome"],
                    "passed_check_count": contract["passed_check_count"],
                    "selected_candidate_id": "receiver_side_answerable_basis_candidate_001",
                    "complete_body_omitted": True,
                },
            }
        )
    return None, None, validations


def _parse_exact_records(text: str) -> tuple[dict[str, str] | None, bool]:
    records: dict[str, str] = {}
    for line in text.splitlines():
        if "=" not in line:
            return None, False
        key, value = line.split("=", 1)
        if not key or not value or key in records:
            return None, False
        records[key] = value
    return records, True


def _validate_packet_texts(
    paths: Sequence[Path | str], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, list[dict[str, Any]]]:
    validations: list[dict[str, Any]] = []
    if len(paths) != len(PACKET_TEXT_RELATIVE_PATHS):
        _add_check(checks, "packet_text.path_count", False, "READ_CONTRACT_INVALID")
        return "READ_CONTRACT_INVALID", "packet text path count is invalid", validations
    for index, (supplied, relative, expected_text, digest, byte_count) in enumerate(
        zip(
            paths,
            PACKET_TEXT_RELATIVE_PATHS,
            PACKET_TEXT_CONTENTS,
            PACKET_TEXT_SHA256,
            PACKET_TEXT_BYTE_COUNTS,
        )
    ):
        name = relative.name
        validation = {
            "surface_path": str(relative),
            "expected_sha256": digest,
            "observed_sha256": None,
            "expected_byte_count": byte_count,
            "observed_byte_count": None,
            "strict_utf8_validated": False,
            "bom_absent": False,
            "exact_content_validated": False,
            "duplicate_record_keys_absent": False,
            "surface_validated": False,
            "complete_body_omitted": True,
        }
        validations.append(validation)
        payload, error = _read_bytes(supplied)
        if error is not None or payload is None:
            _add_check(
                checks,
                "packet_text." + name + ".readable",
                False,
                "PACKET_TEXT_MISSING_OR_UNREADABLE",
            )
            return (
                "PACKET_TEXT_MISSING_OR_UNREADABLE",
                name + " is missing or unreadable",
                validations,
            )
        observed = _sha256(payload)
        validation["observed_sha256"] = observed
        validation["observed_byte_count"] = len(payload)
        if not _add_check(
            checks,
            "packet_text." + name + ".sha256",
            observed == digest,
            "PACKET_TEXT_DIGEST_MISMATCH",
            expected=digest,
        ):
            return "PACKET_TEXT_DIGEST_MISMATCH", name + " digest mismatch", validations
        try:
            text = payload.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            _add_check(
                checks,
                "packet_text." + name + ".utf8",
                False,
                "PACKET_TEXT_INVALID",
            )
            return "PACKET_TEXT_INVALID", name + " is not strict UTF-8", validations
        exact = (
            len(payload) == byte_count
            and text == expected_text
            and not payload.startswith(b"\xef\xbb\xbf")
        )
        if name == "attestation_statement.txt":
            duplicate_free = text == "knock knock back"
        else:
            _, duplicate_free = _parse_exact_records(text)
        for part, valid in (
            ("exact_bytes", exact),
            ("record_set", duplicate_free),
        ):
            if not _add_check(
                checks,
                "packet_text." + name + "." + part,
                valid,
                "PACKET_TEXT_INVALID",
            ):
                return "PACKET_TEXT_INVALID", name + " content is invalid", validations
        validation.update(
            {
                "strict_utf8_validated": True,
                "bom_absent": True,
                "exact_content_validated": True,
                "duplicate_record_keys_absent": True,
                "surface_validated": True,
            }
        )
    return None, None, validations


def _conduct_contracts() -> tuple[dict[str, Any], ...]:
    return (
        {"name": "presence_operation_specification", "kind": "text", "marker": "# Presence Operation", "relative_path": SOURCE_BODY_CONDUCT_RELATIVE_PATHS[0], "sha256": SOURCE_BODY_CONDUCT_SHA256[0]},
        {"name": "presence_operation_resolver", "kind": "text", "marker": 'RESOLVER_MODULE = "resolve_presence_operation_v0_min"', "relative_path": SOURCE_BODY_CONDUCT_RELATIVE_PATHS[1], "sha256": SOURCE_BODY_CONDUCT_SHA256[1]},
        {"name": "presence_operation_result", "kind": "json", "relative_path": SOURCE_BODY_CONDUCT_RELATIVE_PATHS[2], "sha256": SOURCE_BODY_CONDUCT_SHA256[2], "module": "resolve_presence_operation_v0_min", "version": "0.1.0", "outcome": "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION"},
        {"name": "reception_boundary_specification", "kind": "text", "marker": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY", "relative_path": SOURCE_BODY_CONDUCT_RELATIVE_PATHS[3], "sha256": SOURCE_BODY_CONDUCT_SHA256[3]},
        {"name": "reception_boundary_resolver", "kind": "text", "marker": "resolve_receiver_side_answerable_basis_reception_boundary_v0_min", "relative_path": SOURCE_BODY_CONDUCT_RELATIVE_PATHS[4], "sha256": SOURCE_BODY_CONDUCT_SHA256[4]},
        {"name": "reception_boundary_result", "kind": "json", "relative_path": SOURCE_BODY_CONDUCT_RELATIVE_PATHS[5], "sha256": SOURCE_BODY_CONDUCT_SHA256[5], "module": "resolve_receiver_side_answerable_basis_reception_boundary_v0_min_v2", "version": "0.2.0", "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_ALLOWED"},
        {"name": "reception_operation_specification", "kind": "text", "marker": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION", "relative_path": SOURCE_BODY_CONDUCT_RELATIVE_PATHS[6], "sha256": SOURCE_BODY_CONDUCT_SHA256[6]},
        {"name": "reception_operation_resolver", "kind": "text", "marker": 'RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_reception_operation_v0_min"', "relative_path": SOURCE_BODY_CONDUCT_RELATIVE_PATHS[7], "sha256": SOURCE_BODY_CONDUCT_SHA256[7]},
        {"name": "reception_operation_result", "kind": "json", "relative_path": SOURCE_BODY_CONDUCT_RELATIVE_PATHS[8], "sha256": SOURCE_BODY_CONDUCT_SHA256[8], "module": "resolve_receiver_side_answerable_basis_reception_operation_v0_min", "version": "0.1.0", "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED"},
    )


def _validate_conduct_surfaces(
    paths: Sequence[Path | str], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, list[dict[str, Any]]]:
    validations: list[dict[str, Any]] = []
    contracts = _conduct_contracts()
    if len(paths) != len(contracts):
        _add_check(checks, "source_body_conduct.path_count", False, "READ_CONTRACT_INVALID")
        return "READ_CONTRACT_INVALID", "conduct path count is invalid", validations
    for supplied, contract in zip(paths, contracts):
        validation = {
            "surface_path": str(contract["relative_path"]),
            "surface_class": contract["name"],
            "expected_sha256": contract["sha256"],
            "observed_sha256": None,
            "strict_content_validated": False,
            "bounded_standing_validated": False,
            "surface_validated": False,
            "complete_body_omitted": True,
        }
        validations.append(validation)
        payload, error = _read_bytes(supplied)
        if error is not None or payload is None:
            _add_check(
                checks,
                "source_body_conduct." + contract["name"] + ".readable",
                False,
                "SOURCE_BODY_CONDUCT_SURFACE_MISSING_OR_UNREADABLE",
            )
            return (
                "SOURCE_BODY_CONDUCT_SURFACE_MISSING_OR_UNREADABLE",
                contract["name"] + " is missing or unreadable",
                validations,
            )
        observed = _sha256(payload)
        validation["observed_sha256"] = observed
        if not _add_check(
            checks,
            "source_body_conduct." + contract["name"] + ".sha256",
            observed == contract["sha256"],
            "SOURCE_BODY_CONDUCT_SURFACE_DIGEST_MISMATCH",
            expected=contract["sha256"],
        ):
            return (
                "SOURCE_BODY_CONDUCT_SURFACE_DIGEST_MISMATCH",
                contract["name"] + " digest mismatch",
                validations,
            )
        if contract["kind"] == "json":
            parsed, parse_error = _parse_json_bytes(payload)
            valid = (
                parse_error is None
                and isinstance(parsed, Mapping)
                and parsed.get("resolver_module") == contract["module"]
                and parsed.get("result_version") == contract["version"]
                and parsed.get("outcome") == contract["outcome"]
                and _block_is_clear(parsed)
            )
        else:
            try:
                text = payload.decode("utf-8", errors="strict")
                valid = not payload.startswith(b"\xef\xbb\xbf") and contract["marker"] in text
            except UnicodeDecodeError:
                valid = False
        if not _add_check(
            checks,
            "source_body_conduct." + contract["name"] + ".standing",
            valid,
            "SOURCE_BODY_CONDUCT_SURFACE_INVALID",
        ):
            return (
                "SOURCE_BODY_CONDUCT_SURFACE_INVALID",
                contract["name"] + " standing is invalid",
                validations,
            )
        validation.update(
            {
                "strict_content_validated": True,
                "bounded_standing_validated": True,
                "surface_validated": True,
            }
        )
    return None, None, validations


def _validate_contracts(checks: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    matter_valid = (
        len(REQUIRED_CONDITIONS) == 10
        and tuple(REQUIRED_CONDITION_VALUES) == REQUIRED_CONDITIONS
        and REQUIRED_CONDITION_VALUES[REQUIRED_CONDITIONS[0]] is True
        and all(REQUIRED_CONDITION_VALUES[item] is False for item in REQUIRED_CONDITIONS[1:])
        and EVIDENCE_CLASSES
        == (
            "CUSTODY_AND_CONTROL",
            "EXECUTION_AND_ATTESTATION_FORM",
            "ADVERSARIAL_INTEGRITY_AND_BOUNDED_ADMISSIBILITY",
        )
        and tuple(
            item
            for evidence_class in EVIDENCE_CLASSES
            for item in EVIDENCE_CLASS_CONDITION_MAPPING[evidence_class]
        )
        == REQUIRED_CONDITIONS
        and CONDITION_EVALUATION_FAMILY
        == (
            "SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS",
            "REQUIRES_BASIS",
            "INDETERMINATE",
            "NOT_EVALUATED",
        )
        and REQUIRED_BASIS_CLASS_FAMILY
        == (
            "CUSTODY_DISTINCT_BASIS",
            "EXTERNAL_AUTHENTICITY_BASIS",
            "OTHER_EXACT_NAMED_BASIS",
            "NONE",
        )
    )
    if not _add_check(checks, "contract.matter_and_families", matter_valid, "MATTER_CONTRACT_INVALID"):
        return "MATTER_CONTRACT_INVALID", "matter or result family is invalid"
    ceiling_valid = len(DEPENDENCY_CEILING_CONTRACT) == 10 and all(
        set(item) == {"condition_id", "ceiling"}
        and isinstance(item["condition_id"], str)
        and isinstance(item["ceiling"], str)
        for item in DEPENDENCY_CEILING_CONTRACT
    )
    if not _add_check(checks, "contract.dependency_ceilings", ceiling_valid, "DEPENDENCY_CEILING_INVALID"):
        return "DEPENDENCY_CEILING_INVALID", "dependency ceiling contract is invalid"
    ledger_valid = CONDITION_LEDGER_SCHEMA_FIELDS == (
        "condition_id",
        "required_value",
        "prior_condition_posture",
        "evidence_class",
        "permitted_artifact_references",
        "supporting_fields_or_bytes",
        "support_proposition",
        "limitation",
        "dependency_conditions",
        "dependency_ceiling",
        "candidate_evidence_considered_but_not_admitted",
        "evaluation_posture",
        "required_basis_class",
        "compact_support_boolean",
        "successor_condition_posture",
        "prior_posture_preserved",
        "no_overwrite",
    )
    if not _add_check(checks, "contract.condition_ledger_schema", ledger_valid, "CONDITION_LEDGER_SCHEMA_INVALID"):
        return "CONDITION_LEDGER_SCHEMA_INVALID", "condition ledger schema is invalid"
    raw_valid = _exact_equal(RAW_SIGNAL_POSTURE, {
        "raw_signal_body_known_to_exist": True,
        "raw_signal_body_considered": True,
        "raw_signal_body_admitted": False,
        "raw_signal_body_read_authorized": False,
        "signal_morphology_evaluation_authorized": False,
        "authenticity_upgrade_from_signal_authorized": False,
    })
    if not _add_check(checks, "contract.raw_signal_non_admission", raw_valid, "RAW_SIGNAL_POSTURE_INVALID"):
        return "RAW_SIGNAL_POSTURE_INVALID", "raw signal posture is invalid"
    try:
        start = datetime.fromisoformat(KNOCK_GENERATED_AT.replace("Z", "+00:00"))
        end = datetime.fromisoformat(RECEIVER_ATTESTATION_CONFIRMED_AT.replace("Z", "+00:00"))
        seconds = int((end - start).total_seconds())
    except ValueError:
        seconds = -1
    temporal_valid = (
        seconds == KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL_SECONDS
        and KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL_COMPONENTS
        == {"days": 12, "hours": 18, "minutes": 29, "seconds": 52}
        and KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL
        == "12 days, 18 hours, 29 minutes, 52 seconds"
    )
    if not _add_check(checks, "contract.temporal_interval", temporal_valid, "TEMPORAL_EVIDENCE_INVALID"):
        return "TEMPORAL_EVIDENCE_INVALID", "temporal interval is invalid"
    _add_check(
        checks,
        "contract.excluded_reads",
        len(EXCLUDED_READ_IDENTIFIERS) == 20,
        "READ_CONTRACT_INVALID",
    )
    if checks[-1]["passed"] is False:
        return "READ_CONTRACT_INVALID", "excluded read contract is invalid"
    return None, None


def _default_validations() -> dict[str, Any]:
    return {
        "specification_validation": _empty_specification_validation(),
        "prior_presence_artifact_validation": _empty_artifact_validation(
            PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH, PRIOR_PRESENCE_SHA256
        ),
        "source_admissibility_boundary_artifact_validation": _empty_artifact_validation(
            SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH,
            SOURCE_ADMISSIBILITY_BOUNDARY_SHA256,
        ),
        "later_modal_artifact_validation": _empty_artifact_validation(
            LATER_MODAL_ARTIFACT_RELATIVE_PATH, LATER_MODAL_SHA256
        ),
        "modal_terminal_summary_validation": {
            "terminal_summary_path": str(MODAL_TERMINAL_SUMMARY_RELATIVE_PATH),
            "expected_sha256": MODAL_TERMINAL_SUMMARY_SHA256,
            "observed_sha256": None,
            "strict_utf8_validated": False,
            "standing_markers_validated": False,
            "terminal_summary_validated": False,
        },
        "carriage_lineage_artifact_validations": [],
        "receiver_packet_text_validations": [],
        "source_body_conduct_validations": [],
    }


def _branch_values(outcome: str) -> dict[str, Any]:
    if outcome == OUTCOME_ALLOWED:
        return {
            "boundary_result": RESULT_ALLOWED,
            "recorded": True,
            "result_recorded": True,
            "allowed": True,
            "not_allowed": False,
            "exhausted": True,
            "completed_count": 1,
            "future_route": ADMISSIBLE_FUTURE_ROUTE,
            "admissibility": ADMISSIBILITY_PASSED,
        }
    if outcome == OUTCOME_NOT_ALLOWED:
        return {
            "boundary_result": RESULT_NOT_ALLOWED,
            "recorded": True,
            "result_recorded": True,
            "allowed": False,
            "not_allowed": True,
            "exhausted": True,
            "completed_count": 1,
            "future_route": None,
            "admissibility": ADMISSIBILITY_PASSED,
        }
    return {
        "boundary_result": RESULT_NOT_EVALUATED,
        "recorded": False,
        "result_recorded": False,
        "allowed": False,
        "not_allowed": False,
        "exhausted": False,
        "completed_count": 0,
        "future_route": None,
        "admissibility": ADMISSIBILITY_NOT_EVALUATED,
    }


def _declared_request_posture(
    request: Mapping[str, Any], *, validated: bool
) -> dict[str, Any]:
    selected_field = (
        "body_held_receiver_answerable_basis_integrity_condition_"
        "evaluation_consideration_selected"
    )
    return {
        "canonical_schema_validated": validated,
        "canonical_identity_and_paths_validated": validated,
        "matter_and_evidence_contract_validated": validated,
        "excluded_read_contract_validated": validated,
        "raw_signal_non_admission_validated": validated,
        "declared_non_claims_validated": validated,
        "result_and_semantic_preclaims_absent": validated,
        "unknown_request_fields_absent": validated,
        "selection": request.get(selected_field) if type(request.get(selected_field)) is bool else None,
    }


def _boundary_object(outcome: str, selection: bool | None) -> dict[str, Any]:
    branch = _branch_values(outcome)
    return {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        BOUNDARY_KEY + "_id": BOUNDARY_ID,
        BOUNDARY_KEY + "_type": BOUNDARY_TYPE,
        BOUNDARY_KEY + "_version": BOUNDARY_VERSION,
        BOUNDARY_KEY + "_scope": BOUNDARY_SCOPE,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "ordered_ten_condition_matter": list(REQUIRED_CONDITIONS),
        "required_condition_values": copy.deepcopy(REQUIRED_CONDITION_VALUES),
        "evidence_class_family": list(EVIDENCE_CLASSES),
        "evidence_class_condition_mapping": {
            key: list(value) for key, value in EVIDENCE_CLASS_CONDITION_MAPPING.items()
        },
        "condition_evaluation_family": list(CONDITION_EVALUATION_FAMILY),
        "required_basis_class_family": list(REQUIRED_BASIS_CLASS_FAMILY),
        "later_operation_result_family": list(LATER_OPERATION_RESULT_FAMILY),
        "condition_evaluations": {
            condition: "NOT_EVALUATED" for condition in REQUIRED_CONDITIONS
        },
        "condition_ledger_populated": False,
        "any_condition_evaluated": False,
        "later_operation_created": False,
        "later_operation_executed": False,
        "later_operation_result_selected": False,
        (
            "body_held_receiver_answerable_basis_integrity_condition_"
            "evaluation_consideration_selected"
        ): selection,
        BOUNDARY_KEY + "_recorded": branch["recorded"],
        BOUNDARY_KEY + "_result_recorded": branch["result_recorded"],
        BOUNDARY_KEY + "_result": branch["boundary_result"],
        (
            "body_held_receiver_answerable_basis_integrity_condition_"
            "evaluation_consideration_allowed"
        ): branch["allowed"],
        (
            "body_held_receiver_answerable_basis_integrity_condition_"
            "evaluation_consideration_not_allowed"
        ): branch["not_allowed"],
        BOUNDARY_KEY + "_exhausted": branch["exhausted"],
        "completed_consideration_posture_count": branch["completed_count"],
        "admissible_future_route": branch["future_route"],
        "source_and_record_basis_admissibility_evaluation": branch["admissibility"],
        "scope_and_matter_admissibility_evaluation": branch["admissibility"],
        "transition_admissibility_evaluation": branch["admissibility"],
        **_canonical_non_claims(),
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get(BOUNDARY_KEY, {})
    decision = result.get("boundary_decision", {})
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "outcome": result.get("outcome"),
        "boundary_result": result.get("boundary_result"),
        "blocked": result.get("outcome") == OUTCOME_BLOCKED,
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "ordered_ten_condition_matter": list(REQUIRED_CONDITIONS),
        "decision_code": decision.get("decision_code") if isinstance(decision, Mapping) else None,
        "decision_reason": decision.get("decision_reason") if isinstance(decision, Mapping) else None,
        "selection": decision.get("selection") if isinstance(decision, Mapping) else None,
        "boundary_recorded": boundary.get(BOUNDARY_KEY + "_recorded") if isinstance(boundary, Mapping) else False,
        "boundary_result_recorded": boundary.get(BOUNDARY_KEY + "_result_recorded") if isinstance(boundary, Mapping) else False,
        "boundary_exhausted": boundary.get(BOUNDARY_KEY + "_exhausted") if isinstance(boundary, Mapping) else False,
        "completed_consideration_posture_count": result.get("completed_consideration_posture_count"),
        "admissible_future_route": result.get("admissible_future_route"),
        "all_ten_conditions_not_evaluated": isinstance(boundary, Mapping) and all(
            value == "NOT_EVALUATED"
            for value in boundary.get("condition_evaluations", {}).values()
        ) and len(boundary.get("condition_evaluations", {})) == 10,
        "later_operation_not_created_or_executed": isinstance(boundary, Mapping)
        and boundary.get("later_operation_created") is False
        and boundary.get("later_operation_executed") is False,
        "raw_signal_body_considered": True,
        "raw_signal_body_admitted": False,
        "read_contract_closed": result.get("frozen_read_contract_posture", {}).get("read_contract_closed", False),
        "prior_presence_result_preserved": result.get("lineage_preservation_posture", {}).get("prior_presence_result_preserved", False),
        "later_modal_standing_preserved": result.get("lineage_preservation_posture", {}).get("later_two_source_supported_modal_evaluations_preserved", False),
        "result_level_non_claims_canonical_false": result.get("result_level_non_claims_canonical_false"),
        "complete_material_omission_posture": result.get("omission_posture", {}).get("complete_material_omission_posture", False),
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    code: str | None = None,
    reason: str | None = None,
    request_validated: bool = False,
    validations: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    branch = _branch_values(outcome)
    selected_field = (
        "body_held_receiver_answerable_basis_integrity_condition_"
        "evaluation_consideration_selected"
    )
    selection = request.get(selected_field)
    if type(selection) is not bool:
        selection = None
    if outcome == OUTCOME_ALLOWED:
        decision_code = DECISION_CODE_ALLOWED
        decision_reason = DECISION_REASON_ALLOWED
    elif outcome == OUTCOME_NOT_ALLOWED:
        decision_code = DECISION_CODE_NOT_ALLOWED
        decision_reason = DECISION_REASON_NOT_ALLOWED
    else:
        decision_code = None
        decision_reason = None
    failed = sum(item.get("passed") is False for item in checks)
    passed = sum(item.get("passed") is True for item in checks)
    completed = outcome in (OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED)
    all_validations = _default_validations()
    if validations:
        all_validations.update(copy.deepcopy(dict(validations)))
    boundary = _boundary_object(outcome, selection)
    result: dict[str, Any] = {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "boundary_result": branch["boundary_result"],
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code if outcome == OUTCOME_BLOCKED else None,
            "block_code": code if outcome == OUTCOME_BLOCKED else None,
            "reason": reason if outcome == OUTCOME_BLOCKED else None,
        },
        "failed_check_count": failed,
        "passed_check_count": passed,
        "completed_consideration_posture_count": branch["completed_count"],
        "admissible_future_route": branch["future_route"],
        "result_level_non_claims_canonical_false": True,
        DECLARED_REQUEST_KEY: _declared_request_posture(
            request, validated=request_validated
        ),
        METADATA_KEY: {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
            "prior_presence_artifact_path": str(PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH),
            "source_admissibility_boundary_artifact_path": str(SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH),
            "later_modal_artifact_path": str(LATER_MODAL_ARTIFACT_RELATIVE_PATH),
            "modal_terminal_summary_path": str(MODAL_TERMINAL_SUMMARY_RELATIVE_PATH),
        },
        **all_validations,
        "frozen_read_contract_posture": {
            "governing_and_current_standing_surface_count": 5,
            "carriage_lineage_surface_count": 7,
            "receiver_packet_text_surface_count": 8,
            "source_body_conduct_surface_count": 9,
            "all_governing_and_current_standing_surfaces_selected": completed,
            "all_carriage_lineage_surfaces_selected": completed,
            "all_receiver_packet_text_surfaces_selected": completed,
            "all_source_body_conduct_surfaces_selected": completed,
            "no_other_surface_selected": True,
            "request_json_admitted_only_through_explicit_from_path_api": True,
            "read_contract_closed": completed,
            "broad_availability_is_not_permission": True,
        },
        "excluded_read_posture": {
            "excluded_read_identifiers": list(EXCLUDED_READ_IDENTIFIERS),
            "excluded_reads_performed": False,
            "raw_signal_json_opened": False,
            "original_zip_bytes_opened": False,
            "archive_extracted": False,
            "glob_used": False,
            "rglob_used": False,
            "directory_scan_performed": False,
            "latest_file_selected": False,
            "source_reconstructed": False,
        },
        "raw_signal_considered_but_not_admitted_posture": copy.deepcopy(RAW_SIGNAL_POSTURE),
        "temporal_evidence_posture": {
            "knock_generated_at": KNOCK_GENERATED_AT,
            "receiver_attestation_confirmed_at": RECEIVER_ATTESTATION_CONFIRMED_AT,
            "knock_to_receiver_attestation_interval_seconds": KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL_SECONDS,
            "knock_to_receiver_attestation_interval_components": copy.deepcopy(KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL_COMPONENTS),
            "knock_to_receiver_attestation_interval": KNOCK_TO_RECEIVER_ATTESTATION_INTERVAL,
            "current_clock_used": False,
            "actual_withholding_inferred": False,
            "actual_refusal_inferred": False,
            "receiver_freedom_inferred": False,
            "universal_automation_absence_inferred": False,
        },
        "exact_matter_and_evidence_class_posture": {
            "selected_matter_class": SELECTED_MATTER_CLASS,
            "ordered_ten_condition_matter": list(REQUIRED_CONDITIONS),
            "required_condition_values": copy.deepcopy(REQUIRED_CONDITION_VALUES),
            "evidence_class_family": list(EVIDENCE_CLASSES),
            "evidence_class_condition_mapping": {
                key: list(value) for key, value in EVIDENCE_CLASS_CONDITION_MAPPING.items()
            },
            "condition_evaluation_family": list(CONDITION_EVALUATION_FAMILY),
            "required_basis_class_family": list(REQUIRED_BASIS_CLASS_FAMILY),
            "later_operation_result_family": list(LATER_OPERATION_RESULT_FAMILY),
            "condition_results_selected": False,
            "operation_result_selected": False,
        },
        "dependency_ceiling_contract": copy.deepcopy(list(DEPENDENCY_CEILING_CONTRACT)),
        "condition_ledger_schema_contract": {
            "required_fields": list(CONDITION_LEDGER_SCHEMA_FIELDS),
            "ledger_rows_populated": False,
            "selected_condition_results_emitted": False,
        },
        "admissibility_evaluations": {
            "source_and_record_basis_admissibility_evaluation": branch["admissibility"],
            "scope_and_matter_admissibility_evaluation": branch["admissibility"],
            "transition_admissibility_evaluation": branch["admissibility"],
        },
        "boundary_decision": {
            "selection": selection,
            "decision_code": decision_code,
            "decision_reason": decision_reason,
        },
        "boundary_posture": {
            BOUNDARY_KEY + "_recorded": branch["recorded"],
            BOUNDARY_KEY + "_result_recorded": branch["result_recorded"],
            BOUNDARY_KEY + "_exhausted": branch["exhausted"],
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_consideration_allowed": branch["allowed"],
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_consideration_not_allowed": branch["not_allowed"],
            "completed_consideration_posture_count": branch["completed_count"],
            "source_and_record_basis_admissibility_evaluation": branch["admissibility"],
            "scope_and_matter_admissibility_evaluation": branch["admissibility"],
            "transition_admissibility_evaluation": branch["admissibility"],
            "single_use_only": completed,
            "boundary_exhaustion_is_not_evaluation": True,
            "boundary_exhaustion_is_not_complete_receiver_answerable_basis": True,
            "boundary_exhaustion_is_not_standing_or_presence": True,
        },
        BOUNDARY_KEY: boundary,
        "lineage_preservation_posture": (
            _canonical_lineage_posture()
            if completed
            else {field: False for field in LINEAGE_PRESERVATION_FIELDS}
        ),
        "omission_posture": _canonical_omission_posture(),
        "non_claims": _canonical_non_claims(),
        NON_MEANING_KEY: _canonical_non_meaning(),
        "blocked_conversions": list(BLOCKED_CONVERSIONS),
        STATEMENT_KEY: {
            "one_frozen_read_contract_considered": completed,
            "ten_condition_matter_preserved": completed,
            "three_evidence_classes_preserved": completed,
            "no_condition_evaluated": True,
            "no_condition_ledger_populated": True,
            "no_later_operation_created_or_executed": True,
            "raw_signal_considered_but_not_admitted": True,
            "prior_presence_standing_not_overwritten": True,
            "later_modal_standing_not_overwritten": True,
            "result_level_non_claims_canonical_false": True,
        },
        CHECKS_KEY: copy.deepcopy(checks),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
    }
    result[SUMMARY_KEY] = _summary_from_result(result)
    return result


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_default_result(
) -> dict[str, Any]:
    """Return the pre-execution posture without reading the filesystem."""
    checks = [_check("execution.not_started", False, code="NOT_EXECUTED")]
    return _build_result(
        _new_canonical_request(),
        OUTCOME_BLOCKED,
        checks,
        code="NOT_EXECUTED",
        reason="boundary resolution has not been executed",
    )


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_result(
) -> dict[str, Any]:
    """Compatibility alias for the pure pre-execution result constructor."""
    return build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_default_result()


def resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min(
    request: Mapping[str, Any] | None = None,
    *,
    governing_specification_path: Path | str | None = None,
    prior_presence_artifact_path: Path | str | None = None,
    source_admissibility_boundary_artifact_path: Path | str | None = None,
    later_modal_artifact_path: Path | str | None = None,
    modal_terminal_summary_path: Path | str | None = None,
    carriage_lineage_paths: Sequence[Path | str] | None = None,
    receiver_packet_text_paths: Sequence[Path | str] | None = None,
    source_body_conduct_paths: Sequence[Path | str] | None = None,
) -> dict[str, Any]:
    """Resolve one exact boundary from explicit governed paths only."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared = _new_canonical_request()
    elif not isinstance(request, Mapping):
        declared = _new_canonical_request()
        _add_check(checks, "request.mapping", False, "REQUEST_NOT_MAPPING")
        return _build_result(
            declared,
            OUTCOME_BLOCKED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared request is not a mapping",
        )
    else:
        declared = copy.deepcopy(dict(request))
    code, reason = _validate_request(declared, checks)
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason)

    validations: dict[str, Any] = {}
    spec_path = (
        GOVERNING_SPECIFICATION_PATH
        if governing_specification_path is None
        else governing_specification_path
    )
    prior_path = (
        PRIOR_PRESENCE_ARTIFACT_PATH
        if prior_presence_artifact_path is None
        else prior_presence_artifact_path
    )
    source_path = (
        SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_PATH
        if source_admissibility_boundary_artifact_path is None
        else source_admissibility_boundary_artifact_path
    )
    modal_path = (
        LATER_MODAL_ARTIFACT_PATH
        if later_modal_artifact_path is None
        else later_modal_artifact_path
    )
    terminal_path = (
        MODAL_TERMINAL_SUMMARY_PATH
        if modal_terminal_summary_path is None
        else modal_terminal_summary_path
    )
    carriage_paths = tuple(
        CARRIAGE_LINEAGE_PATHS
        if carriage_lineage_paths is None
        else carriage_lineage_paths
    )
    packet_paths = tuple(
        PACKET_TEXT_PATHS
        if receiver_packet_text_paths is None
        else receiver_packet_text_paths
    )
    conduct_paths = tuple(
        SOURCE_BODY_CONDUCT_PATHS
        if source_body_conduct_paths is None
        else source_body_conduct_paths
    )

    code, reason, section = _validate_specification(spec_path, checks)
    validations["specification_validation"] = section
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason, request_validated=True, validations=validations)
    code, reason, section = _validate_prior_presence(prior_path, checks)
    validations["prior_presence_artifact_validation"] = section
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason, request_validated=True, validations=validations)
    code, reason, section = _validate_source_admissibility(source_path, checks)
    validations["source_admissibility_boundary_artifact_validation"] = section
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason, request_validated=True, validations=validations)
    code, reason, section = _validate_later_modal(modal_path, checks)
    validations["later_modal_artifact_validation"] = section
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason, request_validated=True, validations=validations)
    code, reason, section = _validate_modal_terminal_summary(terminal_path, checks)
    validations["modal_terminal_summary_validation"] = section
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason, request_validated=True, validations=validations)
    code, reason, section = _validate_carriage_lineage(carriage_paths, checks)
    validations["carriage_lineage_artifact_validations"] = section
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason, request_validated=True, validations=validations)
    code, reason, section = _validate_packet_texts(packet_paths, checks)
    validations["receiver_packet_text_validations"] = section
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason, request_validated=True, validations=validations)
    code, reason, section = _validate_conduct_surfaces(conduct_paths, checks)
    validations["source_body_conduct_validations"] = section
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason, request_validated=True, validations=validations)
    code, reason = _validate_contracts(checks)
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason, request_validated=True, validations=validations)

    selection_field = (
        "body_held_receiver_answerable_basis_integrity_condition_"
        "evaluation_consideration_selected"
    )
    selected = declared[selection_field]
    outcome = OUTCOME_ALLOWED if selected else OUTCOME_NOT_ALLOWED
    for check_id in (
        "admissibility.source_and_record_basis",
        "admissibility.scope_and_matter",
        "admissibility.transition",
        "lineage.prior_and_later_standing_preserved",
        "omission.complete_material_omitted",
        "nonclaims.canonical_false",
        "decision.branch_cardinality",
        "future_route.not_inflated",
    ):
        _add_check(checks, check_id, True, "ADMISSIBILITY_BLOCKED")
    return _build_result(
        declared,
        outcome,
        checks,
        request_validated=True,
        validations=validations,
    )


def resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_from_path(
    request_path: Path | str,
    **resolver_paths: Any,
) -> dict[str, Any]:
    """Strictly load one explicit request path and return a bounded result."""
    value, _, error = _read_json(request_path)
    if error is not None or not isinstance(value, Mapping):
        checks = [_check("request_path.strict_json_mapping", False, code="REQUEST_JSON_INVALID")]
        return _build_result(
            _new_canonical_request(),
            OUTCOME_BLOCKED,
            checks,
            code="REQUEST_JSON_INVALID",
            reason="explicit request path is missing, malformed, duplicate-keyed, or not a mapping",
        )
    return resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min(
        value,
        **resolver_paths,
    )


def _contains_prohibited_complete_material(value: Any) -> bool:
    forbidden = {
        "complete_upstream_artifact",
        "complete_candidate_body",
        "complete_candidate_evaluation_material",
        "raw_accelerometer_body",
        "raw_signal_body",
        "original_zip_bytes",
        "archive_bytes",
        "filesystem_permissions",
        "acl_data",
        "device_control_data",
        "private_communications",
        "semantic_payload",
        "sufficiency_basis_records",
    }
    if isinstance(value, Mapping):
        return any(key in forbidden or _contains_prohibited_complete_material(item) for key, item in value.items())
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_prohibited_complete_material(item) for item in value)
    return False


def _checks_valid(result: Mapping[str, Any]) -> bool:
    checks = result.get(CHECKS_KEY)
    if not isinstance(checks, list) or not checks:
        return False
    if any(
        not isinstance(item, Mapping)
        or type(item.get("passed")) is not bool
        or set(item) != {"check_id", "passed", "block_code", "failure_code", "expected"}
        or (
            item.get("passed") is False
            and (
                item.get("block_code") not in BLOCK_CODES
                or item.get("failure_code") not in BLOCK_CODES
            )
        )
        or (
            item.get("passed") is True
            and (item.get("block_code") is not None or item.get("failure_code") is not None)
        )
        for item in checks
    ):
        return False
    return (
        result.get("passed_check_count")
        == sum(item["passed"] is True for item in checks)
        and result.get("failed_check_count")
        == sum(item["passed"] is False for item in checks)
    )


def _structural_result_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    if outcome not in OUTCOME_FAMILY or result.get("result_version") != RESULT_VERSION or result.get("resolver_module") != RESOLVER_MODULE:
        return False
    if not _checks_valid(result) or _contains_prohibited_complete_material(result):
        return False
    if not _canonical_false_mapping(result.get("non_claims")):
        return False
    if result.get("result_level_non_claims_canonical_false") is not True:
        return False
    if result.get("omission_posture") != _canonical_omission_posture():
        return False
    if result.get(NON_MEANING_KEY) != _canonical_non_meaning():
        return False
    if result.get("blocked_conversions") != list(BLOCKED_CONVERSIONS):
        return False
    if result.get("what_remains_open") != list(WHAT_REMAINS_OPEN):
        return False
    branch = _branch_values(str(outcome))
    if (
        result.get("boundary_result") != branch["boundary_result"]
        or result.get("completed_consideration_posture_count") != branch["completed_count"]
        or result.get("admissible_future_route") != branch["future_route"]
    ):
        return False
    block = result.get("block")
    if not isinstance(block, Mapping) or block.get("blocked") is not (outcome == OUTCOME_BLOCKED):
        return False
    boundary = result.get(BOUNDARY_KEY)
    if not isinstance(boundary, Mapping):
        return False
    if boundary.get("condition_evaluations") != {
        condition: "NOT_EVALUATED" for condition in REQUIRED_CONDITIONS
    }:
        return False
    if any(
        boundary.get(field) is not False
        for field in (
            "condition_ledger_populated",
            "any_condition_evaluated",
            "later_operation_created",
            "later_operation_executed",
            "later_operation_result_selected",
        )
    ):
        return False
    if result.get("raw_signal_considered_but_not_admitted_posture") != RAW_SIGNAL_POSTURE:
        return False
    if result.get(SUMMARY_KEY) != _summary_from_result(result):
        return False
    if outcome in (OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED):
        if result.get("failed_check_count") != 0:
            return False
        if result.get("lineage_preservation_posture") != _canonical_lineage_posture():
            return False
        evaluations = result.get("admissibility_evaluations")
        if not isinstance(evaluations, Mapping) or any(
            item != ADMISSIBILITY_PASSED for item in evaluations.values()
        ):
            return False
    return True


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return the compact summary projection for a compatible result."""
    if not isinstance(result, Mapping) or not _structural_result_valid(result):
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationBoundaryV0MinError(
            "summary requires a compatible boundary result"
        )
    return copy.deepcopy(_summary_from_result(result))


def _canonical_completed_result_matches(result: Mapping[str, Any]) -> bool:
    if not _structural_result_valid(result) or result.get("outcome") not in (
        OUTCOME_ALLOWED,
        OUTCOME_NOT_ALLOWED,
    ):
        return False
    declared = result.get(DECLARED_REQUEST_KEY)
    if not isinstance(declared, Mapping) or type(declared.get("selection")) is not bool:
        return False
    expected = resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min(
        _new_canonical_request(selected=declared["selection"])
    )
    return _exact_equal(dict(result), expected)


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _output_path_allowed(path: Path) -> bool:
    try:
        resolved = path.resolve()
        root = OUTPUT_ROOT.resolve()
        canonical = (OUTPUT_ROOT / OUTPUT_FILENAME).resolve()
        protected = (
            (REPO_ROOT / "reference").resolve(),
            (REPO_ROOT / "spec").resolve(),
            (REPO_ROOT / "src").resolve(),
            (REPO_ROOT / "tests").resolve(),
            PRIOR_PRESENCE_ARTIFACT_PATH.parent.resolve(),
            SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_PATH.parent.resolve(),
            LATER_MODAL_ARTIFACT_PATH.parent.resolve(),
            PACKET_TEXT_PATHS[0].parent.resolve(),
            (REPO_ROOT / "artifacts/contaminated_lineage").resolve(),
        )
        return (
            OUTPUT_ROOT.name == CANONICAL_OUTPUT_ROOT.name
            and resolved == canonical
            and _path_within(resolved, root)
            and not any(_path_within(resolved, item) for item in protected)
        )
    except (OSError, RuntimeError, TypeError, ValueError):
        return False


def write_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one canonical completed result at the exact no-overwrite path."""
    if not isinstance(result, Mapping) or not _canonical_completed_result_matches(result):
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationBoundaryV0MinError(
            "WRITE_REFUSED: malformed, inconsistent, or noncanonical boundary result"
        )
    try:
        target = (
            _as_repo_path(output_path)
            if output_path is not None
            else OUTPUT_ROOT / OUTPUT_FILENAME
        )
    except (OSError, TypeError, ValueError) as exc:
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationBoundaryV0MinError(
            "WRITE_REFUSED: invalid output path"
        ) from exc
    if not _output_path_allowed(target):
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationBoundaryV0MinError(
            "WRITE_REFUSED: output path is outside the exact canonical result path"
        )
    if target.exists():
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationBoundaryV0MinError(
            "WRITE_REFUSED: canonical result path already exists"
        )
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(
                dict(result),
                handle,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationBoundaryV0MinError(
            "WRITE_REFUSED: unable to write canonical boundary result"
        ) from exc
    return target
