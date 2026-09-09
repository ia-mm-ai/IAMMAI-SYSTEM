"""Explicit local commands. Text and origin references are data, never executed."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .model import LRMError, MAX_EVENT_BYTES, parse_json
from .store import Workspace


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog="lrm", description="Local relevance workspace: evidence is not authority."
    )
    root.add_argument("--db", required=True, type=Path, help="explicit local SQLite workspace path")
    commands = root.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="create a new workspace; never overwrite")
    for name in ("admit", "select", "relate", "supersede", "retract"):
        command = commands.add_parser(name)
        command.add_argument("--expect", required=True, type=int, help="last observed head revision")
        command.add_argument("--reason", required=True, help="explicit rationale, preserved in history")
        if name == "admit":
            command.add_argument("file", type=Path, help="UTF-8 JSON evidence record")
        elif name == "select":
            command.add_argument("--scope", required=True)
            command.add_argument("ids", nargs="*", help="complete selection; omit all to clear")
        elif name == "relate":
            command.add_argument("kind", choices=("supports", "contradicts", "related"))
            command.add_argument("left")
            command.add_argument("right")
        elif name == "supersede":
            command.add_argument("old")
            command.add_argument("new")
        else:
            command.add_argument("id")
    for name in ("state", "lookup", "compare", "history", "verify"):
        command = commands.add_parser(name)
        command.add_argument("--at", help="RFC3339 historical cutoff or explicit future projection")
        if name == "state":
            command.add_argument("--scope", required=True)
        elif name == "lookup":
            command.add_argument("id")
        elif name == "compare":
            command.add_argument("left")
            command.add_argument("right")
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        workspace = Workspace(args.db)
        if args.command == "init":
            workspace = Workspace.create(args.db)
            result = workspace.read("verify")
        elif args.command in ("state", "lookup", "compare", "history", "verify"):
            result = workspace.read(
                args.command, scope=getattr(args, "scope", None),
                record_id=getattr(args, "id", None), left=getattr(args, "left", None),
                right=getattr(args, "right", None), at=args.at,
            )
        else:
            if args.command == "admit":
                if not args.file.is_file():
                    raise LRMError("record input must be a regular JSON file")
                with args.file.open("rb") as handle:
                    raw = handle.read(MAX_EVENT_BYTES + 1)
                if len(raw) > MAX_EVENT_BYTES:
                    raise LRMError("record input exceeds the size limit")
                data = {"record": parse_json(raw.decode("utf-8"))}
            elif args.command == "select":
                data = {"scope": args.scope, "ids": args.ids}
            elif args.command == "relate":
                data = {"kind": args.kind, "left": args.left, "right": args.right}
            elif args.command == "supersede":
                data = {"old": args.old, "new": args.new}
            else:
                data = {"id": args.id}
            result = workspace.append(args.command, data, reason=args.reason, expected_revision=args.expect)
        print(json.dumps(result, indent=2, ensure_ascii=True, allow_nan=False))
        return 0
    except (LRMError, OSError, UnicodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
