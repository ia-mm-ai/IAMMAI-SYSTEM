"""Bounded tests for the portable source-body verification command report module.

These tests prove only bounded report construction. Report building is not
command execution, command invocation, command output from a live run, command
result, command success, source, authority, currentness, final completion,
deployment, runtime hosting, public release, continuation, reusable permission,
or follow-on work.
"""

from __future__ import annotations

import copy
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import portable_source_body_verification_command as command  # noqa: E402
from portable_source_body_verification_command import (  # noqa: E402
    build_portable_verification_command_report,
    build_portable_verification_command_summary,
    write_portable_verification_command_report,
)


BUILT = "PORTABLE_VERIFICATION_COMMAND_REPORT_BUILT"
NOT_BUILT = "PORTABLE_VERIFICATION_COMMAND_REPORT_NOT_BUILT"
REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_VERIFICATION_COMMAND_REPORT_REQUIRES_ADDITIONAL_BASIS"
)
BLOCKED = "PORTABLE_VERIFICATION_COMMAND_REPORT_BLOCKED"
STATUS_FAMILY = {BUILT, NOT_BUILT, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

REQUIRED_NON_CLAIMS = (
    "command_implemented",
    "command_executed",
    "command_authorized_to_run",
    "command_invocation_created",
    "command_output_created",
    "command_result_created",
    "command_success_created",
    "command_output_became_source",
    "command_output_became_authority",
    "command_success_created_currentness",
    "command_success_claimed_final_completion",
    "command_became_authority",
    "full_prior_artifacts_embedded",
    "prior_artifacts_mutated",
    "manifest_implemented",
    "checksum_implemented",
    "signature_implemented",
    "packet_implemented",
    "deployment_created",
    "runtime_hosting_created",
    "public_release_created",
    "operation_permission_created",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "continuation_authorized",
    "publication_flow_opened",
    "reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "follow_on_work_authorized",
)

SELECTED_REFERENCE_FIELDS = (
    "selected_result_id",
    "selected_result_path",
    "selected_result_outcome",
    "selected_result_failed_check_count",
    "selected_result_passed_check_count",
    "selected_result_summary",
    "selected_result_non_claims",
    "selected_result_basis_reference",
    "selected_result_artifact_family",
    "selected_result_artifact_size_class",
)

SELECTED_REFERENCE_REQUEST_FIELDS = (
    "selected_command_implementation_boundary_reference",
    "selected_command_boundary_reference",
    "selected_artifact_emission_containment_reference",
    "selected_evidence_manifest_reference",
    "selected_portable_verification_reference",
)

TOP_LEVEL_SECTIONS = {
    "portable_source_body_verification_command_report_metadata",
    "declared_command_report_question",
    "selected_command_implementation_boundary_reference",
    "selected_command_boundary_reference",
    "selected_artifact_emission_containment_reference",
    "selected_evidence_manifest_reference",
    "selected_portable_verification_reference",
    "declared_evidence_references",
    "reference_shape_checks",
    "non_claim_checks",
    "checker_findings",
    "bounded_report_statement",
    "report_non_meaning",
    "what_remains_open",
    "non_claims",
    "status",
    "block",
    "portable_source_body_verification_command_summary",
}

QUESTION = (
    "Can the bounded checker-only portable verification command report be "
    "built from declared reference-shaped evidence without command execution?"
)


def required_false_non_claims() -> dict[str, bool]:
    return {name: False for name in REQUIRED_NON_CLAIMS}


def make_reference(
    result_id: str,
    outcome: str,
    family: str,
    *,
    passed: int = 41,
    failed: int = 0,
    extra: dict | None = None,
) -> dict:
    reference = {
        "selected_result_id": result_id,
        "selected_result_path": f"artifacts/{family}/{result_id}.json",
        "selected_result_outcome": outcome,
        "selected_result_failed_check_count": failed,
        "selected_result_passed_check_count": passed,
        "selected_result_summary": {
            "selected_result_summary_declared": True,
            "bounded_summary_only": True,
            "summary_is_not_source": True,
        },
        "selected_result_non_claims": {
            "command_implemented": False,
            "command_executed": False,
            "command_authorized_to_run": False,
            "command_invocation_created": False,
            "command_output_created": False,
            "command_result_created": False,
            "command_success_created": False,
            "command_output_became_source": False,
            "command_output_became_authority": False,
            "command_success_created_currentness": False,
            "command_success_claimed_final_completion": False,
            "deployment_created": False,
            "runtime_hosting_created": False,
            "public_release_created": False,
            "final_completion_claimed": False,
            "continuation_authorized": False,
            "follow_on_work_authorized": False,
        },
        "selected_result_basis_reference": f"{family}:reference-shaped:{result_id}",
        "selected_result_artifact_family": family,
        "selected_result_artifact_size_class": "synthetic-reference-kb",
        "path_is_reference_only": True,
        "artifact_existence_does_not_create_currentness": True,
        "selected_result_artifact_size_class_is_descriptive_only": True,
        "summary_is_not_source": True,
        "selected_non_claims_preserve_anti_collapse_posture": True,
        "full_prior_artifacts_embedded": False,
    }
    if extra:
        reference.update(extra)
    return reference


def declared_evidence_references() -> dict:
    return {
        "declared_evidence_references_present": True,
        "references_are_reference_shaped": True,
        "required_source_surface_references": [
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
            "reference/IAMMAI/RANKED_SURFACE_INDEX.md",
        ],
        "required_spec_surface_references": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_V0_MIN_SPEC.md",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_V0_MIN_SPEC.md",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_V0_MIN_SPEC.md",
        ],
        "required_resolver_surface_references": [
            "src/portable_source_body_verification_command.py",
            "src/resolve_portable_source_body_verification_command_implementation_boundary.py",
        ],
        "required_test_surface_references": [
            "tests/test_portable_source_body_verification_command.py",
            "tests/test_resolve_portable_source_body_verification_command_implementation_boundary.py",
        ],
        "required_artifact_root_references": [
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_command_implementation_boundary/",
            "artifacts/integrity_host_v0_min_coexistence_artifact_emission_containment_boundary/",
        ],
        "evidence_references_are_evidence_only": True,
        "paths_do_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
        "summaries_do_not_become_source": True,
        "full_prior_artifacts_embedded": False,
    }


