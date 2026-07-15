# Cross-Carrier Seam Proof 004 Report

This report is a human-readable companion to the machine-readable cross-carrier proof 004 snapshot. It is an implementation-local readability surface only and does not function as protocol law.

## Metadata

- Generated at: `2026-04-04T23:14:36Z`
- Report path: `lab/snapshots/cross_carrier_seam_proof_004_report__20260404T231436Z.md`
- Source snapshot path: `lab/snapshots/cross_carrier_seam_proof_004_snapshot__20260404T214817Z.json`
- Source snapshot generated at: `2026-04-04T21:48:17Z`
- Snapshot acquisition mode: `existing_snapshot`
- Proof root: `lab/cross_carrier_seam_proof_004`
- Proof id: `cross_carrier_seam_proof_004`
- Proof name: `Fourth Cross-Carrier Seam Proof`
- Internalized archive status: `true`

## Current Proof Reading

The fourth cross-carrier seam proof presently reads as one ranked proof object with two source-side release turns and two imported receiving-side bounded arrival turns preserved in the same body.

- Source-side release lineage remains source-side: `true`
- Receiving-side clean bounded in-between arrival remains receiving-side: `true`
- Receiving-side obsolete-origin bounded in-between arrival remains receiving-side: `true`
- Import preserves relation without merger: `true`
- Internalized archive status: `true`
- Source run count: `2`
- Imported receiving branch count: `2`
- Clean source execution id: `execution-7f48b1ff3ec1456aa803553b10a02d51`
- Obsolete-origin source execution id: `execution-98c5d45277c940e5aadb9a452a5a292d`
- Clean receiving execution id: `execution-ae3be271825b44fda431ccec146b384d`
- Obsolete-origin receiving execution id: `execution-592fd6601aad4565aa4dd94a69ddcf59`

Source-side release lineage remains source-side release lineage. Receiving-side clean bounded in-between arrival remains clean receiving-side arrival lineage. Receiving-side obsolete-origin bounded in-between arrival remains obsolete-origin receiving-side arrival lineage. Import preserves relation without merger.

## Source-Side Clean-Origin Release Lineage

- Source execution id: `execution-7f48b1ff3ec1456aa803553b10a02d51`
- Source run path: `lab/cross_carrier_seam_proof_004/source_runs/execution-7f48b1ff3ec1456aa803553b10a02d51`
- Summary path: `lab/cross_carrier_seam_proof_004/source_runs/execution-7f48b1ff3ec1456aa803553b10a02d51/summary/summary.json`
- Manifest path: `lab/cross_carrier_seam_proof_004/source_runs/execution-7f48b1ff3ec1456aa803553b10a02d51/manifest/manifest.json`
- Origin approval condition path: `lab/cross_carrier_seam_proof_004/source_runs/execution-7f48b1ff3ec1456aa803553b10a02d51/release/origin_approval_condition.json`
- Package path: `lab/cross_carrier_seam_proof_004/source_runs/execution-7f48b1ff3ec1456aa803553b10a02d51/package/transfer_package.json`
- Run represents: `clean_origin_release`
- Origin approval condition status: `origin_clean`
- Origin approval lawfully sovereign: `true`
- Release without origin ratification: `false`
- Continued compliance would ratify distortion: `false`
- Release lawful: `true`
- Lawful release outcome: `lawful_release_with_clean_origin_approval`
- Source remains source: `true`
- Origin remains lineage-visible: `true`
- Package valid: `true`
- Expected arrival status: `bounded_in_between`
- Downstream full closure granted: `false`

The clean-origin release remains a source-side control case. It keeps source and origin relation explicit while still refusing to convert release into downstream final standing.

## Source-Side Obsolete-Origin Release Lineage

- Source execution id: `execution-98c5d45277c940e5aadb9a452a5a292d`
- Source run path: `lab/cross_carrier_seam_proof_004/source_runs/execution-98c5d45277c940e5aadb9a452a5a292d`
- Summary path: `lab/cross_carrier_seam_proof_004/source_runs/execution-98c5d45277c940e5aadb9a452a5a292d/summary/summary.json`
- Manifest path: `lab/cross_carrier_seam_proof_004/source_runs/execution-98c5d45277c940e5aadb9a452a5a292d/manifest/manifest.json`
- Origin approval condition path: `lab/cross_carrier_seam_proof_004/source_runs/execution-98c5d45277c940e5aadb9a452a5a292d/release/origin_approval_condition.json`
- Package path: `lab/cross_carrier_seam_proof_004/source_runs/execution-98c5d45277c940e5aadb9a452a5a292d/package/transfer_package.json`
- Run represents: `obsolete_origin_lawful_egress`
- Origin approval condition status: `origin_obsolete_or_contaminated`
- Origin approval lawfully sovereign: `false`
- Release without origin ratification: `true`
- Continued compliance would ratify distortion: `true`
- Release lawful: `true`
- Lawful release outcome: `lawful_egress_without_origin_ratification`
- Source remains source: `true`
- Origin remains lineage-visible: `true`
- Package valid: `true`
- Expected arrival status: `bounded_in_between`
- Downstream full closure granted: `false`

The obsolete-origin release is the specific lawful-egress threshold. Source remains source, origin remains lineage-visible, withheld origin approval is not treated as sovereign veto, and the release does not pretend to grant downstream closure.

## Receiving-Side Clean Bounded In-Between Arrival

