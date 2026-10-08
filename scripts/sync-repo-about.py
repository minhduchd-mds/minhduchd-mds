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

# Curated, factual descriptions for projects whose README is extensive or starts
# with a banner, making automatic first-sentence extraction less informative.
CURATED = {
    "Kingmast": "Warning-only ADAS research: multi-camera perception, radar fusion, TTC/THW and driver-focused HMI.",
    "miraai": "Local-first multimodal AI companion research: voice, gestures, computer vision and desktop experiences.",
    "cv-template": "Interactive CV Studio with editable templates, resume export and career preparation tools.",
    "open-design": "Open-source, local-first AI design workspace for agent-assisted design and multi-format outputs.",
    "esp32-rf-high-frequency": "Receive-only ESP32-S3 RF observatory for calibration, signal monitoring and repeatable experiments.",
    "SM-OS-mini": "Minimal ESP32-S3 runtime research for safe device resource management and programmable project services.",
    "Customer-service-bot": "Self-hosted omnichannel customer-service bot platform with multi-bot workflows and deployment tooling.",
    "AI-design.tools": "Figma-oriented AI design tooling, design-token utilities and practical transformation workflows.",
    "AI-Design-Tools": "Experimental design tools for PDF, code export and UI transformation workflows.",
    "desygn-ai": "AI design engineering platform with audit, design-to-code workflows and design-system tooling.",
    "Soi": "AI-assisted design QA research comparing interfaces and highlighting UI inconsistencies.",
    "MiraOPS_suite": "Local-first multi-tool workspace for product engineering and design operations.",
}
WEAK_PLACEHOLDERS = {"test", "demo", "sss", "s", "php", "kit", "sd", "japan"}


def is_weak_description(description: str) -> bool:
    value = description.strip()
    return len(value) < 25 or value.casefold() in WEAK_PLACEHOLDERS



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
    # Choose a meaningful introductory sentence when an explicit About is absent.
    # Ignore headings, badges, HTML wrappers, code, navigation and status labels.
    for line in lines[:65]:
        item = line.strip()
        if not item or item.startswith(("#", "![", "[![", "<", "|", "-", "* ", "`")):
            continue
        candidate = clean(item)
        if len(candidate) >= 45 and not candidate.lower().startswith(
            ("status", "documentation", "quick start", "getting started", "version")
        ):
            return candidate
    # Historical or otherwise ambiguous repositories get a neutral description.
    return clean(f"{name}: source code and project documentation. See README for status and scope.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write empty About fields to GitHub.")
    parser.add_argument("--include-private", action="store_true", help="Include private repositories.")
    parser.add_argument("--refresh-weak", action="store_true", help="Replace short/placeholder existing descriptions too.")
    parser.add_argument("--refresh-curated", action="store_true", help="Refresh only non-empty curated featured descriptions; never mass-rewrite others.")
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
    replacements = 0
    for repo in sorted(repos, key=lambda r: r["name"].casefold()):
        if repo["isArchived"] or (repo["isPrivate"] and not args.include_private):
            continue
        scanned += 1
        name = repo["name"]
        existing = (repo.get("description") or "").strip()
        replace_weak = bool(existing and args.refresh_weak and is_weak_description(existing))
        replace_curated = bool(existing and args.refresh_curated and name in CURATED)
        if existing and not (replace_weak or replace_curated):
            continue
        if not existing:
            missing += 1
        else:
            replacements += 1
        summary = CURATED.get(name) or make_description(name, get_readme(name))
        if summary == existing:
            continue
        mode = "REPLACE" if existing else "FILL"
        print(f'{"APPLY" if args.apply else "DRY-RUN"} {mode} {OWNER}/{name}: {summary}')
        if args.apply:
            try:
                gh("repo", "edit", f"{OWNER}/{name}", "--description", summary)
                applied += 1
            except subprocess.CalledProcessError as exc:
                failures += 1
                print(f"  FAILED: {exc}", file=sys.stderr)
    print(f"scanned={scanned} missing={missing} weak_or_curated={replacements} updated={applied} failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
