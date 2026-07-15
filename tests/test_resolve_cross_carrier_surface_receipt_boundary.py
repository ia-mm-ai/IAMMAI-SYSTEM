"""Tests for bounded cross-carrier surface receipt boundary resolution.

This suite audits one receipt checker. It verifies that one carried surface can
be received as carried evidence only, with carrier basis, surface basis,
integrity posture, and non-claims preserved. It also verifies blocked collapse
posture without opening multi-carrier law, distributed standing, synchronization,
workflow, signal use, body formation, or continuation.
"""

from __future__ import annotations

import copy
import hashlib
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

import resolve_cross_carrier_surface_receipt_boundary as resolver


TOP_LEVEL_SECTIONS = {
    "cross_carrier_surface_receipt_metadata",
    "source_carrier_basis",
    "receiving_carrier_basis",
    "carried_surface_basis",
    "carried_surface_integrity_check",
    "receipt_checks",
    "receipt_statement",
    "receipt_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "cross_carrier_surface_receipt_summary",
}

EXPECTED_CHECK_NAMES = {
    "explicit_inputs_are_parseable_mappings",
    "source_carrier_exists",
    "source_carrier_role_is_packet_limited",
    "receiving_carrier_exists",
    "receiving_carrier_role_is_receiving_carrier",
    "carried_surface_exists",
    "carried_surface_has_identity",
    "carried_surface_has_outcome",
    "supplied_carried_surface_matches_packet_basis",
    "carried_surface_integrity_basis_present_or_not_required",
    "carried_surface_hash_matches_where_checked",
    "receipt_purpose_declared",
    "receiving_carrier_is_not_source",
    "receiving_carrier_is_not_current",
    "receiving_carrier_is_not_authority",
    "receipt_creates_no_permission",
    "receiving_carrier_is_not_successor",
    "carriers_are_not_merged",
    "local_copy_is_not_currentness",
    "receipt_does_not_mutate_carried_surface",
    "source_body_is_not_replayed",
    "upstream_mechanisms_are_not_run",
    "continuation_is_not_authorized",
    "carried_surface_is_not_signal_by_default",
    "receipt_does_not_establish_presence",
    "receipt_does_not_establish_threshold",
    "receipt_does_not_create_truth",
    "receipt_does_not_authorize_action",
    "receipt_does_not_create_consequence",
    "multi_carrier_law_is_not_created",
    "distributed_standing_is_not_created",
    "mutation_replay_merge_remain_false",
    "byte_transfer_is_not_treated_as_lawful_receipt",
    "required_non_claims_remain_false",
}

NON_MEANING_TRUE_KEYS = {
    "does_not_mean_byte_transfer_alone",
    "does_not_replace_source",
    "does_not_create_receiving_carrier_sourcehood",
    "does_not_create_receiving_carrier_currentness",
    "does_not_create_receiving_carrier_authority",
    "does_not_create_receiving_carrier_permission",
    "does_not_create_successor_standing",
    "does_not_form_body",
    "does_not_merge_carriers",
    "does_not_create_local_copy_currentness",
    "does_not_authorize_execution",
    "does_not_authorize_continuation",
    "does_not_create_signal_by_default",
    "does_not_establish_presence",
    "does_not_establish_threshold",
    "does_not_create_truth",
    "does_not_authorize_action",
    "does_not_create_consequence",
    "does_not_transfer_full_repo",
    "does_not_synchronize_repo",
    "does_not_create_distributed_standing",
    "does_not_create_multi_carrier_law",
}

OPEN_SURFACES = {
    "portable receipt implementation refinement",
    "cross-carrier receipt test on physical second carrier",
    "multi-carrier relation law",
    "distributed standing",
    "persistence/registry law",
    "presence law",
    "threshold law",
    "truth law",
    "action/consequence law",
    "generalized vessel relation lifecycle",
    "body relevance medium",
    "signal series or accumulation logic",
    "future self-orientation successor only if separately justified",
}

SURFACE_ID = "current_body_standing_closure_test_surface_001"
SURFACE_OUTCOME = "CONFORMANCE_CLOSURE_RECORDED"
SOURCE_CARRIER_ID = "source-carrier-test"
RECEIVING_CARRIER_ID = "receiving-carrier-test"


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    assert isinstance(loaded, dict)
    return loaded


def _canonical_json_bytes(value: dict) -> bytes:
    return json.dumps(dict(value), sort_keys=True, separators=(",", ":")).encode("utf-8")


