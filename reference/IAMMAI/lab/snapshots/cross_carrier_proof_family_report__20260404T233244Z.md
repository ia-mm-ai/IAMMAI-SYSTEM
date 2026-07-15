# Cross-Carrier Proof Family Report

This report is a human-readable companion to the machine-readable cross-carrier family snapshot. It is built directly from the latest cross-carrier family snapshot already present under `lab/snapshots/`.

It is an implementation-local readability surface only. It does not regenerate snapshot state, rerun proofs, mutate prior artifacts, or function as protocol law.

## Metadata

- Generated at: `2026-04-04T23:32:44Z`
- Report path: `lab/snapshots/cross_carrier_proof_family_report__20260404T233244Z.md`
- Source snapshot path: `lab/snapshots/cross_carrier_family_snapshot__20260404T233244Z.json`
- Source snapshot generated at: `2026-04-04T23:32:44Z`
- Lab root: `lab`

## Family Summary

- Total cross-carrier proofs discovered: `4`
- Total source runs discovered across the family: `6`
- Total receiving imported branches discovered across the family: `8`
- Total receiving imported runs discovered across the family: `8`
- Proof ids present: `cross_carrier_seam_proof_001`, `cross_carrier_seam_proof_002`, `cross_carrier_seam_proof_003`, `cross_carrier_seam_proof_004`

The family remains a set of distinct bounded cross-carrier proof turns rather than one flat transfer story. Proof 001, proof 002, and proof 003 preserve different seam concerns and together form a growing body of cross-carrier seam evidence without implying full relational field, mesh, or middleware.

## Family Progression

- Proof 001 preserves the first bounded cross-carrier seam split between source validity or invalidity and visible receiving-side ingress or refusal.
- Proof 002 preserves the contaminated receiving parser or governance case in which technical receipt can occur while lawful ingress is still denied.
- Proof 003 preserves the receiver-local embodied contamination case in which the same valid package diverges by receiving-side local condition.

## Current Proof Reading

The current cross-carrier line reads as a family of distinct bounded proof-bearing experiments rather than as one flat transfer object. Each proof keeps its own concern, its own lineage surfaces, and its own ingress or refusal structure.

## Proof 001: First Cross-Carrier Seam Proof

- Proof id: `cross_carrier_seam_proof_001`
- Distinct concern: Bounded first cross-carrier seam proof for source validity or invalidity and lawful ingress versus visible refusal or non-passage.
- Script path: `lab/run_cross_carrier_seam_proof_001.py`
- Internalized archive status: `true`
- Source run count: `2`
- Receiving imported branch names: `lawful`, `refusal_non_passage`
- Latest source run path: `lab/cross_carrier_seam_proof_001/source_runs/execution-f72b3f6777fc47368c18567fa4df305e/package/transfer_package.json`
- Latest source summary path: `lab/cross_carrier_seam_proof_001/source_runs/execution-f72b3f6777fc47368c18567fa4df305e/summary/summary.json`
- Latest source execution id: `execution-f72b3f6777fc47368c18567fa4df305e`
- Imported branch `lawful`: latest summary `lab/cross_carrier_seam_proof_001/receiving_imports/lawful/execution-a57cdf2c25ce4cf9bcd96a4bc17b2144/summary/summary.json`, latest outcome `lawful_derivative_ingress`
- Imported branch `refusal_non_passage`: latest summary `lab/cross_carrier_seam_proof_001/receiving_imports/refusal_non_passage/execution-c1a76f07c4fb4b70aebb3c40831c775d/summary/summary.json`, latest outcome `refusal_non_passage`
- Receiving outcome counts: `lawful_derivative_ingress=1`, `refusal_non_passage=1`
- Receiving technical receipt counts: `not surfaced in preserved summary fields`
- Receiving arrival-status counts: `derivative_only=1`, `none=1`
- Receiving blocking-condition counts: `not surfaced in preserved summary fields`
- Mismatched cases present: `false`
- No mismatched cases are surfaced in the preserved summary fields for this proof.
- Proof-specific snapshot surface: `lab/snapshots/cross_carrier_seam_proof_001_snapshot__20260403T165931Z.json`
- Proof-specific report surface: `lab/snapshots/cross_carrier_seam_proof_001_report__20260403T165931Z.md`
- Threshold note: Current visible family account posture preserves the first cross-carrier proof line through `v1/11_TRANSFER_ACCOUNT_ENTRY__FIRST_CROSS_CARRIER_SEAM_PROOF.md`, `v1/12_TRANSFER_ACCOUNT_ENTRY__CROSS_CARRIER_PROOF_INTERNALIZED.md`, and `v1/14_TRANSFER_ACCOUNT_ENTRY__CROSS_CARRIER_PROOF_READABILITY_THRESHOLD.md`.

