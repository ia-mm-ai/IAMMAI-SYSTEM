"""Tests for the contact protocol v0 six-phase checker."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

import contact_protocol_v0 as proto

REPO_ROOT = Path(__file__).resolve().parents[1]
LIVE_LOCALITY = REPO_ROOT / "locality"

NOW = datetime(2026, 9, 6, 12, 0, 0, tzinfo=timezone.utc)


class ContactProtocolTestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="locality_test_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        for name in (
            proto.PRESENCE_DIR_NAME,
            proto.TERMS_DIR_NAME,
            proto.VESTIBULE_DIR_NAME,
            proto.CONTACT_DIR_NAME,
            proto.REVIEW_DIR_NAME,
            proto.RELATIONS_DIR_NAME,
            proto.REVOCATIONS_DIR_NAME,
        ):
            (self.root / name).mkdir()
        (self.root / proto.PRESENCE_DIR_NAME / "identity").mkdir()
        (self.root / proto.PRESENCE_DIR_NAME / "identity" / "PERSON.md").write_text(
            "person\n", encoding="utf-8"
        )
        terms_path = self.root / proto.TERMS_DIR_NAME / proto.TERMS_FILE_NAME
        terms_path.write_text("terms body\n", encoding="utf-8")
        self.terms_hash = proto.sha256_of_file(terms_path)
        (self.root / proto.TERMS_DIR_NAME / proto.TERMS_HASH_FILE_NAME).write_text(
            self.terms_hash + "\n", encoding="utf-8"
        )
        self.dossier_hash = proto.seal_dossier(self.root)
        assert self.dossier_hash

    def write_contact(
        self,
        name: str = "visitor_001.json",
        identity: str = "visitor-a",
        terms_hash: str | None = None,
        dossier_hash: str | None = None,
        contacted_at: str = "2026-09-01T00:00:00Z",
        **overrides: object,
    ) -> Path:
        body = {
            "identity": identity,
            "accepted_terms_sha256": (
                self.terms_hash if terms_hash is None else terms_hash
            ),
            "witnessed_dossier_sha256": (
                self.dossier_hash if dossier_hash is None else dossier_hash
            ),
            "requested_scope": "read",
            "contacted_at": contacted_at,
        }
        body.update(overrides)
        path = self.root / proto.CONTACT_DIR_NAME / name
        path.write_text(json.dumps(body, indent=1), encoding="utf-8")
        return path

    def write_acceptance(
        self,
        contact_path: Path,
        relation: str = "relation_001",
        accepted_at: str = "2026-09-05T00:00:00Z",
        expires_at: str = "2026-09-08T00:00:00Z",
        **overrides: object,
    ) -> Path:
        body = {
            "contact_sha256": proto.sha256_of_file(contact_path),
            "granted_scope": "read",
            "accepted_at": accepted_at,
            "expires_at": expires_at,
        }
        body.update(overrides)
        relation_dir = self.root / proto.RELATIONS_DIR_NAME / relation
        relation_dir.mkdir(exist_ok=True)
        path = relation_dir / proto.ACCEPTANCE_FILE_NAME
        path.write_text(json.dumps(body, indent=1), encoding="utf-8")
        return path

    def write_revocation(self, contact_path: Path, name: str = "rev_001.json") -> Path:
        body = {
            "contact_sha256": proto.sha256_of_file(contact_path),
            "revoked_at": "2026-09-06T00:00:00Z",
        }
        path = self.root / proto.REVOCATIONS_DIR_NAME / name
        path.write_text(json.dumps(body, indent=1), encoding="utf-8")
        return path


class TestDossierAnchor(ContactProtocolTestBase):
    def test_seal_and_verify_roundtrip(self) -> None:
        self.assertEqual(proto.read_recorded_dossier_hash(self.root), self.dossier_hash)

    def test_dossier_edit_breaks_recorded_hash(self) -> None:
        (self.root / proto.PRESENCE_DIR_NAME / "identity" / "PERSON.md").write_text(
            "edited person\n", encoding="utf-8"
        )
        self.assertIsNone(proto.read_recorded_dossier_hash(self.root))

    def test_reseal_restores_anchor_with_new_identity(self) -> None:
        (self.root / proto.PRESENCE_DIR_NAME / "new_claim.md").write_text(
            "claim\n", encoding="utf-8"
        )
        new_hash = proto.seal_dossier(self.root)
        self.assertIsNotNone(new_hash)
        self.assertNotEqual(new_hash, self.dossier_hash)
        self.assertEqual(proto.read_recorded_dossier_hash(self.root), new_hash)

    def test_empty_dossier_cannot_seal(self) -> None:
        empty = Path(tempfile.mkdtemp(prefix="locality_empty_"))
        self.addCleanup(shutil.rmtree, empty, True)
        (empty / proto.PRESENCE_DIR_NAME).mkdir()
        self.assertIsNone(proto.seal_dossier(empty))


class TestVestibule(ContactProtocolTestBase):
    def test_vestibule_renders_both_anchors_and_grants_nothing(self) -> None:
        packet = proto.build_vestibule(self.root)
        self.assertIsNotNone(packet)
        self.assertEqual(packet["dossier_sha256"], self.dossier_hash)
        self.assertEqual(packet["terms_sha256"], self.terms_hash)
        self.assertEqual(packet["grants"], "NOTHING")
        self.assertEqual(packet["retains"], "NOTHING")

    def test_vestibule_is_never_persisted(self) -> None:
        proto.build_vestibule(self.root)
        contents = list((self.root / proto.VESTIBULE_DIR_NAME).iterdir())
        self.assertEqual(contents, [])

    def test_broken_anchor_shows_nobody_anything(self) -> None:
        (self.root / proto.TERMS_DIR_NAME / proto.TERMS_HASH_FILE_NAME).unlink()
        self.assertIsNone(proto.build_vestibule(self.root))


class TestFullPassage(ContactProtocolTestBase):
    def test_lawful_passage_reaches_relation(self) -> None:
        contact = self.write_contact()
        self.write_acceptance(contact)
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertTrue(decision.admitted)
        self.assertEqual(decision.phase, proto.PHASE_4_RELATION)
        self.assertEqual(decision.reasons, ())

    def test_check_is_reproducible(self) -> None:
        contact = self.write_contact()
        self.write_acceptance(contact)
        self.assertEqual(
            proto.check_relation(self.root, contact, NOW),
            proto.check_relation(self.root, contact, NOW),
        )


class TestPhaseTyping(ContactProtocolTestBase):
    def test_valid_contact_without_acceptance_is_phase_2_waiting(self) -> None:
        contact = self.write_contact()
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertFalse(decision.admitted)
        self.assertEqual(decision.phase, proto.PHASE_2_CONTACT)
        self.assertEqual(decision.reasons, ("NO_ACCEPTANCE",))

    def test_review_directory_types_phase_3(self) -> None:
        contact = self.write_contact()
        contact_hash = proto.sha256_of_file(contact)
        (self.root / proto.REVIEW_DIR_NAME / contact_hash).mkdir()
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertFalse(decision.admitted)
        self.assertEqual(decision.phase, proto.PHASE_3_REVIEW)

    def test_review_never_admits_by_itself(self) -> None:
        contact = self.write_contact()
        contact_hash = proto.sha256_of_file(contact)
        (self.root / proto.REVIEW_DIR_NAME / contact_hash).mkdir()
        far_future = datetime(2126, 1, 1, tzinfo=timezone.utc)
        decision = proto.check_relation(self.root, contact, far_future)
        self.assertFalse(decision.admitted)

    def test_broken_anchor_is_phase_0(self) -> None:
        contact = self.write_contact()
        self.write_acceptance(contact)
        (self.root / proto.PRESENCE_DIR_NAME / proto.DOSSIER_HASH_FILE_NAME).unlink()
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertEqual(decision.phase, proto.PHASE_0_PRESENCE)
        self.assertEqual(decision.reasons, ("ANCHOR_MISSING_OR_BROKEN",))


class TestContactEvent(ContactProtocolTestBase):
    def test_malformed_contact_is_void(self) -> None:
        path = self.root / proto.CONTACT_DIR_NAME / "bad.json"
        path.write_text("{not json", encoding="utf-8")
        decision = proto.check_relation(self.root, path, NOW)
        self.assertEqual(decision.reasons, ("CONTACT_VOID",))
        self.assertEqual(decision.phase, proto.PHASE_1_VESTIBULE)

    def test_extra_field_is_void(self) -> None:
        contact = self.write_contact(extra="field")
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertEqual(decision.reasons, ("CONTACT_VOID",))

    def test_wrong_terms_hash_means_terms_not_accepted(self) -> None:
        contact = self.write_contact(terms_hash="0" * 64)
        self.write_acceptance(contact)
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertIn("TERMS_NOT_ACCEPTED", decision.reasons)

    def test_stale_dossier_hash_means_reality_not_held(self) -> None:
        contact = self.write_contact()
        self.write_acceptance(contact)
        (self.root / proto.PRESENCE_DIR_NAME / "new_claim.md").write_text(
            "claim\n", encoding="utf-8"
        )
        proto.seal_dossier(self.root)
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("REALITY_NOT_HELD", decision.reasons)

    def test_newer_contact_invalidates_older(self) -> None:
        old = self.write_contact(name="a.json", contacted_at="2026-09-01T00:00:00Z")
        self.write_contact(name="b.json", contacted_at="2026-09-02T00:00:00Z")
        self.write_acceptance(old)
        decision = proto.check_relation(self.root, old, NOW)
        self.assertIn("CONTACT_NOT_STANDING", decision.reasons)

    def test_ambiguous_timestamps_leave_no_standing_contact(self) -> None:
        self.write_contact(name="a.json", contacted_at="2026-09-01T00:00:00Z")
        self.write_contact(name="b.json", contacted_at="2026-09-01T00:00:00Z")
        self.assertIsNone(proto.standing_contact_path(self.root, "visitor-a"))

    def test_void_attempt_remains_as_trail(self) -> None:
        path = self.root / proto.CONTACT_DIR_NAME / "bad.json"
        path.write_text("{not json", encoding="utf-8")
        proto.check_relation(self.root, path, NOW)
        self.assertTrue(path.is_file())


class TestAcceptance(ContactProtocolTestBase):
    def test_acceptance_binds_to_exact_contact_bytes(self) -> None:
        contact = self.write_contact()
        self.write_acceptance(contact)
        contact.write_text(contact.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("NO_ACCEPTANCE", decision.reasons)

    def test_acceptance_for_unmade_contact_admits_nothing(self) -> None:
        contact = self.write_contact()
        self.write_acceptance(contact, contact_sha256="f" * 64)
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertIn("NO_ACCEPTANCE", decision.reasons)

    def test_expired_acceptance_is_not_current(self) -> None:
        contact = self.write_contact()
        self.write_acceptance(contact, expires_at="2026-09-06T00:00:00Z")
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertIn("ACCEPTANCE_NOT_CURRENT", decision.reasons)

    def test_expiry_boundary_is_exclusive(self) -> None:
        contact = self.write_contact()
        self.write_acceptance(contact, expires_at="2026-09-06T12:00:00Z")
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertIn("ACCEPTANCE_NOT_CURRENT", decision.reasons)

    def test_revocation_ends_relation(self) -> None:
        contact = self.write_contact()
        self.write_acceptance(contact)
        self.assertTrue(proto.check_relation(self.root, contact, NOW).admitted)
        self.write_revocation(contact)
        decision = proto.check_relation(self.root, contact, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("REVOKED", decision.reasons)

    def test_relations_do_not_transfer_between_identities(self) -> None:
        contact_a = self.write_contact(name="a.json", identity="visitor-a")
        contact_b = self.write_contact(name="b.json", identity="visitor-b")
        self.write_acceptance(contact_a, relation="relation_a")
        self.assertTrue(proto.check_relation(self.root, contact_a, NOW).admitted)
        self.assertFalse(proto.check_relation(self.root, contact_b, NOW).admitted)


class TestLiveLocality(unittest.TestCase):
    def test_live_anchors_are_intact(self) -> None:
        self.assertIsNotNone(proto.read_recorded_terms_hash(LIVE_LOCALITY))
        self.assertIsNotNone(proto.read_recorded_dossier_hash(LIVE_LOCALITY))

    def test_live_locality_has_all_surfaces(self) -> None:
        for name in (
            proto.PRESENCE_DIR_NAME,
            proto.TERMS_DIR_NAME,
            proto.VESTIBULE_DIR_NAME,
            proto.CONTACT_DIR_NAME,
            proto.REVIEW_DIR_NAME,
            proto.RELATIONS_DIR_NAME,
            proto.REVOCATIONS_DIR_NAME,
        ):
            self.assertTrue((LIVE_LOCALITY / name).is_dir(), name)

    def test_live_vestibule_renders(self) -> None:
        packet = proto.build_vestibule(LIVE_LOCALITY)
        self.assertIsNotNone(packet)
        self.assertEqual(packet["grants"], "NOTHING")

    def test_live_locality_admits_nobody_yet(self) -> None:
        for path in (LIVE_LOCALITY / proto.CONTACT_DIR_NAME).glob("*.json"):
            self.assertFalse(proto.check_relation(LIVE_LOCALITY, path).admitted)


class TestCommandLine(ContactProtocolTestBase):
    def test_cli_check_exit_codes(self) -> None:
        contact = self.write_contact()
        self.assertEqual(proto.main(["check", str(self.root), str(contact)]), 1)
        self.write_acceptance(
            contact,
            accepted_at="2026-01-01T00:00:00Z",
            expires_at="2126-01-01T00:00:00Z",
        )
        self.assertEqual(proto.main(["check", str(self.root), str(contact)]), 0)
        self.assertEqual(proto.main(["nonsense"]), 2)

    def test_cli_seal_and_vestibule(self) -> None:
        self.assertEqual(proto.main(["seal", str(self.root)]), 0)
        self.assertEqual(proto.main(["vestibule", str(self.root)]), 0)


if __name__ == "__main__":
    unittest.main()
