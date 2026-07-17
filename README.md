# Obsidian Auto-Context

**Free Hermes skill that turns disposable agent sessions into a permanent, searchable second brain.**

At the end of any Hermes session, this skill captures the substance — research
findings, decisions, and action items — and writes it into your Obsidian vault
as clean, tagged, wiki-linked Markdown. Secrets are stripped before anything
touches disk. Future sessions retrieve context instead of rebuilding it.

## What you get

- Dated, tagged session notes in your vault
- Auto-appended daily-note rollups
- `[[wiki-links]]` to entities mentioned
- Built-in secret redaction (`references/redact.py`)
- Works on Linux, macOS, Windows

## Install

```
hermes skills install github.com/SkillForge-Labs/obsidian-auto-context
```

Set `OBSIDIAN_VAULT_PATH`, then run `obsidian-save` (or wire it to a
session-end / cron trigger). See `SKILL.md` for full config.

## Why we built it

Agent output is brilliant and ephemeral. The reasoning vanishes when the chat
closes. Compounding memory is the difference between a tool and a system — so
we made the output survive. Free, MIT, no strings.

## About

Built by **[SkillForge Labs](https://x.com/SkillForgeLabs)** — custom AI-agent
builds & tooling for traders and builders. Context systems, skills, automation.

If this saves you time, a ⭐ helps other builders find it. Questions or want a
custom build for your workflow? DM [@SkillForgeLabs](https://x.com/SkillForgeLabs).
