"""Record one additive correction to the completed body-held operation.

The resolver consumes the exact pinned v1 result and appends one successor
posture: a complete ten-row ledger has no partial-ledger standing.  It does
not rewrite the v1 artifact, reevaluate a condition, or create a future route.
"""

from __future__ import annotations

import copy
import hashlib
import json
import math
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinV2Error(
    ValueError
):
    """Raised when a summary or canonical successor write is refused."""


RESOLVER_MODULE = (
    "resolve_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_v0_min_v2"
)
RESULT_VERSION = "0.2.0"
SUCCESSOR_ID = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_001_v2"
)
SUCCESSOR_TYPE = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_"
    "OPERATION_SUCCESSOR"
)
SUCCESSOR_VERSION = "0.2.0"
SUCCESSOR_SCOPE = (
    "RECORD_ONE_ADDITIVE_SUCCESSOR_CORRECTING_NO_PARTIAL_LEDGER_STANDING_ONLY"
)
PRIOR_OPERATION_ID = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_001"
)
PRIOR_OPERATION_TYPE = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_"
    "OPERATION"
)
PRIOR_OPERATION_VERSION = "0.1.0"
PRIOR_OPERATION_SCOPE = (
    "EVALUATE_AND_RECORD_ONE_HETEROGENEOUS_TEN_CONDITION_MATRIX_FROM_ONE_"
    "FROZEN_BODY_HELD_BASIS_ONLY"
)
SELECTED_MATTER_CLASS = (
    "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_REMAINING_TEN_INTEGRITY_"
    "CONDITIONS_ONLY"
)

INTENT_RECORD = (
    "RECORD_BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_OPERATION_V2_SUCCESSOR"
)
OUTCOME_RECORDED = SUCCESSOR_TYPE + "_RECORDED"
OUTCOME_BLOCKED = SUCCESSOR_TYPE + "_BLOCKED"
OUTCOME_FAMILY = (OUTCOME_RECORDED, OUTCOME_BLOCKED)
SUCCESSOR_RESULT_RECORDED = OUTCOME_RECORDED
SUCCESSOR_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
SUCCESSOR_RESULT_FAMILY = (
    SUCCESSOR_RESULT_RECORDED,
    SUCCESSOR_RESULT_NOT_EVALUATED,
)
ADMISSIBLE_FUTURE_ROUTE = None

CONTRADICTION_ID = (
    "V1_NO_PARTIAL_LEDGER_STANDING_FALSE_WITH_COMPLETE_TEN_ROW_LEDGER"
)
CONTRADICTORY_FIELD_PATH = "operation_posture.no_partial_ledger_standing"
CORRECTION_REASON = (
    "THE_COMPLETED_OPERATION_RECORDED_EXACTLY_TEN_ORDERED_ROWS_WITH_NO_"
    "PARTIAL_LEDGER_STANDING"
)
CONTRADICTION_SCOPE = "ONE_DERIVED_OPERATION_POSTURE_FIELD_ONLY"

PRIOR_RESOLVER_MODULE = (
    "resolve_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_v0_min"
)
PRIOR_RESULT_VERSION = "0.1.0"
PRIOR_OUTCOME_RECORDED = PRIOR_OPERATION_TYPE + "_RECORDED"

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_"
    "EVALUATION_OPERATION_V0_MIN_SPEC.md"
)
GOVERNING_SPECIFICATION_PATH = REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPECIFICATION_SHA256 = (
    "3600cc9cf91c4938952b289119aeafbab53831e5e060d3d0e8abff357f4ba3dc"
)
PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_held_receiver_"
    "answerable_basis_integrity_condition_evaluation_operation_v0_min/"
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_001__body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_v0_min_result.json"
)
PRIOR_OPERATION_ARTIFACT_PATH = REPO_ROOT / PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH
PRIOR_OPERATION_ARTIFACT_SHA256 = (
    "18da6cf8f9250445d4708c7dce0ed8327d8d0577643f793f422a0281f9a6abef"
)

CANONICAL_OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_body_held_receiver_"
    "answerable_basis_integrity_condition_evaluation_operation_v0_min_v2"
)
OUTPUT_ROOT = CANONICAL_OUTPUT_ROOT
OUTPUT_FILENAME = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_001_v2__body_held_receiver_answerable_basis_integrity_"
    "condition_evaluation_operation_v0_min_v2_result.json"
)
DETERMINISTIC_FILENAME = OUTPUT_FILENAME

ORDERED_TEN_CONDITION_MATTER = (
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
SERIALIZED_LEDGER_SCHEMA_FIELDS = tuple(sorted(CONDITION_LEDGER_SCHEMA_FIELDS))

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
    "requires_basis_classes": ["EXTERNAL_AUTHENTICITY_BASIS"],
}
EXPECTED_CONDITION_EVALUATIONS = {
    condition: (
        "REQUIRES_BASIS"
        if condition == "forged_receiver_attestation"
        else "SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS"
    )
    for condition in ORDERED_TEN_CONDITION_MATTER
}
EXPECTED_RAW_SIGNAL_POSTURE = {
    "raw_signal_body_known_to_exist": True,
    "raw_signal_body_considered": True,
    "raw_signal_body_admitted": False,
    "raw_signal_body_read_authorized": False,
    "signal_morphology_evaluation_authorized": False,
    "authenticity_upgrade_from_signal_authorized": False,
}
EXPECTED_OPERATION_ADMISSIBILITY = {
    "operation_source_and_record_basis_admissibility_evaluation": "PASSED",
    "operation_scope_and_matter_admissibility_evaluation": "PASSED",
    "operation_transition_admissibility_evaluation": "PASSED",
}

# Canonical semantic digests are over strict JSON values with sorted compact keys.
# They pin every unaffected v1 section without copying the ledger into v2 output.
UNAFFECTED_SECTION_SHA256 = {
    "aggregate_matrix_posture": "26de43c580ed1dc375400e06bf07595ce2651f7e152456c82a9dcbcb283ca077",
    "blocked_conversions": "74e389141a49440b1dfb5b4d21477216191e4443d5047ad5740a0e0f372326ee",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_non_meaning": "36cf9e2181655dc13e1f676b5e4976b1e1f992c4c8560dcc38ef59161b534a18",
    "condition_evaluations": "343991a326db32ca3091b16b583e341f4c7892d3966ff2c5c86e8167dc6ca141",
    "condition_ledger": "99d4169e3f2df330b6b809ab5f6eff77c8f3f15d4a37deda3d0f656e128f1f1d",
    "condition_ledger_schema_contract": "88b1c9d497ef374d5ac4255a95855767a0330271210e71ed0194b18367d22c13",
    "dependency_ceiling_contract": "94113f14d8ba39dd0fae90763a8b9788395ac3cf6350cd86311d65c01b96feb5",
    "exact_matter_and_family_posture": "67d280d56b15da57ce091cccd5299a86ee27e84b678595b5cf9ba869286aef2e",
    "lineage_preservation_posture": "8aef16a1a2d15ff6b13ff654e20f27b7bc7b9166d13785bc3b2f3c69dd819233",
    "non_claims": "75eff15cebdd8bc8eda2145922200437321adfd32274856596725ecbe5f692f2",
    "omission_posture": "f938eb2a85709245cadc0072532a8d854db0eec8869fbc6f536b2f1c23aae1ba",
    "operation_admissibility_evaluations": "39a482f755bba3382864dd70283a74b14bd193661ed87e0d0a761e4677eca2db",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation": "3bd288406a21e38d4e520f47826f7a32dd74a0f88ca8e483cbe9ee8594438e8c",
    "raw_signal_posture": "2653ad7e085480d397ea39567b1b4fb92dd32435c566880c99daa16d82abee3f",
    "temporal_evidence_posture": "d78f679d728e954b113249503d724a9add7859787034a3c6c0f7b5af0141b3aa",
}
OPERATION_POSTURE_EXCEPT_CONTRADICTION_SHA256 = (
    "5e1b553c6b0e1f032e16fefe0a49b225d0f1ac510cc84896433fa8e2d27eb2be"
)

