---
date: {{date:YYYY-[W]WW}}
tags: [weekly-review]
---

# Week {{date:WW}} - {{date:YYYY}}

## Rose (Wins This Week)
-

## Thorn (Challenges)
-

## Bud (Opportunities/Improvements)
-

## This Week's Stats
```dataview
TABLE length(file.tasks.completed) AS "Done", length(file.tasks) AS "Total"
WHERE contains(file.name, "{{date:YYYY-[W]WW}}")
```

## Energy Tracking
What energized me:
-

What depleted me:
-

## Next Week's Focus
1.
2.
3.

## Daily Notes
- [[Monday|{{monday:YYYY-MM-DD}}]]
- [[Tuesday|{{tuesday:YYYY-MM-DD}}]]
- [[Wednesday|{{wednesday:YYYY-MM-DD}}]]
- [[Thursday|{{thursday:YYYY-MM-DD}}]]
- [[Friday|{{friday:YYYY-MM-DD}}]]
- [[Saturday|{{saturday:YYYY-MM-DD}}]]
- [[Sunday|{{sunday:YYYY-MM-DD}}]]

## Active Projects
```dataview
TABLE status, priority
FROM #project
WHERE status = "active"
```