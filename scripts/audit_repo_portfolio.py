#!/usr/bin/env python3
"""Read-only audit of repository About, README and documentation hygiene.

Requires GitHub CLI (gh), authenticated for the selected repositories.
No repository settings or files are modified by this script.
Private repository names never appear unless --include-private is explicitly set.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import sys
from typing import Any

OWNER = "minhduchd-mds"


def gh(*arguments: str) -> str:
    return subprocess.check_output(
        ["gh", *arguments], text=True, stderr=subprocess.PIPE, timeout=40
    ).strip()


def describe_root(repo: dict[str, Any]) -> dict[str, Any]:
    name = repo["name"]
    result: dict[str, Any] = {
        "name": name,
        "url": repo["url"],
        "visibility": "private" if repo.get("isPrivate") else "public",
        "archived": bool(repo.get("isArchived")),
        "about": (repo.get("description") or "").strip(),
        "readme": False,
        "docs_dir": False,
        "security_policy": False,
        "license_file": False,
        "github_config": False,
        "error": None,
    }
    try:
        listing = json.loads(gh("api", f"repos/{OWNER}/{name}/contents"))
        if not isinstance(listing, list):
            raise ValueError("Unexpected root contents response")
        filenames = {entry["name"].lower(): entry.get("type") for entry in listing}
        result["readme"] = any(
            n == "readme" or n.startswith("readme.") for n in filenames
        )
        result["docs_dir"] = filenames.get("docs") == "dir"
        result["security_policy"] = filenames.get("security.md") == "file"
        result["license_file"] = any(
            n == "license" or n.startswith("license.") or
            n == "copying" or n.startswith("copying.") for n in filenames
        )
        result["github_config"] = filenames.get(".github") == "dir"
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, ValueError, KeyError) as exc:
        result["error"] = type(exc).__name__
    return result


def markdown(rows: list[dict[str, Any]]) -> str:
    count = len(rows)
    missing_about = sum(not row["about"] for row in rows)
    missing_readme = sum(not row["readme"] and not row["error"] for row in rows)
    failures = sum(bool(row["error"]) for row in rows)
    lines = [
        "# Repository Documentation Audit",
        "",
        f"Scope: {count} accessible repositories; read-only inspection.",
        f"Missing About: **{missing_about}** · Missing README: **{missing_readme}** · Inspection errors: **{failures}**",
        "",
        "> Missing docs in a historical/learning repository are not necessarily defects.",
        "> This audit checks file existence, not correctness, link validity, runtime security or CI results.",
        "",
        "| Repository | About | README | docs/ | SECURITY | LICENSE | Note |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        safe_name = r["name"].replace("|", "\\|")
        mark = lambda key: "✓" if r[key] else "—"
        note = "inspect failed" if r["error"] else ("archived" if r["archived"] else "")
        lines.append(
            f"| [{safe_name}]({r['url']}) | {mark('about')} | {mark('readme')} | "
            f"{mark('docs_dir')} | {mark('security_policy')} | {mark('license_file')} | {note} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--include-private", action="store_true",
                        help="Explicitly include private repository names in output")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--jobs", type=int, default=5)
    args = parser.parse_args()
    if args.jobs < 1 or args.jobs > 8:
        parser.error("--jobs must be between 1 and 8")
    try:
        repositories = json.loads(gh(
            "repo", "list", OWNER, "--limit", "500", "--json",
            "name,url,description,isPrivate,isArchived",
        ))
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired, ValueError) as exc:
        print(f"Unable to list repositories: {exc}", file=sys.stderr)
        return 2

    selected = [r for r in repositories if args.include_private or not r["isPrivate"]]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        rows = list(pool.map(describe_root, selected))
    rows.sort(key=lambda r: r["name"].casefold())

    if args.format == "json":
        print(json.dumps({
            "owner": OWNER,
            "scope": "public-and-private" if args.include_private else "public-only",
            "repository_count": len(rows),
            "missing_about": sum(not r["about"] for r in rows),
            "missing_readme": sum(not r["readme"] and not r["error"] for r in rows),
            "errors": sum(bool(r["error"]) for r in rows),
            "repositories": rows,
        }, indent=2, ensure_ascii=False))
    else:
        print(markdown(rows), end="")
    return 1 if any(row["error"] for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())
