from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
TRACKED_FOLDERS = ["Chapters", "Drafts", "Research", "Summaries"]
REQUIRED_METADATA = ["title", "status", "word_count", "revision_stage", "sources_used", "tags"]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "chapter"


def extract_frontmatter(path: Path) -> Tuple[Dict[str, object], str]:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        return {}, content

    try:
        _, raw_frontmatter, body = content.split("---\n", 2)
    except ValueError:
        return {}, content

    data: Dict[str, object] = {}
    current_list_key = None
    for raw_line in raw_frontmatter.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.startswith("  - ") and current_list_key:
            data.setdefault(current_list_key, []).append(line[4:].strip())
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            data[key] = []
            current_list_key = key
        else:
            data[key] = coerce_value(value)
            current_list_key = None
    return data, body


def coerce_value(value: str):
    if value.isdigit():
        return int(value)
    return value


def word_count_from_text(text: str) -> int:
    return len(re.findall(r"\b\w+[\w'-]*\b", text))


def markdown_files(*folders: str) -> List[Path]:
    paths: List[Path] = []
    for folder in folders:
        directory = ROOT / folder
        if directory.exists():
            paths.extend(sorted(directory.glob("*.md")))
    return paths


def chapter_sort_key(path: Path):
    metadata, _ = extract_frontmatter(path)
    number = metadata.get("chapter_number")
    if isinstance(number, int):
        return (number, path.name)
    match = re.match(r"(\d+)", path.name)
    return (int(match.group(1)) if match else 9999, path.name)