- Imported branch: `clean`
- Receiving execution id: `execution-ae3be271825b44fda431ccec146b384d`
- Imported run path: `lab/cross_carrier_seam_proof_004/receiving_imports/clean/execution-ae3be271825b44fda431ccec146b384d`
- Summary path: `lab/cross_carrier_seam_proof_004/receiving_imports/clean/execution-ae3be271825b44fda431ccec146b384d/summary/summary.json`
- Manifest path: `lab/cross_carrier_seam_proof_004/receiving_imports/clean/execution-ae3be271825b44fda431ccec146b384d/manifest/manifest.json`
- Origin approval condition snapshot path: `lab/cross_carrier_seam_proof_004/receiving_imports/clean/execution-ae3be271825b44fda431ccec146b384d/package/origin_approval_condition_snapshot.json`
- Package id: `transfer-package-905ff57533534dbdbf50c3eab4e583c9`
- Origin approval condition status: `origin_clean`
- Origin approval lawfully sovereign: `true`
- Technical receipt: `true`
- Package valid: `true`
- Ingress lawful: `true`
- Ingress outcome: `lawful_bounded_in_between_arrival`
- Arrival status: `bounded_in_between`
- Source remains source: `true`
- Origin remains lineage-visible: `true`
- Shared authority: `false`
- Standing upgraded: `false`
- Final closure claimed: `false`
- Release without origin ratification: `false`

On the clean imported branch, the package is technically received and lawfully carried as bounded in-between arrival. The result remains receiving-side lineage and does not inherit silent authority.

## Receiving-Side Obsolete-Origin Bounded In-Between Arrival

- Imported branch: `obsolete_origin`
- Receiving execution id: `execution-592fd6601aad4565aa4dd94a69ddcf59`
- Imported run path: `lab/cross_carrier_seam_proof_004/receiving_imports/obsolete_origin/execution-592fd6601aad4565aa4dd94a69ddcf59`
- Summary path: `lab/cross_carrier_seam_proof_004/receiving_imports/obsolete_origin/execution-592fd6601aad4565aa4dd94a69ddcf59/summary/summary.json`
- Manifest path: `lab/cross_carrier_seam_proof_004/receiving_imports/obsolete_origin/execution-592fd6601aad4565aa4dd94a69ddcf59/manifest/manifest.json`
- Origin approval condition snapshot path: `lab/cross_carrier_seam_proof_004/receiving_imports/obsolete_origin/execution-592fd6601aad4565aa4dd94a69ddcf59/package/origin_approval_condition_snapshot.json`
- Package id: `transfer-package-fdbca801d31046939dbc4d4574a104bf`
- Origin approval condition status: `origin_obsolete_or_contaminated`
- Origin approval lawfully sovereign: `false`
- Technical receipt: `true`
- Package valid: `true`
- Ingress lawful: `true`
- Ingress outcome: `lawful_bounded_in_between_arrival`
- Arrival status: `bounded_in_between`
- Source remains source: `true`
- Origin remains lineage-visible: `true`
- Shared authority: `false`
- Standing upgraded: `false`
- Final closure claimed: `false`
- Release without origin ratification: `true`

On the obsolete-origin imported branch, the package remains valid, arrival remains bounded in-between, and the preserved receiving-side record keeps non-sovereign origin approval distinct from downstream closure.

## Lawful Egress Threshold

The specific architectural advance in proof 004 is that origin may remain source and lineage-visible while obsolete or contaminated origin approval loses sovereignty, lawful egress proceeds without obsolete-origin ratification, and receiving-side arrival remains bounded in-between rather than counterfeit full closure.

- Lawful egress from obsolete container supported: `true`
- Source-side obsolete-origin non-sovereign approval visible: `true`
- Receiving-side obsolete-origin bounded in-between arrival visible: `true`
- Clean control bounded in-between arrival visible: `true`
- Import note path: `lab/cross_carrier_seam_proof_004/receiving_imports/IMPORT_NOTE.md`
- Seam case law path: `SEAM_CASE_LAW__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER.md`
- Transfer-account entry path: `v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md`

Current preserved material supports a bounded lawful-egress reading: source remains source, origin remains lineage-visible, obsolete or contaminated origin approval is visible but non-sovereign, release may proceed without origin ratification, and receiving-side arrival remains bounded in-between rather than counterfeit full closure.

The import note remains a readability aid only. It makes imported receiving-side evidence easier to read, but it does not replace the underlying receiving-side run artifacts.

## What This Shows

- Lawful release from clean origin approval remains visible as a bounded comparison case.
- Lawful egress from obsolete or contaminated origin remains visible without treating withheld origin approval as sovereign veto.
- Bounded in-between arrival is preserved on both receiving-side branches.
- Source remains source and origin remains lineage-visible across release and imported arrival.
- No silent authority inheritance, standing upgrade, or final closure is claimed on the far side.
- Imported receiving-side evidence remains receiving-side evidence even after it is carried back into the main body.

## What It Does Not Yet Show

- Not yet a multi-carrier mesh.
- Not yet bidirectional sync.
- Not yet shared canonical state.
- Not yet a relational field.
- Not yet an exhaustion of lawful-egress or cross-carrier seam jurisprudence.
- Not yet a flattening of source-side and receiving-side evidence into one undifferentiated proof event.

## Partial Read Notes

- No top-level receiver-local condition surface is currently preserved at lab/cross_carrier_seam_proof_004/receiver_local_condition.json.

## Boundary Note

This report is an additive human-readable companion to the machine-readable cross-carrier proof 004 snapshot. It does not replace the snapshot, it does not rewrite prior artifacts, it does not convert imported receiving-side evidence into source-side history, and it does not convert implementation-local readability into protocol law.
