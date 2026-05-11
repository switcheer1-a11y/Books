#!/usr/bin/env python3
from __future__ import annotations

from common import ROOT, extract_frontmatter, markdown_files, word_count_from_text


def main() -> int:
    total = 0
    for path in markdown_files("Chapters", "Drafts", "Research", "Summaries"):
        if path.name.endswith("Template.md") or path.name == "README.md":
            continue
        metadata, body = extract_frontmatter(path)
        words = word_count_from_text(body)
        total += words
        print(f"{path.relative_to(ROOT)}: {words} words (metadata: {metadata.get('word_count', 'n/a')})")
    print(f"Total words: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
