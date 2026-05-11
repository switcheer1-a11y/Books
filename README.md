# Books

A markdown-first nonfiction book-writing repository optimized for VS Code, Git, and GitHub Copilot.

## Repository Structure

- `Chapters/` — chapter files ready for the manuscript
- `Research/` — notes, source extracts, and research summaries
- `Drafts/` — unfinished chapter drafts and fragments
- `References/` — bibliographies, source logs, and citation helpers
- `Exports/` — generated manuscript exports
- `Prompts/` — reusable GitHub Copilot prompt templates
- `Notes/` — planning notes, ideas, and revision notes
- `Manuscripts/` — assembled manuscript indexes and working compilations
- `Summaries/` — AI-generated summaries and recap files
- `scripts/` — lightweight filesystem-based automation utilities

## Starter Files

- `Book-Overview.md`
- `Outline.md`
- `Progress.md`
- `Ideas.md`

## Recommended Workflow

1. Capture concepts in `Ideas.md` and `Notes/`.
2. Research in `Research/` using the research note template.
3. Create a chapter with `python3 scripts/new_chapter.py "Chapter Title"`.
4. Draft unfinished work in `Drafts/` and move completed drafts into `Chapters/`.
5. Run `python3 scripts/organize_files.py` to place files by metadata or filename.
6. Update indexes and progress with `python3 scripts/report_progress.py` and `python3 scripts/build_index.py`.
7. Validate metadata with `python3 scripts/validate_metadata.py` before revision/export.

## Git-Friendly Writing Tips

- Keep one chapter per markdown file for clean diffs.
- Use frontmatter metadata for status, word count, revision stage, sources, and tags.
- Commit by chapter, revision stage, or research milestone.
- Treat exported binary files as disposable outputs rather than primary source files.

See the workflow guides in the repository root for detailed usage.
