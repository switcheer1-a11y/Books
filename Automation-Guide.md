# Automation Usage Guide

## Create a Chapter
```bash
python3 scripts/new_chapter.py "Chapter Title"
```
Creates a new chapter from the template and refreshes `Progress.md`.

## Organize Files
```bash
python3 scripts/organize_files.py
```
Moves files into the expected folders using metadata, tags, status, and filename patterns.

## Build the Manuscript Index
```bash
python3 scripts/build_index.py
```
Generates `Manuscripts/Index.md` from current chapters and summaries.

## Count Words
```bash
python3 scripts/word_count.py
```
Reports word counts for chapters, drafts, and totals.

## Refresh Progress
```bash
python3 scripts/report_progress.py
```
Updates the chapter tracker and totals in `Progress.md`.

## Validate Metadata
```bash
python3 scripts/validate_metadata.py
```
Checks markdown files for required frontmatter fields.
