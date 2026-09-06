"""Tests for the admission gate v0 stateless gatekeeper."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

import admission_gate_v0 as gate

REPO_ROOT = Path(__file__).resolve().parents[1]
LIVE_GATE_ROOT = REPO_ROOT / "admission_gate"

NOW = datetime(2026, 9, 6, 12, 0, 0, tzinfo=timezone.utc)


class AdmissionGateTestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="admission_gate_test_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        (self.root / gate.REQUESTS_DIR_NAME).mkdir()
        (self.root / gate.GRANTS_DIR_NAME).mkdir()
        (self.root / gate.REVOCATIONS_DIR_NAME).mkdir()
        terms_path = self.root / gate.TERMS_FILE_NAME
        terms_path.write_text("terms body\n", encoding="utf-8")
        self.terms_hash = gate.sha256_of_file(terms_path)
        (self.root / gate.TERMS_HASH_FILE_NAME).write_text(
            self.terms_hash + "\n", encoding="utf-8"
        )

    def write_request(
        self,
        name: str = "visitor_001.json",
        identity: str = "visitor-a",
        terms_hash: str | None = None,
        requested_at: str = "2026-09-01T00:00:00Z",
        **overrides: object,
    ) -> Path:
        body = {
            "identity": identity,
            "accepted_terms_sha256": (
                self.terms_hash if terms_hash is None else terms_hash
            ),
            "requested_scope": "read",
            "requested_at": requested_at,
        }
        body.update(overrides)
        path = self.root / gate.REQUESTS_DIR_NAME / name
        path.write_text(json.dumps(body, indent=1), encoding="utf-8")
        return path

    def write_grant(
        self,
        request_path: Path,
        name: str = "grant_001.json",
        granted_at: str = "2026-09-05T00:00:00Z",
        expires_at: str = "2026-09-08T00:00:00Z",
        **overrides: object,
    ) -> Path:
        body = {
            "request_sha256": gate.sha256_of_file(request_path),
            "granted_scope": "read",
            "granted_at": granted_at,
            "expires_at": expires_at,
        }
        body.update(overrides)
        path = self.root / gate.GRANTS_DIR_NAME / name
        path.write_text(json.dumps(body, indent=1), encoding="utf-8")
        return path

    def write_revocation(self, request_path: Path, name: str = "rev_001.json") -> Path:
        body = {
            "request_sha256": gate.sha256_of_file(request_path),
            "revoked_at": "2026-09-06T00:00:00Z",
        }
        path = self.root / gate.REVOCATIONS_DIR_NAME / name
        path.write_text(json.dumps(body, indent=1), encoding="utf-8")
        return path


class TestLawfulAdmission(AdmissionGateTestBase):
    def test_full_lawful_chain_is_admitted(self) -> None:
        request = self.write_request()
        self.write_grant(request)
        decision = gate.check_admission(self.root, request, NOW)
        self.assertTrue(decision.admitted)
        self.assertEqual(decision.outcome, gate.ADMITTED)
        self.assertEqual(decision.reasons, ())

    def test_check_is_reproducible(self) -> None:
        request = self.write_request()
        self.write_grant(request)
        first = gate.check_admission(self.root, request, NOW)
        second = gate.check_admission(self.root, request, NOW)
        self.assertEqual(first, second)


class TestDefaultDeny(AdmissionGateTestBase):
    def test_no_grant_means_not_admitted(self) -> None:
        request = self.write_request()
        decision = gate.check_admission(self.root, request, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("NO_GRANT", decision.reasons)

    def test_waiting_never_becomes_admission(self) -> None:
        request = self.write_request()
        far_future = datetime(2126, 1, 1, tzinfo=timezone.utc)
        decision = gate.check_admission(self.root, request, far_future)
        self.assertFalse(decision.admitted)
        self.assertIn("NO_GRANT", decision.reasons)

    def test_missing_request_file_not_admitted(self) -> None:
        missing = self.root / gate.REQUESTS_DIR_NAME / "ghost.json"
        decision = gate.check_admission(self.root, missing, NOW)
        self.assertFalse(decision.admitted)
        self.assertEqual(decision.reasons, ("REQUEST_VOID",))


class TestVoidRequests(AdmissionGateTestBase):
    def test_wrong_terms_hash_is_not_accepted(self) -> None:
        request = self.write_request(terms_hash="0" * 64)
        self.write_grant(request)
        decision = gate.check_admission(self.root, request, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("TERMS_NOT_ACCEPTED", decision.reasons)

    def test_missing_field_is_void(self) -> None:
        path = self.root / gate.REQUESTS_DIR_NAME / "bad.json"
        path.write_text(
            json.dumps({"identity": "visitor-a", "requested_scope": "read"}),
            encoding="utf-8",
        )
        decision = gate.check_admission(self.root, path, NOW)
        self.assertEqual(decision.reasons, ("REQUEST_VOID",))

    def test_extra_field_is_void(self) -> None:
        request = self.write_request(extra="field")
        decision = gate.check_admission(self.root, request, NOW)
        self.assertEqual(decision.reasons, ("REQUEST_VOID",))

    def test_malformed_json_is_void(self) -> None:
        path = self.root / gate.REQUESTS_DIR_NAME / "broken.json"
        path.write_text("{not json", encoding="utf-8")
        decision = gate.check_admission(self.root, path, NOW)
        self.assertEqual(decision.reasons, ("REQUEST_VOID",))


class TestStandingRequest(AdmissionGateTestBase):
    def test_newer_request_invalidates_older(self) -> None:
        old = self.write_request(name="a.json", requested_at="2026-09-01T00:00:00Z")
        new = self.write_request(name="b.json", requested_at="2026-09-02T00:00:00Z")
        self.write_grant(old, name="grant_old.json")
        decision = gate.check_admission(self.root, old, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("REQUEST_NOT_STANDING", decision.reasons)
        self.assertEqual(
            gate.standing_request_path(self.root, "visitor-a"), new
        )

    def test_grant_does_not_transfer_to_newer_request(self) -> None:
        old = self.write_request(name="a.json", requested_at="2026-09-01T00:00:00Z")
        self.write_grant(old)
        new = self.write_request(name="b.json", requested_at="2026-09-02T00:00:00Z")
        decision = gate.check_admission(self.root, new, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("NO_GRANT", decision.reasons)

    def test_ambiguous_identical_timestamps_leave_no_standing_request(self) -> None:
        self.write_request(name="a.json", requested_at="2026-09-01T00:00:00Z")
        self.write_request(name="b.json", requested_at="2026-09-01T00:00:00Z")
        self.assertIsNone(gate.standing_request_path(self.root, "visitor-a"))

    def test_identities_do_not_interfere(self) -> None:
        request_a = self.write_request(name="a.json", identity="visitor-a")
        request_b = self.write_request(name="b.json", identity="visitor-b")
        self.write_grant(request_a, name="grant_a.json")
        self.assertTrue(gate.check_admission(self.root, request_a, NOW).admitted)
        self.assertFalse(gate.check_admission(self.root, request_b, NOW).admitted)


class TestGrantBinding(AdmissionGateTestBase):
    def test_grant_binds_to_exact_request_bytes(self) -> None:
        request = self.write_request()
        self.write_grant(request)
        request.write_text(
            request.read_text(encoding="utf-8") + "\n", encoding="utf-8"
        )
        decision = gate.check_admission(self.root, request, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("NO_GRANT", decision.reasons)

    def test_grant_for_unmade_request_admits_nothing(self) -> None:
        request = self.write_request()
        self.write_grant(request, request_sha256="f" * 64)
        decision = gate.check_admission(self.root, request, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("NO_GRANT", decision.reasons)

    def test_malformed_grant_is_ignored(self) -> None:
        request = self.write_request()
        path = self.root / gate.GRANTS_DIR_NAME / "bad_grant.json"
        path.write_text("{not json", encoding="utf-8")
        decision = gate.check_admission(self.root, request, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("NO_GRANT", decision.reasons)


class TestPerishabilityAndRevocation(AdmissionGateTestBase):
    def test_expired_grant_is_not_current(self) -> None:
        request = self.write_request()
        self.write_grant(request, expires_at="2026-09-06T00:00:00Z")
        decision = gate.check_admission(self.root, request, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("GRANT_NOT_CURRENT", decision.reasons)

    def test_grant_not_yet_effective_is_not_current(self) -> None:
        request = self.write_request()
        self.write_grant(request, granted_at="2026-09-07T00:00:00Z")
        decision = gate.check_admission(self.root, request, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("GRANT_NOT_CURRENT", decision.reasons)

    def test_expiry_boundary_is_exclusive(self) -> None:
        request = self.write_request()
        self.write_grant(request, expires_at="2026-09-06T12:00:00Z")
        decision = gate.check_admission(self.root, request, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("GRANT_NOT_CURRENT", decision.reasons)

    def test_revocation_ends_admission(self) -> None:
        request = self.write_request()
        self.write_grant(request)
        self.assertTrue(gate.check_admission(self.root, request, NOW).admitted)
        self.write_revocation(request)
        decision = gate.check_admission(self.root, request, NOW)
        self.assertFalse(decision.admitted)
        self.assertIn("REVOKED", decision.reasons)


class TestBrokenAnchorFailsClosed(AdmissionGateTestBase):
    def test_missing_terms_hash_file_admits_nobody(self) -> None:
        (self.root / gate.TERMS_HASH_FILE_NAME).unlink()
        request = self.write_request()
        self.write_grant(request)
        decision = gate.check_admission(self.root, request, NOW)
        self.assertEqual(decision.reasons, ("TERMS_ANCHOR_MISSING_OR_BROKEN",))

    def test_tampered_terms_file_admits_nobody(self) -> None:
        request = self.write_request()
        self.write_grant(request)
        (self.root / gate.TERMS_FILE_NAME).write_text(
            "modified terms\n", encoding="utf-8"
        )
        decision = gate.check_admission(self.root, request, NOW)
        self.assertEqual(decision.reasons, ("TERMS_ANCHOR_MISSING_OR_BROKEN",))


class TestLiveGateAnchor(unittest.TestCase):
    def test_live_terms_anchor_is_intact(self) -> None:
        self.assertIsNotNone(gate.read_recorded_terms_hash(LIVE_GATE_ROOT))

    def test_live_gate_has_all_surfaces(self) -> None:
        for name in (
            gate.REQUESTS_DIR_NAME,
            gate.GRANTS_DIR_NAME,
            gate.REVOCATIONS_DIR_NAME,
        ):
            self.assertTrue((LIVE_GATE_ROOT / name).is_dir(), name)

    def test_live_gate_admits_nobody_yet(self) -> None:
        for path in (LIVE_GATE_ROOT / gate.REQUESTS_DIR_NAME).glob("*.json"):
            decision = gate.check_admission(LIVE_GATE_ROOT, path)
            self.assertFalse(decision.admitted)


class TestCommandLine(AdmissionGateTestBase):
    def test_cli_exit_codes(self) -> None:
        request = self.write_request()
        self.assertEqual(gate.main([str(self.root), str(request)]), 1)
        self.write_grant(
            request,
            granted_at="2026-01-01T00:00:00Z",
            expires_at="2126-01-01T00:00:00Z",
        )
        self.assertEqual(gate.main([str(self.root), str(request)]), 0)
        self.assertEqual(gate.main([str(self.root)]), 2)


if __name__ == "__main__":
    unittest.main()
