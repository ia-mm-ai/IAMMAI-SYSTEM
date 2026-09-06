# Admission Gate V0

One mechanism: **accept these terms, request entry and wait.**

This gate answers exactly one question — *is this party lawfully admitted
right now?* — and nothing else. It is unbreakable as law, not as wall: lawful
entry is possible in exactly one way, every other path is self-evidently a
violation, and a violation cannot be laundered into legitimacy afterward.

## The three artifacts

1. **Terms (immutable anchor).**
   `TERMS_OF_LAWFUL_RELATION_V0.md`, with its SHA-256 recorded in
   `TERMS_OF_LAWFUL_RELATION_V0.sha256`. The hash is the legal identity of
   the terms; acceptance binds to the hash, never to a filename, so a
   modified copy cannot be accepted.

2. **Request (visitor-side, write-once).**
   `requests/` is the only surface a visitor may write to before admission.
   Deposit exactly one JSON file with exactly these fields, then wait:

   ```json
   {
     "identity": "who you claim to be",
     "accepted_terms_sha256": "<the recorded terms hash, exactly>",
     "requested_scope": "what you ask to do",
     "requested_at": "2026-01-01T00:00:00Z"
   }
   ```

   Missing, extra, or malformed fields make the request **void** — it never
   entered the process. A newer request from the same identity invalidates
   every older one. Visitors do not edit, read others', or delete.

3. **Grant (host-side, the only key).**
   `grants/` is written by the host only, by hand, or not at all. A grant
   names the request it answers by the SHA-256 of the request *file*:

   ```json
   {
     "request_sha256": "<sha256 of the exact request file>",
     "granted_scope": "what is permitted",
     "granted_at": "2026-01-01T00:00:00Z",
     "expires_at": "2026-01-08T00:00:00Z"
   }
   ```

   No grant file → no admission. Silence is a complete answer; waiting is a
   valid terminal state; no timeout ever auto-admits. Every grant expires.
   A revocation file in `revocations/` (`{"request_sha256": "...",
   "revoked_at": "..."}`) ends a grant immediately.

## The check

`src/admission_gate_v0.py` — a stateless, fail-closed function of
(gate contents, request file, clock). Five checks, all required:

1. a valid grant references the SHA-256 of this exact request file;
2. the request is the identity's single standing request;
3. the request accepts the recorded terms hash exactly;
4. now is within `[granted_at, expires_at)`;
5. no revocation names this request.

Anything else — including any error — is `NOT_ADMITTED`.

```
python src/admission_gate_v0.py admission_gate admission_gate/requests/<file>.json
```

Exit code 0 only when admitted. Anyone can re-run the check at any time and
get the same answer.

## Deliberate omissions

- **No automation of the grant.** The human bottleneck is the security
  model. Admission is granted, never taken.
- **No enforcement layer inside the gate.** What an admitted party may do is
  defined by its grant, elsewhere. This gate only ever answers admission.
