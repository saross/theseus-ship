# Plan: Thematic Extraction from Chat Evidence

**Status**: Awaiting Brian's ChatGPT export before execution
**Created**: 2025-12-14

## Objective

Extract themes from ~150 conversation files that provide evidence for the paper "An Absence of Judgment: AI's Limitations in Deep Research Tasks".

## Context

**Paper Framework**: Three dimensions of judgment failure:

1. **Epistemic humility** - recognising knowledge boundaries
2. **Inductive/abductive reasoning** - ampliative reasoning, "Peircean surprise"
3. **Correspondence with reality** - grounding in world beyond text

**Unifying concept**: "Technoscholasticism" - privileging textual authority over critical assessment

**Evidence Sources**:

| Source | Files | Status |
|--------|-------|--------|
| Shawn Claude | 128 | Ready |
| Shawn ChatGPT | 44 | Ready |
| Brian Claude MD | 47 | Ready |
| Brian ChatGPT | — | **Pending** |
| Brian PDFs | 10 | Ready |
| Audio transcripts | 1 (transcripts.tex) | Ready |

**Note (2025-12-14):** Shawn Claude expanded from 51→128 after extracting 77 v8 tool metadata conversations. Shawn ChatGPT expanded from 41→44 after extracting 3 tool discovery conversations that were accidentally not in the project.

## Theme Taxonomy

### A. Failure Patterns (Evidence of Judgment Absence)

| Code | Theme | Description |
|------|-------|-------------|
| `TEMP` | Temporality blindness | Cannot reason about time, useful absences |
| `RAND` | Random walk accumulation | Fixed effort regardless of task demands |
| `SCOP` | Scope-confabulation | Quality inversely correlates with scope |
| `VIBE` | Vibes-based operation | Opaque termination criteria |
| `FABR` | Wholesale fabrication | Complete invention of sources/tools |

### B. Success Patterns (Evidence of Bounded Utility)

| Code | Theme | Description |
|------|-------|-------------|
| `MECH` | Mechanical tasks | Success at bounded, judgment-free tasks |
| `MTCH` | Model-task matching | Different models suit different tasks |
| `SCAF` | Scaffolding effect | Prompt engineering compensates for limitations |
| `BOUN` | Judgment boundary | Clear demarcation of success/failure zones |

### C. Methodological Themes

| Code | Theme | Description |
|------|-------|-------------|
| `PROM` | Prompt evolution | V1-V8 iterations and refinements |
| `EVAL` | Quality evaluation | Slop analysis, verification processes |
| `COMP` | Model comparison | Cross-model testing results |

## Approach: Category-First with Theme Tagging

### Phase 1: Organise by Research Lifecycle Stage

Use existing category codes to group conversations:

1. **LIT** - Literature discovery conversations
2. **DISC** - Tool discovery (journal scanning)
3. **META** - Metadata collection (V1-V8 runs)
4. **EVID** - Evidence-of-life searches
5. **COMP** - Model comparison tests
6. **WRIT** - Paper writing/drafting
7. **METH** - Methodology discussions

### Phase 2: Within-Category Theme Extraction

For each category, apply human-in-the-loop workflow (documented in `/grimoire/human-in-the-loop-review.md`):

1. **Automated scan** - Keyword search for theme indicators
2. **Calibration sample** - User reviews 3-5 representative conversations
3. **Pattern extraction** - Document recognition criteria
4. **Assisted completion** - AI pre-fills theme tags with confidence
5. **User validation** - Final approval of theme assignments

### Phase 3: Generate Evidence Index

Create structured output in `/planning/theme-evidence-index.md`.

Format per theme:

```markdown
## FABR: Wholesale Fabrication

### Definition

Complete invention of articles, tools, or sources (not mere name confusion)

### Evidence Sources

1. `extracted-chatgpt-shawn/2025-02-25_v7-[tool].md` - [specific example]
2. `transcripts.tex` lines 500-550 - [Brian reflection on fabrication]
3. `extracted-claude-brian-md/2025-02-12_*.md` - [documented failure]

### Key Quotes

> "[verbatim quote with source reference]"
```

### Phase 4: Cross-Reference with Paper Structure

Map evidence to paper sections:

- **Section 2**: Theoretical framework (judgment dimensions)
- **Section 3**: Methodology (autoethnographic approach)
- **Section 4**: Findings (failure patterns with evidence)
- **Section 5**: Discussion (technoscholasticism synthesis)

## Implementation Steps

1. **Create theme evidence index file** (`/planning/theme-evidence-index.md`)
2. **Categorise all 148 conversations** by lifecycle stage (LIT/DISC/META/EVID/COMP/WRIT/METH)
3. **Extract themes from HIGH-priority categories first**:
   - META (40+ files) - richest source of failure/success patterns
   - COMP (~10 files) - model comparison evidence
   - METH - methodology insights including prompt evolution
4. **Process transcripts.tex** - Extract theoretical reflections and model evaluations
5. **Process Brian's PDFs** - Section planning discussions
6. **Synthesise evidence index** - Consolidate findings with citations
7. **Integrate Brian's ChatGPT export** - Tool discovery runs and "extreme fail" JOAD run

## Outputs

1. `/planning/theme-evidence-index.md` - Structured evidence citations per theme
2. `/planning/conversation-categories.md` - All conversations assigned to lifecycle stages
3. Updates to `/grimoire/human-in-the-loop-review.md` if workflow refinements emerge

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Missing Brian's ChatGPT (contains JOAD failures) | Document gaps, integrate when available |
| Theme overlap/ambiguity | Define clear boundaries in taxonomy |
| Large volume (148 files) | Prioritise by category, batch processing |

## Dependencies

- [x] Shawn's Claude and ChatGPT exports extracted
- [x] Brian's Claude exports converted to MD
- [ ] **Brian's ChatGPT export** - contains critical failure evidence (JOAD "extreme fail" run with 15 hallucinations, tool discovery runs)
- [ ] User validation at calibration checkpoints
