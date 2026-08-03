"""Resolve one bounded body-held ten-condition integrity evaluation operation.

The resolver consumes only the exact frozen basis admitted by the completed
boundary.  It records nine basis-relative support rows and one basis-required
row.  It never reads raw signal or archive bytes and creates no downstream
authority, standing, presence, or automatic route.
"""

from __future__ import annotations

import copy
import hashlib
import json
import math
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinError(
    ValueError
):
    """Raised when a summary or canonical write cannot be completed."""


RESOLVER_MODULE = (
    "resolve_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_v0_min"
)
RESULT_VERSION = "0.1.0"
OPERATION_ID = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_001"
)
OPERATION_TYPE = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_"
    "OPERATION"
)
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = (
    "EVALUATE_AND_RECORD_ONE_HETEROGENEOUS_TEN_CONDITION_MATRIX_FROM_ONE_"
    "FROZEN_BODY_HELD_BASIS_ONLY"
)
SELECTED_MATTER_CLASS = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_REMAINING_TEN_INTEGRITY_"
    "CONDITIONS_ONLY"
)
INTENT_RECORD = (
    "RECORD_BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_OPERATION"
)

OUTCOME_RECORDED = OPERATION_TYPE + "_RECORDED"
OUTCOME_BLOCKED = OPERATION_TYPE + "_BLOCKED"
OUTCOME_FAMILY = (OUTCOME_RECORDED, OUTCOME_BLOCKED)
OPERATION_RESULT_RECORDED = OUTCOME_RECORDED
OPERATION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
OPERATION_RESULT_FAMILY = OUTCOME_FAMILY
RESULT_RECORDED = OPERATION_RESULT_RECORDED
RESULT_NOT_EVALUATED = OPERATION_RESULT_NOT_EVALUATED
RESULT_FAMILY = (RESULT_RECORDED, RESULT_NOT_EVALUATED)
ADMISSIBLE_FUTURE_ROUTE = None

ADMISSIBILITY_PASSED = "PASSED"
ADMISSIBILITY_NOT_EVALUATED = "NOT_EVALUATED"
OPERATION_ADMISSIBILITY_FAMILY = (
    ADMISSIBILITY_PASSED,
    ADMISSIBILITY_NOT_EVALUATED,
)
ADMISSIBILITY_EVALUATION_FAMILY = OPERATION_ADMISSIBILITY_FAMILY

CONDITION_SUPPORTED = "SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS"
CONDITION_REQUIRES_BASIS = "REQUIRES_BASIS"
CONDITION_INDETERMINATE = "INDETERMINATE"
CONDITION_NOT_EVALUATED = "NOT_EVALUATED"
CONDITION_EVALUATION_FAMILY = (
    CONDITION_SUPPORTED,
    CONDITION_REQUIRES_BASIS,
    CONDITION_INDETERMINATE,
    CONDITION_NOT_EVALUATED,
)

BASIS_CUSTODY_DISTINCT = "CUSTODY_DISTINCT_BASIS"
BASIS_EXTERNAL_AUTHENTICITY = "EXTERNAL_AUTHENTICITY_BASIS"
BASIS_OTHER_EXACT_NAMED = "OTHER_EXACT_NAMED_BASIS"
BASIS_NONE = "NONE"
REQUIRED_BASIS_CLASS_FAMILY = (
    BASIS_CUSTODY_DISTINCT,
    BASIS_EXTERNAL_AUTHENTICITY,
    BASIS_OTHER_EXACT_NAMED,
    BASIS_NONE,
)

EVIDENCE_CLASSES = (
    "CUSTODY_AND_CONTROL",
    "EXECUTION_AND_ATTESTATION_FORM",
    "ADVERSARIAL_INTEGRITY_AND_BOUNDED_ADMISSIBILITY",
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
ORDERED_TEN_CONDITION_MATTER = REQUIRED_CONDITIONS
REQUIRED_CONDITION_VALUES = {
    REQUIRED_CONDITIONS[0]: True,
    **{condition: False for condition in REQUIRED_CONDITIONS[1:]},
}
EVIDENCE_CLASS_CONDITION_MAPPING = {
    EVIDENCE_CLASSES[0]: REQUIRED_CONDITIONS[0:2],
    EVIDENCE_CLASSES[1]: REQUIRED_CONDITIONS[2:8],
    EVIDENCE_CLASSES[2]: REQUIRED_CONDITIONS[8:10],
}
HISTORICAL_CONDITION_MATRIX = {
    "receiver_attested": "SATISFIED",
    "receiver_answerable_receipt_present": "SATISFIED",
    "receiver_answerable_basis_custody_distinct": CONDITION_REQUIRES_BASIS,
    "receiver_answerable_basis_controlled_by_declaring_side": CONDITION_REQUIRES_BASIS,
    "receiver_answerable_basis_refusable": CONDITION_REQUIRES_BASIS,
    "receiver_answerable_basis_could_have_been_withheld": CONDITION_REQUIRES_BASIS,
    "repo_local_execution_only": CONDITION_REQUIRES_BASIS,
    "operator_only_attestation": CONDITION_REQUIRES_BASIS,
    "derivative_rendering_attestation": CONDITION_REQUIRES_BASIS,
    "same_custody_countersignature": CONDITION_REQUIRES_BASIS,
    "automatic_acknowledgement": CONDITION_REQUIRES_BASIS,
    "generated_affirmation": CONDITION_REQUIRES_BASIS,
    "forged_receiver_attestation": CONDITION_REQUIRES_BASIS,
    "inadmissible_receiver_basis": CONDITION_REQUIRES_BASIS,
}
HISTORICAL_REQUIRES_BASIS_CONDITIONS = tuple(
    condition
    for condition, posture in HISTORICAL_CONDITION_MATRIX.items()
    if posture == CONDITION_REQUIRES_BASIS
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

DEPENDENCY_CEILING_CONTRACT = (
    {
        "condition_or_family": "same_custody_countersignature",
        "ceiling": "MAY_NOT_OUTRUN_RECEIVER_ANSWERABLE_BASIS_CUSTODY_DISTINCT",
    },
    {
        "condition_or_family": "operator_only_attestation",
        "ceiling": "MAY_NOT_OUTRUN_RECEIVER_ORIGIN_AND_CUSTODY_RELATION_SUPPORT",
    },
    {
        "condition_or_family": "derivative_rendering_attestation",
        "ceiling": "ABSENCE_LIMITED_TO_ADMITTED_SOURCE_BODY_CONDUCT_AND_CARRIED_LINEAGE",
    },
    {
        "condition_or_family": "generated_affirmation",
        "ceiling": "ABSENCE_LIMITED_TO_ADMITTED_SOURCE_BODY_CONDUCT_AND_CARRIED_LINEAGE",
    },
    {
        "condition_or_family": "automatic_acknowledgement",
        "ceiling": "ABSENCE_LIMITED_TO_ADMITTED_MACHINERY_AND_CHRONOLOGY",
    },
    {
        "condition_or_family": "forged_receiver_attestation",
        "ceiling": "MAY_NOT_OUTRUN_CUSTODY_ORIGIN_PRESERVATION_CORRESPONDENCE_AND_EXTERNAL_AUTHENTICITY_BASIS",
    },
    {
        "condition_or_family": "inadmissible_receiver_basis",
        "ceiling": "MAY_NOT_OUTRUN_EXACT_ADMITTED_RELATION_AND_MATTER_SCOPE",
    },
    {
        "condition_or_family": "ALL_NEGATIVE_FORM_CONDITIONS",
        "ceiling": "MAY_NOT_BECOME_UNIVERSAL_ABSENCE",
    },
    {
        "condition_or_family": "ALL_SIBLING_CONDITIONS",
        "ceiling": "NO_SUCCESSFUL_SIBLING_MAY_SILENTLY_STRENGTHEN_ANOTHER",
    },
    {
        "condition_or_family": "ALL_DEPENDENCIES",
        "ceiling": "NO_DEPENDENCY_MAY_BE_BYPASSED",
    },
)

RAW_SIGNAL_POSTURE = {
    "raw_signal_body_known_to_exist": True,
    "raw_signal_body_considered": True,
    "raw_signal_body_admitted": False,
    "raw_signal_body_read_authorized": False,
    "signal_morphology_evaluation_authorized": False,
    "authenticity_upgrade_from_signal_authorized": False,
}
TEMPORAL_EVIDENCE = {
    "knock_generated_at": "2026-07-15T12:08:04Z",
    "receiver_attestation_confirmed_at": "2026-07-28T06:37:56Z",
    "knock_to_receiver_attestation_interval_seconds": 1103392,
    "knock_to_receiver_attestation_interval_components": {
        "days": 12,
        "hours": 18,
        "minutes": 29,
        "seconds": 52,
    },
    "knock_to_receiver_attestation_interval": (
        "12 days, 18 hours, 29 minutes, 52 seconds"
    ),
    "current_clock_used": False,
    "actual_refusal_inferred": False,
    "actual_withholding_inferred": False,
    "receiver_freedom_inferred": False,
    "universal_automation_absence_inferred": False,
}

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_OPERATION_V0_MIN_SPEC.md"
)
GOVERNING_SPECIFICATION_PATH = REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPECIFICATION_SHA256 = (
    "3600cc9cf91c4938952b289119aeafbab53831e5e060d3d0e8abff357f4ba3dc"
)

BOUNDARY_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_BOUNDARY_V0_MIN_SPEC.md"
)
BOUNDARY_SPECIFICATION_PATH = REPO_ROOT / BOUNDARY_SPECIFICATION_RELATIVE_PATH
BOUNDARY_SPECIFICATION_SHA256 = (
    "bc485e14b5da5d72f6702550b237311f367d44b3789c01fdddc45de38bdc3600"
)

BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_held_receiver_"
    "answerable_basis_integrity_condition_evaluation_boundary_v0_min/"
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "boundary_001__body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_boundary_v0_min_result.json"
)
BOUNDARY_ARTIFACT_PATH = REPO_ROOT / BOUNDARY_ARTIFACT_RELATIVE_PATH
BOUNDARY_ARTIFACT_SHA256 = (
    "caeef89956198a47b4d9e3581aafd8d86431c02a22a01531ffe7d4585be417bb"
)
BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH = Path(
    "spec/BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_BOUNDARY_V0_MIN_TERMINAL_SUMMARY.md"
)
BOUNDARY_TERMINAL_SUMMARY_PATH = REPO_ROOT / BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH
BOUNDARY_TERMINAL_SUMMARY_SHA256 = (
    "059bdedcb78aa546367a3393c265c5a2a4dc24d44ca9fab91ad944d7cd621357"
)
CONSUMED_BOUNDARY_ROUTE = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_"
    "BOUNDARY_THEN_SEPARATE_HETEROGENEOUS_TEN_CONDITION_EVALUATION_"
    "OPERATION_ONLY"
)

PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_presence_re_evaluation_"
    "operation_v0_min/presence_re_evaluation_operation_001__presence_re_"
    "evaluation_operation_v0_min_result.json"
)
SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_originating_modal_"
    "fact_source_admissibility_boundary_v0_min/receiver_originating_modal_"
    "fact_source_admissibility_boundary_001__receiver_originating_modal_fact_"
    "source_admissibility_boundary_v0_min_result.json"
)
LATER_MODAL_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_originating_modal_"
    "fact_evaluation_operation_v0_min/receiver_originating_modal_fact_"
    "evaluation_operation_001__receiver_originating_modal_fact_evaluation_"
    "operation_v0_min_result.json"
)
MODAL_TERMINAL_SUMMARY_RELATIVE_PATH = Path(
    "spec/RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_V0_MIN_"
    "TERMINAL_SUMMARY.md"
)
PRIOR_STANDING_RELATIVE_PATHS = (
    PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH,
    SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH,
    LATER_MODAL_ARTIFACT_RELATIVE_PATH,
    MODAL_TERMINAL_SUMMARY_RELATIVE_PATH,
)
PRIOR_STANDING_PATHS = tuple(REPO_ROOT / path for path in PRIOR_STANDING_RELATIVE_PATHS)
(
    PRIOR_PRESENCE_ARTIFACT_PATH,
    SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_PATH,
    LATER_MODAL_ARTIFACT_PATH,
    MODAL_TERMINAL_SUMMARY_PATH,
) = PRIOR_STANDING_PATHS
PRIOR_STANDING_SHA256 = (
    "fa3f05965de18382b48a37d54abeb04ed4e3d4383b8e75c11ccaa1ca07c15776",
    "f24795566eb369ad935e2212aba83ef68bfd1661363cc94da2f53498cc2935ac",
    "5138294e3c9d5f776676afb580b786fc1d6a5518527add7808789be3a744ba57",
    "7ec3f880174f6941340802e2af441aff2b5b163cef4c9efc81d4cb5c887b0682",
)
PRIOR_PRESENCE_SHA256 = PRIOR_STANDING_SHA256[0]
SOURCE_ADMISSIBILITY_BOUNDARY_SHA256 = PRIOR_STANDING_SHA256[1]
LATER_MODAL_SHA256 = PRIOR_STANDING_SHA256[2]
MODAL_TERMINAL_SUMMARY_SHA256 = PRIOR_STANDING_SHA256[3]

