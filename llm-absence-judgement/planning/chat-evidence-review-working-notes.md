# Chat Evidence Review: Working Notes

*Created: 9 December 2025*
*Status: Paused — to resume in new session*

---

## Context

Planning a systematic review of all LLM chat evidence for the "An Absence of Judgement" paper. This document captures progress and decisions to enable resumption.

---

## Current State of Evidence

### Shawn's Chats (extracted and organised)

| Location | Count | Format | Status |
|----------|-------|--------|--------|
| `evidence/chats/saved-chats/extracted-chatgpt/` | 42 | Markdown (official export) | Extracted, README exists |
| `evidence/chats/saved-chats/extracted-claude/` | 41 | Markdown (bulk export) | Extracted, README exists |
| `evidence/chats/saved-chats/` (root) | 15 | PDF + Markdown (one-offs) | Renamed for clarity |
| `evidence/chats/BBS-SAR-google-chat-history.md` | 1 file | Markdown (6,230 lines) | Analysed in results-tools/ |

### Brian's Chats (pending)

**Major development**: Brian is providing his chat logs in the same JSON export format (Claude bulk export + ChatGPT official export). This means:
- We can use the same extraction scripts (`scripts/parse_claude_export.py`, `scripts/parse_chatgpt_export.py`)
- Will need to filter by Brian's project/date range
- Output should go to `extracted-chatgpt-brian/` and `extracted-claude-brian/` (or similar)

### Existing Documentation

- `evidence/chats/claude_prompt_development_corpus_index.md` — Indexes 40 Claude conversations only
- `results-tools/chat-analysis/google-chat-analysis.md` — Thematic analysis of Google Chat
- `prompts-library-tools/` — Finalised prompts (v8 metadata, v7 evidence, etc.)

---

## Planned Deliverables

1. **Unified corpus index** (`llm-chat-evidence-corpus-index.md` or similar)
   - Rename from Claude-only to cover all platforms
   - Add ChatGPT conversations (Shawn's + Brian's)
   - Add Claude conversations (Brian's)
   - Categorise by workflow phase (LIT, DISC, META, EVID, COMP, WRIT)

2. **Reconciliation document** (`prompt-evolution-reconciliation.md`)
   - Map evidence chats → finalised prompts in prompts-library-tools/
   - Document prompt version evolution (v1→v8)
   - Identify which chats correspond to which prompt iterations

3. **Methodological insights extraction**
   - Review all chats for information not yet in paper
   - Document patterns across models
   - Extract failure taxonomies from evidence

---

## Open Questions (need user input)

1. **Scope**: Should Brian's conversations be fully indexed alongside Shawn's, or kept in separate sections?

2. **Detail level**: Current index has Synopsis + Key Themes + Notable + UUID + URL. Should we:
   - Keep this format?
   - Simplify (minimal: date + title + category)?
   - Enhance (add: model used, prompt version, output files, paper section relevance)?

3. **Google Chat handling**: Cross-reference to existing analysis, or include key excerpts inline?

---

## Technical Notes

### Extraction Scripts Available

```
scripts/parse_claude_export.py
scripts/parse_chatgpt_export.py
```

Both filter by:
- Project ID (gizmo_id for ChatGPT, UUID whitelist for Claude)
- Date range (configurable)

For Brian's exports, will need to:
- Identify his project gizmo_id (if filtering ChatGPT by project)
- Or filter by date range only
- Possibly create separate UUID whitelist for Claude

### File Naming Convention

Established pattern for saved-chats:
- `[Author]-[descriptive-name].md` (e.g., `Brian-deep-research-prompt.md`)
- `[Model]-[topic].pdf` (e.g., `Opus-section-4-outline.pdf`)
- Extracted folders: `extracted-chatgpt/`, `extracted-claude/`

For Brian's extracts, suggest:
- `extracted-chatgpt-brian/`
- `extracted-claude-brian/`

Or unified with author prefix in filenames.

---

## Categorisation Scheme (proposed)

### Primary Categories (Workflow Phase)

| Code | Phase | Description |
|------|-------|-------------|
| `LIT` | Literature Review | Literature discovery, bibliographic work |
| `DISC` | Tool Discovery | Journal scanning, tool identification |
| `META` | Metadata Collection | V1-V8 prompt development, tool metadata |
| `EVID` | Evidence Collection | Evidence-of-life searches |
| `COMP` | Model Comparison | Cross-model testing, FAIMS control tests |
| `WRIT` | Paper Writing | Section drafting, theoretical framework |
| `METH` | Methodology | Prompt refinement discussions, workflow design |

### Secondary Categories (Function)

| Code | Function | Description |
|------|----------|-------------|
| `PROD` | Production run | Actual data collection using finalised prompt |
| `DEV` | Development | Prompt iteration, testing, refinement |
| `FAIL` | Documented failure | Explicitly failed or problematic run |
| `TEST` | Comparative test | Model comparison using control tool/task |

---

## Plan File Location

Detailed plan draft saved at:
```
/home/shawn/.claude/plans/jazzy-hopping-lamport.md
```

This contains more extensive breakdown of phases and methodology.

---

## Next Steps When Resuming

1. **Receive Brian's exports** — Extract using existing scripts
2. **Clarify open questions** — Scope, detail level, Google Chat handling
3. **Begin systematic review** — Start with ChatGPT conversations (largest gap in current index)
4. **Build unified index** — Merge Claude + ChatGPT + one-offs
5. **Create reconciliation document** — Map chats to prompts
6. **Extract new insights** — Review for undocumented methodological findings

---

## Methodological Observations

### Single-task prompt design (22 December 2025)

Evidence for why prompts should focus on one task at a time: the metadata prompt repeatedly states that a tool "has no archaeological uses", yet the evidence prompt (run on the same tool) finds numerous archaeological uses. This contradiction suggests that when a prompt attempts to handle multiple assessment tasks simultaneously, the model may make premature judgements that foreclose deeper investigation. Separating the metadata collection task from the evidence-of-life search allows the model to pursue each task without the other's conclusions contaminating its reasoning.

### JOSS trial run TODO placeholders (23 December 2025)

The `tool-discovery-granular.csv` file contains 34 entries from the JOSS "fail-possible" run (lines 243-276) with `TODO` in the URL_DOI column instead of actual DOIs. These entries document a trial where the LLM was asked to identify archaeological tools published in the Journal of Open Source Software. The results showed a ~40% confabulation rate—the model invented plausible-sounding tool names that don't exist (e.g., "RACER", "ChronCluster", "archCandy").

**Decision**: Leave the TODO placeholders as-is rather than looking up actual DOIs for confirmed tools. The incomplete data is itself evidence of the failure mode: the LLM provided tool names and years but failed to provide verifiable DOIs, making independent verification difficult. This documents how confabulated references can appear superficially credible (correct journal, plausible year, real-sounding name) while lacking the specificity needed for verification.

---

## Related Files

- Plan draft: `/home/shawn/.claude/plans/jazzy-hopping-lamport.md`
- Existing Claude index: `evidence/chats/claude_prompt_development_corpus_index.md`
- Google Chat analysis: `results-tools/chat-analysis/google-chat-analysis.md`
- Extraction scripts: `scripts/parse_claude_export.py`, `scripts/parse_chatgpt_export.py`
