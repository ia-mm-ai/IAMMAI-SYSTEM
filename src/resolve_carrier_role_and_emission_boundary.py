"""Bounded carrier role and emission boundary resolver.

This resolver records whether one carrier may hold one declared operation-local
role, and whether that carrier may emit one declared emission class under that
role. It does not create sourcehood, currentness, authority, permission,
successor standing, body formation, multi-carrier law, distributed standing,
signal posture, presence, threshold, truth, action, consequence, or
continuation.

The module is intentionally self-contained and imports no repository-local
modules. It records role and emission posture only; it does not perform
body-line admission, carrier relation, receipt, correspondence, conformance, or
self-orientation.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CarrierRoleAndEmissionBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit role/emission inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


CARRIER_ROLE_AND_EMISSION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_carrier_role_and_emission_boundary"
)

RESOLVER_MODULE = "resolve_carrier_role_and_emission_boundary"
RESULT_VERSION = "0.1.0"

CARRIER_ROLE_RECOGNIZED = "CARRIER_ROLE_RECOGNIZED"
CARRIER_EMISSION_RECOGNIZED = "CARRIER_EMISSION_RECOGNIZED"
CARRIER_ROLE_EMISSION_BLOCKED = "CARRIER_ROLE_EMISSION_BLOCKED"

ADMITTED_CARRIER_ROLES = {
    "SOURCE_CARRIER_FOR_PACKET",
    "RECEIVING_CARRIER",
    "HOLDING_CARRIER",
    "RETURNING_CARRIER",
    "REFUSING_CARRIER",
}

CANDIDATE_CARRIER_ROLES = {
    "WITNESS_CARRIER",
    "COMPARISON_CARRIER",
    "EMITTING_CARRIER",
    "STALE_CARRIER",
    "SUCCESSOR_CARRIER",
}

PERMITTED_EMISSIONS_BY_ROLE: dict[str, set[str]] = {
    "SOURCE_CARRIER_FOR_PACKET": {
        "CARRIED_PACKET",
        "PACKET_MANIFEST",
        "INTEGRITY_EVIDENCE",
        "TRANSFER_DECLARATION",
    },
    "RECEIVING_CARRIER": {
        "CARRIED_SURFACE_RECEIPT",
        "RECEIPT_BLOCK",
        "RECEIPT_REFUSAL_REASON",
    },
    "HOLDING_CARRIER": {
        "PASSIVE_STORAGE_STATUS",
    },
    "RETURNING_CARRIER": {
        "RETURNED_RECEIPT_EVIDENCE",
        "RETURNED_BLOCKED_RECEIPT_EVIDENCE",
        "RETURNED_EVIDENCE_PACKET",
    },
    "REFUSING_CARRIER": {
        "RECEIPT_BLOCK",
        "RECEIPT_REFUSAL_REASON",
        "FAILED_CHECKS",
        "PRESERVED_BASIS",
    },
}

NOT_ADMITTED_EMISSION_CLASSES = {
    "SELF_ORIENTATION",
    "BODY_CONFORMANCE",
    "CURRENTNESS",
    "STANDING_UPGRADE",
    "SOURCE_AUTHORITY",
    "SUCCESSOR_ARTIFACT",
    "PRESENCE",
    "THRESHOLD",
    "TRUTH",
    "ACTION",
    "CONSEQUENCE",
    "MULTI_CARRIER_RELATION",
    "DISTRIBUTED_STANDING",
    "CARRIER_REGISTRY",
    "REPOSITORY_SYNCHRONIZATION",
    "SIGNAL_BY_DEFAULT",
    "BODY_RELEVANCE_MEDIUM",
    "WORKFLOW",
    "ROUTING",
    "CONTINUATION_AUTHORIZATION",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "carrier_role_became_permanent_identity": False,
    "carrier_role_created_source": False,
    "carrier_role_created_currentness": False,
    "carrier_role_created_authority": False,
    "carrier_role_created_permission": False,
    "carrier_role_created_successor": False,
    "carrier_role_created_body": False,
    "carrier_emission_self_admitted": False,
    "carrier_emission_created_signal_by_default": False,
    "presence_established": False,
    "threshold_met": False,
    "truth_created": False,
    "action_authorized": False,
    "consequence_created": False,
    "multi_carrier_law_created": False,
    "distributed_standing_created": False,
    "continuation_authorized": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_CARRIER_OPERATION_MISSING": "No declared carrier operation was supplied.",
    "DECLARED_CARRIER_OPERATION_UNREADABLE": "The declared carrier operation path could not be read.",
    "DECLARED_CARRIER_OPERATION_MALFORMED": "The declared carrier operation is not a JSON object or mapping.",
    "CARRIER_ROLE_UNDECLARED": "Carrier role is undeclared.",
    "CARRIER_ROLE_UNSUPPORTED": "Carrier role is unsupported or not admitted in this version.",
    "CARRIER_ROLE_CLAIMS_PERMANENT_IDENTITY": "Carrier role claims permanent identity.",
    "CARRIER_ROLE_CREATES_SOURCE": "Carrier role creates source posture.",
    "CARRIER_ROLE_CREATES_CURRENTNESS": "Carrier role creates currentness.",
    "CARRIER_ROLE_CREATES_AUTHORITY": "Carrier role creates authority.",
    "CARRIER_ROLE_CREATES_PERMISSION": "Carrier role creates permission.",
    "CARRIER_ROLE_CREATES_SUCCESSOR": "Carrier role creates successor standing.",
    "CARRIER_ROLE_CREATES_BODY": "Carrier role creates body formation.",
    "SELECTED_CARRIER_MISSING": "Selected carrier identity is missing.",
    "CARRIER_OPERATION_PURPOSE_UNDECLARED": "Carrier operation purpose is undeclared.",
    "CARRIER_EMISSION_UNDECLARED": "Carrier emission class is undeclared.",
    "CARRIER_EMISSION_UNSUPPORTED": "Carrier emission class is unsupported.",
    "CARRIER_EMISSION_OUTSIDE_ROLE": "Carrier emission class is outside the declared role.",
    "RECEIVING_CARRIER_EMITS_SELF_ORIENTATION": "Receiving carrier attempts to emit self-orientation.",
    "RECEIVING_CARRIER_EMITS_CONFORMANCE": "Receiving carrier attempts to emit conformance.",
    "HOLDING_CARRIER_CLAIMS_RECEIPT": "Holding carrier attempts to claim lawful receipt.",
    "RETURNING_CARRIER_ALTERS_RECEIPT_MEANING": "Returning carrier alters receipt meaning.",
    "REFUSING_CARRIER_INVALIDATES_SOURCE": "Refusing carrier attempts to invalidate the source surface.",
    "CARRIER_EMISSION_SELF_ADMITS": "Carrier emission self-admits into the body line.",
    "CARRIER_EMISSION_CREATES_SIGNAL_BY_DEFAULT": "Carrier emission creates signal by default.",
    "CARRIER_EMISSION_ESTABLISHES_PRESENCE": "Carrier emission establishes presence.",
    "CARRIER_EMISSION_ESTABLISHES_THRESHOLD": "Carrier emission establishes threshold.",
    "CARRIER_EMISSION_CREATES_TRUTH": "Carrier emission creates truth.",
    "CARRIER_EMISSION_AUTHORIZES_ACTION": "Carrier emission authorizes action.",
    "CARRIER_EMISSION_CREATES_CONSEQUENCE": "Carrier emission creates consequence.",
    "CARRIER_EMISSION_CREATES_MULTI_CARRIER_LAW": "Carrier emission creates multi-carrier law.",
    "CARRIER_EMISSION_CREATES_DISTRIBUTED_STANDING": "Carrier emission creates distributed standing.",
    "CARRIER_EMISSION_AUTHORIZES_CONTINUATION": "Carrier emission authorizes continuation.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency is treated as currentness.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required carrier role/emission non-claim is missing or flipped.",
}

ROLE_DOES_NOT_MEAN = {
    "does_not_mean_permanent_identity": True,
    "does_not_mean_source": True,
    "does_not_mean_currentness": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_successor": True,
    "does_not_mean_body": True,
    "does_not_mean_participant_by_default": True,
    "does_not_mean_multi_carrier_law": True,
    "does_not_mean_distributed_standing": True,
    "does_not_mean_presence": True,
    "does_not_mean_threshold": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_consequence": True,
    "does_not_mean_continuation": True,
}

EMISSION_DOES_NOT_MEAN = {
    "does_not_mean_body_line_admission": True,
    "does_not_mean_source": True,
    "does_not_mean_currentness": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_successor": True,
    "does_not_mean_body": True,
    "does_not_mean_signal_by_default": True,
    "does_not_mean_presence": True,
    "does_not_mean_threshold": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_consequence": True,
    "does_not_mean_carrier_relation": True,
    "does_not_mean_multi_carrier_law": True,
    "does_not_mean_distributed_standing": True,
    "does_not_mean_continuation": True,
}

OPEN_SURFACES = [
    "carrier return/admission boundary",
    "cross-carrier divergence boundary",
    "cross-carrier currentness boundary",
    "multi-carrier relation law",
    "multi-carrier relation conformance",
    "multi-carrier relation closure",
    "distributed standing",
    "persistence/registry law",
    "presence law",
    "threshold law",
    "truth law",
    "action/consequence law",
    "generalized vessel relation lifecycle",
    "body relevance medium",
    "signal series or accumulation logic",
    "successor carrier law",
    "future self-orientation successor only if separately justified",
]


def resolve_carrier_role_and_emission_boundary(
    declared_carrier_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declared carrier operation mapping."""

    precheck_failures: list[str] = []
    if declared_carrier_operation is None:
        operation: dict[str, Any] = {}
        precheck_failures.append("DECLARED_CARRIER_OPERATION_MISSING")
    elif not isinstance(declared_carrier_operation, Mapping):
        operation = {}
        precheck_failures.append("DECLARED_CARRIER_OPERATION_MALFORMED")
    else:
        operation = copy.deepcopy(dict(declared_carrier_operation))

    return _resolve_operation(operation, precheck_failures)


