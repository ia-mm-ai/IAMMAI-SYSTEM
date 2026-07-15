"""Tests for one local first-crossing boundary allowance only.

Synthetic fixtures prove that a completed descendant-body creation line can
permit consideration of a later first-crossing operation without authorizing a
crossing, relation, runtime, coupling, presence, identity, or follow-on work.
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

import resolve_first_crossing_boundary_v0_min as resolver


class FirstCrossingBoundaryV0MinTests(unittest.TestCase):
    """Exercise the boundary without converting it into a crossing operation."""

    REFERENCE_FILENAMES = {
        "first_crossing_boundary_spec_reference": "first_crossing_boundary_spec.md",
        "descendant_body_creation_operation_terminal_summary_reference": (
            "descendant_body_creation_operation_summary.md"
        ),
        "descendant_body_creation_boundary_terminal_summary_reference": (
            "descendant_body_creation_boundary_summary.md"
        ),
        "candidate_standing_operation_terminal_summary_reference": (
            "candidate_standing_operation_summary.md"
        ),
        "existence_claim_evidence_check_terminal_summary_reference": (
            "existence_claim_evidence_check_summary.md"
        ),
    }

    CONVERSION_FALSE_FIELDS = (
        "first_crossing_authorized",
        "crossing_authorized",
        "first_crossing_performed",
        "crossing_performed",
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

    def _first_crossing_boundary_spec_text(self) -> str:
        lines: list[str] = ["# First Crossing Boundary V0 Minimum Specification"]
        for _, variants in resolver.TARGET_SPEC_MARKER_CLASSES:
            lines.extend(variants[0])
        return "\n".join(dict.fromkeys(lines)) + "\n"

    def _descendant_body_creation_operation_summary_text(self) -> str:
        markers = resolver.UPSTREAM_REQUIREMENTS[0][4][0]
        return "\n".join(markers) + "\n"

    def _descendant_body_creation_boundary_summary_text(self) -> str:
        markers = resolver.UPSTREAM_REQUIREMENTS[1][4][0]
        return "\n".join(markers) + "\n"

    def _candidate_standing_operation_summary_text(self) -> str:
        markers = resolver.UPSTREAM_REQUIREMENTS[2][4][0]
        return "\n".join((*markers, "candidate standing created")) + "\n"

    def _existence_claim_evidence_check_summary_text(self) -> str:
        markers = resolver.UPSTREAM_REQUIREMENTS[3][4][0]
        return "\n".join(
            (*markers, "descendant_body_basis_candidate_a_created = true", "descendant_body_basis_candidate_b_created = true", "descendant_body_basis_derivation_event_recorded = true")
        ) + "\n"

    def _fixture_texts(self) -> dict[str, str]:
        return {
            "first_crossing_boundary_spec_reference": self._first_crossing_boundary_spec_text(),
            "descendant_body_creation_operation_terminal_summary_reference": (
                self._descendant_body_creation_operation_summary_text()
            ),
            "descendant_body_creation_boundary_terminal_summary_reference": (
                self._descendant_body_creation_boundary_summary_text()
            ),
            "candidate_standing_operation_terminal_summary_reference": (
                self._candidate_standing_operation_summary_text()
            ),
            "existence_claim_evidence_check_terminal_summary_reference": (
                self._existence_claim_evidence_check_summary_text()
            ),
        }

    def _remove_marker(self, text: str, marker: str) -> str:
        """Remove every case-insensitive copy to avoid marker-substring residue."""

        return re.sub(re.escape(marker), "missing posture marker", text, flags=re.IGNORECASE)

    def _build_valid_synthetic_request(
        self, root: Path, text_overrides: dict[str, str] | None = None
    ) -> dict[str, Any]:
        texts = self._fixture_texts()
        texts.update(text_overrides or {})
        references: dict[str, str] = {}
        for field, filename in self.REFERENCE_FILENAMES.items():
            references[field] = str(self._write_markdown(root / filename, texts[field]))
        return resolver.build_declared_first_crossing_boundary_v0_min_request(**references)

    def _block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def _checks(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        checks = result.get("first_crossing_boundary_checks")
        self.assertIsInstance(checks, list)
        return checks

    def _failed_check_count(self, result: dict[str, Any]) -> int:
        return sum(check.get("passed") is False for check in self._checks(result))

    def _passed_check_count(self, result: dict[str, Any]) -> int:
        return sum(check.get("passed") is True for check in self._checks(result))

    def _boundary(self, result: dict[str, Any]) -> dict[str, Any]:
        boundary = result.get("first_crossing_boundary")
        self.assertIsInstance(boundary, dict)
        return boundary

    def assert_allowed_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))

    def assert_requires_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        for check in self._checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if isinstance(code, str):
                    self.assertIn(code, resolver.BLOCK_CODES)

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

    def assert_boundary_wrapper_separation(self, result: dict[str, Any]) -> None:
        boundary = self._boundary(result)
        for wrapper_field in (
            "outcome",
            "block",
            "first_crossing_boundary_checks",
            "non_claims",
            "first_crossing_boundary_summary",
            "first_crossing_boundary_metadata",
            "first_crossing_boundary_material",
        ):
            self.assertNotIn(wrapper_field, boundary)

    def assert_no_conversion(self, result: dict[str, Any]) -> None:
        boundary = self._boundary(result)
        for field in self.CONVERSION_FALSE_FIELDS:
            self.assertIs(boundary.get(field), False, field)

    def assert_final_false_posture(self, result: dict[str, Any]) -> None:
        self.assert_canonical_non_claims(result)
        self.assert_no_conversion(result)

    def _assert_allowed_material(self, result: dict[str, Any]) -> None:
        material = result.get("first_crossing_boundary_material")
        self.assertIsInstance(material, dict)
        self.assertEqual(
            set(material),
            {
                "descendant_body_creation_reference",
                "descendant_body_pair_reference",
                "boundary_evaluation",
            },
        )
        creation = material["descendant_body_creation_reference"]
        self.assertEqual(
            creation["prior_descendant_body_creation_operation_type"],
            resolver.PRIOR_DESCENDANT_BODY_CREATION_OPERATION_TYPE,
        )
        self.assertEqual(
            creation["prior_descendant_body_creation_operation_outcome"],
            resolver.PRIOR_DESCENDANT_BODY_CREATION_OPERATION_OUTCOME_REQUIRED,
        )
        self.assertEqual(
            creation["prior_descendant_body_creation_result"],
            resolver.PRIOR_DESCENDANT_BODY_CREATION_RESULT_REQUIRED,
        )
        for field in (
            "prior_descendant_body_creation_supported",
            "prior_descendant_body_creation_authorized",
            "prior_descendant_body_creation_performed",
            "prior_descendant_body_a_created",
            "prior_descendant_body_b_created",
            "prior_descendant_body_created",
        ):
            self.assertIs(creation[field], True, field)
        pair = material["descendant_body_pair_reference"]
        self.assertEqual(pair["descendant_body_a_id"], resolver.DESCENDANT_BODY_A_ID)
        self.assertEqual(pair["descendant_body_b_id"], resolver.DESCENDANT_BODY_B_ID)
        self.assertEqual(pair["descendant_body_pair_scope"], resolver.DESCENDANT_BODY_PAIR_SCOPE)
        for field in (
            "descendant_body_a_created",
            "descendant_body_b_created",
            "descendant_body_created",
            "descendant_body_pair_non_hierarchy_preserved",
            "descendant_bodies_remain_sibling",
        ):
            self.assertIs(pair[field], True, field)
        for field in (
            "descendant_body_a_is_first_crossing",
            "descendant_body_b_is_first_crossing",
            "descendant_body_creation_is_first_crossing",
            "descendant_body_is_crossing",
            "descendant_body_is_relation",
            "descendant_body_is_presence",
            "descendant_body_is_identity",
            "coupling_created",
        ):
            self.assertIs(pair[field], False, field)
        evaluation = material["boundary_evaluation"]
        self.assertIs(evaluation["first_crossing_operation_consideration_allowed"], True)
        self.assertEqual(
            evaluation["first_crossing_boundary_result"],
            "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED",
        )
        for field in (
            "first_crossing_authorized",
            "crossing_authorized",
            "first_crossing_performed",
            "crossing_performed",
            "relation_created",
            "coupling_created",
            "presence_established",
            "identity_created",
            "follow_on_authorized",
        ):
            self.assertIs(evaluation[field], False, field)

    def test_public_api_constants_and_default_request(self) -> None:
        for name in (
            "resolve_first_crossing_boundary_v0_min",
            "resolve_first_crossing_boundary_v0_min_from_path",
            "write_first_crossing_boundary_v0_min_result",
            "build_first_crossing_boundary_v0_min_summary",
            "build_declared_first_crossing_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_first_crossing_boundary_v0_min")
        self.assertEqual(resolver.BOUNDARY_ID, "first_crossing_boundary_001")
        self.assertEqual(resolver.BOUNDARY_TYPE, "FIRST_CROSSING_BOUNDARY")
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(
            resolver.BOUNDARY_SCOPE,
            "CONSIDER_FIRST_CROSSING_AFTER_DESCENDANT_BODY_CREATION_ONLY",
        )
        self.assertEqual(
            resolver.PRIOR_DESCENDANT_BODY_CREATION_OPERATION_TYPE,
            "DESCENDANT_BODY_CREATION_OPERATION",
        )
        self.assertEqual(
            resolver.PRIOR_DESCENDANT_BODY_CREATION_OPERATION_OUTCOME_REQUIRED,
            "DESCENDANT_BODY_CREATION_OPERATION_CREATED",
        )
        self.assertEqual(
            resolver.PRIOR_DESCENDANT_BODY_CREATION_RESULT_REQUIRED,
            "DESCENDANT_BODY_CREATION_SUPPORTED",
        )
        for name in (
            "PRIOR_DESCENDANT_BODY_CREATION_SUPPORTED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_CREATION_AUTHORIZED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_CREATION_PERFORMED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_A_CREATED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_B_CREATED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_CREATED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED",
            "PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED",
            "PRIOR_CROSSING_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertEqual(
            resolver.ADMISSIBLE_FUTURE_ROUTE,
            "FIRST_CROSSING_BOUNDARY_THEN_FIRST_CROSSING_OPERATION_ONLY",
        )
        self.assertEqual(resolver.DESCENDANT_BODY_A_ID, "descendant_body_a_001")
        self.assertEqual(resolver.DESCENDANT_BODY_B_ID, "descendant_body_b_001")
        self.assertEqual(resolver.DESCENDANT_BODY_PAIR_SCOPE, "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY")
        self.assertEqual(resolver.CANDIDATE_A_STANDING_SOURCE_ID, "descendant_body_basis_candidate_a_001")
        self.assertEqual(resolver.CANDIDATE_B_STANDING_SOURCE_ID, "descendant_body_basis_candidate_b_001")
        self.assertEqual(resolver.CANDIDATE_A_ROLE, "CANDIDATE_A")
        self.assertEqual(resolver.CANDIDATE_B_ROLE, "CANDIDATE_B")
        self.assertEqual(resolver.CANDIDATE_A_STANDING_LABEL, "CANDIDATE_A_STANDING")
        self.assertEqual(resolver.CANDIDATE_B_STANDING_LABEL, "CANDIDATE_B_STANDING")
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("integrity_host_v0_min_coexistence_first_crossing_boundary_v0_min"))
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_ALLOWED,
            resolver.OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        })
        for code in resolver.BLOCK_CODES:
            self.assertIsInstance(code, str)
        request = resolver.build_declared_first_crossing_boundary_v0_min_request()
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertTrue(str(request["first_crossing_boundary_spec_reference"]).endswith("FIRST_CROSSING_BOUNDARY_V0_MIN_SPEC.md"))
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(request[field], False)
            self.assertIs(request["declared_non_claims"][field], False)

    def test_synthetic_allowed_result_and_material(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self._build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_first_crossing_boundary_v0_min(request)
        self.assert_allowed_not_blocked(result)
        self.assertEqual(self._failed_check_count(result), 0)
        self.assertGreater(self._passed_check_count(result), 0)
        self.assertEqual(result["result_version"], "0.1.0")
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        for section in (
            "first_crossing_boundary_metadata",
            "declared_first_crossing_boundary_basis",
            "upstream_basis",
            "first_crossing_boundary",
            "first_crossing_boundary_material",
            "first_crossing_boundary_checks",
            "first_crossing_boundary_statement",
            "first_crossing_boundary_non_meaning",
            "boundary_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "first_crossing_boundary_summary",
        ):
            self.assertIn(section, result)
        boundary = self._boundary(result)
        self.assertEqual(boundary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(
            boundary["prior_descendant_body_creation_operation_type"],
            resolver.PRIOR_DESCENDANT_BODY_CREATION_OPERATION_TYPE,
        )
        self.assertEqual(
            boundary["prior_descendant_body_creation_operation_outcome_required"],
            resolver.PRIOR_DESCENDANT_BODY_CREATION_OPERATION_OUTCOME_REQUIRED,
        )
        self.assertEqual(
            boundary["prior_descendant_body_creation_result_required"],
            resolver.PRIOR_DESCENDANT_BODY_CREATION_RESULT_REQUIRED,
        )
        for field in (
            "prior_descendant_body_creation_supported_required",
            "prior_descendant_body_creation_authorized_required",
            "prior_descendant_body_creation_performed_required",
            "prior_descendant_body_a_created_required",
            "prior_descendant_body_b_created_required",
            "prior_descendant_body_created_required",
            *resolver.ALLOWED_TRUE_RECORDED_FIELDS,
        ):
            self.assertIs(boundary[field], True, field)
        self.assertEqual(
            boundary["first_crossing_boundary_result"],
            "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED",
        )
        self.assert_boundary_wrapper_separation(result)
        self.assert_canonical_non_claims(result)
        self.assert_no_conversion(result)
        marker_checks = [
            check for check in self._checks(result)
            if str(check.get("check_name", "")).endswith("markers present")
        ]
        self.assertTrue(marker_checks)
        self.assertTrue(all(check["passed"] is True for check in marker_checks))
        self._assert_allowed_material(result)

    def test_default_live_request_is_allowed_when_all_references_exist(self) -> None:
        request = resolver.build_declared_first_crossing_boundary_v0_min_request()
        references = [request["first_crossing_boundary_spec_reference"]]
        references.extend(request[field] for field, *_ in resolver.UPSTREAM_REQUIREMENTS)
        if not all((REPOSITORY_ROOT / Path(reference)).is_file() for reference in references):
            self.skipTest("default first-crossing boundary references are not all present")
        result = resolver.resolve_first_crossing_boundary_v0_min(request)
        self.assert_allowed_not_blocked(result)
        self.assertEqual(self._failed_check_count(result), 0)
        boundary = self._boundary(result)
        self.assertEqual(boundary["first_crossing_boundary_result"], "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED")
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(boundary[field], True, field)
        self.assert_no_conversion(result)
        self.assert_canonical_non_claims(result)

    def test_missing_or_insufficient_basis_requires_or_blocks_without_conversion(self) -> None:
        def missing(field: str) -> Callable[[Path, dict[str, Any]], None]:
            def apply(root: Path, request: dict[str, Any]) -> None:
                request[field] = str(root / "missing" / self.safe_json_filename(field))
            return apply

        cases: list[tuple[str, Callable[[Path, dict[str, Any]], None], str]] = []
        for field, *_rest, allowance in resolver.UPSTREAM_REQUIREMENTS:
            expected = resolver.OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION if allowance else resolver.OUTCOME_BLOCKED
            cases.append((f"missing {field}", missing(field), expected))
        for index, (field, _default, _missing_code, _marker_code, variants, _flag, allowance) in enumerate(resolver.UPSTREAM_REQUIREMENTS):
            for marker in variants[0]:
                def corrupt(root: Path, request: dict[str, Any], *, field: str = field, marker: str = marker) -> None:
                    path = Path(request[field])
                    self._write_markdown(
                        path,
                        self._remove_marker(path.read_text(encoding="utf-8"), marker),
                    )
                expected = resolver.OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION if allowance else resolver.OUTCOME_BLOCKED
                cases.append((f"corrupt {field} {index} {marker}", corrupt, expected))
        for case_name, apply, expected in cases:
            with self.subTest(case=case_name):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    apply(Path(directory), request)
                    result = resolver.resolve_first_crossing_boundary_v0_min(request)
                if expected == resolver.OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION:
                    self.assert_requires_not_blocked(result)
                    detail = result["boundary_result_detail"]
                    self.assertTrue(detail["missing_or_insufficient_descendant_body_creation"])
                    self.assertIs(self._boundary(result)["first_crossing_operation_consideration_allowed"], False)
                else:
                    self.assert_blocked_with_public_code(result)
                self.assert_final_false_posture(result)

    def test_intents_and_request_shape_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self._build_valid_synthetic_request(Path(directory))
            no_record = copy.deepcopy(request)
            no_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_first_crossing_boundary_v0_min(no_record)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            block = result["block"]
            self.assertIs(block["blocked"], False)
            boundary = self._boundary(result)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(boundary[field], False, field)
            self.assert_final_false_posture(result)

            explicit = copy.deepcopy(request)
            explicit["intent"] = resolver.INTENT_BLOCK
            blocked = resolver.resolve_first_crossing_boundary_v0_min(explicit)
            self.assert_blocked_with_public_code(blocked)
            self.assertEqual(self._block_code(blocked), "EXPLICIT_BLOCK_REQUESTED")
            self.assert_final_false_posture(blocked)

            malformed_cases: list[tuple[str, Any]] = [
                ("non-mapping", []),
                ("unsupported intent", {**request, "intent": "UNSUPPORTED"}),
            ]
            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                invalid = copy.deepcopy(request)
                invalid[field] = (not expected) if isinstance(expected, bool) else f"wrong_{expected}"
                malformed_cases.append((field, invalid))
            for name, payload in malformed_cases:
                with self.subTest(case=name):
                    invalid_result = resolver.resolve_first_crossing_boundary_v0_min(payload)
                    self.assert_blocked_with_public_code(invalid_result)
                    self.assert_final_false_posture(invalid_result)

    def test_target_and_upstream_marker_classes_are_enforced(self) -> None:
        for class_name, variants in resolver.TARGET_SPEC_MARKER_CLASSES:
            marker = variants[0][-1]
            with self.subTest(target_marker_class=class_name):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    path = Path(request["first_crossing_boundary_spec_reference"])
                    self._write_markdown(
                        path,
                        self._remove_marker(path.read_text(encoding="utf-8"), marker),
                    )
                    result = resolver.resolve_first_crossing_boundary_v0_min(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(self._block_code(result), "FIRST_CROSSING_BOUNDARY_SPEC_MARKER_MISSING")
                self.assert_final_false_posture(result)

    def test_prohibited_requests_and_top_level_posture_block(self) -> None:
        cases: list[tuple[str, str, str]] = [
            (field, field, code) for field, code in resolver.PROHIBITED_REQUEST_FLAGS.items()
        ]
        cases.extend(
            (field, field, "RESULT_POSTURE_PRECLAIMED" if field in resolver.ALLOWED_TRUE_RECORDED_FIELDS else "NON_CLAIM_MISSING_OR_FLIPPED")
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS
        )
        for name, field, expected_code in cases:
            with self.subTest(case=name):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    request[field] = True
                    result = resolver.resolve_first_crossing_boundary_v0_min(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(self._block_code(result), expected_code)
                self.assert_final_false_posture(result)

    def test_declared_non_claim_canonicalization_blocks_flips_and_malformed_inputs(self) -> None:
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(flipped_non_claim=field):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    request["declared_non_claims"][field] = True
                    result = resolver.resolve_first_crossing_boundary_v0_min(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(self._block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                self.assert_final_false_posture(result)
        malformed: list[tuple[str, Any]] = [
            ("missing", None),
            ("non-mapping", []),
            ("missing-field", "missing-field"),
            ("non-bool", "non-bool"),
        ]
        for name, value in malformed:
            with self.subTest(declared_non_claims=name):
                with tempfile.TemporaryDirectory() as directory:
                    request = self._build_valid_synthetic_request(Path(directory))
                    if value is None:
                        request.pop("declared_non_claims")
                    elif value == "missing-field":
                        request["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
                    elif value == "non-bool":
                        request["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = "false"
                    else:
                        request["declared_non_claims"] = value
                    result = resolver.resolve_first_crossing_boundary_v0_min(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(self._block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                self.assert_final_false_posture(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request = self._build_valid_synthetic_request(root / "basis")
            request_path = self._write_json(root / self.safe_json_filename("valid request"), request)
            result = resolver.resolve_first_crossing_boundary_v0_min_from_path(request_path)
            self.assert_allowed_not_blocked(result)
            self.assertEqual(self._failed_check_count(result), 0)
            self.assertEqual(result["result_version"], "0.1.0")
            self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
            for name, contents, expected_code in (
                ("missing", None, "REQUEST_PATH_UNREADABLE"),
                ("invalid", "not JSON", "REQUEST_JSON_INVALID"),
                ("array", [], "REQUEST_NOT_MAPPING"),
            ):
                with self.subTest(path_case=name):
                    path = root / self.safe_json_filename(name)
                    if contents is not None:
                        if isinstance(contents, str):
                            path.write_text(contents, encoding="utf-8")
                        else:
                            self._write_json(path, contents)
                    malformed = resolver.resolve_first_crossing_boundary_v0_min_from_path(path)
                    self.assert_blocked_with_public_code(malformed)
                    self.assertEqual(self._block_code(malformed), expected_code)
            output = root / "first_crossing_output" / resolver.DETERMINISTIC_FILENAME
            first_written = resolver.write_first_crossing_boundary_v0_min_result(result, output)
            second_written = resolver.write_first_crossing_boundary_v0_min_result(result, output)
            self.assertTrue(first_written.is_file())
            self.assertTrue(second_written.is_file())
            self.assertNotEqual(first_written, second_written)
            self.assertEqual(json.loads(first_written.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertIn("first_crossing_boundary_v0_min_result", first_written.name)
            self.assertIn("first_crossing_boundary", str(resolver.OUTPUT_ROOT))
            upstream_roots = (
                "descendant_body_creation_operation",
                "descendant_body_creation_boundary",
                "candidate_standing_operation",
                "runtime",
                "daemon",
            )
            self.assertFalse(any(root_name in first_written.parts for root_name in upstream_roots))

    def test_summary_and_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self._build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_first_crossing_boundary_v0_min(request)
            summary = resolver.build_first_crossing_boundary_v0_min_summary(result)
        self.assert_allowed_not_blocked(result)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        for field in (
            "boundary_id",
            "boundary_type",
            "boundary_version",
            "boundary_scope",
            "prior_descendant_body_creation_operation_type",
            "prior_descendant_body_creation_operation_outcome_required",
            "prior_descendant_body_creation_result_required",
            "first_crossing_boundary_result",
            "first_crossing_operation_consideration_allowed",
            *resolver.ALLOWED_TRUE_RECORDED_FIELDS,
        ):
            self.assertIn(field, summary)
        self.assertEqual(summary["first_crossing_boundary_result"], "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED")
        self.assertIs(summary["first_crossing_operation_consideration_allowed"], True)
        self.assertEqual(summary["missing_or_insufficient_descendant_body_creation"], [])
        self._assert_allowed_material(result)
        self.assert_boundary_wrapper_separation(result)
        self.assert_canonical_non_claims(result)

    def test_non_mutation_and_hostile_content_containment(self) -> None:
        sentinel = "RAW_HIDDEN_CONTAMINATED_LINEAGE_MUST_NOT_RETURN"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            texts = {field: f"{text}{sentinel}\n" for field, text in self._fixture_texts().items()}
            request = self._build_valid_synthetic_request(root, texts)
            request["hostile_payload"] = {"raw": sentinel, "nested": [sentinel]}
            before_request = copy.deepcopy(request)
            before_texts = {
                field: Path(path).read_text(encoding="utf-8")
                for field, path in request.items()
                if field in self.REFERENCE_FILENAMES
            }
            result = resolver.resolve_first_crossing_boundary_v0_min(request)
            after_texts = {
                field: Path(path).read_text(encoding="utf-8")
                for field, path in request.items()
                if field in self.REFERENCE_FILENAMES
            }
        self.assertEqual(request, before_request)
        self.assertEqual(after_texts, before_texts)
        self.assert_allowed_not_blocked(result)
        self.assertNotIn(sentinel, json.dumps(result, sort_keys=True))
        self.assert_no_conversion(result)
        self.assert_canonical_non_claims(result)


if __name__ == "__main__":
    unittest.main()
