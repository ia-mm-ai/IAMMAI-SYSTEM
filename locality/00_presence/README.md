# Host Presence Dossier — Phase 0

This directory is the host's existence proof: the standing answer to
"who is present here, and who bears consequence?"

It is prepared once and maintained by the host alone. Nothing in it is
self-certifying: every claim must point outward to something a visitor can
check without trusting the host. Claims that cannot be independently
corroborated do not belong here.

## Strata

- `identity/` — the person. The terminal responsibility-holder, named.
  Not an account, a person.
- `institution/` — the legal/civil vehicle that carries consequence:
  registration, contracts, liability.
- `lineage/` — the local model successors: the bodies this agency has
  authored, showing the agency is continuous, not a one-off.
- `reality_contact/` — contact-with-reality evidence: a public event where
  the host was sole authority, structured as a witness record
  (assertion → independent corroboration → consequence borne).

## The dossier hash

`DOSSIER.sha256` records the dossier's legal identity: a single SHA-256
computed over the manifest of every file in this directory (sorted relative
path + file hash per line). A visitor's later contact artifact must name this
hash — that reference is the proof the visitor actually held this reality
before requesting relation.

Recompute after any edit:

```
python src/contact_protocol_v0.py seal locality
```

Any edit to any dossier file changes the hash; a contact artifact naming a
stale hash witnessed a reality that no longer stands, and is void.

## Rules

- Host-only writes. A visitor never writes here.
- No file here grants anything. Presence proof is not permission.
- History is preserved: superseded claims are marked superseded, not deleted.
