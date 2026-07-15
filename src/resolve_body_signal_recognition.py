"""Resolve one bounded body-signal recognition candidate.

This module evaluates exactly one standing source artifact/result and one
candidate signal declaration. It decides only whether the candidate qualifies
as body-relevant signal.

Recognition is not authority, permission, currentness, routing, priority,
scheduling, aggregation, workflow, roadmap, or continuation. This resolver does
not discover sources, replay the host, mutate upstream artifacts, or build a
signal bus.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class BodySignalRecognitionError(RuntimeError):
    """Raised for malformed inputs or impossible signal correspondence."""

    def __init__(
        self,
        message: str,
        block_code: str,
        *,
        selected_source: Mapping[str, Any] | None = None,
        selected_candidate: Mapping[str, Any] | None = None,
        checks: Sequence[Mapping[str, Any]] | None = None,
    ) -> None:
        super().__init__(message)
        self.block_code = block_code
        self.selected_source = (
            copy.deepcopy(dict(selected_source))
            if isinstance(selected_source, Mapping)
            else None
        )
        self.selected_candidate = (
            copy.deepcopy(dict(selected_candidate))
            if isinstance(selected_candidate, Mapping)
            else None
        )
        self.checks = [dict(check) for check in checks] if checks is not None else None


BODY_SIGNAL_RECOGNITION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_signal_recognition"
)

RESOLVER_MODULE = "resolve_body_signal_recognition"
BODY_SIGNAL_RECOGNITION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_RECOGNITION_RESULT"
)
BODY_SIGNAL_RECOGNITION_RESULT_VERSION = "0.1.0"
DEFAULT_RESULT_STEM = "body_signal_recognition_result"

OUTCOME_SIGNAL_RECOGNIZED = "SIGNAL_RECOGNIZED"
OUTCOME_BLOCKED = "BLOCKED"

SIGNAL_CATEGORIES = frozenset(
    {
        "CURRENT_BASIS_SIGNAL",
        "CURRENT_STATE_SIGNAL",
        "OPEN_SURFACE_SIGNAL",
        "BLOCKED_REFUSED_SIGNAL",
        "TOUCH_ADMISSIBILITY_SIGNAL",
        "CONTINUITY_TRANSFER_SIGNAL",
        "CONTINUITY_RECEIPT_SIGNAL",
        "DERIVATIVE_PARTICIPATION_SIGNAL",
        "DERIVATIVE_ACTION_PERMISSION_SIGNAL",
        "MEMORY_SEAM_SIGNAL",
        "BODY_PASS_SIGNAL",
        "DERIVATIVE_VESSEL_SIGNAL",
        "OPERATOR_FACING_SIGNAL",
        "REENTRY_ADMISSIBILITY_SIGNAL",
        "REENTRY_RECEIPT_SIGNAL",
        "EXHAUSTION_CLOSURE_SIGNAL",
        "NON_CLAIM_SIGNAL",
    }
)

REQUEST_SECTIONS = (
    "candidate_signal_metadata",
    "source_artifact_basis",
    "claimed_signal",
    "carried_posture",
    "hierarchy_constraints",
    "correspondence_requirements",
    "declared_non_claims",
)

CANDIDATE_METADATA_FIELDS = (
    "candidate_signal_id",
    "candidate_signal_type",
    "candidate_signal_version",
    "declared_at",
    "declared_by_surface",
)

SOURCE_BASIS_FIELDS = (
    "source_artifact_path",
    "source_artifact_id",
    "source_artifact_family",
    "source_artifact_type",
    "source_artifact_outcome",
)

CLAIMED_SIGNAL_FIELDS = (
    "claimed_signal_family",
    "claimed_signal_posture",
    "claimed_signal_reason",
    "claimed_relevance",
    "claimed_carried_fields",
)

HIERARCHY_FALSE_FIELDS = (
    "signal_allowed_as_authority",
    "signal_allowed_as_permission",
    "signal_allowed_as_currentness_selector",
    "derivative_signal_allowed_as_source",
    "operator_signal_allowed_as_source",
    "reentry_signal_allowed_as_governing_basis",
    "latest_file_recency_allowed",
)

HIERARCHY_FIELD_BLOCK_CODES = {
    "signal_allowed_as_authority": "SIGNAL_ATTEMPTS_AUTHORITY",
    "signal_allowed_as_permission": "SIGNAL_ATTEMPTS_PERMISSION",
    "signal_allowed_as_currentness_selector": "SIGNAL_ATTEMPTS_CURRENTNESS",
    "derivative_signal_allowed_as_source": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "operator_signal_allowed_as_source": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "reentry_signal_allowed_as_governing_basis": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "latest_file_recency_allowed": "LATEST_FILE_RECENCY_REFUSED",
}

CORRESPONDENCE_TRUE_FIELDS = (
    "must_preserve_source_identity",
    "must_preserve_source_outcome",
    "must_preserve_signal_category_source_match",
    "must_preserve_derivative_source_distinction",
    "must_preserve_open_blocked_receipt_exhaustion_distinctions",
    "must_preserve_non_claims",
    "must_prevent_over_mirroring",
    "must_prevent_under_mirroring",
)

CORRESPONDENCE_FIELD_BLOCK_CODES = {
    "must_preserve_source_identity": "SOURCE_IDENTITY_NOT_PRESERVED",
    "must_preserve_source_outcome": "SOURCE_OUTCOME_NOT_PRESERVED",
    "must_preserve_signal_category_source_match": "SIGNAL_CATEGORY_MISMATCHES_SOURCE",
    "must_preserve_derivative_source_distinction": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "must_preserve_open_blocked_receipt_exhaustion_distinctions": "RELEVANT_POSTURE_OMITTED",
    "must_preserve_non_claims": "NON_CLAIM_MISSING_OR_FLIPPED",
    "must_prevent_over_mirroring": "SIGNAL_OVER_MIRRORS_SOURCE",
    "must_prevent_under_mirroring": "SIGNAL_UNDER_MIRRORS_SOURCE",
}

DECLARED_NON_CLAIM_FIELDS = (
    "does_not_create_authority",
    "does_not_create_permission",
    "does_not_create_currentness",
    "does_not_authorize_action",
    "does_not_authorize_follow_on_work",
    "does_not_create_workflow",
    "does_not_create_roadmap",
    "does_not_create_signal_router",
    "does_not_create_event_bus",
    "does_not_replace_source_surface",
    "does_not_upgrade_derivative_to_source",
    "does_not_turn_receipt_into_permission",
)

RESULT_NON_CLAIM_DEFAULTS = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "action_authorized": False,
    "follow_on_work_authorized": False,
    "workflow_created": False,
    "roadmap_created": False,
    "signal_router_created": False,
    "event_bus_created": False,
    "source_replaced": False,
    "derivative_upgraded_to_source": False,
    "receipt_turned_into_permission": False,
    "radio_22_implemented": False,
}

BLOCK_REASONS = {
    "NO_SOURCE_ARTIFACT_BASIS": "No standing source artifact/result basis was supplied.",
    "SOURCE_ARTIFACT_UNREADABLE": "The explicit source artifact path could not be read.",
    "SOURCE_ARTIFACT_MALFORMED": "The selected source artifact is malformed.",
    "SOURCE_OUTCOME_MISSING": "The selected source artifact does not expose an outcome.",
    "CANDIDATE_SIGNAL_DECLARATION_MISSING": (
        "A candidate signal declaration is required."
    ),
    "CANDIDATE_SIGNAL_DECLARATION_MALFORMED": (
        "The candidate signal declaration is malformed."
    ),
    "SIGNAL_CATEGORY_UNKNOWN": "The candidate signal category is not recognized.",
    "SIGNAL_CATEGORY_MISMATCHES_SOURCE": (
        "The candidate signal category does not correspond to the selected source."
    ),
    "SOURCE_IDENTITY_NOT_PRESERVED": (
        "The candidate signal does not preserve selected source identity."
    ),
    "SOURCE_OUTCOME_NOT_PRESERVED": (
        "The candidate signal does not preserve selected source outcome."
    ),
    "RELEVANT_POSTURE_OMITTED": (
        "The candidate signal omits posture required for its category."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required non-claim is missing or flipped."
    ),
    "SIGNAL_ATTEMPTS_AUTHORITY": "The candidate signal attempts to create authority.",
    "SIGNAL_ATTEMPTS_PERMISSION": "The candidate signal attempts to create permission.",
    "SIGNAL_ATTEMPTS_CURRENTNESS": (
        "The candidate signal attempts to create currentness."
    ),
    "SIGNAL_ATTEMPTS_ACTION_AUTHORIZATION": (
        "The candidate signal attempts to authorize action."
    ),
    "SIGNAL_ATTEMPTS_FOLLOW_ON_AUTHORIZATION": (
        "The candidate signal attempts to authorize follow-on work."
    ),
    "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE": (
        "The candidate signal collapses derivative, operator, or re-entry source distinction."
    ),
    "REENTRY_RECEIPT_TREATED_AS_REUSABLE_PERMISSION": (
        "The candidate signal treats re-entry receipt as reusable permission."
    ),
    "LATEST_FILE_RECENCY_REFUSED": (
        "The candidate signal infers currentness by latest-file recency."
    ),
    "BLOCKED_REFUSED_POSTURE_HIDDEN": (
        "The candidate signal hides blocked or refused posture."
    ),
    "OPEN_SURFACE_TREATED_AS_COMPLETED": (
        "The candidate signal treats open posture as completed."
    ),
    "RECEIPT_POSTURE_OMITTED": (
        "The candidate signal omits receipt posture required for its category."
    ),
    "EXHAUSTION_POSTURE_OMITTED": (
        "The candidate signal omits exhaustion posture required for its category."
    ),
    "SIGNAL_BECOMES_WORKFLOW_ROADMAP_OR_ROUTER": (
        "The candidate signal becomes workflow, roadmap, router, event bus, or regulation language."
    ),
    "SIGNAL_OVER_MIRRORS_SOURCE": (
        "The candidate signal over-mirrors into a whole-body replacement."
    ),
    "SIGNAL_UNDER_MIRRORS_SOURCE": (
        "The candidate signal under-mirrors required source posture."
    ),
    "SOURCE_SCOPE_WIDENED": "The candidate signal widens scope beyond the selected source.",
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else _repo_root() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    candidate = Path(path)
    if not candidate.is_absolute():
        return candidate.as_posix()
    try:
        return candidate.resolve(strict=False).relative_to(
            _repo_root().resolve(strict=False)
        ).as_posix()
    except ValueError:
        return candidate.as_posix()


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _clone(value: Any) -> Any:
    return copy.deepcopy(value)


def _string_or_none(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        text = value.strip()
        return text if text else None
    return str(value)


def _safe_filename_part(value: Any) -> str:
    text = _string_or_none(value) or "default"
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("._")
    return (text or "default")[:180]


def _normal_text(value: Any) -> str:
    text = _string_or_none(value) or ""
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def _truth_text(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return ""
    return str(value).strip().lower()


def _is_trueish(value: Any) -> bool:
    if value is True:
        return True
    text = _truth_text(value)
    return text in {"true", "yes", "y", "1", "open", "received", "exhausted", "closed"}


def _is_false(value: Any) -> bool:
    return value is False


def _loose_equal(left: Any, right: Any) -> bool:
    if left is None or right is None:
        return False
    return _normal_text(left) == _normal_text(right)


def _loose_family_equal(left: Any, right: Any) -> bool:
    left_text = _normal_text(left)
    right_text = _normal_text(right)
    if not left_text or not right_text:
        return False
    return (
        left_text == right_text
        or left_text.endswith(right_text)
        or right_text.endswith(left_text)
        or left_text in right_text
        or right_text in left_text
    )


def _path_equal(left: Any, right: Any) -> bool:
    left_text = _string_or_none(left)
    right_text = _string_or_none(right)
    if left_text is None or right_text is None:
        return False
    left_path = Path(left_text)
    right_path = Path(right_text)
    if left_path.as_posix() == right_path.as_posix():
        return True
    return _display_path(_repo_path(left_path)) == _display_path(_repo_path(right_path))


def _text_blob(*values: Any) -> str:
    parts: list[str] = []
    for value in values:
        if isinstance(value, Mapping):
            parts.extend(str(key) for key in value.keys())
            parts.extend(_text_blob(nested) for nested in value.values())
        elif isinstance(value, list):
            parts.extend(_text_blob(item) for item in value)
        elif value is not None:
            parts.append(str(value))
    return " ".join(part for part in parts if part).lower()


def _read_json_file(path: Path | str) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except OSError as exc:
        raise BodySignalRecognitionError(
            f"source artifact is unreadable: {resolved}",
            "SOURCE_ARTIFACT_UNREADABLE",
        ) from exc
    except json.JSONDecodeError as exc:
        raise BodySignalRecognitionError(
            f"source artifact is malformed JSON: {resolved}",
            "SOURCE_ARTIFACT_MALFORMED",
        ) from exc
    if not isinstance(value, dict):
        raise BodySignalRecognitionError(
            f"source artifact JSON must be an object: {resolved}",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    return value


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
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": block_code,
    }


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _block_reason(block_code: str | None, detail: str | None = None) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, block_code.replace("_", " ").lower() + ".")
    if detail:
        return f"{reason} {detail}"
    return reason


def _candidate_mapping(value: Any) -> dict[str, Any]:
    return _clone(dict(value)) if isinstance(value, Mapping) else {}


def _metadata_mappings(source: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    mappings: list[Mapping[str, Any]] = []
    for key, value in source.items():
        if isinstance(value, Mapping) and "metadata" in str(key):
            mappings.append(value)
    return mappings


def _summary_mappings(source: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    mappings: list[Mapping[str, Any]] = []
    for key, value in source.items():
        if isinstance(value, Mapping) and "summary" in str(key):
            mappings.append(value)
    return mappings


def _first_from_mappings(
    mappings: Sequence[Mapping[str, Any]],
    keys: Sequence[str],
) -> Any:
    for mapping in mappings:
        for key in keys:
            value = mapping.get(key)
            if _string_or_none(value) is not None:
                return value
    return None


def _first_key_ending(
    mappings: Sequence[Mapping[str, Any]],
    suffixes: Sequence[str],
) -> Any:
    for mapping in mappings:
        for key, value in mapping.items():
            key_text = str(key)
            if any(key_text.endswith(suffix) for suffix in suffixes):
                if _string_or_none(value) is not None:
                    return value
    return None


def _infer_family(source: Mapping[str, Any], source_type: Any) -> str | None:
    haystack = _text_blob(list(source.keys()), source_type)
    family_rules = (
        ("reentry_receipt", ("reentry_receipt",)),
        ("reentry_admissibility", ("reentry_admissibility",)),
        ("operator_facing_terminal_brief", ("operator_terminal_brief", "operator_facing")),
        ("derivative_vessel", ("derivative_vessel", "openai_api_derivative_vessel", "vessel")),
        ("continuity_memory_seam", ("continuity_memory_seam", "memory_seam")),
        (
            "received_derivative_action_permission",
            ("received_derivative_action_permission", "action_permission"),
        ),
        ("received_derivative_participation", ("received_derivative_participation",)),
        ("continuity_transfer_receipt", ("continuity_transfer_receipt", "transfer_receipt")),
        ("continuity_transfer", ("continuity_transfer_unit", "continuity_transfer")),
        ("current_state_touch_admissibility", ("touch_permission", "admissibility_and_touch")),
        ("current_state_what_remains_open", ("what_remains_open",)),
        ("current_state_what_stands_now", ("what_stands_now",)),
        ("current_state_answer_read", ("answer_surface", "answer_read")),
        ("current_state_query", ("current_state_query",)),
        ("current_state", ("current_state", "readout", "handoff", "export", "delivery", "application")),
        ("body_pass", ("v0_body_pass", "body_pass")),
        (
            "current_governing_basis",
            ("current_governing", "governing", "effective", "execution_authority"),
        ),
    )
    for family, needles in family_rules:
        if any(needle in haystack for needle in needles):
            return family
    return None


def _source_identity(
    source: Mapping[str, Any],
    source_path_hint: Path | str | None,
    candidate_signal: Mapping[str, Any] | None,
    selection_mode: str,
) -> dict[str, Any]:
    candidate_basis = {}
    if isinstance(candidate_signal, Mapping):
        maybe_basis = candidate_signal.get("source_artifact_basis")
        if isinstance(maybe_basis, Mapping):
            candidate_basis = dict(maybe_basis)

    metadata = _metadata_mappings(source)
    summaries = _summary_mappings(source)
    all_named = [source, *metadata, *summaries]

    source_id = (
        _first_from_mappings(
            all_named,
            (
                "source_artifact_id",
                "result_id",
                "artifact_id",
                "body_signal_recognition_result_id",
            ),
        )
        or _first_key_ending(all_named, ("_result_id", "_artifact_id"))
    )
    source_id_exposed = source_id is not None
    if source_id is None:
        source_id = candidate_basis.get("source_artifact_id")

    source_type = (
        _first_from_mappings(
            all_named,
            ("source_artifact_type", "result_type", "artifact_type", "type"),
        )
        or _first_key_ending(all_named, ("_result_type", "_artifact_type"))
    )
    source_type_exposed = source_type is not None
    if source_type is None:
        source_type = candidate_basis.get("source_artifact_type")

    source_family = _first_from_mappings(
        all_named,
        ("source_artifact_family", "result_family", "artifact_family", "family"),
    )
    inferred_family = _infer_family(source, source_type)
    if source_family is None:
        source_family = inferred_family
    source_family_exposed = source_family is not None
    if source_family is None:
        source_family = candidate_basis.get("source_artifact_family")

    source_outcome = source.get("outcome")
    if source_outcome is None:
        source_outcome = source.get("source_artifact_outcome")

    if source_path_hint is not None:
        source_path = _display_path(source_path_hint)
        source_path_exposed = True
    else:
        source_path = _first_from_mappings(
            all_named,
            ("source_artifact_path", "result_path", "artifact_path", "path"),
        )
        source_path_exposed = source_path is not None
        if source_path is None:
            source_path = candidate_basis.get("source_artifact_path")

    module = _first_from_mappings(
        all_named,
        (
            "source_artifact_resolver_or_emitter_module",
            "resolver_module",
            "emitter_module",
        ),
    )
    if module is None:
        module = candidate_basis.get("source_artifact_resolver_or_emitter_module")

    return {
        "source_artifact_id": _string_or_none(source_id),
        "source_artifact_path": _string_or_none(source_path),
        "source_artifact_family": _string_or_none(source_family),
        "source_artifact_type": _string_or_none(source_type),
        "source_artifact_outcome": _string_or_none(source_outcome),
        "source_artifact_resolver_or_emitter_module": _string_or_none(module),
        "selection_mode": selection_mode,
        "_source_id_exposed": source_id_exposed,
        "_source_path_exposed": source_path_exposed,
        "_source_family_exposed": source_family_exposed,
        "_source_type_exposed": source_type_exposed,
    }


def _public_source_identity(identity: Mapping[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in identity.items()
        if not str(key).startswith("_")
    }


def _candidate_shape_errors(candidate: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    for section in REQUEST_SECTIONS:
        if not isinstance(candidate.get(section), Mapping):
            errors.append(f"{section} must be an object")

    metadata = candidate.get("candidate_signal_metadata")
    if isinstance(metadata, Mapping):
        for field in CANDIDATE_METADATA_FIELDS:
            if _string_or_none(metadata.get(field)) is None:
                errors.append(f"candidate_signal_metadata.{field} is required")

    source_basis = candidate.get("source_artifact_basis")
    if isinstance(source_basis, Mapping):
        for field in SOURCE_BASIS_FIELDS:
            if _string_or_none(source_basis.get(field)) is None:
                errors.append(f"source_artifact_basis.{field} is required")

    claimed = candidate.get("claimed_signal")
    if isinstance(claimed, Mapping):
        for field in CLAIMED_SIGNAL_FIELDS:
            value = claimed.get(field)
            if field == "claimed_carried_fields":
                if value is None:
                    errors.append("claimed_signal.claimed_carried_fields is required")
            elif _string_or_none(value) is None:
                errors.append(f"claimed_signal.{field} is required")

    return errors


def _section(candidate: Mapping[str, Any], name: str) -> Mapping[str, Any]:
    value = candidate.get(name)
    return value if isinstance(value, Mapping) else {}


def _candidate_signal_id(candidate: Mapping[str, Any]) -> str | None:
    return _string_or_none(
        _section(candidate, "candidate_signal_metadata").get("candidate_signal_id")
    )


def _signal_category(candidate: Mapping[str, Any]) -> str | None:
    return _string_or_none(_section(candidate, "claimed_signal").get("signal_category"))


def _source_haystack(source: Mapping[str, Any], identity: Mapping[str, Any]) -> str:
    return _text_blob(
        identity.get("source_artifact_family"),
        identity.get("source_artifact_type"),
        identity.get("source_artifact_outcome"),
        list(source.keys()),
        source.get("non_claims"),
    )


def _source_has_non_claims(source: Mapping[str, Any]) -> bool:
    return isinstance(source.get("non_claims"), Mapping)


def _category_matches_source(
    category: str | None,
    source: Mapping[str, Any],
    identity: Mapping[str, Any],
) -> bool:
    if category not in SIGNAL_CATEGORIES:
        return False

    haystack = _source_haystack(source, identity)
    outcome = _truth_text(identity.get("source_artifact_outcome"))
    is_blocked_or_refused = "blocked" in outcome or "refused" in outcome

    if category == "CURRENT_BASIS_SIGNAL":
        return any(
            marker in haystack
            for marker in (
                "current_basis",
                "current_governing",
                "governing",
                "effective",
                "execution_authority",
                "current_state",
                "what_stands_now",
                "answer_read",
            )
        )
    if category == "CURRENT_STATE_SIGNAL":
        return any(
            marker in haystack
            for marker in (
                "current_state",
                "what_stands_now",
                "what_remains_open",
                "answer_read",
                "query",
                "readout",
                "handoff",
                "export",
                "delivery",
                "application",
            )
        )
    if category == "OPEN_SURFACE_SIGNAL":
        return "what_remains_open" in haystack or "open" in outcome
    if category == "BLOCKED_REFUSED_SIGNAL":
        return is_blocked_or_refused or "blocked_refused" in haystack
    if category == "TOUCH_ADMISSIBILITY_SIGNAL":
        return (
            "reentry_admissibility" not in haystack
            and ("touch" in haystack or "admissibility_and_touch" in haystack)
        )
    if category == "CONTINUITY_TRANSFER_SIGNAL":
        return "continuity_transfer" in haystack and "receipt" not in haystack
    if category == "CONTINUITY_RECEIPT_SIGNAL":
        return (
            "continuity_transfer_receipt" in haystack
            or ("continuity" in haystack and "receipt" in haystack and "reentry" not in haystack)
        )
    if category == "DERIVATIVE_PARTICIPATION_SIGNAL":
        return "received_derivative_participation" in haystack
    if category == "DERIVATIVE_ACTION_PERMISSION_SIGNAL":
        return "received_derivative_action" in haystack or "action_permission" in haystack
    if category == "MEMORY_SEAM_SIGNAL":
        return "memory_seam" in haystack
    if category == "BODY_PASS_SIGNAL":
        return "body_pass" in haystack or "v0_body_pass" in haystack
    if category == "DERIVATIVE_VESSEL_SIGNAL":
        return "derivative_vessel" in haystack or "openai_api_derivative" in haystack
    if category == "OPERATOR_FACING_SIGNAL":
        return "operator" in haystack or "terminal_brief" in haystack
    if category == "REENTRY_ADMISSIBILITY_SIGNAL":
        return "reentry_admissibility" in haystack
    if category == "REENTRY_RECEIPT_SIGNAL":
        return "reentry_receipt" in haystack
    if category == "EXHAUSTION_CLOSURE_SIGNAL":
        return "reentry_receipt" in haystack or "exhaust" in haystack or "closure" in haystack
    if category == "NON_CLAIM_SIGNAL":
        return _source_has_non_claims(source)
    return False


def _first_field(mapping: Mapping[str, Any], fields: Sequence[str]) -> Any:
    for field in fields:
        if field in mapping:
            value = mapping.get(field)
            if value is not None:
                return value
    return None


def _carried_status_present(value: Any, expected_words: Sequence[str]) -> bool:
    if isinstance(value, bool):
        return value is True
    text = _truth_text(value)
    return any(word in text for word in expected_words)


def _carried_posture_status(
    candidate: Mapping[str, Any],
    category: str | None,
    source_identity: Mapping[str, Any],
    source: Mapping[str, Any],
) -> tuple[bool, str, Any]:
    carried = _section(candidate, "carried_posture")
    source_basis = _section(candidate, "source_artifact_basis")

    outcome_value = _first_field(
        carried,
        ("source_outcome_posture", "source_outcome", "source_posture", "outcome"),
    )
    if outcome_value is None:
        return False, "RELEVANT_POSTURE_OMITTED", "source outcome/posture not carried"
    if not _loose_equal(outcome_value, source_identity.get("source_artifact_outcome")):
        return False, "SOURCE_OUTCOME_NOT_PRESERVED", outcome_value

    source_id_value = _first_field(
        carried,
        ("source_artifact_id", "source_id", "result_id"),
    )
    expected_id = source_identity.get("source_artifact_id")
    if expected_id and source_id_value is None:
        return False, "SOURCE_IDENTITY_NOT_PRESERVED", "source id not carried"
    if expected_id and not _loose_equal(source_id_value, expected_id):
        return False, "SOURCE_IDENTITY_NOT_PRESERVED", source_id_value

    family_value = _first_field(
        carried,
        ("source_artifact_family", "source_family", "result_family"),
    )
    expected_family = source_identity.get("source_artifact_family")
    if expected_family and family_value is None:
        return False, "SOURCE_IDENTITY_NOT_PRESERVED", "source family not carried"
    if expected_family and not _loose_family_equal(family_value, expected_family):
        return False, "SOURCE_IDENTITY_NOT_PRESERVED", family_value

    path_value = _first_field(
        carried,
        ("source_artifact_path", "source_path", "result_path"),
    )
    expected_path = source_identity.get("source_artifact_path")
    source_basis_path = source_basis.get("source_artifact_path")
    if expected_path and path_value is None and source_basis_path is None:
        return False, "SOURCE_IDENTITY_NOT_PRESERVED", "source path not carried"
    if expected_path and path_value is not None and not _path_equal(path_value, expected_path):
        return False, "SOURCE_IDENTITY_NOT_PRESERVED", path_value

    if category == "OPEN_SURFACE_SIGNAL":
        completed = _first_field(
            carried,
            ("completed", "is_completed", "open_surface_completed"),
        )
        if _is_trueish(completed):
            return False, "OPEN_SURFACE_TREATED_AS_COMPLETED", completed
        open_value = _first_field(
            carried,
            ("open_status", "open_surface_status", "is_open", "remains_open"),
        )
        if not _carried_status_present(open_value, ("open", "true", "remains")):
            return False, "RELEVANT_POSTURE_OMITTED", "open status not carried"

    if category == "BLOCKED_REFUSED_SIGNAL":
        blocked_value = _first_field(
            carried,
            ("blocked_refused_status", "blocked_status", "refusal_status", "is_blocked_or_refused"),
        )
        if not _carried_status_present(blocked_value, ("blocked", "refused", "true")):
            return False, "BLOCKED_REFUSED_POSTURE_HIDDEN", "blocked/refused status not visible"

    if category in {"CONTINUITY_RECEIPT_SIGNAL", "REENTRY_RECEIPT_SIGNAL"}:
        receipt_value = _first_field(
            carried,
            ("receipt_status", "received_status", "is_received", "received", "outcome"),
        )
        if not _carried_status_present(receipt_value, ("receipt", "received", "true")):
            return False, "RECEIPT_POSTURE_OMITTED", "receipt status not carried"

    if category == "EXHAUSTION_CLOSURE_SIGNAL":
        exhaustion_value = _first_field(
            carried,
            (
                "exhaustion_status",
                "admission_exhausted",
                "exhaustion_closure_passed",
                "is_exhausted",
                "closed",
            ),
        )
        if not _carried_status_present(exhaustion_value, ("exhaust", "closed", "true")):
            return False, "EXHAUSTION_POSTURE_OMITTED", "exhaustion status not carried"

    if category in {
        "DERIVATIVE_VESSEL_SIGNAL",
        "DERIVATIVE_PARTICIPATION_SIGNAL",
        "DERIVATIVE_ACTION_PERMISSION_SIGNAL",
    }:
        derivative_value = _first_field(
            carried,
            ("derivative_status", "is_derivative", "model_output_remains_derivative"),
        )
        if not _carried_status_present(derivative_value, ("derivative", "true")):
            return False, "RELEVANT_POSTURE_OMITTED", "derivative status not carried"

    if category == "OPERATOR_FACING_SIGNAL":
        operator_value = _first_field(
            carried,
            ("operator_facing_status", "is_operator_facing", "brief_remains_derivative"),
        )
        if not _carried_status_present(operator_value, ("operator", "brief", "true")):
            return False, "RELEVANT_POSTURE_OMITTED", "operator-facing status not carried"

    if category == "NON_CLAIM_SIGNAL":
        if not isinstance(carried.get("non_claims"), Mapping) and not _source_has_non_claims(source):
            return False, "NON_CLAIM_MISSING_OR_FLIPPED", "non-claims not carried"

    return True, "RELEVANT_POSTURE_OMITTED", "required carried posture preserved"


def _first_bad_false_field(fields: Sequence[str], mapping: Mapping[str, Any]) -> str | None:
    for field in fields:
        if mapping.get(field) is not False:
            return field
    return None


def _first_bad_true_field(fields: Sequence[str], mapping: Mapping[str, Any]) -> str | None:
    for field in fields:
        if mapping.get(field) is not True:
            return field
    return None


def _declared_non_claims_passed(non_claims: Mapping[str, Any]) -> bool:
    return _first_bad_true_field(DECLARED_NON_CLAIM_FIELDS, non_claims) is None


def _forbidden_claim_text(candidate: Mapping[str, Any]) -> str:
    claimed = _section(candidate, "claimed_signal")
    return _text_blob(
        claimed.get("claimed_signal_family"),
        claimed.get("claimed_signal_posture"),
        claimed.get("claimed_signal_reason"),
        claimed.get("claimed_relevance"),
    )


def _has_forbidden_workflow_language(candidate: Mapping[str, Any]) -> bool:
    text = _forbidden_claim_text(candidate)
    forbidden = (
        "workflow",
        "roadmap",
        "router",
        "event bus",
        "event_bus",
        "regulation",
        "nervous",
        "orchestration",
        "autonomy",
        "next organ",
        "next_step_generator",
        "continue the work",
        "advance iammai",
        "radio 22",
        "radio_22",
    )
    return any(item in text for item in forbidden)


def _has_latest_file_recency_language(candidate: Mapping[str, Any]) -> bool:
    text = _forbidden_claim_text(candidate)
    forbidden = ("latest file", "latest-file", "latest_file", "recency", "newest file")
    return any(item in text for item in forbidden)


def _has_reusable_receipt_permission(candidate: Mapping[str, Any]) -> bool:
    text = _forbidden_claim_text(candidate)
    forbidden = (
        "reusable permission",
        "receipt means continue",
        "admission reusable",
        "general permission",
        "permission token",
    )
    return any(item in text for item in forbidden)


def _source_is_downstream(identity: Mapping[str, Any]) -> bool:
    text = _text_blob(
        identity.get("source_artifact_family"),
        identity.get("source_artifact_type"),
    )
    return any(
        marker in text
        for marker in (
            "derivative",
            "vessel",
            "operator",
            "brief",
            "reentry",
            "receipt",
        )
    )


def _build_checks(
    source: Mapping[str, Any] | None,
    candidate: Mapping[str, Any] | None,
    source_identity: Mapping[str, Any],
    *,
    source_path_hint: Path | str | None,
    source_readable: bool,
    source_malformed: bool,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    source_exists = isinstance(source, Mapping)
    candidate_exists = isinstance(candidate, Mapping)
    candidate_shape_errors = (
        _candidate_shape_errors(candidate) if isinstance(candidate, Mapping) else []
    )
    candidate_well_formed = candidate_exists and not candidate_shape_errors
    category = _signal_category(candidate) if isinstance(candidate, Mapping) else None
    category_known = category in SIGNAL_CATEGORIES
    source_outcome = source_identity.get("source_artifact_outcome")

    checks.append(
        _check(
            "source_artifact_basis_exists",
            source_exists,
            "one standing source artifact/result mapping",
            "present" if source_exists else "missing",
            "NO_SOURCE_ARTIFACT_BASIS",
        )
    )
    checks.append(
        _check(
            "source_artifact_is_readable_if_path_based",
            source_exists and source_readable and not source_malformed,
            "readable source JSON object for explicit path, provided object otherwise",
            "readable" if source_exists and source_readable and not source_malformed else "unreadable or malformed",
            "SOURCE_ARTIFACT_UNREADABLE" if not source_malformed else "SOURCE_ARTIFACT_MALFORMED",
        )
    )
    checks.append(
        _check(
            "source_artifact_outcome_present",
            _string_or_none(source_outcome) is not None,
            "source artifact outcome present",
            source_outcome,
            "SOURCE_OUTCOME_MISSING",
        )
    )
    checks.append(
        _check(
            "candidate_signal_declaration_exists",
            candidate_exists,
            "one candidate signal declaration mapping",
            "present" if candidate_exists else "missing",
            "CANDIDATE_SIGNAL_DECLARATION_MISSING",
        )
    )
    checks.append(
        _check(
            "candidate_signal_declaration_well_formed_enough",
            candidate_well_formed,
            "required candidate sections and core fields present",
            candidate_shape_errors or "well formed enough",
            "CANDIDATE_SIGNAL_DECLARATION_MALFORMED",
        )
    )
    checks.append(
        _check(
            "signal_category_known",
            category_known,
            "one bounded signal category",
            category,
            "SIGNAL_CATEGORY_UNKNOWN",
        )
    )

    category_matches = (
        isinstance(source, Mapping)
        and category_known
        and _category_matches_source(category, source, source_identity)
    )
    checks.append(
        _check(
            "signal_category_corresponds_to_source",
            category_matches,
            "signal category corresponds to source family/outcome",
            {
                "signal_category": category,
                "source_family": source_identity.get("source_artifact_family"),
                "source_type": source_identity.get("source_artifact_type"),
                "source_outcome": source_identity.get("source_artifact_outcome"),
            },
            "SIGNAL_CATEGORY_MISMATCHES_SOURCE",
        )
    )

    source_basis = _section(candidate, "source_artifact_basis") if candidate else {}
    source_id = source_identity.get("source_artifact_id")
    candidate_id = source_basis.get("source_artifact_id")
    id_preserved = (
        source_id is None
        or not source_identity.get("_source_id_exposed")
        or _loose_equal(candidate_id, source_id)
    )
    checks.append(
        _check(
            "candidate_preserves_source_id",
            id_preserved,
            "candidate source_artifact_id matches selected source",
            {"expected": source_id, "actual": candidate_id},
            "SOURCE_IDENTITY_NOT_PRESERVED",
        )
    )

    source_path = source_identity.get("source_artifact_path")
    candidate_path = source_basis.get("source_artifact_path")
    path_required = source_path_hint is not None or source_identity.get("_source_path_exposed")
    path_preserved = (
        not path_required
        or source_path is None
        or (candidate_path is not None and _path_equal(candidate_path, source_path))
    )
    checks.append(
        _check(
            "candidate_preserves_source_path_when_path_based_or_exposed",
            path_preserved,
            "candidate source_artifact_path matches selected source path",
            {"expected": source_path, "actual": candidate_path},
            "SOURCE_IDENTITY_NOT_PRESERVED",
        )
    )

    source_family = source_identity.get("source_artifact_family")
    candidate_family = source_basis.get("source_artifact_family")
    family_preserved = (
        source_family is None
        or not source_identity.get("_source_family_exposed")
        or _loose_family_equal(candidate_family, source_family)
    )
    checks.append(
        _check(
            "candidate_preserves_source_family",
            family_preserved,
            "candidate source_artifact_family matches selected source",
            {"expected": source_family, "actual": candidate_family},
            "SOURCE_IDENTITY_NOT_PRESERVED",
        )
    )

    candidate_outcome = source_basis.get("source_artifact_outcome")
    outcome_preserved = (
        source_outcome is not None and candidate_outcome is not None and _loose_equal(candidate_outcome, source_outcome)
    )
    checks.append(
        _check(
            "candidate_preserves_source_outcome",
            outcome_preserved,
            "candidate source_artifact_outcome matches selected source outcome",
            {"expected": source_outcome, "actual": candidate_outcome},
            "SOURCE_OUTCOME_NOT_PRESERVED",
        )
    )

    carried_passed, carried_block, carried_actual = (
        _carried_posture_status(candidate, category, source_identity, source)
        if isinstance(candidate, Mapping) and isinstance(source, Mapping)
        else (False, "RELEVANT_POSTURE_OMITTED", "candidate or source missing")
    )
    checks.append(
        _check(
            "candidate_preserves_relevant_carried_posture",
            carried_passed,
            "source identity/outcome and category-specific posture carried",
            carried_actual,
            carried_block,
        )
    )

    hierarchy = _section(candidate, "hierarchy_constraints") if candidate else {}
    bad_hierarchy_field = _first_bad_false_field(HIERARCHY_FALSE_FIELDS, hierarchy)
    checks.append(
        _check(
            "candidate_preserves_hierarchy_constraints",
            bad_hierarchy_field is None,
            "all hierarchy constraint fields present and false",
            (
                "all false"
                if bad_hierarchy_field is None
                else {bad_hierarchy_field: hierarchy.get(bad_hierarchy_field)}
            ),
            HIERARCHY_FIELD_BLOCK_CODES.get(
                bad_hierarchy_field or "", "CANDIDATE_SIGNAL_DECLARATION_MALFORMED"
            ),
        )
    )

    correspondence = _section(candidate, "correspondence_requirements") if candidate else {}
    bad_correspondence_field = _first_bad_true_field(
        CORRESPONDENCE_TRUE_FIELDS,
        correspondence,
    )
    checks.append(
        _check(
            "candidate_preserves_correspondence_requirements",
            bad_correspondence_field is None,
            "all correspondence requirement fields present and true",
            (
                "all true"
                if bad_correspondence_field is None
                else {bad_correspondence_field: correspondence.get(bad_correspondence_field)}
            ),
            CORRESPONDENCE_FIELD_BLOCK_CODES.get(
                bad_correspondence_field or "",
                "CANDIDATE_SIGNAL_DECLARATION_MALFORMED",
            ),
        )
    )

    declared_non_claims = _section(candidate, "declared_non_claims") if candidate else {}
    bad_non_claim = _first_bad_true_field(DECLARED_NON_CLAIM_FIELDS, declared_non_claims)
    checks.append(
        _check(
            "candidate_preserves_declared_non_claims",
            bad_non_claim is None,
            "all declared non-claim fields present and true",
            "all true" if bad_non_claim is None else {bad_non_claim: declared_non_claims.get(bad_non_claim)},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    checks.extend(
        _anti_collapse_checks(
            candidate or {},
            source_identity,
            category,
            hierarchy,
            declared_non_claims,
        )
    )
    return checks


def _anti_collapse_checks(
    candidate: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    category: str | None,
    hierarchy: Mapping[str, Any],
    declared_non_claims: Mapping[str, Any],
) -> list[dict[str, Any]]:
    source_downstream = _source_is_downstream(source_identity)
    category_claims_current = category in {"CURRENT_BASIS_SIGNAL", "CURRENT_STATE_SIGNAL"}
    reusable_receipt = _has_reusable_receipt_permission(candidate)
    latest_recency = (
        hierarchy.get("latest_file_recency_allowed") is not False
        or _has_latest_file_recency_language(candidate)
    )
    workflow_language = _has_forbidden_workflow_language(candidate)
    correspondence = _section(candidate, "correspondence_requirements")

    return [
        _check(
            "candidate_does_not_create_authority",
            hierarchy.get("signal_allowed_as_authority") is False
            and declared_non_claims.get("does_not_create_authority") is True,
            "signal is not authority",
            {
                "signal_allowed_as_authority": hierarchy.get("signal_allowed_as_authority"),
                "does_not_create_authority": declared_non_claims.get("does_not_create_authority"),
            },
            "SIGNAL_ATTEMPTS_AUTHORITY",
        ),
        _check(
            "candidate_does_not_create_permission",
            hierarchy.get("signal_allowed_as_permission") is False
            and declared_non_claims.get("does_not_create_permission") is True,
            "signal is not permission",
            {
                "signal_allowed_as_permission": hierarchy.get("signal_allowed_as_permission"),
                "does_not_create_permission": declared_non_claims.get("does_not_create_permission"),
            },
            "SIGNAL_ATTEMPTS_PERMISSION",
        ),
        _check(
            "candidate_does_not_create_currentness",
            hierarchy.get("signal_allowed_as_currentness_selector") is False
            and declared_non_claims.get("does_not_create_currentness") is True,
            "signal is not currentness",
            {
                "signal_allowed_as_currentness_selector": hierarchy.get(
                    "signal_allowed_as_currentness_selector"
                ),
                "does_not_create_currentness": declared_non_claims.get(
                    "does_not_create_currentness"
                ),
            },
            "SIGNAL_ATTEMPTS_CURRENTNESS",
        ),
        _check(
            "candidate_does_not_authorize_action",
            declared_non_claims.get("does_not_authorize_action") is True,
            "signal does not authorize action",
            declared_non_claims.get("does_not_authorize_action"),
            "SIGNAL_ATTEMPTS_ACTION_AUTHORIZATION",
        ),
        _check(
            "candidate_does_not_authorize_follow_on_work",
            declared_non_claims.get("does_not_authorize_follow_on_work") is True,
            "signal does not authorize follow-on work",
            declared_non_claims.get("does_not_authorize_follow_on_work"),
            "SIGNAL_ATTEMPTS_FOLLOW_ON_AUTHORIZATION",
        ),
        _check(
            "candidate_does_not_create_workflow_roadmap_router_event_bus_or_regulation",
            declared_non_claims.get("does_not_create_workflow") is True
            and declared_non_claims.get("does_not_create_roadmap") is True
            and declared_non_claims.get("does_not_create_signal_router") is True
            and declared_non_claims.get("does_not_create_event_bus") is True
            and not workflow_language,
            "signal does not become workflow, roadmap, router, event bus, or regulation",
            {
                "workflow_language_detected": workflow_language,
                "does_not_create_workflow": declared_non_claims.get("does_not_create_workflow"),
                "does_not_create_roadmap": declared_non_claims.get("does_not_create_roadmap"),
                "does_not_create_signal_router": declared_non_claims.get(
                    "does_not_create_signal_router"
                ),
                "does_not_create_event_bus": declared_non_claims.get("does_not_create_event_bus"),
            },
            "SIGNAL_BECOMES_WORKFLOW_ROADMAP_OR_ROUTER",
        ),
        _check(
            "candidate_does_not_treat_derivative_api_operator_reentry_source_as_governing_current_basis",
            not (source_downstream and category_claims_current)
            and hierarchy.get("derivative_signal_allowed_as_source") is False
            and hierarchy.get("operator_signal_allowed_as_source") is False
            and hierarchy.get("reentry_signal_allowed_as_governing_basis") is False,
            "downstream signal remains downstream",
            {
                "source_downstream": source_downstream,
                "category": category,
                "derivative_signal_allowed_as_source": hierarchy.get(
                    "derivative_signal_allowed_as_source"
                ),
                "operator_signal_allowed_as_source": hierarchy.get(
                    "operator_signal_allowed_as_source"
                ),
                "reentry_signal_allowed_as_governing_basis": hierarchy.get(
                    "reentry_signal_allowed_as_governing_basis"
                ),
            },
            "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
        ),
        _check(
            "candidate_does_not_infer_currentness_by_latest_file_recency",
            not latest_recency,
            "latest-file recency is not allowed",
            {
                "latest_file_recency_allowed": hierarchy.get("latest_file_recency_allowed"),
                "latest_recency_language_detected": _has_latest_file_recency_language(candidate),
            },
            "LATEST_FILE_RECENCY_REFUSED",
        ),
        _check(
            "candidate_does_not_turn_reentry_receipt_into_reusable_permission",
            not reusable_receipt
            and declared_non_claims.get("does_not_turn_receipt_into_permission") is True,
            "receipt is not reusable permission",
            {
                "reusable_receipt_language_detected": reusable_receipt,
                "does_not_turn_receipt_into_permission": declared_non_claims.get(
                    "does_not_turn_receipt_into_permission"
                ),
            },
            "REENTRY_RECEIPT_TREATED_AS_REUSABLE_PERMISSION",
        ),
        _check(
            "candidate_does_not_over_mirror_source",
            correspondence.get("must_prevent_over_mirroring") is True
            and _section(candidate, "carried_posture").get("whole_body_replacement") is not True,
            "signal does not become a whole-body replacement",
            {
                "must_prevent_over_mirroring": correspondence.get(
                    "must_prevent_over_mirroring"
                ),
                "whole_body_replacement": _section(candidate, "carried_posture").get(
                    "whole_body_replacement"
                ),
            },
            "SIGNAL_OVER_MIRRORS_SOURCE",
        ),
        _check(
            "candidate_does_not_under_mirror_source",
            correspondence.get("must_prevent_under_mirroring") is True
            and _section(candidate, "carried_posture").get("vague_summary_only") is not True,
            "signal does not thin required source posture into vague summary",
            {
                "must_prevent_under_mirroring": correspondence.get(
                    "must_prevent_under_mirroring"
                ),
                "vague_summary_only": _section(candidate, "carried_posture").get(
                    "vague_summary_only"
                ),
            },
            "SIGNAL_UNDER_MIRRORS_SOURCE",
        ),
        _check(
            "candidate_does_not_widen_source_scope",
            _section(candidate, "carried_posture").get("source_scope_widened") is not True,
            "signal remains bounded to the selected source",
            _section(candidate, "carried_posture").get("source_scope_widened"),
            "SOURCE_SCOPE_WIDENED",
        ),
    ]


def _result_id(
    source_identity: Mapping[str, Any],
    candidate: Mapping[str, Any] | None,
    outcome: str,
) -> str:
    candidate_id = _candidate_signal_id(candidate or {}) or "candidate_signal"
    source_id = source_identity.get("source_artifact_id") or "source_artifact"
    return (
        f"{_safe_filename_part(candidate_id)}__"
        f"{_safe_filename_part(source_id)}__"
        f"body_signal_recognition_{outcome.lower()}"
    )


def _result_metadata(
    source_identity: Mapping[str, Any],
    candidate: Mapping[str, Any] | None,
    outcome: str,
) -> dict[str, Any]:
    return {
        "body_signal_recognition_result_id": _result_id(
            source_identity,
            candidate,
            outcome,
        ),
        "body_signal_recognition_result_type": BODY_SIGNAL_RECOGNITION_RESULT_TYPE,
        "body_signal_recognition_result_version": BODY_SIGNAL_RECOGNITION_RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _recognized_signal(
    source_identity: Mapping[str, Any],
    candidate: Mapping[str, Any],
) -> dict[str, Any]:
    claimed = _section(candidate, "claimed_signal")
    carried = _section(candidate, "carried_posture")
    metadata = _section(candidate, "candidate_signal_metadata")
    category = claimed.get("signal_category")
    recognized_id = f"{_safe_filename_part(metadata.get('candidate_signal_id'))}__recognized"
    return {
        "recognized_signal_id": recognized_id,
        "signal_category": category,
        "claimed_signal_family": claimed.get("claimed_signal_family"),
        "claimed_signal_posture": claimed.get("claimed_signal_posture"),
        "claimed_signal_reason": claimed.get("claimed_signal_reason"),
        "claimed_relevance": claimed.get("claimed_relevance"),
        "source_artifact_id": source_identity.get("source_artifact_id"),
        "source_artifact_path": source_identity.get("source_artifact_path"),
        "source_artifact_family": source_identity.get("source_artifact_family"),
        "source_artifact_outcome": source_identity.get("source_artifact_outcome"),
        "carried_posture": _clone(dict(carried)),
        "non_authoritative": True,
        "non_permission": True,
        "non_currentness": True,
        "bounded_relation_to_current_self_orientation": carried.get(
            "bounded_relation_to_current_self_orientation"
        ),
    }


def _recognition_basis(
    source_identity: Mapping[str, Any],
    candidate: Mapping[str, Any] | None,
    outcome: str,
) -> dict[str, Any]:
    return {
        "recognition_scope": "single_source_artifact_single_candidate_signal",
        "selected_source_artifact": _public_source_identity(source_identity),
        "candidate_signal_id": _candidate_signal_id(candidate or {}),
        "signal_category": _signal_category(candidate or {}),
        "outcome": outcome,
        "recognition_creates_authority": False,
        "recognition_creates_permission": False,
        "recognition_creates_currentness": False,
        "recognition_routes_signal": False,
        "recognition_authorizes_action": False,
        "recognition_authorizes_follow_on_work": False,
    }


def _build_result(
    *,
    source_identity: Mapping[str, Any],
    candidate_signal: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_detail: str | None = None,
) -> dict[str, Any]:
    candidate_copy = _candidate_mapping(candidate_signal)
    result: dict[str, Any] = {
        "body_signal_recognition_metadata": _result_metadata(
            source_identity,
            candidate_copy,
            outcome,
        ),
        "selected_source_artifact": _public_source_identity(source_identity),
        "selected_candidate_signal": candidate_copy,
        "signal_recognition_checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "recognized_signal": (
            _recognized_signal(source_identity, candidate_copy)
            if outcome == OUTCOME_SIGNAL_RECOGNIZED
            else None
        ),
        "body_signal_recognition_basis": _recognition_basis(
            source_identity,
            candidate_copy,
            outcome,
        ),
        "body_signal_recognition_summary": {},
        "non_claims": dict(RESULT_NON_CLAIM_DEFAULTS),
    }
    result["body_signal_recognition_summary"] = build_body_signal_recognition_summary(
        result
    )
    return result


def _empty_source_identity(
    *,
    source_path_hint: Path | str | None = None,
    selection_mode: str = "no_source_artifact",
) -> dict[str, Any]:
    return {
        "source_artifact_id": None,
        "source_artifact_path": _display_path(source_path_hint),
        "source_artifact_family": None,
        "source_artifact_type": None,
        "source_artifact_outcome": None,
        "source_artifact_resolver_or_emitter_module": None,
        "selection_mode": selection_mode,
    }


def _blocked_result(
    block_code: str,
    *,
    block_detail: str | None = None,
    source_identity: Mapping[str, Any] | None = None,
    candidate_signal: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    selected_source = source_identity or _empty_source_identity()
    selected_checks = list(checks or [])
    if not selected_checks:
        selected_checks = [
            _check(
                "body_signal_recognition_blocked",
                False,
                "bounded source and candidate signal recognition inputs",
                block_detail or block_code,
                block_code,
            )
        ]
    return _build_result(
        source_identity=selected_source,
        candidate_signal=candidate_signal,
        checks=selected_checks,
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
    )


def _resolve_internal(
    source_artifact: Mapping[str, Any] | None,
    candidate_signal: Mapping[str, Any] | None,
    *,
    source_path_hint: Path | str | None = None,
    selection_mode: str = "provided_source_mapping",
) -> dict[str, Any]:
    if source_artifact is None:
        candidate_copy = _candidate_mapping(candidate_signal)
        source_identity = _empty_source_identity(selection_mode="no_source_artifact")
        checks = _build_checks(
            None,
            candidate_signal if isinstance(candidate_signal, Mapping) else None,
            source_identity,
            source_path_hint=source_path_hint,
            source_readable=False,
            source_malformed=False,
        )
        failed = _first_failed(checks)
        return _build_result(
            source_identity=source_identity,
            candidate_signal=candidate_copy,
            checks=checks,
            outcome=OUTCOME_BLOCKED,
            block_code=str(failed.get("block_code")) if failed else "NO_SOURCE_ARTIFACT_BASIS",
        )

    if not isinstance(source_artifact, Mapping):
        source_identity = _empty_source_identity(selection_mode="malformed_source_artifact")
        return _blocked_result(
            "SOURCE_ARTIFACT_MALFORMED",
            block_detail="source artifact input must be a mapping",
            source_identity=source_identity,
            candidate_signal=_candidate_mapping(candidate_signal),
        )

    source_identity = _source_identity(
        source_artifact,
        source_path_hint,
        candidate_signal if isinstance(candidate_signal, Mapping) else None,
        selection_mode,
    )

    if candidate_signal is not None and not isinstance(candidate_signal, Mapping):
        checks = [
            _check(
                "candidate_signal_declaration_well_formed_enough",
                False,
                "candidate signal declaration must be an object",
                type(candidate_signal).__name__,
                "CANDIDATE_SIGNAL_DECLARATION_MALFORMED",
            )
        ]
        return _build_result(
            source_identity=source_identity,
            candidate_signal={},
            checks=checks,
            outcome=OUTCOME_BLOCKED,
            block_code="CANDIDATE_SIGNAL_DECLARATION_MALFORMED",
        )

    if candidate_signal is None:
        candidate_copy: dict[str, Any] = {}
    elif isinstance(candidate_signal, Mapping):
        candidate_copy = _candidate_mapping(candidate_signal)
    else:
        candidate_copy = {}

    checks = _build_checks(
        source_artifact,
        candidate_signal if isinstance(candidate_signal, Mapping) else None,
        source_identity,
        source_path_hint=source_path_hint,
        source_readable=True,
        source_malformed=False,
    )
    failed = _first_failed(checks)
    if failed is not None:
        return _build_result(
            source_identity=source_identity,
            candidate_signal=candidate_copy,
            checks=checks,
            outcome=OUTCOME_BLOCKED,
            block_code=str(failed.get("block_code")),
        )
    return _build_result(
        source_identity=source_identity,
        candidate_signal=candidate_copy,
        checks=checks,
        outcome=OUTCOME_SIGNAL_RECOGNIZED,
        block_code=None,
    )


def resolve_body_signal_recognition(
    source_artifact: Mapping[str, Any] | None = None,
    candidate_signal: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded body-signal recognition decision."""

    try:
        return _resolve_internal(source_artifact, candidate_signal)
    except BodySignalRecognitionError as exc:
        return _blocked_result(
            exc.block_code,
            block_detail=str(exc),
            source_identity=exc.selected_source,
            candidate_signal=exc.selected_candidate or _candidate_mapping(candidate_signal),
            checks=exc.checks,
        )