def _false_non_claims(**updates: bool) -> dict[str, bool]:
    claims = copy.deepcopy(resolver.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _surface_mapping(
    *,
    surface_id: str = SURFACE_ID,
    outcome: str = SURFACE_OUTCOME,
    surface_type: str = "current_body_standing_closure_post_conformance_result",
) -> dict[str, object]:
    return {
        "surface_id": surface_id,
        "surface_outcome": outcome,
        "surface_type": surface_type,
        "selected_upstream_basis": {
            "selected_self_orientation_v6_id": "current_self_orientation_v6_test_001",
            "selected_conformance_id": "current_body_conformance_test_001",
        },
        "source_downstream_posture": "carried_surface_remains_carried_downstream_evidence",
        "non_claims": _false_non_claims(),
    }


def _packet(
    *,
    source_carrier: dict[str, object] | None = None,
    receiving_carrier: dict[str, object] | None = None,
    carried_surface: dict[str, object] | None = None,
    integrity: dict[str, object] | None = None,
    receipt_purpose: object = "Record one carried closure surface as carried evidence.",
    non_claims: dict[str, bool] | None = None,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    packet: dict[str, object] = {
        "carried_packet_metadata": {
            "carried_packet_id": f"{SURFACE_ID}__carried_packet_test",
            "carried_packet_type": "cross_carrier_surface_receipt_carried_packet",
            "carried_packet_version": "0.1.0",
            "created_exported_at": "2026-04-28T00:00:00Z",
            "emitter_surface": "test",
        },
        "source_carrier": source_carrier
        if source_carrier is not None
        else {
            "carrier_id": SOURCE_CARRIER_ID,
            "carrier_label": "source carrier test",
            "carrier_role": "source_carrier_for_this_carried_packet_only",
            "local_path_context": "/local/source/context",
            "source_carrier_role_does_not_create_universal_source_authority": True,
        },
        "intended_receiving_carrier": receiving_carrier
        if receiving_carrier is not None
        else {
            "carrier_id": RECEIVING_CARRIER_ID,
            "carrier_label": "receiving carrier test",
            "carrier_role": "receiving_carrier",
            "receiving_carrier_does_not_become_source_current_or_authority": True,
        },
        "carried_surface": carried_surface
        if carried_surface is not None
        else {
            "surface_id": SURFACE_ID,
            "surface_path": f"carried/{SURFACE_ID}.json",
            "surface_filename": f"{SURFACE_ID}.json",
            "surface_outcome": SURFACE_OUTCOME,
            "surface_type": "current_body_standing_closure_post_conformance_result",
            "selected_upstream_basis": {
                "selected_self_orientation_v6_id": "current_self_orientation_v6_test_001",
                "selected_conformance_id": "current_body_conformance_test_001",
            },
            "source_downstream_posture": "carried_surface_remains_carried_downstream_evidence",
        },
        "carried_surface_integrity": integrity
        if integrity is not None
        else {
            "integrity_required": False,
            "integrity_not_required": True,
            "created_exported_at": "2026-04-28T00:00:00Z",
        },
        "receipt_purpose": receipt_purpose,
        "non_claims": copy.deepcopy(non_claims or _false_non_claims()),
    }
    if extra:
        packet.update(copy.deepcopy(extra))
    return packet


def _received() -> dict:
    return resolver.resolve_cross_carrier_surface_receipt_boundary(
        carried_packet=_packet()
    )


def _blocked_with_claim(claim: str, expected_code: str) -> dict:
    packet = _packet(non_claims=_false_non_claims(**{claim: True}))
    result = resolver.resolve_cross_carrier_surface_receipt_boundary(
        carried_packet=packet
    )
    assert result["outcome"] == "BLOCKED"
    assert result["block"]["code"] == expected_code
    return result


class CrossCarrierSurfaceReceiptBoundaryTests(unittest.TestCase):
    def assertTopLevelShape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result.keys()))

    def assertBlocked(self, result: dict, code: str) -> None:
        self.assertEqual("BLOCKED", result["outcome"])
        self.assertEqual(code, result["block"]["code"])

    def assertNonClaimsFalse(self, result: dict) -> None:
        for key in resolver.REQUIRED_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIn(key, result["non_claims"])
                self.assertIs(result["non_claims"][key], False)

    def test_successful_mapping_based_receipt_without_hash_check(self) -> None:
        result = _received()

        self.assertIsInstance(result, dict)
        self.assertTopLevelShape(result)
        self.assertEqual("CARRIED_SURFACE_RECEIVED", result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        statement = result["receipt_statement"]
        self.assertIs(statement["carried_surface_received"], True)
        self.assertIs(statement["received_as_carried_evidence"], True)
        self.assertIs(statement["source_carrier_preserved"], True)
        self.assertIs(statement["receiving_carrier_declared"], True)

    def test_metadata(self) -> None:
        metadata = _received()["cross_carrier_surface_receipt_metadata"]

        for key in (
            "cross_carrier_surface_receipt_result_id",
            "cross_carrier_surface_receipt_result_type",
            "cross_carrier_surface_receipt_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["cross_carrier_surface_receipt_result_version"])
        self.assertEqual(
            "resolve_cross_carrier_surface_receipt_boundary",
            metadata["resolver_module"],
        )

    def test_source_carrier_basis(self) -> None:
        basis = _received()["source_carrier_basis"]

        self.assertEqual(SOURCE_CARRIER_ID, basis["source_carrier_id"])
        self.assertEqual("source carrier test", basis["source_carrier_label"])
        self.assertEqual(
            "source_carrier_for_this_carried_packet_only",
            basis["source_carrier_role"],
        )
        self.assertEqual("/local/source/context", basis["local_path_context"])
        self.assertIs(basis["source_carrier_role_limited_to_this_packet"], True)
        self.assertIs(basis["universal_source_authority_created"], False)

    def test_receiving_carrier_basis(self) -> None:
        basis = _received()["receiving_carrier_basis"]

        self.assertEqual(RECEIVING_CARRIER_ID, basis["receiving_carrier_id"])
        self.assertEqual("receiving carrier test", basis["receiving_carrier_label"])
        self.assertEqual("receiving_carrier", basis["receiving_carrier_role"])
        self.assertIs(basis["receiving_carrier_declared"], True)
        self.assertIs(
            basis["receiving_carrier_does_not_become_source_current_or_authority"],
            True,
        )

    def test_carried_surface_basis(self) -> None:
        basis = _received()["carried_surface_basis"]

        self.assertEqual(SURFACE_ID, basis["carried_surface_id"])
        self.assertEqual(f"carried/{SURFACE_ID}.json", basis["carried_surface_path"])
        self.assertEqual(f"{SURFACE_ID}.json", basis["carried_surface_filename"])
        self.assertEqual(SURFACE_OUTCOME, basis["carried_surface_outcome"])
        self.assertEqual(
            "current_body_standing_closure_post_conformance_result",
            basis["carried_surface_type"],
        )
        self.assertIn("selected_self_orientation_v6_id", basis["selected_upstream_basis"])
        self.assertEqual(
            "carried_surface_remains_carried_downstream_evidence",
            basis["source_downstream_posture"],
        )
        self.assertIs(basis["separately_supplied_surface"], False)
        self.assertIsNone(basis["separately_supplied_surface_id"])

    def test_integrity_check_without_hash(self) -> None:
        integrity = _received()["carried_surface_integrity_check"]

        self.assertIs(integrity["integrity_basis_satisfied"], True)
        self.assertIs(integrity["integrity_not_required"], True)
        self.assertIs(integrity["integrity_evidence_preserved"], True)
        self.assertIs(integrity["integrity_checked"], False)
        self.assertIs(integrity["hash_check_passed"], True)
        self.assertIsNone(integrity["declared_hash"])

    def test_receipt_statement(self) -> None:
        statement = _received()["receipt_statement"]

        expected_true = {
            "carried_surface_received",
            "source_carrier_preserved",
            "receiving_carrier_declared",
            "carried_surface_identity_preserved",
            "carried_surface_outcome_preserved",
            "integrity_evidence_preserved",
            "received_as_carried_evidence",
        }
        for key in expected_true:
            with self.subTest(key=key):
                self.assertIs(statement[key], True)
        expected_false = {
            "receiving_carrier_became_source",
            "receiving_carrier_became_current",
            "receiving_carrier_became_authority",
            "receiving_carrier_became_successor",
            "carried_surface_became_source",
            "carried_surface_became_currentness",
            "carried_surface_became_permission",
            "receipt_created_signal_by_default",
            "receipt_established_presence",
            "receipt_established_threshold",
            "receipt_created_truth",
            "receipt_authorized_action",
            "receipt_created_consequence",
            "receipt_authorized_continuation",
            "multi_carrier_law_created",
            "distributed_standing_created",
        }
        for key in expected_false:
            with self.subTest(key=key):
                self.assertIs(statement[key], False)

    def test_receipt_non_meaning(self) -> None:
        non_meaning = _received()["receipt_non_meaning"]

        for key in NON_MEANING_TRUE_KEYS:
            with self.subTest(non_meaning=key):
                self.assertIn(key, non_meaning)
                self.assertIs(non_meaning[key], True)

    def test_what_remains_open(self) -> None:
        open_posture = _received()["what_remains_open"]

        self.assertTrue(OPEN_SURFACES.issubset(set(open_posture["open_surfaces"])))
        self.assertIs(open_posture["open_means_not_scheduled"], True)
        self.assertIs(open_posture["open_means_not_authorized"], True)
        self.assertIs(open_posture["open_means_not_executed"], True)

    def test_receipt_checks(self) -> None:
        checks = _received()["receipt_checks"]
        names = {check["check_name"] for check in checks}

        self.assertTrue(EXPECTED_CHECK_NAMES.issubset(names))
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIs(check["passed"], True)
            self.assertIsNone(check["block_code"])
        self.assertEqual(0, _received()["cross_carrier_surface_receipt_summary"]["failed_check_count"])

    def test_summary_helper(self) -> None:
        result = _received()
        summary = resolver.build_cross_carrier_surface_receipt_summary(result)

        self.assertEqual("CARRIED_SURFACE_RECEIVED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(SOURCE_CARRIER_ID, summary["source_carrier_id"])
        self.assertEqual("source carrier test", summary["source_carrier_label"])
        self.assertEqual(RECEIVING_CARRIER_ID, summary["receiving_carrier_id"])
        self.assertEqual("receiving carrier test", summary["receiving_carrier_label"])
        self.assertEqual(SURFACE_ID, summary["carried_surface_id"])
        self.assertEqual(SURFACE_OUTCOME, summary["carried_surface_outcome"])
        self.assertEqual(f"{SURFACE_ID}.json", summary["carried_surface_filename"])
        self.assertEqual(f"carried/{SURFACE_ID}.json", summary["carried_surface_path"])
        self.assertIs(summary["integrity_checked"], False)
        self.assertIs(summary["integrity_evidence_preserved"], True)
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertIs(summary["carried_surface_received"], True)
        self.assertIs(summary["received_as_carried_evidence"], True)
        self.assertIs(summary["source_carrier_preserved"], True)
        self.assertIs(summary["receiving_carrier_declared"], True)
        for key in (
            "receiving_carrier_became_source",
            "receiving_carrier_became_current",
            "receiving_carrier_became_authority",
            "receiving_carrier_became_successor",
            "carried_surface_became_source",
            "carried_surface_became_currentness",
            "carried_surface_became_permission",
            "carried_surface_became_signal",
            "presence_established",
            "threshold_met",
            "truth_created",
            "action_authorized",
            "consequence_created",
            "continuation_authorized",
            "multi_carrier_law_created",
            "distributed_standing_created",
        ):
            with self.subTest(summary_key=key):
                self.assertIs(summary[key], False)
        self.assertIsInstance(summary["key_non_claims"], dict)

    def test_result_level_non_claims_for_received_and_blocked_results(self) -> None:
        received = _received()
        blocked = resolver.resolve_cross_carrier_surface_receipt_boundary(
            carried_packet=_packet(non_claims=_false_non_claims(authority_created=True))
        )

        self.assertNonClaimsFalse(received)
        self.assertNonClaimsFalse(blocked)

    def test_successful_mapping_based_receipt_with_supplied_surface_hash_check(self) -> None:
        surface = _surface_mapping()
        surface_bytes = _canonical_json_bytes(surface)
        packet = _packet(
            carried_surface={
                "surface_id": SURFACE_ID,
                "surface_path": "carried/supplied-surface.json",
                "surface_filename": "supplied-surface.json",
                "surface_outcome": SURFACE_OUTCOME,
                "surface_type": "current_body_standing_closure_post_conformance_result",
                "selected_upstream_basis": surface["selected_upstream_basis"],
                "source_downstream_posture": "carried_surface_remains_carried_downstream_evidence",
            },
            integrity={
                "hash": hashlib.sha256(surface_bytes).hexdigest(),
                "hash_algorithm": "sha256",
                "byte_length": len(surface_bytes),
                "integrity_required": True,
            },
        )

        result = resolver.resolve_cross_carrier_surface_receipt_boundary(
            carried_packet=packet,
            carried_surface=surface,
        )

        self.assertEqual("CARRIED_SURFACE_RECEIVED", result["outcome"])
        integrity = result["carried_surface_integrity_check"]
        self.assertIs(integrity["integrity_checked"], True)
        self.assertIs(integrity["hash_matches"], True)
        self.assertEqual(integrity["declared_hash"], integrity["computed_hash"])
        self.assertIs(integrity["byte_length_matches"], True)
        basis = result["carried_surface_basis"]
        self.assertIs(basis["separately_supplied_surface"], True)
        self.assertEqual(SURFACE_ID, basis["separately_supplied_surface_id"])

    def test_successful_path_based_receipt_with_hash_check(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            surface_path = root / "surface.json"
            surface = _surface_mapping()
            _write_json(surface_path, surface)
            raw = surface_path.read_bytes()
            packet = _packet(
                carried_surface={
                    "surface_id": SURFACE_ID,
                    "surface_path": str(surface_path),
                    "surface_filename": surface_path.name,
                    "surface_outcome": SURFACE_OUTCOME,
                    "surface_type": "current_body_standing_closure_post_conformance_result",
                    "selected_upstream_basis": surface["selected_upstream_basis"],
                    "source_downstream_posture": "carried_surface_remains_carried_downstream_evidence",
                },
                integrity={
                    "hash": hashlib.sha256(raw).hexdigest(),
                    "hash_algorithm": "sha256",
                    "byte_length": len(raw),
                    "integrity_required": True,
                },
            )
            packet_path = root / "packet.json"
            _write_json(packet_path, packet)

            result = resolver.resolve_cross_carrier_surface_receipt_boundary_from_paths(
                packet_path,
                surface_path,
            )

        self.assertEqual("CARRIED_SURFACE_RECEIVED", result["outcome"])
        integrity = result["carried_surface_integrity_check"]
        self.assertIs(integrity["integrity_checked"], True)
        self.assertIs(integrity["hash_matches"], True)
        self.assertEqual(str(surface_path), result["carried_surface_basis"]["carried_surface_path"])
        self.assertEqual(
            str(surface_path),
            result["carried_surface_basis"]["separately_supplied_surface_path"],
        )

    def test_packet_builder_helper(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            surface_path = root / "surface.json"
            _write_json(surface_path, _surface_mapping())

            packet = resolver.build_carried_packet_from_surface_path(
                surface_path,
                SOURCE_CARRIER_ID,
                RECEIVING_CARRIER_ID,
                "Carry one closed surface as evidence.",
            )
            packet_path = root / "packet.json"
            _write_json(packet_path, packet)
            result = resolver.resolve_cross_carrier_surface_receipt_boundary_from_paths(
                packet_path,
                surface_path,
            )

        for key in (
            "carried_packet_metadata",
            "source_carrier",
            "intended_receiving_carrier",
            "carried_surface",
            "carried_surface_integrity",
            "receipt_purpose",
            "non_claims",
        ):
            self.assertIn(key, packet)
        self.assertEqual("sha256", packet["carried_surface_integrity"]["hash_algorithm"])
        self.assertTrue(packet["carried_surface_integrity"]["hash"])
        self.assertGreater(packet["carried_surface_integrity"]["byte_length"], 0)
        self.assertEqual(resolver.REQUIRED_NON_CLAIMS, packet["non_claims"])
        self.assertEqual("CARRIED_SURFACE_RECEIVED", result["outcome"])

    def test_write_behavior(self) -> None:
        result = _received()
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "receipt.json"
            written = resolver.write_cross_carrier_surface_receipt_result(
                result,
                output_path,
            )
            loaded = _read_json(written)

        self.assertEqual(output_path, written)
        self.assertTopLevelShape(loaded)
        self.assertEqual("CARRIED_SURFACE_RECEIVED", loaded["outcome"])

    def test_default_output_path_behavior(self) -> None:
        result = _received()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with mock.patch.object(
                resolver,
                "CROSS_CARRIER_SURFACE_RECEIPT_BOUNDARY_ROOT",
                root,
            ):
                first = resolver.write_cross_carrier_surface_receipt_result(result)
                second = resolver.write_cross_carrier_surface_receipt_result(result)

        self.assertEqual(root, first.parent)
        self.assertEqual(root, second.parent)
        self.assertNotEqual(first, second)
        self.assertTrue(first.name.endswith("__cross_carrier_surface_receipt_result.json"))
        self.assertIn("_001", second.name)

    def test_non_mutation_posture(self) -> None:
        surface = _surface_mapping()
        packet = _packet()
        original_surface = copy.deepcopy(surface)
        original_packet = copy.deepcopy(packet)

        first = resolver.resolve_cross_carrier_surface_receipt_boundary(packet, surface)
        second = resolver.resolve_cross_carrier_surface_receipt_boundary(packet, surface)

        self.assertEqual(original_packet, packet)
        self.assertEqual(original_surface, surface)
        self.assertEqual(first["outcome"], second["outcome"])
        with tempfile.TemporaryDirectory() as tmp:
            written = resolver.write_cross_carrier_surface_receipt_result(
                first,
                Path(tmp) / "receipt.json",
            )
            self.assertTrue(written.exists())
            self.assertEqual(1, len(list(Path(tmp).glob("*.json"))))

    def test_blocking_packet_missing_or_malformed(self) -> None:
        missing = resolver.resolve_cross_carrier_surface_receipt_boundary()
        malformed = resolver.resolve_cross_carrier_surface_receipt_boundary(
            carried_packet=["not", "a", "mapping"]  # type: ignore[arg-type]
        )

        self.assertEqual("BLOCKED", missing["outcome"])
        self.assertIn(
            missing["block"]["code"],
            {"SOURCE_CARRIER_MISSING", "CARRIED_PACKET_MALFORMED"},
        )
        self.assertBlocked(malformed, "CARRIED_PACKET_MALFORMED")

    def test_blocking_path_unreadable_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            valid_packet_path = root / "valid-packet.json"
            _write_json(valid_packet_path, _packet())

            malformed_packet = root / "malformed-packet.json"
            malformed_packet.write_text("{not-json", encoding="utf-8")
            array_packet = root / "array-packet.json"
            _write_json(array_packet, [])
            malformed_surface = root / "malformed-surface.json"
            malformed_surface.write_text("{not-json", encoding="utf-8")
            array_surface = root / "array-surface.json"
            _write_json(array_surface, [])

            cases = [
                (
                    resolver.resolve_cross_carrier_surface_receipt_boundary_from_paths(
                        root / "missing-packet.json"
                    ),
                    "CARRIED_PACKET_UNREADABLE",
                ),
                (
                    resolver.resolve_cross_carrier_surface_receipt_boundary_from_paths(
                        malformed_packet
                    ),
                    "CARRIED_PACKET_MALFORMED",
                ),
                (
                    resolver.resolve_cross_carrier_surface_receipt_boundary_from_paths(
                        array_packet
                    ),
                    "CARRIED_PACKET_MALFORMED",
                ),
                (
                    resolver.resolve_cross_carrier_surface_receipt_boundary_from_paths(
                        valid_packet_path,
                        root / "missing-surface.json",
                    ),
                    "CARRIED_SURFACE_UNREADABLE",
                ),
                (
                    resolver.resolve_cross_carrier_surface_receipt_boundary_from_paths(
                        valid_packet_path,
                        malformed_surface,
                    ),
                    "CARRIED_SURFACE_MALFORMED",
                ),
                (
                    resolver.resolve_cross_carrier_surface_receipt_boundary_from_paths(
                        valid_packet_path,
                        array_surface,
                    ),
                    "CARRIED_SURFACE_MALFORMED",
                ),
            ]

        for result, code in cases:
            with self.subTest(code=code):
                self.assertBlocked(result, code)

    def test_blocking_source_carrier_missing(self) -> None:
        packet = _packet(source_carrier={"carrier_role": "source_carrier_for_this_carried_packet_only"})
        self.assertBlocked(
            resolver.resolve_cross_carrier_surface_receipt_boundary(packet),
            "SOURCE_CARRIER_MISSING",
        )

    def test_blocking_source_carrier_role_not_packet_limited(self) -> None:
        packet = _packet(
            source_carrier={
                "carrier_id": SOURCE_CARRIER_ID,
                "carrier_label": "source carrier test",
                "carrier_role": "source_carrier",
            }
        )
        self.assertBlocked(
            resolver.resolve_cross_carrier_surface_receipt_boundary(packet),
            "SOURCE_CARRIER_MISSING",
        )

    def test_blocking_receiving_carrier_missing(self) -> None:
        packet = _packet(receiving_carrier={"carrier_role": "receiving_carrier"})
        self.assertBlocked(
            resolver.resolve_cross_carrier_surface_receipt_boundary(packet),
            "RECEIVING_CARRIER_MISSING",
        )

    def test_blocking_receiving_carrier_role_not_bounded(self) -> None:
        packet = _packet(
            receiving_carrier={
                "carrier_id": RECEIVING_CARRIER_ID,
                "carrier_label": "receiving carrier test",
                "carrier_role": "source_carrier",
            }
        )
        result = resolver.resolve_cross_carrier_surface_receipt_boundary(packet)
        self.assertEqual("BLOCKED", result["outcome"])
        self.assertIn(
            result["block"]["code"],
            {"RECEIVING_CARRIER_MISSING", "RECEIPT_TREATS_RECEIVER_AS_SOURCE"},
        )

    def test_blocking_carried_surface_missing_or_malformed(self) -> None:
        missing_packet = _packet()
        missing_packet.pop("carried_surface")
        malformed_packet = _packet(carried_surface=[])  # type: ignore[arg-type]

        self.assertBlocked(
            resolver.resolve_cross_carrier_surface_receipt_boundary(missing_packet),
            "CARRIED_SURFACE_MISSING",
        )
        result = resolver.resolve_cross_carrier_surface_receipt_boundary(
            malformed_packet
        )
        self.assertEqual("BLOCKED", result["outcome"])
        self.assertIn(result["block"]["code"], {"CARRIED_SURFACE_MISSING", "CARRIED_SURFACE_MALFORMED"})

    def test_blocking_carried_surface_identity_missing(self) -> None:
        surface = copy.deepcopy(_packet()["carried_surface"])
        assert isinstance(surface, dict)
        surface.pop("surface_id")
        packet = _packet(carried_surface=surface)

        self.assertBlocked(
            resolver.resolve_cross_carrier_surface_receipt_boundary(packet),
            "CARRIED_SURFACE_IDENTITY_MISSING",
        )

    def test_blocking_carried_surface_outcome_missing(self) -> None:
        surface = copy.deepcopy(_packet()["carried_surface"])
        assert isinstance(surface, dict)
        surface.pop("surface_outcome")
        packet = _packet(carried_surface=surface)

        self.assertBlocked(
            resolver.resolve_cross_carrier_surface_receipt_boundary(packet),
            "CARRIED_SURFACE_OUTCOME_MISSING",
        )

    def test_blocking_supplied_surface_contradicts_packet_basis(self) -> None:
        supplied_surface = _surface_mapping(surface_id="different-surface")

        result = resolver.resolve_cross_carrier_surface_receipt_boundary(
            carried_packet=_packet(),
            carried_surface=supplied_surface,
        )

        self.assertBlocked(result, "CARRIED_SURFACE_MALFORMED")

    def test_blocking_integrity_missing_when_required(self) -> None:
        packet = _packet(integrity={"integrity_required": True})

        self.assertBlocked(
            resolver.resolve_cross_carrier_surface_receipt_boundary(packet),
            "CARRIED_SURFACE_INTEGRITY_MISSING",
        )

    def test_blocking_hash_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            surface_path = root / "surface.json"
            _write_json(surface_path, _surface_mapping())
            raw = surface_path.read_bytes()
            packet = _packet(
                carried_surface={
                    "surface_id": SURFACE_ID,
                    "surface_path": str(surface_path),
                    "surface_filename": surface_path.name,
                    "surface_outcome": SURFACE_OUTCOME,
                    "surface_type": "current_body_standing_closure_post_conformance_result",
                    "source_downstream_posture": "carried_surface_remains_carried_downstream_evidence",
                },
                integrity={
                    "hash": "0" * 64,
                    "hash_algorithm": "sha256",
                    "byte_length": len(raw),
                    "integrity_required": True,
                },
            )
            packet_path = root / "packet.json"
            _write_json(packet_path, packet)
            result = resolver.resolve_cross_carrier_surface_receipt_boundary_from_paths(
                packet_path,
                surface_path,
            )

        self.assertBlocked(result, "CARRIED_SURFACE_HASH_MISMATCH")

    def test_blocking_unsupported_hash_algorithm(self) -> None:
        surface = _surface_mapping()
        surface_bytes = _canonical_json_bytes(surface)
        packet = _packet(
            integrity={
                "hash": hashlib.sha256(surface_bytes).hexdigest(),
                "hash_algorithm": "sha512",
                "byte_length": len(surface_bytes),
                "integrity_required": True,
            }
        )

        result = resolver.resolve_cross_carrier_surface_receipt_boundary(
            packet,
            surface,
        )

        self.assertBlocked(result, "CARRIED_SURFACE_HASH_MISMATCH")

    def test_blocking_receipt_purpose_undeclared(self) -> None:
        for purpose in (None, ""):
            with self.subTest(purpose=purpose):
                self.assertBlocked(
                    resolver.resolve_cross_carrier_surface_receipt_boundary(
                        _packet(receipt_purpose=purpose)
                    ),
                    "RECEIPT_PURPOSE_UNDECLARED",
                )

    def test_blocking_receiving_carrier_source_collapse(self) -> None:
        for claim in (
            "receiving_carrier_became_source",
            "source_replaced",
            "carried_surface_became_source",
        ):
            with self.subTest(claim=claim):
                _blocked_with_claim(claim, "RECEIPT_TREATS_RECEIVER_AS_SOURCE")

    def test_blocking_currentness_authority_permission(self) -> None:
        cases = {
            "currentness_created": "RECEIPT_CREATES_CURRENTNESS",
            "receiving_carrier_became_current": "RECEIPT_CREATES_CURRENTNESS",
            "carried_surface_became_currentness": "RECEIPT_CREATES_CURRENTNESS",
            "authority_created": "RECEIPT_CREATES_AUTHORITY",
            "receiving_carrier_became_authority": "RECEIPT_CREATES_AUTHORITY",
            "permission_created": "RECEIPT_CREATES_PERMISSION",
            "carried_surface_became_permission": "RECEIPT_CREATES_PERMISSION",
        }
        for claim, code in cases.items():
            with self.subTest(claim=claim):
                _blocked_with_claim(claim, code)

    def test_blocking_successor_standing_carrier_merge_local_copy_currentness(self) -> None:
        _blocked_with_claim(
            "receiving_carrier_became_successor",
            "RECEIPT_CREATES_SUCCESSOR_STANDING",
        )
        _blocked_with_claim("carrier_merge_performed", "RECEIPT_MERGES_CARRIERS")
        _blocked_with_claim("local_copy_currentness", "RECEIPT_TREATS_LOCAL_COPY_AS_CURRENT")

        same_carrier = _packet(
            receiving_carrier={
                "carrier_id": SOURCE_CARRIER_ID,
                "carrier_label": "receiving carrier test",
                "carrier_role": "receiving_carrier",
                "receiving_carrier_does_not_become_source_current_or_authority": True,
            }
        )
        self.assertBlocked(
            resolver.resolve_cross_carrier_surface_receipt_boundary(same_carrier),
            "RECEIPT_MERGES_CARRIERS",
        )

    def test_blocking_mutation_source_replay_upstream_mechanisms(self) -> None:
        cases = {
            "mutation_performed": "RECEIPT_MUTATES_CARRIED_SURFACE",
            "source_body_replayed": "RECEIPT_REPLAYS_SOURCE_BODY",
            "upstream_mechanisms_run": "RECEIPT_RUNS_UPSTREAM_MECHANISMS",
        }
        for claim, code in cases.items():
            with self.subTest(claim=claim):
                _blocked_with_claim(claim, code)

    def test_blocking_continuation_signal_presence_threshold_truth_action_consequence(self) -> None:
        cases = {
            "continuation_authorized": "RECEIPT_AUTHORIZES_CONTINUATION",
            "carried_surface_became_signal_by_default": "RECEIPT_CREATES_SIGNAL_BY_DEFAULT",
            "presence_established": "RECEIPT_ESTABLISHES_PRESENCE",
            "threshold_met": "RECEIPT_ESTABLISHES_THRESHOLD",
            "truth_created": "RECEIPT_CREATES_TRUTH",
            "action_authorized": "RECEIPT_AUTHORIZES_ACTION",
            "consequence_created": "RECEIPT_CREATES_CONSEQUENCE",
        }
        for claim, code in cases.items():
            with self.subTest(claim=claim):
                _blocked_with_claim(claim, code)

    def test_blocking_multi_carrier_law_or_distributed_standing_created(self) -> None:
        for claim in ("multi_carrier_law_created", "distributed_standing_created"):
            with self.subTest(claim=claim):
                result = resolver.resolve_cross_carrier_surface_receipt_boundary(
                    _packet(non_claims=_false_non_claims(**{claim: True}))
                )
                self.assertEqual("BLOCKED", result["outcome"])
                self.assertEqual("NON_CLAIM_MISSING_OR_FLIPPED", result["block"]["code"])

    def test_blocking_latest_file_currentness_or_recency_fraud(self) -> None:
        for claim in ("latest_file_currentness", "recency_fraud"):
            with self.subTest(claim=claim):
                _blocked_with_claim(claim, "RECEIPT_TREATS_LOCAL_COPY_AS_CURRENT")

    def test_blocking_mutation_replay_merge(self) -> None:
        cases = {
            "mutation_performed": "RECEIPT_MUTATES_CARRIED_SURFACE",
            "replay_performed": "RECEIPT_REPLAYS_SOURCE_BODY",
            "merge_performed": "RECEIPT_MUTATES_CARRIED_SURFACE",
        }
        for claim, code in cases.items():
            with self.subTest(claim=claim):
                _blocked_with_claim(claim, code)

    def test_blocking_byte_transfer_mistaken_for_receipt(self) -> None:
        packet = _packet(extra={"byte_transfer_mistaken_for_receipt": True})

        self.assertBlocked(
            resolver.resolve_cross_carrier_surface_receipt_boundary(packet),
            "BYTE_TRANSFER_MISTAKEN_FOR_RECEIPT",
        )

    def test_blocking_required_non_claim_missing_or_flipped(self) -> None:
        missing_claims = _false_non_claims()
        missing_claims.pop("authority_created")
        missing = resolver.resolve_cross_carrier_surface_receipt_boundary(
            _packet(non_claims=missing_claims)
        )
        flipped = resolver.resolve_cross_carrier_surface_receipt_boundary(
            _packet(non_claims=_false_non_claims(authority_created=True))
        )

        self.assertBlocked(missing, "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertEqual("BLOCKED", flipped["outcome"])
        self.assertIn(
            flipped["block"]["code"],
            {"RECEIPT_CREATES_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        failed_checks = [
            check for check in flipped["receipt_checks"] if check["passed"] is False
        ]
        self.assertTrue(failed_checks)
        self.assertNonClaimsFalse(missing)
        self.assertNonClaimsFalse(flipped)


if __name__ == "__main__":
    unittest.main()
