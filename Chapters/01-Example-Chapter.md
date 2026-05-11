---
title: Example Chapter
chapter_number: 1
status: completed
word_count: 255
revision_stage: revised
sources_used:
  - Research/Example-Research-Note.md
  - References/Source-Log.md
tags:
  - chapter
  - example
  - foundation
summary: Introduces the project structure and explains how a markdown-first workflow supports nonfiction writing.
---

# Example Chapter

## Objective
Show how a simple repository structure can reduce friction while researching, outlining, drafting, and revising a nonfiction book.

## Key Ideas
- Keep each chapter in its own markdown file.
- Track progress and revision state in frontmatter.
- Use lightweight automation to organize files without adding application complexity.

## Draft
A strong nonfiction workflow does not need a heavy publishing system. It needs a reliable place to gather ideas, turn research into structure, and keep chapters moving from rough draft to polished manuscript. This repository is designed around that principle.

Each major writing activity has a home. Research notes live in `Research/`. Early material that is not ready for the manuscript stays in `Drafts/`. Completed chapter drafts move into `Chapters/`, where they can be reviewed in order, linked from an index, and revised with clean Git history. Summaries make it easier to return to a project after time away, and `Exports/` provides a predictable destination for generated output files.

Because the workflow is markdown-first, the repository remains easy to edit in VS Code, simple to diff in Git, and convenient to extend with GitHub Copilot. Prompt templates, chapter templates, and metadata validation all support a repeatable writing process without turning the repository into an application. The result is a structure that stays lightweight while still helping the writer maintain momentum, consistency, and traceability.

## Sources and Evidence
- See the example research note for supporting observations about tooling and process design.

## Revision Notes
- Expand with reader personas and project-specific examples when adapting this repository for a real book.
