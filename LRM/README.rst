LRM — Local Relevance Medium
============================

A self-contained successor, version 0.2: continuing local memory with explicit
selection, bounded temporary consultation, correction, and regulation. Memory
can continue when a consultation ends; continued memory does not imply continued
presence.

This is a working Python library and command-line application, not another
sequence of permission specifications. It requires Python 3.12+ with SQLite and
no third-party packages, network access, actor runtime, credentials, or source
authority. Copying this folder is sufficient. The predecessor material informed
the design; none of its modules, artifacts, identifiers, or terminal summaries
is loaded or required.

Concept
-------

The medium answers:

    What evidence is available for this scope, what was explicitly selected,
    why, what is no longer usable, and what else remains visible? Can a bounded
    local consultation begin, and has that particular consultation stopped?

It does not answer:

    What is universally true, who has governing authority, or what action is
    authorized?

The core distinction is
**remembered != selected != presently consulted != true != authorized**.
An admitted record is available evidence, not accepted truth. An explicit
selection is a local choice of material to consult, not an authority transfer.
A relation is a declared relationship, not a discovered fact. Even a selected
record with no lapse conditions is not certified correct.

Currentness is relational, not "latest wins"
------------------------------------------

There is no universal ``current`` flag attached to a record. A view is evaluated
against a named scope, the recorded selection for that scope, the journal
revision, and a time. Newer observations never replace selected observations
just because they are newer. Selection never makes alternatives disappear.

``active_ids`` means **explicitly selected and not locally ineligible at the
evaluation time**. It is deliberately not called constitutional currentness,
governing standing, verified truth, or action permission. LRM operationalizes a
narrow local consultation relation; it does not purport to resolve IAMMAI's
authority-bearing currentness.

The selection can be replaced or cleared explicitly. Retraction, supersession,
and declared expiry can make selected material lapse, without quietly selecting
a replacement. An unwithdrawn contradiction remains visible even when both sides
are selected.
No majority, score, timestamp, file name, or availability test chooses a winner.

Durable memory, disposable consultation
---------------------------------------

The continuing local body consists of evidence, selections, relation declarations,
regulation, and their journal. A **consultation** is a separate, finite local use
of one selected set. It has its own ID, selected scope/IDs/revision, basis head
hash, opening rationale, and mandatory expiry no more than 24 hours away.
Opening does not start a process, invoke an actor, or host a shared runtime.

The read-side ``presence`` is exactly integer ``1`` when that consultation is
open, before expiry, not invalidated, and all its pinned evidence remains
eligible; otherwise it is integer ``0``. This is a description of a **local
consultation's availability**, not observation or certification of anyone's
physical presence, identity, participation, jurisdiction, or source standing.
Not finding a consultation is an error, not invented evidence of absence.

When presence is zero, ``consultation`` returns lifecycle metadata and reasons
but no record bodies or relation packet. When it is one, the complete pinned
set is returned; there is no partial packet, implicit substitute, or promotion of
new evidence. The packet is a view, not an execution capability/token.

Scope regulation is orthogonal to memory:

* ``held`` stops existing consultations of that scope, refuses new ones, and
  refuses nonempty selections. Clearing selection, recording evidence,
  correcting/withdrawing claims, and closing consultations remain possible.
* ``open`` releases that hold. It does not revive stopped consultations, clear
  an earlier invalidation, select a replacement, or create presence.
* Hold does not retract evidence. ``state.active_ids`` still means eligible
  selected memory, not permission to use it; check ``regulation`` separately.
* Lookup, comparison, and history remain available for inspection and correction.
  Regulation is a local workflow rule, **not an access-control boundary**.

Closing one consultation leaves the source evidence, selected set, other
consultations, and history intact. The ID cannot be reused or renewed in place.
Further consultation requires a fresh, explicit opening. Selection replacement
(even with identical IDs), a scope hold, or retraction/supersession of pinned
evidence invalidates a still-open, unexpired consultation. Releasing a hold or
later reselecting the old IDs cannot reverse that invalidation.

All presence is evaluated for the requested historical view. A historical
``presence=1`` does not mean it is present now. Expiry needs no background timer
or expiry event: the next view observes it. Returned packets are point-in-time
data; LRM cannot recall copies or stop external work already started by a caller.

