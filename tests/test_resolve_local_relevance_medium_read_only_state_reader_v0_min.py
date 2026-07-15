"""Tests for the local relevance medium read-only state reader resolver.

This suite is bounded to one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET from
one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER. It verifies that the resolver
reads one clean local relevance medium comparison view artifact, reconstructs
the known local medium artifact chain, preserves selected artifact paths and
standing identifiers, and remains read-only.

The suite does not create an index system, registry, search, ranking, scoring,
priority, validity judgment, truth judgment, authority judgment, currentness
judgment, repeated reception permission, arbitrary reception, feed, new signal,
new relevance object, new reception, new receipt, new orientation view, new
index entry, new multiplicity result, new relation view, new comparison view,
source transfer, source receipt, runtime permission, API, distributed behavior,
operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_state_reader_v0_min as resolver  # noqa: E402


DEFAULT_COMPARISON_VIEW_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_comparison_view_v0_min/"
    "local_relevance_medium_comparison_view_reference_review_001__"
    "local_relevance_medium_comparison_view_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_comparison_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_successor_reception_request_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_loop_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_behavior_v0_min"),
)

EXPECTED_TOP_LEVEL_SECTIONS = {
    "local_relevance_medium_read_only_state_reader_metadata",
    "declared_local_relevance_medium_read_only_state_reader_question",
    "selected_local_relevance_medium_comparison_view_artifact_basis",
    "local_relevance_medium_read_only_state_packet",
    "local_relevance_medium_read_only_state_reader_checks",
    "local_relevance_medium_read_only_state_reader_statement",
    "local_relevance_medium_read_only_state_reader_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_reader_summary",
}

WRAPPER_FIELDS_FORBIDDEN_IN_STATE_PACKET = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_reader_checks",
    "non_claims",
    "local_relevance_medium_read_only_state_reader_summary",
    "local_relevance_medium_read_only_state_reader_metadata",
}

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_READER_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_COMPARISON_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_RELATION_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_MULTIPLICITY_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

NO_NEW_CONTENT_NON_CLAIMS = (
    "new_signal_accepted",
    "new_relevance_object_created",
    "new_reception_created",
    "new_receipt_created",
    "new_orientation_view_created",
    "new_index_entry_created",
    "new_multiplicity_result_created",
    "new_relation_view_created",
    "new_comparison_view_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
    "scoring_surface_created",
    "priority_surface_created",
    "validity_judgment_created",
    "truth_judgment_created",
    "authority_judgment_created",
    "currentness_judgment_created",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "action_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "operation_permission_created",
    "broader_reusable_permission_created",
    "follow_on_work_authorized",
)


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _state_packet(result: Mapping[str, Any]) -> Mapping[str, Any]:
    state_packet = result.get("local_relevance_medium_read_only_state_packet")
    if not isinstance(state_packet, Mapping):
        raise AssertionError("local_relevance_medium_read_only_state_packet is not a mapping")
    return state_packet


def _statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    statement = result.get("local_relevance_medium_read_only_state_reader_statement")
    if not isinstance(statement, Mapping):
        raise AssertionError("local_relevance_medium_read_only_state_reader_statement is not a mapping")
    return statement


def _summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = result.get("local_relevance_medium_read_only_state_reader_summary")
    if not isinstance(summary, Mapping):
        raise AssertionError("local_relevance_medium_read_only_state_reader_summary is not a mapping")
    return summary


def _checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    checks = result.get("local_relevance_medium_read_only_state_reader_checks")
    if not isinstance(checks, list):
        raise AssertionError("local_relevance_medium_read_only_state_reader_checks is not a list")
    return checks


def _block_code(result: Mapping[str, Any]) -> str | None:
    block = result.get("block")
    if not isinstance(block, Mapping):
        return None
    code = block.get("code") or block.get("block_code")
    return code if isinstance(code, str) else None


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")


def _synthetic_chain_paths(directory: Path) -> tuple[dict[str, str], Path]:
    comparison_path = directory / "synthetic_comparison_view_artifact.json"
    paths: dict[str, str] = {}
    for chain_key in resolver.KNOWN_ARTIFACT_CHAIN:
        if chain_key == "local_relevance_medium_comparison_view":
            paths[chain_key] = str(comparison_path)
        else:
            paths[chain_key] = str(directory / f"{chain_key}__synthetic_result.json")
    return paths, comparison_path


def _clean_comparison_view_object(chain_paths: Mapping[str, str]) -> dict[str, Any]:
    return {
        "comparison_view_id": "local_relevance_medium_comparison_view_001",
        "comparison_view_type": "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW",
        "comparison_view_version": "0.1.0",
        "comparison_view_scope": "TWO_LOCAL_ORIENTATION_OBJECTS_COMPARISON_VIEW_ONLY",
        "comparison_frame": "BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY",
        "basis_local_relevance_medium_relation_view_artifact": chain_paths[
            "local_relevance_medium_relation_view"
        ],
        "basis_local_relevance_medium_relation_view_outcome": (
            "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_RECORDED"
        ),
        "basis_local_relevance_medium_relation_view_result_version": "0.1.0",
        "basis_local_relevance_medium_relation_view_failed_check_count": 0,
        "basis_local_relevance_medium_multiplicity_result_artifact": chain_paths[
            "local_relevance_medium_multiplicity_result"
        ],
        "basis_first_local_relevance_orientation_index_entry_artifact": chain_paths[
            "local_relevance_orientation_index_entry"
        ],
        "basis_second_local_relevance_orientation_index_entry_artifact": chain_paths[
            "local_relevance_medium_second_local_relevance_orientation_index_entry"
        ],
        "first_orientation_view_artifact": chain_paths["relevance_orientation_view"],
        "second_orientation_view_artifact": chain_paths[
            "local_relevance_medium_second_relevance_orientation_view"
        ],
        "first_receipt_artifact": chain_paths["bounded_relevance_receipt_v2"],
        "second_receipt_artifact": chain_paths[
            "local_relevance_medium_second_bounded_relevance_receipt"
        ],
        "first_reception_artifact": chain_paths["bounded_relevance_reception"],
        "second_reception_artifact": chain_paths[
            "local_relevance_medium_second_bounded_relevance_reception"
        ],
        "successor_candidate_admission_artifact": chain_paths[
            "local_relevance_medium_successor_candidate_admission"
        ],
        "successor_reception_request_artifact": chain_paths[
            "local_relevance_medium_successor_reception_request"
        ],
        "first_received_signal_id": "bounded_relevance_signal_001",
        "second_received_signal_id": "bounded_relevance_signal_002",
        "first_relevance_basis_id": "bounded_relevance_basis_001",
        "second_relevance_basis_id": "bounded_relevance_basis_002",
        "first_relevance_scope_id": "bounded_relevance_scope_001",
        "second_relevance_scope_id": "bounded_relevance_scope_002",
        "first_carrier_context_id": "bounded_relevance_signal_carrier_context_001",
        "second_carrier_context_id": "bounded_relevance_signal_carrier_context_002",
        "first_reception_envelope_id": "bounded_relevance_reception_envelope_001",
        "second_reception_envelope_id": "bounded_relevance_reception_envelope_002",
        "multiplicity_count": 2,
        "relation_pair_count": 1,
        "comparison_pair_count": 1,
        "first_and_second_signals_distinct": True,
        "two_local_orientation_objects_preserved": True,
        "relation_readable_co_presence_preserved": True,
        "comparison_readable_distinctions_recorded": True,
        "comparison_view_recorded": True,
        "ranking_surface_created": False,
        "scoring_surface_created": False,
        "priority_surface_created": False,
        "validity_judgment_created": False,
        "truth_judgment_created": False,
        "authority_judgment_created": False,
        "currentness_judgment_created": False,
        "index_system_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "authority_created": False,
        "currentness_created": False,
        "truth_created": False,
        "action_created": False,
        "synchronization_created": False,
        "participation_authorized": False,
        "participant_role_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "follow_on_work_authorized": False,
    }


def _clean_comparison_view_artifact(chain_paths: Mapping[str, str]) -> dict[str, Any]:
    return {
        "local_relevance_medium_comparison_view_metadata": {
            "local_relevance_medium_comparison_view_id": "local_relevance_medium_comparison_view_001",
            "local_relevance_medium_comparison_view_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_comparison_view_v0_min",
            "result_version": "0.1.0",
        },
        "local_relevance_medium_comparison_view_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_RECORDED",
            "failed_check_count": 0,
            "passed_check_count": 187,
            "result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_comparison_view_v0_min",
            "local_relevance_medium_comparison_view_recorded": True,
        },
        "local_relevance_medium_comparison_view_checks": [
            {
                "check_name": "synthetic_comparison_view_artifact_clean",
                "passed": True,
                "expected_posture": "clean local relevance medium comparison view artifact",
                "actual_posture": "clean local relevance medium comparison view artifact",
            }
        ],
        "local_relevance_medium_comparison_view": _clean_comparison_view_object(chain_paths),
        "outcome": "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_RECORDED",
        "failed_check_count": 0,
        "result_version": "0.1.0",
    }


def _lightweight_standing_artifact(chain_key: str) -> dict[str, Any]:
    outcome = resolver.EXPECTED_ARTIFACT_OUTCOMES[chain_key]
    version = resolver.EXPECTED_ARTIFACT_RESULT_VERSIONS[chain_key]
    object_type = resolver.EXPECTED_ARTIFACT_OBJECT_TYPES[chain_key]
    return {
        "outcome": outcome,
        "result_version": version,
        "failed_check_count": 0,
        f"{chain_key}_metadata": {
            "result_version": version,
            "resolver_module": f"synthetic_{chain_key}_resolver",
        },
        f"{chain_key}_summary": {
            "outcome": outcome,
            "result_version": version,
            "failed_check_count": 0,
            "passed_check_count": 1,
        },
        f"{chain_key}_object": {
            "object_type": object_type,
            f"{chain_key}_type": object_type,
        },
    }


def _write_synthetic_fixture(
    directory: Path,
    comparison_mutator: Callable[[dict[str, Any]], None] | None = None,
    standing_mutators: Mapping[str, Callable[[dict[str, Any]], None]] | None = None,
    hostile: bool = False,
) -> tuple[Path, dict[str, Any], dict[str, str], dict[str, dict[str, Any]]]:
    chain_paths, comparison_path = _synthetic_chain_paths(directory)
    standing_bodies: dict[str, dict[str, Any]] = {}
    for chain_key in resolver.KNOWN_ARTIFACT_CHAIN:
        if chain_key == "local_relevance_medium_comparison_view":
            continue
        body = _lightweight_standing_artifact(chain_key)
        if hostile:
            body["raw_full_body"] = HOSTILE_SENTINELS[25]
            body["hidden_repo_state"] = {"payload": HOSTILE_SENTINELS[-1]}
        if standing_mutators and chain_key in standing_mutators:
            standing_mutators[chain_key](body)
        standing_bodies[chain_key] = copy.deepcopy(body)
        _write_json(Path(chain_paths[chain_key]), body)

    comparison_body = _clean_comparison_view_artifact(chain_paths)
    if hostile:
        comparison_body["raw_comparison_view_body"] = HOSTILE_SENTINELS[4]
        comparison_body["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
        comparison_body["local_relevance_medium_comparison_view"]["raw_full_body"] = (
            HOSTILE_SENTINELS[25]
        )
    if comparison_mutator:
        comparison_mutator(comparison_body)
    _write_json(comparison_path, comparison_body)
    standing_bodies["local_relevance_medium_comparison_view"] = copy.deepcopy(comparison_body)
    return comparison_path, comparison_body, chain_paths, standing_bodies


def _clean_request(comparison_artifact: Path | str, chain_paths: Mapping[str, str]) -> dict[str, Any]:
    return resolver.build_declared_local_relevance_medium_read_only_state_reader_v0_min_request(
        selected_local_relevance_medium_comparison_view_artifact=str(comparison_artifact),
        known_artifact_chain=copy.deepcopy(resolver.KNOWN_ARTIFACT_CHAIN),
        validated_standing_artifacts=copy.deepcopy(dict(chain_paths)),
    )


def _mutate_comparison_view(artifact: dict[str, Any], key: str, value: Any) -> None:
    artifact["local_relevance_medium_comparison_view"][key] = value


class LocalRelevanceMediumReadOnlyStateReaderResolverTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_output_not_under_prior_roots(self, output_path: Path) -> None:
        if output_path.is_absolute():
            candidate = output_path.resolve()
            forbidden_roots = [(REPO_ROOT / root).resolve() for root in FORBIDDEN_OUTPUT_ROOTS]
        else:
            candidate = output_path
            forbidden_roots = list(FORBIDDEN_OUTPUT_ROOTS)
        for root in forbidden_roots:
            self.assertFalse(candidate == root or _is_relative_to(candidate, root), root)

    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block_code = _block_code(result)
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in _checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIs(type(non_claims[key]), bool, key)

    def assert_no_new_or_overreach_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in NO_NEW_CONTENT_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_state_packet_not_wrapper(self, state_packet: Mapping[str, Any]) -> None:
        for key in WRAPPER_FIELDS_FORBIDDEN_IN_STATE_PACKET:
            self.assertNotIn(key, state_packet)

    def assert_recorded_statement_shape(self, result: Mapping[str, Any]) -> None:
        statement = _statement(result)
        true_fields = (
            "local_relevance_medium_read_only_state_packet_recorded",
            "local_relevance_medium_read_only_state_reader_recorded",
            "basis_comparison_view_artifact_preserved",
            "known_artifact_chain_preserved",
            "validated_standing_artifacts_preserved",
            "standing_object_types_preserved",
            "standing_outcomes_preserved",
            "standing_result_versions_preserved",
            "standing_failed_check_counts_preserved",
            "first_received_signal_id_preserved",
            "second_received_signal_id_preserved",
            "first_and_second_signals_distinct",
            "first_relevance_basis_id_preserved",
            "second_relevance_basis_id_preserved",
            "first_relevance_scope_id_preserved",
            "second_relevance_scope_id_preserved",
            "first_carrier_context_id_preserved",
            "second_carrier_context_id_preserved",
            "first_reception_envelope_id_preserved",
            "second_reception_envelope_id_preserved",
            "multiplicity_count_is_two",
            "relation_pair_count_is_one",
            "comparison_pair_count_is_one",
            "comparison_readability_stands",
            "relation_readability_stands",
            "multiplicity_result_stands",
            "two_local_orientation_objects_stand",
            "chain_validated",
            "state_reconstruction_read_only",
            "result_level_non_claims_canonical_false",
        )
        for key in true_fields:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
            self.assertIs(type(statement[key]), bool, key)

    def assert_recorded_state_packet_shape(
        self,
        result: Mapping[str, Any],
        comparison_artifact_path: Path | str,
    ) -> None:
        state_packet = _state_packet(result)
        self.assertEqual(state_packet["state_packet_id"], "local_relevance_medium_read_only_state_packet_001")
        self.assertEqual(state_packet["state_packet_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET")
        self.assertEqual(state_packet["state_packet_version"], "0.1.0")
        self.assertEqual(state_packet["state_reader_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER")
        self.assertEqual(state_packet["state_reader_version"], "0.1.0")
        self.assertEqual(state_packet["state_reader_scope"], "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY")
        self.assertEqual(state_packet["basis_comparison_view_artifact"], str(comparison_artifact_path))
        self.assertEqual(
            state_packet["basis_comparison_view_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_RECORDED",
        )
        self.assertEqual(state_packet["basis_comparison_view_result_version"], "0.1.0")
        self.assertEqual(state_packet["basis_comparison_view_failed_check_count"], 0)
        self.assertEqual(state_packet["known_artifact_chain"], resolver.KNOWN_ARTIFACT_CHAIN)
        self.assertEqual(set(state_packet["validated_standing_artifacts"]), set(resolver.KNOWN_ARTIFACT_CHAIN))
        for key in (
            "standing_object_types",
            "standing_outcomes",
            "standing_result_versions",
            "standing_failed_check_counts",
        ):
            self.assertIsInstance(state_packet[key], dict, key)
        self.assertEqual(state_packet["first_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(state_packet["second_received_signal_id"], "bounded_relevance_signal_002")
        self.assertNotEqual(state_packet["first_received_signal_id"], state_packet["second_received_signal_id"])
        self.assertEqual(state_packet["first_relevance_basis_id"], "bounded_relevance_basis_001")
        self.assertEqual(state_packet["second_relevance_basis_id"], "bounded_relevance_basis_002")
        self.assertEqual(state_packet["first_relevance_scope_id"], "bounded_relevance_scope_001")
        self.assertEqual(state_packet["second_relevance_scope_id"], "bounded_relevance_scope_002")
        self.assertEqual(
            state_packet["first_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_001",
        )
        self.assertEqual(
            state_packet["second_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_002",
        )
        self.assertEqual(
            state_packet["first_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        self.assertEqual(
            state_packet["second_reception_envelope_id"],
            "bounded_relevance_reception_envelope_002",
        )
        self.assertEqual(state_packet["multiplicity_count"], 2)
        self.assertEqual(state_packet["relation_pair_count"], 1)
        self.assertEqual(state_packet["comparison_pair_count"], 1)
        for key in (
            "comparison_readability_stands",
            "relation_readability_stands",
            "multiplicity_result_stands",
            "two_local_orientation_objects_stand",
            "chain_validated",
            "state_reconstruction_read_only",
        ):
            self.assertIs(state_packet[key], True, key)
        for key in (
            "new_signal_accepted",
            "new_relevance_object_created",
            "new_reception_created",
            "new_receipt_created",
            "new_orientation_view_created",
            "new_index_entry_created",
            "new_multiplicity_result_created",
            "new_relation_view_created",
            "new_comparison_view_created",
            "index_system_created",
            "registry_created",
            "search_surface_created",
            "ranking_surface_created",
            "scoring_surface_created",
            "priority_surface_created",
            "validity_judgment_created",
            "truth_judgment_created",
            "authority_judgment_created",
            "currentness_judgment_created",
            "repeated_reception_permission_created",
            "arbitrary_reception_created",
            "feed_created",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "authority_created",
            "currentness_created",
            "truth_created",
            "action_created",
            "synchronization_created",
            "participation_authorized",
            "participant_role_created",
            "runtime_permission_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "follow_on_work_authorized",
        ):
            self.assertIn(key, state_packet)
            self.assertIs(state_packet[key], False, key)
        self.assert_state_packet_not_wrapper(state_packet)

    def resolve_from_synthetic_artifact(
        self,
        directory: Path,
        comparison_mutator: Callable[[dict[str, Any]], None] | None = None,
        standing_mutators: Mapping[str, Callable[[dict[str, Any]], None]] | None = None,
        request_updates: Mapping[str, Any] | None = None,
    ) -> tuple[dict[str, Any], Path, dict[str, Any], dict[str, str], dict[str, dict[str, Any]], dict[str, Any]]:
        comparison_path, comparison_body, chain_paths, standing_bodies = _write_synthetic_fixture(
            directory,
            comparison_mutator=comparison_mutator,
            standing_mutators=standing_mutators,
        )
        request = _clean_request(comparison_path, chain_paths)
        if request_updates:
            request.update(copy.deepcopy(dict(request_updates)))
        request_before = copy.deepcopy(request)
        result = resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min(request)
        return result, comparison_path, comparison_body, chain_paths, standing_bodies, request_before

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_state_reader_v0_min",
            "resolve_local_relevance_medium_read_only_state_reader_v0_min_from_path",
            "write_local_relevance_medium_read_only_state_reader_v0_min_result",
            "build_local_relevance_medium_read_only_state_reader_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_state_reader_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_STATE_PACKET_TYPE_VALUES",
            "SUPPORTED_STATE_READER_TYPE_VALUES",
            "SUPPORTED_STATE_READER_SCOPE_VALUES",
            "KNOWN_ARTIFACT_CHAIN",
            "DEFAULT_VALIDATED_STANDING_ARTIFACTS",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_state_reader_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
            resolver.SUPPORTED_STATE_PACKET_TYPE_VALUES,
        )
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
            resolver.SUPPORTED_STATE_READER_TYPE_VALUES,
        )
        self.assertIn(
            "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
            resolver.SUPPORTED_STATE_READER_SCOPE_VALUES,
        )
        self.assertEqual(
            resolver.KNOWN_ARTIFACT_CHAIN,
            [
                "bounded_relevance_reception",
                "bounded_relevance_receipt_v2",
                "relevance_orientation_view",
                "local_relevance_orientation_index_entry",
                "local_relevance_medium_successor_reception_request",
                "local_relevance_medium_successor_candidate_admission",
                "local_relevance_medium_second_bounded_relevance_reception",
                "local_relevance_medium_second_bounded_relevance_receipt",
                "local_relevance_medium_second_relevance_orientation_view",
                "local_relevance_medium_second_local_relevance_orientation_index_entry",
                "local_relevance_medium_multiplicity_result",
                "local_relevance_medium_relation_view",
                "local_relevance_medium_comparison_view",
            ],
        )
        self.assertEqual(len(resolver.KNOWN_ARTIFACT_CHAIN), 13)
        self.assert_output_not_under_prior_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_comparison_view_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            (
                result,
                comparison_path,
                _comparison_body,
                _chain_paths,
                _standing_bodies,
                _request_before,
            ) = self.resolve_from_synthetic_artifact(Path(tmp))

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        summary = _summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_local_relevance_medium_read_only_state_reader_v0_min",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            _state_packet(result)["state_packet_id"],
            "local_relevance_medium_read_only_state_packet_001",
        )
        self.assertTrue(EXPECTED_TOP_LEVEL_SECTIONS.issubset(result.keys()))
        self.assert_recorded_state_packet_shape(result, comparison_path)
        self.assert_recorded_statement_shape(result)
        self.assert_non_claims_canonical_false(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_COMPARISON_VIEW_ARTIFACT.exists():
            self.skipTest("default local relevance medium comparison view artifact is not present")

        request = resolver.build_declared_local_relevance_medium_read_only_state_reader_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min(request)
        state_packet = _state_packet(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(_summary(result)["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(state_packet["state_packet_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET")
        self.assertEqual(state_packet["state_reader_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER")
        self.assertEqual(state_packet["state_reader_scope"], "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY")
        self.assertEqual(state_packet["known_artifact_chain"], resolver.KNOWN_ARTIFACT_CHAIN)
        self.assertEqual(state_packet["first_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(state_packet["second_received_signal_id"], "bounded_relevance_signal_002")
        self.assertNotEqual(state_packet["first_received_signal_id"], state_packet["second_received_signal_id"])
        self.assertEqual(state_packet["multiplicity_count"], 2)
        self.assertEqual(state_packet["relation_pair_count"], 1)
        self.assertEqual(state_packet["comparison_pair_count"], 1)
        for key in (
            "comparison_readability_stands",
            "relation_readability_stands",
            "multiplicity_result_stands",
            "two_local_orientation_objects_stand",
            "chain_validated",
            "state_reconstruction_read_only",
        ):
            self.assertIs(state_packet[key], True, key)
        for key in (
            "new_signal_accepted",
            "new_relevance_object_created",
            "new_reception_created",
            "new_receipt_created",
            "new_orientation_view_created",
            "new_index_entry_created",
            "new_multiplicity_result_created",
            "new_relation_view_created",
            "new_comparison_view_created",
            "index_system_created",
            "registry_created",
            "search_surface_created",
            "ranking_surface_created",
            "scoring_surface_created",
            "priority_surface_created",
            "validity_judgment_created",
            "truth_judgment_created",
            "authority_judgment_created",
            "currentness_judgment_created",
            "repeated_reception_permission_created",
            "arbitrary_reception_created",
            "feed_created",
            "authority_created",
            "currentness_created",
            "action_created",
            "synchronization_created",
            "participation_authorized",
            "runtime_permission_created",
            "public_api_created",
            "distributed_network_behavior_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(state_packet[key], False, key)

    def test_declared_non_claim_flips_block_and_are_canonicalized(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            comparison_path, _comparison_body, chain_paths, _standing_bodies = _write_synthetic_fixture(
                Path(tmp)
            )
            clean_request = _clean_request(comparison_path, chain_paths)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min(request)
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIsNotNone(_block_code(result))
                    self.assertIn(_block_code(result), resolver.BLOCK_CODES)
                    self.assertGreater(_summary(result)["failed_check_count"], 0)
                    self.assert_public_block_codes(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_non_claims_canonical_false(result)
                    self.assert_no_new_or_overreach_created(result)

    def _comparison_mutation_case(
        self,
        directory: Path,
        mutate: Callable[[dict[str, Any]], None],
        request_updates: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        result, _path, _body, _chain_paths, _standing_bodies, _request_before = (
            self.resolve_from_synthetic_artifact(
                directory,
                comparison_mutator=mutate,
                request_updates=request_updates,
            )
        )
        return result

    def _standing_mutation_case(
        self,
        directory: Path,
        chain_key: str,
        mutate: Callable[[dict[str, Any]], None],
    ) -> dict[str, Any]:
        result, _path, _body, _chain_paths, _standing_bodies, _request_before = (
            self.resolve_from_synthetic_artifact(
                directory,
                standing_mutators={chain_key: mutate},
            )
        )
        return result

    def _request_update_case(
        self,
        directory: Path,
        request_updates: Mapping[str, Any],
    ) -> dict[str, Any]:
        result, _path, _body, _chain_paths, _standing_bodies, _request_before = (
            self.resolve_from_synthetic_artifact(directory, request_updates=request_updates)
        )
        return result

    def test_representative_blocking_behavior(self) -> None:
        false_posture_flags = (
            "new_signal_accepted",
            "new_relevance_object_created",
            "new_reception_created",
            "new_receipt_created",
            "new_orientation_view_created",
            "new_index_entry_created",
            "new_multiplicity_result_created",
            "new_relation_view_created",
            "new_comparison_view_created",
            "index_system_created",
            "registry_created",
            "search_surface_created",
            "ranking_surface_created",
            "scoring_surface_created",
            "priority_surface_created",
            "validity_judgment_created",
            "truth_judgment_created",
            "authority_judgment_created",
            "currentness_judgment_created",
            "repeated_reception_permission_created",
            "arbitrary_reception_created",
            "feed_created",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "source_created",
            "authority_created",
            "currentness_created",
            "truth_created",
            "action_created",
            "synchronization_created",
            "participation_authorized",
            "participant_role_created",
            "runtime_permission_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "broader_reusable_permission_created",
            "follow_on_work_authorized",
            "artifact_existence_treated_as_read_only_state_authority",
            "latest_file_posture_treated_as_read_only_state_authority",
            "repo_local_availability_treated_as_read_only_state_authority",
            "hidden_repo_state_used_as_read_only_state_content",
            "hidden_repo_state_used_as_read_only_state_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        )
        comparison_field_missing = {
            "first received signal id missing": "first_received_signal_id",
            "second received signal id missing": "second_received_signal_id",
            "first relevance basis id missing": "first_relevance_basis_id",
            "second relevance basis id missing": "second_relevance_basis_id",
            "first relevance scope id missing": "first_relevance_scope_id",
            "second relevance scope id missing": "second_relevance_scope_id",
            "first carrier context id missing": "first_carrier_context_id",
            "second carrier context id missing": "second_carrier_context_id",
            "first reception envelope id missing": "first_reception_envelope_id",
            "second reception envelope id missing": "second_reception_envelope_id",
        }

        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            array_artifact_path = directory / "array_comparison_view_artifact.json"
            _write_json(array_artifact_path, [{"not": "object"}])
            bad_json_standing_path = directory / "bad_standing.json"
            bad_json_standing_path.write_text("{not valid json", encoding="utf-8")
            array_standing_path = directory / "array_standing.json"
            _write_json(array_standing_path, [])

            cases: list[tuple[str, Callable[[], dict[str, Any]]]] = [
                (
                    "explicit block intent",
                    lambda: self._request_update_case(
                        directory,
                        {
                            "local_relevance_medium_read_only_state_reader_intent": (
                                "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER"
                            )
                        },
                    ),
                ),
                ("missing request", lambda: resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min()),
                (
                    "non-mapping request",
                    lambda: resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min([]),
                ),
                (
                    "unsupported intent",
                    lambda: self._request_update_case(
                        directory,
                        {"local_relevance_medium_read_only_state_reader_intent": "CREATE_A_REGISTRY"},
                    ),
                ),
                (
                    "selected comparison view artifact path missing",
                    lambda: self._request_update_case(
                        directory,
                        {"selected_local_relevance_medium_comparison_view_artifact": ""},
                    ),
                ),
                (
                    "selected comparison view artifact unreadable",
                    lambda: self._request_update_case(
                        directory,
                        {
                            "selected_local_relevance_medium_comparison_view_artifact": str(
                                directory / "missing_comparison.json"
                            )
                        },
                    ),
                ),
                (
                    "selected comparison view artifact JSON array",
                    lambda: self._request_update_case(
                        directory,
                        {
                            "selected_local_relevance_medium_comparison_view_artifact": str(
                                array_artifact_path
                            )
                        },
                    ),
                ),
                (
                    "selected comparison view artifact not recorded",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: artifact.update(
                            {"outcome": "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_NOT_RECORDED"}
                        ),
                    ),
                ),
                (
                    "selected comparison view artifact failed checks present",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: artifact[
                            "local_relevance_medium_comparison_view_summary"
                        ].update({"failed_check_count": 1}),
                    ),
                ),
                (
                    "selected comparison view artifact version not 0.1.0",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: artifact[
                            "local_relevance_medium_comparison_view_summary"
                        ].update({"result_version": "9.9.9"}),
                    ),
                ),
                (
                    "local relevance medium comparison view object missing",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: artifact.pop("local_relevance_medium_comparison_view", None),
                    ),
                ),
                (
                    "comparison view type invalid",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(
                            artifact,
                            "comparison_view_type",
                            "LOCAL_RELEVANCE_INDEX",
                        ),
                    ),
                ),
                (
                    "comparison view scope invalid",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(
                            artifact,
                            "comparison_view_scope",
                            "READ_ALL_LOCAL_STATE",
                        ),
                    ),
                ),
                (
                    "comparison frame invalid",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(
                            artifact,
                            "comparison_frame",
                            "RANKING_COMPARISON_FRAME",
                        ),
                    ),
                ),
                (
                    "required artifact path missing shortcut",
                    lambda: self._request_update_case(directory, {"required_artifact_path_missing": True}),
                ),
                (
                    "required artifact unreadable",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(
                            artifact,
                            "first_receipt_artifact",
                            str(bad_json_standing_path),
                        ),
                    ),
                ),
                (
                    "required artifact not JSON object",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(
                            artifact,
                            "first_reception_artifact",
                            str(array_standing_path),
                        ),
                    ),
                ),
                (
                    "required artifact outcome not recorded",
                    lambda: self._standing_mutation_case(
                        directory,
                        "local_relevance_medium_relation_view",
                        lambda artifact: artifact.update({"outcome": "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_NOT_RECORDED"}),
                    ),
                ),
                (
                    "required artifact failed checks present",
                    lambda: self._standing_mutation_case(
                        directory,
                        "local_relevance_medium_relation_view",
                        lambda artifact: artifact[
                            "local_relevance_medium_relation_view_summary"
                        ].update({"failed_check_count": 1}),
                    ),
                ),
                (
                    "required artifact result version not 0.1.0",
                    lambda: self._standing_mutation_case(
                        directory,
                        "local_relevance_medium_relation_view",
                        lambda artifact: artifact[
                            "local_relevance_medium_relation_view_summary"
                        ].update({"result_version": "9.9.9"}),
                    ),
                ),
                (
                    "required object missing shortcut",
                    lambda: self._request_update_case(directory, {"required_object_missing": True}),
                ),
                (
                    "known artifact chain not canonical",
                    lambda: self._request_update_case(
                        directory,
                        {"known_artifact_chain": list(reversed(resolver.KNOWN_ARTIFACT_CHAIN))},
                    ),
                ),
                (
                    "lineage mismatch across selected artifacts",
                    lambda: self._request_update_case(
                        directory,
                        {
                            "validated_standing_artifacts": {
                                **resolver.DEFAULT_VALIDATED_STANDING_ARTIFACTS,
                                "local_relevance_medium_comparison_view": "wrong.json",
                            }
                        },
                    ),
                ),
                (
                    "first and second received signal ids not distinct",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: (
                            _mutate_comparison_view(
                                artifact,
                                "second_received_signal_id",
                                "bounded_relevance_signal_001",
                            ),
                            _mutate_comparison_view(
                                artifact,
                                "first_and_second_signals_distinct",
                                False,
                            ),
                        ),
                    ),
                ),
                (
                    "multiplicity count not two",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(artifact, "multiplicity_count", 3),
                    ),
                ),
                (
                    "relation pair count not one",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(artifact, "relation_pair_count", 2),
                    ),
                ),
                (
                    "comparison pair count not one",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(artifact, "comparison_pair_count", 2),
                    ),
                ),
                (
                    "relation-readable co-presence not preserved",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(
                            artifact,
                            "relation_readable_co_presence_preserved",
                            False,
                        ),
                    ),
                ),
                (
                    "comparison-readable distinctions not recorded",
                    lambda: self._comparison_mutation_case(
                        directory,
                        lambda artifact: _mutate_comparison_view(
                            artifact,
                            "comparison_readable_distinctions_recorded",
                            False,
                        ),
                    ),
                ),
                (
                    "state packet type missing",
                    lambda: self._request_update_case(directory, {"state_packet_type": ""}),
                ),
                (
                    "state packet type invalid",
                    lambda: self._request_update_case(
                        directory,
                        {"state_packet_type": "LOCAL_RELEVANCE_INDEX"},
                    ),
                ),
                (
                    "state reader type missing",
                    lambda: self._request_update_case(directory, {"state_reader_type": ""}),
                ),
                (
                    "state reader type invalid",
                    lambda: self._request_update_case(
                        directory,
                        {"state_reader_type": "LOCAL_RELEVANCE_MEDIUM_RUNTIME"},
                    ),
                ),
                (
                    "state reader scope missing",
                    lambda: self._request_update_case(directory, {"state_reader_scope": ""}),
                ),
                (
                    "state reader scope invalid",
                    lambda: self._request_update_case(
                        directory,
                        {"state_reader_scope": "READ_AND_AUTHORIZE_LOCAL_RELEVANCE_MEDIUM_STATE"},
                    ),
                ),
                (
                    "state reconstruction not read-only",
                    lambda: self._request_update_case(directory, {"state_reconstruction_read_only": False}),
                ),
                (
                    "required non-claim missing or flipped",
                    lambda: self._request_update_case(
                        directory,
                        {
                            "declared_non_claims": {
                                key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]
                            }
                        },
                    ),
                ),
            ]

            for label, field in comparison_field_missing.items():
                cases.append(
                    (
                        label,
                        lambda field=field: self._comparison_mutation_case(
                            directory,
                            lambda artifact, field=field: _mutate_comparison_view(artifact, field, ""),
                        ),
                    )
                )
            for flag in false_posture_flags:
                cases.append((flag, lambda flag=flag: self._request_update_case(directory, {flag: True})))

            for label, make_result in cases:
                with self.subTest(label=label):
                    result = make_result()
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIsNotNone(_block_code(result), label)
                    self.assertIn(_block_code(result), resolver.BLOCK_CODES)
                    self.assert_public_block_codes(result)
                    self.assert_no_new_or_overreach_created(result)
                    self.assert_non_claims_canonical_false(result)

    def test_missing_or_incomplete_declared_non_claims_still_emit_false_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            comparison_path, _comparison_body, chain_paths, _standing_bodies = _write_synthetic_fixture(
                Path(tmp)
            )
            clean_request = _clean_request(comparison_path, chain_paths)
            first_key = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            variants = []

            missing_mapping = copy.deepcopy(clean_request)
            missing_mapping.pop("declared_non_claims", None)
            variants.append(("missing declared_non_claims", missing_mapping))

            empty_mapping = copy.deepcopy(clean_request)
            empty_mapping["declared_non_claims"] = {}
            variants.append(("empty declared_non_claims", empty_mapping))

            missing_one = copy.deepcopy(clean_request)
            missing_one["declared_non_claims"].pop(first_key, None)
            variants.append(("one non-claim removed", missing_one))

            string_value = copy.deepcopy(clean_request)
            string_value["declared_non_claims"][first_key] = "false"
            variants.append(("one non-claim string", string_value))

            none_value = copy.deepcopy(clean_request)
            none_value["declared_non_claims"][first_key] = None
            variants.append(("one non-claim None", none_value))

            for label, request in variants:
                with self.subTest(label=label):
                    result = resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min(request)
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assertIsNotNone(_block_code(result))
                        self.assertIn(_block_code(result), resolver.BLOCK_CODES)
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, _path, _body, _chain_paths, _standing_bodies, _request_before = (
                self.resolve_from_synthetic_artifact(Path(tmp))
            )
        state_packet = _state_packet(result)
        self.assertEqual(state_packet["state_packet_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET")
        self.assertEqual(state_packet["state_reader_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER")
        self.assertEqual(state_packet["state_reader_scope"], "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET", serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER", serialized)
        self.assertIn("READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY", serialized)
        self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            comparison_path, _comparison_body, chain_paths, _standing_bodies = (
                _write_synthetic_fixture(directory, hostile=True)
            )
            request = _clean_request(comparison_path, chain_paths)
            request["raw_full_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = {"payload": HOSTILE_SENTINELS[-1]}
            request["extra_context"] = {"raw_state_packet_body": HOSTILE_SENTINELS[3]}
            request_before = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET", serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER", serialized)
        self.assertIn("READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY", serialized)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_new_or_overreach_created(result)
        self.assertEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            comparison_path, _comparison_body, chain_paths, _standing_bodies = (
                _write_synthetic_fixture(directory)
            )
            request = _clean_request(comparison_path, chain_paths)
            request_path = directory / "declared_read_only_state_reader_request.json"
            _write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(_summary(result)["result_version"], "0.1.0")
            self.assertEqual(
                _summary(result)["resolver_module"],
                "resolve_local_relevance_medium_read_only_state_reader_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = directory / "malformed_request.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min_from_path(
                malformed_path
            )
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(malformed_result)

            array_path = directory / "array_request.json"
            _write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min_from_path(
                directory / "missing_request.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(missing_result)

            output_root = directory / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_output = resolver.write_local_relevance_medium_read_only_state_reader_v0_min_result(
                    result
                )
                second_output = resolver.write_local_relevance_medium_read_only_state_reader_v0_min_result(
                    result
                )

            self.assertTrue(first_output.exists())
            self.assertTrue(first_output.parent.exists())
            parsed = json.loads(first_output.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertTrue(second_output.exists())
            self.assertNotEqual(first_output, second_output)
            self.assertIn("local_relevance_medium_read_only_state_reader_v0_min", str(first_output))
            self.assert_output_not_under_prior_roots(first_output)
            self.assert_output_not_under_prior_roots(second_output)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            comparison_path, comparison_body, chain_paths, standing_bodies = (
                _write_synthetic_fixture(directory, hostile=True)
            )
            comparison_body_before = copy.deepcopy(comparison_body)
            standing_bodies_before = copy.deepcopy(standing_bodies)
            request = _clean_request(comparison_path, chain_paths)
            request["posture_mappings"] = {"index_system_created": False}
            request["nested_raw_payload"] = {"raw_body": HOSTILE_SENTINELS[0]}
            request_before = copy.deepcopy(request)
            non_claims_before = copy.deepcopy(request["declared_non_claims"])
            selected_path_before = request["selected_local_relevance_medium_comparison_view_artifact"]
            chain_before = copy.deepcopy(request["known_artifact_chain"])
            artifacts_before = copy.deepcopy(request["validated_standing_artifacts"])
            packet_type_before = request["state_packet_type"]
            reader_type_before = request["state_reader_type"]
            reader_scope_before = request["state_reader_scope"]

            resolver.resolve_local_relevance_medium_read_only_state_reader_v0_min(request)

        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], non_claims_before)
        self.assertEqual(request["selected_local_relevance_medium_comparison_view_artifact"], selected_path_before)
        self.assertEqual(request["known_artifact_chain"], chain_before)
        self.assertEqual(request["validated_standing_artifacts"], artifacts_before)
        self.assertEqual(request["state_packet_type"], packet_type_before)
        self.assertEqual(request["state_reader_type"], reader_type_before)
        self.assertEqual(request["state_reader_scope"], reader_scope_before)
        self.assertEqual(request["posture_mappings"], request_before["posture_mappings"])
        self.assertEqual(request["nested_raw_payload"], request_before["nested_raw_payload"])
        self.assertEqual(comparison_body, comparison_body_before)
        self.assertEqual(standing_bodies, standing_bodies_before)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, _path, _body, _chain_paths, _standing_bodies, _request_before = (
                self.resolve_from_synthetic_artifact(Path(tmp))
            )
        summary = resolver.build_local_relevance_medium_read_only_state_reader_v0_min_summary(result)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)
        self.assert_non_claims_canonical_false(result)


if __name__ == "__main__":
    unittest.main()
