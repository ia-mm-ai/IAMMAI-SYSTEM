"""Bounded tests for the operator-facing terminal brief resolver.

This suite exercises
``src/resolve_operator_facing_terminal_brief__bounded_current_state_read.py``
as one shell-owned, bounded downstream consumer of one successful v3 bounded
current-state vessel result. It keeps the source result family brutally narrow
and verifies that the brief remains derivative only.

This is not a chat-shell, dashboard, workflow, or authority-surface test.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Iterator, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


import openai_api_vessel__bounded_current_state_read_v3 as vessel_v3
import resolve_operator_facing_terminal_brief__bounded_current_state_read as brief


EXPECTED_RESULT_KEYS = {
    "operator_terminal_brief_metadata",
    "selected_vessel_result",
    "brief_request",
    "brief_output",
    "outcome",
    "block",
    "brief_summary",
    "non_claims",
}

EXPECTED_REQUEST_KEYS = {
    "brief_request_id",
    "brief_use_case",
    "admitted_use_class",
    "allowed_source_result_family",
    "selected_vessel_result_id",
    "selected_vessel_result_path",
    "selected_source_surface_id",
    "question",
    "derivative_answer",
    "brief_instructions",
}


def read_json(path: Path | str) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object at {path}")
    return value


def file_digest(path: Path | str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class OperatorTerminalBriefTests(unittest.TestCase):
    def build_v3_vessel_result(
        self,
        vessel_result_id: str = "what_stands_now_result_001__bounded_current_state_read_v3_answered",
        *,
        source_id: str = "what_stands_now_result_001",
        source_family: str = brief.UPSTREAM_ALLOWED_SOURCE_FAMILY,
        allowed_source_family: str = brief.UPSTREAM_ALLOWED_SOURCE_FAMILY,
        result_type: str = brief.SUPPORTED_SOURCE_RESULT_TYPE,
        outcome: str = brief.SOURCE_OUTCOME_ANSWERED,
        question: str = "What stands now?",
        answer: str = "bounded derivative read v3",
        metadata_overrides: Mapping[str, Any] | None = None,
        selected_source_overrides: Mapping[str, Any] | None = None,
        vessel_request_overrides: Mapping[str, Any] | None = None,
        derivative_answer_overrides: Mapping[str, Any] | None = None,
        top_level_overrides: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        metadata = {
            "vessel_result_id": vessel_result_id,
            "vessel_result_type": result_type,
            "vessel_result_version": vessel_v3.VESSEL_RESULT_VERSION,
            "generated_at": "2026-04-24T00:00:00Z",
            "resolver_module": vessel_v3.RESOLVER_MODULE,
            "successor_of_module": vessel_v3.SUCCESSOR_OF_MODULE,
        }
        if metadata_overrides:
            metadata.update(metadata_overrides)

        selected_source = {
            "selected_source_surface_path": (
                "artifacts/integrity_host_v0_min_coexistence_current_state_"
                "what_stands_now/selected.json"
            ),
            "selected_source_surface_id": source_id,
            "selected_source_surface_family": source_family,
            "selected_source_surface_outcome": vessel_v3.SOURCE_OUTCOME_ANSWERED,
        }
        if selected_source_overrides:
            selected_source.update(selected_source_overrides)

        vessel_request = {
            "vessel_request_id": f"{source_id}__bounded_current_state_read_request",
            "vessel_use_case": vessel_v3.VESSEL_USE_CASE,
            "admitted_use_class": vessel_v3.SUPPORTED_USE_CLASS,
            "allowed_source_family": allowed_source_family,
            "selected_source_surface_id": source_id,
            "selected_source_surface_path": (
                "artifacts/integrity_host_v0_min_coexistence_current_state_"
                "what_stands_now/selected.json"
            ),
            "question": question,
            "bounded_source_payload": {
                "current_governing_source_run_path": (
                    "artifacts/integrity_host_v0_min_coexistence_source_runs/"
                    "run_20260424T000000_000000Z"
                ),
                "current_governing_ingress_run_path": (
                    "artifacts/integrity_host_v0_min_coexistence_receiving_ingress/"
                    "run_20260424T000000_000000Z"
                ),
                "current_authority_artifact_path": (
                    "artifacts/integrity_host_v0_min_coexistence_execution_authority/"
                    "current_execution_authority.json"
                ),
                "preserved_run_count": 2,
                "application_basis": "bounded application basis",
                "delivery_basis": "bounded delivery basis",
                "answer_read_basis": "bounded answer/read basis",
            },
            "instructions": "bounded instructions",
        }
        if vessel_request_overrides:
            vessel_request.update(vessel_request_overrides)

        derivative_answer = {
            "answer": answer,
            "answer_basis": "bounded_source_payload",
            "source_remains_source": True,
            "model_output_remains_derivative": True,
        }
        if derivative_answer_overrides:
            derivative_answer.update(derivative_answer_overrides)

        result = {
            "openai_api_derivative_vessel_v3_metadata": metadata,
            "selected_source_surface": selected_source,
            "vessel_request": vessel_request,
            "api_runtime": {
                "model_name_used": "gpt-bounded-v3-test",
                "explicit_model_env_override_used": True,
                "local_setup_present": True,
                "openai_package_present": True,
                "api_key_present": True,
                "strict_structured_output_path_used": True,
            },
            "model_output": {
                "raw_output_text": json.dumps({"answer": answer}),
                "parsed_output": {"answer": answer},
                "refusal_signal": None,
            },
            "outcome": outcome,
            "block": {
                "block_code": None,
                "block_reason": None,
            },
            "derivative_answer": derivative_answer,
            "vessel_summary": {
                "selected_source_surface_id": source_id,
                "allowed_source_family": allowed_source_family,
                "question": question,
                "outcome": outcome,
                "block_code": None,
                "block_reason": None,
            },
            "non_claims": dict(vessel_v3.NON_CLAIM_DEFAULTS),
        }
        if outcome != brief.SOURCE_OUTCOME_ANSWERED:
            result["block"] = {
                "block_code": "TEST_BLOCK",
                "block_reason": "test block for non-successful vessel result",
            }
        if top_level_overrides:
            result.update(top_level_overrides)
        return result

    def write_v3_vessel_result(
        self,
        temp_root: Path,
        file_name: str,
        result: Mapping[str, Any],
    ) -> Path:
        output_path = temp_root / brief.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT / file_name
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return output_path

    @contextlib.contextmanager
    def patched_brief_root(self, temp_root: Path) -> Iterator[None]:
        with mock.patch.object(brief, "_repo_root", return_value=temp_root):
            yield

    def assert_refused(self, result: Mapping[str, Any], block_code: str) -> None:
        self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
        self.assertEqual(brief.OUTCOME_REFUSED, result["outcome"])
        self.assertEqual(block_code, result["block"]["block_code"])
        self.assertIsInstance(result["block"]["block_reason"], str)
        self.assertTrue(result["block"]["block_reason"])
        brief_output = result["brief_output"]
        self.assertIsNone(brief_output["brief_text"])
        self.assertEqual("bounded_derivative_vessel_result", brief_output["brief_basis"])
        self.assertIs(brief_output["source_remains_source"], True)
        self.assertIs(brief_output["vessel_output_remains_derivative"], True)
        self.assertIs(brief_output["brief_remains_derivative"], True)
        self.assert_non_claims_false(result)

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertEqual(set(brief.NON_CLAIM_DEFAULTS), set(non_claims))
        for key, value in non_claims.items():
            self.assertIs(value, False, key)

    def test_builds_brief_request_from_valid_v3_vessel_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact = self.build_v3_vessel_result()
            artifact_path = self.write_v3_vessel_result(temp_root, "selected.json", artifact)

            with self.patched_brief_root(temp_root):
                request = brief.build_operator_terminal_brief_request(
                    read_json(artifact_path),
                    artifact_path,
                )

            self.assertEqual(EXPECTED_REQUEST_KEYS, set(request))
            self.assertEqual(
                "what_stands_now_result_001__bounded_current_state_read_v3_answered__operator_terminal_brief_request",
                request["brief_request_id"],
            )
            self.assertEqual(brief.BRIEF_USE_CASE, request["brief_use_case"])
            self.assertEqual(brief.ADMITTED_USE_CLASS, request["admitted_use_class"])
            self.assertEqual(
                brief.ALLOWED_SOURCE_RESULT_FAMILY,
                request["allowed_source_result_family"],
            )
            self.assertEqual(
                "what_stands_now_result_001__bounded_current_state_read_v3_answered",
                request["selected_vessel_result_id"],
            )
            self.assertEqual(
                (brief.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT / "selected.json").as_posix(),
                request["selected_vessel_result_path"],
            )
            self.assertEqual("what_stands_now_result_001", request["selected_source_surface_id"])
            self.assertEqual("What stands now?", request["question"])
            self.assertEqual("bounded derivative read v3", request["derivative_answer"])
            self.assertIn("Do not widen source scope", request["brief_instructions"])
            self.assertIn("Keep the brief derivative", request["brief_instructions"])

    def test_resolves_success_from_explicit_path_and_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact = self.build_v3_vessel_result()
            artifact_path = self.write_v3_vessel_result(temp_root, "selected.json", artifact)

            with self.patched_brief_root(temp_root):
                explicit = brief.resolve_operator_terminal_brief(artifact_path)
                discovered = brief.resolve_operator_terminal_brief()

            for result in (explicit, discovered):
                self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
                self.assertEqual(brief.OUTCOME_BRIEF_RENDERED, result["outcome"])
                self.assertIsNone(result["block"]["block_code"])
                self.assertIsNone(result["block"]["block_reason"])

                selected = result["selected_vessel_result"]
                self.assertEqual(
                    (brief.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT / "selected.json").as_posix(),
                    selected["selected_vessel_result_path"],
                )
                self.assertEqual(
                    "what_stands_now_result_001__bounded_current_state_read_v3_answered",
                    selected["selected_vessel_result_id"],
                )
                self.assertEqual(
                    brief.ALLOWED_SOURCE_RESULT_FAMILY,
                    selected["selected_vessel_result_family"],
                )
                self.assertEqual(
                    brief.SOURCE_OUTCOME_ANSWERED,
                    selected["selected_vessel_result_outcome"],
                )
                self.assertEqual("what_stands_now_result_001", selected["selected_source_surface_id"])
                self.assertEqual(
                    brief.UPSTREAM_ALLOWED_SOURCE_FAMILY,
                    selected["selected_source_surface_family"],
                )

                brief_request = result["brief_request"]
                self.assertEqual(brief.BRIEF_USE_CASE, brief_request["brief_use_case"])
                self.assertEqual(brief.ADMITTED_USE_CLASS, brief_request["admitted_use_class"])
                self.assertEqual(
                    brief.ALLOWED_SOURCE_RESULT_FAMILY,
                    brief_request["allowed_source_result_family"],
                )
                self.assertEqual("What stands now?", brief_request["question"])

                brief_output = result["brief_output"]
                self.assertIsInstance(brief_output["brief_text"], str)
                self.assertTrue(brief_output["brief_text"])
                self.assertEqual(
                    "bounded_derivative_vessel_result",
                    brief_output["brief_basis"],
                )
                self.assertIs(brief_output["source_remains_source"], True)
                self.assertIs(brief_output["vessel_output_remains_derivative"], True)
                self.assertIs(brief_output["brief_remains_derivative"], True)
                self.assertLessEqual(brief_output["brief_text"].count("\n"), 4)
                self.assertIn("what_stands_now_result_001", brief_output["brief_text"])
                self.assertIn("What stands now?", brief_output["brief_text"])
                self.assertIn("bounded derivative read v3", brief_output["brief_text"])
                self.assertIn("bounded_derivative_vessel_result", brief_output["brief_text"])
                lowered = brief_output["brief_text"].lower()
                self.assertNotIn("authority:", lowered)
                self.assertNotIn("standing:", lowered)
                self.assertNotIn("rank:", lowered)
                self.assertNotIn("provenance:", lowered)

                metadata = result["operator_terminal_brief_metadata"]
                for key in (
                    "brief_result_id",
                    "brief_result_type",
                    "brief_result_version",
                    "generated_at",
                    "resolver_module",
                ):
                    self.assertIsInstance(metadata[key], str)
                    self.assertTrue(metadata[key])

                self.assert_non_claims_false(result)

                summary = brief.build_operator_terminal_brief_summary(result)
                self.assertEqual(
                    "what_stands_now_result_001__bounded_current_state_read_v3_answered",
                    summary["selected_vessel_result_id"],
                )
                self.assertEqual("what_stands_now_result_001", summary["selected_source_surface_id"])
                self.assertEqual("What stands now?", summary["question"])
                self.assertEqual(brief.OUTCOME_BRIEF_RENDERED, summary["outcome"])
                self.assertIsNone(summary["block_code"])
                self.assertIsNone(summary["block_reason"])

            self.assertEqual(
                explicit["selected_vessel_result"]["selected_vessel_result_id"],
                discovered["selected_vessel_result"]["selected_vessel_result_id"],
            )
            self.assertEqual(
                explicit["brief_output"]["brief_text"],
                discovered["brief_output"]["brief_text"],
            )

    def test_refuses_missing_unreadable_malformed_and_not_successful_results(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)

            missing_path = temp_root / brief.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT / "missing.json"
            unreadable_path = temp_root / brief.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT / "dir_as_path"
            unreadable_path.mkdir(parents=True)
            malformed_path = temp_root / brief.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT / "malformed.json"
            malformed_path.parent.mkdir(parents=True, exist_ok=True)
            malformed_path.write_text("{ not-json\n", encoding="utf-8")
            not_successful_path = self.write_v3_vessel_result(
                temp_root,
                "blocked.json",
                self.build_v3_vessel_result(outcome=brief.OUTCOME_REFUSED),
            )

            scenarios = [
                (missing_path, "MISSING_VESSEL_RESULT"),
                (unreadable_path, "VESSEL_RESULT_UNREADABLE"),
                (malformed_path, "VESSEL_RESULT_MALFORMED"),
                (not_successful_path, "VESSEL_RESULT_NOT_SUCCESSFUL"),
            ]

            with self.patched_brief_root(temp_root):
                for source_path, block_code in scenarios:
                    with self.subTest(source_path=str(source_path)):
                        result = brief.resolve_operator_terminal_brief(source_path)
                        self.assert_refused(result, block_code)

                        summary = brief.build_operator_terminal_brief_summary(result)
                        self.assertEqual(brief.OUTCOME_REFUSED, summary["outcome"])
                        self.assertEqual(block_code, summary["block_code"])
                        self.assertIsInstance(summary["block_reason"], str)

    def test_refuses_invalid_source_result_family_and_invalid_upstream_source_family(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            wrong_family_path = self.write_v3_vessel_result(
                temp_root,
                "wrong_family.json",
                self.build_v3_vessel_result(result_type="SOME_OTHER_RESULT_TYPE"),
            )
            wrong_upstream_selected_path = self.write_v3_vessel_result(
                temp_root,
                "wrong_upstream_selected.json",
                self.build_v3_vessel_result(source_family="current_state_query_result"),
            )
            wrong_upstream_request_path = self.write_v3_vessel_result(
                temp_root,
                "wrong_upstream_request.json",
                self.build_v3_vessel_result(
                    allowed_source_family="current_state_query_result"
                ),
            )

            with self.patched_brief_root(temp_root):
                wrong_family = brief.resolve_operator_terminal_brief(wrong_family_path)
                self.assert_refused(wrong_family, "INVALID_SOURCE_RESULT_FAMILY")

                wrong_upstream_selected = brief.resolve_operator_terminal_brief(
                    wrong_upstream_selected_path
                )
                self.assert_refused(
                    wrong_upstream_selected,
                    "INVALID_UPSTREAM_SOURCE_FAMILY",
                )

                wrong_upstream_request = brief.resolve_operator_terminal_brief(
                    wrong_upstream_request_path
                )
                self.assert_refused(
                    wrong_upstream_request,
                    "INVALID_UPSTREAM_SOURCE_FAMILY",
                )

    def test_refuses_widened_source_attempt_and_malformed_brief_packet(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_v3_vessel_result(
                temp_root,
                "selected.json",
                self.build_v3_vessel_result(),
            )

            with self.patched_brief_root(temp_root):
                packet = brief.build_operator_terminal_brief_request(
                    read_json(artifact_path),
                    artifact_path,
                )

                widened = dict(packet)
                widened["allowed_source_result_family"] = "some_other_vessel_family"
                with self.assertRaises(brief.OperatorTerminalBriefError) as raised:
                    brief._validate_brief_request(widened)
                self.assertEqual("WIDENED_SOURCE_ATTEMPT", raised.exception.block_code)

                malformed_packets = [
                    {"selected_vessel_result_id": None},
                    {"selected_source_surface_id": None},
                    {"question": None},
                    {"derivative_answer": None},
                    {"brief_request_id": 7},
                ]
                for overrides in malformed_packets:
                    malformed = dict(packet)
                    malformed.update(overrides)
                    with self.subTest(overrides=overrides):
                        with self.assertRaises(brief.OperatorTerminalBriefError) as malformed_raised:
                            brief._validate_brief_request(malformed)
                        self.assertEqual(
                            "MALFORMED_BRIEF_PACKET",
                            malformed_raised.exception.block_code,
                        )

                missing_lineage_path = self.write_v3_vessel_result(
                    temp_root,
                    "missing_lineage.json",
                    self.build_v3_vessel_result(
                        metadata_overrides={"vessel_result_id": None}
                    ),
                )
                refused = brief.resolve_operator_terminal_brief(missing_lineage_path)
                self.assert_refused(refused, "VESSEL_RESULT_MALFORMED")

    def test_refuses_brief_output_outside_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_v3_vessel_result(
                temp_root,
                "selected.json",
                self.build_v3_vessel_result(),
            )

            with self.patched_brief_root(temp_root):
                with mock.patch.object(
                    brief,
                    "_render_operator_terminal_brief",
                    side_effect=brief.OperatorTerminalBriefError(
                        "forced malformed brief output",
                        "BRIEF_OUTPUT_OUTSIDE_CONTRACT",
                    ),
                ):
                    result = brief.resolve_operator_terminal_brief(artifact_path)

            self.assert_refused(result, "BRIEF_OUTPUT_OUTSIDE_CONTRACT")

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_v3_vessel_result(
                temp_root,
                "selected.json",
                self.build_v3_vessel_result(),
            )
            before_digest = file_digest(artifact_path)
            before_payload = read_json(artifact_path)

            with self.patched_brief_root(temp_root):
                first = brief.resolve_operator_terminal_brief(artifact_path)
                second = brief.resolve_operator_terminal_brief(artifact_path)

            self.assertEqual(brief.OUTCOME_BRIEF_RENDERED, first["outcome"])
            self.assertEqual(brief.OUTCOME_BRIEF_RENDERED, second["outcome"])
            self.assertEqual(before_digest, file_digest(artifact_path))
            self.assertEqual(before_payload, read_json(artifact_path))
            self.assertFalse((temp_root / brief.OPERATOR_TERMINAL_BRIEF_ROOT).exists())

    def test_write_and_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_v3_vessel_result(
                temp_root,
                "selected.json",
                self.build_v3_vessel_result(),
            )

            with self.patched_brief_root(temp_root):
                result = brief.resolve_operator_terminal_brief(artifact_path)

                explicit_path = (
                    temp_root / "written" / "nested" / "operator_terminal_brief.json"
                )
                written_path = brief.write_operator_terminal_brief_result(
                    result,
                    explicit_path,
                )
                self.assertEqual(explicit_path, written_path)
                self.assertTrue(written_path.is_file())
                self.assertEqual(EXPECTED_RESULT_KEYS, set(read_json(written_path)))
                with self.assertRaises(FileExistsError):
                    brief.write_operator_terminal_brief_result(result, explicit_path)

                first_default = brief.write_operator_terminal_brief_result(result)
                second_default = brief.write_operator_terminal_brief_result(result)

            self.assertEqual(
                temp_root / brief.OPERATOR_TERMINAL_BRIEF_ROOT,
                first_default.parent,
            )
            self.assertTrue(
                first_default.name.endswith("__operator_terminal_brief_result.json")
            )
            self.assertIn("_001", second_default.stem)
            self.assertNotEqual(first_default, second_default)


if __name__ == "__main__":
    unittest.main()
