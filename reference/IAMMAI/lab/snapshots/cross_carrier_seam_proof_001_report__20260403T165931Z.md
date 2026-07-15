# Cross-Carrier Seam Proof 001 Report

This report is a human-readable companion to the machine-readable cross-carrier proof snapshot. It is an implementation-local readability surface only and does not function as protocol law.

## Metadata

- Generated at: `2026-04-03T16:59:31Z`
- Report path: `lab/snapshots/cross_carrier_seam_proof_001_report__20260403T165931Z.md`
- Source snapshot path: `lab/snapshots/cross_carrier_seam_proof_001_snapshot__20260403T165931Z.json`
- Proof root: `lab/cross_carrier_seam_proof_001`
- Proof id: `cross_carrier_seam_proof_001`
- Proof name: `First Cross-Carrier Seam Proof`
- Internalized archive status: `true`

## Current Proof Reading

The first cross-carrier seam proof presently reads as one ranked proof object with three distinct sides preserved in the same archive body.

- Source-side release lineage remains source-side: `true`
- Receiving-side lawful ingress remains receiving-side: `true`
- Receiving-side refusal / non-passage remains receiving-side: `true`
- Import preserves relation without merger: `true`
- Imported receiving-side evidence readability note: `lab/cross_carrier_seam_proof_001/receiving_imports/IMPORT_NOTE.md`

Source-side release lineage remains source-side release lineage. Receiving-side lawful ingress and receiving-side refusal or non-passage remain receiving-side lineage. Import preserves relation without merger.

## Source-Side Release Lineage

- Source run count: `2`
- Source runs root: `lab/cross_carrier_seam_proof_001/source_runs`

### Lawful Package Release

- Execution id: `execution-71a0490222f8433e9b3081eecc817d3a`
- Path: `lab/cross_carrier_seam_proof_001/source_runs/execution-71a0490222f8433e9b3081eecc817d3a`
- Mode: `release`
- Expected receiving outcome: `lawful_derivative_ingress`
- Package ingress lawful if received: `true`
- `source_remains_source = true`
- `shared_authority = false`
- `standing_transferred = false`
- Package attempted unlawful standing transfer: `false`

### Invalid Package Release For Refusal / Non-Passage

- Execution id: `execution-f72b3f6777fc47368c18567fa4df305e`
- Path: `lab/cross_carrier_seam_proof_001/source_runs/execution-f72b3f6777fc47368c18567fa4df305e`
- Mode: `release_invalid`
- Expected receiving outcome: `refusal_non_passage`
- Package ingress lawful if received: `false`
- `source_remains_source = true`
- `shared_authority = false`
- `standing_transferred = false`
- Package attempted unlawful standing transfer: `true`

## Receiving-Side Lawful Ingress

- Imported branch: `lawful`
- Branch path: `lab/cross_carrier_seam_proof_001/receiving_imports/lawful`
- Imported run count: `1`
- Receiving execution id: `execution-a57cdf2c25ce4cf9bcd96a4bc17b2144`
- Imported run path: `lab/cross_carrier_seam_proof_001/receiving_imports/lawful/execution-a57cdf2c25ce4cf9bcd96a4bc17b2144`
- Mode: `ingress`
- Ingress outcome: `lawful_derivative_ingress`
- Ingress lawful: `true`
- Arrival status: `derivative_only`
- `source_remains_source = true`
- `shared_authority = false`
- `standing_upgraded = false`
- Receiving-side lawful ingress remains derivative-only rather than becoming silent standing.

## Receiving-Side Refusal / Non-Passage

- Imported branch: `refusal_non_passage`
- Branch path: `lab/cross_carrier_seam_proof_001/receiving_imports/refusal_non_passage`
- Imported run count: `1`
- Receiving execution id: `execution-c1a76f07c4fb4b70aebb3c40831c775d`
- Imported run path: `lab/cross_carrier_seam_proof_001/receiving_imports/refusal_non_passage/execution-c1a76f07c4fb4b70aebb3c40831c775d`
- Mode: `ingress`
- Ingress outcome: `refusal_non_passage`
- Ingress lawful: `false`
- Arrival status: `none`
- `source_remains_source = true`
- `shared_authority = false`
- `standing_upgraded = false`
- `refusal_visible = true`
- `non_passage = true`
- Receiving-side refusal remains visible rather than being hidden inside transport success.

## Internalized Archive Relation

The current archive no longer carries only the source-side release runs. It now also carries imported receiving-side lawful ingress lineage and imported receiving-side refusal or non-passage lineage.

- Source run count inside the body: `2`
- Imported receiving branch count inside the body: `2`
- Internalized archive support note: `The first cross-carrier seam proof is internally carried where source-side release lineage and imported receiving-side lineage are co-present inside the same body without merger.`
- Import note remains a readability surface only; it does not replace the imported run artifacts.

## What This Shows

- Lawful derivative-only ingress is preserved as a receiving-side outcome rather than being rewritten as source-side history.
- Source remains source across release and receiving-side ingress.
- No silent authority inheritance is required for the proof to remain legible.
- Visible refusal and non-passage are preserved on the invalid transfer rather than disappearing into transport success.
- The proof is now internally carried on both sides without merger between source-side and receiving-side lineage.

## What It Does Not Yet Show

- Not yet a multi-carrier mesh.
- Not yet bidirectional sync.
- Not yet shared canonical state.
- Not yet a relational field.
- Not yet a flattening of source-side and receiving-side evidence into one undifferentiated proof event.

## Boundary Note

This report is an additive human-readable companion to the machine-readable cross-carrier proof snapshot. It does not replace the snapshot, it does not rewrite prior artifacts, and it does not convert implementation-local readability into protocol law.
