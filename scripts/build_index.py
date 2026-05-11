#!/usr/bin/env python3
from __future__ import annotations

from common import ROOT, chapter_sort_key, extract_frontmatter, markdown_files

INDEX_PATH = ROOT / "Manuscripts" / "Index.md"


def main() -> int:
    chapters = [path for path in sorted(markdown_files("Chapters"), key=chapter_sort_key) if path.name != "Chapter-Template.md"]
    summaries = [path for path in markdown_files("Summaries") if path.name != "README.md"]

    lines = ["# Manuscript Index", "", "## Chapters"]
    if chapters:
        for path in chapters:
            metadata, _ = extract_frontmatter(path)
            lines.append(f"- Chapter {metadata.get('chapter_number', '?')} — [{metadata.get('title', path.stem)}]({path.relative_to(ROOT).as_posix()})")
    else:
        lines.append("- No chapters yet")

    lines.extend(["", "## Summaries"])
    if summaries:
        for path in summaries:
            lines.append(f"- [{path.stem.replace('-', ' ')}]({path.relative_to(ROOT).as_posix()})")
    else:
        lines.append("- No summaries yet")

    INDEX_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Updated {INDEX_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
