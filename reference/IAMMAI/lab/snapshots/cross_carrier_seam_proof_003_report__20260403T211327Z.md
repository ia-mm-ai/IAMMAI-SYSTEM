# Cross-Carrier Seam Proof 003 Report

This report is a human-readable companion to the machine-readable cross-carrier proof 003 snapshot. It is an implementation-local readability surface only and does not function as protocol law.

## Metadata

- Generated at: `2026-04-03T21:13:27Z`
- Report path: `lab/snapshots/cross_carrier_seam_proof_003_report__20260403T211327Z.md`
- Source snapshot path: `lab/snapshots/cross_carrier_seam_proof_003_snapshot__20260403T211327Z.json`
- Proof root: `lab/cross_carrier_seam_proof_003`
- Proof id: `cross_carrier_seam_proof_003`
- Proof name: `Third Cross-Carrier Seam Proof`
- Internalized archive status: `true`

## Current Proof Reading

The third cross-carrier seam proof presently reads as one ranked proof object with distinct source-side and receiving-side lineages preserved in the same body.

- Source-side release lineage remains source-side: `true`
- Receiving-side clean lawful ingress remains receiving-side: `true`
- Receiving-side contaminated non-passage remains receiving-side: `true`
- Import preserves relation without merger: `true`
- Receiver-local embodied contamination visible: `true`
- Source run count: `1`
- Imported receiving branch count: `2`
- Source package id: `transfer-package-02af9dff5a6a44518c823d2957976490`
- Clean branch outcome: `lawful_derivative_ingress`
- Contaminated branch outcome: `receiver_local_contamination_non_passage`

Source-side release lineage remains source-side release lineage. Receiving-side clean lawful ingress remains clean receiving-side ingress lineage. Receiving-side contaminated non-passage remains contaminated receiving-side non-passage lineage. Import preserves relation without merger.

## Source-Side Release Lineage

- Source run count: `1`
- Source runs root: `lab/cross_carrier_seam_proof_003/source_runs`
- Source execution id: `execution-bf52e3aefeb1433cbf69f11598f1dd59`
- Source run path: `lab/cross_carrier_seam_proof_003/source_runs/execution-bf52e3aefeb1433cbf69f11598f1dd59`
- Source package path: `lab/cross_carrier_seam_proof_003/source_runs/execution-bf52e3aefeb1433cbf69f11598f1dd59/package/transfer_package.json`
- Package id: `transfer-package-02af9dff5a6a44518c823d2957976490`
- Canonical witness id: `witness-fb0af49008764f0f96d6df6b01a0e341`
- Package valid: `true`
- Canonical body schema valid: `true`
- `source_remains_source = true`
- `shared_authority = false`
- `standing_transferred = false`
- Expected clean receiver-local outcome: `lawful_derivative_ingress`
- Expected contaminated receiver-local outcome: `receiver_local_contamination_non_passage`
- Receiver-local condition controls admissibility: `true`
- Same valid package may diverge by receiver-local condition: `true`
- Do not blame source for receiver-local contamination: `true`

The source-side release remains source-side release lineage. It does not silently transfer authority, and it does not predetermine that every technically receivable arrival will become lawful receiving-side ingress.

## Receiving-Side Clean Lawful Ingress

- Imported branch: `clean`
- Branch path: `lab/cross_carrier_seam_proof_003/receiving_imports/clean`
- Imported run count: `1`
- Receiving execution id: `execution-ed200b44ab054962af8ed194fdd5361c`
- Imported run path: `lab/cross_carrier_seam_proof_003/receiving_imports/clean/execution-ed200b44ab054962af8ed194fdd5361c`
- Summary path: `lab/cross_carrier_seam_proof_003/receiving_imports/clean/execution-ed200b44ab054962af8ed194fdd5361c/summary/summary.json`
- Receiver-local condition snapshot path: `lab/cross_carrier_seam_proof_003/receiving_imports/clean/execution-ed200b44ab054962af8ed194fdd5361c/package/receiver_local_condition_snapshot.json`
- Package id: `transfer-package-02af9dff5a6a44518c823d2957976490`
- Receiver-local condition status: `admissible`
- Receiver-local governance admissible: `true`
- Technical receipt: `true`
- Package valid: `true`
- Ingress lawful: `true`
- Ingress outcome: `lawful_derivative_ingress`
- Arrival status: `derivative_only`
- `source_remains_source = true`
- `shared_authority = false`
- `standing_upgraded = false`

On the clean imported branch, the same valid package is technically received and admitted lawfully as derivative-only ingress. Source remains source, shared authority does not appear, and the receiving-side result remains receiving-side lineage.

