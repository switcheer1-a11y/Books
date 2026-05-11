#!/usr/bin/env python3
from __future__ import annotations

from common import REQUIRED_METADATA, ROOT, extract_frontmatter, markdown_files


TARGET_FOLDERS = ("Chapters", "Drafts", "Research", "Summaries")


def main() -> int:
    failures = []
    for path in markdown_files(*TARGET_FOLDERS):
        if path.name in {"README.md", "Chapter-Template.md", "Research-Note-Template.md"}:
            continue
        metadata, _ = extract_frontmatter(path)
        missing = [field for field in REQUIRED_METADATA if field not in metadata]
        if missing:
            failures.append(f"{path.relative_to(ROOT)} missing: {', '.join(missing)}")

    if failures:
        print("Metadata validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("All tracked markdown files contain required metadata.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