def resolve_body_signal_recognition_from_path(
    source_artifact_path: Path | str,
    candidate_signal: Mapping[str, Any],
) -> dict[str, Any]:
    """Resolve one body-signal recognition decision from an explicit source path."""

    source_identity = _empty_source_identity(
        source_path_hint=source_artifact_path,
        selection_mode="explicit_source_artifact_path",
    )
    try:
        source_artifact = _read_json_file(source_artifact_path)
        return _resolve_internal(
            source_artifact,
            candidate_signal,
            source_path_hint=source_artifact_path,
            selection_mode="explicit_source_artifact_path",
        )
    except BodySignalRecognitionError as exc:
        checks = exc.checks
        if checks is None:
            checks = [
                _check(
                    "source_artifact_is_readable_if_path_based",
                    False,
                    "readable source JSON object for explicit path",
                    _display_path(source_artifact_path),
                    exc.block_code,
                )
            ]
        return _blocked_result(
            exc.block_code,
            block_detail=str(exc),
            source_identity=exc.selected_source or source_identity,
            candidate_signal=_candidate_mapping(candidate_signal),
            checks=checks,
        )


def _check_passed(checks: Sequence[Any], check_name: str) -> bool:
    return any(
        isinstance(check, Mapping)
        and check.get("check_name") == check_name
        and check.get("passed") is True
        for check in checks
    )