## Proof 002: Contaminated Receiving Parser Case

- Proof id: `cross_carrier_seam_proof_002`
- Distinct concern: Bounded contaminated receiving parser or governance case in which a valid package may be technically received while lawful ingress is denied.
- Script path: `lab/run_cross_carrier_seam_proof_002.py`
- Internalized archive status: `true`
- Source run count: `1`
- Receiving imported branch names: `clean`, `contaminated_non_passage`
- Latest source run path: `lab/cross_carrier_seam_proof_002/source_runs/execution-6887b6d9bcb043bf9f7111ab1aa23afd/package/transfer_package.json`
- Latest source summary path: `lab/cross_carrier_seam_proof_002/source_runs/execution-6887b6d9bcb043bf9f7111ab1aa23afd/summary/summary.json`
- Latest source execution id: `execution-6887b6d9bcb043bf9f7111ab1aa23afd`
- Imported branch `clean`: latest summary `lab/cross_carrier_seam_proof_002/receiving_imports/clean/execution-13de737f57f9406584093fbe1557c7d1/summary/summary.json`, latest outcome `lawful_derivative_ingress`
- Imported branch `contaminated_non_passage`: latest summary `lab/cross_carrier_seam_proof_002/receiving_imports/contaminated_non_passage/execution-b67a0b5b6fc54a31ac2bbfcf119be752/summary/summary.json`, latest outcome `contaminated_parser_non_passage`
- Receiving outcome counts: `contaminated_parser_non_passage=1`, `lawful_derivative_ingress=1`
- Receiving technical receipt counts: `true=2`
- Receiving arrival-status counts: `derivative_only=1`, `none=1`
- Receiving blocking-condition counts: `receiving_parser_governance_contamination=1`
- Mismatched cases present: `false`
- No mismatched cases are surfaced in the preserved summary fields for this proof.
- Proof-specific snapshot surface: `unreadable`
- Proof-specific report surface: `unreadable`
- Threshold note: Within the current family archive, proof 002 stands as the distinct contaminated receiving parser/governance turn in which technical receipt remains visible while lawful ingress can still be denied.

## Proof 003: Receiver-Local Embodied Contamination

- Proof id: `cross_carrier_seam_proof_003`
- Distinct concern: Bounded receiver-local embodied contamination case in which the same valid package diverges by receiving-side local condition.
- Script path: `lab/run_cross_carrier_seam_proof_003.py`
- Internalized archive status: `true`
- Source run count: `1`
- Receiving imported branch names: `clean`, `contaminated_non_passage`
- Latest source run path: `lab/cross_carrier_seam_proof_003/source_runs/execution-bf52e3aefeb1433cbf69f11598f1dd59/package/transfer_package.json`
- Latest source summary path: `lab/cross_carrier_seam_proof_003/source_runs/execution-bf52e3aefeb1433cbf69f11598f1dd59/summary/summary.json`
- Latest source execution id: `execution-bf52e3aefeb1433cbf69f11598f1dd59`
- Imported branch `clean`: latest summary `lab/cross_carrier_seam_proof_003/receiving_imports/clean/execution-ed200b44ab054962af8ed194fdd5361c/summary/summary.json`, latest outcome `lawful_derivative_ingress`
- Imported branch `contaminated_non_passage`: latest summary `lab/cross_carrier_seam_proof_003/receiving_imports/contaminated_non_passage/execution-dcbec996f0bd43fbad21649ccce30c26/summary/summary.json`, latest outcome `receiver_local_contamination_non_passage`
- Receiving outcome counts: `lawful_derivative_ingress=1`, `receiver_local_contamination_non_passage=1`
- Receiving technical receipt counts: `true=2`
- Receiving arrival-status counts: `derivative_only=1`, `none=1`
- Receiving blocking-condition counts: `receiver_local_parser_governance_contamination=1`
- Mismatched cases present: `false`
- No mismatched cases are surfaced in the preserved summary fields for this proof.
- Proof-specific snapshot surface: `lab/snapshots/cross_carrier_seam_proof_003_snapshot__20260403T211327Z.json`
- Proof-specific report surface: `lab/snapshots/cross_carrier_seam_proof_003_report__20260403T211327Z.md`
- Threshold note: Current visible family account posture preserves the receiver-local proof line through `v1/16_TRANSFER_ACCOUNT_ENTRY__RECEIVER_LOCAL_CROSS_CARRIER_PROOF.md` and `v1/17_TRANSFER_ACCOUNT_ENTRY__RECEIVER_LOCAL_CROSS_CARRIER_PROOF_READABILITY_THRESHOLD.md`.

