#!/usr/bin/env python3
"""
Obsidian Vault Health Check Script

This script analyzes an Obsidian vault for common issues:
- Broken wikilinks
- Orphaned notes (no incoming or outgoing links)
- Missing frontmatter
- Duplicate titles
- Stub notes (less than 100 words)

Usage:
    python vault_health.py /path/to/vault

Output:
    Prints a health report to stdout with issues categorized and counted
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Set, Dict, List, Tuple

def extract_wikilinks(content: str) -> Set[str]:
    """Extract all wikilinks from note content."""
    # Match [[Note]] and [[Note|Display]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return set(re.findall(pattern, content))

def get_note_files(vault_path: Path) -> List[Path]:
    """Get all markdown files in vault, excluding .obsidian directory."""
    notes = []
    for file in vault_path.rglob('*.md'):
        if '.obsidian' not in file.parts:
            notes.append(file)
    return notes

def check_frontmatter(content: str) -> bool:
    """Check if note has YAML frontmatter."""
    return content.startswith('---\n') or content.startswith('---\r\n')

def count_words(content: str) -> int:
    """Count words in markdown content (excluding frontmatter and code blocks)."""
    # Remove frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]

    # Remove code blocks
    content = re.sub(r'```[\s\S]*?```', '', content)

    # Count words
    words = re.findall(r'\b\w+\b', content)
    return len(words)

def analyze_vault(vault_path: str) -> Dict:
    """Analyze vault and return health report."""
    vault = Path(vault_path)
    if not vault.exists():
        print(f"Error: Vault path does not exist: {vault_path}")
        sys.exit(1)

    notes = get_note_files(vault)

    # Data structures
    all_links = defaultdict(set)  # file -> set of links
    all_titles = {}  # file -> title (from filename)
    broken_links = defaultdict(set)  # file -> set of broken links
    missing_frontmatter = []
    stubs = []  # (file, word_count)
    duplicate_titles = defaultdict(list)  # title -> [files]

    # Build note index
    note_names = {}  # Note name -> file path
    for note_file in notes:
        note_name = note_file.stem
        note_names[note_name] = note_file
        all_titles[note_file] = note_name
        duplicate_titles[note_name].append(note_file)

    # Analyze each note
    for note_file in notes:
        try:
            content = note_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Warning: Could not read {note_file}: {e}")
            continue

        # Check frontmatter
        if not check_frontmatter(content):
            missing_frontmatter.append(note_file)

        # Check word count
        word_count = count_words(content)
        if word_count < 100:
            stubs.append((note_file, word_count))

        # Extract and check links
        links = extract_wikilinks(content)
        all_links[note_file] = links

        for link in links:
            # Handle links with heading references
            link_target = link.split('#')[0].strip()
            if link_target and link_target not in note_names:
                broken_links[note_file].add(link)

    # Find orphaned notes (no incoming or outgoing links)
    linked_notes = set()
    for links in all_links.values():
        for link in links:
            link_target = link.split('#')[0].strip()
            if link_target in note_names:
                linked_notes.add(note_names[link_target])

    orphaned = []
    for note_file in notes:
        has_outgoing = len(all_links[note_file]) > 0
        has_incoming = note_file in linked_notes

        if not has_outgoing and not has_incoming:
            orphaned.append(note_file)

    # Find actual duplicates (more than one file with same name)
    true_duplicates = {title: files for title, files in duplicate_titles.items() if len(files) > 1}

    return {
        'total_notes': len(notes),
        'broken_links': dict(broken_links),
        'orphaned_notes': orphaned,
        'missing_frontmatter': missing_frontmatter,
        'stubs': stubs,
        'duplicate_titles': true_duplicates,
    }

def print_report(results: Dict, vault_path: str):
    """Print formatted health report."""
    print("=" * 60)
    print(f"OBSIDIAN VAULT HEALTH REPORT")
    print(f"Vault: {vault_path}")
    print("=" * 60)
    print()

    print(f"Total Notes Analyzed: {results['total_notes']}")
    print()

    # Broken Links
    if results['broken_links']:
        print(f"🔴 BROKEN LINKS: {len(results['broken_links'])} notes with broken links")
        for note, links in list(results['broken_links'].items())[:10]:  # Show first 10
            print(f"  - {note.relative_to(Path(vault_path))}")
            for link in list(links)[:3]:  # Show first 3 links per note
                print(f"    → [[{link}]]")
        if len(results['broken_links']) > 10:
            print(f"  ... and {len(results['broken_links']) - 10} more")
        print()
    else:
        print("✅ No broken links found")
        print()

    # Orphaned Notes
    if results['orphaned_notes']:
        print(f"🟡 ORPHANED NOTES: {len(results['orphaned_notes'])} notes with no connections")
        for note in results['orphaned_notes'][:10]:  # Show first 10
            print(f"  - {note.relative_to(Path(vault_path))}")
        if len(results['orphaned_notes']) > 10:
            print(f"  ... and {len(results['orphaned_notes']) - 10} more")
        print()
    else:
        print("✅ No orphaned notes found")
        print()

    # Missing Frontmatter
    if results['missing_frontmatter']:
        print(f"🟡 MISSING FRONTMATTER: {len(results['missing_frontmatter'])} notes")
        for note in results['missing_frontmatter'][:10]:  # Show first 10
            print(f"  - {note.relative_to(Path(vault_path))}")
        if len(results['missing_frontmatter']) > 10:
            print(f"  ... and {len(results['missing_frontmatter']) - 10} more")
        print()
    else:
        print("✅ All notes have frontmatter")
        print()

    # Stubs
    if results['stubs']:
        print(f"🟡 STUB NOTES: {len(results['stubs'])} notes with < 100 words")
        for note, word_count in results['stubs'][:10]:  # Show first 10
            print(f"  - {note.relative_to(Path(vault_path))} ({word_count} words)")
        if len(results['stubs']) > 10:
            print(f"  ... and {len(results['stubs']) - 10} more")
        print()
    else:
        print("✅ No stub notes found")
        print()

    # Duplicate Titles
    if results['duplicate_titles']:
        print(f"🟡 DUPLICATE TITLES: {len(results['duplicate_titles'])} titles with multiple files")
        for title, files in list(results['duplicate_titles'].items())[:5]:  # Show first 5
            print(f"  Title: {title}")
            for file in files:
                print(f"    - {file.relative_to(Path(vault_path))}")
        if len(results['duplicate_titles']) > 5:
            print(f"  ... and {len(results['duplicate_titles']) - 5} more")
        print()
    else:
        print("✅ No duplicate titles found")
        print()

    # Summary
    issues_found = sum([
        len(results['broken_links']),
        len(results['orphaned_notes']),
        len(results['missing_frontmatter']),
        len(results['stubs']),
        len(results['duplicate_titles']),
    ])

    print("=" * 60)
    if issues_found == 0:
        print("✅ VAULT HEALTH: EXCELLENT - No issues found!")
    elif issues_found < 10:
        print(f"🟡 VAULT HEALTH: GOOD - {issues_found} minor issues found")
    elif issues_found < 50:
        print(f"🟡 VAULT HEALTH: FAIR - {issues_found} issues found")
    else:
        print(f"🔴 VAULT HEALTH: NEEDS ATTENTION - {issues_found} issues found")
    print("=" * 60)

def main():
    if len(sys.argv) < 2:
        print("Usage: python vault_health.py /path/to/vault")
        sys.exit(1)

    vault_path = sys.argv[1]
    results = analyze_vault(vault_path)
    print_report(results, vault_path)

if __name__ == '__main__':
    main()
