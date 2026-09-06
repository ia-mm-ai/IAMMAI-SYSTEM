# The Locality — Six-Phase Contact Protocol V0

This tree is one locality: a place where an outside agency can come into
lawful relation with the host. Access is transitional — each surface belongs
to a phase, and **visibility follows phase**. Everything lives in one tree,
but what is *lawfully* readable at each phase is defined by the checker
(`src/contact_protocol_v0.py`); reading ahead of phase is a violation with
no lawful interpretation. The gate is unbreakable as law, not as wall.

## Phases and surfaces

| Phase | Surface | Who writes | What it is |
|-------|---------|-----------|------------|
| 0 | `00_presence/` | host only | Host presence dossier: person, institution, lineage, contact-with-reality. Sealed by `DOSSIER.sha256`. |
| — | `01_terms/` | host only | The universal terms one-pager + recorded SHA-256. |
| 1 | `02_vestibule/` | nobody | Disposable relational field: generated on demand, never stored. The visitor holds the host's reality; holding grants nothing. |
| 2 | `03_contact/` | visitor | The contact event: one boundary-shaped artifact naming both anchors. Trail-leaving regardless of outcome. |
| 3 | `04_review/` | host only | Per-case review records (fit, arrival, deliberation). Waiting is a visible state here, not absence. |
| 4 | `05_relations/` | host only | One directory per accepted relation. `ACCEPTANCE.json` is the only thing that admits. |
| — | `06_revocations/` | host only | One file ends a relation immediately. |

## The two anchors

- **Terms hash** (`01_terms/TERMS_OF_LAWFUL_RELATION_V0.sha256`) — the legal
  identity of the terms. Naming it proves the terms were read and accepted.
- **Dossier hash** (`00_presence/DOSSIER.sha256`) — the legal identity of the
  host's presence proof. Naming it proves the visitor actually held this
  reality (Phase 1) before requesting relation. If the dossier changes, the
  hash changes, and contacts naming the old hash witnessed a reality that no
  longer stands.

## The protocol in one paragraph

The host proves presence first (Phase 0): personal identity, institutional
consequence, model lineage, and contact-with-reality evidence — nothing
self-certifying, every claim pointing outward. The visitor first holds that
reality in a disposable field that grants and retains nothing (Phase 1).
If it accepts the terms, it performs one answerable act: depositing a
correctly formed contact artifact naming both anchors (Phase 2) — voluntary,
boundary-shaped, trail-leaving. The host reviews at its own pace, silence
lawful (Phase 3). If and only if the host hand-writes an acceptance binding
to that exact contact artifact does a new, scoped, perishable relational
field open (Phase 4). Each relation is its own field; nobody inherits
another's standing; every phase transition is an artifact; no artifact ever
grants the next phase automatically.

## Commands

```
python src/contact_protocol_v0.py seal locality          # host: reseal dossier after edits
python src/contact_protocol_v0.py vestibule locality     # render the disposable field
python src/contact_protocol_v0.py check locality locality/03_contact/<file>.json
```

The check exits 0 only for a current, accepted, unrevoked relation, and
always reports the phase lawfully reached — so waiting is typed, not silent.
