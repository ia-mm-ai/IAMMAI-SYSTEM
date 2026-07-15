"""Tests for the v2 derivative participant participation-motion boundary.

The target resolver records one boundary object only. It preserves the v1
participation-motion-boundary resolver as predecessor evidence, verifies the
standing role-admission and continuation basis, and keeps participation motion,
output, action, re-entry, reception, vessel, runtime, interface, source,
authority, currentness, truth, and follow-on surfaces uncreated.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2 as resolver  # noqa: E402


BOUNDARY_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY"
)
BOUNDARY_SCOPE = "SELECTED_PARTICIPATION_MOTION_CONSIDERATION_ONLY"
ROLE_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_RECORDED"
)
CONTINUATION_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_RECORDED"
ROLE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION"
ROLE_SCOPE = "SELECTED_ROLE_ADMISSION_ONLY"
CONTINUATION_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION"
CONTINUATION_SCOPE = "SELECTED_CONTINUATION_ONLY"
SELECTED_COMMAND = "state"

REQ_FALSE = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
PUBLIC_CODES = set(resolver.BLOCK_CODES)
FIELD_CODES = getattr(
    resolver,
    "FALSE_FIELD_BLOCK_CODES",
    {key: key.upper() for key in REQ_FALSE},
)

EXPECTED_WRAPPER_SECTIONS = {
    "result_version",
    "resolver_module",
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_metadata",
    "declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_question",
    "selected_role_admission_terminal_summary_basis",
    "selected_role_admission_artifact_basis",
    "selected_continuation_terminal_summary_basis",
    "selected_continuation_artifact_basis",
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary",
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_checks",
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_statement",
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_summary",
}

FORBIDDEN_WRAPPER_FIELDS_IN_BOUNDARY = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_summary",
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_metadata",
}

ROLE_POSITIVE_FIELDS = (
    "local_relevance_medium_read_only_derivative_participant_role_admission_recorded",
    "derivative_participant_role_admission_created",
    "bounded_derivative_participant_role_admitted",
    "role_admission_local_only",
    "role_admission_read_only",
    "role_admission_selected_state_only",
    "role_admission_basis_reference_only",
    "role_admission_inside_continuation_body",
    "role_admission_from_continuation_only",
)

CONTINUATION_POSITIVE_FIELDS = (
    "selected_continuation_recorded",
    "continuation_created",
    "continuation_local_only",
    "continuation_read_only",
    "continuation_basis_reference_only",
    "continuation_selected_state_only",
    "continuation_from_second_operation",
    "continuation_sequence_count_is_2",
)

BOUNDARY_POSITIVE_FIELDS = (
    "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_recorded",
    "future_participation_motion_may_be_considered",
    "participation_motion_boundary_created",
    "participation_motion_boundary_local_only",
    "participation_motion_boundary_read_only",
    "participation_motion_boundary_selected_state_only",
    "participation_motion_boundary_basis_reference_only",
)

EVIDENCE_FIELDS = (
    "continuation_v1_failure_evidence_preserved",
    "role_admission_v1_failure_evidence_preserved",
    "predecessor_failure_evidence_preserved",
)

BOUNDARY_ONLY_FALSE_FIELDS = (
    "participation_motion_created",
    "participant_output_authorized",
    "action_authorization_created",
    "participant_reentry_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "third_operation_created",
    "unbounded_operation_sequence_created",
    "reusable_operation_permission_created",
    "general_operation_permission_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
    "unsupported_lookup_keys_permitted",
    "new_lookup_entry_created",
    "new_signal_accepted",
    "new_entry_accepted",
    "new_relevance_object_created",
    "new_index_entry_created",
    "filesystem_discovery_performed",
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "registry_created",
    "search_surface_created",
    "query_surface_created",
    "ranking_surface_created",
    "scoring_surface_created",
    "priority_surface_created",
    "validity_judgment_created",
    "truth_judgment_created",
    "authority_judgment_created",
    "currentness_judgment_created",
    "received_derivative_participation_authority_imported",
    "received_derivative_action_authority_imported",
    "bounded_derivative_vessel_authority_imported",
    "derivative_vessel_relation_authority_imported",
    "role_admission_treated_as_participation_permission",
    "artifact_existence_treated_as_participation_motion_authority",
    "latest_file_posture_treated_as_participation_motion_authority",
    "repo_local_availability_treated_as_participation_motion_authority",
    "hidden_repo_state_used_as_participation_motion_content",
    "hidden_repo_state_used_as_participation_motion_authority",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "synchronization_created",
    "deployment_created",
    "public_release_created",
    "broader_reusable_permission_created",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "continuation_v1_failure_repaired",
    "continuation_v1_failure_hidden",
    "continuation_v1_failure_claimed_passed",
    "role_admission_v1_failure_repaired",
    "role_admission_v1_failure_hidden",
    "role_admission_v1_failure_claimed_passed",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

CORE_BOUNDARY_FALSE_FIELDS = (
    "participation_motion_created",
    "participant_output_authorized",
    "action_authorization_created",
    "participant_reentry_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "synchronization_created",
    "follow_on_work_authorized",
)

HOSTILE_SENTINELS = (
    "RAW_PARTICIPATION_MOTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPATION_MOTION_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_OUTPUT_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_AUTHORIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_DERIVATIVE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_VESSEL_RELATION_BODY_MUST_NOT_RETURN",
    "RAW_ROLE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "PRESERVED_DERIVATIVE_ANCESTOR_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _json_round_trip(value: Any) -> Any:
    return json.loads(json.dumps(value))


class LocalRelevanceMediumReadOnlyDerivativeParticipantParticipationMotionBoundaryV0MinV2Tests(
    unittest.TestCase
):
    def write_json(self, path: Path, value: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def false_non_claims(self) -> dict[str, bool]:
        return {key: False for key in REQ_FALSE}

    def clean_role_artifact(
        self,
        *,
        object_overrides: Mapping[str, Any] | None = None,
        object_omits: tuple[str, ...] = (),
        statement_overrides: Mapping[str, Any] | None = None,
        summary_overrides: Mapping[str, Any] | None = None,
        non_meaning_overrides: Mapping[str, Any] | None = None,
        top_level_non_claim_overrides: Mapping[str, Any] | None = None,
        failed_check_count: int = 0,
        outcome: str = ROLE_OUTCOME,
        result_version: str = "0.1.0",
        extra_sections: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        non_claims = self.false_non_claims()
        role_object = {
            "role_admission_id": "local_relevance_medium_read_only_derivative_participant_role_admission_001",
            "role_admission_type": ROLE_TYPE,
            "role_admission_version": result_version,
            "role_admission_scope": ROLE_SCOPE,
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "selected_command_preserved": True,
            "selected_continuation_recorded": True,
            "continuation_created": True,
            "continuation_local_only": True,
            "continuation_read_only": True,
            "continuation_basis_reference_only": True,
            "continuation_selected_state_only": True,
            "continuation_from_second_operation": True,
            "continuation_operation_sequence_count": 2,
            "continuation_sequence_count_is_2": True,
            "local_relevance_medium_read_only_derivative_participant_role_admission_recorded": True,
            "role_admission_recorded": True,
            "derivative_participant_role_admission_created": True,
            "bounded_derivative_participant_role_admitted": True,
            "role_admission_local_only": True,
            "role_admission_read_only": True,
            "role_admission_selected_state_only": True,
            "role_admission_basis_reference_only": True,
            "role_admission_inside_continuation_body": True,
            "role_admission_from_continuation_only": True,
            "continuation_v1_failure_evidence_preserved": True,
            "role_admission_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        role_object.update(non_claims)
        if object_overrides:
            role_object.update(copy.deepcopy(dict(object_overrides)))
        for key in object_omits:
            role_object.pop(key, None)

        statement = dict(role_object)
        statement.update({key: False for key in REQ_FALSE})
        if statement_overrides:
            statement.update(copy.deepcopy(dict(statement_overrides)))

        summary = {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "passed_check_count": 251,
            **{key: True for key in ROLE_POSITIVE_FIELDS},
            **{key: True for key in CONTINUATION_POSITIVE_FIELDS},
            "role_admission_v1_failure_evidence_preserved": True,
            "continuation_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        if summary_overrides:
            summary.update(copy.deepcopy(dict(summary_overrides)))

        non_meaning = {
            "this_is_role_admission_only": True,
            "role_admission_v1_failure_evidence_preserved": True,
            "continuation_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
        }
        if non_meaning_overrides:
            non_meaning.update(copy.deepcopy(dict(non_meaning_overrides)))

        top_non_claims = dict(non_claims)
        if top_level_non_claim_overrides:
            top_non_claims.update(copy.deepcopy(dict(top_level_non_claim_overrides)))

        artifact = {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "local_relevance_medium_read_only_derivative_participant_role_admission": role_object,
            "local_relevance_medium_read_only_derivative_participant_role_admission_statement": statement,
            "local_relevance_medium_read_only_derivative_participant_role_admission_summary": summary,
            "local_relevance_medium_read_only_derivative_participant_role_admission_non_meaning": non_meaning,
            "local_relevance_medium_read_only_derivative_participant_role_admission_checks": [],
            "local_relevance_medium_read_only_derivative_participant_role_admission_metadata": {
                "local_relevance_medium_read_only_derivative_participant_role_admission_version": result_version,
                "resolver_module": "synthetic_role_admission_basis",
            },
            "non_claims": top_non_claims,
        }
        if extra_sections:
            artifact.update(copy.deepcopy(dict(extra_sections)))
        return artifact

    def clean_continuation_artifact(
        self,
        *,
        object_overrides: Mapping[str, Any] | None = None,
        object_omits: tuple[str, ...] = (),
        statement_overrides: Mapping[str, Any] | None = None,
        summary_overrides: Mapping[str, Any] | None = None,
        non_meaning_overrides: Mapping[str, Any] | None = None,
        top_level_non_claim_overrides: Mapping[str, Any] | None = None,
        failed_check_count: int = 0,
        outcome: str = CONTINUATION_OUTCOME,
        result_version: str = "0.1.0",
        extra_sections: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        non_claims = self.false_non_claims()
        continuation_object = {
            "continuation_id": "local_relevance_medium_read_only_continuation_001",
            "continuation_type": CONTINUATION_TYPE,
            "continuation_version": result_version,
            "continuation_scope": CONTINUATION_SCOPE,
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "selected_command_preserved": True,
            "selected_continuation_recorded": True,
            "local_relevance_medium_read_only_continuation_recorded": True,
            "continuation_created": True,
            "continuation_local_only": True,
            "continuation_read_only": True,
            "continuation_basis_reference_only": True,
            "continuation_selected_state_only": True,
            "continuation_from_second_operation": True,
            "continuation_operation_sequence_count": 2,
            "continuation_sequence_count_is_2": True,
            "participation_authorized": False,
            "participant_role_created": False,
            "continuation_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        continuation_object.update(non_claims)
        if object_overrides:
            continuation_object.update(copy.deepcopy(dict(object_overrides)))
        for key in object_omits:
            continuation_object.pop(key, None)

        statement = dict(continuation_object)
        statement.update({key: False for key in REQ_FALSE})
        if statement_overrides:
            statement.update(copy.deepcopy(dict(statement_overrides)))

        summary = {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "passed_check_count": 1371,
            **{key: True for key in CONTINUATION_POSITIVE_FIELDS},
            "continuation_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        if summary_overrides:
            summary.update(copy.deepcopy(dict(summary_overrides)))

        non_meaning = {
            "this_is_continuation_only": True,
            "continuation_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
        }
        if non_meaning_overrides:
            non_meaning.update(copy.deepcopy(dict(non_meaning_overrides)))

        top_non_claims = dict(non_claims)
        if top_level_non_claim_overrides:
            top_non_claims.update(copy.deepcopy(dict(top_level_non_claim_overrides)))

        artifact = {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "local_relevance_medium_read_only_continuation": continuation_object,
            "local_relevance_medium_read_only_continuation_statement": statement,
            "local_relevance_medium_read_only_continuation_summary": summary,
            "local_relevance_medium_read_only_continuation_non_meaning": non_meaning,
            "local_relevance_medium_read_only_continuation_checks": [],
            "local_relevance_medium_read_only_continuation_metadata": {
                "local_relevance_medium_read_only_continuation_version": result_version,
                "resolver_module": "synthetic_continuation_basis",
            },
            "non_claims": top_non_claims,
        }
        if extra_sections:
            artifact.update(copy.deepcopy(dict(extra_sections)))
        return artifact

    def request_for_paths(
        self,
        role_path: Path | str,
        continuation_path: Path | str,
        **overrides: Any,
    ) -> dict[str, Any]:
        request = (
            resolver.build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_request(
                selected_role_admission_artifact=role_path,
                selected_continuation_artifact=continuation_path,
                selected_command=SELECTED_COMMAND,
                boundary_type=BOUNDARY_TYPE,
                boundary_scope=BOUNDARY_SCOPE,
            )
        )
        request.update(copy.deepcopy(overrides))
        return request

    def result_from_artifacts(
        self,
        tmp_path: Path,
        role_artifact: Mapping[str, Any] | None = None,
        continuation_artifact: Mapping[str, Any] | None = None,
        **request_overrides: Any,
    ) -> tuple[dict[str, Any], dict[str, Any], Path, Path]:
        role_value = self.clean_role_artifact() if role_artifact is None else copy.deepcopy(dict(role_artifact))
        continuation_value = (
            self.clean_continuation_artifact()
            if continuation_artifact is None
            else copy.deepcopy(dict(continuation_artifact))
        )
        role_path = self.write_json(tmp_path / "role_admission.json", role_value)
        continuation_path = self.write_json(tmp_path / "continuation.json", continuation_value)
        request = self.request_for_paths(role_path, continuation_path, **request_overrides)
        result = resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2(
            request
        )
        return result, request, role_path, continuation_path

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result[
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary"
        ]
        self.assertIsInstance(boundary, Mapping)
        return boundary

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result[
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_statement"
        ]
        self.assertIsInstance(statement, Mapping)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result[
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_summary"
        ]
        self.assertIsInstance(summary, Mapping)
        return summary

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result[
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_checks"
        ]
        self.assertIsInstance(checks, list)
        return checks

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, Mapping)
        return non_claims

    def block_code(self, result: Mapping[str, Any]) -> Any:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def emitted_codes(self, result: Mapping[str, Any]) -> list[str]:
        codes: list[str] = []
        code = self.block_code(result)
        if isinstance(code, str):
            codes.append(code)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if isinstance(value, str):
                    codes.append(value)
        return codes

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        for code in self.emitted_codes(result):
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = self.non_claims(result)
        for key in REQ_FALSE:
            self.assertIn(key, non_claims)
            self.assertIs(type(non_claims[key]), bool, key)
            self.assertIs(non_claims[key], False, key)
            self.assertNotEqual(non_claims[key], "[REDACTED]", key)

    def assert_hidden_repo_state_false(self, result: Mapping[str, Any]) -> None:
        for section in (self.boundary(result), self.statement(result), self.non_claims(result)):
            self.assertIs(section["hidden_repo_state_used_as_participation_motion_content"], False)
            self.assertIs(section["hidden_repo_state_used_as_participation_motion_authority"], False)

    def assert_no_redacted_boolean_posture(self, result: Mapping[str, Any]) -> None:
        for section in (self.boundary(result), self.statement(result), self.non_claims(result)):
            for key, value in section.items():
                if key in REQ_FALSE or key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                    self.assertNotEqual(value, "[REDACTED]", key)
                    if isinstance(value, bool):
                        self.assertIs(type(value), bool, key)

    def assert_serialized_excludes_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_strings_present(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(BOUNDARY_TYPE, serialized)
        self.assertIn(BOUNDARY_SCOPE, serialized)
        self.assertIn(SELECTED_COMMAND, serialized)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertNotEqual(self.boundary(result)["boundary_type"], "[REDACTED]")
        self.assertNotEqual(self.boundary(result)["boundary_scope"], "[REDACTED]")

    def assert_boundary_object_is_not_wrapper(self, result: Mapping[str, Any]) -> None:
        self.assertTrue(EXPECTED_WRAPPER_SECTIONS.issubset(set(result)))
        boundary = self.boundary(result)
        for key in FORBIDDEN_WRAPPER_FIELDS_IN_BOUNDARY:
            self.assertNotIn(key, boundary)

    def assert_boundary_only(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in BOUNDARY_ONLY_FALSE_FIELDS:
            self.assertIn(key, boundary, key)
            self.assertIs(boundary[key], False, key)
        self.assertIs(boundary["role_admission_treated_as_participation_permission"], False)
        for key in (
            "received_derivative_participation_authority_imported",
            "received_derivative_action_authority_imported",
            "bounded_derivative_vessel_authority_imported",
            "derivative_vessel_relation_authority_imported",
        ):
            self.assertIs(boundary[key], False, key)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_boundary_only(result)
        self.assert_hidden_repo_state_false(result)

    def assert_recorded_clean_result(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(result["result_version"], "0.1.0")
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(self.summary(result)["passed_check_count"], 0)
        self.assertEqual(self.summary(result)["failed_check_count"], 0)
        self.assertEqual(self.summary(result)["result_version"], "0.1.0")
        self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
        self.assert_boundary_object_is_not_wrapper(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_hidden_repo_state_false(result)
        self.assert_no_redacted_boolean_posture(result)
        self.assert_boundary_only(result)
        self.assert_official_strings_present(result)

    def assert_expected_code_present(self, result: Mapping[str, Any], expected: str) -> None:
        self.assertIn(expected, resolver.BLOCK_CODES)
        self.assertIn(expected, self.emitted_codes(result))

    def assert_success_boundary_fields(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_001",
        )
        self.assertEqual(boundary["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(boundary["boundary_scope"], BOUNDARY_SCOPE)
        self.assertEqual(boundary["basis_role_admission_outcome"], ROLE_OUTCOME)
        self.assertEqual(boundary["basis_role_admission_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_role_admission_failed_check_count"], 0)
        self.assertEqual(boundary["basis_continuation_outcome"], CONTINUATION_OUTCOME)
        self.assertEqual(boundary["basis_continuation_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_continuation_failed_check_count"], 0)
        self.assertEqual(boundary["selected_command"], SELECTED_COMMAND)
        self.assertIs(boundary["selected_command_is_state"], True)
        self.assertIs(boundary["selected_command_preserved"], True)
        for key in CONTINUATION_POSITIVE_FIELDS + ROLE_POSITIVE_FIELDS + BOUNDARY_POSITIVE_FIELDS:
            self.assertIs(boundary[key], True, key)
        self.assertEqual(boundary["continuation_operation_sequence_count"], 2)
        for key in EVIDENCE_FIELDS:
            self.assertIs(boundary[key], True, key)
        self.assertIs(boundary["result_level_non_claims_canonical_false"], True)

    def assert_success_statement_fields(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        self.assertIs(
            statement[
                "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_recorded"
            ],
            True,
        )
        self.assertIs(statement["future_participation_motion_may_be_considered"], True)
        for key in (
            "participation_motion_created",
            "participant_output_authorized",
            "action_authorization_created",
            "participant_reentry_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "role_admission_treated_as_participation_permission",
            "hidden_repo_state_used_as_participation_motion_content",
            "hidden_repo_state_used_as_participation_motion_authority",
        ):
            self.assertIs(statement[key], False, key)
        self.assertIs(statement["result_level_non_claims_canonical_false"], True)

    def assert_path_block_or_bounded_error(self, func: Any) -> None:
        try:
            result = func()
        except resolver.LocalRelevanceMediumReadOnlyDerivativeParticipantParticipationMotionBoundaryV0MinV2Error:
            return
        self.assert_blocked_with_public_code(result)

    def test_public_api_constants_and_builder_defaults(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2",
            "resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_from_path",
            "write_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_result",
            "build_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_summary",
            "build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_NOT_RECORDED",
            "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_BOUNDARY_TYPE_VALUES",
            "SUPPORTED_BOUNDARY_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2",
        )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_BLOCKED,
            ),
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2"
            )
        )
        self.assertIn(BOUNDARY_TYPE, resolver.SUPPORTED_BOUNDARY_TYPE_VALUES)
        self.assertIn(BOUNDARY_SCOPE, resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, "state")

        for key in (
            BOUNDARY_POSITIVE_FIELDS
            + (
                "local_relevance_medium_read_only_derivative_participant_role_admission_recorded",
                "bounded_derivative_participant_role_admitted",
            )
            + CONTINUATION_POSITIVE_FIELDS
            + EVIDENCE_FIELDS
            + ("result_level_non_claims_canonical_false",)
        ):
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)

        for key in (
            "participation_motion_created",
            "participant_output_authorized",
            "action_authorization_created",
            "participant_reentry_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "third_operation_created",
            "unbounded_operation_sequence_created",
            "reusable_operation_permission_created",
            "role_admission_treated_as_participation_permission",
            "received_derivative_participation_authority_imported",
            "received_derivative_action_authority_imported",
            "bounded_derivative_vessel_authority_imported",
            "derivative_vessel_relation_authority_imported",
            "hidden_repo_state_used_as_participation_motion_content",
            "hidden_repo_state_used_as_participation_motion_authority",
            "source_created",
            "authority_created",
            "currentness_created",
            "truth_created",
            "follow_on_work_authorized",
            "continuation_v1_failure_repaired",
            "role_admission_v1_failure_repaired",
            "predecessor_failure_repaired",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)

        for code in (
            "PARTICIPATION_MOTION_CREATED",
            "PARTICIPANT_OUTPUT_AUTHORIZED",
            "ACTION_AUTHORIZATION_CREATED",
            "PARTICIPANT_REENTRY_CREATED",
            "DERIVATIVE_RECEPTION_AUTHORIZED",
            "VESSEL_RELATION_AUTHORIZED",
            "RUNTIME_HOSTING_CREATED",
            "PUBLIC_API_CREATED",
            "RECEIVED_DERIVATIVE_PARTICIPATION_AUTHORITY_IMPORTED",
            "BOUNDED_DERIVATIVE_VESSEL_AUTHORITY_IMPORTED",
            "ROLE_ADMISSION_TREATED_AS_PARTICIPATION_PERMISSION",
            "HIDDEN_REPO_STATE_USED_AS_PARTICIPATION_MOTION_CONTENT",
            "HIDDEN_REPO_STATE_USED_AS_PARTICIPATION_MOTION_AUTHORITY",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_request()
        )
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(request["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(request["boundary_scope"], BOUNDARY_SCOPE)
        self.assertTrue(
            request["selected_role_admission_artifact"].endswith(
                "local_relevance_medium_read_only_derivative_participant_role_admission_001__local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_result.json"
            )
        )
        self.assertTrue(
            request["selected_continuation_artifact"].endswith(
                "local_relevance_medium_read_only_continuation_reference_review_001__local_relevance_medium_read_only_continuation_v0_min_result.json"
            )
        )
        for key in REQ_FALSE:
            self.assertIn(key, request["declared_non_claims"])
            self.assertIs(request["declared_non_claims"][key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, request, _, _ = self.result_from_artifacts(Path(tmp))
        self.assert_recorded_clean_result(result)
        self.assert_success_boundary_fields(result)
        self.assert_success_statement_fields(result)
        self.assertEqual(
            self.boundary(result)["boundary_id"],
            request[
                "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_id"
            ],
        )

    def test_successful_recorded_result_from_default_live_artifacts_if_present(self) -> None:
        request = (
            resolver.build_declared_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_request()
        )
        role_path = REPO_ROOT / request["selected_role_admission_artifact"]
        continuation_path = REPO_ROOT / request["selected_continuation_artifact"]
        if not role_path.exists() or not continuation_path.exists():
            self.skipTest("default live basis artifacts are not present")
        result = resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2(
            request
        )
        self.assert_recorded_clean_result(result)
        self.assert_success_boundary_fields(result)
        self.assertTrue(
            self.boundary(result)["basis_role_admission_artifact"].endswith(role_path.name)
        )
        self.assertTrue(
            self.boundary(result)["basis_continuation_artifact"].endswith(continuation_path.name)
        )

    def test_declared_non_claim_flips_block_but_result_non_claims_remain_canonical(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, request, _, _ = self.result_from_artifacts(Path(tmp))
            for key in REQ_FALSE:
                with self.subTest(key=key):
                    mutated = copy.deepcopy(request)
                    mutated["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2(
                        mutated
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(self.non_claims(result)[key], False)

    def test_representative_blocking_behavior(self) -> None:
        cases: list[tuple[str, dict[str, Any]]] = [
            ("explicit_block_intent", {"request": {"local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent": "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_PARTICIPATION_MOTION_BOUNDARY"}}),
            ("missing_request_fields", {"request_replace": {}}),
            ("non_mapping_request", {"direct": []}),
            ("unsupported_intent", {"request": {"local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_intent": "UNSUPPORTED"}}),
            ("role_path_missing", {"request": {"selected_role_admission_artifact": ""}}),
            ("role_unreadable", {"request": {"selected_role_admission_artifact": "missing-role.json"}}),
            ("role_array", {"role_value": []}),
            ("role_not_recorded", {"role": {"outcome": "NOT_RECORDED"}}),
            ("role_failed_checks", {"role": {"failed_check_count": 1}}),
            ("role_version", {"role": {"result_version": "9.9.9"}}),
            ("continuation_path_missing", {"request": {"selected_continuation_artifact": ""}}),
            ("continuation_unreadable", {"request": {"selected_continuation_artifact": "missing-continuation.json"}}),
            ("continuation_array", {"continuation_value": []}),
            ("continuation_not_recorded", {"continuation": {"outcome": "NOT_RECORDED"}}),
            ("continuation_failed_checks", {"continuation": {"failed_check_count": 1}}),
            ("continuation_version", {"continuation": {"result_version": "9.9.9"}}),
            ("selected_command_missing", {"request": {"selected_command": None}}),
            ("selected_command_not_state", {"request": {"selected_command": "lookup"}}),
            ("boundary_type_missing", {"request": {"boundary_type": None}}),
            ("boundary_type_unsupported", {"request": {"boundary_type": "UNSUPPORTED"}}),
            ("boundary_scope_missing", {"request": {"boundary_scope": None}}),
            ("boundary_scope_unsupported", {"request": {"boundary_scope": "UNSUPPORTED"}}),
            ("non_claim_missing", {"request": {"declared_non_claims": {}}}),
        ]
        role_positive_cases = {
            "role_admission_not_recorded": "local_relevance_medium_read_only_derivative_participant_role_admission_recorded",
            "role_admission_not_created": "derivative_participant_role_admission_created",
            "bounded_role_not_admitted": "bounded_derivative_participant_role_admitted",
            "role_not_local": "role_admission_local_only",
            "role_not_read_only": "role_admission_read_only",
            "role_not_selected_state": "role_admission_selected_state_only",
            "role_not_basis_reference": "role_admission_basis_reference_only",
            "role_not_inside_continuation": "role_admission_inside_continuation_body",
            "role_not_from_continuation": "role_admission_from_continuation_only",
        }
        continuation_positive_cases = {
            "selected_continuation_not_recorded": "selected_continuation_recorded",
            "continuation_not_created": "continuation_created",
            "continuation_not_local": "continuation_local_only",
            "continuation_not_read_only": "continuation_read_only",
            "continuation_not_basis_reference": "continuation_basis_reference_only",
            "continuation_not_selected_state": "continuation_selected_state_only",
            "continuation_not_from_second_operation": "continuation_from_second_operation",
            "continuation_sequence_count_not_2": "continuation_sequence_count_is_2",
        }
        cases.extend((name, {"role_object": {key: False}}) for name, key in role_positive_cases.items())
        cases.extend((name, {"continuation_object": {key: False}}) for name, key in continuation_positive_cases.items())
        cases.append(("continuation_operation_sequence_count_not_2", {"continuation_object": {"continuation_operation_sequence_count": 3, "continuation_sequence_count_is_2": False}}))
        cases.extend((f"{key}_true", {"role_object": {key: True}}) for key in BOUNDARY_ONLY_FALSE_FIELDS)
        cases.extend((f"evidence_{key}_not_preserved", {"role_object": {key: False}}) for key in EVIDENCE_FIELDS)

        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            for name, config in cases:
                with self.subTest(name=name):
                    if "direct" in config:
                        result = resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2(
                            config["direct"]
                        )
                        self.assert_blocked_with_public_code(result)
                        continue

                    role_artifact: Any = config.get(
                        "role_value",
                        self.clean_role_artifact(object_overrides=config.get("role_object")),
                    )
                    continuation_artifact: Any = config.get(
                        "continuation_value",
                        self.clean_continuation_artifact(
                            object_overrides=config.get("continuation_object")
                        ),
                    )
                    role_path = self.write_json(base / f"{name}_role.json", role_artifact)
                    continuation_path = self.write_json(
                        base / f"{name}_continuation.json", continuation_artifact
                    )
                    request = self.request_for_paths(role_path, continuation_path)
                    if config.get("request_replace") is not None:
                        request = copy.deepcopy(config["request_replace"])
                    if "request" in config:
                        request.update(copy.deepcopy(config["request"]))
                    result = resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

    def test_positive_basis_can_be_derived_from_statement_summary_or_non_meaning(self) -> None:
        role_omits = ROLE_POSITIVE_FIELDS + (
            "role_admission_v1_failure_evidence_preserved",
            "predecessor_failure_evidence_preserved",
        )
        continuation_omits = CONTINUATION_POSITIVE_FIELDS + (
            "continuation_v1_failure_evidence_preserved",
            "predecessor_failure_evidence_preserved",
        )
        with tempfile.TemporaryDirectory() as tmp:
            for key in role_omits:
                with self.subTest(role_key=key):
                    role = self.clean_role_artifact(object_omits=(key,))
                    result, _, _, _ = self.result_from_artifacts(Path(tmp), role_artifact=role)
                    self.assert_recorded_clean_result(result)
            for key in continuation_omits:
                with self.subTest(continuation_key=key):
                    continuation = self.clean_continuation_artifact(object_omits=(key,))
                    result, _, _, _ = self.result_from_artifacts(
                        Path(tmp), continuation_artifact=continuation
                    )
                    self.assert_recorded_clean_result(result)

    def test_explanatory_true_values_do_not_count_as_forbidden_exact_posture(self) -> None:
        explanatory = {
            "explanatory_posture": {
                "participation_motion_not_created": True,
                "participant_output_not_authorized": True,
                "action_authorization_not_created": True,
                "participant_reentry_not_created": True,
                "derivative_reception_not_authorized": True,
                "vessel_relation_not_authorized": True,
                "runtime_hosting_not_created": True,
                "source_not_created": True,
                "authority_not_created": True,
                "currentness_not_created": True,
                "truth_not_created": True,
                "role_admission_not_treated_as_participation_permission": True,
                "hidden_repo_state_used_as_participation_motion_content_false_posture": True,
                "hidden_repo_state_used_as_participation_motion_authority_false_posture": True,
                "result_level_non_claims_canonical_false": True,
            },
            "basis_commentary": {"raw_state_body_not_embedded": True},
            "false_posture_preserved": {"participant_output_not_authorized": True},
            "non_claim_preservation": {"hidden_repo_state_used_as_participation_motion_content_false_posture": True},
            "lineage_evidence": {"predecessor_failure_evidence_preserved": True},
        }
        role_extra = copy.deepcopy(explanatory)
        role_extra["local_relevance_medium_read_only_derivative_participant_role_admission_checks"] = [
            {
                "check_name": "participation_motion_created_false_posture",
                "actual_posture": True,
                "passed": True,
            }
        ]
        continuation_extra = copy.deepcopy(explanatory)
        with tempfile.TemporaryDirectory() as tmp:
            result, _, _, _ = self.result_from_artifacts(
                Path(tmp),
                role_artifact=self.clean_role_artifact(extra_sections=role_extra),
                continuation_artifact=self.clean_continuation_artifact(
                    extra_sections=continuation_extra
                ),
            )
        self.assert_recorded_clean_result(result)
        self.assert_success_boundary_fields(result)

    def test_exact_forbidden_true_blocks_from_selected_object_or_top_non_claims(self) -> None:
        exact_keys = (
            "participation_motion_created",
            "participant_output_authorized",
            "action_authorization_created",
            "participant_reentry_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "received_derivative_participation_authority_imported",
            "received_derivative_action_authority_imported",
            "bounded_derivative_vessel_authority_imported",
            "derivative_vessel_relation_authority_imported",
            "role_admission_treated_as_participation_permission",
            "source_created",
            "authority_created",
            "currentness_created",
            "truth_created",
            "follow_on_work_authorized",
            "hidden_repo_state_used_as_participation_motion_content",
            "hidden_repo_state_used_as_participation_motion_authority",
            "consumed_request_reopened",
            "authorization_token_reused",
        )
        with tempfile.TemporaryDirectory() as tmp:
            for key in exact_keys:
                with self.subTest(selected_object_key=key):
                    role = self.clean_role_artifact(object_overrides={key: True})
                    result, _, _, _ = self.result_from_artifacts(Path(tmp), role_artifact=role)
                    self.assert_blocked_with_public_code(result)
                    self.assert_expected_code_present(result, FIELD_CODES[key])

                with self.subTest(top_level_non_claim_key=key):
                    role = self.clean_role_artifact(
                        object_omits=(key,),
                        statement_overrides={key: False},
                        summary_overrides={key: False},
                        non_meaning_overrides={key: False},
                        top_level_non_claim_overrides={key: True},
                    )
                    result, _, _, _ = self.result_from_artifacts(Path(tmp), role_artifact=role)
                    self.assert_blocked_with_public_code(result)
                    self.assert_expected_code_present(result, FIELD_CODES[key])

    def test_raw_hidden_and_ancestor_sentinel_content_is_contained(self) -> None:
        role = self.clean_role_artifact(
            extra_sections={
                "raw_payload": list(HOSTILE_SENTINELS),
                "hidden_state_payload": {"value": "HIDDEN_REPO_STATE_MUST_NOT_RETURN"},
                "basis_commentary": "PRESERVED_DERIVATIVE_ANCESTOR_AUTHORITY_IMPORT_MUST_NOT_RETURN",
            }
        )
        continuation = self.clean_continuation_artifact(
            extra_sections={
                "raw_payload": list(HOSTILE_SENTINELS),
                "hidden_state_payload": {"value": "RAW_STATE_BODY_MUST_NOT_RETURN"},
            }
        )
        with tempfile.TemporaryDirectory() as tmp:
            request_before: dict[str, Any] | None = None
            result, request, _, _ = self.result_from_artifacts(
                Path(tmp), role_artifact=role, continuation_artifact=continuation
            )
            request_before = _json_round_trip(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_serialized_excludes_sentinels(result)
        self.assert_official_strings_present(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_hidden_repo_state_false(result)
        self.assert_boundary_only(result)
        self.assertEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            result, request, _, _ = self.result_from_artifacts(root)
            request_path = self.write_json(root / "request.json", request)
            from_path = resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_from_path(
                request_path
            )
            self.assert_recorded_clean_result(from_path)

            malformed = root / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            self.assert_path_block_or_bounded_error(
                lambda: resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_from_path(
                    malformed
                )
            )
            array_path = self.write_json(root / "array.json", [])
            self.assert_path_block_or_bounded_error(
                lambda: resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_from_path(
                    array_path
                )
            )
            self.assert_path_block_or_bounded_error(
                lambda: resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_from_path(
                    root / "missing.json"
                )
            )

            output_root = root / "artifacts" / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_result(
                    result
                )
                second = resolver.write_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2_result(
                    result
                )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIsInstance(json.loads(first.read_text(encoding="utf-8")), dict)
            self.assertIn(
                "local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2",
                str(first),
            )
            forbidden_roots = (
                "participation_motion_boundary_v0_min/",
                "derivative_participant_role_admission_v0_min_v2",
                "continuation_v0_min",
                "received_derivative_participation",
                "received_derivative_action_permission",
                "derivative_vessel_relation",
                "source_transfer",
                "source_receipt",
                "public_api",
                "participant_facing_interface",
                "distributed_network",
            )
            for forbidden in forbidden_roots:
                self.assertNotIn(forbidden, str(first))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            role = self.clean_role_artifact(
                extra_sections={
                    "raw_state_payload": "RAW_STATE_BODY_MUST_NOT_RETURN",
                    "nested": {"hidden": "HIDDEN_REPO_STATE_MUST_NOT_RETURN"},
                }
            )
            continuation = self.clean_continuation_artifact(
                extra_sections={"raw_payload": "RAW_CONTINUATION_BODY_MUST_NOT_RETURN"}
            )
            role_before = _json_round_trip(role)
            continuation_before = _json_round_trip(continuation)
            result, request, _, _ = self.result_from_artifacts(
                root, role_artifact=role, continuation_artifact=continuation
            )
            request_before = _json_round_trip(request)
            resolver.resolve_local_relevance_medium_read_only_derivative_participant_participation_motion_boundary_v0_min_v2(
                request
            )
        self.assert_recorded_clean_result(result)
        self.assertEqual(role, role_before)
        self.assertEqual(continuation, continuation_before)
        self.assertEqual(request, request_before)

    def test_v1_predecessor_preservation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, _, _, _ = self.result_from_artifacts(Path(tmp))
        self.assert_recorded_clean_result(result)
        boundary = self.boundary(result)
        summary = self.summary(result)
        for key in EVIDENCE_FIELDS:
            self.assertIs(boundary[key], True, key)
            self.assertIs(summary[key], True, key)
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "continuation_v1_failure_repaired",
            "continuation_v1_failure_hidden",
            "continuation_v1_failure_claimed_passed",
            "role_admission_v1_failure_repaired",
            "role_admission_v1_failure_hidden",
            "role_admission_v1_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(boundary[key], False, key)
        self.assertIs(boundary["role_admission_treated_as_participation_permission"], False)
        self.assert_hidden_repo_state_false(result)


if __name__ == "__main__":
    unittest.main()
