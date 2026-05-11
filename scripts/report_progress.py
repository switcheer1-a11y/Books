#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from common import ROOT, chapter_sort_key, extract_frontmatter, markdown_files, word_count_from_text

PROGRESS_PATH = ROOT / "Progress.md"
START_MARKER = "<!-- AUTO-CHAPTER-LIST:START -->"
END_MARKER = "<!-- AUTO-CHAPTER-LIST:END -->"


def chapter_line(path: Path) -> tuple[str, int, bool]:
    metadata, body = extract_frontmatter(path)
    title = str(metadata.get("title", path.stem))
    status = str(metadata.get("status", "draft"))
    revision = str(metadata.get("revision_stage", "draft"))
    words = word_count_from_text(body)
    checked = "x" if status == "completed" else " "
    return (
        f"- [{checked}] Chapter {metadata.get('chapter_number', '?')} — {title} (`{path.relative_to(ROOT)}`) — status: {status} — revision: {revision} — words: {words}",
        words,
        status == "completed",
    )


def update_progress() -> None:
    chapter_files = sorted(markdown_files("Chapters", "Drafts"), key=chapter_sort_key)
    lines = []
    total_words = 0
    completed = 0
    drafts = 0
    for path in chapter_files:
        if path.name in {"Chapter-Template.md", "README.md"}:
            continue
        metadata, _ = extract_frontmatter(path)
        if "chapter_number" not in metadata:
            continue
        line, words, is_completed = chapter_line(path)
        lines.append(line)
        total_words += words
        if is_completed:
            completed += 1
        else:
            drafts += 1

    tracker = "\n".join(lines) if lines else "- [ ] No chapter files yet"
    updated = f"# Writing Progress\n\n## Snapshot\n- Total chapter files: {len(lines)}\n- Completed chapters: {completed}\n- Draft chapters: {drafts}\n- Total tracked words: {total_words}\n\n## Chapter Tracker\n\n{START_MARKER}\n{tracker}\n{END_MARKER}\n\n## Next Actions\n- Add the next chapter with `python3 scripts/new_chapter.py \"Chapter Title\"`\n- Draft unfinished sections in `Drafts/`\n- Run `python3 scripts/report_progress.py` after structural changes\n"
    PROGRESS_PATH.write_text(updated, encoding="utf-8")
    print(f"Updated {PROGRESS_PATH.relative_to(ROOT)}")


def main() -> int:
    update_progress()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