## Receiving-Side Contaminated Non-Passage

- Imported branch: `contaminated_non_passage`
- Branch path: `lab/cross_carrier_seam_proof_003/receiving_imports/contaminated_non_passage`
- Imported run count: `1`
- Receiving execution id: `execution-dcbec996f0bd43fbad21649ccce30c26`
- Imported run path: `lab/cross_carrier_seam_proof_003/receiving_imports/contaminated_non_passage/execution-dcbec996f0bd43fbad21649ccce30c26`
- Summary path: `lab/cross_carrier_seam_proof_003/receiving_imports/contaminated_non_passage/execution-dcbec996f0bd43fbad21649ccce30c26/summary/summary.json`
- Receiver-local condition snapshot path: `lab/cross_carrier_seam_proof_003/receiving_imports/contaminated_non_passage/execution-dcbec996f0bd43fbad21649ccce30c26/package/receiver_local_condition_snapshot.json`
- Package id: `transfer-package-02af9dff5a6a44518c823d2957976490`
- Receiver-local condition status: `contaminated`
- Receiver-local governance admissible: `false`
- Technical receipt: `true`
- Package valid: `true`
- Ingress lawful: `false`
- Ingress outcome: `receiver_local_contamination_non_passage`
- Arrival status: `none`
- Refusal visible: `true`
- Non-passage: `true`
- Blocking condition: `receiver_local_parser_governance_contamination`
- Source fault: `false`
- `source_remains_source = true`
- `shared_authority = false`
- `standing_upgraded = false`

On the contaminated imported branch, the same valid package is still technically received, but lawful ingress is denied. Visible refusal and non-passage remain preserved, the blocking condition stays receiver-local, and source-side validity is not rewritten into source fault.

## Receiver-Local Embodiment Threshold

The specific advance in proof 003 is that contamination is no longer carried only as a scenario label. The proof now preserves a receiver-local condition surface and shows the same valid package yielding different lawful outcomes because the receiving-side local condition differs.

- Receiver-local embodiment supported in the current snapshot: `true`
- Same valid package across source and receiving sides: `true`
- Clean and contaminated condition statuses diverge: `true`
- Clean condition artifact id: `receiver-local-condition-859436d736ec47e7b56b1bcab2d3df04`
- Contaminated condition artifact id: `receiver-local-condition-6f2d72b5d9984e7bb1f9e4f21e5fc133`
- Top-level receiver-local condition artifact: `lab/cross_carrier_seam_proof_003/receiver_local_condition.json`
- Top-level receiver-local condition currently visible: `true`
- Top-level receiver-local parser status: `contaminated`
- Top-level receiver-local governance admissible: `false`
- Top-level receiver-local parser contaminated: `true`
- Import note path: `lab/cross_carrier_seam_proof_003/receiving_imports/IMPORT_NOTE.md`

The top-level receiver-local condition artifact remains an implementation-local surface only. It helps make receiver-local contamination visibly embodied rather than merely scenario-labeled, but it does not replace the imported receiving-side runs or convert them into protocol law.

The import note likewise remains a readability surface only. It preserves the fact that the clean and contaminated branches are imported receiving-side evidence, not source-side history.

In bounded terms: the same valid package `transfer-package-02af9dff5a6a44518c823d2957976490` ingresses lawfully under the clean receiver-local condition and fails lawfully with visible non-passage under the contaminated receiver-local condition.

## What This Shows

- Lawful derivative-only ingress is preserved on the clean receiving side under an admissible receiver-local condition.
- Source remains source across release and receiving-side ingress.
- No silent authority inheritance is required for the proof to remain legible.
- Technical receipt and lawful admissibility remain distinct rather than collapsing into one transport story.
- The same valid package can remain valid while receiver-local contamination blocks lawful ingress.
- Visible refusal and non-passage are preserved on the contaminated receiving side without false blame shift back to source.
- Imported receiving-side evidence remains receiving-side evidence even after it is carried back into the main body.

## What It Does Not Yet Show

- Not yet a multi-carrier mesh.
- Not yet bidirectional sync.
- Not yet shared canonical state.
- Not yet a relational field.
- Not yet an exhaustion of cross-carrier seam jurisprudence.
- Not yet a flattening of source-side and receiving-side evidence into one undifferentiated proof event.

## Boundary Note

This report is an additive human-readable companion to the machine-readable cross-carrier proof 003 snapshot. It does not replace the snapshot, it does not rewrite prior artifacts, it does not convert imported receiving-side evidence into source-side history, and it does not convert implementation-local readability into protocol law.
