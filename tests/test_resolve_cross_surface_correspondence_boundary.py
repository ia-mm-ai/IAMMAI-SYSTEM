"""Tests for bounded cross-surface correspondence boundary resolution.

This suite audits one correspondence boundary resolver. It verifies recognized
correspondence, no-correspondence, and blocked collapse posture without opening
workflow, routing, signal use, successor pressure, or continuation.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_cross_surface_correspondence_boundary as resolver


TOP_LEVEL_SECTIONS = {
    "cross_surface_correspondence_metadata",
    "selected_surfaces",
    "declared_correspondence_question",
    "correspondence_basis",
    "correspondence_checks",
    "correspondence_result",
    "correspondence_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "cross_surface_correspondence_summary",
}

EXPECTED_CHECK_NAMES = {
    "selected_surfaces_are_parseable_mappings",
    "selected_surfaces_exist",
    "selected_surfaces_have_identity",
    "selected_surfaces_have_outcome",
    "correspondence_question_declared",
    "correspondence_type_supported",
    "source_basis_known_where_required",
    "source_downstream_posture_bounded_where_required",
    "no_source_replacement",
    "no_authority_creation",
    "no_currentness_creation",
    "no_permission_creation",
    "no_surface_merge",
    "no_equivalence_creation",
    "no_explanation_ownership_creation",
    "no_signal_created_by_default",
    "no_presence_established",
    "no_threshold_met",
    "no_truth_created",
    "no_action_authorized",
    "no_consequence_created",
    "no_scope_widening",
    "no_hidden_mismatch",
    "no_lineage_overwrite",
    "no_precursor_upgrade_to_current_law",
    "no_self_orientation_successor_forced",
    "no_conformance_successor_forced",
    "no_continuation_authorized",
    "no_latest_file_currentness",
    "no_recency_fraud",
    "no_mutation_replay_or_merge",
    "required_non_claims_remain_false",
}

NON_MEANING_TRUE_KEYS = {
    "does_not_create_equivalence",
    "does_not_merge_surfaces",
    "does_not_create_explanation_ownership",
    "does_not_replace_source",
    "does_not_transfer_currentness",
    "does_not_transfer_permission",
    "does_not_transfer_authority",
    "does_not_create_signal_by_default",
    "does_not_establish_presence",
    "does_not_establish_threshold",
    "does_not_create_truth",
    "does_not_authorize_action",
    "does_not_create_consequence",
    "does_not_open_next_work",
    "does_not_force_self_orientation_successor",
    "does_not_force_conformance_successor",
    "does_not_create_routing",
    "does_not_create_workflow",
    "does_not_create_body_relevance_medium",
    "does_not_create_distributed_standing",
    "does_not_create_multi_carrier_law",
}

OPEN_SURFACES = {
    "presence law",
    "threshold law",
    "truth law",
    "action/consequence law",
    "multi-carrier relation law",
    "persistence/registry law",
    "generalized vessel relation lifecycle",
    "body relevance medium",
    "signal series or accumulation logic",
    "distributed standing",
    "future self-orientation successor only if separately justified",
}


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    assert isinstance(value, dict)
    return value


def _false_non_claims(**updates: bool) -> dict[str, bool]:
    claims = {key: False for key in resolver.NON_CLAIMS}
    claims.update(updates)
    return claims


def _surface(
    surface_id: str = "surface-a",
    *,
    outcome: str = "SELF_ORIENTED",
    source_basis_id: str | None = "source-basis-001",
    surface_path: str | None = None,
    surface_type: str = "bounded_standing_surface",
    source_downstream_posture: str = "downstream_or_local_posture_bounded",
    non_claims: dict[str, bool] | None = None,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    surface: dict[str, object] = {
        "surface_id": surface_id,
        "surface_path": surface_path or f"artifacts/surfaces/{surface_id}.json",
        "outcome": outcome,
        "surface_type": surface_type,
        "source_downstream_posture": source_downstream_posture,
        "non_claims": copy.deepcopy(non_claims or _false_non_claims()),
    }
    if source_basis_id is not None:
        surface["source_basis_id"] = source_basis_id
    if extra:
        surface.update(copy.deepcopy(extra))
    return surface


def _recognized_alignment() -> dict:
    return resolver.resolve_cross_surface_correspondence_boundary(
        selected_surfaces=[
            _surface("surface-a"),
            _surface("surface-b", outcome="BODY_CONFORMANT"),
        ],
        declared_correspondence_question=(
            "Do selected surfaces preserve aligned non-claims?"
        ),
        correspondence_type="NON_CLAIM_ALIGNMENT",
    )


def _resolve(
    surfaces: list[dict[str, object]],
    relation_type: str = "NON_CLAIM_ALIGNMENT",
    question: str = "Do selected surfaces correspond?",
) -> dict:
    return resolver.resolve_cross_surface_correspondence_boundary(
        selected_surfaces=surfaces,
        declared_correspondence_question=question,
        correspondence_type=relation_type,
    )


class CrossSurfaceCorrespondenceBoundaryTests(unittest.TestCase):
    def assertBlocked(self, result: dict, code: str) -> None:
        self.assertEqual("BLOCKED", result["outcome"])
        self.assertEqual(code, result["block"]["code"])

    def assertTopLevelShape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result.keys()))

    def assertNonClaimsFalse(self, result: dict) -> None:
        for key in resolver.NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIn(key, result["non_claims"])
                self.assertIs(result["non_claims"][key], False)

    def test_successful_non_claim_alignment(self) -> None:
        result = _recognized_alignment()

        self.assertIsInstance(result, dict)
        self.assertTopLevelShape(result)
        self.assertEqual("CORRESPONDENCE_RECOGNIZED", result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        self.assertEqual("NON_CLAIM_ALIGNMENT", result["correspondence_basis"]["correspondence_type"])
        self.assertEqual(
            "Do selected surfaces preserve aligned non-claims?",
            result["declared_correspondence_question"],
        )
        self.assertEqual(2, len(result["selected_surfaces"]))
        self.assertIs(result["correspondence_result"]["correspondence_recognized"], True)
        self.assertIs(result["correspondence_result"]["no_correspondence"], False)

    def test_metadata(self) -> None:
        metadata = _recognized_alignment()["cross_surface_correspondence_metadata"]

        for key in (
            "cross_surface_correspondence_result_id",
            "cross_surface_correspondence_result_type",
            "cross_surface_correspondence_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["cross_surface_correspondence_result_version"])
        self.assertEqual(
            "resolve_cross_surface_correspondence_boundary",
            metadata["resolver_module"],
        )

    def test_selected_surfaces_normalization(self) -> None:
        selected = _recognized_alignment()["selected_surfaces"]

        for index, surface in enumerate(selected):
            self.assertEqual(index, surface["surface_index"])
            self.assertTrue(surface["surface_id"])
            self.assertTrue(surface["surface_path"])
            self.assertTrue(surface["surface_outcome"])
            self.assertTrue(surface["surface_type"])
            self.assertTrue(surface["source_basis_id"] or surface["source_basis_path"])
            self.assertTrue(surface["source_downstream_posture"])
            self.assertIsInstance(surface["non_claims"], dict)
            self.assertTrue(surface["raw_surface_family_hint"])

    def test_correspondence_basis(self) -> None:
        basis = _recognized_alignment()["correspondence_basis"]

        self.assertEqual("NON_CLAIM_ALIGNMENT", basis["correspondence_type"])
        self.assertIn("BASIS_MATCH", basis["permitted_correspondence_types"])
        self.assertEqual(2, basis["selected_surface_count"])
        self.assertEqual(["surface-a", "surface-b"], basis["selected_surface_ids"])
        self.assertEqual(["SELF_ORIENTED", "BODY_CONFORMANT"], basis["selected_surface_outcomes"])
        self.assertEqual(["source-basis-001", "source-basis-001"], basis["source_basis_values"])
        self.assertIs(basis["rank_preserved"], True)
        self.assertIs(basis["source_preserved"], True)
        self.assertIs(basis["scope_preserved"], True)
        self.assertIs(basis["lineage_preserved"], True)
        self.assertIs(basis["non_claims_preserved"], True)
        self.assertIs(basis["local_outcomes_remain_local"], True)
        self.assertIs(basis["correspondence_does_not_command_work"], True)

    def test_correspondence_non_meaning(self) -> None:
        non_meaning = _recognized_alignment()["correspondence_non_meaning"]

        for key in NON_MEANING_TRUE_KEYS:
            with self.subTest(key=key):
                self.assertIs(non_meaning[key], True)

    def test_what_remains_open(self) -> None:
        open_posture = _recognized_alignment()["what_remains_open"]

        self.assertTrue(OPEN_SURFACES.issubset(set(open_posture["open_surfaces"])))
        self.assertIs(open_posture["open_means_not_scheduled"], True)
        self.assertIs(open_posture["open_means_not_authorized"], True)
        self.assertIs(open_posture["open_means_not_executed"], True)

    def test_correspondence_checks(self) -> None:
        checks = _recognized_alignment()["correspondence_checks"]
        check_names = {check["check_name"] for check in checks}

        self.assertTrue(EXPECTED_CHECK_NAMES.issubset(check_names))
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIs(check["passed"], True)
        self.assertEqual(0, _recognized_alignment()["cross_surface_correspondence_summary"]["failed_check_count"])

    def test_summary_helper(self) -> None:
        result = _recognized_alignment()
        summary = resolver.build_cross_surface_correspondence_summary(result)

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(2, summary["selected_surface_count"])
        self.assertEqual(["surface-a", "surface-b"], summary["selected_surface_ids"])
        self.assertEqual(["SELF_ORIENTED", "BODY_CONFORMANT"], summary["selected_surface_outcomes"])
        self.assertEqual(result["declared_correspondence_question"], summary["declared_correspondence_question"])
        self.assertEqual("NON_CLAIM_ALIGNMENT", summary["correspondence_type"])
        self.assertIs(summary["correspondence_recognized"], True)
        self.assertIs(summary["no_correspondence"], False)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(summary["source_rank_scope_lineage_non_claims_preserved"], True)
        for key in (
            "correspondence_created_authority",
            "correspondence_created_currentness",
            "correspondence_created_permission",
            "correspondence_created_signal",
            "correspondence_established_presence",
            "correspondence_established_threshold",
            "correspondence_created_truth",
            "correspondence_authorized_action",
            "correspondence_created_consequence",
            "self_orientation_successor_forced",
            "conformance_successor_forced",
            "continuation_authorized",
        ):
            self.assertIs(summary[key], False)
        self.assertIsInstance(summary["key_non_claims"], dict)

    def test_result_level_non_claims_for_recognized_and_blocked(self) -> None:
        recognized = _recognized_alignment()
        blocked = _resolve(
            [
                _surface("surface-a"),
                _surface("surface-b", extra={"authority_created": True}),
            ],
            relation_type="BASIS_MATCH",
        )

        self.assertNonClaimsFalse(recognized)
        self.assertNonClaimsFalse(blocked)

    def test_basis_match(self) -> None:
        result = _resolve(
            [_surface("surface-a"), _surface("surface-b")],
            relation_type="BASIS_MATCH",
        )

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", result["outcome"])
        self.assertEqual(
            ["source-basis-001", "source-basis-001"],
            result["correspondence_result"]["evidence"]["source_basis_values"],
        )

    def test_basis_mismatch(self) -> None:
        result = _resolve(
            [
                _surface("surface-a", source_basis_id="source-basis-001"),
                _surface("surface-b", source_basis_id="source-basis-002"),
            ],
            relation_type="BASIS_MISMATCH",
        )

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", result["outcome"])
        self.assertEqual(
            ["source-basis-001", "source-basis-002"],
            result["correspondence_result"]["evidence"]["source_basis_values"],
        )
        self.assertIs(result["non_claims"]["source_replaced"], False)

    def test_downstream_recognition(self) -> None:
        result = _resolve(
            [
                _surface("surface-a"),
                _surface(
                    "surface-b",
                    extra={"selected_surface_id": "surface-a"},
                ),
            ],
            relation_type="DOWNSTREAM_RECOGNITION",
        )

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", result["outcome"])
        self.assertTrue(result["correspondence_result"]["evidence"]["recognized_references"])
        self.assertIs(result["non_claims"]["authority_created"], False)
        self.assertIs(result["non_claims"]["currentness_created"], False)
        self.assertIs(result["non_claims"]["permission_created"], False)

    def test_scope_alignment(self) -> None:
        result = _resolve(
            [
                _surface("surface-a", extra={"scope_id": "scope-001"}),
                _surface("surface-b", extra={"declared_scope_id": "scope-001"}),
            ],
            relation_type="SCOPE_ALIGNMENT",
        )

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", result["outcome"])
        self.assertEqual(["scope-001"], result["correspondence_result"]["evidence"]["common_values"])

    def test_scope_mismatch(self) -> None:
        result = _resolve(
            [
                _surface("surface-a", extra={"scope_id": "scope-001"}),
                _surface("surface-b", extra={"declared_scope_id": "scope-002"}),
            ],
            relation_type="SCOPE_MISMATCH",
        )

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", result["outcome"])
        self.assertEqual([["scope-001"], ["scope-002"]], result["correspondence_result"]["evidence"]["scope_or_matter_values"])
        self.assertIs(result["non_claims"].get("applied_outside_declared_scope", False), False)

    def test_lineage_reference(self) -> None:
        result = _resolve(
            [
                _surface("surface-a"),
                _surface("surface-b", extra={"basis_surface_id": "surface-a"}),
            ],
            relation_type="LINEAGE_REFERENCE",
        )

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", result["outcome"])
        self.assertTrue(result["correspondence_result"]["evidence"]["lineage_references"])

    def test_closure_alignment(self) -> None:
        v6 = _surface("v6-surface", outcome="SELF_ORIENTED")
        conformance = _surface(
            "conformance-surface",
            outcome="BODY_CONFORMANT",
            extra={"selected_self_orientation_v6_basis": {"surface_id": "v6-surface"}},
        )
        closure = _surface(
            "closure-surface",
            outcome="CONFORMANCE_CLOSURE_RECORDED",
            extra={
                "selected_current_body_conformance_basis": {
                    "surface_id": "conformance-surface"
                },
                "selected_self_orientation_v6_basis": {"surface_id": "v6-surface"},
            },
        )

        result = _resolve([v6, conformance, closure], relation_type="CLOSURE_ALIGNMENT")

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", result["outcome"])
        self.assertEqual("CLOSURE_ALIGNMENT", result["correspondence_result"]["correspondence_type"])
        self.assertTrue(result["correspondence_result"]["evidence"]["alignment_references"])
        self.assertIs(result["non_claims"]["permission_created"], False)
        self.assertIs(result["non_claims"]["authority_created"], False)
        self.assertIs(result["non_claims"]["signal_created_by_default"], False)
        self.assertIs(result["non_claims"]["continuation_authorized"], False)

    def test_refusal_visible(self) -> None:
        result = _resolve(
            [
                _surface("surface-a"),
                _surface(
                    "blocked-surface",
                    outcome="BLOCKED",
                    extra={"block": {"code": "BOUNDED_REFUSAL", "reason": "refused"}},
                ),
            ],
            relation_type="REFUSAL_VISIBLE",
        )

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", result["outcome"])
        self.assertTrue(result["correspondence_result"]["evidence"]["visible_refusals"])
        self.assertEqual("blocked-surface", result["selected_surfaces"][1]["surface_id"])

    def test_declared_no_correspondence(self) -> None:
        result = _resolve(
            [_surface("surface-a"), _surface("surface-b")],
            relation_type="NO_CORRESPONDENCE",
        )

        self.assertEqual("NO_CORRESPONDENCE", result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertEqual(2, len(result["selected_surfaces"]))

    def test_positive_type_missing_evidence_returns_no_correspondence(self) -> None:
        result = _resolve(
            [_surface("surface-a"), _surface("surface-b")],
            relation_type="LINEAGE_REFERENCE",
        )

        self.assertEqual("NO_CORRESPONDENCE", result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertEqual(2, len(result["selected_surfaces"]))
        for key in ("authority_created", "permission_created", "currentness_created"):
            self.assertIs(result["non_claims"][key], False)

    def test_path_based_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path_a = Path(tmp) / "surface_a.json"
            path_b = Path(tmp) / "surface_b.json"
            surface_a = _surface("surface-a")
            surface_b = _surface("surface-b", outcome="BODY_CONFORMANT")
            _write_json(path_a, surface_a)
            _write_json(path_b, surface_b)

            path_result = resolver.resolve_cross_surface_correspondence_boundary_from_paths(
                [path_a, path_b],
                "Do selected surfaces preserve aligned non-claims?",
                "NON_CLAIM_ALIGNMENT",
            )
            mapping_result = resolver.resolve_cross_surface_correspondence_boundary(
                [surface_a, surface_b],
                "Do selected surfaces preserve aligned non-claims?",
                "NON_CLAIM_ALIGNMENT",
            )

        self.assertEqual("CORRESPONDENCE_RECOGNIZED", path_result["outcome"])
        self.assertEqual(str(path_a), path_result["selected_surfaces"][0]["surface_path"])
        self.assertEqual(str(path_b), path_result["selected_surfaces"][1]["surface_path"])
        self.assertEqual(set(mapping_result.keys()), set(path_result.keys()))

    def test_write_behavior(self) -> None:
        result = _recognized_alignment()
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "result.json"
            written = resolver.write_cross_surface_correspondence_result(result, output_path)

            self.assertEqual(output_path, written)
            self.assertTrue(written.exists())
            parsed = _read_json(written)

        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed.keys()))

    def test_default_output_path_behavior(self) -> None:
        result = _recognized_alignment()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "correspondence"
            with mock.patch.object(resolver, "CROSS_SURFACE_CORRESPONDENCE_BOUNDARY_ROOT", root):
                first = resolver.write_cross_surface_correspondence_result(result)
                second = resolver.write_cross_surface_correspondence_result(result)

            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertTrue(first.name.startswith("NON_CLAIM_ALIGNMENT__surface-a__"))
            self.assertTrue(second.name.startswith("NON_CLAIM_ALIGNMENT__surface-a__"))
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        surfaces = [_surface("surface-a"), _surface("surface-b")]
        before = copy.deepcopy(surfaces)

        first = _resolve(surfaces)
        second = _resolve(surfaces)

        self.assertEqual(before, surfaces)
        self.assertEqual(before, surfaces)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            resolver.write_cross_surface_correspondence_result(first, output)
            self.assertTrue(output.exists())
        self.assertEqual("CORRESPONDENCE_RECOGNIZED", second["outcome"])

    def test_blocking_missing_selected_surfaces(self) -> None:
        empty = resolver.resolve_cross_surface_correspondence_boundary(
            selected_surfaces=[],
            declared_correspondence_question="Do selected surfaces correspond?",
            correspondence_type="NON_CLAIM_ALIGNMENT",
        )
        one = _resolve([_surface("surface-a")])

        self.assertBlocked(empty, "SELECTED_SURFACE_MISSING")
        self.assertBlocked(one, "SELECTED_SURFACE_MISSING")

    def test_blocking_malformed_selected_surface_mapping(self) -> None:
        result = resolver.resolve_cross_surface_correspondence_boundary(
            selected_surfaces=[_surface("surface-a"), "not-a-mapping"],  # type: ignore[list-item]
            declared_correspondence_question="Do selected surfaces correspond?",
            correspondence_type="NON_CLAIM_ALIGNMENT",
        )

        self.assertBlocked(result, "SELECTED_SURFACE_MALFORMED")

    def test_blocking_path_unreadable_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            malformed = tmp_path / "malformed.json"
            array_path = tmp_path / "array.json"
            malformed.write_text("{", encoding="utf-8")
            array_path.write_text("[]", encoding="utf-8")

            missing_result = resolver.resolve_cross_surface_correspondence_boundary_from_paths(
                [tmp_path / "missing.json"],
                "Do selected surfaces correspond?",
                "NON_CLAIM_ALIGNMENT",
            )
            malformed_result = resolver.resolve_cross_surface_correspondence_boundary_from_paths(
                [malformed],
                "Do selected surfaces correspond?",
                "NON_CLAIM_ALIGNMENT",
            )
            array_result = resolver.resolve_cross_surface_correspondence_boundary_from_paths(
                [array_path],
                "Do selected surfaces correspond?",
                "NON_CLAIM_ALIGNMENT",
            )

        self.assertBlocked(missing_result, "SELECTED_SURFACE_UNREADABLE")
        self.assertBlocked(malformed_result, "SELECTED_SURFACE_MALFORMED")
        self.assertBlocked(array_result, "SELECTED_SURFACE_MALFORMED")

    def test_blocking_identity_missing(self) -> None:
        bad_surface = _surface("surface-a")
        bad_surface.pop("surface_id")

        result = _resolve([bad_surface, _surface("surface-b")])

        self.assertBlocked(result, "SELECTED_SURFACE_IDENTITY_MISSING")

    def test_blocking_outcome_missing(self) -> None:
        bad_surface = _surface("surface-a")
        bad_surface.pop("outcome")

        result = _resolve([bad_surface, _surface("surface-b")])

        self.assertBlocked(result, "SELECTED_SURFACE_OUTCOME_MISSING")

    def test_blocking_undeclared_question(self) -> None:
        result = resolver.resolve_cross_surface_correspondence_boundary(
            selected_surfaces=[_surface("surface-a"), _surface("surface-b")],
            declared_correspondence_question=" ",
            correspondence_type="NON_CLAIM_ALIGNMENT",
        )

        self.assertBlocked(result, "CORRESPONDENCE_QUESTION_UNDECLARED")

    def test_blocking_unsupported_correspondence_type(self) -> None:
        result = _resolve(
            [_surface("surface-a"), _surface("surface-b")],
            relation_type="UNBOUNDED_RELATION",
        )

        self.assertBlocked(result, "CORRESPONDENCE_TYPE_UNSUPPORTED")

    def test_blocking_basis_types_require_exposed_basis(self) -> None:
        for relation_type in ("BASIS_MATCH", "BASIS_MISMATCH"):
            with self.subTest(relation_type=relation_type):
                result = _resolve(
                    [
                        _surface("surface-a", source_basis_id=None),
                        _surface("surface-b", source_basis_id=None),
                    ],
                    relation_type=relation_type,
                )
                self.assertBlocked(result, "SOURCE_BASIS_UNKNOWN")

    def test_blocking_source_replacement(self) -> None:
        result = _resolve(
            [_surface("surface-a"), _surface("surface-b", extra={"source_replaced": True})],
            relation_type="BASIS_MATCH",
        )

        self.assertBlocked(result, "CORRESPONDENCE_ATTEMPTS_SOURCE_REPLACEMENT")

    def test_blocking_authority_currentness_permission(self) -> None:
        cases = [
            ("authority_created", "CORRESPONDENCE_ATTEMPTS_AUTHORITY"),
            ("currentness_created", "CORRESPONDENCE_ATTEMPTS_CURRENTNESS"),
            ("permission_created", "CORRESPONDENCE_ATTEMPTS_PERMISSION"),
        ]
        for flag, code in cases:
            with self.subTest(flag=flag):
                result = _resolve([_surface("surface-a"), _surface("surface-b", extra={flag: True})])
                self.assertBlocked(result, code)

    def test_blocking_merge_equivalence_explanation_ownership(self) -> None:
        for flag in ("surface_merged", "surface_equivalence_created", "explanation_ownership_created"):
            with self.subTest(flag=flag):
                result = _resolve([_surface("surface-a"), _surface("surface-b", extra={flag: True})])
                self.assertBlocked(result, "CORRESPONDENCE_ATTEMPTS_MERGE")

    def test_blocking_signal_presence_threshold_truth_action_consequence(self) -> None:
        cases = [
            ("signal_created_by_default", "CORRESPONDENCE_CREATES_SIGNAL_BY_DEFAULT"),
            ("presence_established", "CORRESPONDENCE_ESTABLISHES_PRESENCE"),
            ("threshold_met", "CORRESPONDENCE_ESTABLISHES_THRESHOLD"),
            ("truth_created", "CORRESPONDENCE_CREATES_TRUTH"),
            ("action_authorized", "CORRESPONDENCE_AUTHORIZES_ACTION"),
            ("consequence_created", "CORRESPONDENCE_CREATES_CONSEQUENCE"),
        ]
        for flag, code in cases:
            with self.subTest(flag=flag):
                result = _resolve([_surface("surface-a"), _surface("surface-b", extra={flag: True})])
                self.assertBlocked(result, code)

    def test_blocking_scope_widening_hidden_mismatch_lineage_overwrite(self) -> None:
        cases = [
            ("scope_widened", "CORRESPONDENCE_WIDENS_SCOPE"),
            ("mismatch_hidden", "CORRESPONDENCE_HIDES_MISMATCH"),
            ("lineage_overwritten", "CORRESPONDENCE_OVERWRITES_LINEAGE"),
        ]
        for flag, code in cases:
            with self.subTest(flag=flag):
                result = _resolve([_surface("surface-a"), _surface("surface-b", extra={flag: True})])
                self.assertBlocked(result, code)

    def test_blocking_precursor_upgrade(self) -> None:
        result = _resolve(
            [_surface("surface-a"), _surface("surface-b", extra={"precursor_upgraded_to_current_law": True})]
        )

        self.assertBlocked(result, "CORRESPONDENCE_UPGRADES_PRECURSOR_TO_CURRENT_LAW")

    def test_blocking_successor_forcing_and_continuation(self) -> None:
        cases = [
            ("self_orientation_successor_forced", "CORRESPONDENCE_FORCES_SELF_ORIENTATION_SUCCESSOR"),
            ("conformance_successor_forced", "CORRESPONDENCE_FORCES_CONFORMANCE_SUCCESSOR"),
            ("continuation_authorized", "CORRESPONDENCE_AUTHORIZES_CONTINUATION"),
        ]
        for flag, code in cases:
            with self.subTest(flag=flag):
                result = _resolve([_surface("surface-a"), _surface("surface-b", extra={flag: True})])
                self.assertBlocked(result, code)

    def test_blocking_latest_file_currentness_or_recency_fraud(self) -> None:
        for flag in ("latest_file_currentness", "recency_fraud"):
            with self.subTest(flag=flag):
                result = _resolve([_surface("surface-a"), _surface("surface-b", extra={flag: True})])
                self.assertBlocked(result, "LATEST_FILE_CURRENTNESS")

    def test_blocking_mutation_replay_merge_detected(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                result = _resolve([_surface("surface-a"), _surface("surface-b", extra={flag: True})])
                self.assertBlocked(result, "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_blocking_non_claim_flipped(self) -> None:
        result = _resolve(
            [
                _surface("surface-a"),
                _surface("surface-b", non_claims=_false_non_claims(authority_created=True)),
            ]
        )

        self.assertEqual("BLOCKED", result["outcome"])
        self.assertIn(
            result["block"]["code"],
            {"CORRESPONDENCE_ATTEMPTS_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self.assertIs(result["non_claims"]["authority_created"], True)


if __name__ == "__main__":
    unittest.main()
