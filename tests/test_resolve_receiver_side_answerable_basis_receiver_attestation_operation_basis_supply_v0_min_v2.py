"""Current-state successor tests for receiver-attestation basis supply.

The preserved v1 suite first passed 45/45 before the canonical live artifact
existed. Its current post-live posture is 42/45 because three tests retain the
then-correct output-root-absence assertion. This additive suite inherits all
45 behaviors, replaces only those three phase-specific assertions, and adds
live-artifact custody checks. It does not edit or expected-fail the v1 suite.
"""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from types import ModuleType
from typing import Any
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

V1_TEST_PATH = REPOSITORY_ROOT / (
    "tests/test_resolve_receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_supply_v0_min.py"
)
V2_TEST_PATH = Path(__file__).resolve()
RESOLVER_PATH = REPOSITORY_ROOT / (
    "src/resolve_receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_supply_v0_min.py"
)
SPECIFICATION_PATH = REPOSITORY_ROOT / (
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_SUPPLY_V0_MIN_SPEC.md"
)
TERMINAL_SUMMARY_PATH = REPOSITORY_ROOT / (
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_SUPPLY_V0_MIN_TERMINAL_SUMMARY.md"
)
LIVE_ARTIFACT_PATH = REPOSITORY_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_supply_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "supply_001__receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_supply_v0_min_result.json"
)
EXPECTED_LIVE_ARTIFACT_SHA256 = (
    "9d877d5ce48ec6aa484e649bc54928d692eed62feefe8383169d37f462228325"
)
EXPECTED_DECLARED_BASIS_SHA256 = (
    "8e1bf1eba4e2916078f83ad2afe1f66d8d4c4dfd7b7955674a20b5ed730f2165"
)
WRITER_NAME = (
    "write_receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_supply_v0_min_result"
)


class _DuplicateJsonKeyError(ValueError):
    """Raised when the independent live-artifact loader sees a duplicate."""


def _reject_duplicate_json_keys(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def _reject_non_finite_json(value: str) -> Any:
    raise ValueError(value)


def _strict_json_mapping(path: Path) -> dict[str, Any]:
    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_reject_duplicate_json_keys,
        parse_constant=_reject_non_finite_json,
    )
    if not isinstance(value, dict):
        raise AssertionError(f"strict JSON root is not a mapping: {path}")
    return value


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def _directory_snapshot(root: Path) -> dict[str, tuple[str, str | None]]:
    if not root.is_dir():
        raise AssertionError(f"canonical output root is not a directory: {root}")
    snapshot: dict[str, tuple[str, str | None]] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            snapshot[relative] = ("symlink", os.readlink(path))
        elif path.is_file():
            snapshot[relative] = ("file", _sha256(path))
        elif path.is_dir():
            snapshot[relative] = ("directory", None)
        else:
            snapshot[relative] = ("other", None)
    return snapshot


