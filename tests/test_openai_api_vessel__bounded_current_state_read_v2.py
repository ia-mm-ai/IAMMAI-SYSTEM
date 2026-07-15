"""Bounded tests for the successor OpenAI API derivative vessel.

This suite exercises
``src/openai_api_vessel__bounded_current_state_read_v2.py`` as one
shell-owned, bounded derivative read over one already-standing current-state
surface. It keeps source-family scope brutally narrow and verifies that the
successor exists to harden the output-format boundary rather than widen vessel
doctrine, body law, or agent behavior.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
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


import openai_api_vessel__bounded_current_state_read_v2 as vessel
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver


EXPECTED_RESULT_KEYS = {
    "openai_api_derivative_vessel_v2_metadata",
    "selected_source_surface",
    "vessel_request",
    "api_runtime",
    "model_output",
    "outcome",
    "block",
    "derivative_answer",
    "vessel_summary",
    "non_claims",
}

EXPECTED_PACKET_KEYS = {
    "vessel_request_id",
    "vessel_use_case",
    "admitted_use_class",
    "allowed_source_family",
    "selected_source_surface_id",
    "selected_source_surface_path",
    "question",
    "bounded_source_payload",
    "instructions",
}

EXPECTED_PAYLOAD_KEYS = {
    "current_governing_source_run_path",
    "current_governing_ingress_run_path",
    "current_authority_artifact_path",
    "preserved_run_count",
    "application_basis",
    "delivery_basis",
    "answer_read_basis",
}

ORIGINAL_V1_OUTPUT_ROOT = Path(
    "artifacts/openai_api_derivative_vessel__bounded_current_state_read"
)


def read_json(path: Path | str) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object at {path}")
    return value


def file_digest(path: Path | str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class FakeResponse:
    def __init__(self, output_text: str) -> None:
        self.output_text = output_text


class StrictFakeOpenAI:
    output_text = json.dumps({"answer": "bounded derivative read v2"})
    create_error: Exception | None = None
    instances: list["StrictFakeOpenAI"] = []

    class _Responses:
        def __init__(self, client: "StrictFakeOpenAI") -> None:
            self.client = client

        def create(
            self,
            *,
            model: str,
            instructions: str,
            input: str,
            max_output_tokens: int,
            text: Mapping[str, Any] | None = None,
        ) -> FakeResponse:
            self.client.create_calls.append(
                {
                    "model": model,
                    "instructions": instructions,
                    "input": input,
                    "max_output_tokens": max_output_tokens,
                    "text": text,
                }
            )
            if type(self.client).create_error is not None:
                raise type(self.client).create_error
            return FakeResponse(type(self.client).output_text)

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.create_calls: list[dict[str, Any]] = []
        self.responses = self._Responses(self)
        type(self).instances.append(self)

    @classmethod
    def reset(cls) -> None:
        cls.output_text = json.dumps({"answer": "bounded derivative read v2"})
        cls.create_error = None
        cls.instances = []


class FallbackFakeOpenAI:
    output_text = json.dumps({"answer": "bounded derivative read v2"})
    create_error: Exception | None = None
    instances: list["FallbackFakeOpenAI"] = []

    class _Responses:
        def __init__(self, client: "FallbackFakeOpenAI") -> None:
            self.client = client

        def create(self, **kwargs: Any) -> FakeResponse:
            self.client.create_calls.append(kwargs)
            if type(self.client).create_error is not None:
                raise type(self.client).create_error
            return FakeResponse(type(self.client).output_text)

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.create_calls: list[dict[str, Any]] = []
        self.responses = self._Responses(self)
        type(self).instances.append(self)

    @classmethod
    def reset(cls) -> None:
        cls.output_text = json.dumps({"answer": "bounded derivative read v2"})
        cls.create_error = None
        cls.instances = []


class OpenAIBoundedCurrentStateReadV2Tests(unittest.TestCase):
    def build_what_stands_now_result(
        self,
        source_id: str = "what_stands_now_result_001",
        *,
        outcome: str = stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
        answer_overrides: Mapping[str, Any] | None = None,
        summary_overrides: Mapping[str, Any] | None = None,
        top_level_overrides: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        answer = {
            "current_governing_source_run_path": (
                "artifacts/integrity_host_v0_min_coexistence_source_runs/"
                "run_20260423T000000_000000Z"
            ),
            "current_governing_ingress_run_path": (
                "artifacts/integrity_host_v0_min_coexistence_receiving_ingress/"
                "run_20260423T000000_000000Z"
            ),
            "current_authority_artifact_path": (
                "artifacts/integrity_host_v0_min_coexistence_execution_authority/"
                "current_execution_authority.json"
            ),
            "current_family_packet_path": (
                "artifacts/integrity_host_v0_min_coexistence_run_family/"
                "current_run_family.json"
            ),
            "current_status_packet_path": (
                "artifacts/integrity_host_v0_min_coexistence_preserved_run_status/"
                "current_preserved_run_status.json"
            ),
            "current_governing_packet_path": (
                "artifacts/integrity_host_v0_min_coexistence_current_governing/"
                "current_governing_packet.json"
            ),
            "preserved_run_count": 2,
            "application_basis": "bounded application basis",
            "delivery_basis": "bounded delivery basis",
            "answer_read_basis": "bounded answer/read basis",
            "hidden_extra_context": "do not pass this through the vessel",
        }
        if answer_overrides:
            answer.update(answer_overrides)

        summary = {
            "what_stands_now_result_id": source_id,
            "outcome": outcome,
            "effective_current_governing_source_run_path": answer[
                "current_governing_source_run_path"
            ],
            "effective_current_governing_ingress_run_path": answer[
                "current_governing_ingress_run_path"
            ],
            "hidden_summary_context": "do not pass this through the vessel",
        }
        if summary_overrides:
            summary.update(summary_overrides)

        result = {
            "what_stands_now_metadata": {
                "what_stands_now_result_id": source_id,
                "what_stands_now_result_type": stand_resolver.WHAT_STANDS_NOW_RESULT_TYPE,
                "what_stands_now_result_version": (
                    stand_resolver.WHAT_STANDS_NOW_RESULT_VERSION
                ),
                "generated_at": "2026-04-23T00:00:00Z",
                "resolver_module": stand_resolver.RESOLVER_MODULE,
            },
            "selected_current_state_answer_read": {
                "current_state_answer_read_result_id": (
                    f"{source_id}__selected_answer_read"
                ),
                "current_state_answer_read_result_path": (
                    "artifacts/integrity_host_v0_min_coexistence_current_state_"
                    "answer_surface/current_state_answer_surface_result.json"
                ),
                "current_state_answer_read_result_outcome": "ANSWERED",
            },
            "what_stands_now_request": {
                "what_stands_now_request_id": f"{source_id}__request",
                "query_family": stand_resolver.QUERY_FAMILY,
                "requested_stand_now_fields": [
                    "current_governing_source_run_path",
                    "current_governing_ingress_run_path",
                    "current_authority_artifact_path",
                    "preserved_run_count",
                    "application_basis",
                    "delivery_basis",
                    "answer_read_basis",
                ],
                "query_basis": "bounded current-state vessel v2 test request",
            },
            "effective_stand_now_inputs": {
                "effective_authority_artifact_path": answer[
                    "current_authority_artifact_path"
                ],
                "effective_family_packet_path": answer["current_family_packet_path"],
                "effective_status_packet_path": answer["current_status_packet_path"],
                "effective_current_governing_packet_path": answer[
                    "current_governing_packet_path"
                ],
                "effective_source_run_path": answer[
                    "current_governing_source_run_path"
                ],
                "effective_ingress_run_path": answer[
                    "current_governing_ingress_run_path"
                ],
            },
            "checks": [
                {
                    "check_name": "bounded_current_state_surface_exists",
                    "passed": True,
                    "expected_posture": "bounded_answered_surface",
                    "actual_posture": "bounded_answered_surface",
                }
            ],
            "outcome": outcome,
            "block": {
                "block_code": None,
                "block_reason": None,
            },
            "what_stands_now_answer": answer,
            "what_stands_now_summary": summary,
            "non_claims": dict(stand_resolver.NON_CLAIM_DEFAULTS),
            "hidden_top_level_context": "do not pass this through the vessel",
        }
        if outcome != stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW:
            result["block"] = {
                "block_code": "TEST_BLOCK",
                "block_reason": "test block for non-answered artifact",
            }
        if top_level_overrides:
            result.update(top_level_overrides)
        return result

    def write_what_stands_now_result(
        self,
        temp_root: Path,
        file_name: str,
        result: Mapping[str, Any],
    ) -> Path:
        output_path = temp_root / vessel.CURRENT_STATE_WHAT_STANDS_NOW_ROOT / file_name
        stand_resolver.write_current_state_what_stands_now_result(result, output_path)
        return output_path

    @contextlib.contextmanager
    def patched_vessel_runtime(
        self,
        temp_root: Path,
        *,
        env: Mapping[str, str] | None,
        openai_value: Any = StrictFakeOpenAI,
        openai_import_error: Exception | None = None,
    ) -> Iterator[None]:
        StrictFakeOpenAI.reset()
        FallbackFakeOpenAI.reset()
        with contextlib.ExitStack() as stack:
            stack.enter_context(
                mock.patch.object(vessel, "_repo_root", return_value=temp_root)
            )
            stack.enter_context(mock.patch.dict(os.environ, env or {}, clear=True))
            stack.enter_context(mock.patch.object(vessel, "OpenAI", openai_value))
            if openai_import_error is not None:
                stack.enter_context(
                    mock.patch.object(
                        vessel,
                        "_OPENAI_IMPORT_ERROR",
                        openai_import_error,
                    )
                )
            yield

    def assert_refused(self, result: Mapping[str, Any], block_code: str) -> None:
        self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
        self.assertEqual(vessel.OUTCOME_REFUSED, result["outcome"])
        self.assertEqual(block_code, result["block"]["block_code"])
        self.assertIsInstance(result["block"]["block_reason"], str)
        self.assertTrue(result["block"]["block_reason"])
        derivative_answer = result["derivative_answer"]
        self.assertIsNone(derivative_answer["answer"])
        self.assertEqual("bounded_source_payload", derivative_answer["answer_basis"])
        self.assertIs(derivative_answer["source_remains_source"], True)
        self.assertIs(derivative_answer["model_output_remains_derivative"], True)
        self.assert_non_claims_false(result)

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertEqual(set(vessel.NON_CLAIM_DEFAULTS), set(non_claims))
        for key, value in non_claims.items():
            self.assertIs(value, False, key)

    def test_builds_bounded_packet_from_real_what_stands_now_shape(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            result = self.build_what_stands_now_result()
            artifact_path = self.write_what_stands_now_result(
                temp_root,
                "selected.json",
                result,
            )

            with mock.patch.object(vessel, "_repo_root", return_value=temp_root):
                packet = vessel.build_bounded_current_state_vessel_request(
                    read_json(artifact_path),
                    artifact_path,
                    "What stands now?",
                )

            self.assertEqual(EXPECTED_PACKET_KEYS, set(packet))
            self.assertEqual(
                "what_stands_now_result_001__bounded_current_state_read_request",
                packet["vessel_request_id"],
            )
            self.assertEqual(vessel.VESSEL_USE_CASE, packet["vessel_use_case"])
            self.assertEqual(vessel.SUPPORTED_USE_CLASS, packet["admitted_use_class"])
            self.assertEqual(
                vessel.ALLOWED_SOURCE_FAMILY,
                packet["allowed_source_family"],
            )
            self.assertEqual(
                "what_stands_now_result_001",
                packet["selected_source_surface_id"],
            )
            self.assertEqual(
                (vessel.CURRENT_STATE_WHAT_STANDS_NOW_ROOT / "selected.json").as_posix(),
                packet["selected_source_surface_path"],
            )
            self.assertEqual("What stands now?", packet["question"])
            self.assertEqual(EXPECTED_PAYLOAD_KEYS, set(packet["bounded_source_payload"]))
            self.assertEqual(
                "artifacts/integrity_host_v0_min_coexistence_source_runs/"
                "run_20260423T000000_000000Z",
                packet["bounded_source_payload"]["current_governing_source_run_path"],
            )
            self.assertEqual(
                "artifacts/integrity_host_v0_min_coexistence_receiving_ingress/"
                "run_20260423T000000_000000Z",
                packet["bounded_source_payload"]["current_governing_ingress_run_path"],
            )
            self.assertEqual(
                "artifacts/integrity_host_v0_min_coexistence_execution_authority/"
                "current_execution_authority.json",
                packet["bounded_source_payload"]["current_authority_artifact_path"],
            )
            self.assertEqual(2, packet["bounded_source_payload"]["preserved_run_count"])
            self.assertEqual(
                "bounded application basis",
                packet["bounded_source_payload"]["application_basis"],
            )
            self.assertEqual(
                "bounded delivery basis",
                packet["bounded_source_payload"]["delivery_basis"],
            )
            self.assertEqual(
                "bounded answer/read basis",
                packet["bounded_source_payload"]["answer_read_basis"],
            )
            self.assertNotIn("hidden_top_level_context", packet)
            self.assertNotIn("hidden_extra_context", packet["bounded_source_payload"])
            self.assertIn("Do not widen source scope", packet["instructions"])
            self.assertIn(
                "Do not assign rank, authority, provenance, status, or non-claims",
                packet["instructions"],
            )

    def test_refuses_source_family_widening_and_invalid_source_family(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            result = self.build_what_stands_now_result()
            artifact_path = self.write_what_stands_now_result(
                temp_root,
                "selected.json",
                result,
            )

            with mock.patch.object(vessel, "_repo_root", return_value=temp_root):
                packet = vessel.build_bounded_current_state_vessel_request(
                    read_json(artifact_path),
                    artifact_path,
                )
                packet["allowed_source_family"] = "current_state_query_result"
                with self.assertRaises(vessel.OpenAIDerivativeVesselV2Error) as raised:
                    vessel._validate_vessel_request(packet)
            self.assertEqual("WIDENED_SOURCE_ATTEMPT", raised.exception.block_code)

            invalid_path = temp_root / vessel.CURRENT_STATE_WHAT_STANDS_NOW_ROOT / "invalid.json"
            invalid_path.parent.mkdir(parents=True, exist_ok=True)
            invalid_path.write_text(
                json.dumps(
                    {
                        "answer_surface_metadata": {
                            "answer_surface_result_id": "not_what_stands_now"
                        },
                        "outcome": "ANSWERED",
                    },
                    indent=2,
                    sort_keys=True,
                )
                + "\n",
                encoding="utf-8",
            )
            with self.patched_vessel_runtime(
                temp_root,
                env={"OPENAI_API_KEY": "test-api-key"},
                openai_value=StrictFakeOpenAI,
            ):
                invalid_result = vessel.resolve_bounded_current_state_read(invalid_path)
            self.assert_refused(invalid_result, "INVALID_SOURCE_FAMILY")
            self.assertEqual(
                (vessel.CURRENT_STATE_WHAT_STANDS_NOW_ROOT / "invalid.json").as_posix(),
                invalid_result["selected_source_surface"]["selected_source_surface_path"],
            )
            self.assertIsNone(
                invalid_result["selected_source_surface"]["selected_source_surface_id"]
            )

    def test_strict_success_preserves_successor_metadata_and_shell_owned_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            self.write_what_stands_now_result(
                temp_root,
                "a.json",
                self.build_what_stands_now_result("what_stands_now_result_a"),
            )
            self.write_what_stands_now_result(
                temp_root,
                "z.json",
                self.build_what_stands_now_result("what_stands_now_result_z"),
            )
            self.write_what_stands_now_result(
                temp_root,
                "zz_blocked.json",
                self.build_what_stands_now_result(
                    "what_stands_now_result_blocked",
                    outcome=stand_resolver.OUTCOME_BLOCKED,
                ),
            )

            with self.patched_vessel_runtime(
                temp_root,
                env={
                    "OPENAI_API_KEY": "test-api-key",
                    "OPENAI_MODEL": "gpt-bounded-v2-test",
                },
                openai_value=StrictFakeOpenAI,
            ):
                result = vessel.resolve_bounded_current_state_read()

            self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
            self.assertEqual(vessel.OUTCOME_ANSWERED_DERIVATIVE_READ, result["outcome"])
            self.assertIsNone(result["block"]["block_code"])
            self.assertIsNone(result["block"]["block_reason"])
            self.assertEqual(
                (vessel.CURRENT_STATE_WHAT_STANDS_NOW_ROOT / "z.json").as_posix(),
                result["selected_source_surface"]["selected_source_surface_path"],
            )
            self.assertEqual(
                "what_stands_now_result_z",
                result["selected_source_surface"]["selected_source_surface_id"],
            )
            self.assertEqual(
                vessel.ALLOWED_SOURCE_FAMILY,
                result["selected_source_surface"]["selected_source_surface_family"],
            )
            self.assertEqual(
                stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
                result["selected_source_surface"]["selected_source_surface_outcome"],
            )
            self.assertEqual(
                "bounded derivative read v2",
                result["derivative_answer"]["answer"],
            )
            self.assertEqual(
                "bounded_source_payload",
                result["derivative_answer"]["answer_basis"],
            )
            self.assertIs(result["derivative_answer"]["source_remains_source"], True)
            self.assertIs(
                result["derivative_answer"]["model_output_remains_derivative"],
                True,
            )
            self.assert_non_claims_false(result)
            self.assertNotEqual(
                vessel.OPENAI_API_DERIVATIVE_VESSEL_V2_ROOT,
                ORIGINAL_V1_OUTPUT_ROOT,
            )

            metadata = result["openai_api_derivative_vessel_v2_metadata"]
            for key in (
                "vessel_result_id",
                "vessel_result_type",
                "vessel_result_version",
                "generated_at",
                "resolver_module",
                "successor_of_module",
            ):
                self.assertIsInstance(metadata[key], str)
                self.assertTrue(metadata[key])
            self.assertEqual(
                vessel.RESOLVER_MODULE,
                metadata["resolver_module"],
            )
            self.assertEqual(
                "openai_api_vessel__bounded_current_state_read",
                metadata["successor_of_module"],
            )

            api_runtime = result["api_runtime"]
            self.assertEqual("gpt-bounded-v2-test", api_runtime["model_name_used"])
            self.assertIs(api_runtime["explicit_model_env_override_used"], True)
            self.assertIs(api_runtime["local_setup_present"], True)
            self.assertIs(api_runtime["openai_package_present"], True)
            self.assertIs(api_runtime["api_key_present"], True)
            self.assertIs(api_runtime["strict_format_enforcement_used"], True)
            self.assertIs(api_runtime["fallback_extraction_path_used"], False)

            self.assertEqual(1, len(StrictFakeOpenAI.instances))
            client = StrictFakeOpenAI.instances[0]
            self.assertEqual("test-api-key", client.api_key)
            self.assertEqual(1, len(client.create_calls))
            call = client.create_calls[0]
            self.assertEqual("gpt-bounded-v2-test", call["model"])
            self.assertEqual(vessel.MAX_OUTPUT_TOKENS, call["max_output_tokens"])
            self.assertIn("Do not widen source scope", call["instructions"])
            self.assertIn(
                "Do not assign rank, authority, provenance, status, or non-claims",
                call["instructions"],
            )
            self.assertIsInstance(call["text"], dict)
            self.assertEqual(
                "json_schema",
                call["text"]["format"]["type"],
            )
            self.assertEqual(
                vessel.STRICT_OUTPUT_SCHEMA_NAME,
                call["text"]["format"]["name"],
            )
            self.assertIs(call["text"]["format"]["strict"], True)
            self.assertEqual(
                vessel.STRICT_OUTPUT_SCHEMA,
                call["text"]["format"]["schema"],
            )
            model_input = json.loads(call["input"])
            self.assertEqual(
                {
                    "vessel_use_case",
                    "admitted_use_class",
                    "allowed_source_family",
                    "selected_source_surface_id",
                    "selected_source_surface_path",
                    "question",
                    "bounded_source_payload",
                },
                set(model_input),
            )
            self.assertEqual(EXPECTED_PAYLOAD_KEYS, set(model_input["bounded_source_payload"]))
            self.assertNotIn("what_stands_now_metadata", model_input)
            self.assertNotIn("what_stands_now_answer", model_input)
            self.assertNotIn("hidden_top_level_context", call["input"])
            self.assertNotIn("hidden_extra_context", call["input"])

    def test_tiny_refusal_output_is_wrapped_as_shell_refusal(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_what_stands_now_result(
                temp_root,
                "selected.json",
                self.build_what_stands_now_result(),
            )
            StrictFakeOpenAI.output_text = json.dumps(
                {"refusal_code": vessel.MODEL_REFUSAL_CODE}
            )

            with self.patched_vessel_runtime(
                temp_root,
                env={"OPENAI_API_KEY": "test-api-key"},
                openai_value=StrictFakeOpenAI,
            ):
                StrictFakeOpenAI.output_text = json.dumps(
                    {"refusal_code": vessel.MODEL_REFUSAL_CODE}
                )
                result = vessel.resolve_bounded_current_state_read(artifact_path)

            self.assert_refused(result, "INSUFFICIENT_GROUNDING")
            self.assertEqual(
                vessel.MODEL_REFUSAL_CODE,
                result["model_output"]["refusal_code"],
            )
            self.assertEqual(
                {"refusal_code": vessel.MODEL_REFUSAL_CODE},
                result["model_output"]["parsed_output"],
            )

    def test_fallback_extracts_single_json_object_from_wrapped_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_what_stands_now_result(
                temp_root,
                "selected.json",
                self.build_what_stands_now_result("what_stands_now_result_wrapped"),
            )
            wrapped_output = (
                "Here is the bounded answer.\n"
                '{"answer":"wrapped derivative answer"}\n'
                "End."
            )

            with self.patched_vessel_runtime(
                temp_root,
                env={"OPENAI_API_KEY": "test-api-key"},
                openai_value=FallbackFakeOpenAI,
            ):
                FallbackFakeOpenAI.output_text = wrapped_output
                result = vessel.resolve_bounded_current_state_read(artifact_path)

            self.assertEqual(vessel.OUTCOME_ANSWERED_DERIVATIVE_READ, result["outcome"])
            self.assertEqual(
                "wrapped derivative answer",
                result["derivative_answer"]["answer"],
            )
            self.assertIs(
                result["api_runtime"]["strict_format_enforcement_used"],
                False,
            )
            self.assertIs(
                result["api_runtime"]["fallback_extraction_path_used"],
                True,
            )
            self.assertEqual(
                wrapped_output,
                result["model_output"]["raw_output_text"],
            )
            self.assertEqual(
                {"answer": "wrapped derivative answer"},
                result["model_output"]["parsed_output"],
            )
            self.assertEqual(1, len(FallbackFakeOpenAI.instances))
            self.assertEqual(1, len(FallbackFakeOpenAI.instances[0].create_calls))
            self.assertNotIn("text", FallbackFakeOpenAI.instances[0].create_calls[0])

    def test_malformed_and_widened_model_outputs_are_refused(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_what_stands_now_result(
                temp_root,
                "selected.json",
                self.build_what_stands_now_result(),
            )

            scenarios = [
                ("not-json", "MODEL_OUTPUT_MALFORMED"),
                (json.dumps({}), "MODEL_OUTPUT_OUTSIDE_CONTRACT"),
                (json.dumps({"answer": 7}), "MODEL_OUTPUT_OUTSIDE_CONTRACT"),
                (
                    json.dumps({"answer": "ok", "rank": "self-assigned"}),
                    "MODEL_OUTPUT_OUTSIDE_CONTRACT",
                ),
                (
                    'prefix {"answer":"ok","extra":"forbidden"} suffix',
                    "MODEL_OUTPUT_OUTSIDE_CONTRACT",
                ),
                (
                    '{"answer":"one"} {"answer":"two"}',
                    "MODEL_OUTPUT_MALFORMED",
                ),
            ]

            for output_text, expected_block_code in scenarios:
                with self.subTest(output_text=output_text):
                    with self.patched_vessel_runtime(
                        temp_root,
                        env={"OPENAI_API_KEY": "test-api-key"},
                        openai_value=FallbackFakeOpenAI,
                    ):
                        FallbackFakeOpenAI.output_text = output_text
                        result = vessel.resolve_bounded_current_state_read(artifact_path)
                    self.assert_refused(result, expected_block_code)

    def test_missing_local_setup_and_api_failure_are_refused_explicitly(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_what_stands_now_result(
                temp_root,
                "selected.json",
                self.build_what_stands_now_result(),
            )

            with self.patched_vessel_runtime(
                temp_root,
                env={},
                openai_value=StrictFakeOpenAI,
            ):
                missing_key = vessel.resolve_bounded_current_state_read(artifact_path)
            self.assert_refused(missing_key, "LOCAL_SETUP_FAILURE")
            self.assertIs(missing_key["api_runtime"]["api_key_present"], False)

            with self.patched_vessel_runtime(
                temp_root,
                env={"OPENAI_API_KEY": "test-api-key"},
                openai_value=None,
                openai_import_error=ImportError("openai missing for test"),
            ):
                missing_package = vessel.resolve_bounded_current_state_read(artifact_path)
            self.assert_refused(missing_package, "LOCAL_SETUP_FAILURE")
            self.assertIs(
                missing_package["api_runtime"]["openai_package_present"],
                False,
            )

            with self.patched_vessel_runtime(
                temp_root,
                env={"OPENAI_API_KEY": "test-api-key"},
                openai_value=StrictFakeOpenAI,
            ):
                StrictFakeOpenAI.create_error = RuntimeError("api exploded")
                api_failure = vessel.resolve_bounded_current_state_read(artifact_path)
            self.assert_refused(api_failure, "API_CALL_FAILURE")

    def test_summary_write_helpers_and_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_what_stands_now_result(
                temp_root,
                "selected.json",
                self.build_what_stands_now_result("what_stands_now_result_write"),
            )

            with self.patched_vessel_runtime(
                temp_root,
                env={"OPENAI_API_KEY": "test-api-key"},
                openai_value=StrictFakeOpenAI,
            ):
                result = vessel.resolve_bounded_current_state_read(artifact_path)

            summary = vessel.build_bounded_current_state_vessel_summary(result)
            self.assertEqual(
                "what_stands_now_result_write",
                summary["selected_source_surface_id"],
            )
            self.assertEqual(
                vessel.ALLOWED_SOURCE_FAMILY,
                summary["allowed_source_family"],
            )
            self.assertEqual("What stands now?", summary["question"])
            self.assertEqual(
                vessel.OUTCOME_ANSWERED_DERIVATIVE_READ,
                summary["outcome"],
            )

            explicit_path = temp_root / "written" / "nested" / "vessel_v2_result.json"
            written_path = vessel.write_bounded_current_state_vessel_result(
                result,
                explicit_path,
            )
            self.assertEqual(explicit_path, written_path)
            self.assertTrue(written_path.is_file())
            self.assertEqual(EXPECTED_RESULT_KEYS, set(read_json(written_path)))
            with self.assertRaises(FileExistsError):
                vessel.write_bounded_current_state_vessel_result(result, explicit_path)

            with mock.patch.object(vessel, "_repo_root", return_value=temp_root):
                first_default = vessel.write_bounded_current_state_vessel_result(result)
                second_default = vessel.write_bounded_current_state_vessel_result(result)
            self.assertEqual(
                temp_root / vessel.OPENAI_API_DERIVATIVE_VESSEL_V2_ROOT,
                first_default.parent,
            )
            self.assertTrue(
                first_default.name.endswith(
                    "__bounded_current_state_vessel_v2_result.json"
                )
            )
            self.assertIn("_001", second_default.stem)
            self.assertNotEqual(first_default, second_default)
            self.assertFalse((temp_root / ORIGINAL_V1_OUTPUT_ROOT).exists())

    def test_vessel_resolution_does_not_mutate_sources_or_v1_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            artifact_path = self.write_what_stands_now_result(
                temp_root,
                "selected.json",
                self.build_what_stands_now_result("what_stands_now_result_mutation"),
            )
            before_digest = file_digest(artifact_path)
            before_payload = read_json(artifact_path)

            with self.patched_vessel_runtime(
                temp_root,
                env={"OPENAI_API_KEY": "test-api-key"},
                openai_value=StrictFakeOpenAI,
            ):
                first = vessel.resolve_bounded_current_state_read(artifact_path)
                second = vessel.resolve_bounded_current_state_read(artifact_path)

            self.assertEqual(vessel.OUTCOME_ANSWERED_DERIVATIVE_READ, first["outcome"])
            self.assertEqual(vessel.OUTCOME_ANSWERED_DERIVATIVE_READ, second["outcome"])
            self.assertEqual(before_digest, file_digest(artifact_path))
            self.assertEqual(before_payload, read_json(artifact_path))
            self.assertFalse((temp_root / vessel.OPENAI_API_DERIVATIVE_VESSEL_V2_ROOT).exists())
            self.assertFalse((temp_root / ORIGINAL_V1_OUTPUT_ROOT).exists())


if __name__ == "__main__":
    unittest.main()
