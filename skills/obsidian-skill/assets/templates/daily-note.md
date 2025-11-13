---
date: {{date:YYYY-MM-DD}}
tags: [daily-note]
---

# {{date:YYYY-MM-DD dddd}}

[[{{date-1d:YYYY-MM-DD}}|<- Yesterday]] | [[{{date+1d:YYYY-MM-DD}}|Tomorrow ->]]

## Tasks

### High Priority
- [ ]

### Today's Tasks
- [ ]

### Waiting On
- [ ]

## Meetings
-

## Notes

## Reflections

---

## Created Today
```dataview
LIST
WHERE file.cday = date(this.date)
SORT file.ctime DESC
```

## Modified Today
```dataview
LIST
WHERE file.mday = date(this.date) AND file.cday != date(this.date)
SORT file.mtime DESC
```