CARRIAGE_LINEAGE_RELATIVE_PATHS = (
    Path(
        "artifacts/integrity_host_v0_min_coexistence_receiver_side_"
        "answerable_basis_reception_operation_v0_min/receiver_side_"
        "answerable_basis_reception_operation_001__receiver_side_answerable_"
        "basis_reception_operation_v0_min_result_001.json"
    ),
    Path(
        "artifacts/integrity_host_v0_min_coexistence_receiver_side_"
        "answerable_basis_candidate_evaluation_operation_v0_min_v3/receiver_"
        "side_answerable_basis_candidate_evaluation_operation_001__receiver_"
        "side_answerable_basis_candidate_evaluation_operation_v0_min_v3_"
        "result.json"
    ),
    Path(
        "artifacts/integrity_host_v0_min_coexistence_receiver_side_"
        "answerable_basis_candidate_sufficiency_operation_v0_min/receiver_"
        "side_answerable_basis_candidate_sufficiency_operation_001__receiver_"
        "side_answerable_basis_candidate_sufficiency_operation_v0_min_result_"
        "001.json"
    ),
    Path(
        "artifacts/integrity_host_v0_min_coexistence_receiver_side_"
        "answerable_basis_receiver_attestation_operation_basis_declaration_"
        "v0_min/receiver_side_answerable_basis_receiver_attestation_operation_"
        "basis_declaration_001__receiver_side_answerable_basis_receiver_"
        "attestation_operation_basis_declaration_v0_min_result.json"
    ),
    Path(
        "artifacts/integrity_host_v0_min_coexistence_receiver_side_"
        "answerable_basis_receiver_attestation_operation_basis_supply_v0_min/"
        "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
        "supply_001__receiver_side_answerable_basis_receiver_attestation_"
        "operation_basis_supply_v0_min_result.json"
    ),
    Path(
        "artifacts/integrity_host_v0_min_coexistence_receiver_side_"
        "answerable_basis_receiver_attestation_operation_v0_min/receiver_side_"
        "answerable_basis_receiver_attestation_operation_001__receiver_side_"
        "answerable_basis_receiver_attestation_operation_v0_min_result_001.json"
    ),
    Path(
        "artifacts/integrity_host_v0_min_coexistence_receiver_side_"
        "answerable_basis_receiver_answerable_receipt_operation_v0_min/"
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_"
        "001__receiver_side_answerable_basis_receiver_answerable_receipt_"
        "operation_v0_min_result.json"
    ),
)
CARRIAGE_LINEAGE_PATHS = tuple(REPO_ROOT / path for path in CARRIAGE_LINEAGE_RELATIVE_PATHS)
CARRIAGE_LINEAGE_SHA256 = (
    "722cd329fe85d484bf6e626f42faa034ba23c3b7e9e6196519a2c4c7e609b315",
    "952c08a4ca383f2506fa70ca93e086668511d224ee8c9fd51eb20b44e699fd1b",
    "7271d8cb62ce75fd4c5a42e09775d481edf62dae813790d16f8361c0e06509f4",
    "a60e496a4a53dd1019ab429e6b80fba2d20e1e2829b575fc56de9753ea885d37",
    "9d877d5ce48ec6aa484e649bc54928d692eed62feefe8383169d37f462228325",
    "175821764f0f284311c21968994473ad6157148fae360102540a9e1a237533e9",
    "a80c4d99b3b4d33f9b267989a4696e088e10f25845b536d0b188e1554973dfcb",
)
CANDIDATE_RECEPTION_ARTIFACT_RELATIVE_PATH = CARRIAGE_LINEAGE_RELATIVE_PATHS[0]
CANDIDATE_EVALUATION_ARTIFACT_RELATIVE_PATH = CARRIAGE_LINEAGE_RELATIVE_PATHS[1]
CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH = CARRIAGE_LINEAGE_RELATIVE_PATHS[2]
ATTESTATION_BASIS_DECLARATION_ARTIFACT_RELATIVE_PATH = CARRIAGE_LINEAGE_RELATIVE_PATHS[3]
ATTESTATION_BASIS_SUPPLY_ARTIFACT_RELATIVE_PATH = CARRIAGE_LINEAGE_RELATIVE_PATHS[4]
RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH = CARRIAGE_LINEAGE_RELATIVE_PATHS[5]
RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH = CARRIAGE_LINEAGE_RELATIVE_PATHS[6]
CANDIDATE_RECEPTION_SHA256 = CARRIAGE_LINEAGE_SHA256[0]
CANDIDATE_EVALUATION_SHA256 = CARRIAGE_LINEAGE_SHA256[1]
CANDIDATE_SUFFICIENCY_SHA256 = CARRIAGE_LINEAGE_SHA256[2]
ATTESTATION_BASIS_DECLARATION_SHA256 = CARRIAGE_LINEAGE_SHA256[3]
ATTESTATION_BASIS_SUPPLY_SHA256 = CARRIAGE_LINEAGE_SHA256[4]
RECEIVER_ATTESTATION_SHA256 = CARRIAGE_LINEAGE_SHA256[5]
RECEIVER_ANSWERABLE_RECEIPT_SHA256 = CARRIAGE_LINEAGE_SHA256[6]

PACKET_TEXT_BASE = Path(
    "artifacts/actual_receiver_attestation_capture/receiver_attestation_"
    "capture_001/extracted/receiver_attestation_001"
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
        "capture_tool_description=macimu-based reader of the Apple SPU accelerometer, 5.0 s window, full rate\n"
        "capture_gesture=two knocks of the receiver's wrist on the MacBook palm rest\n"
        "capture_recorded_at=2026-07-27T21:50:57+02:00\n"
        "capture_declared_by_receiver=true\n"
    ),
    "attested_at=2026-07-28T06:37:56Z\n",
    "knock knock back",
    (
        "knock_result_path=artifacts/integrity_host_v0_min_coexistence_presence_operation_v0_min/presence_operation_001__presence_operation_v0_min_result.json\n"
        "knock_outcome=PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION\n"
        "knock_result_sha256=7cab32728cef1bf8de9d1ec544188f155c6564832678d74b501fdccb3e4111d3\n"
        "knock_generated_at=2026-07-15T12:08:04Z\n"
        "source_body_commit=ef640316263d8c8036946d75393df624185308a1\n"
        "knock_reference_note=This receipt answers exactly one knock: the presence operation identified above, and nothing else.\n"
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

SOURCE_BODY_CONDUCT_RELATIVE_PATHS = (
    Path("spec/PRESENCE_OPERATION_V0_MIN_SPEC.md"),
    Path("src/resolve_presence_operation_v0_min.py"),
    Path(
        "artifacts/integrity_host_v0_min_coexistence_presence_operation_v0_min/"
        "presence_operation_001__presence_operation_v0_min_result.json"
    ),
    Path("spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_V0_MIN_SPEC.md"),
    Path("src/resolve_receiver_side_answerable_basis_reception_boundary_v0_min.py"),
    Path(
        "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
        "basis_reception_boundary_v0_min_v2/receiver_side_answerable_basis_"
        "reception_boundary_001__receiver_side_answerable_basis_reception_"
        "boundary_v0_min_v2_result.json"
    ),
    Path("spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_V0_MIN_SPEC.md"),
    Path("src/resolve_receiver_side_answerable_basis_reception_operation_v0_min.py"),
    CARRIAGE_LINEAGE_RELATIVE_PATHS[0],
)
SOURCE_BODY_CONDUCT_PATHS = tuple(REPO_ROOT / path for path in SOURCE_BODY_CONDUCT_RELATIVE_PATHS)
SOURCE_BODY_CONDUCT_SHA256 = (
    "58f75c47294d90dab10a2b6388dfd142f71181e1a1101bedf91c4fe3c1895ad6",
    "c8e8414938e806359c0256e1cd6b425fda0d3b3621b4bcf6c3deb20406cb876a",
    "7cab32728cef1bf8de9d1ec544188f155c6564832678d74b501fdccb3e4111d3",
    "fbb1fde665ac7f85d3224c3d2538a0b8586f61feb988ab87a9230708a1e890d5",
    "f4bf39090ad24afb33d366764eac2f03dd38a54dc0a9ce6a1a34b9d753779446",
    "3ac18bec045113cc58b02b0140cb2db3e550851fb0dd7c42463603517bbf5120",
    "7da57e73084210037f7ed86f7b8094c126549187dc43d89455bc5ddefd161444",
    "b7ff6c9b44083b97b801373ab0e0abd279069de2d725942cda1f372edae0d596",
    CARRIAGE_LINEAGE_SHA256[0],
)

CANONICAL_OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_body_held_receiver_"
    "answerable_basis_integrity_condition_evaluation_operation_v0_min"
)
OUTPUT_ROOT = CANONICAL_OUTPUT_ROOT
OUTPUT_FILENAME = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_001__body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_v0_min_result.json"
)
DETERMINISTIC_FILENAME = OUTPUT_FILENAME

EXCLUDED_READ_CONTRACT = (
    "raw_signal_json",
    "original_zip_or_archive_bytes",
    "archive_extraction",
    "complete_bounded_capture_signal_body",
    "complete_candidate_body",
    "complete_candidate_evaluation_material_beyond_compact_result",
    "filesystem_permissions_or_acl_data",
    "device_control_records",
    "private_communications",
    "broad_git_or_pr_history",
    "sibling_discovery_or_latest_file_selection",
    "alternative_source_search_or_source_reconstruction",
    "glob_rglob_or_directory_scan",
    "unrelated_receiver_side_material",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "all_ten_conditions_established_as_reality_wide_facts",
    "receiver_attested_reevaluated",
    "receiver_answerable_receipt_present_reevaluated",
    "receiver_answerable_basis_refusable_reevaluated",
    "receiver_answerable_basis_could_have_been_withheld_reevaluated",
    "actual_refusal_established",
    "actual_withholding_established",
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
    "threshold_machinery_created",
    "truth_settlement_created",
    "field_machinery_created",
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
    "evaluation_operation_permission_created",
    "reusable_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_route_created",
    "same_body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_rerun_authorized",
    "automatic_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_retry_created",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_debt_created",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_obligation_created",
    "scheduled_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_created",
    "automatic_next_step_created",
    "repair_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforcement_performed",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "raw_signal_body_admitted",
    "raw_signal_body_read_authorized",
    "signal_morphology_evaluation_authorized",
    "authenticity_upgrade_from_signal_authorized",
    "later_operation_created",
    "later_operation_executed",
    "later_operation_result_selected",
    "prior_artifact_overwritten",
    "prior_condition_posture_overwritten",
    "source_naturalized",
    "jurisdiction_collapsed",
)

LINEAGE_PRESERVATION_FIELDS = (
    "boundary_result_preserved",
    "boundary_route_consumed_by_this_operation_only",
    "prior_presence_result_preserved",
    "historical_fourteen_condition_matrix_preserved",
    "prior_twelve_requires_basis_rows_preserved",
    "later_refusability_support_preserved",
    "later_withholdability_support_preserved",
    "both_modal_establishment_fields_remain_false",
    "receiver_originating_relation_preserved",
    "carried_arrival_remains_non_native",
    "source_not_naturalized",
    "jurisdiction_not_collapsed",
    "all_seven_carriage_lineage_surfaces_preserved",
    "all_eight_packet_text_surfaces_preserved_as_bounded_evidence",
    "all_nine_conduct_surfaces_preserved_as_bounded_source_body_evidence",
    "raw_signal_remains_non_admitted",
    "no_prior_artifact_repaired_invalidated_superseded_normalized_replaced_or_overwritten",
    "contaminated_lineage_unchanged",
)
OMISSION_POSTURE_FIELDS = (
    "complete_upstream_artifact_bodies_omitted",
    "complete_candidate_body_omitted",
    "complete_candidate_evaluation_body_omitted",
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
)
NON_MEANING_FIELDS = (
    "prior_requires_basis_standing_is_not_failure",
    "boundary_permission_is_not_condition_support",
    "operation_recording_is_not_universal_establishment",
    "body_held_support_is_not_reality_wide_truth",
    "custody_relation_support_is_not_custody_proof",
    "declared_provenance_is_not_proven_provenance",
    "receiver_label_is_not_receiver_identity",
    "admitted_record_relative_absence_is_not_universal_absence",
    "internal_consistency_is_not_non_forgery",
    "hashes_prove_preservation_not_authorship",
    "source_body_non_prescription_is_not_no_external_pressure",
    "source_body_non_generation_is_not_no_external_generation",
    "bounded_admissibility_is_not_global_admissibility",
    "supported_sibling_does_not_strengthen_another_automatically",
    "dependency_ceiling_is_not_condition_denial",
    "requires_basis_is_not_failure",
    "condition_level_basis_requirement_does_not_block_recorded_heterogeneous_operation",
    "considered_evidence_is_not_admitted_evidence",
    "raw_signal_existence_is_not_read_permission",
    "condition_evaluation_is_not_complete_receiver_answerable_basis",
    "operation_exhaustion_is_not_complete_receiver_answerable_basis",
    "operation_exhaustion_is_not_presence",
    "open_does_not_mean_next",
)
BLOCKED_CONVERSIONS = (
    "BOUNDARY_PERMISSION_TO_CONDITION_SUPPORT",
    "BODY_HELD_SUPPORT_TO_REALITY_WIDE_ESTABLISHMENT",
    "CUSTODY_RELATION_TO_CUSTODY_PROOF_OR_RECEIVER_IDENTITY",
    "DECLARED_PROVENANCE_TO_PROVEN_PROVENANCE",
    "INTERNAL_CONSISTENCY_OR_HASH_TO_NON_FORGERY_OR_AUTHORSHIP",
    "ADMITTED_RECORD_RELATIVE_ABSENCE_TO_UNIVERSAL_ABSENCE",
    "BOUNDED_ADMISSIBILITY_TO_GLOBAL_RECEIVER_BASIS_ADMISSIBILITY",
    "RAW_SIGNAL_EXISTENCE_TO_READ_MORPHOLOGY_OR_AUTHENTICITY_UPGRADE",
    "SUPPORTED_SIBLING_TO_STRONGER_SIBLING_POSTURE",
    "CONDITION_EVALUATION_TO_COMPLETE_RECEIVER_ANSWERABLE_BASIS",
    "OPERATION_EXHAUSTION_TO_COMPLETE_BASIS_PRESENCE_TRUTH_OR_AUTHORITY",
    "OPERATION_RESULT_TO_REPEAT_RETRY_DEBT_OBLIGATION_SCHEDULE_OR_AUTOMATIC_NEXT",
    "OPERATION_RESULT_TO_REPAIR_SCAN_DISCOVERY_VALIDATION_OR_RECONSTRUCTION",
)
WHAT_REMAINS_OPEN = (
    "operation_tests",
    "operation_request",
    "operation_live_result",
    "operation_terminal_summary",
    "external_authenticity_basis",
    "cryptographic_receiver_identity",
    "raw_signal_morphology_under_separate_admission",
    "complete_receiver_answerable_basis",
    "later_presence_re_evaluation",
    "presence_support_authorization_establishment_and_recording",
    "threshold",
    "truth_settlement",
    "identity",
    "custody_proof",
    "provenance_proof",
    "physical_validity",
    "authority",
    "truth",
    "standing",
    "relation",
    "coupling",
    "field_machinery",
    "runtime",
    "api",
    "public_interface",
    "public_intake",
    "output",
    "action",
    "derivative_reception",
    "synchronization",
    "repair",
    "validation",
    "follow_on_work",
)