How the broader reference was used
----------------------------------

The SOURCE/NUCLEUS/FORM/FIELD account supplied a useful distinction, not an
implementation dependency or a governing basis:

* **Continuing local state and memory:** the workspace survives process exit and
  a temporary consultation's closure.
* **Capability:** inspection describes the functions this software implements
  and current local blockers, not a source's inherent capacity or permission.
* **Regulation:** local use can be held, released, or ended without destroying
  the underlying memory.
* **Temporary presence:** an expiring consultation has a precise local 1/0
  status, independent of persistent evidence.
* **Interface:** the CLI and Python API are ways to use this body, not its source
  identity or constitutional embodiment.

LRM does **not** implement t-SOURCE activation, NUCLEUS embodiment, FIELD hosting,
cross-jurisdiction admission, participant authentication, or the right of one
participant to control another. It requires none of these to run. Any external
FIELD integration would have to establish its own admission and withdrawal
rules; a local consultation is not proof that those rules were satisfied.

What changed from the predecessor
--------------------------------

* Two fixed locators become caller-named evidence records in arbitrary explicit
  scopes, within a documented small-workspace limit.
* The long boundary/permission/result chain becomes nine journal operations and
  seven read operations over one validated event history, plus initialization.
* Current local selection is recorded directly, with rationale and revision
  checks, rather than inferred from artifact succession.
* Continued use is ordinary, explicit invocation. It does not need a separately
  embodied actor, a derivative participant role, or a running daemon.
* Evidence and history remain distinguishable from truth, authority, and action.
  Old files remain untouched; this is not an automatic migration or replacement
  of the repository's governing body.
* Relative to LRM 0.1, durable selection and temporary consultation are now
  separate. Scope holds and explicit exit regulate the latter, while relation
  withdrawal makes mistaken interpretations correctable without erasure.

Quick start
-----------

All commands below use an explicit disposable workspace outside the repository.
Do not reuse an existing file for ``init``::

    cd /home/runner/work/IAMMAI-SYSTEM/IAMMAI-SYSTEM/LRM
    WORK="$(mktemp -d)"
    DB="$WORK/garden.sqlite"

    python -m lrm --db "$DB" init
    python -m lrm --db "$DB" admit /home/runner/work/IAMMAI-SYSTEM/IAMMAI-SYSTEM/LRM/examples/observation.json --expect 0 --reason "Record the first observation"
    python -m lrm --db "$DB" admit /home/runner/work/IAMMAI-SYSTEM/IAMMAI-SYSTEM/LRM/examples/alternative.json --expect 1 --reason "Preserve a different account"
    python -m lrm --db "$DB" relate contradicts soil-dry soil-wet --expect 2 --reason "These accounts differ on the same subject"
    python -m lrm --db "$DB" select --scope garden soil-dry soil-wet --expect 3 --reason "Consult both without settling the disagreement"
    python -m lrm --db "$DB" state --scope garden
    python -m lrm --db "$DB" compare soil-dry soil-wet

The state has both IDs active and one declared conflict. It has no winner.
Observation timestamps in these fixtures are illustrative, not freshness claims.

An explicit replacement does not silently transfer selection::

    python -m lrm --db "$DB" supersede soil-dry soil-wet --expect 4 --reason "Local review replaces the first account"
    python -m lrm --db "$DB" state --scope garden
    python -m lrm --db "$DB" select --scope garden soil-wet --expect 5 --reason "Narrow the consultation set explicitly"
    python -m lrm --db "$DB" retract soil-wet --expect 6 --reason "Withdraw reliance pending another observation"
    python -m lrm --db "$DB" state --scope garden
    python -m lrm --db "$DB" lookup soil-dry
    python -m lrm --db "$DB" history
    python -m lrm --db "$DB" verify

After retraction there is no active selection. Both records, all reasons, and
the previous selections are still inspectable. Nothing falls back to the old
record. To clear a selection deliberately, use ``select --scope garden`` with
no IDs, the latest ``--expect`` revision, and a reason.

Temporary consultation example
-------------------------------

