---
name: obsidian-auto-context
description: >
  Automatically captures Hermes agent session context — research findings,
  decisions, tool outputs, and task summaries — into an Obsidian vault as
  linked, tagged Markdown notes. Supports daily notes, backlinks, and
  redaction of secrets. Turns disposable chat sessions into a permanent,
  searchable second brain.
version: 1.0.0
author: SkillForge Labs
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [obsidian, memory, second-brain, research, productivity, context]
    category: productivity
    requires_toolsets: [obsidian, file, memory]
    fallback_for_toolsets: [memory]
---

# Obsidian Auto-Context

Capture what your agent learns before it disappears. This skill writes the
substance of each Hermes session — key findings, decisions, and action items —
into your Obsidian vault as clean, linked Markdown, so future sessions (and
future you) can retrieve it instead of rebuilding context from scratch.

## Why this exists

Agent sessions are brilliant and ephemeral. The reasoning evaporates when the
chat ends. This skill makes the output survive: every research pass becomes a
dated, tagged note in your vault, wiki-linked to related entities, and safe
(secrets are stripped before anything is written to disk).

## When to use

- End of a research or analysis session
- After making or recording a decision
- After creating or updating a skill or workflow
- On a scheduled cron summary (daily/weekly rollup)
- Manually, any time: `obsidian-save`

## What it writes

For each capture, one Markdown note containing:

- **Frontmatter** — `date`, `tags`, `source: hermes`, `session`
- **Summary** — 2–4 sentence synthesis of the session
- **Key findings** — bulleted, each with its source/link where available
- **Decisions** — what was decided and why (if any)
- **Action items** — `- [ ]` checkboxes
- **Links** — `[[wiki-links]]` to entities mentioned (people, tools, tickers, projects)

Notes land in `<vault>/10-Sessions/YYYY-MM-DD/` by default and are appended to
that day's daily note under a `## Sessions` heading.

## How it works

1. At session end (or on trigger), the skill collects the session transcript
   and any tool results already in context.
2. It runs `references/redact.py` over the text to strip secrets
   (API keys, tokens, `.env`-style values, emails if configured).
3. It asks the model to produce the structured note above.
4. It writes the note via the `obsidian` toolset (or the `file` toolset,
   pointed at the vault path) and links it into the daily note.

## Configuration

Set these in your Hermes config or `.hermes.md`:

```
OBSIDIAN_VAULT_PATH   absolute path to your vault (required)
SESSIONS_FOLDER       default: 10-Sessions
REDACT_EMAILS         true/false, default false
DAILY_NOTE_FOLDER     default: 00-Daily
```

## Example output

```markdown
---
date: 2026-07-18
tags: [hermes, research, trading-tools]
source: hermes
session: 20260718_research
---

# Session — Backtesting frameworks scan

**Summary**
Compared three open-source backtesting engines for an equities workflow.
VectorBT wins on speed for parameter sweeps; NautilusTrader for event-driven
validation. Filed a decision to use both in sequence.

## Key findings
- VectorBT: vectorized, fast sweeps — [docs](https://vectorbt.dev)
- NautilusTrader: event-driven, venue-agnostic adapters

## Decisions
- Sweep in VectorBT -> validate survivors in Nautilus.

## Action items
- [ ] Clone both repos and run the sample notebooks

## Links
[[VectorBT]] · [[NautilusTrader]] · [[Backtesting]]
```

## Install

```
hermes skills install github.com/SkillForgeLabs/obsidian-auto-context
```

Then set `OBSIDIAN_VAULT_PATH` and run `obsidian-save` at the end of any session.

---

Built by **SkillForge Labs** — tools & context systems for AI-agent builders.
Free and MIT-licensed. If it saves you time, a star on the repo helps others find it.
