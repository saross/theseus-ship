# LLM Absence Judgement

Research project investigating Large Language Model (LLM) capabilities and limitations in autonomous research tasks, with a focus on the discovery and documentation of archaeological and historical software tools.

## Project Overview

**Paper Title**: "An Absence of Judgment: AI's Limitations in Deep Research Tasks"

**Authors**: Brian Ballsun-Stanton (BBS), Shawn A. Ross (SAR)

**Core Argument**: LLMs lack three crucial dimensions of judgement—epistemic humility, inductive capacity, and correspondence with reality—which limits them to "mundane utility" rather than autonomous research. We propose "technoscholasticism" as a framework: like medieval scholastics, these tools privilege textual authority over critical assessment of knowledge claims.

**Methodology**: Autoethnographic investigation of frontier models (February–May 2025) applied to a real research task: compiling a dataset of archaeological/historical software tools to study software longevity and sustainability.

## Repository Structure

```text
llm-absence-judgement/
├── absence-judgement.tex      # Main manuscript (LaTeX)
├── slides.tex                 # Presentation slides
├── *.bib                      # Bibliography files
│
├── docs/handover/             # Detailed handover documentation
├── planning/                  # Session tracking, to-dos
├── grimoire/                  # Workflow patterns for Claude Code
│
├── prompts-library-tools/     # Versioned prompts (v1-v8)
├── preliminary-work/          # Evidence corpus and chat transcripts
├── results-tools/             # Output data and verification
├── scripts/                   # Python analysis scripts
├── text-revisions/            # Draft sections and revisions
└── archive/                   # Superseded files
```

## Quick Start

- **For new contributors**: See `docs/handover/handoff-to-claude-code.md`
- **For data analysis**: See `results-tools/README.md`
- **For methodology**: See `prompts-library-tools/`
- **For detailed manifests**: See `docs/handover/project-data-manifest.md`

## Key Files

### Results

- `results-tools/02-tool-metadata.xlsx` — Comprehensive tool metadata (97 tools)
- `results-tools/tool-discovery-granular.csv` — 350 discovery events with verification
- `results-tools/tool-discovery-summary.csv` — 244 unique tools (de-duplicated)

### Evidence Corpus

- `preliminary-work/evidence/chats/` — LLM conversation transcripts
- `preliminary-work/evidence/` — Supporting evidence files

### Prompts

- `prompts-library-tools/01-tool-discovery.tex` — Tool discovery prompt
- `prompts-library-tools/02-tool-metadata-v8.tex` — Metadata collection prompt (current)
- `prompts-library-tools/03-tool-evidence-v7.tex` — Evidence of life prompt (current)

## Key Quantitative Findings

| Metric | Value |
|--------|-------|
| Raw discoveries | 244 unique tools |
| Verified as research tools | 156 (after manual verification) |
| Confabulations identified | 36 |
| Misattributed (generic software) | 52 |
| Metadata success rate | 92% (90/98) |
| Evidence rows collected | 1,179 |

## Contributors

- **Brian Ballsun-Stanton** (BBS) — Lead author, methodology design
- **Shawn A. Ross** (SAR) — Co-author, data collection

## Licence

See manuscript for licensing terms.