SPEC_REQUIRED_MARKERS = (
    (
        "title",
        "# Body-Held Receiver-Answerable-Basis Integrity-Condition Evaluation Operation V0 Minimum Specification",
    ),
    ("operation_id", f"`body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_id = {OPERATION_ID}`"),
    ("operation_type", f"`body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_type = {OPERATION_TYPE}`"),
    ("operation_scope", f"`body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_scope = {OPERATION_SCOPE}`"),
    ("matter_class", f"`selected_matter_class = {SELECTED_MATTER_CLASS}`"),
    ("boundary_digest", BOUNDARY_ARTIFACT_SHA256),
    ("boundary_terminal_digest", BOUNDARY_TERMINAL_SUMMARY_SHA256),
    ("condition_supported", f"`{CONDITION_SUPPORTED}`"),
    ("condition_requires_basis", f"`{CONDITION_REQUIRES_BASIS}`"),
    ("condition_indeterminate", f"`{CONDITION_INDETERMINATE}`"),
    ("condition_not_evaluated", f"`{CONDITION_NOT_EVALUATED}`"),
    ("external_authenticity", f"`{BASIS_EXTERNAL_AUTHENTICITY}`"),
    ("recorded", f"`{OUTCOME_RECORDED}`"),
    ("blocked", f"`{OUTCOME_BLOCKED}`"),
    ("raw_signal_not_admitted", "`raw_signal_body_admitted = false`"),
    ("future_route", "`admissible_future_route = null`"),
    ("nonclaims", "## 15. Required False Non-Claims"),
    ("closing_lock", "## 18. Closing Lock"),
)

PROHIBITED_DIRECT_REQUEST_FIELDS = frozenset(
    {
        *REQUIRED_CONDITIONS,
        "condition_evaluations",
        "condition_results",
        "condition_ledger",
        "operation_result",
        "successor_condition_posture",
        "compact_support_boolean",
        "semantic_payload",
        "raw_signal_body",
        "raw_signal_content",
        "archive_bytes",
        "zip_bytes",
        "complete_candidate_body",
        "complete_candidate_evaluation_body",
        "custody_proof",
        "receiver_identity",
        "provenance_proof",
        "physical_validity_proof",
        "non_forgery_claim",
        "universal_absence",
        "global_admissibility",
        "complete_receiver_answerable_basis",
        "presence",
        "truth",
        "standing",
        "authority",
        "output",
        "action",
        "admissible_future_route",
        "automatic_next",
        "glob",
        "rglob",
        "scan",
        "discovery",
        "repair",
        "replacement",
        "normalization",
        "reconstruction",
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
        "REQUEST_TYPE_MISMATCH",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "RESULT_POSTURE_PRECLAIMED",
        "SPECIFICATION_MISSING_OR_UNREADABLE",
        "SPECIFICATION_DIGEST_MISMATCH",
        "SPECIFICATION_INVALID",
        "BOUNDARY_SPECIFICATION_MISSING_OR_UNREADABLE",
        "BOUNDARY_SPECIFICATION_DIGEST_MISMATCH",
        "BOUNDARY_SPECIFICATION_INVALID",
        "BOUNDARY_ARTIFACT_MISSING_OR_UNREADABLE",
        "BOUNDARY_ARTIFACT_DIGEST_MISMATCH",
        "BOUNDARY_ARTIFACT_INVALID",
        "BOUNDARY_ROUTE_INVALID",
        "BOUNDARY_TERMINAL_SUMMARY_MISSING_OR_UNREADABLE",
        "BOUNDARY_TERMINAL_SUMMARY_DIGEST_MISMATCH",
        "BOUNDARY_TERMINAL_SUMMARY_INVALID",
        "PRIOR_STANDING_SURFACE_MISSING_OR_UNREADABLE",
        "PRIOR_STANDING_SURFACE_DIGEST_MISMATCH",
        "PRIOR_STANDING_SURFACE_INVALID",
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
        "EXCLUDED_READ_REQUESTED",
        "RAW_SIGNAL_POSTURE_INVALID",
        "TEMPORAL_EVIDENCE_INVALID",
        "MATTER_CONTRACT_INVALID",
        "LEDGER_CONTRACT_INVALID",
        "DEPENDENCY_CEILING_INVALID",
        "AGGREGATE_MATRIX_INVALID",
        "ADMISSIBILITY_BLOCKED",
        "LINEAGE_PRESERVATION_INVALID",
        "OMISSION_POSTURE_INVALID",
    }
)

DECLARED_REQUEST_KEY = (
    "declared_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_request"
)
OPERATION_KEY = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation"
)
CHECKS_KEY = OPERATION_KEY + "_checks"
SUMMARY_KEY = OPERATION_KEY + "_summary"
STATEMENT_KEY = OPERATION_KEY + "_statement"
NON_MEANING_KEY = OPERATION_KEY + "_non_meaning"
METADATA_KEY = OPERATION_KEY + "_metadata"


def _refs(*values: str) -> list[str]:
    return list(values)


def _row(
    condition_id: str,
    evidence_class: str,
    references: Sequence[str],
    fields: Sequence[str],
    proposition: str,
    limitation: str,
    dependencies: Sequence[str],
    ceiling: str,
    *,
    posture: str = CONDITION_SUPPORTED,
    basis: str = BASIS_NONE,
    compact: bool | None = True,
    candidates: Sequence[str] = (),
) -> dict[str, Any]:
    return {
        "condition_id": condition_id,
        "required_value": REQUIRED_CONDITION_VALUES[condition_id],
        "prior_condition_posture": CONDITION_REQUIRES_BASIS,
        "evidence_class": evidence_class,
        "permitted_artifact_references": list(references),
        "supporting_fields_or_bytes": list(fields),
        "support_proposition": proposition,
        "limitation": limitation,
        "dependency_conditions": list(dependencies),
        "dependency_ceiling": ceiling,
        "candidate_evidence_considered_but_not_admitted": list(candidates),
        "evaluation_posture": posture,
        "required_basis_class": basis,
        "compact_support_boolean": compact,
        "successor_condition_posture": posture,
        "prior_posture_preserved": True,
        "no_overwrite": True,
    }


_PACKET = tuple(str(path) for path in PACKET_TEXT_RELATIVE_PATHS)
_CARRIAGE = tuple(str(path) for path in CARRIAGE_LINEAGE_RELATIVE_PATHS)
_CONDUCT = tuple(str(path) for path in SOURCE_BODY_CONDUCT_RELATIVE_PATHS)

EXPECTED_CONDITION_LEDGER = (
    _row(
        REQUIRED_CONDITIONS[0], EVIDENCE_CLASSES[0],
        _refs(_PACKET[0], _PACKET[1], str(SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH), *_CARRIAGE),
        _refs("exact path, digest, byte-count, custody-relation, source-origin, carried-arrival, non-naturalization, jurisdiction, identity, correspondence, completion, and omission records"),
        "the admitted records support a distinct receiver-side custody relation from the source-body repository",
        "this is not proof of exclusive custody, filesystem permissions, access control, device ownership, or absence of shared control",
        (),
        "support remains limited to admitted custody-relation and carriage records",
    ),
    _row(
        REQUIRED_CONDITIONS[1], EVIDENCE_CLASSES[0],
        _refs(_PACKET[6], *_CONDUCT),
        _refs("prescribed_by_declaring_side=false", "attestation_words_authored_by_receiver_only=true", "no recorded outbound prescription, named-recipient solicitation, reminder, retry, polling, automatic intake, or generated semantic response"),
        "declaring-side prescription or control is not supported by the admitted receiver declaration and source-body conduct records",
        "this does not prove absence of private communication, informal influence, external pressure, undisclosed coordination, or pre-sealing editing",
        (REQUIRED_CONDITIONS[0],),
        "may not outrun receiver-origin, custody-relation support, receiver declaration, or bounded source-body conduct",
    ),
    _row(
        REQUIRED_CONDITIONS[2], EVIDENCE_CLASSES[1],
        _refs(_PACKET[0], _PACKET[1], *_CARRIAGE),
        _refs("exact receiver working-directory and capture-method bytes", "compact carried-arrival chronology and correspondence fields"),
        "the admitted lineage contains receiver-side execution outside the IAMMAI-SYSTEM repository, so repo-local-only execution is not supported",
        "this does not prove that no preparatory, replay, copied, or externally dependent step occurred elsewhere",
        (REQUIRED_CONDITIONS[0],),
        "support remains limited to exact declared receiver-side paths, capture metadata, and carried-arrival chronology",
    ),
    _row(
        REQUIRED_CONDITIONS[3], EVIDENCE_CLASSES[1],
        _refs(str(SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH), _PACKET[1], _PACKET[3], _PACKET[5], _PACKET[6], *_CARRIAGE),
        _refs("receiver-originating source relation", "exact receiver statement surfaces", "exact capture-method and capture-only surfaces", "compact custody and carriage correspondence fields"),
        "an operator-only source-body attestation is not supported because the admitted lineage carries receiver-originating statement and physical-response capture metadata",
        "this does not establish the legal, biological, cryptographic, or exclusive identity of the receiver, or prove absence of another unseen author",
        (REQUIRED_CONDITIONS[0], "receiver-originating source relation"),
        "MAY_NOT_OUTRUN_RECEIVER_ORIGIN_AND_CUSTODY_RELATION_SUPPORT",
    ),
    _row(
        REQUIRED_CONDITIONS[4], EVIDENCE_CLASSES[1],
        _refs(str(SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH), *_CARRIAGE, *_CONDUCT),
        _refs("compact receiver-origin, carried-arrival, non-naturalization, carriage, and source-body conduct fields"),
        "derivative rendering by the source body is not supported in the admitted source-body and carried lineage",
        "this does not prove absence of off-repo DI assistance, external generation, copied wording, replay, or synthesis before capture",
        ("receiver-originating source relation", "carried arrival", "bounded source-body conduct"),
        "ABSENCE_LIMITED_TO_ADMITTED_SOURCE_BODY_CONDUCT_AND_CARRIED_LINEAGE",
    ),
    _row(
        REQUIRED_CONDITIONS[5], EVIDENCE_CLASSES[1],
        _refs(_PACKET[0], str(SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH), *_CARRIAGE),
        _refs("row 1 custody-relation support", "receiver-origin fields", "compact carriage correspondence"),
        "same-custody countersignature is not supported by the admitted custody-relation, receiver-origin, and carriage records",
        "this does not prove absence of shared credentials, undeclared common control, shared filesystem access, or hidden replication",
        (REQUIRED_CONDITIONS[0],),
        "MAY_NOT_OUTRUN_RECEIVER_ANSWERABLE_BASIS_CUSTODY_DISTINCT",
    ),
    _row(
        REQUIRED_CONDITIONS[6], EVIDENCE_CLASSES[1],
        _refs(_PACKET[2], _PACKET[4], _PACKET[6], *_CONDUCT),
        _refs("knock_generated_at=2026-07-15T12:08:04Z", "confirmed_by_receiver_at=2026-07-28T06:37:56Z", "knock_to_receiver_attestation_interval_seconds=1103392", "bounded source-body machinery fields"),
        "automatic acknowledgement is not supported by the admitted source-body machinery or the admitted response chronology",
        "this does not prove absence of external automation, macros, scripts, scheduling, or systems outside the admitted record domain",
        ("admitted source-body machinery", "admitted chronology", "receiver-originating modal support"),
        "ABSENCE_LIMITED_TO_ADMITTED_MACHINERY_AND_CHRONOLOGY",
    ),
    _row(
        REQUIRED_CONDITIONS[7], EVIDENCE_CLASSES[1],
        _refs(str(SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH), _PACKET[3], _PACKET[5], _PACKET[6], *_CARRIAGE, *_CONDUCT),
        _refs("receiver-origin, carried-lineage, exact receiver-statement, and source-body generated-semantic-content posture"),
        "source-body-generated affirmation is not supported by the admitted body-held records",
        "this does not prove absence of external generation, external DI assistance, copied wording, or synthesis before capture",
        ("receiver-originating source relation", "bounded source-body conduct"),
        "ABSENCE_LIMITED_TO_ADMITTED_SOURCE_BODY_CONDUCT_AND_CARRIED_LINEAGE",
    ),
    _row(
        REQUIRED_CONDITIONS[8], EVIDENCE_CLASSES[2],
        _refs(str(SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH), *_CARRIAGE),
        _refs("compact custody, receiver-origin, preservation, digest, identity-correspondence, candidate-correspondence, and carriage fields"),
        "admitted hashes, lineage, identity correspondence, and compact records support preservation and internal consistency but do not lawfully establish non-forgery",
        "cryptographic receiver signature, trusted device attestation, independent witness, exclusive key control, and proof against pre-hash fabrication remain outside body custody",
        (REQUIRED_CONDITIONS[0], "receiver-originating source relation", "preservation integrity", "candidate correspondence", "external authenticity"),
        "MAY_NOT_OUTRUN_CUSTODY_ORIGIN_PRESERVATION_CORRESPONDENCE_AND_EXTERNAL_AUTHENTICITY_BASIS",
        posture=CONDITION_REQUIRES_BASIS,
        basis=BASIS_EXTERNAL_AUTHENTICITY,
        compact=None,
        candidates=("raw accelerometer signal body exists", "potential signal-morphology relevance recognized", "raw signal not admitted", "raw signal not read", "no morphology evaluation", "no authenticity upgrade"),
    ),
    _row(
        REQUIRED_CONDITIONS[9], EVIDENCE_CLASSES[2],
        _refs(str(SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH), *_CARRIAGE),
        _refs("compact completed-result, exact-admission, relation, matter, identity-correspondence, preservation, and omission fields"),
        "inadmissibility is not supported for the exact matters and operations in which the receiver basis was already admitted",
        "this does not establish admissibility for identity, custody proof, provenance proof, physical validity, other jurisdictions, future presence, or any newly named matter",
        ("completed bounded reception", "candidate evaluation", "candidate sufficiency", "attestation basis declaration", "attestation basis supply", "attestation operation", "receipt operation", "source admissibility", "exact present matter"),
        "MAY_NOT_OUTRUN_EXACT_ADMITTED_RELATION_AND_MATTER_SCOPE",
    ),
)
EXPECTED_CONDITION_ROWS = EXPECTED_CONDITION_LEDGER

