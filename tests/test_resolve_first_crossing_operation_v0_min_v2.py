"""Tests for the v2 bounded first-crossing operation successor only.

Synthetic fixtures require the completed first-crossing boundary allowance and
the two descendant-body records before recording separate first-crossing
records. V2 preserves the v1 test failure as lineage evidence and locks the
missing follow-on-work authorization prohibition without creating downstream work.
"""

from __future__ import annotations

import copy
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

import resolve_first_crossing_operation_v0_min_v2 as resolver


class FirstCrossingOperationV0MinV2Tests(unittest.TestCase):
    """Exercise the v2 successor without converting first crossing into relation."""

    REFERENCE_FILENAMES = {
        "first_crossing_operation_spec_reference": "first_crossing_operation_spec.md",
        "first_crossing_boundary_terminal_summary_reference": (
            "first_crossing_boundary_summary.md"
        ),
        "descendant_body_creation_operation_terminal_summary_reference": (
            "descendant_body_creation_operation_summary.md"
        ),
        "descendant_body_creation_boundary_terminal_summary_reference": (
            "descendant_body_creation_boundary_summary.md"
        ),
        "existence_claim_evidence_check_terminal_summary_reference": (
            "existence_claim_evidence_check_summary.md"
        ),
    }

    CONVERSION_FALSE_FIELDS = (
        "relation_created",
        "field_machinery_created",
        "runtime_created",
        "api_created",
        "currentness_created",
        "authority_created",
        "standing_created",
        "output_authorized",
        "action_authorized",
        "derivative_reception_authorized",
        "synchronization_authorized",
        "coupling_assigned_to_descendant_body_a",
        "coupling_assigned_to_descendant_body_b",
        "coupling_assigned_to_candidate_a",
        "coupling_assigned_to_candidate_b",
        "coupling_created",
        "third_candidate_created",
        "third_model_admitted",
        "presence_established",
        "identity_created",
        "standing_descendant_created",
        "descendant_standing_check_performed",
        "follow_on_authorized",
        "follow_on_work_authorized",
        "scan_performed",
        "repository_scan_performed",
        "file_discovery_performed",
        "repair_performed",
        "validation_enforced",
    )

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def _write_markdown(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"synthetic Markdown path is a directory: {path}")
        path.write_text(text, encoding="utf-8")
        return path

    def _write_json(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"synthetic JSON path is a directory: {path}")
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def _first_crossing_operation_spec_text(self) -> str:
        """Build every exact resolver-accepted target marker class."""

        lines = ["# First Crossing Operation V0 Minimum Specification"]
        for _class_name, variants in resolver.TARGET_SPEC_MARKER_CLASSES:
            lines.extend(variants[0])
        return "\n".join(dict.fromkeys(lines)) + "\n"

    def _first_crossing_boundary_summary_text(self) -> str:
        markers = resolver.UPSTREAM_REQUIREMENTS[0][4][0]
        return "\n".join(markers) + "\n"

    def _descendant_body_creation_operation_summary_text(self) -> str:
        markers = resolver.UPSTREAM_REQUIREMENTS[1][4][0]
        return "\n".join(markers) + "\n"

    def _descendant_body_creation_boundary_summary_text(self) -> str:
        markers = resolver.UPSTREAM_REQUIREMENTS[2][4][0]
        return "\n".join(markers) + "\n"

    def _existence_claim_evidence_check_summary_text(self) -> str:
        markers = resolver.UPSTREAM_REQUIREMENTS[3][4][0]
        return "\n".join(
            (
                *markers,
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
            )
        ) + "\n"

    def _fixture_texts(self) -> dict[str, str]:
        return {
            "first_crossing_operation_spec_reference": (
                self._first_crossing_operation_spec_text()
            ),
            "first_crossing_boundary_terminal_summary_reference": (
                self._first_crossing_boundary_summary_text()
            ),
            "descendant_body_creation_operation_terminal_summary_reference": (
                self._descendant_body_creation_operation_summary_text()
            ),
            "descendant_body_creation_boundary_terminal_summary_reference": (
                self._descendant_body_creation_boundary_summary_text()
            ),
            "existence_claim_evidence_check_terminal_summary_reference": (
                self._existence_claim_evidence_check_summary_text()
            ),
        }

    def _remove_marker(self, text: str, marker: str) -> str:
        """Remove all copies so a marker does not survive in a duplicate section."""

        return re.sub(re.escape(marker), "missing posture marker", text, flags=re.IGNORECASE)

    def _build_valid_synthetic_request(
        self, root: Path, text_overrides: dict[str, str] | None = None
    ) -> dict[str, Any]:
        texts = self._fixture_texts()
        texts.update(text_overrides or {})
        references: dict[str, str] = {}
        for field, filename in self.REFERENCE_FILENAMES.items():
            references[field] = str(self._write_markdown(root / filename, texts[field]))
        return resolver.build_first_crossing_operation_v0_min_v2_request(**references)

    def _block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def _checks(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        checks = result.get("first_crossing_operation_checks")
        self.assertIsInstance(checks, list)
        return checks

    def _failed_check_count(self, result: dict[str, Any]) -> int:
        return sum(check.get("passed") is False for check in self._checks(result))

    def _passed_check_count(self, result: dict[str, Any]) -> int:
        return sum(check.get("passed") is True for check in self._checks(result))

    def _operation(self, result: dict[str, Any]) -> dict[str, Any]:
        operation = result.get("first_crossing_operation")
        self.assertIsInstance(operation, dict)
        return operation

    def assert_recorded_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))

    def assert_requires_boundary_allowance_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))

    def assert_not_recorded_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        for check in self._checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if isinstance(code, str):
                    self.assertIn(code, resolver.BLOCK_CODES, code)

    def assert_blocked_with_public_code(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertGreater(self._failed_check_count(result), 0)
        code = self._block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)

    def assert_canonical_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(field, non_claims)
            self.assertIs(non_claims[field], False, field)

    def assert_operation_wrapper_separation(self, result: dict[str, Any]) -> None:
        operation = self._operation(result)
        for wrapper_field in (
            "outcome",
            "block",
            "first_crossing_operation_checks",
            "first_crossing_operation_material",
            "non_claims",
            "first_crossing_operation_summary",
            "first_crossing_operation_metadata",
        ):
            self.assertNotIn(wrapper_field, operation)

    def assert_no_conversion(self, result: dict[str, Any]) -> None:
        operation = self._operation(result)
        for field in self.CONVERSION_FALSE_FIELDS:
            self.assertIs(operation.get(field), False, field)

    def assert_final_false_posture(self, result: dict[str, Any]) -> None:
        self.assert_canonical_non_claims(result)
        self.assert_no_conversion(result)

    def _assert_recorded_material(self, result: dict[str, Any]) -> None:
        material = result.get("first_crossing_operation_material")
        self.assertIsInstance(material, dict)
        self.assertEqual(
            set(material),
            {
                "first_crossing_a_evaluation",
                "first_crossing_b_evaluation",
                "first_crossing_pair_evaluation",
            },
        )
        for prefix, crossing_id, body_id, source_id, role, label in (
            (
                "first_crossing_a_evaluation",
                resolver.FIRST_CROSSING_A_ID,
                resolver.DESCENDANT_BODY_A_ID,
                resolver.CANDIDATE_A_STANDING_SOURCE_ID,
                resolver.CANDIDATE_A_ROLE,
                resolver.CANDIDATE_A_STANDING_LABEL,
            ),
            (
                "first_crossing_b_evaluation",
                resolver.FIRST_CROSSING_B_ID,
                resolver.DESCENDANT_BODY_B_ID,
                resolver.CANDIDATE_B_STANDING_SOURCE_ID,
                resolver.CANDIDATE_B_ROLE,
                resolver.CANDIDATE_B_STANDING_LABEL,
            ),
        ):
            evaluation = material[prefix]
            self.assertEqual(evaluation["first_crossing_id"], crossing_id)
            self.assertEqual(evaluation["descendant_body_id"], body_id)
            self.assertEqual(evaluation["candidate_standing_source_id"], source_id)
            self.assertEqual(evaluation["candidate_role"], role)
            self.assertEqual(evaluation["candidate_standing_label"], label)
            for field in (
                "descendant_body_created",
                "first_crossing_supported",
                "first_crossing_authorized",
                "crossing_authorized",
                "first_crossing_performed",
                "crossing_performed",
                "first_crossing_recorded",
            ):
                self.assertIs(evaluation[field], True, f"{prefix}.{field}")
            for field in (
                "descendant_body_is_first_crossing",
                "relation_created",
                "coupling_created",
                "presence_established",
                "identity_created",
            ):
                self.assertIs(evaluation[field], False, f"{prefix}.{field}")

        pair = material["first_crossing_pair_evaluation"]
        for field in (
            "both_first_crossings_supported",
            "both_first_crossings_authorized",
            "both_first_crossings_performed",
            "both_first_crossings_recorded",
            "first_crossing_a_recorded",
            "first_crossing_b_recorded",
            "crossing_authorized",
            "crossing_performed",
            "descendant_bodies_remain_sibling",
            "descendant_body_non_hierarchy_preserved",
            "candidate_standing_non_hierarchy_preserved",
            "regulation_not_sovereign_over_motion",
            "motion_does_not_erase_regulation",
        ):
            self.assertIs(pair[field], True, field)
        self.assertEqual(pair["first_crossing_pair_scope"], resolver.FIRST_CROSSING_PAIR_SCOPE)
        for field in (
            "relation_created",
            "coupling_assigned",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "presence_established",
            "identity_created",
            "standing_descendant_created",
            "descendant_standing_check_performed",
            "follow_on_authorized",
        ):
            self.assertIs(pair[field], False, field)

    def test_public_api_constants_and_default_request(self) -> None:
        for name in (
            "resolve_first_crossing_operation_v0_min_v2",
            "resolve_first_crossing_operation_v0_min_v2_from_path",
            "write_first_crossing_operation_v0_min_v2_result",
            "build_first_crossing_operation_v0_min_v2_summary",
            "build_first_crossing_operation_v0_min_v2_request",
            "build_declared_first_crossing_operation_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "build_first_crossing_operation_v0_min_request",
            "build_declared_first_crossing_operation_v0_min_request",
        ):
            self.assertIs(
                getattr(resolver, name),
                resolver.build_first_crossing_operation_v0_min_v2_request,
            )
        exact_values = {
            "RESULT_VERSION": "0.2.0",
            "RESOLVER_MODULE": "resolve_first_crossing_operation_v0_min_v2",
            "OPERATION_ID": "first_crossing_operation_001",
            "OPERATION_TYPE": "FIRST_CROSSING_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": "EVALUATE_FIRST_CROSSING_AFTER_BOUNDARY_ALLOWANCE_ONLY",
            "PRIOR_FIRST_CROSSING_BOUNDARY_TYPE": "FIRST_CROSSING_BOUNDARY",
            "PRIOR_FIRST_CROSSING_BOUNDARY_OUTCOME_REQUIRED": "FIRST_CROSSING_BOUNDARY_ALLOWED",
            "PRIOR_FIRST_CROSSING_BOUNDARY_RESULT_REQUIRED": "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED",
            "ADMISSIBLE_FUTURE_ROUTE": "FIRST_CROSSING_OPERATION_THEN_RELATION_BOUNDARY_ONLY",
            "DESCENDANT_BODY_A_ID": "descendant_body_a_001",
            "DESCENDANT_BODY_B_ID": "descendant_body_b_001",
            "DESCENDANT_BODY_PAIR_SCOPE": "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY",
            "CANDIDATE_A_STANDING_SOURCE_ID": "descendant_body_basis_candidate_a_001",
            "CANDIDATE_B_STANDING_SOURCE_ID": "descendant_body_basis_candidate_b_001",
            "CANDIDATE_A_ROLE": "CANDIDATE_A",
            "CANDIDATE_B_ROLE": "CANDIDATE_B",
            "CANDIDATE_A_STANDING_LABEL": "CANDIDATE_A_STANDING",
            "CANDIDATE_B_STANDING_LABEL": "CANDIDATE_B_STANDING",
            "FIRST_CROSSING_A_ID": "first_crossing_a_001",
            "FIRST_CROSSING_B_ID": "first_crossing_b_001",
            "FIRST_CROSSING_PAIR_SCOPE": "SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
        }
        for name, expected in exact_values.items():
            self.assertEqual(getattr(resolver, name), expected)
        for name in (
            "PRIOR_FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_CREATION_REFERENCED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_A_REFERENCED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_B_REFERENCED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_CREATED_REFERENCED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_FIRST_CROSSING_AUTHORIZED_REQUIRED",
            "PRIOR_CROSSING_AUTHORIZED_REQUIRED",
            "PRIOR_FIRST_CROSSING_PERFORMED_REQUIRED",
            "PRIOR_CROSSING_PERFORMED_REQUIRED",
            "PRIOR_RELATION_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_first_crossing_operation_v0_min_v2"
            )
        )
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_RECORDED,
            resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            resolver.OUTCOME_BLOCKED,
        })
        for code in resolver.BLOCK_CODES:
            self.assertIsInstance(code, str)
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_work_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )
        request = resolver.build_first_crossing_operation_v0_min_v2_request()
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertTrue(
            str(request["first_crossing_operation_spec_reference"]).endswith(
                "FIRST_CROSSING_OPERATION_V0_MIN_SPEC.md"
            )
        )
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(request[field], False, field)
            self.assertIs(request["declared_non_claims"][field], False, field)
        for field in resolver.PROHIBITED_REQUEST_FLAGS:
            self.assertIs(request[field], False, field)

    def test_default_synthetic_complete_operation_records_recorded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self._build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
        self.assert_recorded_not_blocked(result)
        self.assertEqual(self._failed_check_count(result), 0)
        self.assertGreater(self._passed_check_count(result), 0)
        self.assertEqual(result["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        for section in (
            "first_crossing_operation_metadata",
            "declared_first_crossing_operation_basis",
            "upstream_basis",
            "first_crossing_operation",
            "first_crossing_operation_material",
            "first_crossing_operation_checks",
            "first_crossing_operation_statement",
            "first_crossing_operation_non_meaning",
            "first_crossing_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "first_crossing_operation_summary",
        ):
            self.assertIn(section, result)
        operation = self._operation(result)
        for field, expected in (
            ("operation_id", resolver.OPERATION_ID),
            ("operation_type", resolver.OPERATION_TYPE),
            ("operation_version", resolver.OPERATION_VERSION),
            ("operation_scope", resolver.OPERATION_SCOPE),
            ("prior_first_crossing_boundary_type", resolver.PRIOR_FIRST_CROSSING_BOUNDARY_TYPE),
            ("prior_first_crossing_boundary_outcome_required", resolver.PRIOR_FIRST_CROSSING_BOUNDARY_OUTCOME_REQUIRED),
            ("prior_first_crossing_boundary_result_required", resolver.PRIOR_FIRST_CROSSING_BOUNDARY_RESULT_REQUIRED),
            ("descendant_body_a_id", resolver.DESCENDANT_BODY_A_ID),
            ("descendant_body_b_id", resolver.DESCENDANT_BODY_B_ID),
            ("descendant_body_pair_scope", resolver.DESCENDANT_BODY_PAIR_SCOPE),
            ("candidate_a_standing_source_id", resolver.CANDIDATE_A_STANDING_SOURCE_ID),
            ("candidate_b_standing_source_id", resolver.CANDIDATE_B_STANDING_SOURCE_ID),
            ("candidate_a_role", resolver.CANDIDATE_A_ROLE),
            ("candidate_b_role", resolver.CANDIDATE_B_ROLE),
            ("candidate_a_standing_label", resolver.CANDIDATE_A_STANDING_LABEL),
            ("candidate_b_standing_label", resolver.CANDIDATE_B_STANDING_LABEL),
            ("first_crossing_a_id", resolver.FIRST_CROSSING_A_ID),
            ("first_crossing_b_id", resolver.FIRST_CROSSING_B_ID),
            ("first_crossing_pair_scope", resolver.FIRST_CROSSING_PAIR_SCOPE),
            ("first_crossing_result", "FIRST_CROSSING_SUPPORTED"),
        ):
            self.assertEqual(operation[field], expected, field)
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation[field], True, field)
        self.assert_operation_wrapper_separation(result)
        self.assert_no_conversion(result)
        self.assert_canonical_non_claims(result)
        marker_checks = [
            check
            for check in self._checks(result)
            if str(check.get("check_name", "")).endswith("markers present")
        ]
        self.assertTrue(marker_checks)
        self.assertTrue(all(check["passed"] is True for check in marker_checks))
        detail = result["first_crossing_result_detail"]
        self.assertEqual(detail["missing_or_insufficient_boundary_allowance"], [])
        self.assertEqual(detail["not_recorded_reasons"], [])

    def test_first_crossing_material_is_two_separate_records_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = resolver.resolve_first_crossing_operation_v0_min_v2(
                self._build_valid_synthetic_request(Path(directory))
            )
        self.assert_recorded_not_blocked(result)
        self._assert_recorded_material(result)
        self.assert_operation_wrapper_separation(result)

    def test_default_live_repo_target_records_when_present(self) -> None:
        request = resolver.build_first_crossing_operation_v0_min_v2_request()
        references = [request["first_crossing_operation_spec_reference"]]
        references.extend(request[field] for field, *_ in resolver.UPSTREAM_REQUIREMENTS)
        if not all((REPOSITORY_ROOT / Path(reference)).is_file() for reference in references):
            self.skipTest("default first-crossing operation references are not all present")
        result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
        self.assert_recorded_not_blocked(result)
        self.assertEqual(self._failed_check_count(result), 0)
        operation = self._operation(result)
        self.assertEqual(operation["first_crossing_result"], "FIRST_CROSSING_SUPPORTED")
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation[field], True, field)
        self.assert_no_conversion(result)
        self.assert_canonical_non_claims(result)

    def test_missing_or_insufficient_boundary_support_requires_or_blocks(self) -> None:
        def missing(field: str) -> Callable[[Path, dict[str, Any]], None]:
            def apply(root: Path, request: dict[str, Any]) -> None:
                request[field] = str(root / "missing" / self.safe_json_filename(field))

            return apply

        cases: list[tuple[str, Callable[[Path, dict[str, Any]], None], str]] = []
        for field, *_rest, allowance_class in resolver.UPSTREAM_REQUIREMENTS:
            expected = (
                resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE
                if allowance_class
                else resolver.OUTCOME_BLOCKED
            )
            cases.append((f"missing {field}", missing(field), expected))
        for field, _default, _missing, _marker, variants, _flag, allowance_class in (
            resolver.UPSTREAM_REQUIREMENTS
        ):
            for marker in variants[0]:
                def corrupt(
                    root: Path,
                    request: dict[str, Any],
                    *,
                    field: str = field,
                    marker: str = marker,
                ) -> None:
                    path = Path(request[field])
                    self._write_markdown(
                        path,
                        self._remove_marker(path.read_text(encoding="utf-8"), marker),
                    )

                expected = (
                    resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE
                    if allowance_class
                    else resolver.OUTCOME_BLOCKED
                )
                cases.append((f"corrupt {field} {marker}", corrupt, expected))
        for case_name, apply, expected in cases:
            with self.subTest(case=case_name):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    apply(Path(directory), request)
                    result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
                if expected == resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE:
                    self.assert_requires_boundary_allowance_not_blocked(result)
                    self.assertEqual(
                        self._operation(result)["first_crossing_result"],
                        "REQUIRES_BOUNDARY_ALLOWANCE",
                    )
                    self.assertTrue(
                        result["first_crossing_result_detail"][
                            "missing_or_insufficient_boundary_allowance"
                        ]
                    )
                else:
                    self.assert_blocked_with_public_code(result)
                self.assert_final_false_posture(result)

    def test_intents_and_support_not_found_do_not_record(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self._build_valid_synthetic_request(Path(directory))
            do_not_record = copy.deepcopy(request)
            do_not_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_first_crossing_operation_v0_min_v2(do_not_record)
            self.assert_not_recorded_not_blocked(result)
            operation = self._operation(result)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(operation[field], False, field)
            self.assert_final_false_posture(result)

            unsupported = copy.deepcopy(request)
            unsupported["first_crossing_support_found"] = False
            result = resolver.resolve_first_crossing_operation_v0_min_v2(unsupported)
            self.assert_not_recorded_not_blocked(result)
            self.assertEqual(self._operation(result)["first_crossing_result"], "FIRST_CROSSING_NOT_SUPPORTED")
            self.assertEqual(result["first_crossing_result_detail"]["not_recorded_reasons"], ["first_crossing_support_found"])
            self.assert_final_false_posture(result)

            explicit_block = copy.deepcopy(request)
            explicit_block["intent"] = resolver.INTENT_BLOCK
            result = resolver.resolve_first_crossing_operation_v0_min_v2(explicit_block)
        self.assert_blocked_with_public_code(result)
        self.assertEqual(self._block_code(result), "EXPLICIT_BLOCK_REQUESTED")
        self.assert_final_false_posture(result)

    def test_request_shape_and_exact_value_mismatches_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self._build_valid_synthetic_request(Path(directory))
            cases: list[tuple[str, Any]] = [
                ("non-mapping", []),
                ("unsupported intent", {**request, "intent": "UNSUPPORTED"}),
            ]
            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                invalid = copy.deepcopy(request)
                invalid[field] = (not expected) if isinstance(expected, bool) else f"wrong_{expected}"
                cases.append((f"wrong {field}", invalid))
            for field in (
                "operation_id",
                "operation_type",
                "operation_version",
                "operation_scope",
                "prior_first_crossing_boundary_type",
                "prior_first_crossing_boundary_outcome_required",
                "prior_first_crossing_boundary_result_required",
                "descendant_body_a_id",
                "descendant_body_b_id",
                "first_crossing_a_id",
                "first_crossing_b_id",
                "admissible_future_route",
            ):
                invalid = copy.deepcopy(request)
                invalid.pop(field)
                cases.append((f"missing {field}", invalid))
            for case_name, payload in cases:
                with self.subTest(case=case_name):
                    result = resolver.resolve_first_crossing_operation_v0_min_v2(payload)
                    self.assert_blocked_with_public_code(result)
                    self.assert_final_false_posture(result)

    def test_target_and_upstream_marker_classes_are_enforced(self) -> None:
        for class_name, variants in resolver.TARGET_SPEC_MARKER_CLASSES:
            marker = variants[0][-1]
            with self.subTest(target_marker_class=class_name):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    path = Path(request["first_crossing_operation_spec_reference"])
                    self._write_markdown(
                        path,
                        self._remove_marker(path.read_text(encoding="utf-8"), marker),
                    )
                    result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(
                    self._block_code(result),
                    "FIRST_CROSSING_OPERATION_SPEC_MARKER_MISSING",
                )
                self.assert_final_false_posture(result)

    def test_v2_follow_on_authorization_flags_block(self) -> None:
        for field in (
            "request_follow_on_authorization",
            "request_follow_on_work_authorization",
        ):
            with self.subTest(prohibited_request_flag=field):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    request[field] = True
                    result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(
                    self._block_code(result),
                    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
                )
                self.assert_final_false_posture(result)

    def test_prohibited_request_flags_block(self) -> None:
        required_flags = {
            **resolver.PROHIBITED_REQUEST_FLAGS,
        }
        required_flags.pop("request_follow_on_authorization")
        required_flags.pop("request_follow_on_work_authorization")
        for field, expected_code in required_flags.items():
            with self.subTest(prohibited_request_flag=field):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    request[field] = True
                    result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(self._block_code(result), expected_code)
                self.assert_final_false_posture(result)

    def test_top_level_and_declared_non_claims_canonicalize_false(self) -> None:
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(top_level_preclaim=field):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    request[field] = True
                    result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
                self.assert_blocked_with_public_code(result)
                expected_code = (
                    "RESULT_POSTURE_PRECLAIMED"
                    if field in resolver.ALLOWED_TRUE_RECORDED_FIELDS
                    else "NON_CLAIM_MISSING_OR_FLIPPED"
                )
                self.assertEqual(self._block_code(result), expected_code)
                self.assert_final_false_posture(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(declared_non_claim_flip=field):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    request["declared_non_claims"][field] = True
                    result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(self._block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                self.assert_final_false_posture(result)
        malformed_cases: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
            ("missing", lambda request: request.pop("declared_non_claims")),
            ("non-mapping", lambda request: request.__setitem__("declared_non_claims", [])),
            (
                "missing field",
                lambda request: request["declared_non_claims"].pop(
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                ),
            ),
            (
                "non-bool",
                lambda request: request["declared_non_claims"].__setitem__(
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0], "false"
                ),
            ),
        ]
        for case_name, apply in malformed_cases:
            with self.subTest(declared_non_claims=case_name):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    apply(request)
                    result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(self._block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                self.assert_final_false_posture(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request = self._build_valid_synthetic_request(root / "basis")
            request_path = self._write_json(root / self.safe_json_filename("valid request"), request)
            result = resolver.resolve_first_crossing_operation_v0_min_v2_from_path(request_path)
            self.assert_recorded_not_blocked(result)
            self.assertEqual(self._failed_check_count(result), 0)
            self.assertEqual(result["result_version"], resolver.RESULT_VERSION)
            self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
            for name, content, expected_code in (
                ("missing", None, "REQUEST_PATH_UNREADABLE"),
                ("invalid", "not JSON", "REQUEST_JSON_INVALID"),
                ("array", [], "REQUEST_NOT_MAPPING"),
            ):
                with self.subTest(path_case=name):
                    path = root / self.safe_json_filename(name)
                    if isinstance(content, str):
                        path.write_text(content, encoding="utf-8")
                    elif content is not None:
                        self._write_json(path, content)
                    malformed = resolver.resolve_first_crossing_operation_v0_min_v2_from_path(path)
                    self.assert_blocked_with_public_code(malformed)
                    self.assertEqual(self._block_code(malformed), expected_code)
            output = root / "first_crossing_operation_output" / resolver.DETERMINISTIC_FILENAME
            first_written = resolver.write_first_crossing_operation_v0_min_v2_result(result, output)
            second_written = resolver.write_first_crossing_operation_v0_min_v2_result(result, output)
            self.assertTrue(first_written.is_file())
            self.assertTrue(second_written.is_file())
            self.assertNotEqual(first_written, second_written)
            self.assertEqual(
                json.loads(first_written.read_text(encoding="utf-8"))["outcome"],
                resolver.OUTCOME_RECORDED,
            )
            self.assertIn("first_crossing_operation_v0_min_v2_result", first_written.name)
            self.assertIn("first_crossing_operation", str(resolver.OUTPUT_ROOT))
            upstream_roots = (
                "first_crossing_boundary",
                "descendant_body_creation_operation",
                "descendant_body_creation_boundary",
                "candidate_standing_operation",
                "runtime",
                "daemon",
                "api",
            )
            self.assertFalse(any(name in first_written.parts for name in upstream_roots))

    def test_summary_and_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self._build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
            summary = resolver.build_first_crossing_operation_v0_min_v2_summary(result)
        self.assert_recorded_not_blocked(result)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        for field in (
            "operation_id",
            "operation_type",
            "operation_version",
            "operation_scope",
            "prior_first_crossing_boundary_type",
            "prior_first_crossing_boundary_outcome_required",
            "prior_first_crossing_boundary_result_required",
            "descendant_body_a_id",
            "descendant_body_b_id",
            "first_crossing_a_id",
            "first_crossing_b_id",
            "first_crossing_result",
            *resolver.ALLOWED_TRUE_RECORDED_FIELDS,
        ):
            self.assertIn(field, summary)
        self.assertEqual(summary["first_crossing_result"], "FIRST_CROSSING_SUPPORTED")
        self.assertEqual(summary["missing_or_insufficient_boundary_allowance"], [])
        self.assertEqual(summary["not_recorded_reasons"], [])
        self._assert_recorded_material(result)
        self.assert_operation_wrapper_separation(result)
        self.assert_final_false_posture(result)

    def test_non_mutation_and_hostile_content_containment(self) -> None:
        sentinel = "RAW_HIDDEN_CONTAMINATED_LINEAGE_MUST_NOT_RETURN"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            texts = {field: f"{text}{sentinel}\n" for field, text in self._fixture_texts().items()}
            request = self._build_valid_synthetic_request(root, texts)
            request["hostile_payload"] = {"raw": sentinel, "nested": [sentinel]}
            before_request = copy.deepcopy(request)
            before_texts = {
                field: Path(request[field]).read_text(encoding="utf-8")
                for field in self.REFERENCE_FILENAMES
            }
            result = resolver.resolve_first_crossing_operation_v0_min_v2(request)
            after_texts = {
                field: Path(request[field]).read_text(encoding="utf-8")
                for field in self.REFERENCE_FILENAMES
            }
        self.assertEqual(request, before_request)
        self.assertEqual(after_texts, before_texts)
        self.assert_recorded_not_blocked(result)
        self.assertNotIn(sentinel, json.dumps(result, sort_keys=True))
        self.assert_final_false_posture(result)


if __name__ == "__main__":
    unittest.main()
