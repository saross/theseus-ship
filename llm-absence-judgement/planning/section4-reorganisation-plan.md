# Plan: Reorganise Section 4 (Findings) by Pipeline Stage

**Created**: 2025-01-13
**Status**: Draft
**Paper**: `/home/shawn/Code/LLM-History-Paper/AbsenceJudgement.tex`
**Working directory**: `/home/shawn/Code/theseus-ship/llm-absence-judgement/text-revisions/`

---

## Objective

Reorganise Section 4 from model-by-model structure to pipeline-stage structure, presenting factual results rather than discussion. The new structure follows the research workflow: Ideation → Literature Discovery → Tool Discovery → Metadata → Evidence.

---

## Workflow

Work section-by-section with user review between batches:

| Batch | Sections | Type |
|-------|----------|------|
| **1** | 4.1 Overview, 4.2 Ideation | Keep + New |
| **2** | 4.3 Literature Discovery | Reorganise |
| **3** | 4.4 Tool Discovery | New |
| **4** | 4.5 Metadata, 4.6 Evidence | New |

**User responsibility**: Cut and save discussion material from existing sections before/during reorganisation.

---

## Current vs. Proposed Structure

### Current Structure (model-by-model)
- 4.1 Overview and Scope
- 4.2 OpenAI (Lit, Data, Synthesis)
- 4.3 Anthropic (Ideation, [unknown], Data)
- 4.4 Google (Ideation, Lit, Data)
- 4.5 Hugging Face Open Deep Research
- 4.6 Other Tools (Perplexity, Elicit)
- 4.7 Comparative Performance

### Proposed Structure (pipeline-stage)
- 4.1 Overview and Scope (keep, flag Table 1 for update)
- 4.2 Ideation and Research Design (NEW - extract from Claude/Gemini sections)
- 4.3 Literature Discovery and Evaluation
  - 4.3.1 OpenAI ChatGPT Deep Research
  - 4.3.2 Other Tools (Perplexity, Elicit)
  - 4.3.3 Comparative Performance (Table 4)
- 4.4 Tool Discovery (NEW - from quantitative data)
- 4.5 Tool Documentation (Metadata) (NEW - from quantitative data)
- 4.6 Tool Evidence Collection (NEW - from quantitative data)

---

## Files

### Output (working directory)
- `/home/shawn/Code/theseus-ship/llm-absence-judgement/text-revisions/section4-draft-reorganised.tex`

### Source Files (read-only reference)
- `/home/shawn/Code/LLM-History-Paper/AbsenceJudgement.tex` — live paper
- `/home/shawn/Code/theseus-ship/llm-absence-judgement/results-tools/*.csv` — quantitative data
- `/home/shawn/Code/theseus-ship/llm-absence-judgement/planning/*.md` — verification records

---

## Section-by-Section Approach

### 4.1 Overview and Scope
- **Action**: Keep as-is
- **Flag**: Table 1 (`tab:tool-usage`) needs update to reflect actual model usage per stage
- **Note**: Lines 369–373 already explain Claude/Gemini research mode unavailability during Feb 2025 lit review

### 4.2 Ideation and Research Design (NEW)
- **Source**: Extract from current 4.2.3 Synthesis (OpenAI), 4.3.1 (Claude), 4.4.1 (Gemini)
- **Approach**: Extract factual comparative results; subsection per model family

**Structure:**
- 4.2.1 OpenAI (GPT-4.5, o1 Pro)
- 4.2.2 Anthropic (Claude 3.7)
- 4.2.3 Google (Gemini 2.5 Pro)
- 4.2.4 Comparative observations (brief)

**Extractable results:**

*OpenAI (from Synthesis section + appendix line 745):*
- Used GPT-4.5 for initial ideation and outlining
- "GPT-4.5 defaulted to sequential summarisation rather than analytical integration"
- "o1 Pro showed only incremental improvements in instruction adherence"
- Both exhibited "confidence collapse" at synthesis boundaries

*Claude:*
- "marginally superior performance in generating research questions"
- "produced more nuanced categories and showed awareness of interdisciplinary considerations"
- Scope self-assessment: "if you want something thorough, I can do 1 to 3" tools

*Gemini:*
- "conflated multiple complex tasks into single operations"
- "poor task decomposition capabilities"
- Thinking logs showed overreach combining directory exploration, chapter analysis, infrastructure assessment

*Comparative:*
- "Gemini's questions proved superior to OpenAI's o3's formulaic approach but lacked both the consistency of Claude 3.7 Sonnet and the occasional insights of GPT-4.5"