ONE_FIELD_DIFFERENCE_CONTRACT = {
    "field_path": CONTRADICTORY_FIELD_PATH,
    "prior_value": False,
    "successor_value": True,
    "correction_reason": CORRECTION_REASON,
    "prior_value_preserved_as_historical": True,
    "successor_value_appended": True,
}
REQUIRED_V1_STANDING_CONTRACT = {
    "resolver_module": PRIOR_RESOLVER_MODULE,
    "result_version": PRIOR_RESULT_VERSION,
    "outcome": PRIOR_OUTCOME_RECORDED,
    "operation_result": PRIOR_OUTCOME_RECORDED,
    "passed_check_count": 182,
    "failed_check_count": 0,
    "blocked": False,
    "operation_basis_supplied": True,
    "operation_basis_admitted": True,
    "evaluation_performed": True,
    "heterogeneous_condition_matrix_recorded": True,
    "operation_exhausted": True,
    "completed_operation_result_posture_count": 1,
    "admissible_future_route": None,
}
UNAFFECTED_STANDING_PRESERVATION_CONTRACT = {
    "section_sha256": copy.deepcopy(UNAFFECTED_SECTION_SHA256),
    "operation_posture_except_contradiction_sha256": (
        OPERATION_POSTURE_EXCEPT_CONTRADICTION_SHA256
    ),
    "condition_order": list(ORDERED_TEN_CONDITION_MATTER),
    "supported_row_count": 9,
    "requires_basis_row_count": 1,
    "requires_basis_condition": "forged_receiver_attestation",
    "requires_basis_class": "EXTERNAL_AUTHENTICITY_BASIS",
    "evidence_class_count": 3,
    "dependency_ceiling_count": 10,
    "future_route": None,
}

CHRONOLOGY = (
    {
        "position": 1,
        "standing": "PRIOR_PRESENCE_REQUIRES_BASIS_STANDING",
        "historically_preserved": True,
    },
    {
        "position": 2,
        "standing": "LATER_RECEIVER_ORIGINATING_MODAL_SUPPORT",
        "historically_preserved": True,
    },
    {
        "position": 3,
        "standing": "COMPLETED_BODY_HELD_INTEGRITY_CONDITION_EVALUATION_BOUNDARY",
        "historically_preserved": True,
    },
    {
        "position": 4,
        "standing": "COMPLETED_V1_TEN_CONDITION_EVALUATION_OPERATION",
        "historically_preserved": True,
    },
    {
        "position": 5,
        "standing": "V2_ONE_FIELD_SUCCESSOR_CORRECTION",
        "historically_preserved": True,
    },
)

REQUIRED_FALSE_NON_CLAIMS = (
    "v1_operation_invalidated",
    "v1_operation_failed",
    "v1_artifact_overwritten",
    "v1_artifact_replaced",
    "v1_artifact_deleted",
    "v1_artifact_normalized",
    "v1_result_superseded",
    "v1_ledger_changed",
    "v1_aggregate_changed",
    "any_condition_evaluation_changed",
    "any_support_proposition_changed",
    "any_limitation_changed",
    "any_evidence_class_changed",
    "any_dependency_ceiling_changed",
    "any_required_basis_class_changed",
    "receiver_attestation_non_forgery_established",
    "custody_proven",
    "receiver_identity_established",
    "provenance_proven",
    "physical_validity_proven",
    "universal_absence_established",
    "global_admissibility_established",
    "complete_receiver_answerable_basis_established",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "truth_created",
    "standing_created",
    "authority_created",
    "threshold_machinery_created",
    "truth_settlement_machinery_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "output_authorized",
    "action_authorized",
    "follow_on_authorized",
    "repeated_successor_permission_created",
    "reusable_successor_route_created",
    "successor_rerun_authorized",
    "automatic_retry_created",
    "debt_created",
    "obligation_created",
    "scheduled_work_created",
    "automatic_next_created",
    "repair_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforcement_performed",
)

NON_MEANING_FIELDS = (
    "successor_correction_is_not_retroactive_overwrite",
    "historical_false_field_preservation_is_not_current_successor_endorsement",
    "one_local_field_contradiction_is_not_operation_failure",
    "v1_operation_recording_remains_valid",
    "v1_matrix_remains_complete",
    "successor_correction_does_not_reevaluate_conditions",
    "successor_correction_does_not_alter_evidence",
    "successor_correction_does_not_alter_support",
    "successor_correction_does_not_establish_reality_wide_facts",
    "successor_correction_is_not_complete_receiver_answerable_basis",
    "successor_exhaustion_is_not_presence",
    "open_does_not_mean_next",
)

BLOCKED_CONVERSIONS = (
    "V1_FIELD_CORRECTION_TO_V1_ARTIFACT_OVERWRITE",
    "ONE_FIELD_SUCCESSOR_TO_FULL_RESULT_REPLACEMENT",
    "LOCAL_POSTURE_CONTRADICTION_TO_OPERATION_FAILURE",
    "SUCCESSOR_CORRECTION_TO_CONDITION_REEVALUATION",
    "SUCCESSOR_CORRECTION_TO_LEDGER_CHANGE",
    "SUCCESSOR_CORRECTION_TO_AGGREGATE_CHANGE",
    "SUCCESSOR_CORRECTION_TO_AUTHENTICITY_OR_NON_FORGERY",
    "SUCCESSOR_CORRECTION_TO_COMPLETE_RECEIVER_ANSWERABLE_BASIS",
    "SUCCESSOR_CORRECTION_TO_PRESENCE_TRUTH_STANDING_OR_AUTHORITY",
    "SUCCESSOR_RESULT_TO_REPEAT_RETRY_DEBT_OBLIGATION_SCHEDULE_OR_AUTOMATIC_NEXT",
    "SUCCESSOR_RESULT_TO_REPAIR_SCAN_DISCOVERY_VALIDATION_OR_RECONSTRUCTION",
)

WHAT_REMAINS_OPEN = (
    "v2 successor tests",
    "v2 successor request",
    "v2 successor live result",
    "operation terminal summary covering v1 and v2 correction lineage",
    "external-authenticity basis",
    "cryptographic receiver identity",
    "raw-signal morphology under separate admission",
    "complete receiver-answerable basis",
    "later presence re-evaluation",
    "presence support, authorization, establishment, and recording",
    "threshold",
    "truth settlement",
    "identity",
    "custody proof",
    "provenance proof",
    "physical validity",
    "authority",
    "truth",
    "standing",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "public interface",
    "public intake",
    "output",
    "action",
    "derivative reception",
    "synchronization",
    "follow-on work",
)

OMISSION_POSTURE_FIELDS = (
    "complete_v1_artifact_body_omitted",
    "complete_v1_condition_ledger_omitted",
    "complete_v1_condition_evaluations_omitted",
    "complete_v1_upstream_artifact_bodies_omitted",
    "raw_signal_body_omitted",
    "zip_and_archive_bytes_omitted",
    "excluded_source_bodies_omitted",
)

