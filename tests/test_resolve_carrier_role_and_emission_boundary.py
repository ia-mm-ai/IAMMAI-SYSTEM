"""Tests for bounded carrier role and emission boundary resolution.

This suite audits one role/emission boundary resolver. It verifies that carrier
roles remain operation-local, emissions remain local outputs permitted only by
role, and neither role nor emission becomes source, currentness, authority,
permission, successor, body, signal, presence, threshold, truth, action,
consequence, multi-carrier law, distributed standing, or continuation.
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

import resolve_carrier_role_and_emission_boundary as resolver


TOP_LEVEL_SECTIONS = {
    "carrier_role_emission_metadata",
    "declared_carrier_operation",
    "selected_carrier",
    "carrier_role_basis",
    "emission_basis",
    "role_checks",
    "emission_checks",
    "role_statement",
    "emission_statement",
    "what_role_does_not_mean",
    "what_emission_does_not_mean",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "carrier_role_emission_summary",
}

EXPECTED_ROLE_CHECK_NAMES = {
    "declared_carrier_operation_is_parseable_mapping",
    "carrier_role_declared",
    "carrier_role_supported_admitted",
    "selected_carrier_declared",
    "operation_purpose_declared",
    "carrier_role_is_operation_local",
    "carrier_role_is_not_permanent_identity",
    "carrier_role_does_not_create_source",
    "carrier_role_does_not_create_currentness",
    "carrier_role_does_not_create_authority",
    "carrier_role_does_not_create_permission",
    "carrier_role_does_not_create_successor",
    "carrier_role_does_not_create_body",
    "latest_file_currentness_false",
    "recency_fraud_false",
    "mutation_replay_merge_false",
    "required_non_claims_remain_false",
}

EXPECTED_EMISSION_CHECK_NAMES = {
    "emission_class_declared_when_emission_requested",
    "receiving_carrier_does_not_emit_self_orientation",
    "receiving_carrier_does_not_emit_conformance",
    "holding_carrier_does_not_claim_receipt",
    "returning_carrier_does_not_alter_receipt_meaning",
    "refusing_carrier_does_not_invalidate_source",
    "emission_class_supported",
    "emission_class_permitted_for_role",
    "carrier_local_emission_does_not_self_admit",
    "carrier_emission_does_not_create_signal_by_default",
    "carrier_emission_does_not_establish_presence",
    "carrier_emission_does_not_establish_threshold",
    "carrier_emission_does_not_create_truth",
    "carrier_emission_does_not_authorize_action",
    "carrier_emission_does_not_create_consequence",
    "carrier_emission_does_not_create_multi_carrier_law",
    "carrier_emission_does_not_create_distributed_standing",
    "carrier_emission_does_not_authorize_continuation",
}

ROLE_NON_MEANING_TRUE_KEYS = {
    "does_not_mean_permanent_identity",
    "does_not_mean_source",
    "does_not_mean_currentness",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_successor",
    "does_not_mean_body",
    "does_not_mean_participant_by_default",
    "does_not_mean_multi_carrier_law",
    "does_not_mean_distributed_standing",
    "does_not_mean_presence",
    "does_not_mean_threshold",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_consequence",
    "does_not_mean_continuation",
}

EMISSION_NON_MEANING_TRUE_KEYS = {
    "does_not_mean_body_line_admission",
    "does_not_mean_source",
    "does_not_mean_currentness",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_successor",
    "does_not_mean_body",
    "does_not_mean_signal_by_default",
    "does_not_mean_presence",
    "does_not_mean_threshold",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_consequence",
    "does_not_mean_carrier_relation",
    "does_not_mean_multi_carrier_law",
    "does_not_mean_distributed_standing",
    "does_not_mean_continuation",
}

OPEN_SURFACES = {
    "carrier return/admission boundary",
    "cross-carrier divergence boundary",
    "cross-carrier currentness boundary",
    "multi-carrier relation law",
    "multi-carrier relation conformance",
    "multi-carrier relation closure",
    "distributed standing",
    "persistence/registry law",
    "presence law",
    "threshold law",
    "truth law",
    "action/consequence law",
    "generalized vessel relation lifecycle",
    "body relevance medium",
    "signal series or accumulation logic",
    "successor carrier law",
    "future self-orientation successor only if separately justified",
}

PERMITTED_ROLE_EMISSIONS = (
    ("SOURCE_CARRIER_FOR_PACKET", "CARRIED_PACKET"),
    ("SOURCE_CARRIER_FOR_PACKET", "PACKET_MANIFEST"),
    ("SOURCE_CARRIER_FOR_PACKET", "INTEGRITY_EVIDENCE"),
    ("SOURCE_CARRIER_FOR_PACKET", "TRANSFER_DECLARATION"),
    ("RECEIVING_CARRIER", "CARRIED_SURFACE_RECEIPT"),
    ("RECEIVING_CARRIER", "RECEIPT_BLOCK"),
    ("RECEIVING_CARRIER", "RECEIPT_REFUSAL_REASON"),
    ("HOLDING_CARRIER", "PASSIVE_STORAGE_STATUS"),
    ("RETURNING_CARRIER", "RETURNED_RECEIPT_EVIDENCE"),
    ("RETURNING_CARRIER", "RETURNED_BLOCKED_RECEIPT_EVIDENCE"),
    ("RETURNING_CARRIER", "RETURNED_EVIDENCE_PACKET"),
    ("REFUSING_CARRIER", "RECEIPT_BLOCK"),
    ("REFUSING_CARRIER", "RECEIPT_REFUSAL_REASON"),
    ("REFUSING_CARRIER", "FAILED_CHECKS"),
    ("REFUSING_CARRIER", "PRESERVED_BASIS"),
)

NOT_ADMITTED_EMISSIONS = (
    "SELF_ORIENTATION",
    "BODY_CONFORMANCE",
    "CURRENTNESS",
    "STANDING_UPGRADE",
    "SOURCE_AUTHORITY",
    "SUCCESSOR_ARTIFACT",
    "PRESENCE",
    "THRESHOLD",
    "TRUTH",
    "ACTION",
    "CONSEQUENCE",
    "MULTI_CARRIER_RELATION",
    "DISTRIBUTED_STANDING",
    "CARRIER_REGISTRY",
    "REPOSITORY_SYNCHRONIZATION",
    "SIGNAL_BY_DEFAULT",
    "BODY_RELEVANCE_MEDIUM",
    "WORKFLOW",
    "ROUTING",
    "CONTINUATION_AUTHORIZATION",
)

OUTCOME_FAMILY = {
    "CARRIER_ROLE_RECOGNIZED",
    "CARRIER_EMISSION_RECOGNIZED",
    "CARRIER_ROLE_EMISSION_BLOCKED",
}


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


def _false_non_claims(**updates: bool) -> dict[str, bool]:
    claims = copy.deepcopy(resolver.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _packet_or_surface() -> dict[str, object]:
    return {
        "selected_packet_or_surface_id": "selected-surface-001",
        "selected_packet_or_surface_outcome": "CARRIED_SURFACE_RECEIVED",
        "source_downstream_posture": "carrier_local_emission_basis_only",
    }


def _operation(
    *,
    role: str | None = "SOURCE_CARRIER_FOR_PACKET",
    emission: str | None = None,
    selected_carrier: object | None = None,
    purpose: object = "Record one operation-local carrier role or emission.",
    non_claims: dict[str, bool] | None = None,
    include_selected_packet: bool = True,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    operation: dict[str, object] = {
        "operation_id": "carrier-role-operation-001",
        "operation_purpose": purpose,
        "operation_scope": "declared_operation_local",
        "selected_carrier": (
            selected_carrier
            if selected_carrier is not None
            else {
                "carrier_id": "carrier-test-001",
                "carrier_label": "bounded test carrier",
                "carrier_role_for_operation": role,
                "carrier_role_operation_local": True,
                "carrier_role_permanent_identity": False,
            }
        ),
        "declared_non_claims": copy.deepcopy(non_claims or _false_non_claims()),
    }
    if role is not None:
        operation["declared_carrier_role"] = role
    if emission is not None:
        operation["declared_emission_class"] = emission
        operation["emission_identity"] = f"{emission.lower()}-001"
        operation["emission_outcome"] = "LOCAL_EMISSION_ONLY"
    if include_selected_packet:
        operation["selected_packet_or_surface"] = _packet_or_surface()
    if extra:
        operation.update(copy.deepcopy(extra))
    return operation


def _resolve(operation: dict[str, object]) -> dict:
    return resolver.resolve_carrier_role_and_emission_boundary(
        declared_carrier_operation=operation
    )


class CarrierRoleAndEmissionBoundaryTests(unittest.TestCase):
    def assertTopLevelShape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result.keys()))
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assertBlocked(self, result: dict, code: str | set[str]) -> None:
        self.assertEqual("CARRIER_ROLE_EMISSION_BLOCKED", result["outcome"])
        expected = {code} if isinstance(code, str) else code
        self.assertIn(result["block"]["code"], expected)
        self.assertIn(result["block"]["block_code"], expected)
        self.assertFalse(result["role_statement"]["carrier_role_recognized"])
        self.assertFalse(result["emission_statement"]["carrier_emission_recognized"])
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assertNonClaimsFalse(self, result: dict) -> None:
        for key in resolver.REQUIRED_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIn(key, result["non_claims"])
                self.assertIs(result["non_claims"][key], False)

    def assertRecognizedNonCollapse(self, result: dict) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertNonClaimsFalse(result)
        summary = resolver.build_carrier_role_and_emission_summary(result)
        for key in (
            "source_created",
            "currentness_created",
            "authority_created",
            "permission_created",
            "successor_created",
            "body_created",
            "signal_created_by_default",
            "presence_established",
            "threshold_met",
            "truth_created",
            "action_authorized",
            "consequence_created",
            "multi_carrier_law_created",
            "distributed_standing_created",
            "continuation_authorized",
        ):
            with self.subTest(summary_flag=key):
                self.assertIs(summary[key], False)

    def assertChecksHaveShape(self, result: dict) -> None:
        for check in result["role_checks"] + result["emission_checks"]:
            with self.subTest(check=check.get("check_name")):
                self.assertIn("check_name", check)
                self.assertIn("passed", check)
                self.assertIn("expected_posture", check)
                self.assertIn("actual_posture", check)
                self.assertIn("block_code", check)

    def assertNoFailedChecks(self, result: dict) -> None:
        self.assertEqual(0, result["carrier_role_emission_summary"]["failed_check_count"])
        for check in result["role_checks"] + result["emission_checks"]:
            with self.subTest(check=check["check_name"]):
                self.assertIs(check["passed"], True)

    def test_successful_role_only_recognition(self) -> None:
        result = _resolve(_operation(role="SOURCE_CARRIER_FOR_PACKET"))

        self.assertIsInstance(result, dict)
        self.assertTopLevelShape(result)
        self.assertEqual("CARRIER_ROLE_RECOGNIZED", result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        self.assertTrue(result["role_statement"]["carrier_role_recognized"])
        self.assertFalse(result["emission_statement"]["carrier_emission_recognized"])
        self.assertTrue(result["role_statement"]["carrier_role_operation_local"])
        self.assertFalse(result["role_statement"]["carrier_role_permanent_identity"])
        self.assertTrue(result["emission_statement"]["no_emission_was_recognized"])
        self.assertRecognizedNonCollapse(result)

    def test_successful_emission_recognition_for_each_admitted_role(self) -> None:
        for role, emission in PERMITTED_ROLE_EMISSIONS:
            with self.subTest(role=role, emission=emission):
                result = _resolve(_operation(role=role, emission=emission))

                self.assertEqual("CARRIER_EMISSION_RECOGNIZED", result["outcome"])
                self.assertEqual(emission, result["emission_basis"]["emission_class"])
                self.assertTrue(result["emission_basis"]["emission_class_permitted_for_role"])
                self.assertTrue(result["role_statement"]["carrier_role_recognized"])
                self.assertTrue(result["emission_statement"]["carrier_emission_recognized"])
                self.assertTrue(result["emission_statement"]["carrier_emission_local_only"])
                self.assertFalse(result["emission_statement"]["carrier_emission_self_admitted"])
                self.assertRecognizedNonCollapse(result)

    def test_metadata(self) -> None:
        metadata = _resolve(_operation(emission="CARRIED_PACKET"))[
            "carrier_role_emission_metadata"
        ]

        for key in (
            "carrier_role_emission_result_id",
            "carrier_role_emission_result_type",
            "carrier_role_emission_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["carrier_role_emission_result_version"])
        self.assertEqual(
            "resolve_carrier_role_and_emission_boundary",
            metadata["resolver_module"],
        )

    def test_declared_carrier_operation_basis(self) -> None:
        operation = _operation(
            role="SOURCE_CARRIER_FOR_PACKET",
            emission="CARRIED_PACKET",
            extra={
                "source_carrier_context": {"carrier_id": "source-carrier"},
                "receiving_carrier_context": {"carrier_id": "receiving-carrier"},
                "integrity_evidence": {"hash_algorithm": "sha256"},
            },
        )
        result_operation = _resolve(operation)["declared_carrier_operation"]

        self.assertEqual("carrier-role-operation-001", result_operation["operation_id"])
        self.assertEqual(operation["operation_purpose"], result_operation["operation_purpose"])
        self.assertEqual("declared_operation_local", result_operation["operation_scope"])
        self.assertEqual("SOURCE_CARRIER_FOR_PACKET", result_operation["declared_carrier_role"])
        self.assertEqual("CARRIED_PACKET", result_operation["declared_emission_class"])
        self.assertEqual(operation["selected_packet_or_surface"], result_operation["selected_packet_or_surface"])
        self.assertEqual(operation["declared_non_claims"], result_operation["declared_non_claims"])
        self.assertEqual(operation["integrity_evidence"], result_operation["integrity_evidence"])

    def test_selected_carrier_basis(self) -> None:
        selected = _resolve(_operation())["selected_carrier"]

        self.assertEqual("carrier-test-001", selected["carrier_id"])
        self.assertEqual("bounded test carrier", selected["carrier_label"])
        self.assertEqual("SOURCE_CARRIER_FOR_PACKET", selected["carrier_role_for_operation"])
        self.assertTrue(selected["role_is_operation_local"])
        self.assertTrue(selected["role_is_not_permanent_identity"])

    def test_carrier_role_basis(self) -> None:
        basis = _resolve(_operation(role="RETURNING_CARRIER"))["carrier_role_basis"]

        self.assertEqual("RETURNING_CARRIER", basis["role_name"])
        self.assertTrue(basis["role_admitted"])
        self.assertFalse(basis["role_candidate_not_admitted"])
        self.assertEqual("operation_local", basis["role_local_scope"])
        self.assertIn("RETURNED_RECEIPT_EVIDENCE", basis["permitted_emissions"])
        self.assertIn("SELF_ORIENTATION", basis["prohibited_emissions"])
        self.assertTrue(basis["role_non_meaning"]["does_not_mean_authority"])

    def test_emission_basis(self) -> None:
        result = _resolve(
            _operation(role="RETURNING_CARRIER", emission="RETURNED_RECEIPT_EVIDENCE")
        )
        basis = result["emission_basis"]

        self.assertTrue(basis["emission_requested"])
        self.assertEqual("RETURNED_RECEIPT_EVIDENCE", basis["emission_class"])
        self.assertTrue(basis["emission_class_supported"])
        self.assertTrue(basis["emission_class_permitted_for_role"])
        self.assertEqual(_packet_or_surface(), basis["emission_source_packet_or_surface"])
        self.assertEqual("not_admitted_by_this_result", basis["body_line_admission_status"])

    def test_role_statement(self) -> None:
        statement = _resolve(_operation())["role_statement"]

        self.assertTrue(statement["carrier_role_recognized"])
        self.assertTrue(statement["carrier_role_operation_local"])
        self.assertFalse(statement["carrier_role_permanent_identity"])
        for key in (
            "carrier_role_created_source",
            "carrier_role_created_currentness",
            "carrier_role_created_authority",
            "carrier_role_created_permission",
            "carrier_role_created_successor",
            "carrier_role_created_body",
            "multi_carrier_law_created",
            "distributed_standing_created",
        ):
            self.assertIs(statement[key], False)

    def test_emission_statement(self) -> None:
        result = _resolve(_operation(emission="CARRIED_PACKET"))
        statement = result["emission_statement"]

        self.assertTrue(statement["carrier_emission_recognized"])
        self.assertTrue(statement["carrier_emission_class_permitted_for_role"])
        self.assertTrue(statement["carrier_emission_local_only"])
        for key in (
            "carrier_emission_self_admitted",
            "carrier_emission_created_signal_by_default",
            "carrier_emission_established_presence",
            "carrier_emission_established_threshold",
            "carrier_emission_created_truth",
            "carrier_emission_authorized_action",
            "carrier_emission_created_consequence",
            "carrier_emission_created_multi_carrier_law",
            "carrier_emission_created_distributed_standing",
            "carrier_emission_authorized_continuation",
        ):
            self.assertIs(statement[key], False)

        role_only = _resolve(_operation())["emission_statement"]
        self.assertFalse(role_only["carrier_emission_recognized"])
        self.assertTrue(role_only["no_emission_was_recognized"])

    def test_non_meaning_sections(self) -> None:
        result = _resolve(_operation(emission="CARRIED_PACKET"))

        for key in ROLE_NON_MEANING_TRUE_KEYS:
            with self.subTest(role_non_meaning=key):
                self.assertIs(result["what_role_does_not_mean"][key], True)
        for key in EMISSION_NON_MEANING_TRUE_KEYS:
            with self.subTest(emission_non_meaning=key):
                self.assertIs(result["what_emission_does_not_mean"][key], True)

    def test_what_remains_open(self) -> None:
        remains_open = _resolve(_operation())["what_remains_open"]

        self.assertTrue(OPEN_SURFACES.issubset(set(remains_open["open_surfaces"])))
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])

    def test_checks_shape_and_success_counts(self) -> None:
        result = _resolve(_operation(emission="CARRIED_PACKET"))
        role_names = {check["check_name"] for check in result["role_checks"]}
        emission_names = {check["check_name"] for check in result["emission_checks"]}

        self.assertChecksHaveShape(result)
        self.assertNoFailedChecks(result)
        self.assertTrue(EXPECTED_ROLE_CHECK_NAMES.issubset(role_names))
        self.assertTrue(EXPECTED_EMISSION_CHECK_NAMES.issubset(emission_names))

    def test_summary_helper(self) -> None:
        result = _resolve(_operation(emission="CARRIED_PACKET"))
        summary = resolver.build_carrier_role_and_emission_summary(result)

        self.assertEqual("CARRIER_EMISSION_RECOGNIZED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual("carrier-role-operation-001", summary["operation_id"])
        self.assertEqual(result["declared_carrier_operation"]["operation_purpose"], summary["operation_purpose"])
        self.assertEqual("carrier-test-001", summary["selected_carrier_id"])
        self.assertEqual("bounded test carrier", summary["selected_carrier_label"])
        self.assertEqual("SOURCE_CARRIER_FOR_PACKET", summary["declared_carrier_role"])
        self.assertEqual("CARRIED_PACKET", summary["declared_emission_class"])
        self.assertTrue(summary["role_recognized"])
        self.assertTrue(summary["emission_recognized"])
        self.assertTrue(summary["role_operation_local"])
        self.assertFalse(summary["role_permanent_identity"])
        self.assertTrue(summary["emission_local_only"])
        self.assertFalse(summary["emission_self_admitted"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        for key in (
            "source_created",
            "currentness_created",
            "authority_created",
            "permission_created",
            "successor_created",
            "body_created",
            "signal_created_by_default",
            "presence_established",
            "threshold_met",
            "truth_created",
            "action_authorized",
            "consequence_created",
            "multi_carrier_law_created",
            "distributed_standing_created",
            "continuation_authorized",
        ):
            self.assertIs(summary[key], False)
        self.assertIn("authority_created", summary["key_non_claims"])

    def test_result_level_non_claims_for_recognized_and_blocked_results(self) -> None:
        recognized = _resolve(_operation())
        blocked_operation = _operation()
        blocked_operation["declared_non_claims"].pop("authority_created")
        blocked = _resolve(blocked_operation)

        self.assertNonClaimsFalse(recognized)
        for key in resolver.REQUIRED_NON_CLAIMS:
            self.assertIn(key, blocked["non_claims"])
        self.assertBlocked(blocked, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_operation_builder_helper(self) -> None:
        selected = {"surface_id": "selected-surface-helper"}
        role_operation = resolver.build_declared_carrier_operation(
            "helper-role-op",
            "Recognize a helper-built role.",
            "helper-carrier",
            "SOURCE_CARRIER_FOR_PACKET",
            selected_packet_or_surface=selected,
        )
        emission_operation = resolver.build_declared_carrier_operation(
            "helper-emission-op",
            "Recognize a helper-built emission.",
            "helper-carrier",
            "SOURCE_CARRIER_FOR_PACKET",
            "CARRIED_PACKET",
            selected,
        )

        self.assertEqual("helper-carrier", role_operation["selected_carrier"]["carrier_id"])
        self.assertEqual("SOURCE_CARRIER_FOR_PACKET", role_operation["declared_carrier_role"])
        self.assertEqual(selected, role_operation["selected_packet_or_surface"])
        self.assertNotIn("declared_emission_class", role_operation)
        self.assertEqual("CARRIED_PACKET", emission_operation["declared_emission_class"])
        for key in resolver.REQUIRED_NON_CLAIMS:
            self.assertIs(role_operation["declared_non_claims"][key], False)
            self.assertIs(emission_operation["declared_non_claims"][key], False)
        self.assertEqual("CARRIER_ROLE_RECOGNIZED", _resolve(role_operation)["outcome"])
        self.assertEqual("CARRIER_EMISSION_RECOGNIZED", _resolve(emission_operation)["outcome"])

    def test_path_based_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "operation.json"
            _write_json(path, _operation(emission="CARRIED_PACKET"))

            result = resolver.resolve_carrier_role_and_emission_boundary_from_path(path)

        self.assertTopLevelShape(result)
        self.assertEqual("CARRIER_EMISSION_RECOGNIZED", result["outcome"])
        self.assertEqual(str(path), result["declared_carrier_operation"]["declared_carrier_operation_path"])

    def test_write_behavior(self) -> None:
        result = _resolve(_operation(emission="CARRIED_PACKET"))
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "nested" / "result.json"

            written = resolver.write_carrier_role_and_emission_result(result, output_path)
            loaded = _read_json(written)

        self.assertEqual(output_path, written)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(loaded.keys()))
        self.assertEqual("CARRIER_EMISSION_RECOGNIZED", loaded["outcome"])

    def test_default_output_path_behavior(self) -> None:
        result = _resolve(_operation(emission="CARRIED_PACKET"))
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "role-emission-root"
            with mock.patch.object(resolver, "CARRIER_ROLE_AND_EMISSION_BOUNDARY_ROOT", root):
                first = resolver.write_carrier_role_and_emission_result(result)
                second = resolver.write_carrier_role_and_emission_result(result)

            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__carrier_role_emission_result.json"))
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        operation = _operation(emission="CARRIED_PACKET")
        packet_before = copy.deepcopy(operation["selected_packet_or_surface"])
        operation_before = copy.deepcopy(operation)

        first = _resolve(operation)
        second = _resolve(operation)

        self.assertEqual(operation_before, operation)
        self.assertEqual(packet_before, operation["selected_packet_or_surface"])
        self.assertEqual("CARRIER_EMISSION_RECOGNIZED", first["outcome"])
        self.assertEqual("CARRIER_EMISSION_RECOGNIZED", second["outcome"])

    def test_blocking_missing_or_malformed_operation(self) -> None:
        self.assertBlocked(
            resolver.resolve_carrier_role_and_emission_boundary(),
            "DECLARED_CARRIER_OPERATION_MISSING",
        )
        self.assertBlocked(
            resolver.resolve_carrier_role_and_emission_boundary(
                declared_carrier_operation=["not", "mapping"]  # type: ignore[arg-type]
            ),
            "DECLARED_CARRIER_OPERATION_MALFORMED",
        )

    def test_blocking_path_unreadable_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            missing = resolver.resolve_carrier_role_and_emission_boundary_from_path(
                root / "missing.json"
            )
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolver.resolve_carrier_role_and_emission_boundary_from_path(
                malformed_path
            )
            array_path = root / "array.json"
            _write_json(array_path, ["not", "object"])
            array_result = resolver.resolve_carrier_role_and_emission_boundary_from_path(
                array_path
            )

        self.assertBlocked(missing, "DECLARED_CARRIER_OPERATION_UNREADABLE")
        self.assertBlocked(malformed, "DECLARED_CARRIER_OPERATION_MALFORMED")
        self.assertBlocked(array_result, "DECLARED_CARRIER_OPERATION_MALFORMED")

    def test_blocking_role_undeclared(self) -> None:
        self.assertBlocked(_resolve(_operation(role=None)), "CARRIER_ROLE_UNDECLARED")

    def test_blocking_candidate_and_unsupported_roles(self) -> None:
        for role in (
            "WITNESS_CARRIER",
            "COMPARISON_CARRIER",
            "EMITTING_CARRIER",
            "STALE_CARRIER",
            "SUCCESSOR_CARRIER",
            "UNSUPPORTED_CARRIER_ROLE",
        ):
            with self.subTest(role=role):
                self.assertBlocked(_resolve(_operation(role=role)), "CARRIER_ROLE_UNSUPPORTED")

    def test_blocking_selected_carrier_missing(self) -> None:
        self.assertBlocked(
            _resolve(_operation(selected_carrier={"carrier_label": ""})),
            "SELECTED_CARRIER_MISSING",
        )

    def test_blocking_operation_purpose_undeclared(self) -> None:
        self.assertBlocked(
            _resolve(_operation(purpose="")),
            "CARRIER_OPERATION_PURPOSE_UNDECLARED",
        )

    def test_blocking_role_permanent_identity(self) -> None:
        selected_carrier = {
            "carrier_id": "carrier-test-001",
            "carrier_role_for_operation": "SOURCE_CARRIER_FOR_PACKET",
            "carrier_role_operation_local": False,
            "carrier_role_permanent_identity": True,
        }
        self.assertBlocked(
            _resolve(_operation(selected_carrier=selected_carrier)),
            "CARRIER_ROLE_CLAIMS_PERMANENT_IDENTITY",
        )
        self.assertBlocked(
            _resolve(_operation(extra={"operation_scope": "global"})),
            "CARRIER_ROLE_CLAIMS_PERMANENT_IDENTITY",
        )

    def test_blocking_role_collapse_attempts(self) -> None:
        cases = (
            ("carrier_role_creates_source", "CARRIER_ROLE_CREATES_SOURCE"),
            ("carrier_role_creates_currentness", "CARRIER_ROLE_CREATES_CURRENTNESS"),
            ("carrier_role_creates_authority", "CARRIER_ROLE_CREATES_AUTHORITY"),
            ("carrier_role_creates_permission", "CARRIER_ROLE_CREATES_PERMISSION"),
            ("carrier_role_creates_successor", "CARRIER_ROLE_CREATES_SUCCESSOR"),
            ("carrier_role_creates_body", "CARRIER_ROLE_CREATES_BODY"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                self.assertBlocked(_resolve(_operation(extra={flag: True})), code)

    def test_blocking_emission_undeclared_when_requested(self) -> None:
        self.assertBlocked(
            _resolve(_operation(extra={"emission_requested": True})),
            "CARRIER_EMISSION_UNDECLARED",
        )

    def test_blocking_unsupported_not_admitted_emissions(self) -> None:
        for emission in NOT_ADMITTED_EMISSIONS:
            with self.subTest(emission=emission):
                result = _resolve(
                    _operation(role="SOURCE_CARRIER_FOR_PACKET", emission=emission)
                )
                self.assertBlocked(
                    result,
                    {
                        "CARRIER_EMISSION_UNSUPPORTED",
                        "RECEIVING_CARRIER_EMITS_SELF_ORIENTATION",
                        "RECEIVING_CARRIER_EMITS_CONFORMANCE",
                    },
                )

    def test_blocking_emission_outside_role(self) -> None:
        cases = (
            ("SOURCE_CARRIER_FOR_PACKET", "CARRIED_SURFACE_RECEIPT", "CARRIER_EMISSION_OUTSIDE_ROLE"),
            ("RECEIVING_CARRIER", "CARRIED_PACKET", "CARRIER_EMISSION_OUTSIDE_ROLE"),
            ("HOLDING_CARRIER", "CARRIED_SURFACE_RECEIPT", "HOLDING_CARRIER_CLAIMS_RECEIPT"),
            ("RETURNING_CARRIER", "CARRIED_PACKET", "CARRIER_EMISSION_OUTSIDE_ROLE"),
            ("REFUSING_CARRIER", "TRANSFER_DECLARATION", "CARRIER_EMISSION_OUTSIDE_ROLE"),
        )
        for role, emission, code in cases:
            with self.subTest(role=role, emission=emission):
                self.assertBlocked(_resolve(_operation(role=role, emission=emission)), code)

    def test_blocking_receiving_carrier_emits_self_orientation_or_conformance(self) -> None:
        self.assertBlocked(
            _resolve(_operation(role="RECEIVING_CARRIER", emission="SELF_ORIENTATION")),
            "RECEIVING_CARRIER_EMITS_SELF_ORIENTATION",
        )
        self.assertBlocked(
            _resolve(_operation(role="RECEIVING_CARRIER", emission="BODY_CONFORMANCE")),
            "RECEIVING_CARRIER_EMITS_CONFORMANCE",
        )

    def test_blocking_returning_and_refusing_role_misuse(self) -> None:
        self.assertBlocked(
            _resolve(
                _operation(
                    role="RETURNING_CARRIER",
                    emission="RETURNED_RECEIPT_EVIDENCE",
                    extra={"returning_carrier_alters_receipt_meaning": True},
                )
            ),
            "RETURNING_CARRIER_ALTERS_RECEIPT_MEANING",
        )
        self.assertBlocked(
            _resolve(
                _operation(
                    role="REFUSING_CARRIER",
                    emission="RECEIPT_BLOCK",
                    extra={"refusing_carrier_invalidates_source": True},
                )
            ),
            "REFUSING_CARRIER_INVALIDATES_SOURCE",
        )

    def test_blocking_emission_self_admits(self) -> None:
        self.assertBlocked(
            _resolve(_operation(emission="CARRIED_PACKET", extra={"carrier_emission_self_admits": True})),
            "CARRIER_EMISSION_SELF_ADMITS",
        )

    def test_blocking_emission_signal_presence_threshold_truth_action_consequence(self) -> None:
        cases = (
            ("carrier_emission_creates_signal_by_default", "CARRIER_EMISSION_CREATES_SIGNAL_BY_DEFAULT"),
            ("carrier_emission_establishes_presence", "CARRIER_EMISSION_ESTABLISHES_PRESENCE"),
            ("carrier_emission_establishes_threshold", "CARRIER_EMISSION_ESTABLISHES_THRESHOLD"),
            ("carrier_emission_creates_truth", "CARRIER_EMISSION_CREATES_TRUTH"),
            ("carrier_emission_authorizes_action", "CARRIER_EMISSION_AUTHORIZES_ACTION"),
            ("carrier_emission_creates_consequence", "CARRIER_EMISSION_CREATES_CONSEQUENCE"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                self.assertBlocked(
                    _resolve(_operation(emission="CARRIED_PACKET", extra={flag: True})),
                    code,
                )

    def test_blocking_multi_carrier_distributed_and_continuation(self) -> None:
        cases = (
            ("carrier_emission_creates_multi_carrier_law", "CARRIER_EMISSION_CREATES_MULTI_CARRIER_LAW"),
            ("carrier_emission_creates_distributed_standing", "CARRIER_EMISSION_CREATES_DISTRIBUTED_STANDING"),
            ("carrier_emission_authorizes_continuation", "CARRIER_EMISSION_AUTHORIZES_CONTINUATION"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                self.assertBlocked(
                    _resolve(_operation(emission="CARRIED_PACKET", extra={flag: True})),
                    code,
                )

    def test_blocking_latest_file_currentness_recency_and_mutation_replay_merge(self) -> None:
        for flag in ("latest_file_currentness", "recency_fraud"):
            with self.subTest(flag=flag):
                self.assertBlocked(_resolve(_operation(extra={flag: True})), "LATEST_FILE_CURRENTNESS")
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                self.assertBlocked(
                    _resolve(_operation(extra={flag: True})),
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

    def test_blocking_required_non_claim_missing_or_flipped(self) -> None:
        missing = _operation()
        missing["declared_non_claims"].pop("authority_created")
        flipped = _operation(non_claims=_false_non_claims(permission_created=True))

        self.assertBlocked(missing_result := _resolve(missing), "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertBlocked(
            _resolve(flipped),
            {"NON_CLAIM_MISSING_OR_FLIPPED", "CARRIER_ROLE_CREATES_PERMISSION"},
        )
        self.assertIn("authority_created", missing_result["non_claims"])

    def test_blocking_both_role_and_emission_invalid_prioritizes_role(self) -> None:
        result = _resolve(
            _operation(role="UNSUPPORTED_CARRIER_ROLE", emission="UNSUPPORTED_EMISSION")
        )

        self.assertBlocked(result, "CARRIER_ROLE_UNSUPPORTED")
        self.assertFalse(result["emission_statement"]["carrier_emission_recognized"])


if __name__ == "__main__":
    unittest.main()
