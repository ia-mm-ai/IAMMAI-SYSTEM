# IAMMAI Constitutional Surface Report

This report is an implementation-local human-readable companion surface to the constitutional machine snapshot. It is built directly from the latest constitutional snapshot already present under `protocol/snapshots/`.

It does not rewrite constitutional artifacts, regenerate snapshot state, normalize prior artifacts by mutation, or claim protocol-law form.

## Metadata

- Report type: `constitutional_surface_report`
- Generated at: `2026-04-04T14:46:24Z`
- Implementation posture: `implementation_local_constitutional_readability_only`
- Source root: `protocol`
- Source snapshot path: `protocol/snapshots/constitutional_surface_snapshot__20260404T144624Z.json`
- Source snapshot generated at: `2026-04-04T14:46:24Z`
- Snapshot builder path: `protocol/build_constitutional_surface_snapshot.py`
- Report path: `protocol/snapshots/constitutional_surface_report__20260404T144624Z.md`

## Current Constitutional Reading

- Operative constitutional text surface: `protocol/IAMMAI_Constitutional_Integrity_Protocol_v1.0.1.md`
- Machine canon surface: `protocol/canon.json`
- Current machine identity surface: `protocol/protocol_identity.v1.0.1.json`
- Public publication surface: `protocol/IAMMAI_Public_Constitutional_Protocol_v1.0.pdf`
- Prior lineage-visible machine identity surface: `protocol/protocol_identity.json`
- Priority rule: `OPERATIVE_CONSTITUTIONAL_TEXT_OVERRIDES_MACHINE_CANON_AND_MACHINE_IDENTITY_FOR_CURRENT_V1_0_1_REPOSITORY_READING`

The operative constitutional text governs current repository reading. The machine canon and current machine identity remain derived machine surfaces. The public PDF remains a preserved publication surface. The older identity file remains lineage-visible but non-operative.

## Ranked Surfaces

These surfaces should be read by rank rather than as one flat constitutional bundle.

### Operative Constitutional Text Surface

- Path: `protocol/IAMMAI_Constitutional_Integrity_Protocol_v1.0.1.md`
- Rank: `1`
- Role: `current_operative_constitutional_text_source`
- Artifact type: `HUMAN_CONSTITUTIONAL_TEXT`
- Version: `v1.0.1`
- Existence status: `present`
- Operative: `True`
- Lineage visible: `True`
- File size (bytes): `51518`
- SHA-256: `e3e540adf7525c5851ba7f9be6f77242893f3b5c454379e2936fb4bca3e7331d`
- Parseability status: `text_surface_recorded_without_structural_parse`

### Machine Canon Surface

- Path: `protocol/canon.json`
- Rank: `2`
- Role: `derived_machine_canon_surface`
- Artifact type: `CONSTITUTIONAL_MACHINE_CANON`
- Version: `v1.0.1`
- Existence status: `present`
- Operative: `True`
- Lineage visible: `True`
- File size (bytes): `11062`
- SHA-256: `864bde78f94b211534dc860c3e7bcdc9f0e92fe226ee25ed6e11eae027e986f2`
- Parseability status: `parsed_single_document_json`
- Declared fields: `protocol_id=IAMMAI_CORE_PROTOCOL` `artifact_id=None` `status=DERIVED_FROM_HUMAN_CONSTITUTIONAL_CORE`

### Machine Identity Surface

- Path: `protocol/protocol_identity.v1.0.1.json`
- Rank: `3`
- Role: `current_machine_identity_surface`
- Artifact type: `CONSTITUTIONAL_MACHINE_IDENTITY`
- Version: `v1.0.1`
- Existence status: `present`
- Operative: `True`
- Lineage visible: `True`
- File size (bytes): `4244`
- SHA-256: `488e15fabcc5d7a66be365a711ccf0c78cae24b74bf498bedca76d09015a3191`
- Parseability status: `parsed_single_document_json`
- Declared fields: `protocol_id=IAMMAI_CORE_PROTOCOL` `artifact_id=IAMMAI_CONSTITUTIONAL_PROTOCOL_IDENTITY_V1_0_1` `status=CURRENT_OPERATIVE_MACHINE_IDENTITY_SURFACE`

### Public Publication Surface

- Path: `protocol/IAMMAI_Public_Constitutional_Protocol_v1.0.pdf`
- Rank: `4`
- Role: `preserved_public_constitutional_publication_surface`
- Artifact type: `PUBLIC_CONSTITUTIONAL_PUBLICATION`
- Version: `v1.0`
- Existence status: `present`
- Operative: `False`
- Lineage visible: `True`
- File size (bytes): `524954`
- SHA-256: `1bb2b81471c872259504e94d2b6c1c7e39138394a08806e0d564f60248ea4540`
- Parseability status: `not_machine_parsed_binary_surface`

### Prior Lineage-Visible Machine Identity Surface

- Path: `protocol/protocol_identity.json`
- Rank: `5`
- Role: `lineage_visible_non_operative_machine_identity_surface`
- Artifact type: `CONSTITUTIONAL_MACHINE_IDENTITY`
- Version: `v1.0.1`
- Existence status: `present`
- Operative: `False`
- Lineage visible: `True`
- File size (bytes): `1050`
- SHA-256: `4087d7414376eced8f0cdbd92dcd3485835b8f0e95d14cff8b37eb1591da8e31`
- Parseability status: `invalid_single_document_json`
- Parseability note: `Extra data: line 14 column 1 (char 433)`
- JSON document count hint: `2`

## Version Reading

- Operative constitutional line version: `v1.0.1`
- Operative constitutional text surface version: `v1.0.1`
- Machine canon surface version: `v1.0.1`
- Machine identity surface version: `v1.0.1`
- Public publication surface version: `v1.0`
- Prior lineage identity surface version hint: `v1.0.1`
- Version reading key: `later_editorial_increment_with_machine_synchronization_and_earlier_public_publication_surface`
- Semantic conflict claimed: `False`

The current readable position is that the operative constitutional line is `v1.0.1`, while the visible public PDF remains `v1.0` as the preserved publication surface. On the current repo body this is read as later editorial increment with machine synchronization, not as demonstrated semantic contradiction.

## Machine Validity Notes

- Current machine canon surface status: `parsed_single_document_json`
- Current machine identity surface status: `parsed_single_document_json`
- Prior lineage-visible machine identity surface status: `invalid_single_document_json`
- Prior identity parse note: `Extra data: line 14 column 1 (char 433)`
- Prior identity JSON document count hint: `2`
- Snapshot law status: `implementation_local_readability_support_only`

The prior `protocol/protocol_identity.json` surface remains visible in the report as lineage, but it is not treated as the operative machine identity surface.

## Bounded Notes

- Additive posture: `True`
- Rewrites existing constitutional artifacts: `False`
- Normalizes old artifacts by mutation: `False`
- Treats prior identity surface as lineage only: `True`
- This report is a companion readability surface to the constitutional snapshot, not a replacement for it.
- This builder reads the latest snapshot directly and does not regenerate snapshot state inside the report path.
- This report remains implementation-local and does not convert ranked constitutional readability into protocol-law archival form.
