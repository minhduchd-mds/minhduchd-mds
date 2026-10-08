#!/usr/bin/env python3
"""Audit and optionally fill blank GitHub repository About descriptions.

Requires Python 3.10+ and authenticated GitHub CLI (gh auth login).
DRY RUN by default. Does NOT touch visibility, topics, homepage, source or README.
Only writes an empty Description field; existing descriptions are preserved.

Usage:
    python3 scripts/sync-repo-about.py
    python3 scripts/sync-repo-about.py --apply
    python3 scripts/sync-repo-about.py --apply --include-private
"""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys

OWNER = "minhduchd-mds"
MAX_DESCRIPTION = 160


def gh(*arguments: str) -> str:
    command = ["gh", *arguments]
    return subprocess.check_output(command, text=True, stderr=subprocess.PIPE).strip()


def get_readme(repo: str) -> str:
    try:
        return gh(
            "api", f"repos/{OWNER}/{repo}/readme",
            "-H", "Accept: application/vnd.github.raw+json",
        )
    except subprocess.CalledProcessError:
        return ""


def clean(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_>#|]", " ", text)
    text = re.sub(r"\s+", " ", text).strip(" -:\t")
    return text[:MAX_DESCRIPTION].rstrip(" ,;:.-")


def make_description(name: str, readme: str) -> str:
    lines = readme.splitlines()
    in_about = False
    about_lines: list[str] = []
    for line in lines:
        if re.match(r"^#{1,3}\s+About\s*$", line, re.I):
            in_about = True
            continue
        if in_about and re.match(r"^#{1,3}\s+", line):
            break
        if in_about and line.strip() and not line.lstrip().startswith(("![", "<", "|", "- ", "* ", "`")):
            about_lines.append(line.strip())
            if len(" ".join(about_lines)) >= 120:
                break
    if about_lines:
        return clean(" ".join(about_lines))
    # For READMEs without an explicit About, avoid guessing implementation quality.
    return clean(f"{name}: source code and project documentation. See README for status and scope.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write empty About fields to GitHub.")
    parser.add_argument("--include-private", action="store_true", help="Include private repositories.")
    args = parser.parse_args()
    try:
        raw = gh("repo", "list", OWNER, "--limit", "500", "--json",
                 "name,description,isPrivate,isArchived")
        repos = json.loads(raw)
    except (FileNotFoundError, subprocess.CalledProcessError, ValueError) as exc:
        print(f"Cannot list repos: {exc}", file=sys.stderr)
        return 2

    scanned = 0
    missing = 0
    applied = 0
    failures = 0
    for repo in sorted(repos, key=lambda r: r["name"].casefold()):
        if repo["isArchived"] or (repo["isPrivate"] and not args.include_private):
            continue
        scanned += 1
        if (repo.get("description") or "").strip():
            continue
        missing += 1
        name = repo["name"]
        summary = make_description(name, get_readme(name))
        print(f'{"APPLY" if args.apply else "DRY-RUN"} {OWNER}/{name}: {summary}')
        if args.apply:
            try:
                gh("repo", "edit", f"{OWNER}/{name}", "--description", summary)
                applied += 1
            except subprocess.CalledProcessError as exc:
                failures += 1
                print(f"  FAILED: {exc}", file=sys.stderr)
    print(f"scanned={scanned} missing={missing} updated={applied} failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
