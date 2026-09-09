"""Transactional, append-only local history with read-only projections."""

from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Iterator

from .model import (
    LRMError, MAX_EVENT_BYTES, MAX_EVENTS, Projection, canonical, digest,
    normalize_operation, now, parse_json, text, timestamp, validate_event,
)

FORMAT = "LRM/1"


class Workspace:
    """One owner-controlled SQLite file; no upstream runtime or network needed."""

    def __init__(self, path: str | Path, *, clock: Callable[[], str] = now):
        self.path = Path(path).absolute()
        self.clock = clock

    @classmethod
    def create(cls, path: str | Path) -> Workspace:
        workspace = cls(path)
        try:
            with workspace.path.open("xb"):
                pass
        except FileExistsError as exc:
            raise LRMError("workspace already exists; initialization never overwrites") from exc
        try:
            workspace.path.chmod(0o600)
            with workspace._connection(write=True, initialized=False) as connection:
                connection.execute("CREATE TABLE metadata (format TEXT NOT NULL)")
                connection.execute("INSERT INTO metadata VALUES (?)", (FORMAT,))
                connection.execute(
                    "CREATE TABLE events (sequence INTEGER PRIMARY KEY, body TEXT NOT NULL, digest TEXT NOT NULL)"
                )
                connection.execute(
                    "CREATE TRIGGER no_event_update BEFORE UPDATE ON events "
                    "BEGIN SELECT RAISE(ABORT, 'events are immutable'); END"
                )
                connection.execute(
                    "CREATE TRIGGER no_event_delete BEFORE DELETE ON events "
                    "BEGIN SELECT RAISE(ABORT, 'events are immutable'); END"
                )
        except Exception:
            workspace.path.unlink(missing_ok=True)
            raise
        return workspace

    @contextmanager
    def _connection(self, *, write: bool = False, initialized: bool = True) -> Iterator[sqlite3.Connection]:
        if self.path.is_symlink() or not self.path.is_file():
            raise LRMError("workspace must be an existing regular file, not a symlink")
        mode = "rw" if write else "ro"
        connection = None
        try:
            connection = sqlite3.connect(self.path.as_uri() + f"?mode={mode}", timeout=5)
            connection.execute("PRAGMA trusted_schema=OFF")
            connection.execute("BEGIN IMMEDIATE" if write else "BEGIN")
            if initialized:
                metadata = connection.execute("SELECT format FROM metadata LIMIT 2").fetchall()
                if metadata != [(FORMAT,)]:
                    raise LRMError("not a supported LRM workspace")
            yield connection
            connection.commit()
        except sqlite3.Error as exc:
            raise LRMError("workspace database is invalid, locked, or unavailable") from exc
        finally:
            if connection is not None:
                connection.close()

    @staticmethod
    def _replay(connection: sqlite3.Connection) -> tuple[Projection, list[dict]]:
        projection, events = Projection(), []
        rows = connection.execute(
            "SELECT sequence, body, digest FROM events ORDER BY sequence LIMIT ?", (MAX_EVENTS + 1,)
        )
        for sequence, body, stored_digest in rows:
            if len(events) >= MAX_EVENTS:
                raise LRMError("workspace event limit exceeded")
            if not isinstance(body, str):
                raise LRMError("event body must be JSON text")
            event = parse_json(body)
            validate_event(event, projection)
            if sequence != event["sequence"] or body != canonical(event) or stored_digest != digest(event):
                raise LRMError("event integrity check failed")
            projection.apply(event)
            events.append(event)
        return projection, events

    def append(self, action: str, data: dict, *, reason: str, expected_revision: int) -> dict:
        """Commit one operation, or leave the entire workspace unchanged."""
        if type(expected_revision) is not int or expected_revision < 0:
            raise LRMError("expected_revision must be a nonnegative integer")
        data = normalize_operation(action, data)
        reason = text(reason, "reason")
        with self._connection(write=True) as connection:
            projection, _ = self._replay(connection)
            if projection.revision != expected_revision:
                raise LRMError(f"revision conflict: expected {expected_revision}, found {projection.revision}")
            if projection.revision >= MAX_EVENTS:
                raise LRMError("workspace event limit reached")
            event = {
                "format": 1, "sequence": projection.revision + 1,
                "previous_hash": projection.head_hash,
                "recorded_at": timestamp(self.clock()),
                "action": action, "data": data, "reason": reason,
            }
            validate_event(event, projection)
            body = canonical(event)
            if len(body.encode("utf-8")) > MAX_EVENT_BYTES:
                raise LRMError("operation exceeds the event size limit")
            projection.apply(event)
            connection.execute("INSERT INTO events VALUES (?, ?, ?)",
                               (event["sequence"], body, projection.head_hash))
            return {"revision": projection.revision, "head_hash": projection.head_hash,
                    "action": action, "recorded_at": event["recorded_at"]}

    def read(self, operation: str, *, scope: str | None = None, record_id: str | None = None,
             left: str | None = None, right: str | None = None, at: str | None = None) -> dict:
        """Evaluate only evidence known at `at`; later events remain outside that view."""
        at = timestamp(at if at is not None else self.clock())
        with self._connection() as connection:
            head, events = self._replay(connection)
        projection = Projection()
        visible_events = []
        for event in events:
            if event["recorded_at"] <= at:
                projection.apply(event)
                visible_events.append(event)
        if operation == "state":
            result = projection.state(scope, at)
        elif operation == "lookup":
            result = projection.lookup(record_id, at)
        elif operation == "compare":
            result = projection.compare(left, right, at)
        elif operation == "history":
            result = {"events": visible_events}
        elif operation == "verify":
            result = {"integrity": "ok", "verified_event_count": head.revision}
        else:
            raise LRMError("unsupported read operation")
        return json.loads(canonical({
            "format": FORMAT, "as_of": at,
            "revision": projection.revision, "head_revision": head.revision,
            "view_hash": projection.head_hash, "head_hash": head.head_hash,
            "meaning": "local evidence and explicit selection; not truth, authority, or action permission",
            "result": result,
        }))
