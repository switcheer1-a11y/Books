# Chapter Creation Process

1. Run `python3 scripts/new_chapter.py "Chapter Title"`.
2. Fill in the generated frontmatter.
3. Expand the chapter summary, key ideas, and draft sections.
4. Keep `word_count` updated or refresh it with `python3 scripts/word_count.py`.
5. When the chapter is complete, set `status: completed` and move it into `Chapters/` if needed.
6. Run `python3 scripts/report_progress.py` to refresh `Progress.md`.
