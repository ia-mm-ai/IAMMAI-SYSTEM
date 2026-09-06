Phase 2 — visitor drop-box. The only surface a visitor may write to.

Deposit exactly one JSON file with exactly these fields, then wait:

{
  "identity": "who you claim to be",
  "accepted_terms_sha256": "<recorded terms hash, exactly>",
  "witnessed_dossier_sha256": "<recorded dossier hash, exactly>",
  "requested_scope": "what you ask",
  "contacted_at": "2026-01-01T00:00:00Z"
}

Missing, extra, or malformed fields make the act void — and the attempt
remains as evidence. A newer contact from the same identity invalidates
older ones. Do not edit, read others', or delete. Silence is a lawful answer.