Use a fresh workspace for this sequence::

    cd /home/runner/work/IAMMAI-SYSTEM/IAMMAI-SYSTEM/LRM
    WORK="$(mktemp -d)"
    DB="$WORK/consultation.sqlite"
    UNTIL="$(python -c 'from datetime import datetime,timedelta,timezone; print((datetime.now(timezone.utc)+timedelta(hours=1)).isoformat())')"
    python -m lrm --db "$DB" init
    python -m lrm --db "$DB" admit /home/runner/work/IAMMAI-SYSTEM/IAMMAI-SYSTEM/LRM/examples/observation.json --expect 0 --reason "Keep the observation"
    python -m lrm --db "$DB" select --scope garden soil-dry --expect 1 --reason "Select local consultation material"
    python -m lrm --db "$DB" capabilities --scope garden
    python -m lrm --db "$DB" open-consultation visit-1 --scope garden --until "$UNTIL" --expect 2 --reason "A temporary local review"
    python -m lrm --db "$DB" consultation visit-1
    python -m lrm --db "$DB" regulate held --scope garden --expect 3 --reason "Pause local use"
    python -m lrm --db "$DB" consultation visit-1
    python -m lrm --db "$DB" close-consultation visit-1 --expect 4 --reason "End this consultation on local terms"
    python -m lrm --db "$DB" regulate open --scope garden --expect 5 --reason "Allow fresh consultation"
    python -m lrm --db "$DB" consultation visit-1
    python -m lrm --db "$DB" state --scope garden

``presence`` first reads 1, then 0 after the hold, and remains 0 after release.
The observation and selection remain in memory. A new ID and opening are needed
for any new consultation; releasing regulation does not create one.

Record contract
---------------

``admit`` reads one UTF-8 JSON object. Required fields:

================  ==============================================================
Field             Meaning
================  ==============================================================
``id``            Caller-chosen, workspace-unique immutable evidence ID.
``scope``         Exact, case-sensitive local context ID.
``subject``       Short subject within that scope; not a globally resolved entity.
``body``          Plain text, preserved literally as evidence.
``provenance``    Object with ``origin`` and ``basis`` strings.
``observed_at``   Declared observation time, not later than admission time.
================  ==============================================================

``origin`` describes where the material came from; ``basis`` says why it is
relevant here. These are declarations, not authentication or proof. Origins are
never dereferenced: a path or URL is text, not permission to read or fetch it.
LRM does not need the source or actor to be present.

Optional ``valid_from`` and ``valid_until`` define a declared half-open
consultation interval: start inclusive, end exclusive. Omission or JSON null
means that end is unbounded. Without such an interval, age alone never expires
evidence. "Valid" here means within a caller-declared temporal window, not true.
A time-dependent claim should have an appropriate interval chosen by its owner.

IDs/scopes are 1–128 ASCII characters, starting with a letter or digit and then
allowing letters, digits, ``.``, ``_``, ``:``, and ``-``. Subjects are limited to
256 characters, origins to 2,048, basis/reasons to 4,096, bodies to 32,768.
Empty/whitespace-only required strings are rejected. Unknown fields, duplicate
JSON keys, non-finite numbers, invalid Unicode, and malformed types are rejected.
This is a closed contract, not a general JSON document store.

Timestamps must include date, seconds, and an explicit UTC offset, with up to
six fractional digits. They are normalized to UTC. The local clock supplies
journal timestamps; a write that would move the clock backwards is rejected.
A default read also refuses a clock earlier than the stored journal head,
rather than silently presenting historical state as current. There is no
trusted external time source.

Operation contract
------------------

Every write takes ``--expect N`` and ``--reason TEXT``. ``N`` is the last observed
``head_revision``, initially zero. A successful write returns the new revision
and head hash. A stale revision fails rather than losing someone else's update.
Read the workspace again and consciously decide before retrying.
Use a fresh default read to establish this precondition, not the head metadata
attached to a deliberately historical projection.

``admit FILE``
    Preserve a new immutable evidence record. Never select it implicitly.
    Duplicate IDs are errors, including identical re-submission. A corrected
    record needs a new ID.

