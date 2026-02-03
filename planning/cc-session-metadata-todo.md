# CC Session Metadata Population

## Status: Deferred

Created: 2026-02-03

## Context

49 archived CC sessions in `archive/cc-sessions/theseus-ship/` have
placeholder metadata ("Untitled Session", empty tags, empty three_ps).
A proof-of-concept comparison (2026-02-03) showed that **condensed
summary extraction produces insufficient metadata** for substantive
sessions — full read-throughs are required for quality results.

### PoC Findings

| Session | Turns | Synopsis-only quality |
|---------|-------|-----------------------|
| `179adf8a` (Small, 43 turns) | Gets topic, misses scope | Marginal |
| `93e4d187` (Medium, 112 turns) | Generic, content-free | Insufficient |
| `b80b94c6` (Large, 226 turns) | Misleading, wrong topic | Insufficient |

**Root cause:** Sessions typically begin with orientation ("remind me
what we were working on"), so first-N-messages extraction misses the
actual substance, which emerges mid-session.

## Tasks

### Batch 1: Trivial sessions (programmatic) — ~22 sessions

- [ ] Label 8 empty sessions (0 turns) as "Empty Session"
- [ ] Label 14 agent warmup sessions as "Agent Warmup"
- [ ] Apply via `scripts/apply-session-metadata.py` or similar

These can be done quickly with no manual reading required.

### Batch 2+: Substantive sessions (close reading) — ~27 sessions

Each requires a full read-through. Consider combining with research
into LLM-human interaction patterns (double-duty readings).

**Tiers by size:**

- [ ] 6 small agent sub-sessions (tool work, no human text — need
      assistant message analysis)
- [ ] 11 medium sessions (21–100 turns)
- [ ] 10 large sessions (100+ turns)

**Recommended approach:** Take 2–3 sessions per CC session, using the
`convert_session_to_markdown.py` script to produce readable transcripts.
Generate metadata following `archive/cc-sessions/queries/populate-metadata.md`.

### After metadata is populated

- [ ] Regenerate `CATALOG.json` and `CATALOG.md` via
      `scripts/generate_session_catalog.py`
- [ ] Sync updated archive to `LLM-History-Paper`
- [ ] Commit and push both repos

## Available Tools

| Script | Purpose |
|--------|---------|
| `scripts/extract-session-summaries.py` | Triage: identify trivial vs substantive sessions |
| `scripts/convert_session_to_markdown.py` | Convert JSONL to readable Markdown for close reading |
| `scripts/archive_cc_session.py` | Archive new sessions |
| `scripts/generate_session_catalog.py` | Regenerate CATALOG files |
| `archive/cc-sessions/queries/populate-metadata.md` | Prompt template for metadata generation |
