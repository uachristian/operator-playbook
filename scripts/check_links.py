#!/usr/bin/env python3
"""Fail if any relative Markdown link in this repo points at a missing file."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\]\(([^)#\s]+)")
FENCE = re.compile(r"```.*?```", re.S)


def main() -> int:
    broken = 0
    checked = 0
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = FENCE.sub("", md.read_text(encoding="utf-8"))
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            if not (md.parent / target).resolve().exists():
                broken += 1
                print(f"BROKEN {md.relative_to(ROOT)} -> {target}")
    print(f"{checked} relative links checked, {broken} broken")
    return 1 if broken or checked == 0 else 0


if __name__ == "__main__":
    sys.exit(main())