``select --scope S [ID ...]``
    Replace that scope's entire consultation set. IDs must be distinct, known,
    in the same scope, and eligible at commit time. An empty set clears it.
    Re-selection can record an explicit reaffirmation. No ranking is implied
    by the lexically sorted result. While the scope is held only an empty
    selection is accepted. Replacing or clearing the set invalidates previous
    live consultations; reaffirming identical IDs is still a new selection.

``relate KIND LEFT RIGHT``
    Preserve a rationale-bearing relation between distinct records in one scope.
    ``supports`` is directed; ``contradicts`` and ``related`` are symmetric for
    duplicate checking. Relations may describe historical/ineligible evidence.
    Contradictions are not inferred from text. Relations do not propagate
    eligibility or selection, and are not traversed to infer further relations.
    The declaring event's revision identifies the relation for correction.

``withdraw-relation REVISION``
    Withdraw that particular relation declaration with a reason. The original
    stays visible, annotated with its withdrawal; it no longer contributes to
    active conflicts. Neither endpoint is retracted. A new declaration of the
    same relation is allowed under a new revision; withdrawing an old declaration
    cannot withdraw a newer one. Unknown/non-relation revisions and repeated
    withdrawals are errors.

``supersede OLD NEW``
    Record replacement between records with exactly the same scope and subject.
    OLD must not already be superseded/retracted; NEW must be eligible.
    OLD becomes ineligible. NEW is not selected unless explicitly selected.
    Supersession chains cannot cycle because an ineligible record cannot be a
    replacement. Supersession does not mean the earlier observation never existed.

``retract ID``
    Mark a known record ineligible while preserving it. Retraction is permanent
    for this record ID. Retraction of a superseded record is allowed; both reasons
    remain visible. Renewed evidence requires a new ID and explicit selection.

``regulate held|open --scope S``
    Record the scope's regulation state and rationale. The initial implicit state
    is open, including for an empty scope. Setting the existing status is an error.
    Holding invalidates live consultations of this scope only; release permits
    fresh openings, not revival. A held scope still permits memory/correction
    operations and explicit closure.

``open-consultation ID --scope S --until RFC3339``
    Pin the complete, nonempty, currently eligible selected set in an open scope.
    Record the selection revision and preceding journal revision/hash as its
    basis. Expiry must be strictly later than commit time and no more than 24 hours
    away. No future scheduling, auto-renewal, or reopening of old IDs exists.
    Unrelated admissions or changes to another scope do not stop this consultation.

``close-consultation ID``
    End one known consultation explicitly. Closure remains possible when held,
    invalidated, or expired; a second closure is an error. This does not require
    fresh evidence, a release, or an outside participant's approval. Normal
    database integrity and optimistic-revision checks still apply. Each opening
    reserves one future journal slot for its closure; other operations cannot
    consume these slots. This remains a local record of exit, not a safety-critical
    external cancellation mechanism.

Read commands never write workspace state:

``state --scope S``
    Return orientation metadata for all evidence in the scope, the last complete
    selection and its reason, active IDs, lapse reasons, all declared relations,
    and contradictions between active selected records. Bodies are omitted.
    Selection status is ``unselected``, ``cleared``, ``active``, ``partial``, or
    ``lapsed``. Regulation and consultation lifecycle summaries are separate
    fields; a held scope may retain an active memory selection. Withdrawn
    relations remain visible but are excluded from active conflicts. An unknown
    but valid scope is an empty, unselected view.

``lookup ID``
    Return the full evidence record, its content hash, admission revision,
    selection flag, ineligibility reasons, and supersession/retraction details.
    Unknown or not-yet-admitted IDs are errors, not empty invented records.

``compare LEFT RIGHT``
    Return both records, equal/different field names, and their declared
    relations. Requires distinct records in one scope. No semantic analysis,
    relevance score, validity judgment, or preferred record is produced.

``history``
    Return the full visible ordered event history, including reasons and bodies.
    This is also a portable JSON audit export; it is not an executable replay
    request or an import format.

``verify``
    Validate the entire stored journal's format, sequence, hashes, and operation
    semantics. Reports what was checked, not that its claims are true.

