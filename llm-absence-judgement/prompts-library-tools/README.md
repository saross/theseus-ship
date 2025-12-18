# Prompts Library: Tool Research

This directory contains the versioned prompts used for LLM-assisted tool research in the Absence of Judgement project.

## Prompt Evolution

The prompts evolved through multiple iterations (v1-v8) as we refined the methodology based on LLM behaviour observations.

### Current Versions (Production)

| File | Purpose | Version |
|------|---------|---------|
| `01-tool-discovery.tex` | Discover tools mentioned in academic journal articles | v1 (stable) |
| `02-tool-metadata-v8.tex` | Collect comprehensive metadata for discovered tools | v8 (current) |
| `03-tool-evidence-v7.tex` | Gather "evidence of life" for tool sustainability analysis | v7 (current) |

### Historical Versions

Version history for metadata and evidence prompts is preserved in subdirectories:

- `tool-metadata/` — Earlier metadata prompt versions
- `tool-evidence/` — Earlier evidence prompt versions
- `system-prompts/` — System prompt variations tested

### Supporting Files

- `00-lit-review-prompt.tex` — Literature review prompt (exploratory)
- `openarchaeo-preliminary/` — Prompts for OpenArchaeo baseline comparison

## Prompt Design Notes

### Tool Discovery (v1)

The discovery prompt emphasises:

- Research-specific software (not generic platforms)
- Active data processing (not static display)
- Archaeology and historical sciences focus

### Metadata Collection (v8)

Key refinements through versions:

- Added explicit "do not ask questions" instruction (v3)
- Enhanced version tracking requirements (v5)
- Improved handling of commercial software repurposed for research (v7)
- Final cleanup and edge case handling (v8)

### Evidence of Life (v7)

Collects sustainability indicators:

- Repository activity (commits, issues, releases)
- Citation patterns
- Community engagement
- Maintenance status

## Usage

These prompts were primarily used with:

- **ChatGPT Deep Research** — Discovery and evidence collection
- **Claude Research** — Metadata collection (selected for production)
- **OpenAI o3** — Comparison runs
- **Perplexity** — Sample verification runs

See `docs/handover/` for detailed methodology documentation.