def execution_non_authorization_posture() -> dict:
    return {
        "execution_non_authorization_posture_declared": True,
        "command_execution_not_authorized": True,
        "command_invocation_not_created": True,
        "command_authorized_to_run": False,
        "command_output_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "execution_requires_separate_boundary": True,
        "report_building_is_not_live_command_execution": True,
    }


def make_valid_request(extra: dict | None = None) -> dict:
    request = {
        "command_report_request_id": "portable_verification_command_report_reference_review_001",
        "command_report_question": QUESTION,
        "selected_command_implementation_boundary_reference": make_reference(
            "command_implementation_boundary_reference_review_001",
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_RECORDED",
            "portable_source_body_verification_command_implementation_boundary",
            passed=55,
        ),
        "selected_command_boundary_reference": make_reference(
            "command_boundary_reference_review_001_contained",
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_RECORDED",
            "portable_source_body_verification_command_boundary",
            passed=52,
        ),
        "selected_artifact_emission_containment_reference": make_reference(
            "artifact_emission_containment_reference_review_001",
            "ARTIFACT_EMISSION_CONTAINMENT_RECORDED",
            "artifact_emission_containment_boundary",
            passed=38,
        ),
        "selected_evidence_manifest_reference": make_reference(
            "evidence_manifest_reference_review_001",
            "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_RECORDED",
            "portable_source_body_verification_evidence_manifest_boundary",
            passed=47,
        ),
        "selected_portable_verification_reference": make_reference(
            "portable_verification_reference_review_001",
            "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
            "portable_source_body_verification_boundary",
            passed=44,
        ),
        "declared_evidence_references": declared_evidence_references(),
        "execution_non_authorization_posture": execution_non_authorization_posture(),
        "declared_non_claims": required_false_non_claims(),
    }
    if extra:
        request.update(extra)
    return request