``consultation ID``
    Return the pinned scope/IDs, selection revision, basis revision/hash, opening,
    invalidation/closure evidence, expiry, integer presence, and stop reasons.
    Only presence 1 yields record and relation data. Relations are evaluated at
    the read's view, including corrections; the selected evidence set, not an
    entire historical relation graph, is pinned. Declared disagreements do not
    automatically terminate consultation or choose a winner.

``capabilities [--scope S]``
    Describe supported operations, accepted event formats, and size/duration
    limits. With a scope, include its regulation, selection revision, and local
    opening blockers (held, no selection, lapsed selection, event limit, or
    capacity reserved for exits). Report used, reserved, and unreserved event
    capacity separately.
    This is descriptive: it is neither a grant nor a promise that a later write
    will succeed. IDs, deadlines, event size, current revision, and storage state
    are checked on the actual write.

Read commands accept ``--at RFC3339``. The default is the local invocation time.
The default evaluation time is sampled after establishing the database snapshot,
so a concurrent update cannot be included in its revision but hidden by an
earlier automatically chosen time cutoff.
Only events recorded at or before that time enter the projection, and declared
validity is evaluated at that same time. Thus a later retraction does not rewrite
an earlier view. At equal timestamps, journal sequence determines event order.
A future ``--at`` is a projection of already-recorded knowledge, not a prediction
or a scheduled command.

Each read returns ``as_of``, the visible ``revision``/``view_hash``, and the full
stored ``head_revision``/``head_hash``. The latter may advance after the historical
cutoff. For the same stored prefix and evaluation time, the projected content
is deterministic; full-head metadata can change as the workspace grows. Integrity
validation always covers the entire stored journal, even for historical reads.

Library use
-----------

Run from this folder or put it on Python's module search path. The public API is
``from lrm import Workspace, LRMError``:

* ``Workspace.create(path)`` initializes a new file; it refuses an existing path.
* ``Workspace(path)`` opens an existing workspace on each operation.
* ``append(action, data, reason=..., expected_revision=...)`` performs one write.
* ``read(operation, scope=..., record_id=..., left=..., right=..., at=...)``
  returns a detached JSON-compatible result.
  ``consultation`` additionally takes ``consultation_id=...``; ``capabilities``
  takes an optional ``scope``.

``data`` contains ``{"record": record}`` for admission; ``{"scope": S, "ids": [...]}``
for selection; ``{"left": A, "right": B, "kind": K}`` for relation;
``{"old": A, "new": B}`` for supersession; ``{"id": A}`` for retraction.
For regulation use ``{"scope": S, "status": "held"}`` (or ``"open"``);
for opening use ``{"id": C, "scope": S, "until": timestamp}``;
for closure use ``{"id": C}``; for relation withdrawal use ``{"revision": N}``.
There are no constructor side effects and no environment-dependent default
workspace. API misuse raises ``LRMError``; filesystem errors may raise ``OSError``.
The CLI reports operational errors as JSON on stderr with exit code 2. Successful
commands emit JSON on stdout with exit code 0; argparse usage errors use its
standard text diagnostics and exit code 2.

Storage and trust boundary
--------------------------

One owner-controlled local SQLite file contains a format marker and append-only
events. Every event has a sequence, UTC timestamp, action/data, rationale, and
previous-event SHA-256; the row also stores the event hash. Canonical JSON and
semantic replay are checked on every operation. SQL triggers reject direct
event UPDATE/DELETE. Writes run in an immediate transaction with a revision
check; rejected operations leave no partial event. Reads use SQLite read-only
mode. SQLite supplies transactional durability; this is not a home-grown log
locking or crash-recovery implementation.

The design intentionally targets small workspaces: at most 10,000 events and
128 KiB of encoded JSON per input/event. Replay is linear in history length
(some relation/selection validation also scans current collections), and all
evidence is held in memory while projecting. There is no compaction, pruning,
automatic rollover, search index, retention policy, or limitless-throughput claim.
At the limit, reads remain available and writes are refused.
One slot is reserved for each not-yet-explicitly-closed consultation, including
expired or invalidated ones. Ordinary writes stop before consuming those slots,
so an existing consultation can still record its exit. Close finished
consultations to discharge these reservations; expiry alone does not release
them. Opening needs room for both its event and its eventual closure.
Consultation snapshots are reconstructed from the journal; they retain pinned
IDs, not additional copies of evidence bodies. Consultation summaries and history
remain after closure. "Disposable" refers to the use relation, not audit erasure.

