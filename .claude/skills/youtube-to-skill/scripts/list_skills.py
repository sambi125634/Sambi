#!/usr/bin/env python3
"""List every skill under .claude/skills with its frontmatter name + description.

Used by the youtube-to-skill automation to decide whether a new video's
content belongs in an existing skill or needs a brand new one.

Usage:
    python3 list_skills.py [skills_root]

Prints a JSON array: [{"dir": "...", "name": "...", "description": "..."}]
"""
import json
import os
import re
import sys


def parse_frontmatter(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not m:
        return {}
    fm_text = m.group(1)
    data = {}
    current_key = None
    for line in fm_text.splitlines():
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip()
            val = val.strip('"').strip("'")
            data[key] = val
            current_key = key
        elif current_key and line.strip():
            data[current_key] += " " + line.strip()
    return data


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else ".claude/skills"
    results = []
    if not os.path.isdir(root):
        print(json.dumps(results))
        return
    for entry in sorted(os.listdir(root)):
        skill_dir = os.path.join(root, entry)
        skill_md = os.path.join(skill_dir, "SKILL.md")
        if os.path.isfile(skill_md):
            fm = parse_frontmatter(skill_md)
            results.append({
                "dir": entry,
                "name": fm.get("name", entry),
                "description": fm.get("description", ""),
            })
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
