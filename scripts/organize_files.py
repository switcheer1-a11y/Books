#!/usr/bin/env python3
from __future__ import annotations

import shutil
import sys
from pathlib import Path

from common import ROOT, extract_frontmatter

DESTINATIONS = {
    "research": ROOT / "Research",
    "chapter": ROOT / "Chapters",
    "draft": ROOT / "Drafts",
    "export": ROOT / "Exports",
    "summary": ROOT / "Summaries",
}
SKIP_DIRECTORIES = {"Chapters", "Research", "Drafts", "References", "Exports", "Prompts", "Notes", "Manuscripts", "Summaries", "scripts", ".git"}
EXPORT_EXTENSIONS = {".pdf", ".docx", ".epub", ".html", ".rtf", ".odt"}


def choose_destination(path: Path) -> Path | None:
    if path.suffix.lower() in EXPORT_EXTENSIONS:
        return DESTINATIONS["export"]

    metadata = {}
    if path.suffix.lower() == ".md":
        metadata, _ = extract_frontmatter(path)
        if not metadata and not (
            path.name.lower().startswith("research-")
            or path.name.lower().startswith("summary-")
            or path.name[:2].isdigit()
        ):
            return None

    tags = {str(tag).lower() for tag in metadata.get("tags", [])} if isinstance(metadata.get("tags"), list) else set()
    status = str(metadata.get("status", "")).lower()
    name = path.name.lower()

    if "research" in tags or name.startswith("research-"):
        return DESTINATIONS["research"]
    if "summary" in tags or name.startswith("summary-"):
        return DESTINATIONS["summary"]
    if "chapter" in tags or name[:2].isdigit():
        return DESTINATIONS["chapter"] if status == "completed" else DESTINATIONS["draft"]
    if status == "completed":
        return DESTINATIONS["chapter"]
    if status in {"draft", "in-progress", "in_progress", "active"}:
        return DESTINATIONS["draft"]
    return None


def main() -> int:
    search_root = ROOT if len(sys.argv) == 1 else Path(sys.argv[1]).resolve()
    moved = 0
    for path in sorted(search_root.iterdir()):
        if path.is_dir() and path.name in SKIP_DIRECTORIES:
            continue
        if path.is_dir():
            continue
        destination = choose_destination(path)
        if not destination:
            continue
        target = destination / path.name
        if target.resolve() == path.resolve():
            continue
        shutil.move(str(path), str(target))
        print(f"Moved {path.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        moved += 1
    if moved == 0:
        print("No files needed organization.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