## cross_carrier_seam_proof_004

- Proof id: `cross_carrier_seam_proof_004`
- Distinct concern: `unreadable`
- Script path: `lab/run_cross_carrier_seam_proof_004.py`
- Internalized archive status: `true`
- Source run count: `2`
- Receiving imported branch names: `clean`, `obsolete_origin`
- Latest source run path: `lab/cross_carrier_seam_proof_004/source_runs/execution-98c5d45277c940e5aadb9a452a5a292d/package/transfer_package.json`
- Latest source summary path: `lab/cross_carrier_seam_proof_004/source_runs/execution-98c5d45277c940e5aadb9a452a5a292d/summary/summary.json`
- Latest source execution id: `execution-98c5d45277c940e5aadb9a452a5a292d`
- Imported branch `clean`: latest summary `lab/cross_carrier_seam_proof_004/receiving_imports/clean/execution-ae3be271825b44fda431ccec146b384d/summary/summary.json`, latest outcome `lawful_bounded_in_between_arrival`
- Imported branch `obsolete_origin`: latest summary `lab/cross_carrier_seam_proof_004/receiving_imports/obsolete_origin/execution-592fd6601aad4565aa4dd94a69ddcf59/summary/summary.json`, latest outcome `lawful_bounded_in_between_arrival`
- Receiving outcome counts: `lawful_bounded_in_between_arrival=2`
- Receiving technical receipt counts: `true=2`
- Receiving arrival-status counts: `bounded_in_between=2`
- Receiving blocking-condition counts: `not surfaced in preserved summary fields`
- Mismatched cases present: `false`
- No mismatched cases are surfaced in the preserved summary fields for this proof.
- Proof-specific snapshot surface: `lab/snapshots/cross_carrier_seam_proof_004_snapshot__20260404T214817Z.json`
- Proof-specific report surface: `lab/snapshots/cross_carrier_seam_proof_004_report__20260404T231436Z.md`
- Threshold note: This proof stands as a distinct bounded family turn within the current cross-carrier archive.

## What The Cross-Carrier Family Now Shows

- The family now preserves multiple distinct cross-carrier proof turns rather than one generic carrier crossing story.
- Proof 001 preserves source validity or invalidity together with lawful derivative ingress versus visible refusal or non-passage.
- Proof 002 preserves the contaminated receiving parser or governance case in which technical receipt can remain visible while lawful ingress is denied.
- Proof 003 preserves the receiver-local embodied contamination case in which the same valid package diverges by receiver-local condition.
- Imported receiving-side evidence can remain receiving-side lineage inside the same body without being rewritten into source-side history.
- Family readability has been added without flattening source-side release lineage, receiving-side ingress lineage, and receiving-side refusal or non-passage into one undifferentiated event.

## What It Does Not Yet Show

- Not yet a multi-carrier mesh.
- Not yet bidirectional sync.
- Not yet shared canonical state.
- Not yet a relational field.
- Not yet total cross-carrier doctrine.
- Not yet a warrant to treat the family report itself as protocol law.

## Boundary Note

This report is an additive human-readable companion to the machine-readable cross-carrier family snapshot. It does not replace the snapshot, it does not rewrite prior proofs, it does not normalize old outputs by mutation, and it does not flatten the family into one generic transfer story.
