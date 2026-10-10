#!/usr/bin/env python3
"""Check that translations stay consistent with the canonical English text.

Errors (exit 1):
  - missing or malformed header comment
  - language code in the header does not match the file name
  - heading structure differs from CODE_OF_CONDUCT.md
  - URLs or the reporting address missing from a translation
  - source-version differs from the current version but status is not "outdated"
  - translation not listed in README.md or in the language line of CODE_OF_CONDUCT.md

Warnings:
  - outdated translations
  - unresolved [TBD ...] placeholders
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "CODE_OF_CONDUCT.md"
README = ROOT / "README.md"
TRANSLATIONS = ROOT / "translations"

STATUSES = {"needs-review", "reviewed", "outdated"}
SEMVER = r"\d+\.\d+\.\d+"
CANONICAL_HEADER = re.compile(rf"^<!-- version: ({SEMVER}) \| status: (\w+) \| updated: [\d-]+ -->$")
TRANSLATION_HEADER = re.compile(
    rf"^<!-- translation: ([a-z]{{2}}(?:-[A-Z]{{2}})?) \| source-version: ({SEMVER}) \| status: ([a-z-]+) -->$"
)
HEADING = re.compile(r"^(#{1,6}) ")
URL = re.compile(r"\]\((https?://[^)\s]+)\)")
REPORT_ADDRESS = "conduct@millibar.io"

IN_CI = os.environ.get("GITHUB_ACTIONS") == "true"
errors = 0


def report(level, path, message):
    global errors
    rel = path.relative_to(ROOT)
    if level == "error":
        errors += 1
    if IN_CI:
        print(f"::{level} file={rel}::{message}")
    else:
        print(f"{level.upper()}: {rel}: {message}")


def heading_levels(text):
    levels, in_code = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        elif not in_code and (m := HEADING.match(line)):
            levels.append(len(m.group(1)))
    return levels


def urls(text):
    # Localised Creative Commons deeds (…/4.0/deed.de) count as the same link.
    return {re.sub(r"/deed\.[a-z-]+$", "/", u).rstrip("/") for u in URL.findall(text)}


def main():
    canonical = CANONICAL.read_text(encoding="utf-8")
    m = CANONICAL_HEADER.match(canonical.splitlines()[0])
    if not m:
        report("error", CANONICAL, "first line must be '<!-- version: X.Y.Z | status: … | updated: YYYY-MM-DD -->'")
        return 1
    version = m.group(1)
    canonical_levels = heading_levels(canonical)
    canonical_urls = urls(canonical)
    readme = README.read_text(encoding="utf-8")
    language_line = next((l for l in canonical.splitlines() if l.startswith("> Translations:")), "")

    files = sorted(TRANSLATIONS.glob("*.md"))
    if not files:
        print("No translations found.")

    for path in files:
        text = path.read_text(encoding="utf-8")
        code = path.stem
        h = TRANSLATION_HEADER.match(text.splitlines()[0] if text else "")
        if not h:
            report("error", path, "first line must be '<!-- translation: xx | source-version: X.Y.Z | status: … -->'")
            continue
        lang, source_version, status = h.groups()

        if lang != code:
            report("error", path, f"header says '{lang}' but file name is '{code}.md'")
        if status not in STATUSES:
            report("error", path, f"unknown status '{status}' (use one of: {', '.join(sorted(STATUSES))})")

        if source_version != version and status != "outdated":
            report("error", path, f"follows {source_version} but the English text is {version}: "
                                  "update it, or set status to 'outdated'")
        elif status == "outdated":
            report("warning", path, f"outdated: follows {source_version}, English text is {version}")

        levels = heading_levels(text)
        if levels != canonical_levels:
            report("error", path, f"heading structure {levels} differs from CODE_OF_CONDUCT.md {canonical_levels}")

        missing = canonical_urls - urls(text)
        for url in sorted(missing):
            report("error", path, f"missing link {url}")
        if REPORT_ADDRESS not in text:
            report("error", path, f"missing reporting address {REPORT_ADDRESS}")

        if f"translations/{code}.md" not in readme:
            report("error", README, f"translation '{code}' is not listed in the README table")
        if f"translations/{code}.md" not in language_line:
            report("error", CANONICAL, f"translation '{code}' is not listed in the language line")

    for path in [CANONICAL, *files]:
        tbd = len(re.findall(r"\[TBD\b", path.read_text(encoding="utf-8")))
        if tbd:
            report("warning", path, f"{tbd} unresolved [TBD] placeholder(s)")

    print(f"Checked {len(files)} translation(s) against version {version}: "
          f"{'OK' if not errors else f'{errors} error(s)'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
