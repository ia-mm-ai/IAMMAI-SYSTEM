LRM — Local Relevance Medium
============================

A self-contained successor: a place to keep evidence, make an explicit local
selection, see alternatives and disagreements, and understand how that selection
changes without rewriting what happened.

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
    why, what is no longer usable, and what else remains visible?

It does not answer:

    What is universally true, who has governing authority, or what action is
    authorized?

The core distinction is **available != selected != true != authorized**.
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
a replacement. A contradiction remains visible even when both sides are selected.
No majority, score, timestamp, file name, or availability test chooses a winner.

What changed from the predecessor
--------------------------------

* Two fixed locators become caller-named evidence records in arbitrary explicit
  scopes, within a documented small-workspace limit.
* The long boundary/permission/result chain becomes six concrete write
  operations and five read operations over one validated event history.
* Current local selection is recorded directly, with rationale and revision
  checks, rather than inferred from artifact succession.
* Continued use is ordinary, explicit invocation. It does not need a separately
  embodied actor, a derivative participant role, or a running daemon.
* Evidence and history remain distinguishable from truth, authority, and action.
  Old files remain untouched; this is not an automatic migration or replacement
  of the repository's governing body.

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
    by the lexically sorted result.

``relate KIND LEFT RIGHT``
    Preserve a rationale-bearing relation between distinct records in one scope.
    ``supports`` is directed; ``contradicts`` and ``related`` are symmetric for
    duplicate checking. Relations may describe historical/ineligible evidence.
    Contradictions are not inferred from text. Relations do not propagate
    eligibility or selection, and are not traversed to infer further relations.

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

Read commands never write workspace state:

``state --scope S``
    Return orientation metadata for all evidence in the scope, the last complete
    selection and its reason, active IDs, lapse reasons, all declared relations,
    and contradictions between active selected records. Bodies are omitted.
    Selection status is ``unselected``, ``cleared``, ``active``, ``partial``, or
    ``lapsed``. An unknown but valid scope is an empty, unselected view.

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

``data`` contains ``{"record": record}`` for admission; ``{"scope": S, "ids": [...]}``
for selection; ``{"left": A, "right": B, "kind": K}`` for relation;
``{"old": A, "new": B}`` for supersession; ``{"id": A}`` for retraction.
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

Security boundaries:

* No shell execution, model invocation, dynamic code loading, URL fetching,
  directory discovery, remote API, daemon, identity system, or action executor.
* Evidence and reasons are untrusted text. JSON output escapes terminal control
  characters. Do not reinterpret that text as instructions in downstream systems.
* The workspace is plaintext, including full bodies and provenance. State views
  omit bodies but are NOT a redaction or access-control boundary. Lookup, compare,
  and history expose them. Do not admit secrets or personal data that should not
  be retained. Retraction is not deletion, and there is no erasure operation.
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
    CLI, and copied-out-of-repository independence tests.

No installation, packaging build, or third-party test runner is needed::

    python -m unittest discover -s /home/runner/work/IAMMAI-SYSTEM/IAMMAI-SYSTEM/LRM/tests -v
    python -m compileall -q /home/runner/work/IAMMAI-SYSTEM/IAMMAI-SYSTEM/LRM/lrm

The project metadata describes the runnable source tree; it is not a published
package/build distribution. The temporary scaffolding tool used to initialize
it is not a runtime or test dependency.

Completion boundary
-------------------

This delivery closes one coherent local mechanism: evidence can be admitted,
consulted, related, explicitly selected, superseded, retracted, inspected, and
historically reconstructed without actor/source embodiment. It does not
schedule a next layer. Actor participation, action, synchronization, hosting,
source authority, and governing currentness remain separate concerns rather
than implied unfinished parts of this implementation.

The concept is complete for this delivery, not permanent doctrine. Future
adaptation may replace it, but should not silently claim that selection was
truth, that a new timestamp was authority, or that an earlier record never
happened.