EXPECTED_AGGREGATE_MATRIX_POSTURE = {
    "ordered_condition_count": 10,
    "supported_by_admitted_body_held_records_count": 9,
    "requires_basis_count": 1,
    "indeterminate_count": 0,
    "not_evaluated_count": 0,
    "compact_support_true_count": 9,
    "compact_support_false_count": 0,
    "compact_support_null_count": 1,
    "prior_posture_preserved_count": 10,
    "no_overwrite_count": 10,
    "evidence_class_count": 3,
    "dependency_ceiling_count": 10,
    "all_ten_conditions_evaluated": True,
    "condition_ledger_populated": True,
    "condition_result_count": 10,
    "requires_basis_conditions": ["forged_receiver_attestation"],
    "requires_basis_classes": [BASIS_EXTERNAL_AUTHENTICITY],
}


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_lineage_posture(completed: bool) -> dict[str, bool]:
    return {field: completed for field in LINEAGE_PRESERVATION_FIELDS}


def _canonical_omission_posture() -> dict[str, bool]:
    return {
        **{field: True for field in OMISSION_POSTURE_FIELDS},
        "complete_material_omission_posture": True,
    }


def _canonical_non_meaning() -> dict[str, bool]:
    return {field: True for field in NON_MEANING_FIELDS}


def _frozen_read_contract() -> dict[str, Any]:
    return {
        "governing_specification": {
            "path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
            "sha256": GOVERNING_SPECIFICATION_SHA256,
        },
        "completed_boundary_specification": {
            "path": str(BOUNDARY_SPECIFICATION_RELATIVE_PATH),
            "sha256": BOUNDARY_SPECIFICATION_SHA256,
        },
        "completed_boundary": {
            "path": str(BOUNDARY_ARTIFACT_RELATIVE_PATH),
            "sha256": BOUNDARY_ARTIFACT_SHA256,
        },
        "boundary_terminal_summary": {
            "path": str(BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH),
            "sha256": BOUNDARY_TERMINAL_SUMMARY_SHA256,
        },
        "prior_standing_paths": [str(path) for path in PRIOR_STANDING_RELATIVE_PATHS],
        "prior_standing_sha256": list(PRIOR_STANDING_SHA256),
        "carriage_lineage_paths": [str(path) for path in CARRIAGE_LINEAGE_RELATIVE_PATHS],
        "carriage_lineage_sha256": list(CARRIAGE_LINEAGE_SHA256),
        "receiver_packet_text_paths": [str(path) for path in PACKET_TEXT_RELATIVE_PATHS],
        "receiver_packet_text_sha256": list(PACKET_TEXT_SHA256),
        "receiver_packet_text_byte_counts": list(PACKET_TEXT_BYTE_COUNTS),
        "source_body_conduct_paths": [str(path) for path in SOURCE_BODY_CONDUCT_RELATIVE_PATHS],
        "source_body_conduct_sha256": list(SOURCE_BODY_CONDUCT_SHA256),
        "read_contract_closed": True,
        "filesystem_discovery_permitted": False,
        "latest_file_selection_permitted": False,
        "source_reconstruction_permitted": False,
    }


def _identity_request_values() -> dict[str, Any]:
    return {
        "intent": INTENT_RECORD,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_id": OPERATION_ID,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_type": OPERATION_TYPE,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_version": OPERATION_VERSION,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_scope": OPERATION_SCOPE,
        "governing_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "governing_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_specification_sha256": GOVERNING_SPECIFICATION_SHA256,
        "completed_boundary_specification_path": str(BOUNDARY_SPECIFICATION_RELATIVE_PATH),
        "completed_boundary_specification_sha256": BOUNDARY_SPECIFICATION_SHA256,
        "completed_boundary_artifact_path": str(BOUNDARY_ARTIFACT_RELATIVE_PATH),
        "completed_boundary_artifact_sha256": BOUNDARY_ARTIFACT_SHA256,
        "boundary_terminal_summary_path": str(BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH),
        "boundary_terminal_summary_sha256": BOUNDARY_TERMINAL_SUMMARY_SHA256,
        "consumed_boundary_route": CONSUMED_BOUNDARY_ROUTE,
        "prior_standing_paths": [str(path) for path in PRIOR_STANDING_RELATIVE_PATHS],
        "prior_standing_sha256": list(PRIOR_STANDING_SHA256),
        "carriage_lineage_paths": [str(path) for path in CARRIAGE_LINEAGE_RELATIVE_PATHS],
        "carriage_lineage_sha256": list(CARRIAGE_LINEAGE_SHA256),
        "receiver_packet_text_paths": [str(path) for path in PACKET_TEXT_RELATIVE_PATHS],
        "receiver_packet_text_sha256": list(PACKET_TEXT_SHA256),
        "receiver_packet_text_byte_counts": list(PACKET_TEXT_BYTE_COUNTS),
        "source_body_conduct_paths": [str(path) for path in SOURCE_BODY_CONDUCT_RELATIVE_PATHS],
        "source_body_conduct_sha256": list(SOURCE_BODY_CONDUCT_SHA256),
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "ordered_ten_condition_matter": list(REQUIRED_CONDITIONS),
        "required_condition_values": copy.deepcopy(REQUIRED_CONDITION_VALUES),
        "evidence_class_family": list(EVIDENCE_CLASSES),
        "evidence_class_condition_mapping": {
            key: list(value) for key, value in EVIDENCE_CLASS_CONDITION_MAPPING.items()
        },
        "condition_evaluation_family": list(CONDITION_EVALUATION_FAMILY),
        "required_basis_class_family": list(REQUIRED_BASIS_CLASS_FAMILY),
        "operation_result_family": list(OPERATION_RESULT_FAMILY),
        "condition_ledger_field_order": list(CONDITION_LEDGER_SCHEMA_FIELDS),
        "dependency_ceiling_contract": copy.deepcopy(list(DEPENDENCY_CEILING_CONTRACT)),
        "frozen_read_contract": _frozen_read_contract(),
        "excluded_read_contract": list(EXCLUDED_READ_CONTRACT),
        "raw_signal_posture": copy.deepcopy(RAW_SIGNAL_POSTURE),
        "temporal_evidence": copy.deepcopy(TEMPORAL_EVIDENCE),
        "expected_condition_ledger": copy.deepcopy(list(EXPECTED_CONDITION_LEDGER)),
        "expected_aggregate_matrix_posture": copy.deepcopy(EXPECTED_AGGREGATE_MATRIX_POSTURE),
    }


def _new_canonical_request() -> dict[str, Any]:
    return {**_identity_request_values(), "declared_non_claims": _canonical_non_claims()}


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_request() -> dict[str, Any]:
    """Return one fresh canonical operation request."""
    return copy.deepcopy(_new_canonical_request())