**Move to cuts/**: Interpretive framing ("sophistication remained superficial", "arrogance without performance", judgment failure characterisations)

### 4.3 Literature Discovery and Evaluation

#### 4.3.1 OpenAI ChatGPT Deep Research
- **Source**: Current lines 380–386 (keep as-is, already factual)
- **Content**: 43 valid sources (37 unique), two prompting attempts, output composition, citation accuracy issues

#### 4.3.2 Other Tools
- **Source**: Current lines 513–531 (Perplexity + Elicit)
- **Add brief note**: Later tests with Claude/Gemini research modes (after Feb 2025) showed failure modes that didn't warrant pursuit:
  - Claude: Multi-agent architecture promising but sub-agents operated as isolated threads without cross-verification (from current "unknown activity" section)
  - Gemini: Never utilised Google Scholar despite access; "source soup" pattern (from current 4.4.2)

#### 4.3.3 Comparative Performance
- **Source**: Current lines 533–562 + Table 4
- **Keep**: Table 4 (`tab:literature-performance`) and surrounding factual text

### 4.4 Tool Discovery (NEW - to be written)

**Key quantitative findings to present:**
- 244 unique tools discovered across 8 runs
- Primary sources: Internet Archaeology, JOSS, JCAA, JOAD, SoftwareX
- Models used: ChatGPT Deep Research (primary), o3 (limited/problematic), Perplexity (test)

**Confabulation patterns:**
- 15 JOAD fabrications (wholesale hallucinations with plausible names)
- 14 JOSS "DOI hijackings" (both o3 and ChatGPT DR walked DOI sequences, attached fabricated names)
- Key insight: Both models confabulating identical tools indicates shared failure modes, not valid cross-validation

**Run quality breakdown:**
| Status | Count |
|--------|-------|
| Success | 130 |
| Success-secondpass | 44 |
| Fail-possible | 34 |
| Worthless (o3 JOSS) | 29 |
| Extreme fail (JOAD) | 15 |

### 4.5 Tool Documentation / Metadata (NEW - to be written)

**Key quantitative findings to present:**
- 98 tools investigated (92 filtered from discovery + 6 spawned during investigation)
- 90 successful (92%), 8 failed
- Claude Research used for production (after prompt development)

**Spawned tools (serendipitous discoveries):**
- ArchaeoGRID, LogicistWriter, OpenArchaeo, OpenGuide, Rhinoceros 3D, POV-Ray

**Failure types (8 tools):**
- Name collision: 4 (FaceNet, Fountain, Microware, pnuts)
- Minimal footprint: 1 (Bwigg)
- Insufficient documentation: 1 (Wcvt2Pov)
- No online presence: 1 (PyCoCu)
- Productive confabulation: 1 (Grid Machine → led to ArchaeoGRID)

**Key insight**: Zero metadata failures due to fabricated discoveries — all 8 were real mentions that couldn't be resolved

**Brief note on prompt development**: Reference methods section (8 versions, 120→250 lines); fuller treatment in Discussion

### 4.6 Tool Evidence Collection (NEW - to be written)

**Key quantitative findings to present:**
- 1,179 evidence rows across 125 tools
- Two pathways: Discovery (96 tools, 965 rows) + OpenArchaeo no-DVCS (29 tools, 214 rows)
- ChatGPT Deep Research: primary tool (~95% of evidence)

**Verification outcomes (from planning/unverified-events-review.md):**
| Status | Count | % |
|--------|-------|---|
| CONFIRMED | 945 | 91% |
| CONFABULATED | 52 | 5% |
| UNVERIFIABLE | 22 | 2% |
| GRANULARITY_ERROR | 17 | 2% |
| COLLISION | 4 | <1% |
| **Total** | **1,040** | |

**Key insight**: 5% confabulation rate required human verification of every event — labour cost invisible in apparent automation

---

## Tables Requiring Update (flagged for follow-up)

| Table | Label | Issue |
|-------|-------|-------|
| 1 | `tab:tool-usage` | Update to reflect actual model usage per stage |
| 2 | `tab:anthropic-performance` | May need reworking for pipeline-stage structure |
| 3 | `tab:gemini-performance` | May need reworking for pipeline-stage structure |
| 4 | `tab:literature-performance` | Keep as-is |

**Action**: Tables 2-3 flagged for later; focus on text reorganisation first.

---

## Execution Order

### Batch 1: Overview + Ideation
1. Review 4.1 Overview — confirm no changes needed (flag Table 1 for later)
2. Draft 4.2 Ideation — extract factual results from existing Claude/Gemini sections
3. **PAUSE** — User reviews, cuts discussion material from original

### Batch 2: Literature Discovery
4. Draft 4.3 Literature Discovery — reorganise existing OpenAI/Perplexity/Elicit + brief Claude/Gemini "failed out" note
5. **PAUSE** — User reviews

### Batch 3: Tool Discovery
6. Draft 4.4 Tool Discovery — write fresh from quantitative data
7. **PAUSE** — User reviews

### Batch 4: Metadata + Evidence
8. Draft 4.5 Metadata — write fresh from quantitative data
9. Draft 4.6 Evidence — write fresh from quantitative data
10. **PAUSE** — User reviews

### Final Integration
11. User integrates approved sections into live paper (Overleaf)
12. Address flagged table updates

---

## Verification

- Compare word counts: new draft vs. original Section 4
- Check all quantitative claims against source CSV files
- Verify Table 4 data matches comparative findings

---

## Post-Approval

- Copy this plan to `/home/shawn/Code/theseus-ship/llm-absence-judgement/planning/section4-reorganisation-plan.md` for progress tracking

---

## Questions Resolved

- ✓ Claude/Gemini lit search: Research modes not available Feb 2025; later tests failed out
- ✓ Ideation placement: Before lit discovery (Section 4.2)
- ✓ "Unknown activity" section: Treat as failed lit search attempt
- ✓ Cuts folder: Create for discussion material preservation
- ✓ Tables 2-3: Flag for follow-up, focus on text first