PROHIBITED_REQUEST_KEYS = frozenset(
    {
        "semantic_payload",
        "complete_v1_result",
        "complete_v1_result_body",
        "corrected_v1_result",
        "condition_ledger",
        "aggregate_matrix_posture",
        "condition_evaluations",
        "condition_result_selection",
        "evidence_change",
        "raw_signal_body",
        "zip_bytes",
        "archive_bytes",
        "future_route",
        "admissible_future_route",
        "automatic_next",
        "additional_changed_field",
        "second_correction",
        "discovery",
        "glob",
        "rglob",
        "scan",
        "normalization",
        "reconstruction",
        "repair",
        "replacement",
        "latest_file_selection",
        "downstream_standing",
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
        "REQUEST_PROHIBITED_PAYLOAD",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "SPECIFICATION_MISSING_OR_UNREADABLE",
        "SPECIFICATION_DIGEST_MISMATCH",
        "SPECIFICATION_INVALID",
        "V1_ARTIFACT_MISSING_OR_UNREADABLE",
        "V1_ARTIFACT_JSON_INVALID",
        "V1_ARTIFACT_DIGEST_MISMATCH",
        "V1_IDENTITY_INVALID",
        "V1_RESULT_NOT_RECORDED",
        "V1_RESULT_BLOCKED_OR_FAILED",
        "V1_COMPLETION_INVALID",
        "V1_FUTURE_ROUTE_NOT_NULL",
        "V1_ADMISSIBILITY_INVALID",
        "V1_OPERATION_OBJECT_INVALID",
        "V1_AGGREGATE_INVALID",
        "V1_LEDGER_INVALID",
        "V1_LEDGER_CARDINALITY_INVALID",
        "V1_LEDGER_SCHEMA_INVALID",
        "V1_LEDGER_ORDER_INVALID",
        "V1_LEDGER_ROW_INVALID",
        "V1_CONDITION_EVALUATIONS_INVALID",
        "V1_NO_PARTIAL_LEDGER_CHECK_INVALID",
        "V1_CONTRADICTORY_FIELD_INVALID",
        "NO_CORRECTION_MATTER_REMAINS",
        "V1_UNAFFECTED_STANDING_CHANGED",
        "V1_RAW_SIGNAL_POSTURE_INVALID",
        "V1_NON_CLAIMS_INVALID",
        "CORRECTION_BASIS_INVALID",
        "SECOND_SEMANTIC_CHANGE_REQUESTED",
        "EXCLUDED_READ_REQUESTED",
        "DOWNSTREAM_STANDING_PRECLAIMED",
        "WRITE_REFUSED",
    }
)

DECLARED_REQUEST_KEY = (
    "declared_body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_operation_v0_min_v2_successor_request"
)
SUCCESSOR_KEY = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_successor"
)
CHECKS_KEY = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_v0_min_v2_successor_checks"
)
SUMMARY_KEY = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_v0_min_v2_successor_summary"
)
STATEMENT_KEY = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_v0_min_v2_successor_statement"
)
NON_MEANING_KEY = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_v0_min_v2_successor_non_meaning"
)
METADATA_KEY = (
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_"
    "operation_v0_min_v2_successor_metadata"
)


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_non_meaning() -> dict[str, bool]:
    return {field: True for field in NON_MEANING_FIELDS}


def _canonical_omission_posture() -> dict[str, bool]:
    return {
        **{field: True for field in OMISSION_POSTURE_FIELDS},
        "complete_material_omission_posture": True,
    }


def _identity_request_values() -> dict[str, Any]:
    return {
        "intent": INTENT_RECORD,
        "successor_id": SUCCESSOR_ID,
        "successor_type": SUCCESSOR_TYPE,
        "successor_version": SUCCESSOR_VERSION,
        "successor_scope": SUCCESSOR_SCOPE,
        "governing_specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "governing_specification_sha256": GOVERNING_SPECIFICATION_SHA256,
        "prior_operation_artifact_path": str(PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH),
        "prior_operation_artifact_sha256": PRIOR_OPERATION_ARTIFACT_SHA256,
        "prior_operation_id": PRIOR_OPERATION_ID,
        "prior_operation_type": PRIOR_OPERATION_TYPE,
        "prior_operation_version": PRIOR_OPERATION_VERSION,
        "prior_operation_scope": PRIOR_OPERATION_SCOPE,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "contradiction_id": CONTRADICTION_ID,
        "contradictory_field_path": CONTRADICTORY_FIELD_PATH,
        "prior_field_value": False,
        "successor_field_value": True,
        "correction_reason": CORRECTION_REASON,
        "one_field_difference_contract": copy.deepcopy(ONE_FIELD_DIFFERENCE_CONTRACT),
        "required_v1_standing_contract": copy.deepcopy(REQUIRED_V1_STANDING_CONTRACT),
        "unaffected_standing_preservation_contract": copy.deepcopy(
            UNAFFECTED_STANDING_PRESERVATION_CONTRACT
        ),
    }


def _new_canonical_request() -> dict[str, Any]:
    return {
        **_identity_request_values(),
        "declared_non_claims": _canonical_non_claims(),
    }


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_request() -> dict[str, Any]:
    """Return one fresh canonical v2 successor request."""
    return copy.deepcopy(_new_canonical_request())