def all_checks(report: dict) -> list[dict]:
    return list(report["reference_shape_checks"]) + list(report["non_claim_checks"])


def failed_codes(report: dict) -> set[str]:
    codes: set[str] = set()
    block = report.get("block", {})
    if block.get("block_code"):
        codes.add(block["block_code"])
    for check in all_checks(report):
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if code:
                codes.add(code)
    return codes


class PortableSourceBodyVerificationCommandReportTests(unittest.TestCase):
    def assertRequiredNonClaimsFalse(self, report: dict) -> None:
        non_claims = report["non_claims"]
        for name in REQUIRED_NON_CLAIMS:
            self.assertIn(name, non_claims)
            self.assertIs(non_claims[name], False, name)

    def assertCheckRecordsWellFormed(self, checks: list[dict]) -> None:
        self.assertGreater(len(checks), 0)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue(
                "block_code" in check or "failure_code" in check,
                check.get("check_name"),
            )

    def test_successful_report_built(self) -> None:
        request = make_valid_request()
        report = build_portable_verification_command_report(request)

        self.assertIsInstance(report, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(report))
        self.assertEqual(report["status"], BUILT)
        self.assertIn(report["status"], STATUS_FAMILY)
        self.assertIsNone(report["block"]["block_code"])
        self.assertIsNone(report["block"]["block_reason"])
        self.assertEqual(report["checker_findings"]["failed_check_count"], 0)
        self.assertGreater(report["checker_findings"]["passed_check_count"], 0)

        statement = report["bounded_report_statement"]
        self.assertIs(statement["portable_verification_command_report_built"], True)
        self.assertIs(statement["checker_findings_built"], True)
        self.assertIs(statement["reference_shape_checks_passed"], True)
        self.assertIs(statement["non_claim_checks_passed"], True)
        self.assertIs(statement["report_is_non_authoritative"], True)
        self.assertIs(statement["command_execution_not_authorized"], True)
        self.assertIs(statement["command_success_not_created"], True)
        self.assertIs(statement["report_building_is_not_live_command_execution"], True)
        self.assertIs(statement["report_building_is_not_command_invocation"], True)
        self.assertIs(statement["report_building_is_not_command_output_from_a_run"], True)
        self.assertIs(statement["report_status_is_not_command_success"], True)
        self.assertIs(statement["command_executed"], False)
        self.assertIs(statement["command_output_created"], False)
        self.assertIs(statement["command_result_created"], False)
        self.assertIs(statement["command_success_created"], False)
        self.assertIs(statement["final_completion_claimed"], False)
        self.assertRequiredNonClaimsFalse(report)

    def test_metadata_and_declared_question(self) -> None:
        report = build_portable_verification_command_report(make_valid_request())
        metadata = report["portable_source_body_verification_command_report_metadata"]
        for name in (
            "portable_source_body_verification_command_report_id",
            "portable_source_body_verification_command_report_type",
            "portable_source_body_verification_command_report_version",
            "generated_at",
            "module",
        ):
            self.assertTrue(metadata.get(name), name)
        self.assertEqual(
            metadata["portable_source_body_verification_command_report_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["module"], "portable_source_body_verification_command")

        declared = report["declared_command_report_question"]
        self.assertEqual(
            declared["command_report_request_id"],
            "portable_verification_command_report_reference_review_001",
        )
        self.assertEqual(declared["command_report_question"], QUESTION)
        self.assertIs(declared["command_report_question_declared"], True)
        self.assertIs(
            report["bounded_report_statement"][
                "report_building_is_not_live_command_execution"
            ],
            True,
        )
        self.assertIs(
            report["bounded_report_statement"]["report_status_is_not_command_success"],
            True,
        )

    def test_reference_shape_checks_and_selected_references(self) -> None:
        report = build_portable_verification_command_report(make_valid_request())
        self.assertCheckRecordsWellFormed(report["reference_shape_checks"])
        self.assertTrue(all(check["passed"] for check in report["reference_shape_checks"]))

        for section in SELECTED_REFERENCE_REQUEST_FIELDS:
            reference = report[section]
            for field in SELECTED_REFERENCE_FIELDS:
                self.assertIn(field, reference, section)
            self.assertIs(reference["path_is_reference_only"], True)
            self.assertIs(
                reference["artifact_existence_does_not_create_currentness"], True
            )
            self.assertIs(
                reference[
                    "selected_result_artifact_size_class_is_descriptive_only"
                ],
                True,
            )
            self.assertIs(reference["summary_is_not_source"], True)
            self.assertIs(
                reference["selected_non_claims_preserve_anti_collapse_posture"],
                True,
            )
            self.assertIs(reference["full_prior_artifacts_embedded"], False)

        codes = failed_codes(report)
        self.assertNotIn("FULL_PRIOR_ARTIFACT_BODY_EMBEDDED", codes)
        self.assertNotIn("PATH_TREATED_AS_CURRENTNESS", codes)
        self.assertNotIn("ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS", codes)

    def test_non_claim_checks(self) -> None:
        report = build_portable_verification_command_report(make_valid_request())
        self.assertCheckRecordsWellFormed(report["non_claim_checks"])
        self.assertTrue(all(check["passed"] for check in report["non_claim_checks"]))

        missing_request = make_valid_request()
        del missing_request["declared_non_claims"]["command_output_created"]
        missing_report = build_portable_verification_command_report(missing_request)
        self.assertNotEqual(missing_report["status"], BUILT)
        self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", failed_codes(missing_report))

        flipped_request = make_valid_request()
        flipped_request["declared_non_claims"]["command_success_created"] = True
        flipped_report = build_portable_verification_command_report(flipped_request)
        self.assertNotEqual(flipped_report["status"], BUILT)
        self.assertTrue(
            {
                "NON_CLAIM_MISSING_OR_FLIPPED",
                "COMMAND_SUCCESS_CREATED",
            }
            & failed_codes(flipped_report)
        )

    def test_report_non_meaning(self) -> None:
        report = build_portable_verification_command_report(make_valid_request())
        non_meaning = report["report_non_meaning"]
        expected = (
            "command_executed",
            "command_invoked",
            "command_output_created",
            "command_result_created",
            "command_success_created",
            "command_output_became_source",
            "command_output_became_authority",
            "command_success_created_currentness",
            "command_success_claimed_final_completion",
            "report_became_source",
            "report_became_authority",
            "report_created_currentness",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "continuation_authorized",
            "follow_on_work_authorized",
        )
        for name in expected:
            self.assertIs(
                non_meaning[f"report_built_does_not_mean_{name}"],
                True,
                name,
            )

    def test_what_remains_open(self) -> None:
        report = build_portable_verification_command_report(make_valid_request())
        remains_open = report["what_remains_open"]
        open_items = set(remains_open["open_items"])
        for item in (
            "command execution boundary",
            "command invocation",
            "command output from live execution",
            "command result from live execution",
            "command success",
            "manifest implementation",
            "checksum implementation",
            "signature implementation",
            "source-body packet implementation",
            "reproducible environment declaration",
            "runtime hosting",
            "deployment",
            "public release",
            "source transfer",
            "source migration",
            "source receipt",
            "reception authorization",
            "derivative reception",
            "vessel relation",
            "operation permission",
            "public readiness",
            "final completion",
            "continuation",
            "publication flow",
            "reusable permission",
            "successor reception request",
            "follow-on work",
        ):
            self.assertIn(item, open_items)
        self.assertIs(remains_open["open_means_not_scheduled"], True)
        self.assertIs(remains_open["open_means_not_authorized"], True)
        self.assertIs(remains_open["open_means_not_executed"], True)

    def test_summary_helper(self) -> None:
        report = build_portable_verification_command_report(make_valid_request())
        summary = build_portable_verification_command_summary(report)

        self.assertEqual(summary["status"], BUILT)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["command_report_request_id"],
            "portable_verification_command_report_reference_review_001",
        )
        self.assertEqual(summary["command_report_question"], QUESTION)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIs(summary["report_built"], True)
        self.assertIs(summary["checker_findings_built"], True)
        self.assertIs(summary["reference_shape_checks_passed"], True)
        self.assertIs(summary["non_claim_checks_passed"], True)
        self.assertIs(summary["report_non_authoritative"], True)
        self.assertIs(summary["command_execution_not_authorized"], True)
        self.assertIs(summary["command_invocation_not_created"], True)
        self.assertIs(summary["command_output_not_created"], True)
        self.assertIs(summary["command_result_not_created"], True)
        self.assertIs(summary["command_success_not_created"], True)
        self.assertIs(summary["no_full_prior_artifacts_embedded"], True)
        self.assertIs(summary["no_artifact_mutation"], True)
        self.assertIs(summary["no_deployment_runtime_public_release"], True)
        self.assertIs(
            summary["no_operation_permission_public_readiness_final_completion"],
            True,
        )
        self.assertIs(
            summary["no_continuation_publication_flow_reusable_permission"], True
        )
        self.assertIs(
            summary[
                "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work"
            ],
            True,
        )
        for name in REQUIRED_NON_CLAIMS:
            self.assertIn(name, summary["key_non_claims"])
            self.assertIs(summary["key_non_claims"][name], False)

    def test_write_behavior(self) -> None:
        report = build_portable_verification_command_report(make_valid_request())
        report_before = copy.deepcopy(report)
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "nested" / "report-root"
            written = write_portable_verification_command_report(report, output_dir)
            self.assertTrue(written.exists())
            self.assertTrue(written.parent.exists())
            self.assertIn(
                "portable_verification_command_report_reference_review_001__"
                "portable_source_body_verification_command_report.json",
                written.name,
            )

            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))
            self.assertEqual(parsed["status"], BUILT)
            self.assertIs(
                parsed["bounded_report_statement"]["command_execution_not_authorized"],
                True,
            )
            self.assertIs(parsed["non_claims"]["command_executed"], False)
            self.assertEqual(report, report_before)

    def test_default_output_root_and_non_overwrite(self) -> None:
        report = build_portable_verification_command_report(make_valid_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir) / "bounded-command-report-root"
            with patch.object(
                command,
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_REPORT_ROOT",
                temp_root,
            ):
                first = write_portable_verification_command_report(report)
                second = write_portable_verification_command_report(report)

        self.assertEqual(first.parent, temp_root)
        self.assertEqual(second.parent, temp_root)
        self.assertNotEqual(first, second)
        self.assertTrue(second.name.endswith("_001.json"))
        root_text = str(first.parent)
        self.assertIn("command-report-root", root_text)
        for forbidden in (
            "command_execution",
            "deployment",
            "runtime",
            "public_release",
            "manifest_boundary",
            "checksum",
            "packet",
        ):
            self.assertNotIn(forbidden, root_text)

    def test_non_mutation_posture(self) -> None:
        request = make_valid_request()
        original = copy.deepcopy(request)
        selected_originals = {
            key: copy.deepcopy(request[key]) for key in SELECTED_REFERENCE_REQUEST_FIELDS
        }
        evidence_original = copy.deepcopy(request["declared_evidence_references"])

        first = build_portable_verification_command_report(request)
        second = build_portable_verification_command_report(request)

        self.assertEqual(request, original)
        for key, value in selected_originals.items():
            self.assertEqual(request[key], value)
        self.assertEqual(request["declared_evidence_references"], evidence_original)
        self.assertEqual(first["status"], BUILT)
        self.assertEqual(second["status"], BUILT)

        with tempfile.TemporaryDirectory() as temp_dir:
            report_before = copy.deepcopy(first)
            written = write_portable_verification_command_report(
                first, Path(temp_dir) / "additive"
            )
            self.assertTrue(written.exists())
            self.assertEqual(first, report_before)

    def test_missing_or_malformed_request(self) -> None:
        for malformed in (None, "not a mapping"):
            report = build_portable_verification_command_report(malformed)  # type: ignore[arg-type]
            self.assertIsInstance(report, dict)
            self.assertEqual(report["status"], BLOCKED)
            self.assertEqual(report["block"]["block_code"], "COMMAND_REPORT_REQUEST_MALFORMED")

    def test_missing_required_fields(self) -> None:
        cases = (
            ("command_report_question", "COMMAND_REPORT_QUESTION_UNDECLARED"),
            (
                "selected_command_implementation_boundary_reference",
                "COMMAND_IMPLEMENTATION_BOUNDARY_REFERENCE_MISSING",
            ),
            ("selected_command_boundary_reference", "COMMAND_BOUNDARY_REFERENCE_MISSING"),
            (
                "selected_artifact_emission_containment_reference",
                "ARTIFACT_EMISSION_CONTAINMENT_REFERENCE_MISSING",
            ),
            ("selected_evidence_manifest_reference", "EVIDENCE_MANIFEST_REFERENCE_MISSING"),
            ("selected_portable_verification_reference", "PORTABLE_VERIFICATION_REFERENCE_MISSING"),
            ("declared_evidence_references", "DECLARED_EVIDENCE_REFERENCES_MISSING"),
            (
                "execution_non_authorization_posture",
                "EXECUTION_NON_AUTHORIZATION_POSTURE_MISSING",
            ),
        )
        for field, expected_code in cases:
            with self.subTest(field=field):
                request = make_valid_request()
                del request[field]
                report = build_portable_verification_command_report(request)
                self.assertEqual(report["status"], BLOCKED)
                self.assertEqual(report["block"]["block_code"], expected_code)

    def test_reference_shape_missing_required_field(self) -> None:
        request = make_valid_request()
        del request["selected_command_boundary_reference"]["selected_result_summary"]
        report = build_portable_verification_command_report(request)

        self.assertNotEqual(report["status"], BUILT)
        self.assertIn("REFERENCE_SHAPE_MISSING_REQUIRED_FIELD", failed_codes(report))

    def test_failed_check_count_nonzero(self) -> None:
        request = make_valid_request()
        request["selected_portable_verification_reference"][
            "selected_result_failed_check_count"
        ] = 2
        report = build_portable_verification_command_report(request)

        self.assertNotEqual(report["status"], BUILT)
        self.assertIn(report["status"], {NOT_BUILT, REQUIRES_ADDITIONAL_BASIS, BLOCKED})
        failed = [
            check
            for check in report["reference_shape_checks"]
            if check["check_name"] == "failed check counts are zero where required"
        ]
        self.assertEqual(len(failed), 1)
        self.assertIs(failed[0]["passed"], False)
        self.assertEqual(failed[0]["failure_code"], "REQUIRED_FAILED_CHECK_COUNT_NONZERO")

    def test_full_prior_artifact_body_embedded_blocks_and_is_omitted(self) -> None:
        sentinel = "FULL_PRIOR_ARTIFACT_SENTINEL_" + ("x" * 20000)
        request = make_valid_request()
        request["selected_evidence_manifest_reference"]["full_artifact_body"] = sentinel

        report = build_portable_verification_command_report(request)
        serialized = json.dumps(report)

        self.assertNotEqual(report["status"], BUILT)
        self.assertIn("FULL_PRIOR_ARTIFACT_BODY_EMBEDDED", failed_codes(report))
        self.assertNotIn(sentinel, serialized)
        self.assertIn(
            "full_artifact_body",
            report["selected_evidence_manifest_reference"][
                "omitted_full_artifact_body_keys"
            ],
        )
        self.assertIs(
            report["selected_evidence_manifest_reference"][
                "full_artifact_body_not_embedded"
            ],
            True,
        )
        self.assertIs(report["non_claims"]["prior_artifacts_mutated"], False)

    def test_collapse_flags_block(self) -> None:
        cases = (
            ("command_execution_authorized", "COMMAND_EXECUTION_AUTHORIZED"),
            ("command_invocation_exists", "COMMAND_INVOCATION_CREATED"),
            ("command_output_exists", "COMMAND_OUTPUT_CREATED"),
            ("command_result_exists", "COMMAND_RESULT_CREATED"),
            ("command_success_exists", "COMMAND_SUCCESS_CREATED"),
            ("command_output_treated_as_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
            ("report_treated_as_authority", "REPORT_TREATED_AS_AUTHORITY"),
            (
                "command_success_treated_as_currentness",
                "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            ),
            (
                "command_success_treated_as_final_completion",
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            ),
            ("deployment_created", "DEPLOYMENT_CREATED"),
            ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
            ("public_release_created", "PUBLIC_RELEASE_CREATED"),
            ("publication_flow_opened", "CONTINUATION_AUTHORIZED"),
            ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        )
        for flag, expected_code in cases:
            with self.subTest(flag=flag):
                request = make_valid_request({flag: True})
                report = build_portable_verification_command_report(request)
                self.assertEqual(report["status"], BLOCKED)
                self.assertIn(expected_code, failed_codes(report))
                self.assertIs(report["non_claims"]["command_executed"], False)
                self.assertIs(report["non_claims"]["command_output_created"], False)
                self.assertIs(report["non_claims"]["command_success_created"], False)
                self.assertIs(report["non_claims"]["final_completion_claimed"], False)

    def test_requested_status_behavior(self) -> None:
        for requested in (REQUIRES_ADDITIONAL_BASIS, NOT_BUILT):
            with self.subTest(requested=requested):
                report = build_portable_verification_command_report(
                    make_valid_request({"requested_command_report_status": requested})
                )
                self.assertEqual(report["status"], requested)
                self.assertIsNone(report["block"]["block_code"])
                self.assertIs(report["non_claims"]["command_executed"], False)
                self.assertIs(report["non_claims"]["command_output_created"], False)
                self.assertIs(report["non_claims"]["command_result_created"], False)
                self.assertIs(report["non_claims"]["command_success_created"], False)
                self.assertIs(report["non_claims"]["final_completion_claimed"], False)
                self.assertIs(report["non_claims"]["follow_on_work_authorized"], False)

    def test_source_inspection_has_no_obvious_execution_or_network_calls(self) -> None:
        source = (SRC_ROOT / "portable_source_body_verification_command.py").read_text(
            encoding="utf-8"
        )
        forbidden_patterns = (
            r"(^|\n)\s*import\s+subprocess\b",
            r"(^|\n)\s*from\s+subprocess\s+import\b",
            r"\bsubprocess\.",
            r"(^|\n)\s*import\s+requests\b",
            r"(^|\n)\s*from\s+requests\s+import\b",
            r"(^|\n)\s*import\s+urllib\b",
            r"(^|\n)\s*from\s+urllib\s+import\b",
            r"(^|\n)\s*import\s+http\.client\b",
            r"(^|\n)\s*from\s+http\.client\s+import\b",
            r"(^|\n)\s*import\s+socket\b",
            r"(^|\n)\s*from\s+socket\s+import\b",
            r"(^|\n)\s*import\s+openai\b",
            r"(^|\n)\s*from\s+openai\s+import\b",
            r"\bos\.system\s*\(",
            r"\bPopen\s*\(",
            r"\bcheck_call\s*\(",
            r"\bcheck_output\s*\(",
        )
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, source), pattern)
        self.assertNotIn('if __name__ == "__main__"', source)


if __name__ == "__main__":
    unittest.main()
