#!/usr/bin/env python3
from __future__ import annotations

import sys
from datetime import date

from common import ROOT, markdown_files, slugify

TEMPLATE_PATH = ROOT / "Chapters" / "Chapter-Template.md"


def next_chapter_number() -> int:
    chapters = markdown_files("Chapters", "Drafts")
    numbers = []
    for chapter in chapters:
        if chapter.name in {"Chapter-Template.md", "README.md"}:
            continue
        prefix = chapter.name.split("-", 1)[0]
        if prefix.isdigit():
            numbers.append(int(prefix))
    return max(numbers, default=0) + 1


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python3 scripts/new_chapter.py "Chapter Title"')
        return 1

    title = " ".join(sys.argv[1:]).strip()
    number = next_chapter_number()
    slug = slugify(title)
    destination = ROOT / "Drafts" / f"{number:02d}-{slug}.md"
    if destination.exists():
        print(f"{destination.relative_to(ROOT)} already exists")
        return 1

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    content = template.replace("Chapter Title", title, 2)
    content = content.replace("chapter_number: 0", f"chapter_number: {number}", 1)
    content = content.replace("summary: One-sentence chapter summary.", f"summary: Draft created on {date.today().isoformat()}.", 1)

    destination.write_text(content, encoding="utf-8")
    print(f"Created {destination.relative_to(ROOT)}")

    from report_progress import update_progress

    update_progress()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