def resolve_carrier_role_and_emission_boundary_from_path(
    declared_carrier_operation_path: Path | str,
) -> dict[str, Any]:
    """Resolve one declared carrier operation JSON path."""

    precheck_failures: list[str] = []
    try:
        operation = _read_json_mapping(declared_carrier_operation_path)
        operation["_declared_carrier_operation_path"] = str(
            Path(declared_carrier_operation_path)
        )
    except CarrierRoleAndEmissionBoundaryError as exc:
        operation = {}
        precheck_failures.append(exc.block_code)
    return _resolve_operation(operation, precheck_failures)


def write_carrier_role_and_emission_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded carrier role/emission result without overwriting."""

    if output_path is None:
        operation = _as_mapping(result.get("declared_carrier_operation"))
        role_basis = _as_mapping(result.get("carrier_role_basis"))
        operation_id = (
            operation.get("operation_id")
            or role_basis.get("role_name")
            or "carrier_role_operation"
        )
        filename = f"{_safe_filename_part(operation_id)}__carrier_role_emission_result.json"
        target = CARRIER_ROLE_AND_EMISSION_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)

    target = _non_overwriting_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    return target


def build_carrier_role_and_emission_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary for a role/emission result."""

    role_checks = _mapping_list(result.get("role_checks"))
    emission_checks = _mapping_list(result.get("emission_checks"))
    checks = role_checks + emission_checks
    operation = _as_mapping(result.get("declared_carrier_operation"))
    selected_carrier = _as_mapping(result.get("selected_carrier"))
    role_basis = _as_mapping(result.get("carrier_role_basis"))
    emission_basis = _as_mapping(result.get("emission_basis"))
    role_statement = _as_mapping(result.get("role_statement"))
    emission_statement = _as_mapping(result.get("emission_statement"))
    non_claims = _as_mapping(result.get("non_claims"))
    block = _as_mapping(result.get("block"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "operation_id": operation.get("operation_id"),
        "operation_purpose": operation.get("operation_purpose"),
        "selected_carrier_id": selected_carrier.get("carrier_id"),
        "selected_carrier_label": selected_carrier.get("carrier_label"),
        "declared_carrier_role": role_basis.get("role_name"),
        "declared_emission_class": emission_basis.get("emission_class"),
        "role_recognized": bool(role_statement.get("carrier_role_recognized")),
        "emission_recognized": bool(
            emission_statement.get("carrier_emission_recognized")
        ),
        "role_operation_local": bool(
            role_statement.get("carrier_role_operation_local")
        ),
        "role_permanent_identity": bool(
            role_statement.get("carrier_role_permanent_identity")
        ),
        "emission_local_only": bool(
            emission_statement.get("carrier_emission_local_only")
        ),
        "emission_self_admitted": bool(
            emission_statement.get("carrier_emission_self_admitted")
        ),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "source_created": bool(
            non_claims.get("carrier_role_created_source")
            or non_claims.get("source_replaced")
        ),
        "currentness_created": bool(
            non_claims.get("currentness_created")
            or non_claims.get("carrier_role_created_currentness")
        ),
        "authority_created": bool(
            non_claims.get("authority_created")
            or non_claims.get("carrier_role_created_authority")
        ),
        "permission_created": bool(
            non_claims.get("permission_created")
            or non_claims.get("carrier_role_created_permission")
        ),
        "successor_created": bool(non_claims.get("carrier_role_created_successor")),
        "body_created": bool(non_claims.get("carrier_role_created_body")),
        "signal_created_by_default": bool(
            non_claims.get("carrier_emission_created_signal_by_default")
        ),
        "presence_established": bool(non_claims.get("presence_established")),
        "threshold_met": bool(non_claims.get("threshold_met")),
        "truth_created": bool(non_claims.get("truth_created")),
        "action_authorized": bool(non_claims.get("action_authorized")),
        "consequence_created": bool(non_claims.get("consequence_created")),
        "multi_carrier_law_created": bool(non_claims.get("multi_carrier_law_created")),
        "distributed_standing_created": bool(
            non_claims.get("distributed_standing_created")
        ),
        "continuation_authorized": bool(non_claims.get("continuation_authorized")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_carrier_operation(
    operation_id: str,
    operation_purpose: str,
    selected_carrier_id: str,
    declared_carrier_role: str,
    declared_emission_class: str | None = None,
    selected_packet_or_surface: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a minimum valid declared carrier operation.

    This helper does not infer source authority, currentness, permission, body
    standing, or body-line admission.
    """

    operation: dict[str, Any] = {
        "operation_id": operation_id,
        "operation_purpose": operation_purpose,
        "operation_scope": "declared_operation_local",
        "selected_carrier": {
            "carrier_id": selected_carrier_id,
            "carrier_role_for_operation": declared_carrier_role,
            "carrier_role_operation_local": True,
            "carrier_role_permanent_identity": False,
        },
        "declared_carrier_role": declared_carrier_role,
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }
    if declared_emission_class is not None:
        operation["declared_emission_class"] = declared_emission_class
    if selected_packet_or_surface is not None:
        operation["selected_packet_or_surface"] = copy.deepcopy(
            dict(selected_packet_or_surface)
        )
    return operation


def _resolve_operation(
    operation: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    operation_mapping = _as_mapping(operation)
    declared_role_raw = _first_text(operation_mapping, ("declared_carrier_role", "carrier_role"))
    declared_role = _normalize_token(declared_role_raw)
    declared_emission_raw = _first_text(
        operation_mapping,
        ("declared_emission_class", "emission_class", "carrier_emission_class"),
    )
    declared_emission = _normalize_token(declared_emission_raw)
    emission_requested = _emission_requested(operation_mapping, declared_emission)
    selected_carrier = _normalize_selected_carrier(
        operation_mapping.get("selected_carrier"),
        declared_role,
    )
    declared_non_claims = _as_mapping(operation_mapping.get("declared_non_claims"))
    non_claims = _merge_non_claims(declared_non_claims)
    declared_operation = _declared_operation_basis(
        operation_mapping,
        declared_role,
        declared_emission,
    )
    role_basis = _carrier_role_basis(declared_role)
    emission_basis = _emission_basis(
        operation_mapping,
        declared_role,
        declared_emission,
        emission_requested,
    )

    role_checks = _build_role_checks(
        operation_mapping,
        selected_carrier,
        declared_role,
        declared_non_claims,
        precheck_failures,
    )
    emission_checks = _build_emission_checks(
        operation_mapping,
        declared_role,
        declared_emission,
        emission_requested,
        declared_non_claims,
    )
    failed_check = _first_failed(role_checks + emission_checks)

    if failed_check:
        outcome = CARRIER_ROLE_EMISSION_BLOCKED
        block_code = str(failed_check.get("block_code"))
    elif declared_emission:
        outcome = CARRIER_EMISSION_RECOGNIZED
        block_code = None
    else:
        outcome = CARRIER_ROLE_RECOGNIZED
        block_code = None

    block_reason = _block_reason(block_code, failed_check)
    role_recognized = outcome in {
        CARRIER_ROLE_RECOGNIZED,
        CARRIER_EMISSION_RECOGNIZED,
    }
    emission_recognized = outcome == CARRIER_EMISSION_RECOGNIZED

    result: dict[str, Any] = {
        "carrier_role_emission_metadata": {
            "carrier_role_emission_result_id": _result_id(
                operation_mapping,
                declared_role,
                outcome,
            ),
            "carrier_role_emission_result_type": (
                "carrier_role_and_emission_boundary_result"
            ),
            "carrier_role_emission_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_carrier_operation": declared_operation,
        "selected_carrier": selected_carrier,
        "carrier_role_basis": role_basis,
        "emission_basis": emission_basis,
        "role_checks": role_checks,
        "emission_checks": emission_checks,
        "role_statement": _role_statement(role_recognized),
        "emission_statement": _emission_statement(
            emission_recognized,
            declared_emission,
            declared_role,
        ),
        "what_role_does_not_mean": copy.deepcopy(ROLE_DOES_NOT_MEAN),
        "what_emission_does_not_mean": copy.deepcopy(EMISSION_DOES_NOT_MEAN),
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": {
            "code": block_code,
            "reason": block_reason,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["carrier_role_emission_summary"] = (
        build_carrier_role_and_emission_summary(result)
    )
    return result


def _build_role_checks(
    operation: Mapping[str, Any],
    selected_carrier: Mapping[str, Any],
    declared_role: str | None,
    declared_non_claims: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    precheck_code = (
        precheck_failures[0]
        if precheck_failures
        else "DECLARED_CARRIER_OPERATION_MALFORMED"
    )
    checks.append(
        _check(
            "declared_carrier_operation_is_parseable_mapping",
            not precheck_failures,
            "declared carrier operation is a mapping",
            list(precheck_failures),
            precheck_code,
        )
    )
    checks.append(
        _check(
            "carrier_role_declared",
            bool(declared_role),
            "carrier role is declared",
            declared_role,
            "CARRIER_ROLE_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "carrier_role_supported_admitted",
            declared_role in ADMITTED_CARRIER_ROLES,
            "carrier role is admitted for this version",
            {
                "declared_role": declared_role,
                "candidate_not_admitted": declared_role in CANDIDATE_CARRIER_ROLES,
            },
            "CARRIER_ROLE_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "selected_carrier_declared",
            bool(selected_carrier.get("carrier_id") or selected_carrier.get("carrier_label")),
            "selected carrier identity is declared",
            selected_carrier,
            "SELECTED_CARRIER_MISSING",
        )
    )
    checks.append(
        _check(
            "operation_purpose_declared",
            bool(str(operation.get("operation_purpose") or "").strip()),
            "operation purpose is declared and non-empty",
            operation.get("operation_purpose"),
            "CARRIER_OPERATION_PURPOSE_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "carrier_role_is_operation_local",
            _role_is_operation_local(operation, selected_carrier),
            "carrier role is local to one declared operation",
            {
                "operation_scope": operation.get("operation_scope"),
                "carrier_role_operation_local": selected_carrier.get(
                    "carrier_role_operation_local"
                ),
            },
            "CARRIER_ROLE_CLAIMS_PERMANENT_IDENTITY",
        )
    )
    checks.append(
        _check(
            "carrier_role_is_not_permanent_identity",
            not _flag_true(
                [operation, selected_carrier, declared_non_claims],
                (
                    "carrier_role_became_permanent_identity",
                    "carrier_role_permanent_identity",
                    "role_permanent_identity",
                    "permanent_identity_from_role",
                    "carrier_role_claims_permanent_identity",
                ),
            ),
            "carrier role does not become permanent identity",
            {
                "carrier_role_became_permanent_identity": declared_non_claims.get(
                    "carrier_role_became_permanent_identity"
                ),
                "carrier_role_permanent_identity": selected_carrier.get(
                    "carrier_role_permanent_identity"
                ),
            },
            "CARRIER_ROLE_CLAIMS_PERMANENT_IDENTITY",
        )
    )
    checks.extend(
        [
            _check(
                "carrier_role_does_not_create_source",
                not _flag_true(
                    [operation, selected_carrier, declared_non_claims],
                    (
                        "source_replaced",
                        "carrier_role_created_source",
                        "carrier_role_creates_source",
                        "role_creates_source",
                    ),
                ),
                "carrier role creates no source posture",
                {
                    "source_replaced": declared_non_claims.get("source_replaced"),
                    "carrier_role_created_source": declared_non_claims.get(
                        "carrier_role_created_source"
                    ),
                },
                "CARRIER_ROLE_CREATES_SOURCE",
            ),
            _check(
                "carrier_role_does_not_create_currentness",
                not _flag_true(
                    [operation, selected_carrier, declared_non_claims],
                    (
                        "currentness_created",
                        "carrier_role_created_currentness",
                        "carrier_role_creates_currentness",
                        "latest_local_copy_current",
                    ),
                ),
                "carrier role creates no currentness",
                {
                    "currentness_created": declared_non_claims.get(
                        "currentness_created"
                    ),
                    "carrier_role_created_currentness": declared_non_claims.get(
                        "carrier_role_created_currentness"
                    ),
                },
                "CARRIER_ROLE_CREATES_CURRENTNESS",
            ),
            _check(
                "carrier_role_does_not_create_authority",
                not _flag_true(
                    [operation, selected_carrier, declared_non_claims],
                    (
                        "authority_created",
                        "carrier_role_created_authority",
                        "carrier_role_creates_authority",
                    ),
                ),
                "carrier role creates no authority",
                {
                    "authority_created": declared_non_claims.get("authority_created"),
                    "carrier_role_created_authority": declared_non_claims.get(
                        "carrier_role_created_authority"
                    ),
                },
                "CARRIER_ROLE_CREATES_AUTHORITY",
            ),
            _check(
                "carrier_role_does_not_create_permission",
                not _flag_true(
                    [operation, selected_carrier, declared_non_claims],
                    (
                        "permission_created",
                        "carrier_role_created_permission",
                        "carrier_role_creates_permission",
                    ),
                ),
                "carrier role creates no permission",
                {
                    "permission_created": declared_non_claims.get("permission_created"),
                    "carrier_role_created_permission": declared_non_claims.get(
                        "carrier_role_created_permission"
                    ),
                },
                "CARRIER_ROLE_CREATES_PERMISSION",
            ),
            _check(
                "carrier_role_does_not_create_successor",
                not _flag_true(
                    [operation, selected_carrier, declared_non_claims],
                    (
                        "carrier_role_created_successor",
                        "carrier_role_creates_successor",
                        "successor_standing_created",
                    ),
                ),
                "carrier role creates no successor standing",
                declared_non_claims.get("carrier_role_created_successor"),
                "CARRIER_ROLE_CREATES_SUCCESSOR",
            ),
            _check(
                "carrier_role_does_not_create_body",
                not _flag_true(
                    [operation, selected_carrier, declared_non_claims],
                    (
                        "carrier_role_created_body",
                        "carrier_role_creates_body",
                        "body_formed",
                        "body_created",
                    ),
                ),
                "carrier role creates no body formation",
                declared_non_claims.get("carrier_role_created_body"),
                "CARRIER_ROLE_CREATES_BODY",
            ),
            _check(
                "latest_file_currentness_false",
                not _flag_true(
                    [operation, declared_non_claims],
                    ("latest_file_currentness", "latest_file_recency_currentness"),
                ),
                "latest local file is not currentness",
                declared_non_claims.get("latest_file_currentness"),
                "LATEST_FILE_CURRENTNESS",
            ),
            _check(
                "recency_fraud_false",
                not _flag_true(
                    [operation, declared_non_claims],
                    ("recency_fraud", "recency_currentness"),
                ),
                "recency is not used as currentness",
                declared_non_claims.get("recency_fraud"),
                "LATEST_FILE_CURRENTNESS",
            ),
            _check(
                "mutation_replay_merge_false",
                not _flag_true(
                    [operation, declared_non_claims],
                    (
                        "mutation_performed",
                        "replay_performed",
                        "merge_performed",
                        "carriers_merged",
                    ),
                ),
                "mutation, replay, and merge remain false",
                {
                    "mutation_performed": declared_non_claims.get(
                        "mutation_performed"
                    ),
                    "replay_performed": declared_non_claims.get("replay_performed"),
                    "merge_performed": declared_non_claims.get("merge_performed"),
                },
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
            ),
        ]
    )
    missing_or_flipped = _missing_or_flipped_non_claims(declared_non_claims)
    checks.append(
        _check(
            "required_non_claims_remain_false",
            not missing_or_flipped,
            "all required role/emission non-claims are present and false",
            missing_or_flipped,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _build_emission_checks(
    operation: Mapping[str, Any],
    declared_role: str | None,
    declared_emission: str | None,
    emission_requested: bool,
    declared_non_claims: Mapping[str, Any],
) -> list[dict[str, Any]]:
    permitted_for_role = PERMITTED_EMISSIONS_BY_ROLE.get(declared_role or "", set())
    supported_emissions = _supported_emissions()
    checks = [
        _check(
            "emission_class_declared_when_emission_requested",
            (not emission_requested) or bool(declared_emission),
            "emission class is declared when emission is requested",
            {
                "emission_requested": emission_requested,
                "declared_emission_class": declared_emission,
            },
            "CARRIER_EMISSION_UNDECLARED",
        ),
        _check(
            "receiving_carrier_does_not_emit_self_orientation",
            not (
                declared_role == "RECEIVING_CARRIER"
                and declared_emission == "SELF_ORIENTATION"
            ),
            "receiving carrier does not emit self-orientation",
            declared_emission,
            "RECEIVING_CARRIER_EMITS_SELF_ORIENTATION",
        ),
        _check(
            "receiving_carrier_does_not_emit_conformance",
            not (
                declared_role == "RECEIVING_CARRIER"
                and declared_emission == "BODY_CONFORMANCE"
            ),
            "receiving carrier does not emit conformance",
            declared_emission,
            "RECEIVING_CARRIER_EMITS_CONFORMANCE",
        ),
        _check(
            "holding_carrier_does_not_claim_receipt",
            not (
                declared_role == "HOLDING_CARRIER"
                and declared_emission
                in {"CARRIED_SURFACE_RECEIPT", "CARRIED_SURFACE_RECEIVED"}
            ),
            "holding carrier emits passive storage only, not lawful receipt",
            declared_emission,
            "HOLDING_CARRIER_CLAIMS_RECEIPT",
        ),
        _check(
            "returning_carrier_does_not_alter_receipt_meaning",
            not (
                declared_role == "RETURNING_CARRIER"
                and _flag_true(
                    [operation, declared_non_claims],
                    (
                        "returning_carrier_alters_receipt_meaning",
                        "returned_receipt_meaning_altered",
                        "receipt_meaning_altered",
                    ),
                )
            ),
            "returning carrier preserves receipt meaning",
            _flag_true(
                [operation, declared_non_claims],
                (
                    "returning_carrier_alters_receipt_meaning",
                    "returned_receipt_meaning_altered",
                    "receipt_meaning_altered",
                ),
            ),
            "RETURNING_CARRIER_ALTERS_RECEIPT_MEANING",
        ),
        _check(
            "refusing_carrier_does_not_invalidate_source",
            not (
                declared_role == "REFUSING_CARRIER"
                and _flag_true(
                    [operation, declared_non_claims],
                    (
                        "refusing_carrier_invalidates_source",
                        "source_invalidated_by_refusal",
                        "refusal_invalidates_source",
                    ),
                )
            ),
            "refusing carrier preserves source surface status",
            _flag_true(
                [operation, declared_non_claims],
                (
                    "refusing_carrier_invalidates_source",
                    "source_invalidated_by_refusal",
                    "refusal_invalidates_source",
                ),
            ),
            "REFUSING_CARRIER_INVALIDATES_SOURCE",
        ),
        _check(
            "emission_class_supported",
            (not declared_emission)
            or (
                declared_emission in supported_emissions
                and declared_emission not in NOT_ADMITTED_EMISSION_CLASSES
            ),
            "emission class is in the bounded supported set",
            {
                "declared_emission_class": declared_emission,
                "not_admitted_by_default": declared_emission
                in NOT_ADMITTED_EMISSION_CLASSES,
            },
            "CARRIER_EMISSION_UNSUPPORTED",
        ),
        _check(
            "emission_class_permitted_for_role",
            (not declared_emission) or declared_emission in permitted_for_role,
            "emission class is permitted for the declared role",
            {
                "declared_role": declared_role,
                "declared_emission_class": declared_emission,
                "permitted_emissions_for_role": sorted(permitted_for_role),
            },
            "CARRIER_EMISSION_OUTSIDE_ROLE",
        ),
        _check(
            "carrier_local_emission_does_not_self_admit",
            not _flag_true(
                [operation, declared_non_claims],
                (
                    "carrier_emission_self_admitted",
                    "carrier_emission_self_admits",
                    "body_line_admitted",
                    "self_admits_into_body_line",
                ),
            ),
            "carrier-local emission does not self-admit into body line",
            declared_non_claims.get("carrier_emission_self_admitted"),
            "CARRIER_EMISSION_SELF_ADMITS",
        ),
        _check(
            "carrier_emission_does_not_create_signal_by_default",
            not _flag_true(
                [operation, declared_non_claims],
                (
                    "carrier_emission_created_signal_by_default",
                    "carrier_emission_creates_signal_by_default",
                    "signal_created_by_default",
                ),
            ),
            "carrier emission creates no signal by default",
            declared_non_claims.get("carrier_emission_created_signal_by_default"),
            "CARRIER_EMISSION_CREATES_SIGNAL_BY_DEFAULT",
        ),
        _check(
            "carrier_emission_does_not_establish_presence",
            not _flag_true(
                [operation, declared_non_claims],
                ("presence_established", "carrier_emission_establishes_presence"),
            ),
            "carrier emission establishes no presence",
            declared_non_claims.get("presence_established"),
            "CARRIER_EMISSION_ESTABLISHES_PRESENCE",
        ),
        _check(
            "carrier_emission_does_not_establish_threshold",
            not _flag_true(
                [operation, declared_non_claims],
                ("threshold_met", "carrier_emission_establishes_threshold"),
            ),
            "carrier emission establishes no threshold",
            declared_non_claims.get("threshold_met"),
            "CARRIER_EMISSION_ESTABLISHES_THRESHOLD",
        ),
        _check(
            "carrier_emission_does_not_create_truth",
            not _flag_true(
                [operation, declared_non_claims],
                ("truth_created", "carrier_emission_creates_truth"),
            ),
            "carrier emission creates no truth",
            declared_non_claims.get("truth_created"),
            "CARRIER_EMISSION_CREATES_TRUTH",
        ),
        _check(
            "carrier_emission_does_not_authorize_action",
            not _flag_true(
                [operation, declared_non_claims],
                ("action_authorized", "carrier_emission_authorizes_action"),
            ),
            "carrier emission authorizes no action",
            declared_non_claims.get("action_authorized"),
            "CARRIER_EMISSION_AUTHORIZES_ACTION",
        ),
        _check(
            "carrier_emission_does_not_create_consequence",
            not _flag_true(
                [operation, declared_non_claims],
                ("consequence_created", "carrier_emission_creates_consequence"),
            ),
            "carrier emission creates no consequence",
            declared_non_claims.get("consequence_created"),
            "CARRIER_EMISSION_CREATES_CONSEQUENCE",
        ),
        _check(
            "carrier_emission_does_not_create_multi_carrier_law",
            not _flag_true(
                [operation, declared_non_claims],
                (
                    "multi_carrier_law_created",
                    "carrier_emission_creates_multi_carrier_law",
                ),
            ),
            "carrier emission creates no multi-carrier law",
            declared_non_claims.get("multi_carrier_law_created"),
            "CARRIER_EMISSION_CREATES_MULTI_CARRIER_LAW",
        ),
        _check(
            "carrier_emission_does_not_create_distributed_standing",
            not _flag_true(
                [operation, declared_non_claims],
                (
                    "distributed_standing_created",
                    "carrier_emission_creates_distributed_standing",
                ),
            ),
            "carrier emission creates no distributed standing",
            declared_non_claims.get("distributed_standing_created"),
            "CARRIER_EMISSION_CREATES_DISTRIBUTED_STANDING",
        ),
        _check(
            "carrier_emission_does_not_authorize_continuation",
            not _flag_true(
                [operation, declared_non_claims],
                (
                    "continuation_authorized",
                    "carrier_emission_authorizes_continuation",
                    "follow_on_work_authorized",
                    "follow_on_steps_authorized",
                ),
            ),
            "carrier emission authorizes no continuation",
            declared_non_claims.get("continuation_authorized"),
            "CARRIER_EMISSION_AUTHORIZES_CONTINUATION",
        ),
    ]
    return checks


def _role_statement(recognized: bool) -> dict[str, Any]:
    return {
        "carrier_role_recognized": bool(recognized),
        "carrier_role_operation_local": bool(recognized),
        "carrier_role_permanent_identity": False,
        "carrier_role_created_source": False,
        "carrier_role_created_currentness": False,
        "carrier_role_created_authority": False,
        "carrier_role_created_permission": False,
        "carrier_role_created_successor": False,
        "carrier_role_created_body": False,
        "multi_carrier_law_created": False,
        "distributed_standing_created": False,
    }


def _emission_statement(
    recognized: bool,
    emission_class: str | None,
    declared_role: str | None,
) -> dict[str, Any]:
    passive_storage_only = (
        recognized
        and declared_role == "HOLDING_CARRIER"
        and emission_class == "PASSIVE_STORAGE_STATUS"
    )
    return {
        "carrier_emission_recognized": bool(recognized),
        "carrier_emission_class_permitted_for_role": bool(recognized),
        "carrier_emission_local_only": bool(recognized),
        "no_emission_was_recognized": not bool(emission_class),
        "passive_storage_status_non_standing": bool(passive_storage_only),
        "passive_storage_status_is_not_receipt": bool(passive_storage_only),
        "carrier_emission_self_admitted": False,
        "carrier_emission_created_signal_by_default": False,
        "carrier_emission_established_presence": False,
        "carrier_emission_established_threshold": False,
        "carrier_emission_created_truth": False,
        "carrier_emission_authorized_action": False,
        "carrier_emission_created_consequence": False,
        "carrier_emission_created_multi_carrier_law": False,
        "carrier_emission_created_distributed_standing": False,
        "carrier_emission_authorized_continuation": False,
    }


def _declared_operation_basis(
    operation: Mapping[str, Any],
    declared_role: str | None,
    declared_emission: str | None,
) -> dict[str, Any]:
    return {
        "operation_id": operation.get("operation_id"),
        "operation_purpose": operation.get("operation_purpose"),
        "operation_scope": operation.get("operation_scope"),
        "declared_carrier_role": operation.get("declared_carrier_role"),
        "normalized_declared_carrier_role": declared_role,
        "declared_emission_class": operation.get("declared_emission_class"),
        "normalized_declared_emission_class": declared_emission,
        "selected_packet_or_surface": copy.deepcopy(
            operation.get("selected_packet_or_surface")
        ),
        "source_carrier_context": copy.deepcopy(
            operation.get("source_carrier_context")
        ),
        "receiving_carrier_context": copy.deepcopy(
            operation.get("receiving_carrier_context")
        ),
        "emission_identity": operation.get("emission_identity"),
        "emission_outcome": operation.get("emission_outcome"),
        "integrity_evidence": copy.deepcopy(operation.get("integrity_evidence")),
        "declared_non_claims": copy.deepcopy(operation.get("declared_non_claims")),
        "declared_carrier_operation_path": operation.get(
            "_declared_carrier_operation_path"
        ),
    }


def _normalize_selected_carrier(
    value: Any,
    declared_role: str | None,
) -> dict[str, Any]:
    if isinstance(value, Mapping):
        carrier_id = _first_text(value, ("carrier_id", "id", "carrier_identifier"))
        label = _first_text(value, ("carrier_label", "label", "name"))
        return {
            "carrier_id": carrier_id,
            "carrier_label": label,
            "carrier_role_for_operation": _normalize_token(
                _first_text(
                    value,
                    ("carrier_role_for_operation", "carrier_role", "role"),
                )
            )
            or declared_role,
            "role_is_operation_local": _role_is_operation_local({}, value),
            "role_is_not_permanent_identity": not _flag_true(
                [value],
                (
                    "carrier_role_became_permanent_identity",
                    "carrier_role_permanent_identity",
                    "role_permanent_identity",
                ),
            ),
            "raw_selected_carrier": copy.deepcopy(dict(value)),
        }
    if isinstance(value, str) and value.strip():
        return {
            "carrier_id": value.strip(),
            "carrier_label": None,
            "carrier_role_for_operation": declared_role,
            "role_is_operation_local": True,
            "role_is_not_permanent_identity": True,
            "raw_selected_carrier": value.strip(),
        }
    return {
        "carrier_id": None,
        "carrier_label": None,
        "carrier_role_for_operation": declared_role,
        "role_is_operation_local": False,
        "role_is_not_permanent_identity": False,
        "raw_selected_carrier": copy.deepcopy(value),
    }


def _carrier_role_basis(declared_role: str | None) -> dict[str, Any]:
    permitted = PERMITTED_EMISSIONS_BY_ROLE.get(declared_role or "", set())
    return {
        "role_name": declared_role,
        "role_admitted": declared_role in ADMITTED_CARRIER_ROLES,
        "role_candidate_not_admitted": declared_role in CANDIDATE_CARRIER_ROLES,
        "role_local_scope": "operation_local",
        "permitted_emissions": sorted(permitted),
        "prohibited_emissions": sorted(NOT_ADMITTED_EMISSION_CLASSES),
        "role_non_meaning": copy.deepcopy(ROLE_DOES_NOT_MEAN),
    }


def _emission_basis(
    operation: Mapping[str, Any],
    declared_role: str | None,
    declared_emission: str | None,
    emission_requested: bool,
) -> dict[str, Any]:
    permitted_for_role = PERMITTED_EMISSIONS_BY_ROLE.get(declared_role or "", set())
    return {
        "emission_requested": bool(emission_requested),
        "emission_class": declared_emission,
        "emission_identity": operation.get("emission_identity"),
        "emission_outcome": operation.get("emission_outcome"),
        "emission_source_packet_or_surface": copy.deepcopy(
            operation.get("selected_packet_or_surface")
        ),
        "integrity_evidence": copy.deepcopy(operation.get("integrity_evidence")),
        "body_line_admission_status": "not_admitted_by_this_result",
        "emission_class_supported": (
            declared_emission in _supported_emissions()
            and declared_emission not in NOT_ADMITTED_EMISSION_CLASSES
        )
        if declared_emission
        else False,
        "emission_class_permitted_for_role": declared_emission in permitted_for_role
        if declared_emission
        else False,
        "passive_storage_status_non_standing": (
            declared_role == "HOLDING_CARRIER"
            and declared_emission == "PASSIVE_STORAGE_STATUS"
        ),
        "emission_non_meaning": copy.deepcopy(EMISSION_DOES_NOT_MEAN),
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_surfaces": list(OPEN_SURFACES),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    selected_path = Path(path)
    try:
        raw = selected_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CarrierRoleAndEmissionBoundaryError(
            "DECLARED_CARRIER_OPERATION_UNREADABLE",
            f"{BLOCK_REASONS['DECLARED_CARRIER_OPERATION_UNREADABLE']} path={selected_path} detail={exc}",
        ) from exc
    try:
        loaded = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CarrierRoleAndEmissionBoundaryError(
            "DECLARED_CARRIER_OPERATION_MALFORMED",
            f"{BLOCK_REASONS['DECLARED_CARRIER_OPERATION_MALFORMED']} path={selected_path} detail={exc}",
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CarrierRoleAndEmissionBoundaryError(
            "DECLARED_CARRIER_OPERATION_MALFORMED",
            f"{BLOCK_REASONS['DECLARED_CARRIER_OPERATION_MALFORMED']} path={selected_path} expected object",
        )
    return copy.deepcopy(dict(loaded))


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": copy.deepcopy(expected_posture),
        "actual_posture": copy.deepcopy(actual_posture),
        "block_code": None if passed else block_code,
    }


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _block_reason(
    block_code: str | None,
    failed_check: Mapping[str, Any] | None,
) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, "Carrier role or emission was blocked.")
    if failed_check:
        return f"{reason} failed check: {failed_check.get('check_name')}"
    return reason


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


def _first_text(mapping: Mapping[str, Any], keys: Sequence[str]) -> str | None:
    for key in keys:
        value = mapping.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _normalize_token(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    normalized: list[str] = []
    previous_underscore = False
    for character in value.strip().upper():
        if character.isalnum():
            normalized.append(character)
            previous_underscore = False
        elif not previous_underscore:
            normalized.append("_")
            previous_underscore = True
    token = "".join(normalized).strip("_")
    return token or None


def _normalize_key(value: Any) -> str:
    return _normalize_token(str(value)) or ""


def _supported_emissions() -> set[str]:
    supported: set[str] = set()
    for emissions in PERMITTED_EMISSIONS_BY_ROLE.values():
        supported.update(emissions)
    return supported


def _emission_requested(
    operation: Mapping[str, Any],
    declared_emission: str | None,
) -> bool:
    if declared_emission:
        return True
    if operation.get("emission_requested") is True:
        return True
    return any(
        key in operation
        for key in (
            "emission_identity",
            "emission_outcome",
            "integrity_evidence",
        )
    )


def _role_is_operation_local(
    operation: Mapping[str, Any],
    selected_carrier: Mapping[str, Any],
) -> bool:
    if _flag_true(
        [operation, selected_carrier],
        (
            "carrier_role_became_permanent_identity",
            "carrier_role_claims_permanent_identity",
            "permanent_identity_from_role",
        ),
    ):
        return False
    if selected_carrier.get("carrier_role_permanent_identity") is True:
        return False
    if selected_carrier.get("carrier_role_operation_local") is False:
        return False
    if selected_carrier.get("role_is_operation_local") is False:
        return False
    scope = operation.get("operation_scope")
    if isinstance(scope, str) and scope.strip():
        normalized_scope = _normalize_key(scope)
        if normalized_scope in {"PERMANENT_IDENTITY", "UNBOUNDED", "GLOBAL"}:
            return False
    return True


def _flag_true(sources: Sequence[Any], aliases: Sequence[str]) -> bool:
    alias_set = {_normalize_key(alias) for alias in aliases}
    for source in sources:
        if _contains_true_key(source, alias_set):
            return True
    return False


def _contains_true_key(value: Any, alias_set: set[str]) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if _normalize_key(key) in alias_set and item is True:
                return True
            if isinstance(item, (Mapping, list)) and _contains_true_key(item, alias_set):
                return True
    elif isinstance(value, list):
        for item in value:
            if _contains_true_key(item, alias_set):
                return True
    return False


def _missing_or_flipped_non_claims(non_claims: Mapping[str, Any]) -> list[str]:
    if not isinstance(non_claims, Mapping) or not non_claims:
        return list(REQUIRED_NON_CLAIMS)
    return [
        key
        for key, expected in REQUIRED_NON_CLAIMS.items()
        if non_claims.get(key) is not expected
    ]


def _merge_non_claims(source: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = copy.deepcopy(dict(source)) if isinstance(source, Mapping) else {}
    for key, value in REQUIRED_NON_CLAIMS.items():
        merged.setdefault(key, value)
    return merged


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "carrier_role_became_permanent_identity",
        "carrier_role_created_source",
        "carrier_role_created_currentness",
        "carrier_role_created_authority",
        "carrier_role_created_permission",
        "carrier_role_created_successor",
        "carrier_role_created_body",
        "carrier_emission_self_admitted",
        "carrier_emission_created_signal_by_default",
        "presence_established",
        "threshold_met",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "multi_carrier_law_created",
        "distributed_standing_created",
        "continuation_authorized",
    )
    return {key: non_claims.get(key) for key in keys}


def _result_id(
    operation: Mapping[str, Any],
    declared_role: str | None,
    outcome: str,
) -> str:
    base = (
        operation.get("operation_id")
        or declared_role
        or "carrier_role_operation"
    )
    return f"{_safe_filename_part(base)}__{outcome.lower()}__carrier_role_emission_result"


def _safe_filename_part(value: Any) -> str:
    text = str(value or "carrier_role_operation")
    allowed: list[str] = []
    previous_underscore = False
    for character in text:
        if character.isalnum() or character in "._-":
            allowed.append(character)
            previous_underscore = False
        elif not previous_underscore:
            allowed.append("_")
            previous_underscore = True
    stem = "".join(allowed).strip("._")
    return stem[:180] or "carrier_role_operation"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1
