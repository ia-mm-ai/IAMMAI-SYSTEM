"""Tests for the local relevance medium read-only orientation index system.

This suite is bounded to one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX
from one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM. It verifies
that the resolver reads one clean local relevance medium read-only state packet
artifact, indexes exactly two already-standing local orientation locator
entries, preserves deterministic lookup order, and remains read-only.

The suite does not create registry, search, ranking, scoring, priority,
validity judgment, truth judgment, authority judgment, currentness judgment,
repeated reception permission, arbitrary reception, feed, new signal, new
relevance object, new index entry, filesystem discovery, source transfer,
source receipt, runtime permission, API, distributed behavior, operation
permission, or follow-on work.
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

import resolve_local_relevance_medium_read_only_orientation_index_system_v0_min as resolver  # noqa: E402


DEFAULT_STATE_READER_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min/"
    "local_relevance_medium_read_only_state_packet_reference_review_001__"
    "local_relevance_medium_read_only_state_reader_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min"),
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
    "local_relevance_medium_read_only_orientation_index_system_metadata",
    "declared_local_relevance_medium_read_only_orientation_index_system_question",
    "selected_local_relevance_medium_read_only_state_packet_artifact_basis",
    "local_relevance_medium_read_only_orientation_index",
    "local_relevance_medium_read_only_orientation_index_system_checks",
    "local_relevance_medium_read_only_orientation_index_system_statement",
    "local_relevance_medium_read_only_orientation_index_system_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_orientation_index_system_summary",
}

WRAPPER_FIELDS_FORBIDDEN_IN_ORIENTATION_INDEX = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_orientation_index_system_checks",
    "non_claims",
    "local_relevance_medium_read_only_orientation_index_system_summary",
    "local_relevance_medium_read_only_orientation_index_system_metadata",
}

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_SYSTEM_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_BODY_MUST_NOT_RETURN",
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

ORIENTATION_INDEX_FALSE_FIELDS = (
    "new_signal_accepted",
    "new_relevance_object_created",
    "new_index_entry_created",
    "filesystem_discovery_performed",
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
)


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _artifact_relative(path: Path | str) -> Path:
    candidate = Path(path)
    parts = candidate.parts
    if "artifacts" not in parts:
        return candidate
    return Path(*parts[parts.index("artifacts") :])


def _canonical_chain() -> list[str]:
    return list(resolver.KNOWN_ARTIFACT_CHAIN)


def _write_json(path: Path, value: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def _validated_artifacts(temp_root: Path) -> dict[str, str]:
    artifacts = {
        chain_key: str(temp_root / f"{chain_key}.json")
        for chain_key in _canonical_chain()
    }
    artifacts["local_relevance_orientation_index_entry"] = str(
        temp_root / "first_local_relevance_orientation_index_entry.json"
    )
    artifacts[
        "local_relevance_medium_second_local_relevance_orientation_index_entry"
    ] = str(
        temp_root
        / "second_local_relevance_medium_local_relevance_orientation_index_entry.json"
    )
    artifacts["relevance_orientation_view"] = str(
        temp_root / "first_relevance_orientation_view.json"
    )
    artifacts["local_relevance_medium_second_relevance_orientation_view"] = str(
        temp_root / "second_local_relevance_medium_relevance_orientation_view.json"
    )
    return artifacts


def _synthetic_state_packet(temp_root: Path) -> tuple[dict[str, Any], dict[str, str]]:
    artifacts = _validated_artifacts(temp_root)
    packet = {
        "state_packet_id": "local_relevance_medium_read_only_state_packet_001",
        "state_packet_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
        "state_packet_version": "0.1.0",
        "state_reader_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
        "state_reader_version": "0.1.0",
        "state_reader_scope": "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
        "known_artifact_chain": _canonical_chain(),
        "validated_standing_artifacts": artifacts,
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
        "comparison_readability_stands": True,
        "relation_readability_stands": True,
        "multiplicity_result_stands": True,
        "two_local_orientation_objects_stand": True,
        "state_reconstruction_read_only": True,
    }
    return packet, artifacts


def _synthetic_state_reader_artifact(
    temp_root: Path,
    *,
    packet_mutator: Callable[[dict[str, Any], dict[str, str]], None] | None = None,
    artifact_mutator: Callable[[dict[str, Any], dict[str, Any], dict[str, str]], None]
    | None = None,
    include_packet: bool = True,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, str]]:
    packet, artifacts = _synthetic_state_packet(temp_root)
    if packet_mutator is not None:
        packet_mutator(packet, artifacts)
    artifact: dict[str, Any] = {
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "local_relevance_medium_read_only_state_reader_metadata": {
            "result_version": result_version,
            "resolver_module": "resolve_local_relevance_medium_read_only_state_reader_v0_min",
            "failed_check_count": failed_check_count,
        },
        "local_relevance_medium_read_only_state_reader_summary": {
            "result_version": result_version,
            "failed_check_count": failed_check_count,
        },
        "local_relevance_medium_read_only_state_reader_checks": [
            {
                "check_name": "synthetic clean read-only state reader basis",
                "passed": failed_check_count == 0,
            }
        ],
    }
    if include_packet:
        artifact["local_relevance_medium_read_only_state_packet"] = packet
    if artifact_mutator is not None:
        artifact_mutator(artifact, packet, artifacts)
    return artifact, packet, artifacts


def _write_valid_state_reader_artifact(
    temp_root: Path,
    *,
    packet_mutator: Callable[[dict[str, Any], dict[str, str]], None] | None = None,
    artifact_mutator: Callable[[dict[str, Any], dict[str, Any], dict[str, str]], None]
    | None = None,
    include_packet: bool = True,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
) -> tuple[Path, dict[str, Any], dict[str, Any], dict[str, str]]:
    artifact, packet, artifacts = _synthetic_state_reader_artifact(
        temp_root,
        packet_mutator=packet_mutator,
        artifact_mutator=artifact_mutator,
        include_packet=include_packet,
        outcome=outcome,
        result_version=result_version,
        failed_check_count=failed_check_count,
    )
    path = _write_json(temp_root / "synthetic_read_only_state_reader_artifact.json", artifact)
    return path, artifact, packet, artifacts


def _build_request(artifact_path: Path | str) -> dict[str, Any]:
    return resolver.build_declared_local_relevance_medium_read_only_orientation_index_system_v0_min_request(
        selected_local_relevance_medium_read_only_state_packet_artifact=artifact_path
    )


def _orientation_index(result: Mapping[str, Any]) -> Mapping[str, Any]:
    orientation_index = result.get("local_relevance_medium_read_only_orientation_index")
    if not isinstance(orientation_index, Mapping):
        raise AssertionError("local_relevance_medium_read_only_orientation_index is not a mapping")
    return orientation_index


def _statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    statement = result.get("local_relevance_medium_read_only_orientation_index_system_statement")
    if not isinstance(statement, Mapping):
        raise AssertionError("local_relevance_medium_read_only_orientation_index_system_statement is not a mapping")
    return statement


def _summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = result.get("local_relevance_medium_read_only_orientation_index_system_summary")
    if not isinstance(summary, Mapping):
        raise AssertionError("local_relevance_medium_read_only_orientation_index_system_summary is not a mapping")
    return summary


def _checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    checks = result.get("local_relevance_medium_read_only_orientation_index_system_checks")
    if not isinstance(checks, list):
        raise AssertionError("local_relevance_medium_read_only_orientation_index_system_checks is not a list")
    return checks


def _block_code(result: Mapping[str, Any]) -> str | None:
    block = result.get("block")
    if not isinstance(block, Mapping):
        return None
    code = block.get("block_code") or block.get("code")
    return code if isinstance(code, str) else None


class LocalRelevanceMediumReadOnlyOrientationIndexSystemTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        code = _block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in _checks(result):
            for key in ("block_code", "failure_code"):
                emitted_code = check.get(key)
                if emitted_code is not None:
                    self.assertIn(emitted_code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_no_new_or_broader_behavior(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        orientation_index = _orientation_index(result)
        for key in ORIENTATION_INDEX_FALSE_FIELDS:
            if key in orientation_index:
                self.assertIs(orientation_index[key], False, key)

    def assert_orientation_index_not_wrapper_confused(
        self, result: Mapping[str, Any]
    ) -> None:
        orientation_index = _orientation_index(result)
        for key in WRAPPER_FIELDS_FORBIDDEN_IN_ORIENTATION_INDEX:
            self.assertNotIn(key, orientation_index)

    def assert_lookup_table_exact(
        self, orientation_index: Mapping[str, Any], artifacts: Mapping[str, str]
    ) -> None:
        lookup_table = orientation_index.get("lookup_table")
        self.assertIsInstance(lookup_table, Mapping)
        self.assertEqual(set(lookup_table.keys()), set(resolver.LOOKUP_ORDER))
        self.assertEqual(
            orientation_index.get("lookup_order"),
            ["first_orientation_locator", "second_orientation_locator"],
        )

        first_lookup = lookup_table["first_orientation_locator"]
        second_lookup = lookup_table["second_orientation_locator"]
        self.assertEqual(first_lookup["lookup_key"], "first_orientation_locator")
        self.assertEqual(first_lookup["received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(
            first_lookup["locator_entry_artifact"],
            artifacts["local_relevance_orientation_index_entry"],
        )
        self.assertEqual(
            first_lookup["orientation_view_artifact"],
            artifacts["relevance_orientation_view"],
        )
        self.assertEqual(second_lookup["lookup_key"], "second_orientation_locator")
        self.assertEqual(second_lookup["received_signal_id"], "bounded_relevance_signal_002")
        self.assertEqual(
            second_lookup["locator_entry_artifact"],
            artifacts[
                "local_relevance_medium_second_local_relevance_orientation_index_entry"
            ],
        )
        self.assertEqual(
            second_lookup["orientation_view_artifact"],
            artifacts["local_relevance_medium_second_relevance_orientation_view"],
        )

    def assert_not_under_forbidden_roots(self, path: Path | str) -> None:
        relative_path = _artifact_relative(path)
        for forbidden_root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(
                relative_path == forbidden_root
                or _is_relative_to(relative_path, forbidden_root),
                f"{relative_path} wrote under forbidden root {forbidden_root}",
            )

    def assert_recorded_success_shape(
        self,
        result: Mapping[str, Any],
        artifact_path: Path | str,
        artifacts: Mapping[str, str],
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        self.assertTrue(EXPECTED_TOP_LEVEL_SECTIONS.issubset(result.keys()))

        summary = _summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

        orientation_index = _orientation_index(result)
        self.assertEqual(
            orientation_index["orientation_index_id"],
            "local_relevance_medium_read_only_orientation_index_001",
        )
        self.assertEqual(
            orientation_index["orientation_index_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
        )
        self.assertEqual(orientation_index["orientation_index_version"], "0.1.0")
        self.assertEqual(
            orientation_index["orientation_index_system_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
        )
        self.assertEqual(orientation_index["orientation_index_system_version"], "0.1.0")
        self.assertEqual(
            orientation_index["orientation_index_scope"],
            "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
        )
        self.assertEqual(
            orientation_index["basis_read_only_state_packet_artifact"],
            str(artifact_path),
        )
        self.assertEqual(
            orientation_index["basis_read_only_state_reader_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED",
        )
        self.assertEqual(
            orientation_index["basis_read_only_state_reader_result_version"], "0.1.0"
        )
        self.assertEqual(
            orientation_index["basis_read_only_state_reader_failed_check_count"], 0
        )
        self.assertEqual(orientation_index["known_artifact_chain"], _canonical_chain())
        self.assertEqual(
            orientation_index["first_orientation_locator_entry_artifact"],
            artifacts["local_relevance_orientation_index_entry"],
        )
        self.assertEqual(
            orientation_index["second_orientation_locator_entry_artifact"],
            artifacts[
                "local_relevance_medium_second_local_relevance_orientation_index_entry"
            ],
        )
        self.assertEqual(
            orientation_index["first_orientation_view_artifact"],
            artifacts["relevance_orientation_view"],
        )
        self.assertEqual(
            orientation_index["second_orientation_view_artifact"],
            artifacts["local_relevance_medium_second_relevance_orientation_view"],
        )
        self.assertEqual(
            orientation_index["first_received_signal_id"],
            "bounded_relevance_signal_001",
        )
        self.assertEqual(
            orientation_index["second_received_signal_id"],
            "bounded_relevance_signal_002",
        )
        self.assertNotEqual(
            orientation_index["first_received_signal_id"],
            orientation_index["second_received_signal_id"],
        )
        self.assertEqual(
            orientation_index["first_relevance_basis_id"],
            "bounded_relevance_basis_001",
        )
        self.assertEqual(
            orientation_index["second_relevance_basis_id"],
            "bounded_relevance_basis_002",
        )
        self.assertEqual(
            orientation_index["first_relevance_scope_id"],
            "bounded_relevance_scope_001",
        )
        self.assertEqual(
            orientation_index["second_relevance_scope_id"],
            "bounded_relevance_scope_002",
        )
        self.assertEqual(
            orientation_index["first_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_001",
        )
        self.assertEqual(
            orientation_index["second_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_002",
        )
        self.assertEqual(
            orientation_index["first_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        self.assertEqual(
            orientation_index["second_reception_envelope_id"],
            "bounded_relevance_reception_envelope_002",
        )
        self.assertEqual(orientation_index["multiplicity_count"], 2)
        self.assertEqual(orientation_index["relation_pair_count"], 1)
        self.assertEqual(orientation_index["comparison_pair_count"], 1)
        self.assertIs(orientation_index["comparison_readability_stands"], True)
        self.assertIs(orientation_index["relation_readability_stands"], True)
        self.assertIs(orientation_index["multiplicity_result_stands"], True)
        self.assertIs(orientation_index["two_local_orientation_objects_stand"], True)
        self.assert_lookup_table_exact(orientation_index, artifacts)
        self.assertEqual(orientation_index["lookup_key_count"], 2)
        self.assertEqual(orientation_index["lookup_target_count"], 2)
        self.assertEqual(orientation_index["accepted_new_entries_count"], 0)
        self.assertIs(orientation_index["deterministic_local_lookup_enabled"], True)
        self.assertIs(orientation_index["read_only_orientation_index_recorded"], True)
        self.assertIs(
            orientation_index["read_only_orientation_index_system_recorded"], True
        )
        for key in ORIENTATION_INDEX_FALSE_FIELDS:
            self.assertIs(orientation_index[key], False, key)

        self.assert_orientation_index_not_wrapper_confused(result)
        statement = _statement(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        self.assert_non_claims_canonical_false(result)

    def assert_blocked_result(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        block_code = _block_code(result)
        self.assertIsNotNone(block_code)
        self.assertIn(block_code, resolver.BLOCK_CODES)
        self.assertGreater(_summary(result)["failed_check_count"], 0)
        self.assert_public_block_codes(result)
        self.assert_no_new_or_broader_behavior(result)

    def resolve_with_synthetic_basis(
        self,
        *,
        packet_mutator: Callable[[dict[str, Any], dict[str, str]], None] | None = None,
        artifact_mutator: Callable[
            [dict[str, Any], dict[str, Any], dict[str, str]], None
        ]
        | None = None,
        request_mutator: Callable[
            [dict[str, Any], Path, dict[str, Any], dict[str, Any], dict[str, str], Path],
            None,
        ]
        | None = None,
        include_packet: bool = True,
        outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED",
        result_version: str = "0.1.0",
        failed_check_count: int = 0,
        request_override: Any = None,
        use_request_override: bool = False,
    ) -> Mapping[str, Any]:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, artifact, packet, artifacts = _write_valid_state_reader_artifact(
                temp_root,
                packet_mutator=packet_mutator,
                artifact_mutator=artifact_mutator,
                include_packet=include_packet,
                outcome=outcome,
                result_version=result_version,
                failed_check_count=failed_check_count,
            )
            if use_request_override:
                return resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                    request_override
                )
            request = _build_request(artifact_path)
            if request_mutator is not None:
                request_mutator(request, artifact_path, artifact, packet, artifacts, temp_root)
            return resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                request
            )

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_orientation_index_system_v0_min",
            "resolve_local_relevance_medium_read_only_orientation_index_system_v0_min_from_path",
            "write_local_relevance_medium_read_only_orientation_index_system_v0_min_result",
            "build_local_relevance_medium_read_only_orientation_index_system_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_orientation_index_system_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_ORIENTATION_INDEX_TYPE_VALUES",
            "SUPPORTED_ORIENTATION_INDEX_SYSTEM_TYPE_VALUES",
            "SUPPORTED_ORIENTATION_INDEX_SCOPE_VALUES",
            "LOOKUP_ORDER",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_orientation_index_system_v0_min",
        )
        self.assertTrue(Path(resolver.OUTPUT_ROOT).as_posix().endswith(EXPECTED_OUTPUT_ROOT.as_posix()))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
            resolver.SUPPORTED_ORIENTATION_INDEX_TYPE_VALUES,
        )
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
            resolver.SUPPORTED_ORIENTATION_INDEX_SYSTEM_TYPE_VALUES,
        )
        self.assertIn(
            "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
            resolver.SUPPORTED_ORIENTATION_INDEX_SCOPE_VALUES,
        )
        self.assertEqual(
            resolver.LOOKUP_ORDER,
            ["first_orientation_locator", "second_orientation_locator"],
        )
        self.assert_not_under_forbidden_roots(resolver.OUTPUT_ROOT)

    def test_successful_recorded_result_from_synthetic_state_packet_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _packet, artifacts = _write_valid_state_reader_artifact(
                temp_root
            )
            request = _build_request(artifact_path)
            result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                request
            )
            self.assert_recorded_success_shape(result, artifact_path, artifacts)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_STATE_READER_ARTIFACT.exists():
            self.skipTest("default local relevance medium read-only state reader artifact is absent")

        request = resolver.build_declared_local_relevance_medium_read_only_orientation_index_system_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        summary = _summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        orientation_index = _orientation_index(result)
        self.assertEqual(
            orientation_index["orientation_index_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
        )
        self.assertEqual(
            orientation_index["orientation_index_system_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
        )
        self.assertEqual(
            orientation_index["orientation_index_scope"],
            "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
        )
        self.assertEqual(orientation_index["known_artifact_chain"], _canonical_chain())
        self.assertTrue(orientation_index["first_orientation_locator_entry_artifact"])
        self.assertTrue(orientation_index["second_orientation_locator_entry_artifact"])
        self.assertTrue(orientation_index["first_orientation_view_artifact"])
        self.assertTrue(orientation_index["second_orientation_view_artifact"])
        self.assertEqual(
            orientation_index["first_received_signal_id"],
            "bounded_relevance_signal_001",
        )
        self.assertEqual(
            orientation_index["second_received_signal_id"],
            "bounded_relevance_signal_002",
        )
        self.assertNotEqual(
            orientation_index["first_received_signal_id"],
            orientation_index["second_received_signal_id"],
        )
        self.assertEqual(orientation_index["multiplicity_count"], 2)
        self.assertEqual(orientation_index["relation_pair_count"], 1)
        self.assertEqual(orientation_index["comparison_pair_count"], 1)
        self.assertIs(orientation_index["comparison_readability_stands"], True)
        self.assertIs(orientation_index["relation_readability_stands"], True)
        self.assertIs(orientation_index["multiplicity_result_stands"], True)
        self.assertIs(orientation_index["two_local_orientation_objects_stand"], True)
        self.assertEqual(set(orientation_index["lookup_table"].keys()), set(resolver.LOOKUP_ORDER))
        self.assertEqual(orientation_index["lookup_order"], resolver.LOOKUP_ORDER)
        self.assertEqual(orientation_index["lookup_key_count"], 2)
        self.assertEqual(orientation_index["lookup_target_count"], 2)
        self.assertEqual(orientation_index["accepted_new_entries_count"], 0)
        self.assertIs(orientation_index["deterministic_local_lookup_enabled"], True)
        for key in ORIENTATION_INDEX_FALSE_FIELDS:
            self.assertIs(orientation_index[key], False, key)

    def test_result_level_non_claims_canonicalize_illegal_true_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _packet, _artifacts = _write_valid_state_reader_artifact(
                temp_root
            )
            clean_request = _build_request(artifact_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                        request
                    )
                    self.assert_blocked_result(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertNotEqual(result["non_claims"][key], True)

    def test_representative_blocking_behavior(self) -> None:
        def request_set(key: str, value: Any) -> Callable[..., None]:
            def mutate(
                request: dict[str, Any],
                _artifact_path: Path,
                _artifact: dict[str, Any],
                _packet: dict[str, Any],
                _artifacts: dict[str, str],
                _temp_root: Path,
            ) -> None:
                request[key] = value

            return mutate

        def request_pop(key: str) -> Callable[..., None]:
            def mutate(
                request: dict[str, Any],
                _artifact_path: Path,
                _artifact: dict[str, Any],
                _packet: dict[str, Any],
                _artifacts: dict[str, str],
                _temp_root: Path,
            ) -> None:
                request.pop(key, None)

            return mutate

        def request_path_missing(
            request: dict[str, Any],
            _artifact_path: Path,
            _artifact: dict[str, Any],
            _packet: dict[str, Any],
            _artifacts: dict[str, str],
            temp_root: Path,
        ) -> None:
            request["selected_local_relevance_medium_read_only_state_packet_artifact"] = str(
                temp_root / "missing_artifact.json"
            )

        def request_json_array(
            request: dict[str, Any],
            _artifact_path: Path,
            _artifact: dict[str, Any],
            _packet: dict[str, Any],
            _artifacts: dict[str, str],
            temp_root: Path,
        ) -> None:
            array_path = _write_json(temp_root / "array_request_basis.json", [])
            request["selected_local_relevance_medium_read_only_state_packet_artifact"] = str(array_path)

        def remove_artifact_key(chain_key: str) -> Callable[[dict[str, Any], dict[str, str]], None]:
            def mutate(packet: dict[str, Any], _artifacts: dict[str, str]) -> None:
                packet["validated_standing_artifacts"].pop(chain_key, None)

            return mutate

        def packet_set(key: str, value: Any) -> Callable[[dict[str, Any], dict[str, str]], None]:
            def mutate(packet: dict[str, Any], _artifacts: dict[str, str]) -> None:
                packet[key] = value

            return mutate

        def packet_pop(key: str) -> Callable[[dict[str, Any], dict[str, str]], None]:
            def mutate(packet: dict[str, Any], _artifacts: dict[str, str]) -> None:
                packet.pop(key, None)

            return mutate

        shortcut_flags = [
            "lookup_table_not_two_entries",
            "new_signal_accepted",
            "new_relevance_object_created",
            "new_index_entry_created",
            "filesystem_discovery_performed",
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
            "artifact_existence_treated_as_read_only_orientation_index_authority",
            "latest_file_posture_treated_as_read_only_orientation_index_authority",
            "repo_local_availability_treated_as_read_only_orientation_index_authority",
            "hidden_repo_state_used_as_read_only_orientation_index_content",
            "hidden_repo_state_used_as_read_only_orientation_index_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ]

        cases: list[tuple[str, dict[str, Any]]] = [
            (
                "explicit block intent",
                {
                    "request_mutator": request_set(
                        "local_relevance_medium_read_only_orientation_index_system_intent",
                        "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
                    )
                },
            ),
            ("missing request mapping fields", {"request_override": {}, "use_request_override": True}),
            ("non-mapping request", {"request_override": ["not", "mapping"], "use_request_override": True}),
            (
                "unsupported intent",
                {
                    "request_mutator": request_set(
                        "local_relevance_medium_read_only_orientation_index_system_intent",
                        "UNSUPPORTED_INTENT",
                    )
                },
            ),
            (
                "selected read-only state packet artifact path missing",
                {
                    "request_mutator": request_pop(
                        "selected_local_relevance_medium_read_only_state_packet_artifact"
                    )
                },
            ),
            ("selected read-only state packet artifact unreadable", {"request_mutator": request_path_missing}),
            ("selected read-only state packet artifact JSON array", {"request_mutator": request_json_array}),
            (
                "selected read-only state reader artifact not recorded",
                {"outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_NOT_RECORDED"},
            ),
            (
                "selected read-only state reader artifact failed checks present",
                {"failed_check_count": 1},
            ),
            (
                "selected read-only state reader artifact version not 0.1.0",
                {"result_version": "9.9.9"},
            ),
            (
                "local relevance medium read-only state packet object missing",
                {"include_packet": False},
            ),
            (
                "state packet type not local relevance medium read-only state packet",
                {"packet_mutator": packet_set("state_packet_type", "WRONG_STATE_PACKET")},
            ),
            (
                "state reader type not local relevance medium read-only state reader",
                {"packet_mutator": packet_set("state_reader_type", "WRONG_STATE_READER")},
            ),
            (
                "state reader scope not read existing local relevance medium state only",
                {"packet_mutator": packet_set("state_reader_scope", "WRITEABLE_SCOPE")},
            ),
            (
                "known artifact chain not canonical",
                {"packet_mutator": packet_set("known_artifact_chain", list(reversed(_canonical_chain())))},
            ),
            (
                "first orientation locator artifact missing",
                {"packet_mutator": remove_artifact_key("local_relevance_orientation_index_entry")},
            ),
            (
                "second orientation locator artifact missing",
                {
                    "packet_mutator": remove_artifact_key(
                        "local_relevance_medium_second_local_relevance_orientation_index_entry"
                    )
                },
            ),
            (
                "first orientation view artifact missing",
                {"packet_mutator": remove_artifact_key("relevance_orientation_view")},
            ),
            (
                "second orientation view artifact missing",
                {
                    "packet_mutator": remove_artifact_key(
                        "local_relevance_medium_second_relevance_orientation_view"
                    )
                },
            ),
            (
                "first received signal id missing",
                {"packet_mutator": packet_pop("first_received_signal_id")},
            ),
            (
                "second received signal id missing",
                {"packet_mutator": packet_pop("second_received_signal_id")},
            ),
            (
                "first and second received signal ids not distinct",
                {"packet_mutator": packet_set("second_received_signal_id", "bounded_relevance_signal_001")},
            ),
            (
                "first relevance basis id missing",
                {"packet_mutator": packet_pop("first_relevance_basis_id")},
            ),
            (
                "second relevance basis id missing",
                {"packet_mutator": packet_pop("second_relevance_basis_id")},
            ),
            (
                "first relevance scope id missing",
                {"packet_mutator": packet_pop("first_relevance_scope_id")},
            ),
            (
                "second relevance scope id missing",
                {"packet_mutator": packet_pop("second_relevance_scope_id")},
            ),
            (
                "first carrier context id missing",
                {"packet_mutator": packet_pop("first_carrier_context_id")},
            ),
            (
                "second carrier context id missing",
                {"packet_mutator": packet_pop("second_carrier_context_id")},
            ),
            (
                "first reception envelope id missing",
                {"packet_mutator": packet_pop("first_reception_envelope_id")},
            ),
            (
                "second reception envelope id missing",
                {"packet_mutator": packet_pop("second_reception_envelope_id")},
            ),
            ("multiplicity count not two", {"packet_mutator": packet_set("multiplicity_count", 3)}),
            ("relation pair count not one", {"packet_mutator": packet_set("relation_pair_count", 2)}),
            ("comparison pair count not one", {"packet_mutator": packet_set("comparison_pair_count", 2)}),
            (
                "comparison readability does not stand",
                {"packet_mutator": packet_set("comparison_readability_stands", False)},
            ),
            (
                "relation readability does not stand",
                {"packet_mutator": packet_set("relation_readability_stands", False)},
            ),
            (
                "multiplicity result does not stand",
                {"packet_mutator": packet_set("multiplicity_result_stands", False)},
            ),
            (
                "two local orientation objects do not stand",
                {"packet_mutator": packet_set("two_local_orientation_objects_stand", False)},
            ),
            ("orientation index type missing", {"request_mutator": request_pop("orientation_index_type")}),
            (
                "orientation index type unsupported",
                {"request_mutator": request_set("orientation_index_type", "LOCAL_RELEVANCE_INDEX")},
            ),
            (
                "orientation index system type missing",
                {"request_mutator": request_pop("orientation_index_system_type")},
            ),
            (
                "orientation index system type unsupported",
                {"request_mutator": request_set("orientation_index_system_type", "REGISTRY")},
            ),
            ("orientation index scope missing", {"request_mutator": request_pop("orientation_index_scope")}),
            (
                "orientation index scope unsupported",
                {"request_mutator": request_set("orientation_index_scope", "SEARCH_SCOPE")},
            ),
            (
                "lookup order not deterministic",
                {"request_mutator": request_set("lookup_order", ["second_orientation_locator", "first_orientation_locator"])},
            ),
            ("lookup key count not two", {"request_mutator": request_set("lookup_key_count", 1)}),
            ("lookup target count not two", {"request_mutator": request_set("lookup_target_count", 1)}),
            (
                "accepted new entries count not zero",
                {"request_mutator": request_set("accepted_new_entries_count", 1)},
            ),
            (
                "deterministic local lookup not enabled",
                {"request_mutator": request_set("deterministic_local_lookup_enabled", False)},
            ),
            (
                "required non-claim missing",
                {
                    "request_mutator": lambda request, *_args: request[
                        "declared_non_claims"
                    ].pop("new_signal_accepted", None)
                },
            ),
        ]
        cases.extend(
            (f"{flag} asserted", {"request_mutator": request_set(flag, True)})
            for flag in shortcut_flags
        )

        for name, kwargs in cases:
            with self.subTest(name=name):
                result = self.resolve_with_synthetic_basis(**kwargs)
                self.assert_blocked_result(result)

    def test_missing_or_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _packet, _artifacts = _write_valid_state_reader_artifact(
                temp_root
            )
            required_key = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            variants: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
                ("remove declared_non_claims", lambda request: request.pop("declared_non_claims", None)),
                ("declared_non_claims empty", lambda request: request.__setitem__("declared_non_claims", {})),
                (
                    "remove one required non-claim",
                    lambda request: request["declared_non_claims"].pop(required_key, None),
                ),
                (
                    "one required non-claim string",
                    lambda request: request["declared_non_claims"].__setitem__(required_key, "false"),
                ),
                (
                    "one required non-claim none",
                    lambda request: request["declared_non_claims"].__setitem__(required_key, None),
                ),
            ]
            for name, mutate in variants:
                with self.subTest(name=name):
                    request = _build_request(artifact_path)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                        request
                    )
                    self.assertIn(
                        result["outcome"],
                        (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                    )
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _packet, artifacts = _write_valid_state_reader_artifact(
                temp_root
            )
            result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                _build_request(artifact_path)
            )
            self.assert_recorded_success_shape(result, artifact_path, artifacts)
            orientation_index = _orientation_index(result)
            self.assertEqual(
                orientation_index["orientation_index_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
            )
            self.assertEqual(
                orientation_index["orientation_index_system_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
            )
            self.assertEqual(
                orientation_index["orientation_index_scope"],
                "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            for outcome in (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_BLOCKED",
            ):
                self.assertIn(outcome, resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX", serialized)
            self.assertIn(
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
                serialized,
            )
            self.assertIn(
                "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
                serialized,
            )
            self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        sentinel = HOSTILE_SENTINELS[0]

        def artifact_mutator(
            artifact: dict[str, Any],
            packet: dict[str, Any],
            _artifacts: dict[str, str],
        ) -> None:
            artifact["raw_full_body"] = sentinel
            artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            packet["raw_state_packet_body"] = HOSTILE_SENTINELS[5]
            packet["orientation_index_system_body"] = HOSTILE_SENTINELS[2]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _packet, _artifacts = _write_valid_state_reader_artifact(
                temp_root,
                artifact_mutator=artifact_mutator,
            )
            request = _build_request(artifact_path)
            request["raw_full_body"] = HOSTILE_SENTINELS[27]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request["extra_sections"] = {"orientation_index_body": HOSTILE_SENTINELS[1]}
            request_before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            for hostile in HOSTILE_SENTINELS:
                self.assertNotIn(hostile, serialized)
            self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX", serialized)
            self.assertIn(
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
                serialized,
            )
            self.assert_non_claims_canonical_false(result)
            self.assert_no_new_or_broader_behavior(result)
            self.assertEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _packet, _artifacts = _write_valid_state_reader_artifact(
                temp_root
            )
            request_path = _write_json(temp_root / "request.json", _build_request(artifact_path))
            result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(_summary(result)["result_version"], "0.1.0")
            self.assertEqual(_summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_result(malformed_result)

            array_request_path = _write_json(temp_root / "array_request.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min_from_path(
                array_request_path
            )
            self.assert_blocked_result(array_result)

            missing_request_result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min_from_path(
                temp_root / "missing_request.json"
            )
            self.assert_blocked_result(missing_request_result)

            patched_output_root = temp_root / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_output_root):
                first_output = resolver.write_local_relevance_medium_read_only_orientation_index_system_v0_min_result(
                    result
                )
                second_output = resolver.write_local_relevance_medium_read_only_orientation_index_system_v0_min_result(
                    result
                )
            self.assertTrue(first_output.parent.exists())
            self.assertTrue(first_output.exists())
            self.assertTrue(second_output.exists())
            self.assertNotEqual(first_output, second_output)
            with first_output.open("r", encoding="utf-8") as handle:
                self.assertIsInstance(json.load(handle), dict)
            self.assertIn(
                "local_relevance_medium_read_only_orientation_index_system_v0_min",
                first_output.as_posix(),
            )
            self.assert_not_under_forbidden_roots(first_output)
            self.assert_not_under_forbidden_roots(second_output)

    def test_non_mutation_of_inputs_and_postures(self) -> None:
        sentinel = HOSTILE_SENTINELS[0]
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact, packet, _artifacts = _synthetic_state_reader_artifact(temp_root)
            artifact["raw_full_body"] = sentinel
            packet["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            artifact_before = copy.deepcopy(artifact)
            artifact_path = _write_json(
                temp_root / "synthetic_read_only_state_reader_artifact.json",
                artifact,
            )
            request = _build_request(artifact_path)
            request["raw_full_body"] = HOSTILE_SENTINELS[1]
            request["nested_raw"] = {"hidden_repo_state": HOSTILE_SENTINELS[-1]}
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])
            selected_path_before = request[
                "selected_local_relevance_medium_read_only_state_packet_artifact"
            ]
            result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assertEqual(request, request_before)
            self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
            self.assertEqual(
                request["selected_local_relevance_medium_read_only_state_packet_artifact"],
                selected_path_before,
            )
            self.assertEqual(request["orientation_index_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX")
            self.assertEqual(request["orientation_index_system_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM")
            self.assertEqual(request["orientation_index_scope"], "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY")
            self.assertEqual(request["lookup_order"], resolver.LOOKUP_ORDER)
            self.assertEqual(artifact, artifact_before)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _packet, _artifacts = _write_valid_state_reader_artifact(
                temp_root
            )
            request = _build_request(artifact_path)
            result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                request
            )
            summary = resolver.build_local_relevance_medium_read_only_orientation_index_system_v0_min_summary(
                result
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
            self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
            self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
            self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
            self.assertIs(result["non_claims"]["authorization_token_reused"], False)

            for key in (
                "predecessor_failure_hidden",
                "predecessor_failure_repaired",
                "predecessor_failure_claimed_passed",
                "consumed_request_reopened",
                "authorization_token_reused",
            ):
                with self.subTest(key=key):
                    blocked_request = copy.deepcopy(request)
                    blocked_request[key] = True
                    blocked_result = resolver.resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
                        blocked_request
                    )
                    self.assert_blocked_result(blocked_result)


if __name__ == "__main__":
    unittest.main()
