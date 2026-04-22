#!/usr/bin/env python3
"""
Granola sync: extracts completed meeting notes from Granola's local cache
and writes each one to memory/granola/YYYY-MM-DD-slug.md.

Idempotent — if a file for a doc already exists with the same updated_at,
it is skipped. Otherwise it's overwritten.
"""
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

CACHE = Path.home() / "Library" / "Application Support" / "Granola" / "cache-v6.json"
OUT_DIR = Path.home() / ".openclaw" / "workspace" / "memory" / "granola"
INDEX_FILE = OUT_DIR / ".index.json"

def slugify(s, max_len=50):
    s = re.sub(r'[^\w\s-]', '', s or 'untitled').strip()
    s = re.sub(r'[\s_-]+', '-', s).lower()
    return s[:max_len].rstrip('-')

def extract_prosemirror_text(node):
    """Walk a ProseMirror JSON tree and return plain text with basic markdown."""
    if not isinstance(node, dict):
        return ''
    t = node.get('type')
    content = node.get('content', [])
    text = node.get('text', '')

    if t == 'text':
        return text
    if t == 'paragraph':
        inner = ''.join(extract_prosemirror_text(c) for c in content)
        return inner + '\n\n'
    if t in ('heading',):
        level = node.get('attrs', {}).get('level', 2)
        inner = ''.join(extract_prosemirror_text(c) for c in content)
        return '#' * level + ' ' + inner + '\n\n'
    if t == 'bulletList':
        return ''.join(extract_prosemirror_text(c) for c in content) + '\n'
    if t == 'orderedList':
        return ''.join(extract_prosemirror_text(c) for c in content) + '\n'
    if t == 'listItem':
        inner = ''.join(extract_prosemirror_text(c) for c in content).rstrip()
        return '- ' + inner + '\n'
    if t == 'hardBreak':
        return '\n'
    # Fallback: recurse
    return ''.join(extract_prosemirror_text(c) for c in content)

def notes_to_markdown(notes):
    """Granola stores notes as ProseMirror. Convert to markdown."""
    if not notes:
        return ''
    if isinstance(notes, str):
        return notes
    if isinstance(notes, dict):
        # notes is usually {type: 'doc', content: [...]}
        return extract_prosemirror_text(notes).strip()
    return ''

def format_doc(doc):
    title = doc.get('title') or 'Untitled'
    created = doc.get('created_at', '')
    updated = doc.get('updated_at', '')
    summary = doc.get('summary') or ''
    notes_markdown = doc.get('notes_markdown') or ''
    notes = doc.get('notes') or {}
    notes_plain = doc.get('notes_plain') or ''
    people = doc.get('people') or {}
    gcal = doc.get('google_calendar_event') or {}

    # Derive markdown content
    body = notes_markdown or notes_to_markdown(notes) or notes_plain

    lines = [f'# {title}', '']
    if created:
        try:
            dt = datetime.fromisoformat(created.replace('Z','+00:00'))
            lines.append(f'- **Date:** {dt.strftime("%Y-%m-%d %H:%M UTC")}')
        except Exception:
            lines.append(f'- **Date:** {created}')

    # Attendees
    attendee_list = gcal.get('attendees') or []
    if attendee_list:
        names = []
        for a in attendee_list:
            names.append(a.get('displayName') or a.get('email') or '')
        names = [n for n in names if n]
        if names:
            lines.append(f'- **Attendees:** {", ".join(names)}')

    lines.append(f'- **Source:** Granola')
    lines.append(f'- **Doc ID:** `{doc.get("id", "")}`')
    lines.append('')

    if summary:
        lines.append('## Summary')
        lines.append(summary.strip())
        lines.append('')

    if body.strip():
        lines.append('## Notes')
        lines.append(body.strip())
        lines.append('')

    return '\n'.join(lines).rstrip() + '\n'

def should_export(doc):
    """Only export meetings that have content."""
    if doc.get('deleted_at'):
        return False
    has_content = (doc.get('summary') or doc.get('notes_markdown') or
                   (doc.get('notes') and doc['notes']) or doc.get('notes_plain'))
    return bool(has_content)

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if not CACHE.exists():
        print(f'Granola cache not found: {CACHE}', file=sys.stderr)
        sys.exit(1)

    with CACHE.open() as f:
        data = json.load(f)

    docs = data.get('cache', {}).get('state', {}).get('documents', {})

    # Load processing index
    index = {}
    if INDEX_FILE.exists():
        try:
            index = json.loads(INDEX_FILE.read_text())
        except Exception:
            index = {}

    exported = 0
    skipped = 0
    for doc_id, doc in docs.items():
        if not should_export(doc):
            skipped += 1
            continue

        updated_at = doc.get('updated_at', '')
        prev = index.get(doc_id, {})
        if prev.get('updated_at') == updated_at:
            skipped += 1
            continue

        # Build filename: YYYY-MM-DD-slug.md
        created = doc.get('created_at', '')
        try:
            date_prefix = datetime.fromisoformat(created.replace('Z','+00:00')).strftime('%Y-%m-%d')
        except Exception:
            date_prefix = datetime.now().strftime('%Y-%m-%d')
        slug = slugify(doc.get('title') or 'meeting')
        filename = f'{date_prefix}-{slug}.md'
        out_path = OUT_DIR / filename

        content = format_doc(doc)
        out_path.write_text(content)

        index[doc_id] = {'updated_at': updated_at, 'filename': filename}
        exported += 1
        print(f'✓ {filename}')

    INDEX_FILE.write_text(json.dumps(index, indent=2))
    print(f'\n{exported} exported, {skipped} skipped')

if __name__ == '__main__':
    main()
