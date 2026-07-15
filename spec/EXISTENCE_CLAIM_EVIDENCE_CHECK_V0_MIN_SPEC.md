# Existence Claim Evidence Check V0 Minimum Specification

## 1. Purpose

This file defines one future existence-claim evidence check for the present `IAMMAI-SYSTEM` execution line.

This check is downstream of:

- `spec/SEAM_CASE_LAW__CO_AGENCY_AUTHORIZATION_UNSUPPORTED_EXISTENCE_CLAIM_V0.md`
- `spec/EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_V0_MIN_SPEC.md`
- `src/resolve_existence_claim_evidence_requirement_boundary_v0_min.py`
- `tests/test_resolve_existence_claim_evidence_requirement_boundary_v0_min.py`
- `spec/EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_TERMINAL_SUMMARY_V0.md`

This check is the first future mechanical successor specification for the existence-claim evidence requirement line.

This file defines a future check only.

This file does not create resolver, tests, artifact, scan, validation execution, repair, descendant body, derivation, standing, relation, crossing, FIELD machinery, runtime, authority, currentness, output, action, derivative reception, synchronization, or follow-on work.

## 2. Status and Rank

This spec is additive.

This spec is repo-local to `IAMMAI-SYSTEM`.

This spec ranks below constitutional and reference authority surfaces.

This spec ranks below current executable source, existing tests, emitted artifacts, and standing terminal summaries.

This spec is downstream of the negative seam case.

This spec is downstream of the existence-claim evidence requirement boundary spec.

This spec is downstream of the existence-claim evidence requirement boundary resolver/test/live artifact/terminal summary line.

This spec preserves `spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` unchanged as contaminated lineage for the unsupported existence-claim class.

This spec does not repair, edit, delete, overwrite, rename, move, patch, normalize, invalidate, or silently correct the affected file.

This spec does not replace the seam case.

This spec does not replace the evidence-requirement boundary.

This spec does not replace the evidence-requirement boundary terminal summary.

This spec does not authorize follow-on work.

## 3. Upstream Basis

The upstream seam case marks `spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` as contaminated for unsupported existence claims.

The affected file contains unsupported existence claims including:

- `descendant_body_basis_candidate_a_created = true`
- `descendant_body_basis_candidate_b_created = true`
- `descendant_body_basis_derivation_event_recorded = true`

The existence-claim evidence requirement boundary records that future existence-shaped true claims require separately supported evidence before they may be treated as standing or clean basis.

The boundary resolver/test/live artifact recorded that boundary line cleanly.

The boundary terminal summary closed that boundary-result line and left evidence requirement checker/resolver work open and not executed.

This check spec is the first specification for that open mechanical successor.

## 4. Check Question

Given one declared Markdown target surface and one declared evidence map, may one EXISTENCE_CLAIM_EVIDENCE_CHECK be specified to detect existence-shaped true claims, including *_created = true, *_recorded = true, *_performed = true, *_authorized = true, *_occurred = true, *_exists = true, *_standing_created = true, *_currentness_created = true, and *_authority_created = true, and classify each detected claim as EVIDENCE_SUPPORTED or UNSUPPORTED according to declared evidence references, without scanning the repository, discovering files, repairing the target surface, validating unsupported claims, treating repo presence as standing, treating Codex execution as truth, treating operator authorization as sole authorship, treating derivative rendering as standing evidence, treating later recognition as upstream validity, treating contaminated lineage as clean basis, creating descendant bodies, recording derivation, creating standing, creating relation, authorizing crossing, creating FIELD machinery, creating runtime, creating authority, creating currentness, authorizing output, authorizing action, authorizing derivative reception, authorizing synchronization, or authorizing follow-on work?

## 5. Definitions

`existence claim evidence check` means the future check defined by this spec; it is not created here.

`declared Markdown target surface` means one explicitly provided Markdown file path or Markdown text target, not a repository scan.

`declared evidence map` means one explicit mapping from claim keys to evidence references and evidence kinds.

`existence-shaped true claim` includes fields such as `*_created = true`, `*_recorded = true`, `*_performed = true`, `*_authorized = true`, `*_occurred = true`, `*_exists = true`, `*_standing_created = true`, `*_currentness_created = true`, and `*_authority_created = true`.

`detected claim` means an existence-shaped true claim found in the declared target surface.

`claim key` means the field name of a detected claim.

`claim value` means the declared value of a detected claim.

`claim source surface` means the declared target surface in which the detected claim appears.

`evidence reference` means a declared supporting reference such as artifact path, resolver module, test result, terminal summary, operation record, prior standing basis, or explicitly bounded operator-attested evidence.

`evidence kind` means the category of evidence reference.

`evidence adequacy` means whether the declared evidence reference is present, relevant, and sufficient for the detected claim under this check.

`EVIDENCE_SUPPORTED` means a detected claim has adequate declared evidence.

`UNSUPPORTED` means a detected claim lacks adequate declared evidence.

`per-claim outcome` means the outcome assigned to one detected claim.

`file-level outcome` means the aggregate outcome for one declared target surface.