Compatibility with 0.1
----------------------

Existing SQLite ``LRM/1`` journals require no migration, rewrite, or predecessor
repository. Their event bytes, sequence, hashes, evidence, and original selection
semantics remain intact. Without new lifecycle operations, old behavior remains.
Read projections gain regulation/consultation fields and relation-withdrawal
annotations; consumers that require exact output keys must account for these
additive fields.

The container marker remains ``LRM/1``. The five original actions keep event
``format: 1``; the four new actions require ``format: 2``. Both are validated and
replayed in sequence. Version 0.1 readers correctly refuse a journal after a
format-2 event rather than silently ignoring regulation. Keep a backup before
using the new operations if an older reader is still needed. ``capabilities``
identifies the 0.2 contract and supported event versions.

Security boundaries:

* No shell execution, model invocation, dynamic code loading, URL fetching,
  directory discovery, remote API, daemon, identity system, or action executor.
* Evidence and reasons are untrusted text. JSON output escapes terminal control
  characters. Do not reinterpret that text as instructions in downstream systems.
* The workspace is plaintext, including full bodies and provenance. State views
  omit bodies but are NOT a redaction or access-control boundary. Lookup, compare,
  and history expose them. Do not admit secrets or personal data that should not
  be retained. Retraction is not deletion, and there is no erasure operation.
  Neither ``presence=0`` nor a scope hold hides data from owner-level inspection
  or invalidates a packet already returned. Historical reads can still reconstruct
  earlier consultation contents. This is not an external revocation protocol.
* New workspace files are owner-readable/writable on POSIX. Keep the workspace
  and its parent directory under owner control. Do not operate on adversarial
  database files or attacker-writable directories; simple symlink refusal is
  not a filesystem sandbox. Back up a closed/quiescent database using normal
  SQLite-safe procedures.
* Hashes detect accidental/inconsistent changes, not authorship or malicious
  rewriting by someone who controls the database. They cannot by themselves
  detect removal of a valid suffix, replacement of the whole file, or a
  consistently recomputed forged history. An independently retained revision
  and head hash can serve as an external checkpoint; LRM does not host a trust
  service or authenticate that checkpoint.
* ``--reason`` is rationale, not authorization. Anyone with write access can
  make local selections. External authorization, source verification, and any
  consequences of consultation remain outside this application's contract.

Structure and verification
--------------------------

``lrm/model.py``
    Closed input contracts, canonicalization, event validation, and projection.

``lrm/store.py``
    SQLite transactions, integrity replay, revision checks, and time-bound reads.

``lrm/cli.py`` / ``lrm/__main__.py``
    Explicit local JSON command interface.

``examples/``
    Two illustrative conflicting observations.

``tests/test_lrm.py``
    Standard-library unit, persistence, concurrency, integrity, historical-view,
    CLI, copied-out-of-repository independence, regulation, presence lifecycle,
    relation correction, and legacy-journal compatibility tests.

No installation, packaging build, or third-party test runner is needed::

    python -m unittest discover -s /home/runner/work/IAMMAI-SYSTEM/IAMMAI-SYSTEM/LRM/tests -v
    python -m compileall -q /home/runner/work/IAMMAI-SYSTEM/IAMMAI-SYSTEM/LRM/lrm

The project metadata describes the runnable source tree; it is not a published
package/build distribution. The temporary scaffolding tool used to initialize
it is not a runtime or test dependency.

Completion boundary
-------------------

This delivery closes one coherent local mechanism: evidence can be admitted,
related, explicitly selected, superseded, retracted, inspected, and historically
reconstructed; interpretations can be withdrawn; local use can be held or
released; temporary consultation can open and end independently of memory.
All of this works without actor/source embodiment. It does not
schedule a next layer. Actor participation, action, synchronization, hosting,
source authority, and governing currentness remain separate concerns rather
than implied unfinished parts of this implementation.

The concept is complete for this delivery, not permanent doctrine. Future
adaptation may replace it, but should not silently claim that selection was
truth, that a new timestamp was authority, or that an earlier record never
happened.
