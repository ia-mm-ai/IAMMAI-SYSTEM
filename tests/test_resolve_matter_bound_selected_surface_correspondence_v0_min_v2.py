"""Tests for the pure V2 matter-bound correspondence resolver.

The suite preserves one matter, one ordered closed manifest, one declared
question, one relation type, and one completion posture. It verifies relation
support without importing the older resolver's broader extraction semantics.
"""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_matter_bound_selected_surface_correspondence_v0_min_v2 as resolver


TOP_LEVEL_KEYS = {
    "metadata",
    "matter",
    "selected_surface_manifest",
    "declared_correspondence_question",
    "correspondence_basis",
    "finding",
    "checks",
    "result",
    "non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
}

SURFACE_KEYS = {
    "selected_position",
    "surface_id",
    "surface_reference",
    "surface_outcome",
    "surface_rank",
    "source_basis",
    "surface_scope",
    "lineage_references",
    "source_downstream_posture",
    "non_claims",
}


def _declared_non_claims() -> dict[str, bool]:
    return {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS}


def _reconstruction_posture() -> dict[str, bool]:
    return {
        key: False for key in resolver.REQUIRED_FALSE_RECONSTRUCTION_POSTURES
    }


def _surface(position: int, suffix: str) -> dict[str, object]:
    return {
        "selected_position": position,
        "surface_id": f"surface-{suffix}",
        "surface_reference": f"held/surface-{suffix}.json",
        "surface_outcome": f"SURFACE_{suffix.upper()}_STANDS",
        "surface_rank": f"rank-{suffix}",
        "source_basis": f"source-basis-{suffix}",
        "surface_scope": "matter-001-only",
        "lineage_references": [f"lineage-{suffix}-001"],
        "source_downstream_posture": f"bounded-{suffix}-posture",
        "non_claims": {
            "surface_authority_created": False,
            "surface_currentness_created": False,
        },
    }


def _request(
    relation_type: str = "BASIS_MATCH",
    *,
    supported: bool = True,
    evidence_relation_type: str | None = None,
) -> dict[str, object]:
    manifest = [_surface(1, "a"), _surface(2, "b")]
    surface_ids = [str(entry["surface_id"]) for entry in manifest]
    references = [str(entry["surface_reference"]) for entry in manifest]
    return {
        "matter": {
            "matter_id": "matter-001",
            "matter_purpose": "Reconstruct one declared relation only.",
            "matter_scope": "Selected manifest only.",
            "reading_reason": "Read the two standing surfaces together.",
            "outside_boundary": "No inference outside this manifest.",
        },
        "selected_surface_manifest": manifest,
        "declared_correspondence_question": {
            "question_id": "question-001",
            "matter_id": "matter-001",
            "selected_surface_ids": surface_ids,
            "relation_type": relation_type,
            "direction": None,
            "bounded_claim": "Does the exact basis support the declared relation?",
            "basis_references": references,
        },
        "correspondence_basis": {
            "readable": True,
            "available": True,
            "sufficient": True,
            "contradictory": False,
            "evidence_items": [
                {
                    "evidence_id": "evidence-001",
                    "surface_references": references,
                    "relation_type": evidence_relation_type or relation_type,
                    "relation_supported": supported,
                    "basis_fact": "Exact bounded evidence posture.",
                }
            ],
        },
        "reconstruction_posture": _reconstruction_posture(),
        "declared_non_claims": _declared_non_claims(),
    }


def _resolve(request: object) -> dict[str, object]:
    return resolver.resolve_matter_bound_selected_surface_correspondence_v0_min_v2(
        request  # type: ignore[arg-type]
    )


