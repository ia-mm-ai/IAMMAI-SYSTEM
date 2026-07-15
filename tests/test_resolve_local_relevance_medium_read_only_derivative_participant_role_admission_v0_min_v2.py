"""Tests for the v2 local relevance medium read-only role-admission resolver.

This suite verifies one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION object
only. The v1 role-admission resolver remains preserved predecessor evidence:
it broadly held the role-admission membrane, while v2 corrects the sanitizer
and non-claim canonicalization defect for official boolean false posture
fields whose keys mention hidden repo state.

The target remains local, read-only, selected-state-only,
basis-reference-only, downstream of continuation, and role-admission-only. It
admits one bounded derivative participant role without creating participation
motion, output authorization, action authorization, participant re-entry,
derivative reception, vessel relation, runtime/interface/source/authority/
currentness/truth behavior, ancestor derivative authority import, or follow-on
work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2 as resolver  # noqa: E402


ROLE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION"
ROLE_SCOPE = "SELECTED_ROLE_ADMISSION_ONLY"
CONTINUATION_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION"
CONTINUATION_SCOPE = "SELECTED_CONTINUATION_ONLY"
CONTINUATION_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_RECORDED"
SELECTED_COMMAND = "state"

REQ_FALSE = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
FIELD_CODES = getattr(
    resolver,
    "FALSE_FIELD_BLOCK_CODES",
    {key: key.upper() for key in REQ_FALSE},
)

EXPECTED_WRAPPER_SECTIONS = {
    "local_relevance_medium_read_only_derivative_participant_role_admission_metadata",
    "declared_local_relevance_medium_read_only_derivative_participant_role_admission_question",
    "selected_continuation_terminal_summary_basis",
    "selected_continuation_artifact_basis",
    "local_relevance_medium_read_only_derivative_participant_role_admission",
    "local_relevance_medium_read_only_derivative_participant_role_admission_checks",
    "local_relevance_medium_read_only_derivative_participant_role_admission_statement",
    "local_relevance_medium_read_only_derivative_participant_role_admission_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_derivative_participant_role_admission_summary",
}

FORBIDDEN_WRAPPER_FIELDS_IN_ROLE = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_derivative_participant_role_admission_checks",
    "non_claims",
    "local_relevance_medium_read_only_derivative_participant_role_admission_summary",
    "local_relevance_medium_read_only_derivative_participant_role_admission_metadata",
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
    "continuation_v1_failure_evidence_preserved",
    "predecessor_failure_evidence_preserved",
)

ROLE_ONLY_FALSE_FIELDS = (
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
    "hidden_repo_state_used_as_role_admission_content",
    "hidden_repo_state_used_as_role_admission_authority",
    "consumed_request_reopened",
    "authorization_token_reused",
)

HOSTILE_SENTINELS = (
    "RAW_ROLE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPATION_MOTION_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_OUTPUT_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_AUTHORIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_DERIVATIVE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_VESSEL_RELATION_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "PRESERVED_DERIVATIVE_ANCESTOR_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _safe_name(value: Any) -> str:
    text = str(value)
    text = text.replace("/", "_").replace("\\", "_").replace(" ", "_")
    text = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in text)
    while "__" in text:
        text = text.replace("__", "_")
    return text.strip("._-") or "case"


class LocalRelevanceMediumReadOnlyDerivativeParticipantRoleAdmissionV0MinV2Tests(
    unittest.TestCase
):
    def write_json(self, path: Path, value: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def clean_continuation_artifact(
        self,
        *,
        selected_overrides: Mapping[str, Any] | None = None,
        selected_omits: tuple[str, ...] = (),
        statement_overrides: Mapping[str, Any] | None = None,
        summary_overrides: Mapping[str, Any] | None = None,
        non_meaning_overrides: Mapping[str, Any] | None = None,
        top_level_non_claim_overrides: Mapping[str, Any] | None = None,
        failed_check_count: int = 0,
        outcome: str = CONTINUATION_OUTCOME,
        result_version: str = "0.1.0",
        extra_sections: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        non_claims = {key: False for key in REQ_FALSE}
        selected = {
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
            "continuation_operation_sequence_count_is_2": True,
            "continuation_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        selected.update(non_claims)
        if selected_overrides:
            selected.update(copy.deepcopy(dict(selected_overrides)))
        for key in selected_omits:
            selected.pop(key, None)

        statement = {
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
            "continuation_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        statement.update({key: False for key in REQ_FALSE})
        if statement_overrides:
            statement.update(copy.deepcopy(dict(statement_overrides)))

        summary = {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "selected_continuation_recorded": True,
            "continuation_created": True,
            "continuation_local_only": True,
            "continuation_read_only": True,
            "continuation_basis_reference_only": True,
            "continuation_selected_state_only": True,
            "continuation_from_second_operation": True,
            "continuation_operation_sequence_count": 2,
            "continuation_sequence_count_is_2": True,
            "continuation_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        if summary_overrides:
            summary.update(copy.deepcopy(dict(summary_overrides)))

        non_meaning = {
            "continuation_v1_failure_evidence_preserved": True,
            "predecessor_failure_evidence_preserved": True,
            "this_is_continuation_only": True,
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
            "local_relevance_medium_read_only_continuation": selected,
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

    def request_for_artifact(self, artifact_path: Path, **overrides: Any) -> dict[str, Any]:
        request = (
            resolver.build_declared_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_request(
                selected_continuation_artifact=artifact_path,
                selected_command=SELECTED_COMMAND,
                role_admission_type=ROLE_TYPE,
                role_admission_scope=ROLE_SCOPE,
            )
        )
        request.update(copy.deepcopy(overrides))
        return request

    def result_from_artifact(
        self,
        tmp_path: Path,
        artifact: Mapping[str, Any] | None = None,
        **request_overrides: Any,
    ) -> tuple[dict[str, Any], dict[str, Any], Path]:
        artifact_value = (
            self.clean_continuation_artifact()
            if artifact is None
            else copy.deepcopy(dict(artifact))
        )
        artifact_path = self.write_json(tmp_path / "selected_continuation.json", artifact_value)
        request = self.request_for_artifact(artifact_path, **request_overrides)
        result = (
            resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2(
                request
            )
        )
        return result, request, artifact_path

    def role(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        role = result["local_relevance_medium_read_only_derivative_participant_role_admission"]
        self.assertIsInstance(role, Mapping)
        return role

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result[
            "local_relevance_medium_read_only_derivative_participant_role_admission_statement"
        ]
        self.assertIsInstance(statement, Mapping)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result[
            "local_relevance_medium_read_only_derivative_participant_role_admission_summary"
        ]
        self.assertIsInstance(summary, Mapping)
        return summary

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result[
            "local_relevance_medium_read_only_derivative_participant_role_admission_checks"
        ]
        self.assertIsInstance(checks, list)
        return checks

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, Mapping)
        return non_claims

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def block_code(self, result: Mapping[str, Any]) -> Any:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def emitted_codes(self, result: Mapping[str, Any]) -> list[str]:
        codes: list[str] = []
        block_code = self.block_code(result)
        if isinstance(block_code, str):
            codes.append(block_code)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if isinstance(code, str):
                    codes.append(code)
        return codes

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
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

    def assert_role_admission_non_claims(self, result: Mapping[str, Any]) -> None:
        role = self.role(result)
        for key in REQ_FALSE:
            self.assertIn(key, role)
            self.assertIs(role[key], False, key)

    def assert_hidden_repo_state_false(self, result: Mapping[str, Any]) -> None:
        for section in (self.role(result), self.statement(result), self.non_claims(result)):
            self.assertIs(
                section["hidden_repo_state_used_as_role_admission_content"],
                False,
            )
            self.assertIs(
                section["hidden_repo_state_used_as_role_admission_authority"],
                False,
            )

    def assert_no_redacted_boolean_posture(self, result: Mapping[str, Any]) -> None:
        for section in (self.role(result), self.statement(result), self.non_claims(result)):
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
        self.assertIn(ROLE_TYPE, serialized)
        self.assertIn(ROLE_SCOPE, serialized)
        self.assertIn(SELECTED_COMMAND, serialized)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertNotEqual(self.role(result)["role_admission_type"], "[REDACTED]")
        self.assertNotEqual(self.role(result)["role_admission_scope"], "[REDACTED]")

    def assert_role_object_is_not_wrapper(self, result: Mapping[str, Any]) -> None:
        self.assertTrue(EXPECTED_WRAPPER_SECTIONS.issubset(set(result)))
        role = self.role(result)
        for key in FORBIDDEN_WRAPPER_FIELDS_IN_ROLE:
            self.assertNotIn(key, role)

    def assert_role_admission_only(self, result: Mapping[str, Any]) -> None:
        role = self.role(result)
        for key in ROLE_ONLY_FALSE_FIELDS:
            self.assertIn(key, role, key)
            self.assertIs(role[key], False, key)
        self.assertIs(role["consumed_request_token_remains_closed"], True)
        self.assertIs(role["authorization_token_reuse_blocked"], True)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_role_admission_non_claims(result)

    def assert_recorded_clean_result(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertGreater(self.summary(result)["passed_check_count"], 0)
        self.assertEqual(self.summary(result)["result_version"], "0.1.0")
        self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
        self.assert_role_object_is_not_wrapper(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_role_admission_non_claims(result)
        self.assert_hidden_repo_state_false(result)
        self.assert_no_redacted_boolean_posture(result)
        self.assert_role_admission_only(result)

    def assert_expected_code_present(self, result: Mapping[str, Any], expected: str) -> None:
        self.assertIn(expected, resolver.BLOCK_CODES)
        self.assertIn(expected, self.emitted_codes(result))

    def test_public_api_constants_and_builder_defaults(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2",
            "resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_from_path",
            "write_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_result",
            "build_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_summary",
            "build_declared_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_ROLE_ADMISSION_TYPE_VALUES",
            "SUPPORTED_ROLE_ADMISSION_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2"
            )
        )
        self.assertIn(ROLE_TYPE, resolver.SUPPORTED_ROLE_ADMISSION_TYPE_VALUES)
        self.assertIn(ROLE_SCOPE, resolver.SUPPORTED_ROLE_ADMISSION_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)

        required_false_names = (
            "hidden_repo_state_used_as_role_admission_content",
            "hidden_repo_state_used_as_role_admission_authority",
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
            "follow_on_work_authorized",
        )
        for key in required_false_names:
            self.assertIn(key, REQ_FALSE)

        public_codes = (
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
            "HIDDEN_REPO_STATE_USED_AS_ROLE_ADMISSION_CONTENT",
            "HIDDEN_REPO_STATE_USED_AS_ROLE_ADMISSION_AUTHORITY",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        for code in public_codes:
            self.assertIn(code, resolver.BLOCK_CODES)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_request()
        )
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(request["role_admission_type"], ROLE_TYPE)
        self.assertEqual(request["role_admission_scope"], ROLE_SCOPE)
        self.assertTrue(
            str(request["selected_continuation_artifact"]).endswith(
                "local_relevance_medium_read_only_continuation_reference_review_001__local_relevance_medium_read_only_continuation_v0_min_result.json"
            )
        )
        for key in REQ_FALSE:
            self.assertIs(request["declared_non_claims"][key], False)

    def test_records_from_synthetic_continuation_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            result, _request, _path = self.result_from_artifact(Path(root))
        self.assert_recorded_clean_result(result)
        role = self.role(result)
        self.assertEqual(
            role["role_admission_id"],
            "local_relevance_medium_read_only_derivative_participant_role_admission_001",
        )
        self.assertEqual(role["role_admission_type"], ROLE_TYPE)
        self.assertEqual(role["role_admission_version"], "0.1.0")
        self.assertEqual(role["role_admission_scope"], ROLE_SCOPE)
        self.assertEqual(role["basis_continuation_outcome"], CONTINUATION_OUTCOME)
        self.assertEqual(role["basis_continuation_result_version"], "0.1.0")
        self.assertEqual(role["basis_continuation_failed_check_count"], 0)
        self.assertEqual(role["selected_command"], SELECTED_COMMAND)
        self.assertEqual(role["continuation_operation_sequence_count"], 2)
        for key in ROLE_POSITIVE_FIELDS + CONTINUATION_POSITIVE_FIELDS:
            self.assertIs(role[key], True, key)
        self.assertIs(role["continuation_v1_failure_evidence_preserved"], True)
        self.assertIs(role["predecessor_failure_evidence_preserved"], True)
        self.assertIs(role["result_level_non_claims_canonical_false"], True)

        statement = self.statement(result)
        self.assertIs(
            statement[
                "local_relevance_medium_read_only_derivative_participant_role_admission_recorded"
            ],
            True,
        )
        self.assertIs(statement["bounded_derivative_participant_role_admitted"], True)
        self.assertIs(statement["participation_motion_created"], False)
        self.assertIs(statement["participant_output_authorized"], False)
        self.assertIs(statement["action_authorization_created"], False)
        self.assertIs(statement["participant_reentry_created"], False)
        self.assertIs(statement["derivative_reception_authorized"], False)
        self.assertIs(statement["vessel_relation_authorized"], False)
        self.assertIs(statement["result_level_non_claims_canonical_false"], True)

    def test_records_from_default_live_artifact_if_present(self) -> None:
        request = (
            resolver.build_declared_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_request()
        )
        default_path = REPO_ROOT / request["selected_continuation_artifact"]
        if not default_path.exists():
            self.skipTest("default continuation artifact is not present")
        result = (
            resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2(
                request
            )
        )
        self.assert_recorded_clean_result(result)
        role = self.role(result)
        self.assertEqual(role["selected_command"], SELECTED_COMMAND)
        self.assertEqual(role["role_admission_type"], ROLE_TYPE)
        self.assertEqual(role["role_admission_scope"], ROLE_SCOPE)
        self.assertTrue(
            str(role["basis_continuation_artifact"]).endswith(
                "local_relevance_medium_read_only_continuation_reference_review_001__local_relevance_medium_read_only_continuation_v0_min_result.json"
            )
        )

    def test_hidden_repo_state_sanitizer_regression(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            result, _request, _path = self.result_from_artifact(Path(root))
        self.assert_recorded_clean_result(result)
        self.assert_hidden_repo_state_false(result)
        for value in self.non_claims(result).values():
            self.assertNotEqual(value, "[REDACTED]")

    def test_declared_non_claim_flips_block_but_result_non_claims_canonical(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            artifact_path = self.write_json(
                root_path / "continuation.json",
                self.clean_continuation_artifact(),
            )
            base_request = self.request_for_artifact(artifact_path)
            for key in REQ_FALSE:
                with self.subTest(declared_non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_expected_code_present(
                        result,
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                    )
                    self.assertIs(self.non_claims(result)[key], False)
                    self.assert_role_admission_only(result)
                    self.assert_hidden_repo_state_false(result)

    def representative_block_cases(
        self,
        root: Path,
    ) -> list[tuple[str, str, Callable[[dict[str, Any], dict[str, Any], Path], Any]]]:
        def set_artifact_path(path: Path) -> Callable[[dict[str, Any], dict[str, Any], Path], None]:
            return lambda request, artifact, root_path: request.update(
                {"selected_continuation_artifact": str(path)}
            )

        return [
            (
                "explicit_block_intent",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_BLOCK_REQUESTED",
                lambda request, artifact, root_path: request.update(
                    {
                        "local_relevance_medium_read_only_derivative_participant_role_admission_intent": "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION"
                    }
                ),
            ),
            (
                "missing_request",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_QUESTION_UNDECLARED",
                lambda request, artifact, root_path: request.clear(),
            ),
            (
                "unsupported_intent",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_INTENT_UNSUPPORTED",
                lambda request, artifact, root_path: request.update(
                    {
                        "local_relevance_medium_read_only_derivative_participant_role_admission_intent": "UNSUPPORTED_ROLE_ADMISSION_INTENT"
                    }
                ),
            ),
            (
                "artifact_path_missing",
                "CONTINUATION_ARTIFACT_PATH_MISSING",
                lambda request, artifact, root_path: request.pop(
                    "selected_continuation_artifact", None
                ),
            ),
            (
                "artifact_unreadable",
                "CONTINUATION_ARTIFACT_UNREADABLE",
                set_artifact_path(root / "missing_continuation.json"),
            ),
            (
                "artifact_array",
                "CONTINUATION_ARTIFACT_NOT_JSON_OBJECT",
                lambda request, artifact, root_path: request.update(
                    {
                        "selected_continuation_artifact": str(
                            self.write_json(root_path / "array.json", [])
                        )
                    }
                ),
            ),
            (
                "artifact_not_recorded",
                "CONTINUATION_ARTIFACT_NOT_RECORDED",
                lambda request, artifact, root_path: artifact.update(
                    {"outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BLOCKED"}
                ),
            ),
            (
                "artifact_failed_checks",
                "CONTINUATION_ARTIFACT_FAILED_CHECKS_PRESENT",
                lambda request, artifact, root_path: artifact.update({"failed_check_count": 1}),
            ),
            (
                "artifact_version",
                "CONTINUATION_ARTIFACT_VERSION_NOT_0_1_0",
                lambda request, artifact, root_path: artifact.update({"result_version": "0.2.0"}),
            ),
            (
                "selected_command_missing",
                "SELECTED_COMMAND_MISSING",
                lambda request, artifact, root_path: request.pop("selected_command", None),
            ),
            (
                "selected_command_not_state",
                "SELECTED_COMMAND_NOT_STATE",
                lambda request, artifact, root_path: request.update({"selected_command": "status"}),
            ),
            (
                "selected_continuation_not_recorded",
                "SELECTED_CONTINUATION_NOT_RECORDED",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"selected_continuation_recorded": False}),
            ),
            (
                "continuation_not_created",
                "CONTINUATION_NOT_CREATED",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"continuation_created": False}),
            ),
            (
                "continuation_not_local_only",
                "CONTINUATION_LOCAL_ONLY_NOT_TRUE",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"continuation_local_only": False}),
            ),
            (
                "continuation_not_read_only",
                "CONTINUATION_READ_ONLY_NOT_TRUE",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"continuation_read_only": False}),
            ),
            (
                "continuation_not_basis_reference_only",
                "CONTINUATION_BASIS_REFERENCE_ONLY_NOT_TRUE",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"continuation_basis_reference_only": False}),
            ),
            (
                "continuation_not_selected_state_only",
                "CONTINUATION_SELECTED_STATE_ONLY_NOT_TRUE",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"continuation_selected_state_only": False}),
            ),
            (
                "continuation_not_from_second_operation",
                "CONTINUATION_FROM_SECOND_OPERATION_NOT_TRUE",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"continuation_from_second_operation": False}),
            ),
            (
                "continuation_sequence_count",
                "CONTINUATION_OPERATION_SEQUENCE_COUNT_NOT_2",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"continuation_operation_sequence_count": 3}),
            ),
            (
                "continuation_v1_evidence",
                "CONTINUATION_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"continuation_v1_failure_evidence_preserved": False}),
            ),
            (
                "predecessor_evidence",
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
                lambda request, artifact, root_path: artifact[
                    "local_relevance_medium_read_only_continuation"
                ].update({"predecessor_failure_evidence_preserved": False}),
            ),
            (
                "role_type_missing",
                "ROLE_ADMISSION_TYPE_MISSING",
                lambda request, artifact, root_path: request.pop("role_admission_type", None),
            ),
            (
                "role_type_unsupported",
                "ROLE_ADMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION",
                lambda request, artifact, root_path: request.update(
                    {"role_admission_type": "UNSUPPORTED_ROLE_ADMISSION_TYPE"}
                ),
            ),
            (
                "role_scope_missing",
                "ROLE_ADMISSION_SCOPE_MISSING",
                lambda request, artifact, root_path: request.pop("role_admission_scope", None),
            ),
            (
                "role_scope_unsupported",
                "ROLE_ADMISSION_SCOPE_NOT_SELECTED_ROLE_ADMISSION_ONLY",
                lambda request, artifact, root_path: request.update(
                    {"role_admission_scope": "UNSUPPORTED_ROLE_ADMISSION_SCOPE"}
                ),
            ),
        ]

    def test_representative_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            for name, expected_code, mutate in self.representative_block_cases(root_path):
                with self.subTest(name=name):
                    artifact = self.clean_continuation_artifact()
                    artifact_path = root_path / f"{_safe_name(name)}.json"
                    request = self.request_for_artifact(artifact_path)
                    mutate(request, artifact, root_path)
                    if isinstance(request.get("selected_continuation_artifact"), str):
                        selected_path = Path(request["selected_continuation_artifact"])
                        if not selected_path.exists() and name not in (
                            "artifact_unreadable",
                            "artifact_array",
                        ):
                            self.write_json(selected_path, artifact)
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_expected_code_present(result, expected_code)
                    self.assert_role_admission_only(result)
                    self.assert_hidden_repo_state_false(result)

        result = (
            resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2(
                ["not", "a", "mapping"]
            )
        )
        self.assert_blocked_with_public_code(result)
        self.assert_expected_code_present(
            result,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_REQUEST_MALFORMED",
        )

    def test_false_posture_exact_key_blocks(self) -> None:
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
            "artifact_existence_treated_as_role_admission_authority",
            "latest_file_posture_treated_as_role_admission_authority",
            "repo_local_availability_treated_as_role_admission_authority",
            "hidden_repo_state_used_as_role_admission_content",
            "hidden_repo_state_used_as_role_admission_authority",
            "continuation_v1_failure_repaired",
            "continuation_v1_failure_hidden",
            "continuation_v1_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        )
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            for key in exact_keys:
                with self.subTest(selected_object_key=key):
                    artifact = self.clean_continuation_artifact(
                        selected_overrides={key: True}
                    )
                    result, _request, _path = self.result_from_artifact(
                        root_path / f"selected_{_safe_name(key)}",
                        artifact,
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_expected_code_present(result, FIELD_CODES[key])
                    self.assert_canonical_false_non_claims(result)
                    self.assert_role_admission_only(result)

                with self.subTest(top_level_non_claim=key):
                    artifact = self.clean_continuation_artifact(
                        selected_omits=(key,),
                        top_level_non_claim_overrides={key: True},
                    )
                    result, _request, _path = self.result_from_artifact(
                        root_path / f"top_{_safe_name(key)}",
                        artifact,
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_expected_code_present(result, FIELD_CODES[key])
                    self.assert_canonical_false_non_claims(result)
                    self.assert_role_admission_only(result)

    def test_positive_basis_derivation_from_statement_summary_and_non_meaning(self) -> None:
        source_by_field = {
            "selected_continuation_recorded": "fallback",
            "continuation_created": "statement",
            "continuation_local_only": "statement",
            "continuation_read_only": "summary",
            "continuation_basis_reference_only": "statement",
            "continuation_selected_state_only": "summary",
            "continuation_from_second_operation": "statement",
            "continuation_sequence_count_is_2": "summary",
            "continuation_v1_failure_evidence_preserved": "non_meaning",
            "predecessor_failure_evidence_preserved": "summary",
        }
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            for field, source in source_by_field.items():
                with self.subTest(field=field, source=source):
                    statement = {}
                    summary = {}
                    non_meaning = {}
                    if source == "statement":
                        statement[field] = True
                    elif source == "summary":
                        summary[field] = True
                    elif source == "non_meaning":
                        statement.pop(field, None)
                        summary.pop(field, None)
                        non_meaning[field] = True
                    artifact = self.clean_continuation_artifact(
                        selected_omits=(field,),
                        statement_overrides=statement,
                        summary_overrides=summary,
                        non_meaning_overrides=non_meaning,
                    )
                    if field == "selected_continuation_recorded":
                        artifact["local_relevance_medium_read_only_continuation_statement"].pop(
                            field,
                            None,
                        )
                        artifact["local_relevance_medium_read_only_continuation_summary"].pop(
                            field,
                            None,
                        )
                    if field == "continuation_v1_failure_evidence_preserved":
                        artifact["local_relevance_medium_read_only_continuation_statement"].pop(
                            field,
                            None,
                        )
                        artifact["local_relevance_medium_read_only_continuation_summary"].pop(
                            field,
                            None,
                        )
                    result, _request, _path = self.result_from_artifact(
                        root_path / _safe_name(field),
                        artifact,
                    )
                    self.assert_recorded_clean_result(result)
                    self.assertIs(self.role(result)[field], True)

    def test_explanatory_true_values_do_not_block_when_exact_false_posture_clean(
        self,
    ) -> None:
        explanatory = {
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
            "hidden_repo_state_used_as_role_admission_content_false_posture": True,
            "hidden_repo_state_used_as_role_admission_authority_false_posture": True,
            "result_level_non_claims_canonical_false": True,
        }
        artifact = self.clean_continuation_artifact(
            extra_sections={
                "explanatory_posture": copy.deepcopy(explanatory),
                "basis_commentary": copy.deepcopy(explanatory),
                "false_posture_preserved": copy.deepcopy(explanatory),
                "non_claim_preservation": copy.deepcopy(explanatory),
                "lineage_evidence": copy.deepcopy(explanatory),
            }
        )
        artifact["local_relevance_medium_read_only_continuation_checks"] = [
            {
                "check_name": "preserving_false_posture_explanation",
                "passed": True,
                "expected_posture": False,
                "actual_posture": True,
                "block_code": None,
                "failure_code": None,
            }
        ]
        with tempfile.TemporaryDirectory() as root:
            result, _request, _path = self.result_from_artifact(Path(root), artifact)
        self.assert_recorded_clean_result(result)
        self.assert_role_admission_only(result)

    def test_hostile_raw_hidden_and_ancestor_sentinel_content_is_contained(self) -> None:
        artifact = self.clean_continuation_artifact(
            selected_overrides={
                "raw_state_body": "RAW_STATE_BODY_MUST_NOT_RETURN",
                "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                "raw_role_admission_body": "RAW_ROLE_ADMISSION_BODY_MUST_NOT_RETURN",
            },
            extra_sections={
                "raw_full_prior_artifact_body": "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
                "preserved_ancestor_authority": "PRESERVED_DERIVATIVE_ANCESTOR_AUTHORITY_IMPORT_MUST_NOT_RETURN",
                "participant_output_body": "RAW_PARTICIPANT_OUTPUT_BODY_MUST_NOT_RETURN",
                "follow_on_commentary": "RAW_ACTION_AUTHORIZATION_BODY_MUST_NOT_RETURN",
            },
        )
        with tempfile.TemporaryDirectory() as root:
            original_request: dict[str, Any]
            result, original_request, _path = self.result_from_artifact(
                Path(root),
                artifact,
                local_extra_payload={"raw_body": "RAW_CONTINUATION_BODY_MUST_NOT_RETURN"},
            )
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        if result["outcome"] == resolver.OUTCOME_BLOCKED:
            self.assert_blocked_with_public_code(result)
        self.assert_serialized_excludes_sentinels(result)
        self.assert_official_strings_present(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_hidden_repo_state_false(result)
        self.assert_role_admission_only(result)
        self.assertEqual(
            original_request.get("local_extra_payload"),
            {"raw_body": "RAW_CONTINUATION_BODY_MUST_NOT_RETURN"},
        )

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            artifact_path = self.write_json(
                root_path / "continuation.json",
                self.clean_continuation_artifact(),
            )
            request = self.request_for_artifact(artifact_path)
            request_path = self.write_json(root_path / "request.json", request)
            result = (
                resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_from_path(
                    request_path
                )
            )
            self.assert_recorded_clean_result(result)

            malformed = root_path / "malformed.json"
            malformed.write_text("{not-json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_from_path(
                    malformed
                )
            )
            self.assert_blocked_with_public_code(malformed_result)

            array_path = self.write_json(root_path / "array_request.json", [])
            array_result = (
                resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_from_path(
                    array_path
                )
            )
            self.assert_blocked_with_public_code(array_result)

            missing_result = (
                resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_from_path(
                    root_path / "missing_request.json"
                )
            )
            self.assert_blocked_with_public_code(missing_result)

            output_root = root_path / resolver.OUTPUT_ROOT
            first_path = (
                resolver.write_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_result(
                    result,
                    output_path=output_root,
                )
            )
            second_path = (
                resolver.write_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_result(
                    result,
                    output_path=output_root,
                )
            )
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(first_path.parent.exists())
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn(
                "local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2",
                str(first_path),
            )
            forbidden_roots = (
                "derivative_participant_role_admission_v0_min/",
                "continuation_v0_min/",
                "continuation_boundary_v0_min/",
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
                self.assertNotIn(forbidden, str(first_path))

    def test_non_mutation(self) -> None:
        artifact = self.clean_continuation_artifact(
            selected_overrides={
                "hidden_repo_state_used_as_role_admission_content": False,
                "hidden_repo_state_used_as_role_admission_authority": False,
            },
            extra_sections={
                "nested_payload": {
                    "raw_body": "RAW_STATE_BODY_MUST_NOT_RETURN",
                    "closure_token": {"consumed_request_reopened": False},
                }
            },
        )
        artifact_before = copy.deepcopy(artifact)
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            artifact_path = self.write_json(root_path / "continuation.json", artifact)
            request = self.request_for_artifact(artifact_path)
            request["declared_non_claims"]["hidden_repo_state_used_as_role_admission_content"] = False
            request_before = copy.deepcopy(request)
            result = (
                resolver.resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2(
                    request
                )
            )
        self.assert_recorded_clean_result(result)
        self.assertEqual(request, request_before)
        self.assertEqual(artifact, artifact_before)

    def test_v1_predecessor_preservation(self) -> None:
        v1_path = (
            SRC_ROOT
            / "resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min.py"
        )
        before = v1_path.read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as root:
            result, _request, _path = self.result_from_artifact(Path(root))
        after = v1_path.read_text(encoding="utf-8")
        self.assertEqual(after, before)
        self.assert_recorded_clean_result(result)
        role = self.role(result)
        summary = self.summary(result)
        self.assertIs(role["continuation_v1_failure_evidence_preserved"], True)
        self.assertIs(role["predecessor_failure_evidence_preserved"], True)
        self.assertIs(role["predecessor_failure_repaired"], False)
        self.assertIs(role["predecessor_failure_hidden"], False)
        self.assertIs(role["predecessor_failure_claimed_passed"], False)
        self.assertIs(role["consumed_request_token_remains_closed"], True)
        self.assertIs(role["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["continuation_v1_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assert_hidden_repo_state_false(result)


if __name__ == "__main__":
    unittest.main()
