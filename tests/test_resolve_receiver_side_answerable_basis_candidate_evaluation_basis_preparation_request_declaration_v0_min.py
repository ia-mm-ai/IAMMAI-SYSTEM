"""Bounded tests for one preparation-request readiness declaration.

The suite supplies only temporary structural fixtures.  It verifies that a
complete request can become ready for one later issuance without creating an
issuance, delivery, preparer identity, response, declaration, evaluation, or
downstream result.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min as resolver


class ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinTests(
    unittest.TestCase
):
    """Verify readiness only for one separately prepared future request."""

    PREPARER_SENTINEL = "SYNTHETIC_PREPARER_ADDRESS_MUST_NOT_RETURN"
    ROLE_SENTINEL = "SYNTHETIC_PREPARER_ROLE_MUST_NOT_RETURN"
    CANDIDATE_SENTINEL = "SYNTHETIC_CANDIDATE_MATERIAL_MUST_NOT_RETURN"
    SOURCE_SENTINEL = "SYNTHETIC_SOURCE_BODY_MUST_NOT_RETURN"
    STATEMENT_SENTINEL = "SYNTHETIC_REQUEST_STATEMENT_MUST_NOT_RETURN"
    NON_MEANING_SENTINEL = "SYNTHETIC_REQUEST_NON_MEANING_MUST_NOT_RETURN"

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        prefix = f"{index:03d}_" if index is not None else ""
        return f"{prefix}{safe}.json"

    def _clone(self, value: object) -> object:
        return copy.deepcopy(value)

    def _write_text(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"temporary fixture file path is a directory: {path}")
        path.write_text(text, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: object) -> Path:
        return self._write_text(path, json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n")

    def _request_values(self) -> dict[str, str]:
        return {
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_id": resolver.REQUEST_ID,
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_type": resolver.REQUEST_TYPE,
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_version": resolver.REQUEST_VERSION,
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_scope": resolver.REQUEST_SCOPE,
            "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_type": resolver.CANDIDATE_TYPE,
            "receiver_side_answerable_basis_candidate_scope": resolver.CANDIDATE_SCOPE,
            "selected_candidate_reception_operation_id": resolver.SELECTED_RECEPTION_OPERATION_ID,
            "selected_candidate_evaluation_boundary_id": resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            "selected_candidate_evaluation_operation_id": resolver.SELECTED_EVALUATION_OPERATION_ID,
            "selected_evaluation_basis_declaration_id": resolver.SELECTED_EVALUATION_BASIS_DECLARATION_ID,
            "required_response_declaration_id": resolver.REQUIRED_RESPONSE_DECLARATION_ID,
            "required_response_declaration_type": resolver.REQUIRED_RESPONSE_DECLARATION_TYPE,
            "required_response_declaration_version": resolver.REQUIRED_RESPONSE_DECLARATION_VERSION,
            "required_response_declaration_scope": resolver.REQUIRED_RESPONSE_DECLARATION_SCOPE,
            "admissible_future_route": resolver.ADMISSIBLE_FUTURE_ROUTE,
        }

    def _synthetic_preparation_request_specification(self) -> str:
        markers = [
            "# Receiver-Side Answerable Basis Candidate Evaluation Basis Preparation Request Declaration V0 Minimum Specification",
            "Response remains optional.",
            "preparation_request_single_use = true",
            "one bounded preparation-request declaration",
            "ready for issuance is not issuance",
            "no delivery, reception, response, declaration, or evaluation created",
            "preparer reference is not identity, authority, standing, or custody",
        ]
        for marker_class in resolver.PREPARATION_REQUEST_SPEC_MARKER_CLASSES.values():
            markers.extend(marker_class)
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def _synthetic_declaration_terminal_summary(self) -> str:
        markers = [
            "# Receiver-Side Answerable Basis Candidate Evaluation Basis Declaration Terminal Summary V0",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_REQUIRES_DECLARATION_MATERIAL",
            "declaration_result = REQUIRES_DECLARATION_MATERIAL",
            "No declaration material",
            "dimension_record_count = 0",
        ]
        for marker_class in resolver.DECLARATION_SUMMARY_MARKER_CLASSES.values():
            markers.extend(marker_class)
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def _synthetic_declaration_waiting_artifact(self) -> dict[str, object]:
        declaration = {
            "declaration_id": resolver.REQUIRED_RESPONSE_DECLARATION_ID,
            "declaration_type": resolver.REQUIRED_RESPONSE_DECLARATION_TYPE,
            "declaration_version": resolver.REQUIRED_RESPONSE_DECLARATION_VERSION,
            "declaration_scope": resolver.REQUIRED_RESPONSE_DECLARATION_SCOPE,
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result": "REQUIRES_DECLARATION_MATERIAL",
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result_recorded": True,
            "declaration_material_supplied": False,
            "declaration_material_received": False,
            "declaration_material_recorded": False,
            "evaluation_basis_declaration_complete": False,
            "evaluation_basis_declaration_ready_for_supply": False,
            "evaluation_basis_declaration_separately_supplied": False,
            "evaluation_basis_declaration_admitted_by_operation": False,
            "dimension_record_count": 0,
            "evaluation_basis_declaration_resolver_generated": False,
            "evaluation_basis_declaration_candidate_material_reused_as_basis": False,
            "evaluation_basis_declaration_repository_access_treated_as_basis": False,
            "candidate_evaluation_authorized": False,
            "candidate_evaluation_completed": False,
            "candidate_sufficiency_created": False,
            "receiver_attestation_created": False,
            "receiver_attestation_supported": False,
            "receiver_answerable_receipt_present": False,
            "presence_supported": False,
            "presence_authorized": False,
            "presence_established": False,
            "presence_recorded": False,
            "second_candidate_basis_created": False,
            "repeated_supply_permission_created": False,
            "reusable_basis_route_created": False,
            "follow_on_work_authorized": False,
        }
        declared = {
            "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_type": resolver.CANDIDATE_TYPE,
            "receiver_side_answerable_basis_candidate_scope": resolver.CANDIDATE_SCOPE,
            "selected_candidate_reception_operation_id": resolver.SELECTED_RECEPTION_OPERATION_ID,
            "selected_candidate_evaluation_boundary_id": resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            "selected_candidate_evaluation_operation_id": resolver.SELECTED_EVALUATION_OPERATION_ID,
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_id": resolver.REQUIRED_RESPONSE_DECLARATION_ID,
        }
        return {
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_REQUIRES_DECLARATION_MATERIAL",
            "failed_check_count": 0,
            "declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_basis": declared,
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration": declaration,
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_material": {
                "dimension_record_ids": []
            },
            "upstream_basis": {"waiting_operation_identity": {"waiting_only": True}},
        }

    def _fixture_paths(
        self,
        root: Path,
        *,
        include_specification: bool = True,
        include_summary: bool = True,
        include_artifact: bool = True,
    ) -> dict[str, Path]:
        paths = {
            "specification": root / resolver.PREPARATION_REQUEST_SPEC_RELATIVE_PATH,
            "summary": root / resolver.DECLARATION_TERMINAL_SUMMARY_RELATIVE_PATH,
            "artifact": root / resolver.DECLARATION_WAITING_RESULT_RELATIVE_PATH,
        }
        if include_specification:
            self._write_text(paths["specification"], self._synthetic_preparation_request_specification())
        if include_summary:
            self._write_text(paths["summary"], self._synthetic_declaration_terminal_summary())
        if include_artifact:
            self._write_json(paths["artifact"], self._synthetic_declaration_waiting_artifact())
        return paths

    def _request_non_claims(self) -> dict[str, bool]:
        return {key: False for key in resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS}

    def _declared_non_claims(self) -> dict[str, bool]:
        return {key: False for key in resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS}

    def _complete_material(self) -> dict[str, object]:
        return {
            **self._request_values(),
            "intended_preparer_reference": self.PREPARER_SENTINEL,
            "intended_preparer_role_declaration": self.ROLE_SENTINEL,
            "intended_preparer_relation_to_candidate_declaration": (
                "identity established only as free-form wording; " + self.CANDIDATE_SENTINEL
            ),
            "intended_preparer_relation_to_source_body_declaration": (
                "separate custody established only as free-form wording; " + self.SOURCE_SENTINEL
            ),
            "intended_preparer_custody_posture_declaration": "independent evaluator authority standing",
            "request_origin_reference": "synthetic-request-origin",
            "request_timestamp": "2026-07-28T00:00:00Z",
            "required_response_declaration_reference": "synthetic-required-response-reference",
            "response_shape_requirements": {
                "opaque_response_shape": "mandatory response SATISFIED attestation receipt presence",
            },
            "required_response_dimension_ids": list(resolver.REQUIRED_RESPONSE_DIMENSION_IDS),
            "request_statement": {"opaque_statement": self.STATEMENT_SENTINEL},
            "request_non_meaning": {"opaque_non_meaning": self.NON_MEANING_SENTINEL},
            "request_non_claims": self._request_non_claims(),
            "response_optional": True,
            "preparation_request_single_use": True,
        }

    def _base_request(self, material: dict[str, object] | None = None) -> dict[str, object]:
        return resolver.build_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_request(
            preparation_request_material=material,
            preparation_request_material_supplied=material is not None,
            declared_non_claims=self._declared_non_claims(),
        )

    def _resolve_at(self, root: Path, request: object | None = None) -> dict[str, object]:
        with patch.object(resolver, "REPO_ROOT", root):
            return resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min(request)

    def _resolve_synthetic(self, root: Path, request: object | None = None) -> dict[str, object]:
        self._fixture_paths(root)
        return self._resolve_at(root, request)

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def failed_check_count(self, result: dict[str, object]) -> int:
        value = result.get("failed_check_count")
        self.assertIsInstance(value, int)
        return value

    def passed_check_count(self, result: dict[str, object]) -> int:
        value = result.get("passed_check_count")
        self.assertIsInstance(value, int)
        return value

    def declaration(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration")
        self.assertIsInstance(value, dict)
        return value

    def material_metadata(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_material")
        self.assertIsInstance(value, dict)
        return value

    def summary(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_summary")
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        value = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_checks")
        self.assertIsInstance(value, list)
        for item in value:
            self.assertIsInstance(item, dict)
        return value

    def assert_not_blocked(self, result: dict[str, object]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_all_emitted_codes_public(self, result: dict[str, object]) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if value is not None:
                    self.assertIn(value, resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIsInstance(non_claims[key], bool, key)

    def assert_request_non_claims_false(self, material: dict[str, object]) -> None:
        value = material.get("request_non_claims")
        self.assertIsInstance(value, dict)
        for key in resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(value.get(key), False, key)

    def assert_standing_locks(self, result: dict[str, object]) -> None:
        declaration = self.declaration(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(declaration.get(key), False, key)
        detail = result.get("request_result_detail")
        self.assertIsInstance(detail, dict)
        for key in (
            "request_recorded",
            "request_issued",
            "request_delivered",
            "request_received_by_preparer",
            "request_exhausted",
            "response_exists",
            "operation_invocation_exists",
            "dimension_result_exists",
        ):
            self.assertIs(detail.get(key), False, key)
        self.assert_canonical_non_claims(result)

    def assert_blocked_public(self, result: dict[str, object], expected: str | None = None) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected is not None:
            self.assertEqual(code, expected)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_standing_locks(result)
        self.assertIs(self.declaration(result).get("preparation_request_ready_for_issuance"), False)

    def assert_waiting(self, result: dict[str, object], missing: str | None = None) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_REQUEST_MATERIAL)
        self.assertEqual(
            self.declaration(result).get("request_result"),
            resolver.REQUEST_RESULT_REQUIRES_REQUEST_MATERIAL,
        )
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assert_standing_locks(result)
        self.assertIs(self.declaration(result).get("preparation_request_ready_for_issuance"), False)
        missing_values = result.get("missing_or_incomplete_request_material")
        self.assertIsInstance(missing_values, list)
        if missing is not None:
            self.assertIn(missing, missing_values)

    def assert_ready(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(
            self.declaration(result).get("request_result"),
            resolver.REQUEST_RESULT_READY_FOR_ISSUANCE,
        )
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        declaration = self.declaration(result)
        for key in (
            "preparation_request_declaration_recorded",
            "preparation_request_declaration_result_recorded",
            "preparation_request_material_supplied",
            "preparation_request_material_received",
            "preparation_request_material_recorded",
            "preparation_request_declaration_complete",
            "all_selected_identities_match",
            "intended_preparer_reference_supplied",
            "intended_preparer_role_declared",
            "intended_preparer_relation_to_candidate_declared",
            "intended_preparer_relation_to_source_body_declared",
            "intended_preparer_custody_posture_declared",
            "request_origin_reference_supplied",
            "request_timestamp_supplied",
            "required_response_declaration_reference_supplied",
            "exact_eight_dimension_response_scope",
            "request_non_claims_false",
            "response_optional",
            "preparation_request_single_use",
            "preparation_request_ready_for_issuance",
        ):
            self.assertIs(declaration.get(key), True, key)
        self.assert_standing_locks(result)

    def assert_material_omitted(self, result: dict[str, object]) -> None:
        rendered = json.dumps(result, sort_keys=True)
        for sentinel in (
            self.PREPARER_SENTINEL,
            self.ROLE_SENTINEL,
            self.CANDIDATE_SENTINEL,
            self.SOURCE_SENTINEL,
            self.STATEMENT_SENTINEL,
            self.NON_MEANING_SENTINEL,
        ):
            self.assertNotIn(sentinel, rendered)
        for key in (
            "preparation_request_material",
            "intended_preparer_reference",
            "intended_preparer_role_declaration",
            "intended_preparer_relation_to_candidate_declaration",
            "intended_preparer_relation_to_source_body_declaration",
            "intended_preparer_custody_posture_declaration",
            "request_origin_reference",
            "request_timestamp",
            "required_response_declaration_reference",
            "request_statement",
            "request_non_meaning",
            "candidate_material",
            "declaration_response",
        ):
            self.assertNotIn(f'"{key}"', rendered, key)
        metadata = self.material_metadata(result)
        self.assertIs(metadata.get("complete_preparation_request_material_omitted_from_result"), True)
        self.assertIs(metadata.get("sensitive_preparer_address_declarations_omitted_from_result"), True)
        self.assertIs(metadata.get("candidate_material_omitted_from_result"), True)

    def assert_result_structure(self, result: dict[str, object]) -> None:
        required = (
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_metadata",
            "declared_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_basis",
            "upstream_basis",
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration",
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_material",
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_checks",
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_statement",
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_non_meaning",
            "request_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "missing_or_incomplete_request_material",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_summary",
            "resolver_module",
            "result_version",
        )
        for key in required:
            self.assertIn(key, result)
        declaration = self.declaration(result)
        for wrapper_key in (
            "outcome",
            "block",
            "non_claims",
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_checks",
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_summary",
            "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_metadata",
        ):
            self.assertNotIn(wrapper_key, declaration)

    def test_public_api_constants_and_non_claim_contracts(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min",
            "resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_from_path",
            "write_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_result",
            "build_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_summary",
            "build_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_request",
            "build_declared_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min",
        )
        self.assertEqual(resolver.MAX_REQUIRED_RESPONSE_DIMENSIONS, 8)
        self.assertEqual(len(resolver.REQUIRED_RESPONSE_DIMENSION_IDS), 8)
        self.assertIn(resolver.OUTCOME_RECORDED, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_REQUIRES_REQUEST_MATERIAL, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_BLOCKED, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_NOT_RECORDED, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.REQUEST_RESULT_READY_FOR_ISSUANCE, resolver.REQUEST_RESULT_FAMILY)
        self.assertIn(resolver.REQUEST_RESULT_REQUIRES_REQUEST_MATERIAL, resolver.REQUEST_RESULT_FAMILY)
        self.assertIn(resolver.REQUEST_RESULT_NOT_EVALUATED, resolver.REQUEST_RESULT_FAMILY)
        for maximum_name in (
            "MAX_SERIALIZED_PREPARATION_REQUEST_MATERIAL_SIZE",
            "MAX_INTENDED_PREPARER_REFERENCE_LENGTH",
            "MAX_INTENDED_PREPARER_ROLE_DECLARATION_LENGTH",
            "MAX_INTENDED_PREPARER_CANDIDATE_RELATION_DECLARATION_LENGTH",
            "MAX_INTENDED_PREPARER_SOURCE_BODY_RELATION_DECLARATION_LENGTH",
            "MAX_INTENDED_PREPARER_CUSTODY_POSTURE_DECLARATION_LENGTH",
            "MAX_REQUEST_ORIGIN_REFERENCE_LENGTH",
            "MAX_REQUEST_TIMESTAMP_LENGTH",
            "MAX_REQUIRED_RESPONSE_DECLARATION_REFERENCE_LENGTH",
            "MAX_SERIALIZED_RESPONSE_SHAPE_REQUIREMENTS_SIZE",
            "MAX_SERIALIZED_REQUEST_STATEMENT_SIZE",
            "MAX_SERIALIZED_REQUEST_NON_MEANING_SIZE",
        ):
            self.assertIsInstance(getattr(resolver, maximum_name), int)
            self.assertGreater(getattr(resolver, maximum_name), 0)
        for key in (
            "preparation_request_recorded",
            "preparation_request_issued",
            "preparation_request_delivered",
            "preparation_request_received_by_preparer",
            "preparation_request_exhausted",
            "preparer_response_required",
            "declaration_response_recorded",
            "candidate_evaluation_completed",
            "follow_on_work_authorized",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "preparer_identity_established",
            "preparer_role_admitted",
            "declaration_created",
            "dimension_results_created",
            "reusable_request_route_created",
        ):
            self.assertIn(key, resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS)
        for key in resolver.PROHIBITED_REQUEST_FLAGS:
            self.assertIn(resolver.PROHIBITED_REQUEST_FLAGS[key], resolver.BLOCK_CODES)
        for code in (
            "PREPARATION_REQUEST_RESPONSE_NOT_OPTIONAL",
            "PREPARATION_REQUEST_NOT_SINGLE_USE",
            "PREPARATION_REQUEST_RESPONSE_DIMENSION_SCOPE_MISMATCH",
            "PREPARATION_REQUEST_NON_CLAIM_MISSING_OR_FLIPPED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "RESULT_POSTURE_PRECLAIMED",
            "WRITE_REFUSED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        request = self._base_request()
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertIs(request["preparation_request_material_supplied"], False)
        self.assertIsNone(request["preparation_request_material"])
        self.assertEqual(request["declared_non_claims"], self._declared_non_claims())

    def test_default_waiting_and_optional_live_waiting(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = self._resolve_synthetic(Path(temporary))
        self.assert_waiting(result, "preparation_request_material")
        self.assert_result_structure(result)
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        self.assertEqual(result.get("result_version"), resolver.RESULT_VERSION)
        metadata = self.material_metadata(result)
        self.assertIs(metadata.get("preparation_request_material_present"), False)
        self.assertEqual(metadata.get("required_response_dimension_ids"), [])

        live_paths = (
            REPO_ROOT / resolver.PREPARATION_REQUEST_SPEC_RELATIVE_PATH,
            REPO_ROOT / resolver.DECLARATION_TERMINAL_SUMMARY_RELATIVE_PATH,
            REPO_ROOT / resolver.DECLARATION_WAITING_RESULT_RELATIVE_PATH,
        )
        if not all(path.is_file() for path in live_paths):
            self.skipTest("default live preparation-request governing artifacts are not all present")
        live = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min()
        self.assert_waiting(live, "preparation_request_material")

    def test_complete_request_ready_is_not_occurrence_and_omits_material(self) -> None:
        material = self._complete_material()
        request = self._base_request(material)
        before_material = self._clone(material)
        before_request = self._clone(request)
        with tempfile.TemporaryDirectory() as temporary:
            result = self._resolve_synthetic(Path(temporary), request)
        self.assert_ready(result)
        self.assert_result_structure(result)
        self.assert_material_omitted(result)
        self.assertEqual(material, before_material)
        self.assertEqual(request, before_request)
        metadata = self.material_metadata(result)
        self.assertEqual(metadata.get("required_response_dimension_ids"), list(resolver.REQUIRED_RESPONSE_DIMENSION_IDS))
        self.assertEqual(metadata.get("response_shape_requirement_key_names"), ["opaque_response_shape"])
        self.assertIs(metadata.get("request_non_claims_validated"), True)
        self.assertIs(metadata.get("response_optional"), True)
        self.assertIs(metadata.get("preparation_request_single_use"), True)
        summary = self.summary(result)
        self.assertEqual(summary.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(summary.get("request_result"), resolver.REQUEST_RESULT_READY_FOR_ISSUANCE)
        self.assertEqual(summary.get("required_response_dimension_ids"), list(resolver.REQUIRED_RESPONSE_DIMENSION_IDS))
        self.assertIs(summary.get("non_claims_canonical_false"), True)

    def test_partial_material_optional_single_use_and_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            required_keys = tuple(sorted(resolver.REQUIRED_PREPARATION_REQUEST_MATERIAL_KEYS))
            for key in required_keys:
                with self.subTest(missing_field=key):
                    material = self._complete_material()
                    material.pop(key)
                    result = self._resolve_at(root, self._base_request(material))
                    self.assert_waiting(result, f"preparation_request_field:{key}")

            for value in (False, 1, 0, None, "true"):
                with self.subTest(response_optional=repr(value)):
                    material = self._complete_material()
                    material["response_optional"] = value
                    self.assert_blocked_public(
                        self._resolve_at(root, self._base_request(material)),
                        "PREPARATION_REQUEST_RESPONSE_NOT_OPTIONAL",
                    )
            for value in (False, 1, 0, None, "true"):
                with self.subTest(single_use=repr(value)):
                    material = self._complete_material()
                    material["preparation_request_single_use"] = value
                    self.assert_blocked_public(
                        self._resolve_at(root, self._base_request(material)),
                        "PREPARATION_REQUEST_NOT_SINGLE_USE",
                    )
            tuple_material = self._complete_material()
            tuple_material["required_response_dimension_ids"] = resolver.REQUIRED_RESPONSE_DIMENSION_IDS
            self.assert_ready(self._resolve_at(root, self._base_request(tuple_material)))
            malformed_dimensions = (
                list(resolver.REQUIRED_RESPONSE_DIMENSION_IDS[:-1]),
                list(resolver.REQUIRED_RESPONSE_DIMENSION_IDS) + ["extra"],
                [resolver.REQUIRED_RESPONSE_DIMENSION_IDS[0]] * 8,
                list(reversed(resolver.REQUIRED_RESPONSE_DIMENSION_IDS)),
                ["wrong"] + list(resolver.REQUIRED_RESPONSE_DIMENSION_IDS[1:]),
                {"not": "a sequence"},
                "not-a-sequence",
                [],
            )
            for dimensions in malformed_dimensions:
                with self.subTest(dimensions=repr(dimensions)):
                    material = self._complete_material()
                    material["required_response_dimension_ids"] = dimensions
                    self.assert_blocked_public(
                        self._resolve_at(root, self._base_request(material)),
                        "PREPARATION_REQUEST_RESPONSE_DIMENSION_SCOPE_MISMATCH",
                    )

    def test_identity_field_shapes_freeform_opacity_and_limits(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            for field in self._request_values():
                with self.subTest(identity=field):
                    material = self._complete_material()
                    material[field] = "wrong-selected-identity"
                    self.assert_blocked_public(
                        self._resolve_at(root, self._base_request(material)),
                        "PREPARATION_REQUEST_SELECTED_IDENTITY_MISMATCH",
                    )
            malformed = {
                "material_not_mapping": (None, "PREPARATION_REQUEST_MATERIAL_NOT_MAPPING"),
                "unknown_top_level": ("unknown", "PREPARATION_REQUEST_TOP_LEVEL_FIELD_UNKNOWN"),
                "non_string_preparer": ("intended_preparer_reference", "PREPARATION_REQUEST_FIELD_MALFORMED"),
                "non_string_role": ("intended_preparer_role_declaration", "PREPARATION_REQUEST_FIELD_MALFORMED"),
                "non_mapping_shape": ("response_shape_requirements", "PREPARATION_REQUEST_FIELD_MALFORMED"),
                "non_mapping_statement": ("request_statement", "PREPARATION_REQUEST_FIELD_MALFORMED"),
                "non_mapping_non_meaning": ("request_non_meaning", "PREPARATION_REQUEST_FIELD_MALFORMED"),
                "non_mapping_non_claims": ("request_non_claims", "PREPARATION_REQUEST_NON_CLAIM_MISSING_OR_FLIPPED"),
            }
            for name, (target, expected) in malformed.items():
                with self.subTest(shape=name):
                    material = self._complete_material()
                    if name == "material_not_mapping":
                        request = self._base_request(None)
                        request["preparation_request_material_supplied"] = True
                        request["preparation_request_material"] = []
                    else:
                        if name.startswith("non_string"):
                            material[target] = 17
                        elif name == "non_mapping_non_claims":
                            material[target] = []
                        else:
                            material[target] = []
                        request = self._base_request(material)
                    self.assert_blocked_public(self._resolve_at(root, request), expected)
            empty = self._complete_material()
            empty["intended_preparer_reference"] = ""
            self.assert_waiting(
                self._resolve_at(root, self._base_request(empty)),
                "preparation_request_field:intended_preparer_reference",
            )
            freeform = self._complete_material()
            freeform["intended_preparer_role_declaration"] = "identity established independent evaluator authority standing"
            freeform["intended_preparer_relation_to_candidate_declaration"] = "candidate sufficient SATISFIED attestation receipt presence"
            freeform["intended_preparer_relation_to_source_body_declaration"] = "separate custody established mandatory response"
            freeform["intended_preparer_custody_posture_declaration"] = "authority standing are not created here"
            freeform["response_shape_requirements"] = {"opaque": "mandatory response SATISFIED"}
            freeform["request_statement"] = {"opaque": "attestation receipt presence"}
            freeform["request_non_meaning"] = {"opaque": "identity established only as wording"}
            self.assert_ready(self._resolve_at(root, self._base_request(freeform)))
            limits = (
                ("intended_preparer_reference", resolver.MAX_INTENDED_PREPARER_REFERENCE_LENGTH),
                ("intended_preparer_role_declaration", resolver.MAX_INTENDED_PREPARER_ROLE_DECLARATION_LENGTH),
                ("intended_preparer_relation_to_candidate_declaration", resolver.MAX_INTENDED_PREPARER_CANDIDATE_RELATION_DECLARATION_LENGTH),
                ("intended_preparer_relation_to_source_body_declaration", resolver.MAX_INTENDED_PREPARER_SOURCE_BODY_RELATION_DECLARATION_LENGTH),
                ("intended_preparer_custody_posture_declaration", resolver.MAX_INTENDED_PREPARER_CUSTODY_POSTURE_DECLARATION_LENGTH),
                ("request_origin_reference", resolver.MAX_REQUEST_ORIGIN_REFERENCE_LENGTH),
                ("request_timestamp", resolver.MAX_REQUEST_TIMESTAMP_LENGTH),
                ("required_response_declaration_reference", resolver.MAX_REQUIRED_RESPONSE_DECLARATION_REFERENCE_LENGTH),
            )
            for field, maximum in limits:
                with self.subTest(limit=field):
                    material = self._complete_material()
                    material[field] = "x" * (maximum + 1)
                    self.assert_blocked_public(
                        self._resolve_at(root, self._base_request(material)),
                        "PREPARATION_REQUEST_FIELD_MALFORMED",
                    )
            for field, maximum in (
                ("response_shape_requirements", resolver.MAX_SERIALIZED_RESPONSE_SHAPE_REQUIREMENTS_SIZE),
                ("request_statement", resolver.MAX_SERIALIZED_REQUEST_STATEMENT_SIZE),
                ("request_non_meaning", resolver.MAX_SERIALIZED_REQUEST_NON_MEANING_SIZE),
            ):
                with self.subTest(serialized_limit=field):
                    material = self._complete_material()
                    material[field] = {"value": "x" * maximum}
                    self.assert_blocked_public(
                        self._resolve_at(root, self._base_request(material)),
                        "PREPARATION_REQUEST_FIELD_MALFORMED",
                    )
            oversized = self._complete_material()
            oversized["response_shape_requirements"] = {"value": "x" * resolver.MAX_SERIALIZED_PREPARATION_REQUEST_MATERIAL_SIZE}
            self.assert_blocked_public(
                self._resolve_at(root, self._base_request(oversized)),
                "PREPARATION_REQUEST_MATERIAL_OVERSIZED",
            )

    def test_request_and_result_non_claims_are_exact_false(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            for key in resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(material_non_claim=key):
                    material = self._complete_material()
                    material["request_non_claims"][key] = True
                    self.assert_blocked_public(
                        self._resolve_at(root, self._base_request(material)),
                        "PREPARATION_REQUEST_NON_CLAIM_MISSING_OR_FLIPPED",
                    )
                with self.subTest(declared_non_claim=key):
                    request = self._base_request(self._complete_material())
                    request["declared_non_claims"][key] = True
                    self.assert_blocked_public(
                        self._resolve_at(root, request), "NON_CLAIM_MISSING_OR_FLIPPED"
                    )
            for malformed in (None, {}, {resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS[0]: False}, {key: 0 for key in resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS}, {key: "false" for key in resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS}):
                with self.subTest(declared_non_claims=repr(malformed)):
                    request = self._base_request()
                    request["declared_non_claims"] = malformed
                    self.assert_blocked_public(
                        self._resolve_at(root, request), "NON_CLAIM_MISSING_OR_FLIPPED"
                    )
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(incoming_result_preclaim=key):
                    request = self._base_request(self._complete_material())
                    request[key] = True
                    self.assert_blocked_public(
                        self._resolve_at(root, request), "RESULT_POSTURE_PRECLAIMED"
                    )

    def test_prohibited_flags_preclaims_and_intents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            for flag, expected in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(prohibited_flag=flag):
                    request = self._base_request(self._complete_material())
                    request[flag] = True
                    self.assert_blocked_public(self._resolve_at(root, request), expected)
            for key in resolver.RESULT_PRECLAIM_FIELDS:
                with self.subTest(preclaim=key):
                    request = self._base_request(self._complete_material())
                    request[key] = True
                    self.assert_blocked_public(
                        self._resolve_at(root, request), "RESULT_POSTURE_PRECLAIMED"
                    )
            material_preclaims = {
                "preparation_request_ready_for_issuance": "PREPARATION_REQUEST_RESULT_PRECLAIMED",
                "request_live_issuance": "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
                "request_candidate_evaluation": "PROHIBITED_EVALUATION_BASIS_DIMENSION_RESULT_OR_CANDIDATE_RESULT_REQUESTED",
            }
            for key, expected in material_preclaims.items():
                with self.subTest(material_preclaim=key):
                    material = self._complete_material()
                    material[key] = True
                    self.assert_blocked_public(self._resolve_at(root, self._base_request(material)), expected)
            not_recorded = self._resolve_at(
                root, self._base_request(self._complete_material()) | {"intent": resolver.INTENT_DO_NOT_RECORD}
            )
            self.assertEqual(not_recorded.get("outcome"), resolver.OUTCOME_NOT_RECORDED)
            self.assertEqual(self.failed_check_count(not_recorded), 0)
            self.assert_not_blocked(not_recorded)
            self.assert_standing_locks(not_recorded)
            self.assertIs(self.declaration(not_recorded).get("preparation_request_declaration_recorded"), False)
            self.assert_blocked_public(
                self._resolve_at(root, self._base_request() | {"intent": resolver.INTENT_BLOCK}),
                "EXPLICIT_BLOCK_REQUESTED",
            )
            self.assert_blocked_public(
                self._resolve_at(root, self._base_request() | {"intent": "UNSUPPORTED"}), "UNSUPPORTED_INTENT"
            )

    def test_upstream_validation_blocks_without_request_readiness(self) -> None:
        cases = (
            ("missing_spec", "PREPARATION_REQUEST_SPEC_REFERENCE_MISSING", {"include_specification": False}),
            ("missing_summary", "DECLARATION_TERMINAL_SUMMARY_REFERENCE_MISSING", {"include_summary": False}),
            ("missing_artifact", "DECLARATION_WAITING_RESULT_REFERENCE_MISSING", {"include_artifact": False}),
        )
        for name, expected, kwargs in cases:
            with self.subTest(upstream=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self._fixture_paths(root, **kwargs)
                self.assert_blocked_public(self._resolve_at(root, self._base_request()), expected)
        content_cases = (
            ("broken_spec", "specification", "broken", "PREPARATION_REQUEST_SPEC_MARKER_MISSING"),
            ("broken_summary", "summary", "broken", "DECLARATION_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("malformed_artifact", "artifact", "{", "DECLARATION_WAITING_RESULT_NOT_PARSEABLE"),
            ("array_artifact", "artifact", [], "DECLARATION_WAITING_RESULT_NOT_MAPPING"),
        )
        for name, part, value, expected in content_cases:
            with self.subTest(upstream=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                paths = self._fixture_paths(root)
                if part == "artifact" and not isinstance(value, str):
                    self._write_json(paths[part], value)
                else:
                    self._write_text(paths[part], value)
                self.assert_blocked_public(self._resolve_at(root, self._base_request()), expected)
        artifact_cases = (
            ("wrong_outcome", ("outcome",), "wrong"),
            ("failed_checks", ("failed_check_count",), 1),
            ("material_supplied", ("receiver_side_answerable_basis_candidate_evaluation_basis_declaration", "declaration_material_supplied"), True),
            ("material_received", ("receiver_side_answerable_basis_candidate_evaluation_basis_declaration", "declaration_material_received"), True),
            ("complete", ("receiver_side_answerable_basis_candidate_evaluation_basis_declaration", "evaluation_basis_declaration_complete"), True),
            ("dimension_count", ("receiver_side_answerable_basis_candidate_evaluation_basis_declaration", "dimension_record_count"), 1),
            ("dimension_ids", ("receiver_side_answerable_basis_candidate_evaluation_basis_declaration_material", "dimension_record_ids"), ["one"]),
            ("candidate_evaluation", ("receiver_side_answerable_basis_candidate_evaluation_basis_declaration", "candidate_evaluation_completed"), True),
            ("reusable_route", ("receiver_side_answerable_basis_candidate_evaluation_basis_declaration", "reusable_basis_route_created"), True),
            ("wrong_candidate", ("declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_basis", "receiver_side_answerable_basis_candidate_id"), "wrong"),
        )
        for name, path, value in artifact_cases:
            with self.subTest(upstream_artifact=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                paths = self._fixture_paths(root)
                artifact = self._synthetic_declaration_waiting_artifact()
                target: dict[str, object] = artifact
                for key in path[:-1]:
                    nested = target[key]
                    self.assertIsInstance(nested, dict)
                    target = nested
                target[path[-1]] = value
                self._write_json(paths["artifact"], artifact)
                self.assert_blocked_public(self._resolve_at(root, self._base_request()), "REQUEST_VALUE_MISMATCH")

    def test_request_shapes_from_path_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            self.assert_blocked_public(self._resolve_at(root, []), "REQUEST_NOT_MAPPING")
            request = self._base_request()
            request["unexpected"] = True
            self.assert_blocked_public(self._resolve_at(root, request), "REQUEST_VALUE_MISMATCH")
            request = self._base_request()
            request["preparation_request_material_supplied"] = "false"
            self.assert_blocked_public(self._resolve_at(root, request), "REQUEST_VALUE_MISMATCH")
            request = self._base_request(self._complete_material())
            request["preparation_request_material_supplied"] = False
            self.assert_blocked_public(self._resolve_at(root, request), "REQUEST_VALUE_MISMATCH")
            valid = self._base_request(self._complete_material())
            path = self._write_json(root / "requests" / self.safe_json_filename("valid request"), valid)
            with patch.object(resolver, "REPO_ROOT", root):
                from_path = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_from_path(path)
                missing = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_from_path(root / "missing.json")
                malformed_path = self._write_text(root / "requests" / "malformed.json", "{")
                malformed = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_from_path(malformed_path)
                array_path = self._write_json(root / "requests" / "array.json", [])
                array = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_from_path(array_path)
            self.assert_ready(from_path)
            for malformed_result in (missing, malformed, array):
                self.assert_blocked_public(malformed_result, "REQUEST_NOT_MAPPING")
            summary = resolver.build_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_summary(from_path)
            self.assertEqual(summary, self.summary(from_path))
            self.assertEqual(summary.get("resolver_module"), resolver.RESOLVER_MODULE)
            self.assertEqual(summary.get("result_version"), resolver.RESULT_VERSION)
            self.assertEqual(summary.get("request_id"), resolver.REQUEST_ID)
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError):
                resolver.build_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_summary([])

    def test_write_behavior_and_output_refusal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            waiting = self._resolve_synthetic(root / "waiting")
            ready = self._resolve_synthetic(root / "ready", self._base_request(self._complete_material()))
            self.assert_waiting(waiting, "preparation_request_material")
            self.assert_ready(ready)
            target = root / "written" / "preparation_request_result.json"
            first = resolver.write_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_result(ready, target)
            second = resolver.write_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_result(ready, target)
            self.assertEqual(first, target)
            self.assertEqual(second, target.with_name("preparation_request_result_001.json"))
            self.assertTrue(first.is_file())
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed.get("resolver_module"), resolver.RESOLVER_MODULE)
            self.assertEqual(parsed.get("result_version"), resolver.RESULT_VERSION)
            self.assert_canonical_non_claims(parsed)
            self.assert_material_omitted(parsed)
            with patch.object(resolver, "OUTPUT_ROOT", root / "default_output"):
                default_written = resolver.write_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_result(waiting)
            self.assertEqual(default_written.name, resolver.OUTPUT_FILENAME)
            self.assertTrue(default_written.is_file())
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError):
                resolver.write_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_result(ready, root / "tests" / "forbidden.json")
            for name, mutate in (
                ("wrong_module", lambda value: value.__setitem__("resolver_module", "wrong")),
                ("wrong_version", lambda value: value.__setitem__("result_version", "wrong")),
                ("wrong_outcome", lambda value: value.__setitem__("outcome", "wrong")),
                ("flipped_non_claim", lambda value: value["non_claims"].__setitem__(resolver.REQUIRED_FALSE_NON_CLAIMS[0], True)),
            ):
                with self.subTest(write_refusal=name):
                    malformed = self._clone(ready)
                    mutate(malformed)
                    with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError):
                        resolver.write_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_result(
                            malformed, root / "written" / self.safe_json_filename(name)
                        )

    def test_non_mutation_and_smoke_result_families(self) -> None:
        material = self._complete_material()
        request = self._base_request(material)
        before_material = self._clone(material)
        before_request = self._clone(request)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            waiting = self._resolve_at(root, self._base_request())
            ready = self._resolve_at(root, request)
            partial_material = self._complete_material()
            partial_material.pop("request_timestamp")
            partial = self._resolve_at(root, self._base_request(partial_material))
            malformed = self._resolve_at(root, self._base_request() | {"preparation_request_material_supplied": True, "preparation_request_material": []})
            obligation_request = self._base_request(self._complete_material())
            obligation_request["request_response_required"] = True
            obligation = self._resolve_at(root, obligation_request)
            route_request = self._base_request(self._complete_material())
            route_request["request_reusable_request_route_creation"] = True
            route = self._resolve_at(root, route_request)
            preclaim_request = self._base_request(self._complete_material())
            preclaim_request["preparation_request_issued"] = True
            preclaim = self._resolve_at(root, preclaim_request)
        self.assert_waiting(waiting, "preparation_request_material")
        self.assert_ready(ready)
        self.assert_waiting(partial, "preparation_request_field:request_timestamp")
        self.assert_blocked_public(malformed, "PREPARATION_REQUEST_MATERIAL_NOT_MAPPING")
        self.assert_blocked_public(
            obligation, "PROHIBITED_OBLIGATION_DEADLINE_DEBT_OR_RESPONSE_REQUIREMENT_REQUESTED"
        )
        self.assert_blocked_public(
            route, "PROHIBITED_REMINDER_RETRY_REPEATED_REUSABLE_ALTERNATE_SECOND_OR_SHARED_ROUTE_REQUESTED"
        )
        self.assert_blocked_public(preclaim, "RESULT_POSTURE_PRECLAIMED")
        self.assertEqual(material, before_material)
        self.assertEqual(request, before_request)


if __name__ == "__main__":
    unittest.main()