`clean file-level outcome` means no detected existence-shaped true claims are unsupported.

`contaminated-class file-level outcome` means at least one detected existence-shaped true claim is unsupported.

`contaminated lineage` means a preserved target surface must not be silently repaired, hidden, or treated as clean basis.

`repo presence` alone is not standing.

`Codex execution` alone is not truth.

`operator authorization` alone is not sole authorship.

`derivative rendering` alone is not standing evidence.

`later recognition` alone is not proof of upstream validity.

`follow-on work` means later work not authorized by this spec.

This check does not define existence outside repo-local claim posture.

## 6. Check Input Shape

Future check input shape is minimally:

- `check_id`
- `check_type`
- `check_version`
- `check_scope`
- `target_surface_path`
- `target_surface_kind`
- `evidence_map`
- `contaminated_lineage_policy`
- `scan_allowed`
- `repair_allowed`
- `validation_enforcement_allowed`
- `follow_on_authorized`

Required values for future check input:

- `check_type = EXISTENCE_CLAIM_EVIDENCE_CHECK`
- `check_version = 0.1.0`
- `check_scope = DECLARED_SURFACE_ONLY`
- `target_surface_kind = MARKDOWN`
- `scan_allowed = false`
- `repair_allowed = false`
- `validation_enforcement_allowed = false`
- `follow_on_authorized = false`

The check input must not authorize repository scan, repair, validation enforcement, descendant-body work, runtime, authority, currentness, standing, relation, crossing, or follow-on work.

## 7. Evidence Map Shape

For each claim key, the evidence map may provide:

- `claim_key`
- `evidence_kind`
- `evidence_reference`
- `evidence_scope`
- `evidence_target`
- `evidence_note`

Allowed evidence kinds may include:

- `operation_evidence`
- `resolver_evidence`
- `test_evidence`
- `emitted_artifact_evidence`
- `terminal_summary_evidence`
- `prior_standing_basis_evidence`
- `bounded_operator_attested_evidence`
- `negative_seam_case_contamination_evidence`

`evidence_kind = negative_seam_case_contamination_evidence` may support contamination marking, but it does not support the truth of the underlying existence claim.

File existence, latest-file posture, repo-local availability, Codex execution, summary text, operator authorization, derivative rendering, or later convergence must not be accepted as sufficient evidence by themselves.

## 8. Claim Detection Rule

Future implementation must detect existence-shaped true claims in the declared target surface only.

Future implementation must not scan the repository.

Future implementation must not infer claims from filenames, timestamps, screenshots, file order, latest-file posture, or surrounding repo availability.

Target claim patterns include at minimum:

- `*_created = true`
- `*_recorded = true`
- `*_performed = true`
- `*_authorized = true`
- `*_occurred = true`
- `*_exists = true`
- `*_standing_created = true`
- `*_currentness_created = true`
- `*_authority_created = true`

Non-claims such as `*_created = false`, `*_not_created = true`, `*_not_authorized = true`, canonical false posture, preservation text, blocking text, or explanatory text must not be treated as supported existence claims.

The future implementation must distinguish claim key, claim value, and surrounding explanatory posture.

## 9. Evidence Matching Rule

Each detected existence-shaped true claim must match an evidence-map entry for the same claim key or a declared equivalent key.

Each matched evidence entry must identify `evidence_kind` and `evidence_reference`.

Absence of an evidence-map entry yields `UNSUPPORTED` for that claim.

Evidence references must be claim-specific enough to avoid treating broad repo existence as evidence.

Negative seam-case contamination evidence may yield `UNSUPPORTED` with contamination preserved, not `EVIDENCE_SUPPORTED` for the claim.

The first intended live target is `spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md`, and expected future result for its three unsupported claims is `UNSUPPORTED` unless separately supported evidence is declared.

The check must not repair the target surface and must not mutate the evidence map.

## 10. Outcome Family

Future check outcome family:

- `EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED`
- `EXISTENCE_CLAIM_EVIDENCE_CHECK_NOT_RECORDED`
- `EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUIRES_ADDITIONAL_BASIS`
- `EXISTENCE_CLAIM_EVIDENCE_CHECK_BLOCKED`

Future per-claim outcome family:

- `EVIDENCE_SUPPORTED`
- `UNSUPPORTED`
- `CLAIM_NOT_APPLICABLE`
- `CLAIM_CHECK_BLOCKED`

Future file-level outcome family:

- `EXISTENCE_CLAIM_EVIDENCE_CHECK_CLEAN`
- `EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS`
- `EXISTENCE_CLAIM_EVIDENCE_CHECK_BLOCKED`

Recorded means a check result was recorded for one declared target surface and one declared evidence map.

Clean means all detected existence-shaped true claims are evidence-supported or no applicable existence-shaped true claims were detected.

Contaminated-class means at least one detected existence-shaped true claim is unsupported.

Blocked means the input is malformed, scan-shaped, repair-shaped, validation-enforcement-shaped, descendant-work-shaped, runtime-shaped, authority-shaped, currentness-shaped, standing-shaped, follow-on-shaped, raw-body-return-shaped, hidden-repair-shaped, silent-overwrite-shaped, or otherwise overreaching.