def _load_v1_module() -> ModuleType:
    module_name = "_preserved_receiver_attestation_basis_supply_v1_tests"
    specification = importlib.util.spec_from_file_location(
        module_name,
        V1_TEST_PATH,
    )
    if specification is None or specification.loader is None:
        raise ImportError(f"cannot load preserved v1 suite: {V1_TEST_PATH}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[module_name] = module
    specification.loader.exec_module(module)
    return module


_V1_MODULE = _load_v1_module()
resolver = _V1_MODULE.resolver
_V1_TEST_CLASS = _V1_MODULE.ReceiverAttestationOperationBasisSupplyTests

REAL_OUTPUT_ROOT = resolver.OUTPUT_ROOT.resolve()
CANONICAL_LIVE_ARTIFACT_PATH = (
    REAL_OUTPUT_ROOT / resolver.OUTPUT_FILENAME
).resolve()


def _require_exact_live_artifact(
    artifact: Mapping[str, Any],
) -> None:
    expected_top_level = {
        "resolver_module": (
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_supply_v0_min"
        ),
        "result_version": "0.1.0",
        "outcome": resolver.OUTCOME_SUPPLIED,
        "failed_check_count": 0,
        "passed_check_count": 101,
    }
    for field, expected in expected_top_level.items():
        if artifact.get(field) != expected:
            raise AssertionError(
                f"live artifact {field} mismatch: {artifact.get(field)!r}"
            )

    state = artifact.get(_V1_MODULE.STATE_KEY)
    if not isinstance(state, Mapping):
        raise AssertionError("live artifact supply state is not a mapping")
    expected_state_values = {
        "supply_result": resolver.SUPPLY_RESULT_SUPPLIED,
        "decision_code": "BASIS_SUPPLIED",
        "decision_reason": "exact declared basis supplied",
        "basis_supply_selected": True,
        "supply_recorded": True,
        "supply_result_recorded": True,
        "supply_exhausted": True,
        "supply_basis_received": True,
        "receiver_attestation_operation_basis_declared": True,
        "receiver_attestation_operation_basis_supplied": True,
        "receiver_attestation_operation_basis_admitted": False,
        "receiver_attestation_operation_executed": False,
        "receiver_attestation_operation_result_recorded": False,
        "receiver_attestation_recorded": False,
        "receiver_answerable_receipt_present": False,
        "presence_supported": False,
        "presence_authorized": False,
        "presence_established": False,
        "standing_created": False,
        "follow_on_work_authorized": False,
        "declared_basis_digest_algorithm": "SHA-256",
        "declared_basis_sha256": EXPECTED_DECLARED_BASIS_SHA256,
        "declared_basis_digest_correspondence_validated": True,
        "exact_21_field_declared_basis_validated": True,
        "result_level_non_claims_canonical_false": True,
        "complete_material_omitted": True,
    }
    for field, expected in expected_state_values.items():
        if state.get(field) != expected or type(state.get(field)) is not type(
            expected
        ):
            raise AssertionError(
                f"live artifact state {field} mismatch: {state.get(field)!r}"
            )

    decision = artifact.get("supply_decision")
    if not isinstance(decision, Mapping):
        raise AssertionError("live artifact supply decision is not a mapping")
    if decision.get("code") != "BASIS_SUPPLIED":
        raise AssertionError("live artifact decision code mismatch")
    if decision.get("reason") != "exact declared basis supplied":
        raise AssertionError("live artifact decision reason mismatch")

    digest = artifact.get("declared_basis_digest")
    if not isinstance(digest, Mapping):
        raise AssertionError("live artifact digest is not a mapping")
    expected_digest = {
        "declared_basis_digest_algorithm": "SHA-256",
        "declared_basis_sha256": EXPECTED_DECLARED_BASIS_SHA256,
        "declared_basis_digest_correspondence_validated": True,
    }
    for field, expected in expected_digest.items():
        if digest.get(field) != expected:
            raise AssertionError(f"live artifact digest {field} mismatch")

    validation = artifact.get("declared_basis_validation")
    if not isinstance(validation, Mapping):
        raise AssertionError("live artifact basis validation is not a mapping")
    for field in (
        "exact_21_field_declared_basis_validated",
        "declared_basis_posture_maps_validated",
        "non_conversion_statement_validated",
        "basis_non_claims_validated",
    ):
        if validation.get(field) is not True:
            raise AssertionError(f"live artifact validation {field} is not true")

    summary = artifact.get(_V1_MODULE.SUMMARY_KEY)
    if not isinstance(summary, Mapping):
        raise AssertionError("live artifact summary is not a mapping")
    for field in (
        "specification_markers_validated",
        "declaration_artifact_validated",
        "exact_21_field_declared_basis_validated",
        "declared_basis_posture_maps_validated",
        "non_conversion_statement_validated",
        "basis_non_claims_validated",
        "result_level_non_claims_canonical_false",
        "complete_material_omitted",
        "stale_open_list_entries_disclosed",
        "stale_open_list_entries_preserved",
        "stale_open_list_entries_not_used_as_sole_block",
    ):
        if summary.get(field) is not True:
            raise AssertionError(f"live artifact summary {field} is not true")

    non_claims = artifact.get("non_claims")
    if not isinstance(non_claims, Mapping):
        raise AssertionError("live artifact non-claims are not a mapping")
    if set(non_claims) != set(resolver.REQUIRED_FALSE_NON_CLAIMS):
        raise AssertionError("live artifact non-claim key family mismatch")
    if any(type(value) is not bool or value for value in non_claims.values()):
        raise AssertionError("live artifact non-claims are not canonical false")

    basis = artifact.get(resolver.SUPPLIED_BASIS_SECTION)
    if not isinstance(basis, Mapping):
        raise AssertionError("live artifact supplied basis is not a mapping")
    if len(basis) != 21 or set(basis) != set(resolver.CANDIDATE_FIELDS):
        raise AssertionError("live artifact supplied basis is not exact 21-field")


class ReceiverAttestationOperationBasisSupplyV2Tests(_V1_TEST_CLASS):
    """Preserve v1 behavior while validating the lawful post-live state."""

    @classmethod
    def setUpClass(cls) -> None:
        required_paths = [
            V1_TEST_PATH,
            RESOLVER_PATH,
            SPECIFICATION_PATH,
            LIVE_ARTIFACT_PATH,
            TERMINAL_SUMMARY_PATH,
        ]
        required_paths.extend(
            REPOSITORY_ROOT / relative
            for relative in _V1_MODULE.PRESERVED_RELATIVE_PATHS
        )
        cls._preserved_paths = tuple(dict.fromkeys(required_paths))
        for path in cls._preserved_paths:
            if not path.is_file():
                raise AssertionError(f"required preserved input missing: {path}")
        cls._preserved_hashes_v2 = {
            path: _sha256(path) for path in cls._preserved_paths
        }

        if resolver.OUTPUT_ROOT.resolve() != REAL_OUTPUT_ROOT:
            raise AssertionError("resolver real output root changed before v2")
        if not REAL_OUTPUT_ROOT.is_dir():
            raise AssertionError("canonical supply output root is missing")
        if LIVE_ARTIFACT_PATH.resolve() != CANONICAL_LIVE_ARTIFACT_PATH:
            raise AssertionError("canonical live artifact path mismatch")
        if not CANONICAL_LIVE_ARTIFACT_PATH.is_file():
            raise AssertionError("canonical live supply artifact is missing")

        cls._output_snapshot_v2 = _directory_snapshot(REAL_OUTPUT_ROOT)
        expected_snapshot = {
            resolver.OUTPUT_FILENAME: (
                "file",
                EXPECTED_LIVE_ARTIFACT_SHA256,
            )
        }
        if cls._output_snapshot_v2 != expected_snapshot:
            raise AssertionError(
                "canonical output root contains unexpected or altered entries"
            )
        cls._live_artifact_v2 = _strict_json_mapping(LIVE_ARTIFACT_PATH)
        _require_exact_live_artifact(cls._live_artifact_v2)
        if _sha256(LIVE_ARTIFACT_PATH) != EXPECTED_LIVE_ARTIFACT_SHA256:
            raise AssertionError("canonical live artifact SHA-256 mismatch")

        cls._writer_targets_v2: list[Path] = []
        original_writer = getattr(resolver, WRITER_NAME)

        def guarded_writer(
            result: Mapping[str, Any],
            output_path: Path | str | None = None,
        ) -> Path:
            target = (
                resolver.OUTPUT_ROOT / resolver.OUTPUT_FILENAME
                if output_path is None
                else Path(output_path)
            ).resolve()
            cls._writer_targets_v2.append(target)
            if _path_within(target, REAL_OUTPUT_ROOT):
                raise AssertionError(
                    f"v2 writer attempted canonical repository output: {target}"
                )
            return original_writer(result, output_path)

        cls._writer_guard_patch_v2 = patch.object(
            resolver,
            WRITER_NAME,
            guarded_writer,
        )
        cls._writer_guard_patch_v2.start()

    @classmethod
    def tearDownClass(cls) -> None:
        try:
            if resolver.OUTPUT_ROOT.resolve() != REAL_OUTPUT_ROOT:
                raise AssertionError("resolver OUTPUT_ROOT patch leaked")
            current_hashes = {
                path: _sha256(path) for path in cls._preserved_paths
            }
            if current_hashes != cls._preserved_hashes_v2:
                raise AssertionError("preserved supply lineage changed")
            if _directory_snapshot(REAL_OUTPUT_ROOT) != cls._output_snapshot_v2:
                raise AssertionError("canonical supply output directory changed")
            if any(
                _path_within(path, REAL_OUTPUT_ROOT)
                for path in cls._writer_targets_v2
            ):
                raise AssertionError("real repository output root was targeted")
        finally:
            cls._writer_guard_patch_v2.stop()

    def load_live_artifact(self) -> dict[str, Any]:
        artifact = _strict_json_mapping(LIVE_ARTIFACT_PATH)
        _require_exact_live_artifact(artifact)
        return copy.deepcopy(artifact)

    def assert_canonical_output_unchanged(self) -> None:
        self.assertTrue(REAL_OUTPUT_ROOT.is_dir())
        self.assertTrue(CANONICAL_LIVE_ARTIFACT_PATH.is_file())
        self.assertEqual(
            _directory_snapshot(REAL_OUTPUT_ROOT),
            type(self)._output_snapshot_v2,
        )
        self.assertEqual(
            _sha256(LIVE_ARTIFACT_PATH),
            EXPECTED_LIVE_ARTIFACT_SHA256,
        )

    def test_01_public_api_and_constant_contract(self) -> None:
        temporary_absent_root = self.root / "v1_pre_live_absence_posture"
        with patch.object(resolver, "OUTPUT_ROOT", temporary_absent_root):
            super().test_01_public_api_and_constant_contract()
        self.assertEqual(resolver.OUTPUT_ROOT.resolve(), REAL_OUTPUT_ROOT)
        self.assertTrue(resolver.OUTPUT_ROOT.exists())
        self.assertTrue(resolver.OUTPUT_ROOT.is_dir())
        self.assertTrue(CANONICAL_LIVE_ARTIFACT_PATH.is_file())
        _require_exact_live_artifact(self.load_live_artifact())
        self.assert_canonical_output_unchanged()

    def test_36_writer_writes_every_valid_branch_exactly(self) -> None:
        before = _directory_snapshot(REAL_OUTPUT_ROOT)
        temporary_absent_root = self.root / "v1_writer_absence_posture"
        with patch.object(resolver, "OUTPUT_ROOT", temporary_absent_root):
            super().test_36_writer_writes_every_valid_branch_exactly()
        self.assertEqual(resolver.OUTPUT_ROOT.resolve(), REAL_OUTPUT_ROOT)
        self.assertEqual(_directory_snapshot(REAL_OUTPUT_ROOT), before)
        self.assert_canonical_output_unchanged()

    def test_44_preserved_inputs_and_no_repository_artifact_stay_unchanged(
        self,
    ) -> None:
        before_hashes = {
            path: _sha256(path) for path in type(self)._preserved_paths
        }
        before_output = _directory_snapshot(REAL_OUTPUT_ROOT)
        writer_calls_before = len(type(self)._writer_targets_v2)
        temporary_absent_root = self.root / "v1_resolution_absence_posture"
        with patch.object(resolver, "OUTPUT_ROOT", temporary_absent_root):
            super().test_44_preserved_inputs_and_no_repository_artifact_stay_unchanged()
        self.assertEqual(
            len(type(self)._writer_targets_v2),
            writer_calls_before,
            "resolution unexpectedly called the writer",
        )
        self.assertEqual(resolver.OUTPUT_ROOT.resolve(), REAL_OUTPUT_ROOT)
        self.assertEqual(
            {_path: _sha256(_path) for _path in type(self)._preserved_paths},
            before_hashes,
        )
        self.assertEqual(_directory_snapshot(REAL_OUTPUT_ROOT), before_output)
        self.assert_canonical_output_unchanged()

    def test_46_v1_historical_output_root_assertions_are_preserved(
        self,
    ) -> None:
        source = V1_TEST_PATH.read_text(encoding="utf-8")
        exact_source = (
            "self.assertFalse(resolver.OUTPUT_ROOT.exists())"
        )
        self.assertEqual(source.count(exact_source), 3)
        tree = ast.parse(source, filename=str(V1_TEST_PATH))
        observed: dict[str, list[int]] = {}
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            lines: list[int] = []
            for nested in ast.walk(node):
                if (
                    isinstance(nested, ast.Call)
                    and isinstance(nested.func, ast.Attribute)
                    and nested.func.attr == "assertFalse"
                    and len(nested.args) == 1
                    and ast.unparse(nested.args[0])
                    == "resolver.OUTPUT_ROOT.exists()"
                ):
                    lines.append(nested.lineno)
            if lines:
                observed[node.name] = lines
        self.assertEqual(
            set(observed),
            {
                "test_01_public_api_and_constant_contract",
                "test_36_writer_writes_every_valid_branch_exactly",
                "test_44_preserved_inputs_and_no_repository_artifact_stay_unchanged",
            },
        )
        self.assertTrue(all(len(lines) == 1 for lines in observed.values()))
        self.assertEqual(
            _sha256(V1_TEST_PATH),
            type(self)._preserved_hashes_v2[V1_TEST_PATH],
        )
        self.assertTrue(CANONICAL_LIVE_ARTIFACT_PATH.is_file())

    def test_47_current_live_artifact_contract_is_exact(self) -> None:
        artifact = self.load_live_artifact()
        self.assertIsInstance(artifact, dict)
        _require_exact_live_artifact(artifact)
        self.assertEqual(
            set(artifact).intersection({resolver.SUPPLIED_BASIS_SECTION}),
            {resolver.SUPPLIED_BASIS_SECTION},
        )
        basis = artifact[resolver.SUPPLIED_BASIS_SECTION]
        self.assertIsInstance(basis, dict)
        self.assertEqual(len(basis), 21)
        self.assertEqual(set(basis), set(resolver.CANDIDATE_FIELDS))
        self.assert_canonical_output_unchanged()

    def test_48_current_resolution_equals_live_artifact_and_basis(
        self,
    ) -> None:
        request = self.canonical_request()
        request_before = copy.deepcopy(request)
        fresh = self.invoke(request)
        self.assertEqual(request, request_before)
        self.assert_supplied(fresh)
        live = self.load_live_artifact()
        self.assertEqual(fresh, live)
        self.assertEqual(
            fresh[resolver.SUPPLIED_BASIS_SECTION],
            live[resolver.SUPPLIED_BASIS_SECTION],
        )
        self.assertEqual(
            fresh[resolver.SUPPLIED_BASIS_SECTION],
            self.declared_basis(),
        )
        self.assert_canonical_output_unchanged()

    def test_49_current_summary_matches_live_compact_standing(self) -> None:
        live = self.load_live_artifact()
        fresh = self.invoke(self.canonical_request())
        built = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_summary(
                fresh
            )
        )
        self.assertEqual(built, live[_V1_MODULE.SUMMARY_KEY])
        self.assertEqual(built, fresh[_V1_MODULE.SUMMARY_KEY])
        self.assertNotIn(resolver.SUPPLIED_BASIS_SECTION, built)
        self.assertEqual(built["passed_check_count"], 101)
        self.assertEqual(built["failed_check_count"], 0)
        self.assertIs(built["operation_basis_supplied"], True)
        self.assertIs(built["operation_basis_admitted"], False)
        self.assertIs(built["operation_executed"], False)
        self.assertIs(built["operation_result_recorded"], False)
        self.assert_canonical_output_unchanged()

    def test_50_canonical_artifact_sha256_is_stable(self) -> None:
        self.assertEqual(
            _sha256(LIVE_ARTIFACT_PATH),
            EXPECTED_LIVE_ARTIFACT_SHA256,
        )
        self.assertEqual(
            _sha256(LIVE_ARTIFACT_PATH),
            type(self)._preserved_hashes_v2[LIVE_ARTIFACT_PATH],
        )
        self.assert_canonical_output_unchanged()

    def test_51_explicit_temporary_writer_works_with_live_root(
        self,
    ) -> None:
        self.assertTrue(REAL_OUTPUT_ROOT.is_dir())
        result = self.invoke(self.canonical_request())
        output = self.root / "explicit_writer" / "supplied.json"
        written = getattr(resolver, WRITER_NAME)(result, output)
        self.assertEqual(written, output)
        self.assertTrue(output.is_file())
        self.assertEqual(_strict_json_mapping(output), result)
        self.assert_canonical_output_unchanged()

    def test_52_patched_output_root_keeps_filename_and_suffix(
        self,
    ) -> None:
        result = self.invoke(self.canonical_request())
        temporary_root = self.root / "patched_output_root"
        with patch.object(resolver, "OUTPUT_ROOT", temporary_root):
            first = getattr(resolver, WRITER_NAME)(result)
            first_bytes = first.read_bytes()
            second = getattr(resolver, WRITER_NAME)(result)
            third = getattr(resolver, WRITER_NAME)(result)
        stem = Path(resolver.OUTPUT_FILENAME).stem
        self.assertEqual(first.name, resolver.OUTPUT_FILENAME)
        self.assertEqual(second.name, f"{stem}_001.json")
        self.assertEqual(third.name, f"{stem}_002.json")
        self.assertEqual(first.read_bytes(), first_bytes)
        self.assertEqual(resolver.OUTPUT_ROOT.resolve(), REAL_OUTPUT_ROOT)
        self.assert_canonical_output_unchanged()

    def test_53_sandbox_exception_cannot_leak_patch_or_state(self) -> None:
        result = self.invoke(self.canonical_request())
        temporary_root = self.root / "exception_sandbox"
        before = _directory_snapshot(REAL_OUTPUT_ROOT)
        with self.assertRaisesRegex(RuntimeError, "intentional sandbox stop"):
            with patch.object(resolver, "OUTPUT_ROOT", temporary_root):
                output = getattr(resolver, WRITER_NAME)(result)
                self.assertTrue(output.is_file())
                raise RuntimeError("intentional sandbox stop")
        self.assertEqual(resolver.OUTPUT_ROOT.resolve(), REAL_OUTPUT_ROOT)
        self.assertEqual(_directory_snapshot(REAL_OUTPUT_ROOT), before)
        self.assert_canonical_output_unchanged()

    def test_54_repeated_resolution_is_deterministic_and_read_only(
        self,
    ) -> None:
        before_hashes = {
            path: _sha256(path) for path in type(self)._preserved_paths
        }
        before_output = _directory_snapshot(REAL_OUTPUT_ROOT)
        first = self.invoke(self.canonical_request())
        second = self.invoke(self.canonical_request())
        self.assertEqual(first, second)
        self.assertEqual(first, self.load_live_artifact())
        self.assertEqual(
            {_path: _sha256(_path) for _path in type(self)._preserved_paths},
            before_hashes,
        )
        self.assertEqual(_directory_snapshot(REAL_OUTPUT_ROOT), before_output)

    def test_55_real_repository_output_root_was_never_targeted(
        self,
    ) -> None:
        result = self.invoke(self.canonical_request())
        output = self.root / "writer_target_probe" / "result.json"
        self.assertEqual(getattr(resolver, WRITER_NAME)(result, output), output)
        self.assertTrue(type(self)._writer_targets_v2)
        for target in type(self)._writer_targets_v2:
            self.assertFalse(
                _path_within(target, REAL_OUTPUT_ROOT),
                f"writer targeted canonical repository output: {target}",
            )
        self.assertEqual(resolver.OUTPUT_ROOT.resolve(), REAL_OUTPUT_ROOT)
        self.assert_canonical_output_unchanged()


# Keep the preserved base class reachable only through the v2 MRO. Unittest
# discovery scans module globals for TestCase classes, so deleting this alias
# prevents duplicate direct collection without mutating the v1 module or file.
del _V1_TEST_CLASS


if __name__ == "__main__":
    unittest.main()
