"""
UniversalMind public SDK CLI.

ROLE
----
Provide a small install-and-run surface for developers evaluating the public
human-governance contract.

Commands:
- info: show version, license posture, and authority boundary.
- doctor: verify package/API/static UI imports.
- serve: launch the local Workbench/API on loopback only.
"""

from __future__ import annotations

import argparse
import importlib
from pathlib import Path
import sys

from . import __version__


LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="universalmind",
        description="Human-governed approval and audit boundaries for AI agents.",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("info", help="Show product, license, and governance boundary.")
    sub.add_parser("doctor", help="Verify the local SDK installation.")
    serve = sub.add_parser("serve", help="Start the local governance Workbench/API.")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8000)
    return parser


def command_info() -> int:
    print(f"UniversalMind Governance SDK {__version__}")
    print("Boundary: AI may propose; a human retains state-changing authority.")
    print("Execution: this SDK authorizes/denies dispatch but never performs it.")
    print("License: Business Source License 1.1 (source-available, non-production by default).")
    return 0


def command_doctor() -> int:
    checks: list[tuple[str, bool, str]] = []
    checks.append(("python", sys.version_info >= (3, 10), sys.version.split()[0]))

    try:
        module = importlib.import_module("universalmind.api")
        checks.append(("api", hasattr(module, "app"), "universalmind.api:app"))
    except Exception as exc:
        checks.append(("api", False, f"{type(exc).__name__}: {exc}"))

    static_index = Path(__file__).resolve().parent / "static" / "index.html"
    checks.append(("static_ui", static_index.is_file(), str(static_index)))

    ok = all(passed for _, passed, _ in checks)
    for name, passed, detail in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}: {detail}")
    print(f"UniversalMind doctor: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def command_serve(host: str, port: int) -> int:
    if host not in LOOPBACK_HOSTS:
        print(
            "Refusing non-loopback bind: this SDK release has no authentication.",
            file=sys.stderr,
        )
        return 2
    if not 1 <= port <= 65535:
        print("Port must be between 1 and 65535.", file=sys.stderr)
        return 2

    import uvicorn

    uvicorn.run("universalmind.api:app", host=host, port=port, reload=False)
    return 0


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "info":
        return command_info()
    if args.command == "doctor":
        return command_doctor()
    if args.command == "serve":
        return command_serve(args.host, args.port)
    return 2