class MatterBoundSelectedSurfaceCorrespondenceV2Tests(unittest.TestCase):
    def assertBlocked(self, result: dict[str, object]) -> None:
        self.assertEqual(resolver.BLOCKED, result["outcome"])
        block = result["block"]
        self.assertIsInstance(block, dict)
        code = block["code"]
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertIs(result["result"]["bounded_stopping_recorded"], True)
        self.assertCanonicalNonClaims(result)

    def assertCanonicalNonClaims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertEqual(set(resolver.REQUIRED_FALSE_NON_CLAIMS), set(non_claims))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(non_claims[key], False)

    def test_public_contract_is_v2_only_and_has_no_persistence_api(self) -> None:
        self.assertEqual("0.1.0", resolver.RESULT_VERSION)
        self.assertEqual(
            "resolve_matter_bound_selected_surface_correspondence_v0_min_v2",
            resolver.RESOLVER_MODULE,
        )
        self.assertEqual(
            "MATTER_BOUND_SELECTED_SURFACE_CORRESPONDENCE",
            resolver.CORRESPONDENCE_TYPE,
        )
        self.assertEqual(
            "ONE_EXPLICIT_MATTER_ONE_EXPLICIT_SELECTED_SURFACE_MANIFEST_"
            "ONE_DECLARED_CORRESPONDENCE_QUESTION_ONLY",
            resolver.CORRESPONDENCE_SCOPE,
        )
        self.assertEqual(
            {
                "CORRESPONDENCE_RECOGNIZED",
                "NO_CORRESPONDENCE",
                "BLOCKED",
            },
            set(resolver.OUTCOMES),
        )
        self.assertFalse(hasattr(resolver, "write_result"))
        self.assertFalse(hasattr(resolver, "resolve_from_path"))
        self.assertFalse(any(name.startswith("write_") for name in resolver.__all__))

    def test_all_eleven_admitted_relation_types_are_recognized_from_exact_support(self) -> None:
        self.assertEqual(11, len(resolver.ADMITTED_RELATION_TYPES))
        for relation_type in resolver.ADMITTED_RELATION_TYPES:
            with self.subTest(relation_type=relation_type):
                result = _resolve(_request(relation_type))
                self.assertEqual(resolver.CORRESPONDENCE_RECOGNIZED, result["outcome"])
                self.assertEqual(relation_type, result["finding"]["declared_relation_type"])
                self.assertIs(result["finding"]["declared_relation_supported"], True)
                self.assertEqual(["evidence-001"], result["finding"]["supporting_evidence_ids"])
                self.assertIsNone(result["block"]["code"])
                self.assertCanonicalNonClaims(result)

    def test_supported_negative_relations_are_recognized_not_top_level_no_correspondence(self) -> None:
        expected = {
            "BASIS_MISMATCH",
            "SCOPE_MISMATCH",
            "NON_CLAIM_CONFLICT",
            "REFUSAL_VISIBLE",
            "NO_CORRESPONDENCE",
        }
        self.assertEqual(expected, set(resolver.NEGATIVE_RELATION_TYPES))
        for relation_type in sorted(expected):
            with self.subTest(relation_type=relation_type):
                result = _resolve(_request(relation_type, supported=True))
                self.assertEqual(resolver.CORRESPONDENCE_RECOGNIZED, result["outcome"])
                self.assertEqual("DECLARED_RELATION_SUPPORTED", result["finding"]["finding_code"])

    def test_all_three_top_level_outcomes(self) -> None:
        recognized = _resolve(_request("BASIS_MATCH", supported=True))
        no_correspondence = _resolve(_request("BASIS_MATCH", supported=False))
        blocked = _resolve(None)

        self.assertEqual(resolver.CORRESPONDENCE_RECOGNIZED, recognized["outcome"])
        self.assertEqual(resolver.NO_CORRESPONDENCE, no_correspondence["outcome"])
        self.assertEqual(resolver.BLOCKED, blocked["outcome"])
        self.assertIs(recognized["result"]["bounded_completion_recorded"], True)
        self.assertIs(no_correspondence["result"]["bounded_completion_recorded"], True)
        self.assertIs(blocked["result"]["bounded_completion_recorded"], False)

    def test_relation_admission_is_distinct_from_exact_evidence_support(self) -> None:
        request = _request(
            "BASIS_MATCH",
            supported=True,
            evidence_relation_type="BASIS_MISMATCH",
        )
        result = _resolve(request)

        self.assertEqual(resolver.NO_CORRESPONDENCE, result["outcome"])
        self.assertIs(result["finding"]["declared_relation_supported"], False)
        self.assertEqual([], result["finding"]["supporting_evidence_ids"])
        self.assertEqual(
            "BASIS_MISMATCH",
            result["correspondence_basis"]["evidence_items"][0]["relation_type"],
        )
        self.assertEqual(
            "DECLARED_RELATION_NOT_SUPPORTED", result["finding"]["finding_code"]
        )

    def test_manifest_order_is_preserved_without_order_derived_authority(self) -> None:
        first_request = _request("LINEAGE_REFERENCE")
        first_result = _resolve(first_request)
        self.assertEqual(
            ["surface-a", "surface-b"],
            [entry["surface_id"] for entry in first_result["selected_surface_manifest"]],
        )

        reversed_request = _request("LINEAGE_REFERENCE")
        manifest = reversed_request["selected_surface_manifest"]
        manifest.reverse()
        for position, entry in enumerate(manifest, start=1):
            entry["selected_position"] = position
        ids = [entry["surface_id"] for entry in manifest]
        references = [entry["surface_reference"] for entry in manifest]
        reversed_request["declared_correspondence_question"]["selected_surface_ids"] = ids
        reversed_request["declared_correspondence_question"]["basis_references"] = references
        reversed_request["correspondence_basis"]["evidence_items"][0]["surface_references"] = references

        reversed_result = _resolve(reversed_request)
        self.assertEqual(
            ["surface-b", "surface-a"],
            [entry["surface_id"] for entry in reversed_result["selected_surface_manifest"]],
        )
        ranks = {
            entry["surface_id"]: entry["surface_rank"]
            for entry in reversed_result["selected_surface_manifest"]
        }
        self.assertEqual({"surface-a": "rank-a", "surface-b": "rank-b"}, ranks)
        self.assertEqual(resolver.CORRESPONDENCE_RECOGNIZED, reversed_result["outcome"])

    def test_exact_selected_surface_posture_is_required(self) -> None:
        too_small = _request()
        too_small["selected_surface_manifest"] = too_small["selected_surface_manifest"][:1]
        self.assertBlocked(_resolve(too_small))

        for key in sorted(SURFACE_KEYS):
            with self.subTest(missing_surface_key=key):
                request = _request()
                del request["selected_surface_manifest"][0][key]
                self.assertBlocked(_resolve(request))

        malformed_values = {
            "surface_id": "",
            "surface_reference": None,
            "surface_outcome": [],
            "surface_rank": " ",
            "source_basis": None,
            "surface_scope": "",
            "lineage_references": [],
            "source_downstream_posture": None,
            "non_claims": [],
        }
        for key, value in malformed_values.items():
            with self.subTest(malformed_surface_key=key):
                request = _request()
                request["selected_surface_manifest"][0][key] = value
                self.assertBlocked(_resolve(request))

        flipped = _request()
        flipped["selected_surface_manifest"][0]["non_claims"][
            "surface_authority_created"
        ] = True
        self.assertBlocked(_resolve(flipped))

    def test_manifest_identity_reference_and_position_must_be_exact(self) -> None:
        duplicate_id = _request()
        duplicate_id["selected_surface_manifest"][1]["surface_id"] = "surface-a"
        self.assertBlocked(_resolve(duplicate_id))

        duplicate_reference = _request()
        duplicate_reference["selected_surface_manifest"][1][
            "surface_reference"
        ] = "held/surface-a.json"
        self.assertBlocked(_resolve(duplicate_reference))

        wrong_position = _request()
        wrong_position["selected_surface_manifest"][1]["selected_position"] = 3
        self.assertBlocked(_resolve(wrong_position))

        bool_position = _request()
        bool_position["selected_surface_manifest"][0]["selected_position"] = True
        self.assertBlocked(_resolve(bool_position))

    def test_exactly_one_matter_question_and_relation_are_required(self) -> None:
        cases: list[tuple[str, object]] = []

        multiple_matters = _request()
        multiple_matters["matter"] = [multiple_matters["matter"], copy.deepcopy(multiple_matters["matter"])]
        cases.append(("multiple_matters", multiple_matters))

        multiple_questions = _request()
        multiple_questions["declared_correspondence_question"] = [
            multiple_questions["declared_correspondence_question"],
            copy.deepcopy(multiple_questions["declared_correspondence_question"]),
        ]
        cases.append(("multiple_questions", multiple_questions))

        multiple_relations = _request()
        multiple_relations["declared_correspondence_question"]["relation_type"] = [
            "BASIS_MATCH",
            "BASIS_MISMATCH",
        ]
        cases.append(("multiple_relations", multiple_relations))

        missing_question = _request()
        missing_question["declared_correspondence_question"] = None
        cases.append(("missing_question", missing_question))

        for name, request in cases:
            with self.subTest(case=name):
                self.assertBlocked(_resolve(request))

    def test_question_must_bind_exact_matter_manifest_and_basis(self) -> None:
        matter_mismatch = _request()
        matter_mismatch["declared_correspondence_question"]["matter_id"] = "other"
        self.assertBlocked(_resolve(matter_mismatch))

        surface_mismatch = _request()
        surface_mismatch["declared_correspondence_question"]["selected_surface_ids"].reverse()
        self.assertBlocked(_resolve(surface_mismatch))

        basis_mismatch = _request()
        basis_mismatch["declared_correspondence_question"]["basis_references"].reverse()
        self.assertBlocked(_resolve(basis_mismatch))

        malformed_direction = _request()
        malformed_direction["declared_correspondence_question"]["direction"] = []
        self.assertBlocked(_resolve(malformed_direction))

    def test_unreadable_unavailable_contradictory_and_insufficient_basis_block(self) -> None:
        cases = {
            "readable": False,
            "available": False,
            "contradictory": True,
            "sufficient": False,
        }
        for key, value in cases.items():
            with self.subTest(basis_posture=key):
                request = _request()
                request["correspondence_basis"][key] = value
                self.assertBlocked(_resolve(request))

        malformed_bool = _request()
        malformed_bool["correspondence_basis"]["readable"] = 1
        self.assertBlocked(_resolve(malformed_bool))

        no_evidence = _request()
        no_evidence["correspondence_basis"]["evidence_items"] = []
        self.assertBlocked(_resolve(no_evidence))

    def test_evidence_must_be_exact_bounded_and_relation_admitted(self) -> None:
        reference_mismatch = _request()
        reference_mismatch["correspondence_basis"]["evidence_items"][0][
            "surface_references"
        ].reverse()
        self.assertBlocked(_resolve(reference_mismatch))

        unsupported_relation = _request()
        unsupported_relation["correspondence_basis"]["evidence_items"][0][
            "relation_type"
        ] = "SEMANTIC_SIMILARITY"
        self.assertBlocked(_resolve(unsupported_relation))

        duplicate_evidence = _request()
        duplicate_evidence["correspondence_basis"]["evidence_items"].append(
            copy.deepcopy(duplicate_evidence["correspondence_basis"]["evidence_items"][0])
        )
        self.assertBlocked(_resolve(duplicate_evidence))

        full_body = _request()
        full_body["correspondence_basis"]["evidence_items"][0][
            "complete_artifact_body"
        ] = {"raw": "RAW_BODY_MUST_NOT_RETURN"}
        result = _resolve(full_body)
        self.assertBlocked(result)
        self.assertNotIn("RAW_BODY_MUST_NOT_RETURN", json.dumps(result, sort_keys=True))

    def test_every_reconstruction_guardrail_blocks_when_flipped(self) -> None:
        for key in resolver.REQUIRED_FALSE_RECONSTRUCTION_POSTURES:
            with self.subTest(reconstruction_posture=key):
                request = _request()
                request["reconstruction_posture"][key] = True
                result = _resolve(request)
                self.assertBlocked(result)

        missing = _request()
        del missing["reconstruction_posture"][
            resolver.REQUIRED_FALSE_RECONSTRUCTION_POSTURES[0]
        ]
        self.assertBlocked(_resolve(missing))

    def test_negative_relation_collapse_attempt_blocks_explicitly(self) -> None:
        request = _request("NO_CORRESPONDENCE", supported=True)
        request["reconstruction_posture"][
            "supported_negative_relation_treated_as_no_correspondence"
        ] = True
        result = _resolve(request)

        self.assertBlocked(result)
        self.assertEqual("NEGATIVE_RELATION_OUTCOME_COLLAPSE", result["block"]["code"])

    def test_every_required_non_claim_blocks_when_missing_or_flipped(self) -> None:
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(flipped_non_claim=key):
                request = _request()
                request["declared_non_claims"][key] = True
                result = _resolve(request)
                self.assertBlocked(result)
                self.assertCanonicalNonClaims(result)
                self.assertIs(result["non_claims"][key], False)

            with self.subTest(missing_non_claim=key):
                request = _request()
                del request["declared_non_claims"][key]
                result = _resolve(request)
                self.assertBlocked(result)
                self.assertCanonicalNonClaims(result)

    def test_unsupported_vocabulary_and_unknown_fields_block(self) -> None:
        unsupported = _request()
        unsupported["declared_correspondence_question"][
            "relation_type"
        ] = "GENERAL_CORRESPONDENCE"
        self.assertBlocked(_resolve(unsupported))

        extra_top_level = _request()
        extra_top_level["latest_surface"] = "surface-b"
        self.assertBlocked(_resolve(extra_top_level))

        extra_matter = _request()
        extra_matter["matter"]["second_matter_id"] = "matter-002"
        self.assertBlocked(_resolve(extra_matter))

        extra_surface = _request()
        extra_surface["selected_surface_manifest"][0]["priority"] = 1
        self.assertBlocked(_resolve(extra_surface))

        extra_non_claim = _request()
        extra_non_claim["declared_non_claims"]["unbounded_permission_created"] = False
        self.assertBlocked(_resolve(extra_non_claim))

    def test_compact_result_shape_preserves_only_normalized_posture(self) -> None:
        result = _resolve(_request("NON_CLAIM_ALIGNMENT"))

        self.assertEqual(TOP_LEVEL_KEYS, set(result))
        self.assertEqual(
            "matter-001",
            result["matter"]["matter_id"],
        )
        self.assertEqual(SURFACE_KEYS, set(result["selected_surface_manifest"][0]))
        self.assertEqual(
            "NON_CLAIM_ALIGNMENT",
            result["declared_correspondence_question"]["relation_type"],
        )
        serialized = json.dumps(result, sort_keys=True)
        for forbidden in (
            "complete_artifact_body",
            "recursive_ancestry",
            "repository_inventory",
            "generated_at",
            "output_path",
        ):
            self.assertNotIn(forbidden, serialized)
        self.assertCanonicalNonClaims(result)

    def test_input_is_not_mutated_and_output_is_independent(self) -> None:
        request = _request("CLOSURE_ALIGNMENT")
        before = copy.deepcopy(request)
        result = _resolve(request)

        self.assertEqual(before, request)
        result["selected_surface_manifest"][0]["lineage_references"].append("changed")
        result["selected_surface_manifest"][0]["non_claims"][
            "surface_authority_created"
        ] = True
        result["correspondence_basis"]["evidence_items"][0][
            "surface_references"
        ].append("changed")
        self.assertEqual(before, request)

    def test_identical_input_produces_identical_output(self) -> None:
        request = _request("DOWNSTREAM_RECOGNITION")
        first = _resolve(copy.deepcopy(request))
        second = _resolve(copy.deepcopy(request))

        self.assertEqual(first, second)
        self.assertEqual(
            json.dumps(first, sort_keys=True), json.dumps(second, sort_keys=True)
        )

    def test_resolver_performs_no_filesystem_writes(self) -> None:
        request = _request("REFUSAL_VISIBLE")
        with mock.patch("builtins.open", side_effect=AssertionError("filesystem access")), mock.patch.object(
            Path, "write_text", side_effect=AssertionError("filesystem write")
        ), mock.patch.object(Path, "mkdir", side_effect=AssertionError("filesystem write")):
            result = _resolve(request)

        self.assertEqual(resolver.CORRESPONDENCE_RECOGNIZED, result["outcome"])
        self.assertCanonicalNonClaims(result)

    def test_result_booleans_and_block_codes_are_canonical_for_every_outcome(self) -> None:
        results = [
            _resolve(_request(supported=True)),
            _resolve(_request(supported=False)),
            _resolve({}),
        ]
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                for check in result["checks"]:
                    self.assertIs(type(check["passed"]), bool)
                    if check["block_code"] is not None:
                        self.assertIn(check["block_code"], resolver.BLOCK_CODES)
                self.assertIn(result["outcome"], resolver.OUTCOMES)
                self.assertCanonicalNonClaims(result)


if __name__ == "__main__":
    unittest.main()