def build_declared_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Return a canonical request while retaining each caller override visibly."""
    request = _new_canonical_request()
    request.update(copy.deepcopy(overrides))
    return request


def _reject_constant(value: str) -> Any:
    raise ValueError("non-finite JSON number: " + value)


def _pairs_without_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def _parse_json_bytes(payload: bytes) -> tuple[Any | None, str | None]:
    if payload.startswith(b"\xef\xbb\xbf"):
        return None, "UTF-8 BOM is not allowed"
    try:
        text = payload.decode("utf-8", errors="strict")
        value = json.loads(
            text,
            object_pairs_hook=_pairs_without_duplicates,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        return None, str(exc)
    return value, None


def _read_bytes(path: Path | str) -> tuple[bytes | None, str | None]:
    try:
        supplied = Path(path)
        if not supplied.is_file():
            return None, "not a regular file"
        return supplied.read_bytes(), None
    except (OSError, TypeError, ValueError) as exc:
        return None, str(exc)


def _read_json(path: Path | str) -> tuple[Mapping[str, Any] | None, bytes | None, str | None]:
    payload, error = _read_bytes(path)
    if error is not None or payload is None:
        return None, payload, error
    value, error = _parse_json_bytes(payload)
    if error is not None or not isinstance(value, Mapping):
        return None, payload, error or "top-level JSON value is not an object"
    return value, payload, None


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _exact(actual: Any, expected: Any) -> bool:
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, float):
        return math.isfinite(actual) and actual == expected
    if isinstance(expected, Mapping):
        return set(actual) == set(expected) and all(
            _exact(actual[key], expected[key]) for key in expected
        )
    if isinstance(expected, (list, tuple)):
        return len(actual) == len(expected) and all(
            _exact(left, right) for left, right in zip(actual, expected)
        )
    return actual == expected


def _get_path(value: Mapping[str, Any], path: Sequence[str]) -> Any:
    current: Any = value
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return None
        current = current[key]
    return current


def _block_is_clear(value: Mapping[str, Any]) -> bool:
    block = value.get("block")
    return (
        isinstance(block, Mapping)
        and block.get("blocked") is False
        and block.get("code") is None
        and block.get("block_code") is None
    )


def _check(
    check_id: str,
    passed: bool,
    code: str | None = None,
    *,
    expected: Any = None,
) -> dict[str, Any]:
    failure = None if passed else code
    return {
        "check_id": check_id,
        "passed": passed,
        "block_code": failure,
        "failure_code": failure,
        "expected": copy.deepcopy(expected),
    }


def _add_check(
    checks: list[dict[str, Any]],
    check_id: str,
    passed: bool,
    code: str,
    *,
    expected: Any = None,
) -> bool:
    checks.append(_check(check_id, passed, code, expected=expected))
    return passed


def _canonical_false_mapping(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS)
    )


def _validate_request(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None]:
    direct = set(request).intersection(PROHIBITED_DIRECT_REQUEST_FIELDS)
    if direct:
        _add_check(checks, "request.result_or_semantic_preclaim", False, "RESULT_POSTURE_PRECLAIMED")
        return "RESULT_POSTURE_PRECLAIMED", "request contains a result, excluded read, or downstream semantic preclaim"
    expected = _new_canonical_request()
    missing = set(expected).difference(request)
    unknown = set(request).difference(expected)
    if missing:
        _add_check(checks, "request.schema.missing", False, "REQUEST_FIELD_MISSING", expected=sorted(expected))
        return "REQUEST_FIELD_MISSING", "canonical request fields are missing"
    if unknown:
        _add_check(checks, "request.schema.unknown", False, "REQUEST_UNKNOWN_FIELD", expected=sorted(expected))
        return "REQUEST_UNKNOWN_FIELD", "request contains unknown fields"
    _add_check(checks, "request.schema", True, "REQUEST_VALUE_MISMATCH", expected="exact canonical keys")
    for field, expected_value in _identity_request_values().items():
        actual = request.get(field)
        if not _exact(actual, expected_value):
            code = "REQUEST_TYPE_MISMATCH" if type(actual) is not type(expected_value) else "REQUEST_VALUE_MISMATCH"
            _add_check(checks, "request." + field, False, code, expected=expected_value)
            return code, field + " does not match the canonical operation request"
        _add_check(checks, "request." + field, True, "REQUEST_VALUE_MISMATCH", expected=expected_value)
    if not _canonical_false_mapping(request.get("declared_non_claims")):
        _add_check(checks, "request.declared_non_claims", False, "NON_CLAIM_MISSING_OR_FLIPPED", expected=False)
        return "NON_CLAIM_MISSING_OR_FLIPPED", "declared non-claims must be the exact canonical false set"
    _add_check(checks, "request.declared_non_claims", True, "NON_CLAIM_MISSING_OR_FLIPPED", expected=False)
    return None, None


def _empty_validation(relative_path: Path, digest: str) -> dict[str, Any]:
    return {
        "surface_path": str(relative_path),
        "expected_sha256": digest,
        "observed_sha256": None,
        "strict_content_validated": False,
        "surface_validated": False,
        "complete_body_omitted": True,
    }


def _load_pinned_json(
    path: Path | str,
    relative_path: Path,
    digest: str,
    prefix: str,
    code_prefix: str,
    checks: list[dict[str, Any]],
) -> tuple[Mapping[str, Any] | None, dict[str, Any], str | None, str | None]:
    validation = _empty_validation(relative_path, digest)
    value, payload, error = _read_json(path)
    if error is not None or payload is None or value is None:
        code = code_prefix + "_MISSING_OR_UNREADABLE"
        _add_check(checks, prefix + ".strict_json", False, code)
        return None, validation, code, prefix + " is missing, unreadable, malformed, duplicate-keyed, or not an object"
    observed = _sha256(payload)
    validation["observed_sha256"] = observed
    if not _add_check(checks, prefix + ".sha256", observed == digest, code_prefix + "_DIGEST_MISMATCH", expected=digest):
        return None, validation, code_prefix + "_DIGEST_MISMATCH", prefix + " digest mismatch"
    _add_check(checks, prefix + ".strict_json", True, code_prefix + "_INVALID", expected="strict duplicate-key-free object")
    validation["strict_content_validated"] = True
    return value, validation, None, None


def _validate_specification(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_validation(GOVERNING_SPECIFICATION_RELATIVE_PATH, GOVERNING_SPECIFICATION_SHA256)
    validation["marker_validation"] = {name: False for name, _ in SPEC_REQUIRED_MARKERS}
    payload, error = _read_bytes(path)
    if error is not None or payload is None:
        _add_check(checks, "specification.readable", False, "SPECIFICATION_MISSING_OR_UNREADABLE")
        return "SPECIFICATION_MISSING_OR_UNREADABLE", "governing specification is missing or unreadable", validation
    observed = _sha256(payload)
    validation["observed_sha256"] = observed
    if not _add_check(checks, "specification.sha256", observed == GOVERNING_SPECIFICATION_SHA256, "SPECIFICATION_DIGEST_MISMATCH", expected=GOVERNING_SPECIFICATION_SHA256):
        return "SPECIFICATION_DIGEST_MISMATCH", "governing specification digest mismatch", validation
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        _add_check(checks, "specification.utf8", False, "SPECIFICATION_INVALID")
        return "SPECIFICATION_INVALID", "governing specification is not strict UTF-8", validation
    for name, marker in SPEC_REQUIRED_MARKERS:
        valid = marker in text
        validation["marker_validation"][name] = valid
        if not _add_check(checks, "specification.marker." + name, valid, "SPECIFICATION_INVALID", expected=marker):
            return "SPECIFICATION_INVALID", "governing specification marker is missing: " + name, validation
    validation.update({"strict_content_validated": True, "surface_validated": True, "specification_validated": True})
    return None, None, validation


def _validate_boundary(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    value, validation, code, reason = _load_pinned_json(
        path, BOUNDARY_ARTIFACT_RELATIVE_PATH, BOUNDARY_ARTIFACT_SHA256,
        "boundary_artifact", "BOUNDARY_ARTIFACT", checks,
    )
    if code is not None or value is None:
        return code, reason, validation
    boundary = value.get("body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary")
    posture = value.get("boundary_posture")
    admissibility = value.get("admissibility_evaluations")
    decision = value.get("boundary_decision")
    expected_posture = {
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_recorded": True,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_result_recorded": True,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_consideration_allowed": True,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_consideration_not_allowed": False,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_exhausted": True,
        "completed_consideration_posture_count": 1,
        "single_use_only": True,
    }
    valid = (
        value.get("resolver_module") == "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min"
        and value.get("result_version") == "0.1.0"
        and value.get("outcome") == "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_BOUNDARY_ALLOWED"
        and value.get("boundary_result") == "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_CONSIDERATION_ALLOWED"
        and value.get("passed_check_count") == 188
        and value.get("failed_check_count") == 0
        and _block_is_clear(value)
        and isinstance(decision, Mapping)
        and decision.get("decision_code") == "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_ALLOWED"
        and decision.get("selection") is True
        and isinstance(posture, Mapping)
        and all(posture.get(key) is expected for key, expected in expected_posture.items())
        and isinstance(admissibility, Mapping)
        and all(admissibility.get(key) == ADMISSIBILITY_PASSED for key in (
            "source_and_record_basis_admissibility_evaluation",
            "scope_and_matter_admissibility_evaluation",
            "transition_admissibility_evaluation",
        ))
        and isinstance(boundary, Mapping)
        and boundary.get("boundary_id") == "body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_001"
        and boundary.get("boundary_type") == "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_BOUNDARY"
        and boundary.get("boundary_version") == "0.1.0"
        and boundary.get("boundary_scope") == "CONSIDER_ONE_HETEROGENEOUS_BODY_HELD_EVALUATION_OF_TEN_REMAINING_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITIONS_ONLY"
        and boundary.get("selected_matter_class") == SELECTED_MATTER_CLASS
        and boundary.get("body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_result") == "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_CONSIDERATION_ALLOWED"
        and boundary.get("condition_evaluations") == {condition: CONDITION_NOT_EVALUATED for condition in REQUIRED_CONDITIONS}
        and boundary.get("condition_ledger_populated") is False
        and boundary.get("later_operation_result_selected") is False
        and boundary.get("later_operation_created") is False
        and boundary.get("later_operation_executed") is False
        and boundary.get("raw_signal_body_admitted") is False
        and boundary.get("raw_signal_body_read_authorized") is False
        and boundary.get("signal_morphology_evaluation_authorized") is False
        and boundary.get("authenticity_upgrade_from_signal_authorized") is False
        and _get_path(value, ("frozen_read_contract_posture", "read_contract_closed")) is True
    )
    if not _add_check(checks, "boundary_artifact.exact_allowed_standing", valid, "BOUNDARY_ARTIFACT_INVALID"):
        return "BOUNDARY_ARTIFACT_INVALID", "completed boundary standing is invalid", validation
    route_valid = value.get("admissible_future_route") == CONSUMED_BOUNDARY_ROUTE and boundary.get("admissible_future_route") == CONSUMED_BOUNDARY_ROUTE
    if not _add_check(checks, "boundary_artifact.consumed_route", route_valid, "BOUNDARY_ROUTE_INVALID", expected=CONSUMED_BOUNDARY_ROUTE):
        return "BOUNDARY_ROUTE_INVALID", "completed boundary route is absent or changed", validation
    validation.update({"boundary_identity_validated": True, "allowed_result_validated": True, "single_use_route_validated": True, "surface_validated": True, "artifact_validated": True})
    return None, None, validation


def _validate_boundary_specification(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    """Validate the exact completed-boundary specification as frozen law."""
    return _validate_text_surface(
        path,
        BOUNDARY_SPECIFICATION_RELATIVE_PATH,
        BOUNDARY_SPECIFICATION_SHA256,
        (
            "# Body-Held Receiver-Answerable-Basis Integrity-Condition Evaluation Boundary V0 Minimum Specification",
            "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_BOUNDARY",
            CONSUMED_BOUNDARY_ROUTE,
            "raw_signal_body_admitted = false",
        ),
        "boundary_specification",
        "BOUNDARY_SPECIFICATION",
        checks,
    )


def _validate_text_surface(
    path: Path | str,
    relative_path: Path,
    digest: str,
    markers: Sequence[str],
    prefix: str,
    code_prefix: str,
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_validation(relative_path, digest)
    payload, error = _read_bytes(path)
    if error is not None or payload is None:
        code = code_prefix + "_MISSING_OR_UNREADABLE"
        _add_check(checks, prefix + ".readable", False, code)
        return code, prefix + " is missing or unreadable", validation
    observed = _sha256(payload)
    validation["observed_sha256"] = observed
    if not _add_check(checks, prefix + ".sha256", observed == digest, code_prefix + "_DIGEST_MISMATCH", expected=digest):
        return code_prefix + "_DIGEST_MISMATCH", prefix + " digest mismatch", validation
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        _add_check(checks, prefix + ".utf8", False, code_prefix + "_INVALID")
        return code_prefix + "_INVALID", prefix + " is not strict UTF-8", validation
    valid = not payload.startswith(b"\xef\xbb\xbf") and all(marker in text for marker in markers)
    if not _add_check(checks, prefix + ".standing", valid, code_prefix + "_INVALID"):
        return code_prefix + "_INVALID", prefix + " standing is invalid", validation
    validation.update({"strict_content_validated": True, "surface_validated": True})
    return None, None, validation


def _validate_boundary_terminal(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    return _validate_text_surface(
        path,
        BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH,
        BOUNDARY_TERMINAL_SUMMARY_SHA256,
        (
            "# Body-Held Receiver-Answerable-Basis Integrity-Condition Evaluation Boundary V0 Minimum Terminal Summary",
            "outcome = BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_BOUNDARY_ALLOWED",
            CONSUMED_BOUNDARY_ROUTE,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_exhausted = true",
        ),
        "boundary_terminal_summary",
        "BOUNDARY_TERMINAL_SUMMARY",
        checks,
    )


def _validate_prior_standing(
    paths: Sequence[Path | str], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, list[dict[str, Any]]]:
    validations: list[dict[str, Any]] = []
    if len(paths) != 4:
        _add_check(checks, "prior_standing.path_count", False, "READ_CONTRACT_INVALID", expected=4)
        return "READ_CONTRACT_INVALID", "prior standing path count is invalid", validations

    json_values: list[Mapping[str, Any]] = []
    for index, name in enumerate(("prior_presence", "source_admissibility", "later_modal")):
        value, validation, code, reason = _load_pinned_json(
            paths[index],
            PRIOR_STANDING_RELATIVE_PATHS[index],
            PRIOR_STANDING_SHA256[index],
            "prior_standing." + name,
            "PRIOR_STANDING_SURFACE",
            checks,
        )
        validations.append(validation)
        if code is not None or value is None:
            return code, reason, validations
        json_values.append(value)

    presence, source, modal = json_values
    presence_operation = presence.get("presence_re_evaluation_operation")
    presence_posture = presence.get("operation_posture")
    presence_evaluations = presence.get("condition_evaluations")
    presence_valid = (
        presence.get("resolver_module") == "resolve_presence_re_evaluation_operation_v0_min"
        and presence.get("result_version") == "0.1.0"
        and presence.get("outcome") == "PRESENCE_RE_EVALUATION_OPERATION_REQUIRES_RECEIVER_ANSWERABLE_BASIS"
        and presence.get("presence_re_evaluation_operation_result") == "REQUIRES_RECEIVER_ANSWERABLE_BASIS"
        and presence.get("successor_presence_result") == "REQUIRES_RECEIVER_ANSWERABLE_BASIS"
        and presence.get("failed_check_count") == 0
        and presence.get("passed_check_count") == 409
        and _block_is_clear(presence)
        and isinstance(presence_posture, Mapping)
        and presence_posture.get("operation_basis_admitted") is True
        and presence_posture.get("presence_re_evaluation_performed") is True
        and presence_posture.get("presence_re_evaluation_operation_exhausted") is True
        and presence_posture.get("completed_successor_result_posture_count") == 1
        and presence.get("admissible_future_route") is None
        and isinstance(presence_evaluations, Mapping)
        and set(presence_evaluations) == set(HISTORICAL_CONDITION_MATRIX)
        and all(
            isinstance(presence_evaluations.get(condition), Mapping)
            and presence_evaluations[condition].get("evaluation") == expected
            for condition, expected in HISTORICAL_CONDITION_MATRIX.items()
        )
        and isinstance(presence_operation, Mapping)
        and all(
            presence_operation.get(field) is False
            for field in (
                "presence_supported",
                "presence_authorized",
                "presence_established",
                "presence_recorded",
            )
        )
    )
    if not _add_check(checks, "prior_standing.prior_presence.exact_standing", presence_valid, "PRIOR_STANDING_SURFACE_INVALID"):
        return "PRIOR_STANDING_SURFACE_INVALID", "prior presence standing is invalid", validations
    validations[0].update({"identity_completion_matrix_and_false_locks_validated": True, "surface_validated": True})

    source_boundary = source.get("receiver_originating_modal_fact_source_admissibility_boundary")
    source_lineage = source.get("lineage_preservation_posture")
    source_admissibility = source.get("admissibility_evaluations")
    source_valid = (
        source.get("resolver_module") == "resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min"
        and source.get("result_version") == "0.1.0"
        and source.get("outcome") == "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_ALLOWED"
        and source.get("boundary_result") == "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_CONSIDERATION_ALLOWED"
        and source.get("failed_check_count") == 0
        and source.get("passed_check_count") == 308
        and _block_is_clear(source)
        and isinstance(source_boundary, Mapping)
        and all(
            _exact(source_boundary.get(field), expected)
            for field, expected in {
                "source_selection_recorded": True,
                "receiver_originating_modal_fact_source_admissibility_boundary_recorded": True,
                "receiver_originating_modal_fact_source_admissibility_boundary_result_recorded": True,
                "receiver_originating_modal_fact_source_admissibility_boundary_exhausted": True,
                "completed_consideration_posture_count": 1,
                "selected_source_native_standing": False,
                "jurisdiction_distinction_preserved": True,
            }.items()
        )
        and source_boundary.get("selected_source_origin") == "RECEIVER_ORIGINATING"
        and source_boundary.get("selected_source_arrival_posture") == "CARRIED_ARRIVAL"
        and isinstance(source_admissibility, Mapping)
        and set(source_admissibility) == {
            "source_admissibility_evaluation",
            "scope_and_matter_admissibility_evaluation",
            "transition_admissibility_evaluation",
        }
        and all(value == ADMISSIBILITY_PASSED for value in source_admissibility.values())
        and isinstance(source_lineage, Mapping)
        and all(
            source_lineage.get(field) is True
            for field in (
                "selected_source_remains_receiver_originating",
                "source_relation_remains_legible",
                "carried_arrival_remains_non_native",
                "source_not_naturalized",
                "jurisdiction_not_collapsed",
            )
        )
        and source.get("admissible_future_route") == (
            "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_"
            "THEN_SEPARATE_RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_"
            "OPERATION_ONLY"
        )
    )
    if not _add_check(checks, "prior_standing.source_admissibility.exact_standing", source_valid, "PRIOR_STANDING_SURFACE_INVALID"):
        return "PRIOR_STANDING_SURFACE_INVALID", "source-admissibility standing is invalid", validations
    validations[1].update({"identity_completion_source_relation_and_route_validated": True, "surface_validated": True})

    modal_operation = modal.get("receiver_originating_modal_fact_evaluation_operation")
    modal_posture = modal.get("operation_posture")
    modal_excluded = modal.get("excluded_condition_posture")
    modal_lineage = modal.get("lineage_preservation_posture")
    modal_valid = (
        modal.get("resolver_module") == "resolve_receiver_originating_modal_fact_evaluation_operation_v0_min"
        and modal.get("result_version") == "0.1.0"
        and modal.get("outcome") == "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_SUPPORTED"
        and modal.get("operation_result") == "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_SUPPORTED"
        and modal.get("failed_check_count") == 0
        and modal.get("passed_check_count") == 378
        and _block_is_clear(modal)
        and isinstance(modal_posture, Mapping)
        and modal_posture.get("operation_basis_supplied") is True
        and modal_posture.get("operation_basis_admitted") is True
        and modal_posture.get("receiver_originating_modal_fact_evaluation_performed") is True
        and modal_posture.get("receiver_originating_modal_fact_evaluation_operation_exhausted") is True
        and modal_posture.get("completed_modal_fact_evaluation_result_posture_count") == 1
        and modal.get("admissible_future_route") is None
        and isinstance(modal_operation, Mapping)
        and modal_operation.get("receiver_answerable_basis_refusable_evaluation") == "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE"
        and modal_operation.get("receiver_answerable_basis_could_have_been_withheld_evaluation") == "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE"
        and modal_operation.get("receiver_answerable_basis_refusable_supported") is True
        and modal_operation.get("receiver_answerable_basis_could_have_been_withheld_supported") is True
        and modal_operation.get("receiver_answerable_basis_refusable_established") is False
        and modal_operation.get("receiver_answerable_basis_could_have_been_withheld_established") is False
        and all(modal_operation.get(field) is False for field in ("presence_supported", "presence_authorized", "presence_established", "presence_recorded"))
        and isinstance(modal_excluded, Mapping)
        and modal_excluded.get("excluded_condition_evaluation_performed") is False
        and modal_excluded.get("excluded_conditions_not_evaluated") is True
        and modal_excluded.get("condition_evaluations") == {condition: CONDITION_NOT_EVALUATED for condition in REQUIRED_CONDITIONS}
        and isinstance(modal_lineage, Mapping)
        and all(modal_lineage.get(field) is True for field in ("prior_presence_requires_basis_result_preserved", "source_admissibility_boundary_result_preserved", "source_not_naturalized", "jurisdiction_not_collapsed", "contaminated_lineage_unchanged"))
    )
    if not _add_check(checks, "prior_standing.later_modal.exact_standing", modal_valid, "PRIOR_STANDING_SURFACE_INVALID"):
        return "PRIOR_STANDING_SURFACE_INVALID", "later modal standing is invalid", validations
    validations[2].update({"identity_completion_support_without_establishment_and_exclusions_validated": True, "surface_validated": True})

    code, reason, terminal_validation = _validate_text_surface(
        paths[3],
        MODAL_TERMINAL_SUMMARY_RELATIVE_PATH,
        MODAL_TERMINAL_SUMMARY_SHA256,
        (
            "# Receiver-Originating Modal Fact Evaluation Operation V0 Minimum Terminal Summary",
            "terminal_status = RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_COMPLETED_SUPPORTED",
            "outcome = RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_SUPPORTED",
            "passed_check_count = 378",
            "receiver_answerable_basis_refusable_established = false",
            "receiver_answerable_basis_could_have_been_withheld_established = false",
            "open does not mean next",
        ),
        "prior_standing.modal_terminal",
        "PRIOR_STANDING_SURFACE",
        checks,
    )
    validations.append(terminal_validation)
    if code is not None:
        return code, reason, validations
    return None, None, validations


def _validate_carriage_lineage(
    paths: Sequence[Path | str], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, list[dict[str, Any]]]:
    contracts = (
        (
            "candidate_reception",
            "resolve_receiver_side_answerable_basis_reception_operation_v0_min",
            "0.1.0",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED",
            105,
            "receiver_side_answerable_basis_reception_operation",
            (
                (("operation_result_detail", "result"), "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEIVED"),
                (("receiver_side_answerable_basis_reception_operation", "receiver_side_answerable_basis_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
                (("receiver_side_answerable_basis_reception_operation", "receiver_side_answerable_basis_reception_operation_result_recorded"), True),
            ),
        ),
        (
            "candidate_evaluation",
            "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3",
            "0.2.0",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_RECORDED",
            152,
            "receiver_side_answerable_basis_candidate_evaluation_operation",
            (
                (("operation_result_detail", "operation_result"), "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED"),
                (("operation_result_detail", "candidate_evaluation_operation_exhausted"), True),
                (("receiver_side_answerable_basis_candidate_evaluation_operation_basis", "candidate_structural_correspondence", "selected_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        ),
        (
            "candidate_sufficiency",
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min",
            "0.1.0",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_RECORDED",
            140,
            "receiver_side_answerable_basis_candidate_sufficiency_operation",
            (
                (("operation_result_detail", "operation_result"), "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"),
                (("receiver_side_answerable_basis_candidate_sufficiency_operation", "candidate_sufficiency_operation_exhausted"), True),
                (("receiver_side_answerable_basis_candidate_sufficiency_operation", "receiver_side_answerable_basis_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        ),
        (
            "receiver_attestation_operation_basis_declaration",
            "resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min",
            "0.1.0",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_DECLARED",
            55,
            "receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration",
            (
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration", "declaration_result"), "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARED"),
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration", "declaration_exhausted"), True),
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration", "receiver_side_answerable_basis_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        ),
        (
            "receiver_attestation_operation_basis_supply",
            "resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min",
            "0.1.0",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_SUPPLY_SUPPLIED",
            101,
            "receiver_side_answerable_basis_receiver_attestation_operation_basis_supply",
            (
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_supply", "supply_result"), "RECEIVER_ATTESTATION_OPERATION_BASIS_SUPPLIED"),
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_supply", "supply_exhausted"), True),
                (("receiver_side_answerable_basis_receiver_attestation_operation_basis_supply", "receiver_side_answerable_basis_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        ),
        (
            "receiver_attestation_operation",
            "resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min",
            "0.1.0",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_RECORDED",
            160,
            "receiver_side_answerable_basis_receiver_attestation_operation",
            (
                (("operation_result_detail", "operation_result"), "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"),
                (("operation_result_detail", "completed_result_posture_count"), 1),
                (("operation_posture", "operation_exhausted"), True),
                (("selected_operation_and_candidate_identity", "selected_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        ),
        (
            "receiver_answerable_receipt_operation",
            "resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min",
            "0.1.0",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RECORDED",
            357,
            "receiver_side_answerable_basis_receiver_answerable_receipt_operation",
            (
                (("operation_result",), "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_RECORDED"),
                (("operation_posture", "completed_result_posture_count"), 1),
                (("operation_posture", "receiver_answerable_receipt_operation_exhausted"), True),
                (("selected_operation_and_candidate_identity", "selected_candidate_id"), "receiver_side_answerable_basis_candidate_001"),
            ),
        ),
    )
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
    validations: list[dict[str, Any]] = []
    if len(paths) != 7:
        _add_check(checks, "carriage_lineage.path_count", False, "READ_CONTRACT_INVALID", expected=7)
        return "READ_CONTRACT_INVALID", "carriage lineage path count is invalid", validations
    for index, (path, relative, digest, contract) in enumerate(zip(paths, CARRIAGE_LINEAGE_RELATIVE_PATHS, CARRIAGE_LINEAGE_SHA256, contracts)):
        name, module, version, outcome, passed_count, primary_key, required_paths = contract
        prefix = "carriage_lineage." + name
        value, validation, code, reason = _load_pinned_json(path, relative, digest, prefix, "CARRIAGE_LINEAGE_ARTIFACT", checks)
        validations.append(validation)
        if code is not None or value is None:
            return code, reason, validations
        primary = value.get(primary_key)
        identity_and_result = (
            value.get("resolver_module") == module
            and value.get("result_version") == version
            and value.get("outcome") == outcome
            and value.get("failed_check_count") == 0
            and value.get("passed_check_count") == passed_count
            and _block_is_clear(value)
        )
        compact = all(_exact(_get_path(value, field_path), expected) for field_path, expected in required_paths)
        false_locks = isinstance(primary, Mapping) and all(primary.get(field) is False for field in required_false_locks)
        correspondence = True
        if index == 0:
            correspondence = (
                isinstance(primary, Mapping)
                and primary.get("candidate_source_provenance_reference_supplied") is True
                and primary.get("declared_source_provenance_reference_to_verified_provenance") is False
            )
        valid = identity_and_result and compact and false_locks and correspondence
        if not _add_check(checks, prefix + ".identity_completion_correspondence_and_false_locks", valid, "CARRIAGE_LINEAGE_ARTIFACT_INVALID"):
            return "CARRIAGE_LINEAGE_ARTIFACT_INVALID", "carriage lineage standing is invalid", validations
        validation.update({"identity_and_completion_validated": True, "correspondence_validated": True, "false_locks_validated": True, "surface_validated": True, "artifact_validated": True})
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
    if len(paths) != 8:
        _add_check(checks, "packet_text.path_count", False, "READ_CONTRACT_INVALID", expected=8)
        return "READ_CONTRACT_INVALID", "packet text path count is invalid", validations
    for path, relative, digest, byte_count, expected_text in zip(paths, PACKET_TEXT_RELATIVE_PATHS, PACKET_TEXT_SHA256, PACKET_TEXT_BYTE_COUNTS, PACKET_TEXT_CONTENTS):
        name = relative.name
        validation = _empty_validation(relative, digest)
        validation.update({"expected_byte_count": byte_count, "observed_byte_count": None, "bom_absent": False, "exact_content_validated": False, "duplicate_record_keys_absent": False})
        validations.append(validation)
        payload, error = _read_bytes(path)
        if error is not None or payload is None:
            _add_check(checks, "packet_text." + name + ".readable", False, "PACKET_TEXT_MISSING_OR_UNREADABLE")
            return "PACKET_TEXT_MISSING_OR_UNREADABLE", name + " is missing or unreadable", validations
        observed = _sha256(payload)
        validation["observed_sha256"] = observed
        validation["observed_byte_count"] = len(payload)
        if not _add_check(checks, "packet_text." + name + ".sha256", observed == digest, "PACKET_TEXT_DIGEST_MISMATCH", expected=digest):
            return "PACKET_TEXT_DIGEST_MISMATCH", name + " digest mismatch", validations
        try:
            text = payload.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            _add_check(checks, "packet_text." + name + ".utf8", False, "PACKET_TEXT_INVALID")
            return "PACKET_TEXT_INVALID", name + " is not strict UTF-8", validations
        exact = len(payload) == byte_count and text == expected_text and not payload.startswith(b"\xef\xbb\xbf")
        if name == "attestation_statement.txt":
            records_valid = text == "knock knock back"
        else:
            _, records_valid = _parse_exact_records(text)
        if not _add_check(checks, "packet_text." + name + ".exact_bytes", exact, "PACKET_TEXT_INVALID", expected=byte_count):
            return "PACKET_TEXT_INVALID", name + " exact content is invalid", validations
        if not _add_check(checks, "packet_text." + name + ".record_set", records_valid, "PACKET_TEXT_INVALID"):
            return "PACKET_TEXT_INVALID", name + " record set is invalid", validations
        validation.update({"strict_content_validated": True, "surface_validated": True, "bom_absent": True, "exact_content_validated": True, "duplicate_record_keys_absent": True})
    return None, None, validations


def _validate_conduct_surfaces(
    paths: Sequence[Path | str], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, list[dict[str, Any]]]:
    contracts = (
        ("text", "# Presence Operation"),
        ("text", 'RESOLVER_MODULE = "resolve_presence_operation_v0_min"'),
        ("json", "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION"),
        ("text", "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY"),
        ("text", "resolve_receiver_side_answerable_basis_reception_boundary_v0_min"),
        ("json", "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_ALLOWED"),
        ("text", "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION"),
        ("text", 'RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_reception_operation_v0_min"'),
        ("json", "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED"),
    )
    validations: list[dict[str, Any]] = []
    if len(paths) != 9:
        _add_check(checks, "source_body_conduct.path_count", False, "READ_CONTRACT_INVALID", expected=9)
        return "READ_CONTRACT_INVALID", "source-body conduct path count is invalid", validations
    for index, (path, relative, digest, contract) in enumerate(zip(paths, SOURCE_BODY_CONDUCT_RELATIVE_PATHS, SOURCE_BODY_CONDUCT_SHA256, contracts)):
        kind, marker = contract
        prefix = "source_body_conduct." + str(index + 1)
        if kind == "text":
            code, reason, validation = _validate_text_surface(path, relative, digest, (marker,), prefix, "SOURCE_BODY_CONDUCT_SURFACE", checks)
        else:
            value, validation, code, reason = _load_pinned_json(path, relative, digest, prefix, "SOURCE_BODY_CONDUCT_SURFACE", checks)
            if code is None and value is not None:
                valid = value.get("outcome") == marker and _block_is_clear(value)
                if not _add_check(checks, prefix + ".standing", valid, "SOURCE_BODY_CONDUCT_SURFACE_INVALID", expected=marker):
                    code, reason = "SOURCE_BODY_CONDUCT_SURFACE_INVALID", "source-body conduct standing is invalid"
                else:
                    validation["surface_validated"] = True
        validations.append(validation)
        if code is not None:
            return code, reason, validations
    return None, None, validations


def _derive_aggregate(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    postures = [row.get("evaluation_posture") for row in rows]
    compact = [row.get("compact_support_boolean") for row in rows]
    return {
        "ordered_condition_count": len(rows),
        "supported_by_admitted_body_held_records_count": postures.count(CONDITION_SUPPORTED),
        "requires_basis_count": postures.count(CONDITION_REQUIRES_BASIS),
        "indeterminate_count": postures.count(CONDITION_INDETERMINATE),
        "not_evaluated_count": postures.count(CONDITION_NOT_EVALUATED),
        "compact_support_true_count": sum(value is True for value in compact),
        "compact_support_false_count": sum(value is False for value in compact),
        "compact_support_null_count": sum(value is None for value in compact),
        "prior_posture_preserved_count": sum(row.get("prior_posture_preserved") is True for row in rows),
        "no_overwrite_count": sum(row.get("no_overwrite") is True for row in rows),
        "evidence_class_count": len({row.get("evidence_class") for row in rows}),
        "dependency_ceiling_count": len(rows),
        "all_ten_conditions_evaluated": len(rows) == 10 and CONDITION_NOT_EVALUATED not in postures,
        "condition_ledger_populated": len(rows) == 10,
        "condition_result_count": len(rows),
        "requires_basis_conditions": [row.get("condition_id") for row in rows if row.get("evaluation_posture") == CONDITION_REQUIRES_BASIS],
        "requires_basis_classes": [row.get("required_basis_class") for row in rows if row.get("evaluation_posture") == CONDITION_REQUIRES_BASIS],
    }


def _validate_contracts(checks: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    matter_valid = (
        len(REQUIRED_CONDITIONS) == 10
        and list(REQUIRED_CONDITION_VALUES) == list(REQUIRED_CONDITIONS)
        and REQUIRED_CONDITION_VALUES[REQUIRED_CONDITIONS[0]] is True
        and all(REQUIRED_CONDITION_VALUES[item] is False for item in REQUIRED_CONDITIONS[1:])
        and tuple(item for evidence_class in EVIDENCE_CLASSES for item in EVIDENCE_CLASS_CONDITION_MAPPING[evidence_class]) == REQUIRED_CONDITIONS
    )
    if not _add_check(checks, "contract.exact_matter", matter_valid, "MATTER_CONTRACT_INVALID"):
        return "MATTER_CONTRACT_INVALID", "ordered matter, required values, or evidence classes are invalid"
    ledger = list(EXPECTED_CONDITION_LEDGER)
    ledger_valid = (
        [row.get("condition_id") for row in ledger] == list(REQUIRED_CONDITIONS)
        and len({row.get("condition_id") for row in ledger}) == 10
        and all(tuple(row) == CONDITION_LEDGER_SCHEMA_FIELDS for row in ledger)
        and all(row.get("prior_condition_posture") == CONDITION_REQUIRES_BASIS for row in ledger)
        and all(row.get("prior_posture_preserved") is True and row.get("no_overwrite") is True for row in ledger)
        and all(not row.get("candidate_evidence_considered_but_not_admitted") for row in ledger if row.get("condition_id") != "forged_receiver_attestation")
        and ledger[8]["candidate_evidence_considered_but_not_admitted"] == ["raw accelerometer signal body exists", "potential signal-morphology relevance recognized", "raw signal not admitted", "raw signal not read", "no morphology evaluation", "no authenticity upgrade"]
    )
    if not _add_check(checks, "contract.exact_ledger", ledger_valid, "LEDGER_CONTRACT_INVALID"):
        return "LEDGER_CONTRACT_INVALID", "exact ten-row ledger contract is invalid"
    for index, row in enumerate(ledger, start=1):
        row_valid = (
            tuple(row) == CONDITION_LEDGER_SCHEMA_FIELDS
            and row.get("condition_id") == REQUIRED_CONDITIONS[index - 1]
            and _exact(
                row.get("required_value"),
                REQUIRED_CONDITION_VALUES[REQUIRED_CONDITIONS[index - 1]],
            )
            and row.get("prior_condition_posture") == CONDITION_REQUIRES_BASIS
            and row.get("prior_posture_preserved") is True
            and row.get("no_overwrite") is True
        )
        if not _add_check(
            checks,
            f"contract.condition_row.{index}.{row.get('condition_id')}",
            row_valid,
            "LEDGER_CONTRACT_INVALID",
        ):
            return "LEDGER_CONTRACT_INVALID", "one exact condition row is invalid"
    ceilings_valid = len(DEPENDENCY_CEILING_CONTRACT) == 10 and len({(item["condition_or_family"], item["ceiling"]) for item in DEPENDENCY_CEILING_CONTRACT}) == 10
    if not _add_check(checks, "contract.dependency_ceilings", ceilings_valid, "DEPENDENCY_CEILING_INVALID"):
        return "DEPENDENCY_CEILING_INVALID", "dependency-ceiling contract is invalid"
    for index, ceiling in enumerate(DEPENDENCY_CEILING_CONTRACT, start=1):
        if not _add_check(
            checks,
            f"contract.dependency_ceiling.{index}.{ceiling['condition_or_family']}",
            set(ceiling) == {"condition_or_family", "ceiling"}
            and bool(ceiling["condition_or_family"])
            and bool(ceiling["ceiling"]),
            "DEPENDENCY_CEILING_INVALID",
        ):
            return "DEPENDENCY_CEILING_INVALID", "one dependency ceiling is invalid"
    aggregate = _derive_aggregate(ledger)
    if not _add_check(checks, "contract.aggregate_matrix", _exact(aggregate, EXPECTED_AGGREGATE_MATRIX_POSTURE), "AGGREGATE_MATRIX_INVALID", expected=EXPECTED_AGGREGATE_MATRIX_POSTURE):
        return "AGGREGATE_MATRIX_INVALID", "derived aggregate matrix does not match the governing contract"
    if not _add_check(checks, "contract.raw_signal_non_admission", _exact(RAW_SIGNAL_POSTURE, {"raw_signal_body_known_to_exist": True, "raw_signal_body_considered": True, "raw_signal_body_admitted": False, "raw_signal_body_read_authorized": False, "signal_morphology_evaluation_authorized": False, "authenticity_upgrade_from_signal_authorized": False}), "RAW_SIGNAL_POSTURE_INVALID"):
        return "RAW_SIGNAL_POSTURE_INVALID", "raw-signal non-admission posture is invalid"
    temporal_valid = TEMPORAL_EVIDENCE["knock_to_receiver_attestation_interval_seconds"] == 1103392 and TEMPORAL_EVIDENCE["current_clock_used"] is False and all(TEMPORAL_EVIDENCE[key] is False for key in ("actual_refusal_inferred", "actual_withholding_inferred", "receiver_freedom_inferred", "universal_automation_absence_inferred"))
    if not _add_check(checks, "contract.temporal_evidence", temporal_valid, "TEMPORAL_EVIDENCE_INVALID"):
        return "TEMPORAL_EVIDENCE_INVALID", "fixed temporal evidence contract is invalid"
    _add_check(checks, "contract.excluded_reads", True, "EXCLUDED_READ_REQUESTED", expected=list(EXCLUDED_READ_CONTRACT))
    _add_check(checks, "contract.nonclaims", _canonical_false_mapping(_canonical_non_claims()), "NON_CLAIM_MISSING_OR_FLIPPED", expected=False)
    return None, None


def _empty_aggregate() -> dict[str, Any]:
    return {
        "ordered_condition_count": 10,
        "supported_by_admitted_body_held_records_count": 0,
        "requires_basis_count": 0,
        "indeterminate_count": 0,
        "not_evaluated_count": 10,
        "compact_support_true_count": 0,
        "compact_support_false_count": 0,
        "compact_support_null_count": 0,
        "prior_posture_preserved_count": 0,
        "no_overwrite_count": 0,
        "evidence_class_count": 3,
        "dependency_ceiling_count": 10,
        "all_ten_conditions_evaluated": False,
        "condition_ledger_populated": False,
        "condition_result_count": 0,
        "requires_basis_conditions": [],
        "requires_basis_classes": [],
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get(OPERATION_KEY)
    operation = operation if isinstance(operation, Mapping) else {}
    posture = result.get("operation_posture")
    posture = posture if isinstance(posture, Mapping) else {}
    aggregate = result.get("aggregate_matrix_posture")
    aggregate = aggregate if isinstance(aggregate, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    admissibility = result.get("operation_admissibility_evaluations")
    admissibility = admissibility if isinstance(admissibility, Mapping) else {}
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "outcome": result.get("outcome"),
        "operation_result": result.get("operation_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "block_code": block.get("block_code"),
        "operation_basis_supplied": posture.get("operation_basis_supplied"),
        "operation_basis_admitted": posture.get("operation_basis_admitted"),
        "evaluation_performed": posture.get("evaluation_performed"),
        "heterogeneous_condition_matrix_recorded": posture.get("heterogeneous_condition_matrix_recorded"),
        "operation_exhausted": posture.get("operation_exhausted"),
        "completed_operation_result_posture_count": result.get("completed_operation_result_posture_count"),
        "operation_source_and_record_basis_admissibility_evaluation": admissibility.get("operation_source_and_record_basis_admissibility_evaluation"),
        "operation_scope_and_matter_admissibility_evaluation": admissibility.get("operation_scope_and_matter_admissibility_evaluation"),
        "operation_transition_admissibility_evaluation": admissibility.get("operation_transition_admissibility_evaluation"),
        "ordered_condition_count": aggregate.get("ordered_condition_count"),
        "supported_by_admitted_body_held_records_count": aggregate.get("supported_by_admitted_body_held_records_count"),
        "requires_basis_count": aggregate.get("requires_basis_count"),
        "requires_basis_conditions": copy.deepcopy(aggregate.get("requires_basis_conditions")),
        "requires_basis_classes": copy.deepcopy(aggregate.get("requires_basis_classes")),
        "condition_ledger_populated": aggregate.get("condition_ledger_populated"),
        "condition_result_count": aggregate.get("condition_result_count"),
        "raw_signal_body_admitted": result.get("raw_signal_posture", {}).get("raw_signal_body_admitted"),
        "raw_signal_body_read_authorized": result.get("raw_signal_posture", {}).get("raw_signal_body_read_authorized"),
        "result_level_non_claims_canonical_false": result.get("result_level_non_claims_canonical_false"),
        "complete_material_omission_posture": result.get("omission_posture", {}).get("complete_material_omission_posture"),
        "admissible_future_route": result.get("admissible_future_route"),
        "operation_exhaustion_is_not_complete_receiver_answerable_basis": operation.get("operation_exhaustion_is_not_complete_receiver_answerable_basis"),
        "operation_exhaustion_is_not_presence": operation.get("operation_exhaustion_is_not_presence"),
    }


def _build_result(
    request: Any,
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    request_validated: bool = False,
    validations: Mapping[str, Any] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    completed = outcome == OUTCOME_RECORDED
    rows = copy.deepcopy(list(EXPECTED_CONDITION_LEDGER)) if completed else []
    aggregate = _derive_aggregate(rows) if completed else _empty_aggregate()
    evaluations = {condition: CONDITION_NOT_EVALUATED for condition in REQUIRED_CONDITIONS}
    if completed:
        evaluations = {row["condition_id"]: row["evaluation_posture"] for row in rows}
    admissibility_value = ADMISSIBILITY_PASSED if completed else ADMISSIBILITY_NOT_EVALUATED
    operation_result = OPERATION_RESULT_RECORDED if completed else OPERATION_RESULT_NOT_EVALUATED
    validation_sections: dict[str, Any] = {
        "specification_validation": _empty_validation(
            GOVERNING_SPECIFICATION_RELATIVE_PATH,
            GOVERNING_SPECIFICATION_SHA256,
        ),
        "boundary_specification_validation": _empty_validation(
            BOUNDARY_SPECIFICATION_RELATIVE_PATH,
            BOUNDARY_SPECIFICATION_SHA256,
        ),
        "boundary_artifact_validation": _empty_validation(
            BOUNDARY_ARTIFACT_RELATIVE_PATH,
            BOUNDARY_ARTIFACT_SHA256,
        ),
        "boundary_terminal_summary_validation": _empty_validation(
            BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH,
            BOUNDARY_TERMINAL_SUMMARY_SHA256,
        ),
        "prior_standing_validations": [],
        "carriage_lineage_validations": [],
        "receiver_packet_text_validations": [],
        "source_body_conduct_validations": [],
    }
    validation_sections.update(copy.deepcopy(dict(validations or {})))
    operation = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_id": OPERATION_ID,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_type": OPERATION_TYPE,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_version": OPERATION_VERSION,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_scope": OPERATION_SCOPE,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "operation_result": operation_result,
        "operation_basis_supplied": completed,
        "operation_basis_admitted": completed,
        "evaluation_performed": completed,
        "heterogeneous_condition_matrix_recorded": completed,
        "operation_exhausted": completed,
        "completed_operation_result_posture_count": 1 if completed else 0,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_recorded": completed,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_result_recorded": completed,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_performed": completed,
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_exhausted": completed,
        "condition_evaluations": copy.deepcopy(evaluations),
        "all_ten_conditions_evaluated": completed,
        "condition_ledger_populated": completed,
        "condition_result_count": 10 if completed else 0,
        "raw_signal_body_admitted": False,
        "raw_signal_body_read_authorized": False,
        "signal_morphology_evaluation_authorized": False,
        "authenticity_upgrade_from_signal_authorized": False,
        "admissible_future_route": None,
        "operation_exhaustion_is_not_complete_receiver_answerable_basis": True,
        "operation_exhaustion_is_not_presence": True,
    }
    for field in REQUIRED_FALSE_NON_CLAIMS:
        operation[field] = False
    result: dict[str, Any] = {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "operation_result": operation_result,
        "failed_check_count": sum(item["passed"] is False for item in checks),
        "passed_check_count": sum(item["passed"] is True for item in checks),
        "completed_operation_result_posture_count": 1 if completed else 0,
        "admissible_future_route": None,
        "block": {
            "blocked": not completed,
            "code": None if completed else code,
            "block_code": None if completed else code,
            "reason": None if completed else reason,
        },
        METADATA_KEY: {
            "resolver_module": RESOLVER_MODULE,
            "result_version": RESULT_VERSION,
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "governing_specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
            "governing_specification_sha256": GOVERNING_SPECIFICATION_SHA256,
            "deterministic": True,
            "current_clock_used": False,
            "filesystem_discovery_performed": False,
            "network_used": False,
        },
        DECLARED_REQUEST_KEY: (
            copy.deepcopy(dict(request))
            if request_validated and isinstance(request, Mapping)
            else {
                "request_mapping_supplied": isinstance(request, Mapping) and bool(request),
                "canonical_request_validated": False,
                "caller_payload_values_returned": False,
            }
        ),
        "canonical_request_validation": {
            "request_validated": request_validated,
            "exact_schema_validated": request_validated,
            "alternate_result_selection_absent": request_validated,
        },
        **validation_sections,
        "frozen_read_contract_posture": {
            "read_contract_closed": completed,
            "governing_and_current_standing_surface_count": 8,
            "carriage_lineage_surface_count": 7,
            "receiver_packet_text_surface_count": 8,
            "source_body_conduct_surface_count": 9,
            "all_exact_surfaces_validated": completed,
            "no_other_surface_selected": True,
            "filesystem_discovery_performed": False,
            "latest_file_selection_performed": False,
            "source_reconstruction_performed": False,
        },
        "excluded_read_posture": {
            "excluded_read_contract": list(EXCLUDED_READ_CONTRACT),
            "excluded_read_requested": False,
            "excluded_read_performed": False,
            "raw_signal_or_archive_opened": False,
            "glob_rglob_scan_or_discovery_performed": False,
        },
        "raw_signal_posture": copy.deepcopy(RAW_SIGNAL_POSTURE),
        "temporal_evidence_posture": {
            **copy.deepcopy(TEMPORAL_EVIDENCE),
            "temporal_evidence_validated": completed,
        },
        "exact_matter_and_family_posture": {
            "selected_matter_class": SELECTED_MATTER_CLASS,
            "ordered_ten_condition_matter": list(REQUIRED_CONDITIONS),
            "required_condition_values": copy.deepcopy(REQUIRED_CONDITION_VALUES),
            "evidence_class_family": list(EVIDENCE_CLASSES),
            "evidence_class_condition_mapping": {key: list(value) for key, value in EVIDENCE_CLASS_CONDITION_MAPPING.items()},
            "condition_evaluation_family": list(CONDITION_EVALUATION_FAMILY),
            "required_basis_class_family": list(REQUIRED_BASIS_CLASS_FAMILY),
            "operation_result_family": list(OPERATION_RESULT_FAMILY),
        },
        "condition_ledger_schema_contract": {
            "required_fields_in_order": list(CONDITION_LEDGER_SCHEMA_FIELDS),
            "compact_support_boolean_is_not_establishment_boolean": True,
        },
        "dependency_ceiling_contract": copy.deepcopy(list(DEPENDENCY_CEILING_CONTRACT)),
        "condition_evaluations": copy.deepcopy(evaluations),
        "condition_ledger": rows,
        "aggregate_matrix_posture": aggregate,
        "operation_admissibility_evaluations": {
            "operation_source_and_record_basis_admissibility_evaluation": admissibility_value,
            "operation_scope_and_matter_admissibility_evaluation": admissibility_value,
            "operation_transition_admissibility_evaluation": admissibility_value,
        },
        "operation_posture": {
            "operation_basis_supplied": completed,
            "operation_basis_admitted": completed,
            "evaluation_performed": completed,
            "heterogeneous_condition_matrix_recorded": completed,
            "operation_exhausted": completed,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_recorded": completed,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_result_recorded": completed,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_performed": completed,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_exhausted": completed,
            "completed_operation_result_posture_count": 1 if completed else 0,
            "single_use_only": completed,
            "no_partial_ledger_standing": not completed,
            "no_overwrite": True,
            "admissible_future_route": None,
        },
        OPERATION_KEY: operation,
        "lineage_preservation_posture": _canonical_lineage_posture(completed),
        "omission_posture": _canonical_omission_posture(),
        "non_claims": _canonical_non_claims(),
        "result_level_non_claims_canonical_false": True,
        NON_MEANING_KEY: _canonical_non_meaning(),
        "blocked_conversions": list(BLOCKED_CONVERSIONS),
        STATEMENT_KEY: {
            "one_completed_allowed_boundary_consumed": completed,
            "one_frozen_body_held_basis_consumed": completed,
            "exactly_ten_conditions_evaluated": completed,
            "exactly_nine_supported_rows_recorded": completed,
            "exactly_one_requires_basis_row_recorded": completed,
            "requires_basis_row_is_forged_receiver_attestation": completed,
            "condition_level_requires_basis_is_not_operation_failure": True,
            "raw_signal_considered_but_not_admitted": True,
            "prior_standing_not_overwritten": True,
            "future_route_is_null": True,
        },
        CHECKS_KEY: copy.deepcopy(checks),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
    }
    result[SUMMARY_KEY] = _summary_from_result(result)
    return result


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_default_result() -> dict[str, Any]:
    """Return the pure pre-execution posture without filesystem reads."""
    checks = [_check("execution.not_started", False, "NOT_EXECUTED")]
    return _build_result(
        {}, OUTCOME_BLOCKED, checks,
        code="NOT_EXECUTED",
        reason="operation resolution has not been executed",
    )


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result() -> dict[str, Any]:
    """Compatibility alias for the pure default result constructor."""
    return build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_default_result()


def resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min(
    request: Mapping[str, Any] | None = None,
    *,
    governing_specification_path: Path | str | None = None,
    boundary_specification_path: Path | str | None = None,
    boundary_artifact_path: Path | str | None = None,
    boundary_terminal_summary_path: Path | str | None = None,
    prior_presence_artifact_path: Path | str | None = None,
    source_admissibility_boundary_artifact_path: Path | str | None = None,
    later_modal_artifact_path: Path | str | None = None,
    modal_terminal_summary_path: Path | str | None = None,
    carriage_lineage_paths: Sequence[Path | str] | None = None,
    receiver_packet_text_paths: Sequence[Path | str] | None = None,
    source_body_conduct_paths: Sequence[Path | str] | None = None,
) -> dict[str, Any]:
    """Resolve the exact operation from explicit governed paths only."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared = _new_canonical_request()
    elif not isinstance(request, Mapping):
        _add_check(checks, "request.mapping", False, "REQUEST_NOT_MAPPING")
        return _build_result({}, OUTCOME_BLOCKED, checks, code="REQUEST_NOT_MAPPING", reason="declared request is not a mapping")
    else:
        declared = copy.deepcopy(dict(request))
    code, reason = _validate_request(declared, checks)
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, code=code, reason=reason)

    validations: dict[str, Any] = {}
    spec_path = GOVERNING_SPECIFICATION_PATH if governing_specification_path is None else governing_specification_path
    boundary_spec_path = BOUNDARY_SPECIFICATION_PATH if boundary_specification_path is None else boundary_specification_path
    boundary_path = BOUNDARY_ARTIFACT_PATH if boundary_artifact_path is None else boundary_artifact_path
    boundary_terminal_path = BOUNDARY_TERMINAL_SUMMARY_PATH if boundary_terminal_summary_path is None else boundary_terminal_summary_path
    prior_paths = (
        PRIOR_PRESENCE_ARTIFACT_PATH if prior_presence_artifact_path is None else prior_presence_artifact_path,
        SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_PATH if source_admissibility_boundary_artifact_path is None else source_admissibility_boundary_artifact_path,
        LATER_MODAL_ARTIFACT_PATH if later_modal_artifact_path is None else later_modal_artifact_path,
        MODAL_TERMINAL_SUMMARY_PATH if modal_terminal_summary_path is None else modal_terminal_summary_path,
    )
    carriage_paths = tuple(CARRIAGE_LINEAGE_PATHS if carriage_lineage_paths is None else carriage_lineage_paths)
    packet_paths = tuple(PACKET_TEXT_PATHS if receiver_packet_text_paths is None else receiver_packet_text_paths)
    conduct_paths = tuple(SOURCE_BODY_CONDUCT_PATHS if source_body_conduct_paths is None else source_body_conduct_paths)

    validators = (
        ("specification_validation", lambda: _validate_specification(spec_path, checks)),
        ("boundary_specification_validation", lambda: _validate_boundary_specification(boundary_spec_path, checks)),
        ("boundary_artifact_validation", lambda: _validate_boundary(boundary_path, checks)),
        ("boundary_terminal_summary_validation", lambda: _validate_boundary_terminal(boundary_terminal_path, checks)),
        ("prior_standing_validations", lambda: _validate_prior_standing(prior_paths, checks)),
        ("carriage_lineage_validations", lambda: _validate_carriage_lineage(carriage_paths, checks)),
        ("receiver_packet_text_validations", lambda: _validate_packet_texts(packet_paths, checks)),
        ("source_body_conduct_validations", lambda: _validate_conduct_surfaces(conduct_paths, checks)),
    )
    for section_name, validator in validators:
        code, reason, section = validator()
        validations[section_name] = section
        if code is not None:
            return _build_result(declared, OUTCOME_BLOCKED, checks, request_validated=True, validations=validations, code=code, reason=reason)
    code, reason = _validate_contracts(checks)
    if code is not None:
        return _build_result(declared, OUTCOME_BLOCKED, checks, request_validated=True, validations=validations, code=code, reason=reason)

    for check_id in (
        "admissibility.operation_source_and_record_basis",
        "admissibility.operation_scope_and_matter",
        "admissibility.operation_transition",
        "lineage.prior_standing_preserved_without_overwrite",
        "omission.complete_material_omitted",
        "nonclaims.canonical_false",
        "result.no_partial_ledger",
        "result.condition_level_requires_basis_not_failure",
        "result.future_route_null",
    ):
        _add_check(checks, check_id, True, "ADMISSIBILITY_BLOCKED")
    return _build_result(
        declared,
        OUTCOME_RECORDED,
        checks,
        request_validated=True,
        validations=validations,
    )


def resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_from_path(
    request_path: Path | str,
    **resolver_paths: Any,
) -> dict[str, Any]:
    """Strictly load one explicit request JSON object and resolve it."""
    value, _, error = _read_json(request_path)
    if error is not None or value is None:
        checks = [_check("request_path.strict_json_mapping", False, "REQUEST_JSON_INVALID")]
        return _build_result({}, OUTCOME_BLOCKED, checks, code="REQUEST_JSON_INVALID", reason="explicit request path is missing, malformed, duplicate-keyed, non-finite, or not an object")
    return resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min(value, **resolver_paths)


def _contains_prohibited_complete_material(value: Any) -> bool:
    forbidden = {
        "complete_upstream_artifact",
        "complete_upstream_artifact_body",
        "complete_candidate_body",
        "complete_candidate_evaluation_body",
        "raw_accelerometer_body",
        "raw_signal_body",
        "raw_signal_content",
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
        or set(item) != {"check_id", "passed", "block_code", "failure_code", "expected"}
        or type(item.get("passed")) is not bool
        or (item.get("passed") is False and (item.get("block_code") not in BLOCK_CODES or item.get("failure_code") not in BLOCK_CODES))
        or (item.get("passed") is True and (item.get("block_code") is not None or item.get("failure_code") is not None))
        for item in checks
    ):
        return False
    return result.get("passed_check_count") == sum(item["passed"] is True for item in checks) and result.get("failed_check_count") == sum(item["passed"] is False for item in checks)