def build_declared_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Return a canonical request while retaining caller overrides visibly."""
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
        value = json.loads(
            payload.decode("utf-8", errors="strict"),
            object_pairs_hook=_pairs_without_duplicates,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        return None, str(exc)
    return value, None


def _read_bytes(path: Path | str) -> tuple[bytes | None, str | None]:
    try:
        selected = Path(path)
        if not selected.is_file():
            return None, "not a regular file"
        return selected.read_bytes(), None
    except (OSError, TypeError, ValueError) as exc:
        return None, str(exc)


def _read_json(
    path: Path | str,
) -> tuple[Mapping[str, Any] | None, bytes | None, str | None]:
    payload, error = _read_bytes(path)
    if error is not None or payload is None:
        return None, payload, error
    value, error = _parse_json_bytes(payload)
    if error is not None:
        return None, payload, error
    if not isinstance(value, Mapping):
        return None, payload, "top-level JSON value is not an object"
    return value, payload, None


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_digest(value: Any) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return _sha256(payload)


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


def _canonical_false_mapping(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS)
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


def _contains_prohibited_request_key(value: Any) -> bool:
    return isinstance(value, Mapping) and bool(
        set(value).intersection(PROHIBITED_REQUEST_KEYS)
    )


def _validate_request(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None]:
    if _contains_prohibited_request_key(request):
        _add_check(
            checks,
            "request.prohibited_payload_absent",
            False,
            "REQUEST_PROHIBITED_PAYLOAD",
        )
        return (
            "REQUEST_PROHIBITED_PAYLOAD",
            "request contains a semantic payload, excluded read, or second correction",
        )
    expected = _new_canonical_request()
    missing = set(expected).difference(request)
    unknown = set(request).difference(expected)
    if missing:
        _add_check(
            checks,
            "request.schema.missing",
            False,
            "REQUEST_FIELD_MISSING",
            expected=sorted(expected),
        )
        return "REQUEST_FIELD_MISSING", "canonical request fields are missing"
    if unknown:
        _add_check(
            checks,
            "request.schema.unknown",
            False,
            "REQUEST_UNKNOWN_FIELD",
            expected=sorted(expected),
        )
        return "REQUEST_UNKNOWN_FIELD", "request contains unknown fields"
    _add_check(
        checks,
        "request.canonical_schema",
        True,
        "REQUEST_VALUE_MISMATCH",
        expected="exact canonical key set",
    )
    for field, expected_value in _identity_request_values().items():
        actual = request.get(field)
        if not _exact(actual, expected_value):
            code = (
                "REQUEST_TYPE_MISMATCH"
                if type(actual) is not type(expected_value)
                else "REQUEST_VALUE_MISMATCH"
            )
            _add_check(
                checks,
                "request." + field,
                False,
                code,
                expected=expected_value,
            )
            return code, field + " does not match the canonical successor request"
        _add_check(
            checks,
            "request." + field,
            True,
            "REQUEST_VALUE_MISMATCH",
            expected=expected_value,
        )
    if not _canonical_false_mapping(request.get("declared_non_claims")):
        _add_check(
            checks,
            "request.declared_non_claims",
            False,
            "NON_CLAIM_MISSING_OR_FLIPPED",
            expected=_canonical_non_claims(),
        )
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared non-claims are missing, malformed, or not canonical false",
        )
    _add_check(
        checks,
        "request.declared_non_claims",
        True,
        "NON_CLAIM_MISSING_OR_FLIPPED",
        expected="complete canonical false mapping",
    )
    _add_check(
        checks,
        "request.prohibited_payload_absent",
        True,
        "REQUEST_PROHIBITED_PAYLOAD",
    )
    return None, None


def _empty_validation(relative_path: Path, digest: str) -> dict[str, Any]:
    return {
        "path": str(relative_path),
        "expected_sha256": digest,
        "observed_sha256": None,
        "strict_content_validated": False,
        "surface_validated": False,
        "complete_body_omitted": True,
    }


def _validate_specification(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_validation(
        GOVERNING_SPECIFICATION_RELATIVE_PATH,
        GOVERNING_SPECIFICATION_SHA256,
    )
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
        _add_check(
            checks,
            "specification.strict_utf8",
            False,
            "SPECIFICATION_INVALID",
        )
        return "SPECIFICATION_INVALID", "governing specification is not UTF-8", validation
    markers = (
        "# Body-Held Receiver-Answerable-Basis Integrity-Condition Evaluation Operation V0 Minimum Specification",
        PRIOR_OPERATION_TYPE,
        SELECTED_MATTER_CLASS,
        "No blocked result may carry partial ledger standing.",
    )
    valid = not payload.startswith(b"\xef\xbb\xbf") and all(
        marker in text for marker in markers
    )
    if not _add_check(
        checks,
        "specification.governing_markers",
        valid,
        "SPECIFICATION_INVALID",
        expected=list(markers),
    ):
        return "SPECIFICATION_INVALID", "governing specification markers are invalid", validation
    validation.update(
        {
            "strict_content_validated": True,
            "surface_validated": True,
            "specification_validated": True,
        }
    )
    return None, None, validation


def _operation_posture_without_contradiction(value: Mapping[str, Any]) -> Any:
    posture = value.get("operation_posture")
    if not isinstance(posture, Mapping):
        return None
    projected = dict(posture)
    projected.pop("no_partial_ledger_standing", None)
    return projected


def _validate_v1_artifact(
    path: Path | str, checks: list[dict[str, Any]]
) -> tuple[
    str | None,
    str | None,
    dict[str, Any],
    dict[str, Any],
]:
    validation = _empty_validation(
        PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH,
        PRIOR_OPERATION_ARTIFACT_SHA256,
    )
    preservation = {
        "section_sha256": copy.deepcopy(UNAFFECTED_SECTION_SHA256),
        "observed_section_sha256": {},
        "operation_posture_except_contradiction_sha256": (
            OPERATION_POSTURE_EXCEPT_CONTRADICTION_SHA256
        ),
        "observed_operation_posture_except_contradiction_sha256": None,
        "all_unaffected_sections_exactly_equivalent": False,
        "complete_v1_body_omitted": True,
        "full_ledger_omitted": True,
    }
    payload, read_error = _read_bytes(path)
    if read_error is not None or payload is None:
        _add_check(
            checks,
            "v1_artifact.readable",
            False,
            "V1_ARTIFACT_MISSING_OR_UNREADABLE",
        )
        return (
            "V1_ARTIFACT_MISSING_OR_UNREADABLE",
            "exact v1 artifact is missing or unreadable",
            validation,
            preservation,
        )
    value, parse_error = _parse_json_bytes(payload)
    if parse_error is not None or not isinstance(value, Mapping):
        _add_check(
            checks,
            "v1_artifact.strict_duplicate_key_free_json",
            False,
            "V1_ARTIFACT_JSON_INVALID",
        )
        return (
            "V1_ARTIFACT_JSON_INVALID",
            "v1 artifact is malformed, duplicate-keyed, non-finite, or not an object",
            validation,
            preservation,
        )
    _add_check(
        checks,
        "v1_artifact.strict_duplicate_key_free_json",
        True,
        "V1_ARTIFACT_JSON_INVALID",
    )
    observed = _sha256(payload)
    validation["observed_sha256"] = observed
    if not _add_check(
        checks,
        "v1_artifact.sha256",
        observed == PRIOR_OPERATION_ARTIFACT_SHA256,
        "V1_ARTIFACT_DIGEST_MISMATCH",
        expected=PRIOR_OPERATION_ARTIFACT_SHA256,
    ):
        return (
            "V1_ARTIFACT_DIGEST_MISMATCH",
            "v1 artifact digest mismatch",
            validation,
            preservation,
        )

    identity_valid = (
        value.get("resolver_module") == PRIOR_RESOLVER_MODULE
        and value.get("result_version") == PRIOR_RESULT_VERSION
    )
    if not _add_check(
        checks,
        "v1.identity",
        identity_valid,
        "V1_IDENTITY_INVALID",
        expected={
            "resolver_module": PRIOR_RESOLVER_MODULE,
            "result_version": PRIOR_RESULT_VERSION,
        },
    ):
        return "V1_IDENTITY_INVALID", "v1 artifact identity is invalid", validation, preservation

    recorded_valid = (
        value.get("outcome") == PRIOR_OUTCOME_RECORDED
        and value.get("operation_result") == PRIOR_OUTCOME_RECORDED
    )
    if not _add_check(
        checks,
        "v1.recorded_result",
        recorded_valid,
        "V1_RESULT_NOT_RECORDED",
        expected=PRIOR_OUTCOME_RECORDED,
    ):
        return "V1_RESULT_NOT_RECORDED", "v1 operation is not recorded", validation, preservation

    block = value.get("block")
    counts_valid = (
        value.get("passed_check_count") == 182
        and value.get("failed_check_count") == 0
        and isinstance(block, Mapping)
        and block.get("blocked") is False
        and block.get("code") is None
        and block.get("block_code") is None
    )
    if not _add_check(
        checks,
        "v1.counts_and_clear_block",
        counts_valid,
        "V1_RESULT_BLOCKED_OR_FAILED",
        expected="182 passed, 0 failed, unblocked",
    ):
        return (
            "V1_RESULT_BLOCKED_OR_FAILED",
            "v1 operation is blocked, failed, or has wrong check counts",
            validation,
            preservation,
        )

    posture = value.get("operation_posture")
    completion_fields = (
        "operation_basis_supplied",
        "operation_basis_admitted",
        "evaluation_performed",
        "heterogeneous_condition_matrix_recorded",
        "operation_exhausted",
    )
    completion_valid = (
        isinstance(posture, Mapping)
        and all(posture.get(field) is True for field in completion_fields)
        and posture.get("completed_operation_result_posture_count") == 1
        and value.get("completed_operation_result_posture_count") == 1
    )
    if not _add_check(
        checks,
        "v1.completion",
        completion_valid,
        "V1_COMPLETION_INVALID",
        expected="complete and exhausted single operation",
    ):
        return "V1_COMPLETION_INVALID", "v1 operation completion is invalid", validation, preservation

    route_valid = (
        value.get("admissible_future_route") is None
        and posture.get("admissible_future_route") is None
    )
    if not _add_check(
        checks,
        "v1.future_route_null",
        route_valid,
        "V1_FUTURE_ROUTE_NOT_NULL",
        expected=None,
    ):
        return (
            "V1_FUTURE_ROUTE_NOT_NULL",
            "v1 future route is not null",
            validation,
            preservation,
        )

    admissibility_valid = _exact(
        value.get("operation_admissibility_evaluations"),
        EXPECTED_OPERATION_ADMISSIBILITY,
    )
    if not _add_check(
        checks,
        "v1.all_three_admissibility_evaluations",
        admissibility_valid,
        "V1_ADMISSIBILITY_INVALID",
        expected=EXPECTED_OPERATION_ADMISSIBILITY,
    ):
        return "V1_ADMISSIBILITY_INVALID", "v1 admissibility is invalid", validation, preservation

    operation = value.get(
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation"
    )
    operation_valid = (
        isinstance(operation, Mapping)
        and operation.get("operation_id") == PRIOR_OPERATION_ID
        and operation.get(
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_id"
        )
        == PRIOR_OPERATION_ID
        and operation.get("operation_type") == PRIOR_OPERATION_TYPE
        and operation.get("operation_version") == PRIOR_OPERATION_VERSION
        and operation.get("operation_scope") == PRIOR_OPERATION_SCOPE
        and operation.get("selected_matter_class") == SELECTED_MATTER_CLASS
        and operation.get("operation_result") == PRIOR_OUTCOME_RECORDED
        and operation.get("all_ten_conditions_evaluated") is True
        and operation.get("condition_ledger_populated") is True
        and operation.get("condition_result_count") == 10
    )
    if not _add_check(
        checks,
        "v1.operation_object",
        operation_valid,
        "V1_OPERATION_OBJECT_INVALID",
    ):
        return "V1_OPERATION_OBJECT_INVALID", "v1 operation object is invalid", validation, preservation

    aggregate = value.get("aggregate_matrix_posture")
    if not _add_check(
        checks,
        "v1.aggregate_matrix_exact",
        _exact(aggregate, EXPECTED_AGGREGATE_MATRIX_POSTURE),
        "V1_AGGREGATE_INVALID",
        expected=EXPECTED_AGGREGATE_MATRIX_POSTURE,
    ):
        return "V1_AGGREGATE_INVALID", "v1 aggregate matrix is not exact", validation, preservation

    ledger = value.get("condition_ledger")
    if not isinstance(ledger, list):
        _add_check(checks, "v1.ledger.list", False, "V1_LEDGER_INVALID")
        return "V1_LEDGER_INVALID", "v1 condition ledger is not a list", validation, preservation
    _add_check(checks, "v1.ledger.list", True, "V1_LEDGER_INVALID")
    if not _add_check(
        checks,
        "v1.ledger.cardinality",
        len(ledger) == 10,
        "V1_LEDGER_CARDINALITY_INVALID",
        expected=10,
    ):
        return (
            "V1_LEDGER_CARDINALITY_INVALID",
            "v1 ledger does not contain exactly ten rows",
            validation,
            preservation,
        )
    schema_valid = all(
        isinstance(row, Mapping)
        and tuple(row) == SERIALIZED_LEDGER_SCHEMA_FIELDS
        and set(row) == set(CONDITION_LEDGER_SCHEMA_FIELDS)
        for row in ledger
    )
    if not _add_check(
        checks,
        "v1.ledger.exact_seventeen_field_schema",
        schema_valid,
        "V1_LEDGER_SCHEMA_INVALID",
        expected=list(CONDITION_LEDGER_SCHEMA_FIELDS),
    ):
        return "V1_LEDGER_SCHEMA_INVALID", "v1 ledger row schema is invalid", validation, preservation
    observed_ids = [row.get("condition_id") for row in ledger]
    order_valid = (
        observed_ids == list(ORDERED_TEN_CONDITION_MATTER)
        and len(set(observed_ids)) == 10
    )
    if not _add_check(
        checks,
        "v1.ledger.condition_order",
        order_valid,
        "V1_LEDGER_ORDER_INVALID",
        expected=list(ORDERED_TEN_CONDITION_MATTER),
    ):
        return "V1_LEDGER_ORDER_INVALID", "v1 ledger rows are missing, duplicated, unknown, or reordered", validation, preservation
    rows_valid = all(
        row.get("prior_posture_preserved") is True
        and row.get("no_overwrite") is True
        and row.get("evaluation_posture")
        == EXPECTED_CONDITION_EVALUATIONS[row["condition_id"]]
        and (
            row.get("required_basis_class") == "EXTERNAL_AUTHENTICITY_BASIS"
            if row["condition_id"] == "forged_receiver_attestation"
            else row.get("required_basis_class") == "NONE"
        )
        for row in ledger
    )
    if not _add_check(
        checks,
        "v1.ledger.complete_rows_and_locks",
        rows_valid,
        "V1_LEDGER_ROW_INVALID",
    ):
        return "V1_LEDGER_ROW_INVALID", "v1 ledger contains a malformed or incomplete row", validation, preservation
    _add_check(
        checks,
        "v1.ledger.supported_and_requires_basis_counts",
        sum(row.get("evaluation_posture") == "SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS" for row in ledger) == 9
        and sum(row.get("evaluation_posture") == "REQUIRES_BASIS" for row in ledger) == 1,
        "V1_LEDGER_ROW_INVALID",
        expected={"supported": 9, "requires_basis": 1},
    )
    forgery_rows = [
        row for row in ledger if row.get("condition_id") == "forged_receiver_attestation"
    ]
    if not _add_check(
        checks,
        "v1.ledger.forgery_requires_external_authenticity",
        len(forgery_rows) == 1
        and forgery_rows[0].get("evaluation_posture") == "REQUIRES_BASIS"
        and forgery_rows[0].get("required_basis_class") == "EXTERNAL_AUTHENTICITY_BASIS",
        "V1_LEDGER_ROW_INVALID",
    ):
        return "V1_LEDGER_ROW_INVALID", "v1 forgery row standing is invalid", validation, preservation

    evaluations_valid = _exact(
        value.get("condition_evaluations"), EXPECTED_CONDITION_EVALUATIONS
    )
    if not _add_check(
        checks,
        "v1.condition_evaluations_exact",
        evaluations_valid,
        "V1_CONDITION_EVALUATIONS_INVALID",
        expected=EXPECTED_CONDITION_EVALUATIONS,
    ):
        return (
            "V1_CONDITION_EVALUATIONS_INVALID",
            "v1 condition evaluations differ from completed standing",
            validation,
            preservation,
        )

    checks_value = value.get(
        "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_checks"
    )
    matching = (
        [
            item
            for item in checks_value
            if isinstance(item, Mapping)
            and item.get("check_id") == "result.no_partial_ledger"
        ]
        if isinstance(checks_value, list)
        else []
    )
    exact_check_valid = (
        len(matching) == 1
        and matching[0].get("passed") is True
        and matching[0].get("failure_code") is None
        and matching[0].get("block_code") is None
    )
    if not _add_check(
        checks,
        "v1.result_no_partial_ledger_check",
        exact_check_valid,
        "V1_NO_PARTIAL_LEDGER_CHECK_INVALID",
    ):
        return (
            "V1_NO_PARTIAL_LEDGER_CHECK_INVALID",
            "v1 result.no_partial_ledger check is absent, duplicated, or not passed",
            validation,
            preservation,
        )

    if not isinstance(posture, Mapping) or "no_partial_ledger_standing" not in posture:
        _add_check(
            checks,
            "v1.contradictory_field_present",
            False,
            "V1_CONTRADICTORY_FIELD_INVALID",
        )
        return (
            "V1_CONTRADICTORY_FIELD_INVALID",
            "v1 contradictory field is absent or malformed",
            validation,
            preservation,
        )
    prior_value = posture["no_partial_ledger_standing"]
    if prior_value is True:
        _add_check(
            checks,
            "v1.correction_matter_remains",
            False,
            "NO_CORRECTION_MATTER_REMAINS",
            expected=False,
        )
        return (
            "NO_CORRECTION_MATTER_REMAINS",
            "v1 field is already true; no correction matter remains",
            validation,
            preservation,
        )
    if prior_value is not False:
        _add_check(
            checks,
            "v1.contradictory_field_exact_false",
            False,
            "V1_CONTRADICTORY_FIELD_INVALID",
            expected=False,
        )
        return (
            "V1_CONTRADICTORY_FIELD_INVALID",
            "v1 contradictory field is not exactly false",
            validation,
            preservation,
        )
    _add_check(
        checks,
        "v1.contradictory_field_exact_false",
        True,
        "V1_CONTRADICTORY_FIELD_INVALID",
        expected=False,
    )

    all_sections_valid = True
    for section, expected_digest in UNAFFECTED_SECTION_SHA256.items():
        try:
            observed_digest = _canonical_digest(value.get(section))
        except (TypeError, ValueError):
            observed_digest = ""
        preservation["observed_section_sha256"][section] = observed_digest
        valid = observed_digest == expected_digest
        all_sections_valid = all_sections_valid and valid
        if not _add_check(
            checks,
            "v1.unaffected_section." + section,
            valid,
            "V1_UNAFFECTED_STANDING_CHANGED",
            expected=expected_digest,
        ):
            return (
                "V1_UNAFFECTED_STANDING_CHANGED",
                "an unaffected v1 semantic section differs from pinned standing",
                validation,
                preservation,
            )
    try:
        observed_posture_digest = _canonical_digest(
            _operation_posture_without_contradiction(value)
        )
    except (TypeError, ValueError):
        observed_posture_digest = ""
    preservation["observed_operation_posture_except_contradiction_sha256"] = (
        observed_posture_digest
    )
    posture_projection_valid = (
        observed_posture_digest == OPERATION_POSTURE_EXCEPT_CONTRADICTION_SHA256
    )
    if not _add_check(
        checks,
        "v1.operation_posture_except_contradiction",
        posture_projection_valid,
        "V1_UNAFFECTED_STANDING_CHANGED",
        expected=OPERATION_POSTURE_EXCEPT_CONTRADICTION_SHA256,
    ):
        return (
            "V1_UNAFFECTED_STANDING_CHANGED",
            "v1 operation posture changed outside the contradictory field",
            validation,
            preservation,
        )

    if not _add_check(
        checks,
        "v1.raw_signal_non_admission",
        _exact(value.get("raw_signal_posture"), EXPECTED_RAW_SIGNAL_POSTURE),
        "V1_RAW_SIGNAL_POSTURE_INVALID",
        expected=EXPECTED_RAW_SIGNAL_POSTURE,
    ):
        return (
            "V1_RAW_SIGNAL_POSTURE_INVALID",
            "v1 raw-signal non-admission posture is invalid",
            validation,
            preservation,
        )
    v1_non_claims = value.get("non_claims")
    non_claims_valid = (
        isinstance(v1_non_claims, Mapping)
        and bool(v1_non_claims)
        and all(item is False for item in v1_non_claims.values())
        and value.get("result_level_non_claims_canonical_false") is True
    )
    if not _add_check(
        checks,
        "v1.non_claims_canonical_false",
        non_claims_valid,
        "V1_NON_CLAIMS_INVALID",
    ):
        return "V1_NON_CLAIMS_INVALID", "v1 non-claims are not canonical false", validation, preservation

    correction_basis_valid = (
        len(ledger) == 10
        and aggregate.get("condition_result_count") == 10
        and aggregate.get("ordered_condition_count") == 10
        and aggregate.get("all_ten_conditions_evaluated") is True
        and aggregate.get("condition_ledger_populated") is True
        and posture.get("heterogeneous_condition_matrix_recorded") is True
        and posture.get("operation_exhausted") is True
        and posture.get("completed_operation_result_posture_count") == 1
        and value.get("failed_check_count") == 0
        and exact_check_valid
        and rows_valid
        and all_sections_valid
        and posture_projection_valid
    )
    if not _add_check(
        checks,
        "successor.correction_basis",
        correction_basis_valid,
        "CORRECTION_BASIS_INVALID",
    ):
        return "CORRECTION_BASIS_INVALID", "one-field correction basis is incomplete", validation, preservation

    validation.update(
        {
            "strict_content_validated": True,
            "surface_validated": True,
            "artifact_validated": True,
            "identity_and_recorded_result_validated": True,
            "check_counts_validated": True,
            "completion_and_null_route_validated": True,
            "three_admissibility_evaluations_validated": True,
            "aggregate_matrix_validated": True,
            "ten_row_ledger_validated": True,
            "result_no_partial_ledger_check_validated": True,
            "contradictory_false_field_validated": True,
        }
    )
    preservation["all_unaffected_sections_exactly_equivalent"] = True
    return None, None, validation, preservation


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    posture = result.get("successor_posture")
    correction = result.get("correction_posture")
    return {
        "outcome": result.get("outcome"),
        "successor_result": result.get("successor_result"),
        "successor_id": SUCCESSOR_ID,
        "successor_type": SUCCESSOR_TYPE,
        "successor_version": SUCCESSOR_VERSION,
        "successor_scope": SUCCESSOR_SCOPE,
        "prior_operation_id": PRIOR_OPERATION_ID,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "contradiction_id": CONTRADICTION_ID,
        "contradictory_field_path": CONTRADICTORY_FIELD_PATH,
        "prior_no_partial_ledger_standing": (
            correction.get("prior_no_partial_ledger_standing")
            if isinstance(correction, Mapping)
            else None
        ),
        "successor_no_partial_ledger_standing": (
            correction.get("successor_no_partial_ledger_standing")
            if isinstance(correction, Mapping)
            else None
        ),
        "successor_correction_recorded": (
            posture.get("successor_correction_recorded")
            if isinstance(posture, Mapping)
            else False
        ),
        "v1_operation_remains_recorded": (
            correction.get("v1_operation_remains_recorded")
            if isinstance(correction, Mapping)
            else False
        ),
        "v1_matrix_remains_complete": (
            correction.get("v1_matrix_remains_complete")
            if isinstance(correction, Mapping)
            else False
        ),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "result_level_non_claims_canonical_false": True,
        "admissible_future_route": None,
        "open_is_not_next": True,
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    *,
    code: str | None = None,
    reason: str | None = None,
    request_validated: bool = False,
    specification_validation: Mapping[str, Any] | None = None,
    prior_validation: Mapping[str, Any] | None = None,
    unaffected_preservation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    completed = outcome == OUTCOME_RECORDED
    checks_copy = copy.deepcopy(list(checks))
    passed_count = sum(item.get("passed") is True for item in checks_copy)
    failed_count = sum(item.get("passed") is False for item in checks_copy)
    correction = {
        "contradiction_id": CONTRADICTION_ID if completed else None,
        "contradictory_field_path": CONTRADICTORY_FIELD_PATH if completed else None,
        "prior_no_partial_ledger_standing": False if completed else None,
        "successor_no_partial_ledger_standing": True if completed else None,
        "no_partial_ledger_standing_corrected": completed,
        "prior_operation_result_preserved": completed,
        "prior_operation_artifact_preserved": completed,
        "prior_operation_artifact_overwritten": False,
        "prior_operation_posture_overwritten": False,
        "successor_is_additive": completed,
        "correction_scope_stayed_one_field_only": completed,
        "v1_operation_remains_recorded": completed,
        "v1_operation_remains_exhausted": completed,
        "v1_matrix_remains_complete": completed,
    }
    successor_posture = {
        "successor_basis_supplied": completed,
        "successor_basis_admitted": completed,
        "contradiction_evaluated": completed,
        "successor_correction_recorded": completed,
        "successor_exhausted": completed,
        "completed_successor_result_posture_count": 1 if completed else 0,
        "corrected_field_selected": completed,
        "no_second_semantic_change": completed,
        "no_condition_reevaluation": True,
        "raw_signal_or_zip_bytes_read": False,
        "repair_performed": False,
        "repository_scan_performed": False,
        "file_discovery_performed": False,
        "source_reconstruction_performed": False,
        "latest_file_selection_performed": False,
        "admissible_future_route": None,
    }
    successor_object = {
        "successor_id": SUCCESSOR_ID,
        "successor_type": SUCCESSOR_TYPE,
        "successor_version": SUCCESSOR_VERSION,
        "successor_scope": SUCCESSOR_SCOPE,
        "prior_operation_id": PRIOR_OPERATION_ID,
        "selected_matter_class": SELECTED_MATTER_CLASS,
        "successor_result": (
            SUCCESSOR_RESULT_RECORDED
            if completed
            else SUCCESSOR_RESULT_NOT_EVALUATED
        ),
        "successor_no_partial_ledger_standing": True if completed else None,
        "successor_correction_recorded": completed,
        "successor_exhausted": completed,
        "condition_reevaluation_performed": False,
        "v1_artifact_overwritten": False,
        "repair_performed": False,
        "admissible_future_route": None,
    }
    result: dict[str, Any] = {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "successor_result": (
            SUCCESSOR_RESULT_RECORDED
            if completed
            else SUCCESSOR_RESULT_NOT_EVALUATED
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "completed_successor_result_posture_count": 1 if completed else 0,
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
            "successor_id": SUCCESSOR_ID,
            "successor_type": SUCCESSOR_TYPE,
            "successor_version": SUCCESSOR_VERSION,
            "successor_scope": SUCCESSOR_SCOPE,
            "prior_operation_id": PRIOR_OPERATION_ID,
            "selected_matter_class": SELECTED_MATTER_CLASS,
            "governing_specification_path": str(
                GOVERNING_SPECIFICATION_RELATIVE_PATH
            ),
            "governing_specification_sha256": GOVERNING_SPECIFICATION_SHA256,
            "prior_operation_artifact_path": str(
                PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH
            ),
            "prior_operation_artifact_sha256": PRIOR_OPERATION_ARTIFACT_SHA256,
            "deterministic": True,
            "current_clock_used": False,
            "network_used": False,
            "randomness_used": False,
        },
        DECLARED_REQUEST_KEY: (
            copy.deepcopy(dict(request))
            if request_validated
            else {
                "request_mapping_supplied": isinstance(request, Mapping)
                and bool(request),
                "canonical_request_validated": False,
                "caller_payload_values_returned": False,
            }
        ),
        "canonical_request_validation": {
            "request_validated": request_validated,
            "exact_schema_validated": request_validated,
            "one_field_difference_request_validated": request_validated,
            "second_correction_absent": request_validated,
            "semantic_payload_absent": request_validated,
        },
        "specification_validation": copy.deepcopy(
            specification_validation
            if specification_validation is not None
            else _empty_validation(
                GOVERNING_SPECIFICATION_RELATIVE_PATH,
                GOVERNING_SPECIFICATION_SHA256,
            )
        ),
        "prior_v1_artifact_validation": copy.deepcopy(
            prior_validation
            if prior_validation is not None
            else _empty_validation(
                PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH,
                PRIOR_OPERATION_ARTIFACT_SHA256,
            )
        ),
        "contradiction_validation": {
            "contradiction_id": CONTRADICTION_ID,
            "contradictory_field_path": CONTRADICTORY_FIELD_PATH,
            "prior_field_value": False if completed else None,
            "successor_field_value": True if completed else None,
            "contradiction_scope": CONTRADICTION_SCOPE,
            "contradiction_validated": completed,
            "contradiction_affects_operation_result": False,
            "contradiction_affects_condition_ledger": False,
            "contradiction_affects_aggregate_matrix": False,
            "contradiction_affects_admissibility": False,
            "contradiction_affects_non_claims": False,
            "contradiction_affects_future_route": False,
        },
        "exact_one_field_difference": (
            copy.deepcopy(ONE_FIELD_DIFFERENCE_CONTRACT)
            if completed
            else {
                "field_path": None,
                "prior_value": None,
                "successor_value": None,
                "correction_reason": None,
                "prior_value_preserved_as_historical": False,
                "successor_value_appended": False,
            }
        ),
        "unaffected_standing_preservation": copy.deepcopy(
            unaffected_preservation
            if unaffected_preservation is not None
            else {
                "section_sha256": copy.deepcopy(UNAFFECTED_SECTION_SHA256),
                "observed_section_sha256": {},
                "operation_posture_except_contradiction_sha256": (
                    OPERATION_POSTURE_EXCEPT_CONTRADICTION_SHA256
                ),
                "observed_operation_posture_except_contradiction_sha256": None,
                "all_unaffected_sections_exactly_equivalent": False,
                "complete_v1_body_omitted": True,
                "full_ledger_omitted": True,
            }
        ),
        "chronology_preservation": {
            "append_only_order": copy.deepcopy(list(CHRONOLOGY)),
            "chronology_validated": completed,
            "earlier_turns_remain_historically_true": completed,
            "v1_artifact_remains_historical_standing": True,
        },
        "successor_posture": successor_posture,
        "correction_posture": correction,
        SUCCESSOR_KEY: successor_object,
        "lineage_preservation_posture": {
            "v1_artifact_digest_pinned": True,
            "v1_artifact_preserved_without_overwrite": completed,
            "v1_operation_result_preserved": completed,
            "v1_operation_exhaustion_preserved": completed,
            "v1_false_field_preserved_as_historical": completed,
            "v2_true_field_appended": completed,
            "condition_ledger_preserved_without_reemission": completed,
            "aggregate_matrix_preserved_without_recalculation": completed,
            "all_unaffected_semantic_standing_preserved": completed,
            "append_only_lineage_preserved": completed,
        },
        "omission_posture": _canonical_omission_posture(),
        "non_claims": _canonical_non_claims(),
        "result_level_non_claims_canonical_false": True,
        NON_MEANING_KEY: _canonical_non_meaning(),
        "blocked_conversions": list(BLOCKED_CONVERSIONS),
        STATEMENT_KEY: {
            "one_v1_artifact_consumed": completed,
            "one_field_contradiction_evaluated": completed,
            "one_additive_successor_correction_recorded": completed,
            "successor_no_partial_ledger_standing": True if completed else None,
            "v1_operation_remains_recorded": completed,
            "v1_matrix_remains_complete": completed,
            "no_condition_reevaluation": True,
            "no_v1_artifact_overwrite": True,
            "repair_performed": False,
            "future_route_is_null": True,
        },
        CHECKS_KEY: checks_copy,
        "what_remains_open": list(WHAT_REMAINS_OPEN),
    }
    result[SUMMARY_KEY] = _summary_from_result(result)
    return result


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_default_result() -> dict[str, Any]:
    """Return the pure pre-execution successor posture without filesystem reads."""
    checks = [_check("execution.not_started", False, "NOT_EXECUTED")]
    return _build_result(
        {},
        OUTCOME_BLOCKED,
        checks,
        code="NOT_EXECUTED",
        reason="successor resolution has not been executed",
    )


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_result() -> dict[str, Any]:
    """Compatibility alias for the pure default successor constructor."""
    return build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_default_result()


def resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2(
    request: Mapping[str, Any] | None = None,
    *,
    governing_specification_path: Path | str | None = None,
    prior_operation_artifact_path: Path | str | None = None,
) -> dict[str, Any]:
    """Resolve one exact additive successor from two explicitly governed paths."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared = _new_canonical_request()
    elif not isinstance(request, Mapping):
        _add_check(checks, "request.mapping", False, "REQUEST_NOT_MAPPING")
        return _build_result(
            {},
            OUTCOME_BLOCKED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared successor request is not a mapping",
        )
    else:
        declared = copy.deepcopy(dict(request))

    code, reason = _validate_request(declared, checks)
    if code is not None:
        return _build_result(
            declared,
            OUTCOME_BLOCKED,
            checks,
            code=code,
            reason=reason,
        )

    spec_path = (
        GOVERNING_SPECIFICATION_PATH
        if governing_specification_path is None
        else governing_specification_path
    )
    prior_path = (
        PRIOR_OPERATION_ARTIFACT_PATH
        if prior_operation_artifact_path is None
        else prior_operation_artifact_path
    )
    code, reason, specification_validation = _validate_specification(
        spec_path, checks
    )
    if code is not None:
        return _build_result(
            declared,
            OUTCOME_BLOCKED,
            checks,
            code=code,
            reason=reason,
            request_validated=True,
            specification_validation=specification_validation,
        )
    code, reason, prior_validation, unaffected_preservation = _validate_v1_artifact(
        prior_path, checks
    )
    if code is not None:
        return _build_result(
            declared,
            OUTCOME_BLOCKED,
            checks,
            code=code,
            reason=reason,
            request_validated=True,
            specification_validation=specification_validation,
            prior_validation=prior_validation,
            unaffected_preservation=unaffected_preservation,
        )

    final_checks = (
        ("successor.exact_one_field_difference", True, "SECOND_SEMANTIC_CHANGE_REQUESTED"),
        ("successor.no_second_semantic_change", True, "SECOND_SEMANTIC_CHANGE_REQUESTED"),
        ("successor.unaffected_standing_preserved", True, "V1_UNAFFECTED_STANDING_CHANGED"),
        ("successor.raw_signal_and_zip_not_read", True, "EXCLUDED_READ_REQUESTED"),
        ("successor.non_claims_canonical_false", True, "NON_CLAIM_MISSING_OR_FLIPPED"),
        ("successor.future_route_null", True, "DOWNSTREAM_STANDING_PRECLAIMED"),
        ("successor.no_overwrite_repair_discovery_or_reconstruction", True, "EXCLUDED_READ_REQUESTED"),
        ("successor.append_only_chronology", True, "V1_UNAFFECTED_STANDING_CHANGED"),
    )
    for check_id, passed, block_code in final_checks:
        _add_check(checks, check_id, passed, block_code)
    return _build_result(
        declared,
        OUTCOME_RECORDED,
        checks,
        request_validated=True,
        specification_validation=specification_validation,
        prior_validation=prior_validation,
        unaffected_preservation=unaffected_preservation,
    )


def resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_from_path(
    request_path: Path | str,
    **resolver_paths: Any,
) -> dict[str, Any]:
    """Strictly load one explicit request object and resolve the successor."""
    value, _, error = _read_json(request_path)
    if error is not None or value is None:
        checks = [
            _check(
                "request_path.strict_duplicate_key_free_json_mapping",
                False,
                "REQUEST_JSON_INVALID",
            )
        ]
        return _build_result(
            {},
            OUTCOME_BLOCKED,
            checks,
            code="REQUEST_JSON_INVALID",
            reason=(
                "explicit request is missing, malformed, duplicate-keyed, "
                "non-finite, or not an object"
            ),
        )
    return resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2(
        value,
        **resolver_paths,
    )


def _checks_valid(result: Mapping[str, Any]) -> bool:
    checks = result.get(CHECKS_KEY)
    if not isinstance(checks, list) or not checks:
        return False
    if any(
        not isinstance(item, Mapping)
        or set(item)
        != {"check_id", "passed", "block_code", "failure_code", "expected"}
        or type(item.get("passed")) is not bool
        or (
            item.get("passed") is False
            and (
                item.get("block_code") not in BLOCK_CODES
                or item.get("failure_code") not in BLOCK_CODES
            )
        )
        or (
            item.get("passed") is True
            and (
                item.get("block_code") is not None
                or item.get("failure_code") is not None
            )
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


def _contains_complete_v1_material(
    value: Any,
    *,
    parent_key: str | None = None,
) -> bool:
    forbidden = {
        "condition_ledger",
        "condition_evaluations",
        "aggregate_matrix_posture",
        "complete_v1_result",
        "complete_v1_artifact_body",
        "raw_signal_body",
        "zip_bytes",
        "archive_bytes",
    }
    if isinstance(value, Mapping):
        for key, item in value.items():
            if parent_key not in {"section_sha256", "observed_section_sha256"}:
                if key in forbidden:
                    return True
            if _contains_complete_v1_material(item, parent_key=key):
                return True
        return False
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_complete_v1_material(item) for item in value)
    return False


def _structural_result_valid(result: Mapping[str, Any]) -> bool:
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
        or result.get("outcome") not in OUTCOME_FAMILY
        or result.get("admissible_future_route") is not None
    ):
        return False
    if not _checks_valid(result) or _contains_complete_v1_material(result):
        return False
    if (
        not _canonical_false_mapping(result.get("non_claims"))
        or result.get("result_level_non_claims_canonical_false") is not True
        or result.get("omission_posture") != _canonical_omission_posture()
        or result.get(NON_MEANING_KEY) != _canonical_non_meaning()
        or result.get("blocked_conversions") != list(BLOCKED_CONVERSIONS)
        or result.get("what_remains_open") != list(WHAT_REMAINS_OPEN)
    ):
        return False
    completed = result.get("outcome") == OUTCOME_RECORDED
    block = result.get("block")
    posture = result.get("successor_posture")
    correction = result.get("correction_posture")
    successor = result.get(SUCCESSOR_KEY)
    if (
        not isinstance(block, Mapping)
        or block.get("blocked") is completed
        or not isinstance(posture, Mapping)
        or not isinstance(correction, Mapping)
        or not isinstance(successor, Mapping)
    ):
        return False
    expected_result = (
        SUCCESSOR_RESULT_RECORDED
        if completed
        else SUCCESSOR_RESULT_NOT_EVALUATED
    )
    if (
        result.get("successor_result") != expected_result
        or successor.get("successor_result") != expected_result
        or posture.get("successor_correction_recorded") is not completed
        or posture.get("successor_exhausted") is not completed
        or posture.get("completed_successor_result_posture_count")
        != (1 if completed else 0)
        or successor.get("admissible_future_route") is not None
    ):
        return False
    if completed:
        if (
            result.get("failed_check_count") != 0
            or correction.get("prior_no_partial_ledger_standing") is not False
            or correction.get("successor_no_partial_ledger_standing") is not True
            or correction.get("no_partial_ledger_standing_corrected") is not True
            or correction.get("correction_scope_stayed_one_field_only") is not True
            or result.get("exact_one_field_difference")
            != ONE_FIELD_DIFFERENCE_CONTRACT
            or result.get("unaffected_standing_preservation", {}).get(
                "all_unaffected_sections_exactly_equivalent"
            )
            is not True
        ):
            return False
    else:
        if (
            correction.get("prior_no_partial_ledger_standing") is not None
            or correction.get("successor_no_partial_ledger_standing") is not None
            or correction.get("no_partial_ledger_standing_corrected") is not False
        ):
            return False
    return result.get(SUMMARY_KEY) == _summary_from_result(result)


