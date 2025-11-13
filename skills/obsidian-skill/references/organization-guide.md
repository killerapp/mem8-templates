# Organization Best Practices - Reference Guide

## Quick Reference: Folder Structures

### ACE Framework (Recommended)
```
Atlas/          # Knowledge maps, ideas, reference
Calendar/       # Daily notes, time-based entries
Efforts/        # Projects, goals, active work
```
**Use when**: Want structure mapped to human thinking (Space, Time, Importance)

### FINVA (Workflow-Based)
```
Fleeting/       # Quick captures (review weekly)
In Progress/    # Active work
Notes/          # Completed permanent notes
Views/          # MOCs
Archives/       # Old projects
```
**Use when**: Want workflow-stage organization

### Zettelkasten (Research)
```
Fleeting/       # Temporary captures
Permanent/      # Atomic evergreen notes
```
**Use when**: Research-heavy work, need atomic notes

## Maps of Content (MOCs)

Navigation hub notes that link related content:

```markdown
# Topic MOC

## Overview
Brief description

## Sections
- [[Note 1]]
- [[Note 2]]

## Related
- [[Related MOC]]
```

**When to create**: 5+ related notes, mental squeeze point, need navigation

### Automated MOCs with Dataview

```markdown
## Active Projects
```dataview
TABLE status, priority
FROM #project
WHERE status = "active"
```
```

## Tag Strategies

**Hierarchical tags**: `#project/active/high-priority`

**Common conventions**:
- Status: `#status/active`, `#status/completed`
- Type: `#type/project`, `#type/note`
- Priority: `#priority/high`, `#priority/low`

## Best Practices

1. **Minimal folders** (3-7 top-level)
2. **Organize by TYPE not TOPIC** - let links connect topics
3. **Link liberally** - connections over categories
4. **Design for worst day** - must work when tired
5. **Let structure emerge** - don't force premature organization

## Resources

- **ACE Framework**: https://forum.obsidian.md/t/the-ultimate-folder-system-a-quixotic-journey-to-ace/63483
- **FINVA**: https://obsidian.rocks/how-i-use-folders-in-obsidian/
- **Zettelkasten**: https://obsidian.rocks/getting-started-with-zettelkasten-in-obsidian/
- **MOCs**: https://obsidian.rocks/maps-of-content-effortless-organization-for-notes/