def _structural_result_valid(result: Mapping[str, Any]) -> bool:
    if result.get("resolver_module") != RESOLVER_MODULE or result.get("result_version") != RESULT_VERSION or result.get("outcome") not in OUTCOME_FAMILY:
        return False
    if not _checks_valid(result) or _contains_prohibited_complete_material(result):
        return False
    if not _canonical_false_mapping(result.get("non_claims")) or result.get("result_level_non_claims_canonical_false") is not True:
        return False
    if result.get("omission_posture") != _canonical_omission_posture() or result.get(NON_MEANING_KEY) != _canonical_non_meaning():
        return False
    if result.get("blocked_conversions") != list(BLOCKED_CONVERSIONS) or result.get("what_remains_open") != list(WHAT_REMAINS_OPEN):
        return False
    if result.get("admissible_future_route") is not None or result.get("raw_signal_posture") != RAW_SIGNAL_POSTURE:
        return False
    outcome = result.get("outcome")
    completed = outcome == OUTCOME_RECORDED
    block = result.get("block")
    posture = result.get("operation_posture")
    admissibility = result.get("operation_admissibility_evaluations")
    if not isinstance(block, Mapping) or block.get("blocked") is completed:
        return False
    if not isinstance(posture, Mapping) or any(posture.get(field) is not completed for field in ("operation_basis_supplied", "operation_basis_admitted", "evaluation_performed", "heterogeneous_condition_matrix_recorded", "operation_exhausted")):
        return False
    if not isinstance(admissibility, Mapping) or any(value != (ADMISSIBILITY_PASSED if completed else ADMISSIBILITY_NOT_EVALUATED) for value in admissibility.values()):
        return False
    ledger = result.get("condition_ledger")
    aggregate = result.get("aggregate_matrix_posture")
    evaluations = result.get("condition_evaluations")
    if completed:
        if result.get("failed_check_count") != 0 or not _exact(ledger, list(EXPECTED_CONDITION_LEDGER)) or aggregate != EXPECTED_AGGREGATE_MATRIX_POSTURE:
            return False
        if evaluations != {row["condition_id"]: row["evaluation_posture"] for row in EXPECTED_CONDITION_LEDGER}:
            return False
        if result.get("lineage_preservation_posture") != _canonical_lineage_posture(True):
            return False
    else:
        if ledger != [] or aggregate != _empty_aggregate() or evaluations != {condition: CONDITION_NOT_EVALUATED for condition in REQUIRED_CONDITIONS}:
            return False
    return result.get(SUMMARY_KEY) == _summary_from_result(result)


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return the compact summary projection for a compatible result."""
    if not isinstance(result, Mapping) or not _structural_result_valid(result):
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinError(
            "summary requires a compatible operation result"
        )
    return copy.deepcopy(_summary_from_result(result))


def _canonical_completed_result_matches(result: Mapping[str, Any]) -> bool:
    if not _structural_result_valid(result) or result.get("outcome") != OUTCOME_RECORDED:
        return False
    declared = result.get(DECLARED_REQUEST_KEY)
    if not isinstance(declared, Mapping) or not _exact(declared, _new_canonical_request()):
        return False
    expected = resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min(_new_canonical_request())
    return _exact(dict(result), expected)


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
            BOUNDARY_ARTIFACT_PATH.parent.resolve(),
            PRIOR_PRESENCE_ARTIFACT_PATH.parent.resolve(),
            SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_PATH.parent.resolve(),
            LATER_MODAL_ARTIFACT_PATH.parent.resolve(),
            PACKET_TEXT_PATHS[0].parent.resolve(),
        )
        return OUTPUT_ROOT.name == CANONICAL_OUTPUT_ROOT.name and resolved == canonical and _path_within(resolved, root) and not any(_path_within(resolved, item) for item in protected)
    except (OSError, RuntimeError, TypeError, ValueError):
        return False


def write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one exact canonical completed result without overwriting."""
    if not isinstance(result, Mapping) or not _canonical_completed_result_matches(result):
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinError(
            "WRITE_REFUSED: malformed, inconsistent, or noncanonical operation result"
        )
    try:
        target = Path(output_path) if output_path is not None else OUTPUT_ROOT / OUTPUT_FILENAME
    except (TypeError, ValueError) as exc:
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinError(
            "WRITE_REFUSED: invalid output path"
        ) from exc
    if not _output_path_allowed(target):
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinError(
            "WRITE_REFUSED: output path is outside the exact canonical result path"
        )
    if target.exists():
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinError(
            "WRITE_REFUSED: canonical result path already exists"
        )
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(dict(result), handle, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False)
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinError(
            "WRITE_REFUSED: unable to write canonical operation result"
        ) from exc
    return target
