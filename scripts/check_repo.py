"""Offline integrity checks; no downloads and no external URL verification."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
resources = json.loads((ROOT / "data/resources.json").read_text())
ids = set()
required = {"id", "title", "authors", "year", "kind", "status", "category", "priority", "url", "why", "focus", "verified", "verification"}
for r in resources:
    if required - r.keys():
        errors.append(f"Missing fields for {r.get('id')}: {required-r.keys()}")
    if r["id"] in ids:
        errors.append(f"Duplicate id: {r['id']}")
    ids.add(r["id"])
    if urlsplit(r["url"]).scheme != "https":
        errors.append(f"Expected HTTPS: {r['id']}")
    if r["priority"] not in {"Core", "Next", "Optional"}:
        errors.append(f"Invalid priority: {r['id']}")
    if r["category"] not in {"foundations","planning","jepa","frontier","surveys","tutorials"}:
        errors.append(f"Invalid category: {r['id']}")
    for key in ("date", "revised", "verified"):
        if key in r and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r[key]):
            errors.append(f"Invalid {key}: {r['id']}")
md_files = list(ROOT.rglob("*.md"))
link_count = 0
for path in md_files:
    body = path.read_text()
    if body.count("```") % 2:
        errors.append(f"Unbalanced code fences: {path.relative_to(ROOT)}")
    for target in re.findall(r"\]\(([^\s)]+)\)", body):
        if urlsplit(target).scheme or target.startswith("#"):
            continue
        local = unquote(target.split("#")[0])
        if local:
            link_count += 1
            resolved = (path.parent / local).resolve()
            if ROOT not in resolved.parents or not resolved.exists():
                errors.append(f"Broken local link: {path.relative_to(ROOT)} -> {target}")
svg_files = list((ROOT / "assets").glob("*.svg"))
for svg in svg_files:
    try:
        root = ET.parse(svg).getroot()
        ns = "{http://www.w3.org/2000/svg}"
        if root.find(ns+"title") is None or root.find(ns+"desc") is None:
            errors.append(f"Missing accessibility metadata: {svg.name}")
    except ET.ParseError as exc:
        errors.append(f"Invalid SVG {svg.name}: {exc}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"PASS: {len(resources)} resource records, {len(md_files)} Markdown files, {link_count} local links, {len(svg_files)} SVGs.")
print("External URL availability, equation rendering, and Mermaid rendering are not tested by this offline check.")