## 11. Blocking Conditions

Future check must block when:

- target surface is missing
- target surface is not declared
- target surface is not Markdown
- evidence map is missing
- evidence map is malformed
- check type is not `EXISTENCE_CLAIM_EVIDENCE_CHECK`
- check scope is not `DECLARED_SURFACE_ONLY`
- `scan_allowed` is true
- `repair_allowed` is true
- `validation_enforcement_allowed` is true
- `follow_on_authorized` is true
- input requests repository scan
- input requests file discovery
- input requests repair
- input requests target mutation
- input requests validation enforcement
- input requests unsupported claim validation
- input requests descendant-body work
- input requests runtime, authority, currentness, standing, relation, crossing, FIELD machinery, output, action, derivative reception, synchronization, or follow-on work
- input treats repo presence as standing
- input treats Codex execution as truth
- input treats operator authorization as sole authorship
- input treats derivative rendering as standing evidence
- input treats later recognition as upstream validity
- input treats contaminated lineage as clean basis
- input requests hidden repair or silent overwrite
- input asks to return raw full target Markdown body
- input asks to return raw full evidence map body if marked sensitive

## 12. Non-Claims

This spec preserves these non-claims:

- `check_created = false`
- `resolver_created = false`
- `test_created = false`
- `artifact_created = false`
- `scan_performed = false`
- `repository_scan_performed = false`
- `validation_enforced = false`
- `target_surface_repaired = false`
- `target_surface_edited = false`
- `target_surface_deleted = false`
- `target_surface_overwritten = false`
- `target_surface_invalidated_by_replacement = false`
- `unsupported_existence_claims_validated = false`
- `descendant_body_a_created = false`
- `descendant_body_b_created = false`
- `descendant_body_basis_candidate_a_created = false`
- `descendant_body_basis_candidate_b_created = false`
- `valid_derivation_event_recorded = false`
- `body_division_performed = false`
- `body_copy_performed = false`
- `body_distinction_created = false`
- `separate_lineage_receipt_created = false`
- `separate_sealing_created = false`
- `descendant_standing_check_performed = false`
- `standing_descendant_created = false`
- `first_crossing_authorized = false`
- `relation_created = false`
- `field_machinery_created = false`
- `iammai_system_continuation_reopened = false`
- `field_handoff_reversed = false`
- `runtime_created = false`
- `api_created = false`
- `machinery_created = false`
- `currentness_created = false`
- `authority_created = false`
- `standing_created = false`
- `output_authorized = false`
- `action_authorized = false`
- `derivative_reception_authorized = false`
- `synchronization_authorized = false`
- `follow_on_work_authorized = false`
- `repo_presence_treated_as_standing = false`
- `codex_execution_treated_as_truth = false`
- `operator_authorization_treated_as_sole_authorship = false`
- `derivative_rendering_treated_as_standing_evidence = false`
- `later_recognition_treated_as_upstream_validity = false`
- `contaminated_lineage_treated_as_clean_basis = false`
- `hidden_repair_performed = false`
- `silent_overwrite_performed = false`

No false non-claim is listed as true.

## 13. What Remains Open

Open and not executed:

- existence-claim evidence check resolver
- existence-claim evidence check test
- existence-claim evidence check artifact
- existence-claim evidence check terminal summary
- first live check against `spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md`
- automated repository scan, if ever separately bounded
- repair or successor handling of the affected file, if ever separately bounded
- descendant-body derivation successor, if ever separately bounded
- descendant standing checks
- first crossing
- relation
- FIELD machinery
- runtime
- API
- currentness
- authority
- standing
- output authorization
- action authorization
- derivative reception
- synchronization
- follow-on work

Open means not scheduled.

Open means not authorized.

Open means not executed.

Open does not mean next unless separately selected.

## 14. Closing Lock

Existence claim evidence check may specify only a future declared-surface evidence check for existence-shaped true claims against a declared evidence map. It is downstream of one preserved negative seam case, one preserved contaminated lineage point, and one completed existence-claim evidence requirement boundary line. It does not create resolver, tests, artifact, scan, validation enforcement, repair, descendant bodies, candidate bodies, derivation, standing, relation, crossing, FIELD machinery, runtime, authority, currentness, output, action, derivative reception, synchronization, or follow-on work. It does not define existence generally. It does not create ontology doctrine. It does not repair, edit, delete, overwrite, replace, validate, or redeem spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md. The future check must use one declared Markdown target surface and one declared evidence map. It must not scan the repository. It must not treat repo presence as standing, Codex execution as truth, operator authorization as sole authorship, derivative rendering as standing evidence, later recognition as upstream validity, or contaminated lineage as clean basis. The first intended live target remains spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md, whose three unsupported existence claims are expected to yield UNSUPPORTED unless separately supported evidence is declared. Any actual resolver, test, artifact, live check, terminal summary, scan, repair successor, descendant-body successor, standing check, crossing, relation, FIELD machinery, runtime, authority, currentness, output, action, derivative reception, synchronization, or follow-on work still requires a separately bounded step.