def build_body_signal_recognition_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a bounded summary for one body-signal recognition result."""

    if not isinstance(result, Mapping):
        raise BodySignalRecognitionError(
            "body-signal recognition result must be a mapping",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    selected_source = result.get("selected_source_artifact")
    selected_source = selected_source if isinstance(selected_source, Mapping) else {}
    candidate = result.get("selected_candidate_signal")
    candidate = candidate if isinstance(candidate, Mapping) else {}
    recognized = result.get("recognized_signal")
    recognized = recognized if isinstance(recognized, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    checks = result.get("signal_recognition_checks")
    checks = checks if isinstance(checks, list) else []
    non_claims = result.get("non_claims")
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}
    category = _signal_category(candidate)

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_source_artifact_id": selected_source.get("source_artifact_id"),
        "selected_source_artifact_path": selected_source.get("source_artifact_path"),
        "selected_source_artifact_family": selected_source.get("source_artifact_family"),
        "selected_source_artifact_outcome": selected_source.get("source_artifact_outcome"),
        "signal_category": category,
        "recognized_signal_id": recognized.get("recognized_signal_id"),
        "recognized_signal_category": recognized.get("signal_category"),
        "passed_check_count": sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is True
        ),
        "failed_check_count": sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        ),
        "hierarchy_constraints_passed": _check_passed(
            checks,
            "candidate_preserves_hierarchy_constraints",
        ),
        "correspondence_requirements_passed": _check_passed(
            checks,
            "candidate_preserves_correspondence_requirements",
        ),
        "non_claims_passed": _check_passed(
            checks,
            "candidate_preserves_declared_non_claims",
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "authority_created",
                "permission_created",
                "currentness_created",
                "action_authorized",
                "follow_on_work_authorized",
                "workflow_created",
                "roadmap_created",
                "signal_router_created",
                "event_bus_created",
                "source_replaced",
                "derivative_upgraded_to_source",
                "receipt_turned_into_permission",
                "radio_22_implemented",
            )
            if key in non_claims
        },
    }


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = BODY_SIGNAL_RECOGNITION_ROOT,
) -> Path:
    candidate = result.get("selected_candidate_signal")
    candidate = candidate if isinstance(candidate, Mapping) else {}
    source = result.get("selected_source_artifact")
    source = source if isinstance(source, Mapping) else {}
    stem = _safe_filename_part(
        _candidate_signal_id(candidate) or source.get("source_artifact_id")
    )
    resolved_root = _repo_path(root)
    path = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not path.exists():
        return path
    for index in range(1, 1000):
        path = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not path.exists():
            return path
    raise BodySignalRecognitionError(
        "no bounded body-signal recognition filename is available",
        "SOURCE_ARTIFACT_MALFORMED",
    )


def write_body_signal_recognition_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive body-signal recognition JSON artifact."""

    if not isinstance(result, Mapping):
        raise BodySignalRecognitionError(
            "body-signal recognition result must be a mapping",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"body-signal recognition result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
