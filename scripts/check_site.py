#!/usr/bin/env python3
"""Dependency-free static website checks. Run: python3 scripts/check_site.py"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))
ERRORS = []

class Links(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.source = source
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            value = attrs.get(key, "")
            if not value or value.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
                continue
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or value.startswith("//"):
                continue
            target = unquote(parsed.path)
            if not target:
                continue
            resolved = (ROOT / target.lstrip("/") if target.startswith("/") else self.source.parent / target).resolve()
            if not resolved.is_relative_to(ROOT):
                ERRORS.append(f"{self.source.name}: {key} escapes repository: {value}")
            elif resolved.is_dir() and not (resolved / "index.html").is_file():
                ERRORS.append(f"{self.source.name}: directory link lacks index.html: {value}")
            elif not resolved.exists():
                ERRORS.append(f"{self.source.name}: missing local {key}: {value}")

if not HTML_FILES:
    ERRORS.append("No root HTML files found")
for path in HTML_FILES:
    content = path.read_text(encoding="utf-8")
    parser = Links(path)
    try:
        parser.feed(content)
        parser.close()
    except Exception as exc:
        ERRORS.append(f"{path.name}: HTML parsing error: {exc}")
    if path.name == "index.html":
        if "<title" not in content.lower():
            ERRORS.append("index.html: missing title")
        if 'name="viewport"' not in content.lower() and "name='viewport'" not in content.lower():
            ERRORS.append("index.html: missing viewport meta")
if ERRORS:
    print("FAIL — " + str(len(ERRORS)) + " static-site issue(s)")
    for issue in ERRORS:
        print(" - " + issue)
    sys.exit(1)
print(f"PASS — checked {len(HTML_FILES)} HTML files and local asset references")
