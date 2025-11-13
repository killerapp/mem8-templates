# Task Workflows - Reference Guide

## Essential Plugins

- **Daily Notes** (Core)
- **Templater** (Community) - Templates with JavaScript
- **Tasks** (Community) - Vault-wide task management
- **Dataview** (Community) - Query engine
- **Day Planner** (Community) - Time blocking

Install from: Settings → Community Plugins

## Task Syntax (Tasks Plugin)

```markdown
- [ ] Basic task
- [ ] Due date 📅 2025-11-15
- [ ] Start date 🛫 2025-11-13
- [ ] Scheduled date ⏳ 2025-11-14
- [ ] High priority ⏫
- [ ] Low priority 🔽
- [ ] Recurring 🔁 every week
- [x] Completed ✅ 2025-11-12
```

## Query Tasks

````markdown
```tasks
not done
due before in 3 days
group by due
```
````

**Common queries**:
- `not done` - Incomplete tasks
- `priority is high` - High priority
- `path includes Projects/X` - From specific path
- `is recurring` - Recurring tasks

## Time Blocking (Day Planner)

**Setup**: Settings → Day Planner → Command Mode

**Format** (24-hour time):
```markdown
## Today's Schedule

- [ ] 07:00 Morning Routine
- [ ] 08:00 Deep Work
- [ ] 10:00 Meeting
```

**Features**: Timeline view, status bar, drag-and-drop

## GTD Implementation

**Folder structure**:
```
Capture/        # Inbox
Projects/       # Active projects
@home/          # Context lists
@work/
@someday/
```

**Workflow**: Capture → Process → Organize → Review → Do

**Auto lists with Dataview**:
````markdown
## Next Actions - @work
```dataview
TASK
WHERE contains(text, "@work")
WHERE !completed
```
````

## Daily/Weekly Workflow

**Morning Routine**:
1. Open daily note (hotkey or calendar)
2. Review yesterday
3. Set today's priorities (3-5 tasks)
4. Schedule time blocks

**Evening Review**:
1. Check off completed tasks
2. Capture reflections
3. Draft tomorrow's note

**Weekly Review**:
1. Create weekly note
2. Review daily notes
3. Document Rose/Thorn/Bud
4. Set next week's focus (2-3 priorities)
5. Update project statuses

## Templates

Available in `assets/templates/`:
- `daily-note.md` - Daily note structure
- `weekly-review.md` - Weekly review format
- `project.md` - Project note template

## Resources

- **Tasks Plugin**: https://publish.obsidian.md/tasks
- **Dataview**: https://blacksmithgu.github.io/obsidian-dataview/
- **GTD Guide**: https://facedragons.com/productivity/set-up-gtd-in-obsidian/
- **Time Blocking**: https://thesweetsetup.com/timeblocking-in-obsidian/