def build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return the compact projection of a compatible successor result."""
    if not isinstance(result, Mapping) or not _structural_result_valid(result):
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinV2Error(
            "summary requires a compatible v2 successor result"
        )
    return copy.deepcopy(_summary_from_result(result))


def _canonical_completed_result_matches(result: Mapping[str, Any]) -> bool:
    if not _structural_result_valid(result) or result.get("outcome") != OUTCOME_RECORDED:
        return False
    declared = result.get(DECLARED_REQUEST_KEY)
    if not isinstance(declared, Mapping) or not _exact(
        declared, _new_canonical_request()
    ):
        return False
    expected = resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2(
        _new_canonical_request()
    )
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
            PRIOR_OPERATION_ARTIFACT_PATH.parent.resolve(),
        )
        return (
            OUTPUT_ROOT.name == CANONICAL_OUTPUT_ROOT.name
            and resolved == canonical
            and _path_within(resolved, root)
            and not any(_path_within(resolved, item) for item in protected)
        )
    except (OSError, RuntimeError, TypeError, ValueError):
        return False


def write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one exact canonical successor result without overwriting."""
    if not isinstance(result, Mapping) or not _canonical_completed_result_matches(result):
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinV2Error(
            "WRITE_REFUSED: malformed, inconsistent, or noncanonical successor result"
        )
    try:
        target = (
            Path(output_path)
            if output_path is not None
            else OUTPUT_ROOT / OUTPUT_FILENAME
        )
    except (TypeError, ValueError) as exc:
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinV2Error(
            "WRITE_REFUSED: invalid output path"
        ) from exc
    if not _output_path_allowed(target):
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinV2Error(
            "WRITE_REFUSED: output path is outside the exact canonical v2 result path"
        )
    if target.exists():
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinV2Error(
            "WRITE_REFUSED: canonical v2 result path already exists"
        )
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8", newline="\n") as handle:
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
        raise BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinV2Error(
            "WRITE_REFUSED: unable to write canonical v2 successor result"
        ) from exc
    return target
