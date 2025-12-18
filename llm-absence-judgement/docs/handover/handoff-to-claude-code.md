# Handoff Document: Absence of Judgment Project

## For Claude Code Continuation — December 2025

---

## 1. Project Overview

**Paper Title**: "An Absence of Judgment: AI's Limitations in Deep Research Tasks"

**Authors**: Brian Ballsun-Stanton (BBS), Shawn A. Ross (SAR)

**Core Argument**: LLMs lack three crucial dimensions of judgment—epistemic humility, inductive capacity, and correspondence with reality—which limits them to "mundane utility" rather than autonomous research. We propose "technoscholasticism" as a framework: like medieval scholastics, these tools privilege textual authority over critical assessment of knowledge claims.

**Methodology**: Autoethnographic investigation of frontier models (February–May 2025) applied to a real research task: compiling a dataset of archaeological/historical software tools to study software longevity and sustainability.

---

## 2. Paper Status

| Section | Status | Notes |
|---------|--------|-------|
| 1. Introduction | Penultimate | ~750 words |
| 2. Theoretical Framework | Penultimate | Agency, judgment, technoscholasticism |
| 3. Methodology | Penultimate | Autoethnographic approach |
| 4. Findings | **Needs work** | Partially drafted; data subsections incomplete |
| 5. Reflective Analysis | Needs revision | Cross-cutting patterns |
| 6–7. Discussion/Conclusion | Needs revision | |

**Section 4 Structure** (Model→Task organisation):

- 4.1 Overview and Scope ✓
- 4.2 OpenAI
  - 4.2.1 Literature Discovery ✓
  - 4.2.2 Ideation/Research Design (partial)
  - 4.2.3 Data Collection and Extraction — **NEEDS COMPLETION**
- 4.3 Anthropic
  - 4.3.1–4.3.2 (partial)
  - 4.3.3 Data Collection and Extraction — **NEEDS COMPLETION**
- 4.4 Google
  - 4.4.1–4.4.2 (partial)
  - 4.4.3 Data Collection and Extraction — **NEEDS COMPLETION**
- 4.5 Other Tools (Perplexity, Elicit) ✓

---

## 3. Key Quantitative Findings

### Tool Discovery (Canonical figures from Verification #5)

- **91 tools discovered** via AI-assisted journal searches (pre-spawning)
- **97 tools investigated** for metadata (91 + 6 spawned during investigation)
- **374 tools** in OpenArchaeo baseline (376 rows minus 1 duplicate + 1 header leak)
- **20 overlap** (22% redundancy): 19 exact + 1 human-confirmed fuzzy (fellingdater↔fellingDateR)
- **71 unique discoveries** (91 − 20 overlap)
- **15 confirmed hallucinations** (all from JOAD "extreme fail" run)
- **6 spawned tools**: ArchaeoGRID, OpenArchaeo, OpenGuide, Rhinoceros 3D, LogicistWriter, POV-Ray

### Metadata Collection

- **97 tools investigated** for comprehensive metadata
- **89 successful** (92% success rate)
- **7 documented failures** — all attributable to upstream discovery issues or intractability (reduced from 8 after Bwigg reclassification; see Section 6)
- **100% prompt success rate** for documentable tools
- **Claude Research selected** for production (superior accuracy, version awareness)

### Evidence of Life Collection

- **~1,874 evidence rows** (or 1,179 — see discrepancy note below)
- **105–125 unique tools** with evidence
- **95% from ChatGPT Deep Research**
- Coverage split: **849 rows (BBS, A→) / 330 rows (SAR, →Z)** — emerged organically

### Output Quality (Slop Assessment)

- 10 entries evaluated using Shaib et al. (2025) framework
- **2 "None" / 8 "Minimal"** slop ratings
- **Mean: 1.9 anchored claims per 100 words**
- **Mean word count: 678 words** (range 289–986)

---

## 4. Source Files (Now in Repo)

| File | Contents | Key Sheets/Tabs |
|------|----------|-----------------|
| `01a-tool-discovery.xlsx` | Raw discovery outputs | IA-run2-success, JOSS-secondpass, JOAD-extreme fail, etc. |
| `01b-tool-openarchaeo-work.xlsx` | Baseline + DVCS split | 374 baseline tools, DVCS/no-DVCS categorisation |
| `02-tool-metadata.xlsx` | Metadata collection results | V1–V8 tabs showing prompt evolution, 97 tools |
| `03-tool-evidence.xlsx` | Evidence of life data | Combined-tool-references, model comparison sheets |

### Derived CSV Files (in project)

- `tool-discovery-summary.csv` — 244 unique tools (de-duplicated)
- `tool-discovery-granular.csv` — 351 discovery instances
- `tool_verification_status_final.csv` — 242 tools with verification status
- `slop_evaluation_results.csv` — 10 entries with quality metrics
- `word_counts_all_entries.csv` — 89 entries with field-by-field word counts

---

## 5. Outstanding Questions for Brian

### Priority (Essential for Paper)

1. **Gemini Wayback behaviour**: What did the snapshot duplication look like during evidence collection?
2. **Claude vs ChatGPT DR evidence yield**: Any rough comparison of evidence rows returned?
3. **Deep Research session count**: Order of magnitude for evidence collection runs? (10s? 50s? 100s?)
4. **FAIMS fragmentation**: Was Claude producing 4 separate entries (FAIMS, FAIMS Mobile, FAIMS 3.0, Fieldmark) a single-prompt issue or persistent?

### Resolved

- ✓ JOAD "extreme fail" — wholesale fabrication of entries 26–40
- ✓ Coverage split — organic (Brian A→, Shawn →Z)
- ✓ Bwigg — verified real tool (see below)

---

## 6. Recent Findings Not Yet Integrated

### Verification #5 Findings (Canonical Figures)

See Section 3 for tool discovery reconciliation (374 baseline, 20 overlap, 91→97 pipeline).

### Verification #4 Findings (3 Dec 2025)

**ArchABM: Multi-Layered Confabulation ("Spectacular")**
The most sophisticated confabulation pattern discovered. Three simultaneous failure modes:

1. **Fabricated title**: "Agent-based modeling of ancient societies in R" — does not exist
2. **DOI hijacking**: DOI 10.21105/joss.01201 actually points to **TraitDB** (Leehr et al. 2019), a phenotypic trait database
3. **Name collision**: A real "ArchABM" exists — but it's for **indoor air quality and pandemic risk assessment** (Vicomtech, Building and Environment journal 2021), completely unrelated to archaeology

Classification: `FALSE_POSITIVE` (wrong domain) with detailed note capturing all three failure layers.

**archr Confirmed Hallucination**
Despite appearing "cross-validated" (found by 2+ services), web searches confirmed no "archr: Automated Radiocarbon Chronology for R" exists. Real radiocarbon R packages are rcarbon, Bchron, oxcAAR — but no "archr". The model likely generated a statistically plausible name combining "arch" + "r".

**ChronoModelr: Confabulation Near-Match**
No "ChronoModelr" exists on CRAN. The real package is **RChronoModel** (R prefix, not r suffix). LLMs likely conflated ChronoModel (standalone software) with R package naming conventions.
Classification: `CONFABULATED_NEAR_MATCH` — recoverable error pointing to real tool.

**Critical Methodological Finding: Cross-Validation ≠ Verification**
Multiple LLM services can independently hallucinate the same non-existent tool. "Cross-validated" status (found by 2+ services) does not guarantee the tool exists — both services may have similar training data gaps or naming pattern biases.

### Bwigg Reclassification (Verification #3)

**Finding**: Bwigg is a **verified real tool** — Bayesian wiggle-matching for radiocarbon calibration (Christen 2003). It has minimal online footprint because it predates modern web presence conventions.

**Impact**:

- Reduces documented metadata failures from 8 to 7
- Changes failure taxonomy: "insufficient documentation" → "minimal online footprint (methodological limitation)"
- Demonstrates that web-based LLM research cannot document tools that exist primarily in academic literature rather than online

### Evidence Number Discrepancy

Some documents reference **1,874 rows / 105 tools**; others reference **1,179 rows / 125 tools**.

**Likely explanation**: Different spreadsheet versions or before/after deduplication. Needs verification against `03-tool-evidence.xlsx`.

### Evidence Collection Attribution (Corrected)

- **BBS**: 849 rows (71.9%)
- **SAR**: 330 rows (28.0%)
- Total: 1,179 attributed rows
- Source: tool-evidence.csv, Author column

---

## 7. Failure Taxonomy (Current)

### Discovery Failures (Content Fabrication)

| Type | Description | Example |
|------|-------------|---------|
| Simple confabulation | Plausible names that don't exist | archr R package |
| Wholesale fabrication | Entire articles AND tools invented | JOAD entries 26–40 |
| Chimeric confabulation | Real facts from different tools combined | SAGAscape + SAGA GIS |
| DOI hijacking | Real DOI with fabricated content | joad.90 → fake "GeoViz" |
| Multi-layered confabulation | Multiple simultaneous failures | ArchABM: fabricated title + hijacked DOI + name collision |
| Confabulation near-match | Plausible variant of real tool name | ChronoModelr (real: RChronoModel) |

### Discovery Failures (Quality Degradation)

| Type | Description | Example |
|------|-------------|---------|
| Underextraction | Finding fewer tools than exist | IA 31–67: 18 tools from 200 articles vs IA-run2-success: 97 tools from 674 articles |
| Underdiscrimination | Including generic technologies | JCAA-o3 included TensorFlow, Keras, ArcGIS as "tools" |
| Metadata collapse | All entries missing critical fields | JOSS-worthless-o3: 29 entries, all with NaN authors |
| Vibes-based output | Producing entries while acknowledging uncertainty | SoftwareX: CSV entry for "Historical GIS Toolkit" with "Author Unknown (Not yet found in SoftwareX)" |

### Metadata Failures (7 documented)

| Type | Count | Examples |
|------|-------|----------|
| Name collision | 4 | FaceNet, Fountain, Microware, pnuts |
| Minimal online footprint | 1 | Bwigg (real but undocumentable via web) |
| Insufficient documentation | 1 | Wcvt2Pov |
| No online presence | 1 | PyCoCu |

**Note**: Grid Machine (previously counted as confabulation) led serendipitously to ArchaeoGRID discovery, so is now categorised as "productive failure" and excluded from the 7-failure count above. The reduction from 8 to 7 failures comes from Bwigg reclassification (verified real tool with minimal online footprint), not from Grid Machine.

### Operational Lesson: Web Verification Lockups

During verification sessions, checking multiple tools consecutively via web search caused context window crashes/lockups. **Established protocol**: Verify ONE tool at a time, check in before continuing. This pattern should be expected when using web search extensively for verification tasks.

### Success Patterns (Summary)

For detailed analysis, see `success_analysis_comprehensive.md`. Key patterns that distinguished successful runs:

**Complete metadata as quality signal**: Across all successful runs, core metadata fields were 100% populated. Empty author fields (as in JOSS-worthless-o3: 0/29 complete) reliably predict other quality problems.

**Appropriate yield proportions**: Successful runs showed realistic extraction rates. IA-run2-success found tools in 14.4% of articles — appropriate for a general archaeology journal. JOSS-secondpass produced fewer entries (16) than the failed o3 run (29) but with zero confabulations. Failures occurred when models tried to populate expected output slots beyond what sources contained.

**Model-task matching**: Discovery and evidence tasks succeeded with Deep Research; metadata succeeded with Claude Research. Using o3 for discovery or any model for cross-source synthesis produced failures.

**The judgment boundary**: Success occurred when tasks were structured to avoid requiring judgment. Models succeed at finding sources (given clear search terms), extracting metadata (given specific fields), and reporting findings (given simple output format). They fail when asked to evaluate source quality, synthesise across contradictory sources, decide relevance, or infer from absence.

---

## 8. Model-Specific Performance Patterns

### ChatGPT Deep Research

- **Best for**: Evidence collection (highest persistence/yield), eventually CSV output
- **Issues**: Temporal blindness (ArboDat), random walk accumulation, wholesale fabrication (JOAD)
- **Required**: 55-line prompt to constrain output

### Claude Research

- **Best for**: Metadata collection ("take known tool, get rich information"), version awareness
- **Issues**: Persistent CSV refusal (always required follow-up), FAIMS fragmentation, hyperbolic titles
- **Strength**: Realistic scope assessment ("1 to 3 tools thoroughly")

### Google Gemini 2.5 Pro

- **Best for**: Transcription
- **Issues**: Version confusion (FAIMS PostgreSQL/CouchDB mixup), 20-page reports instead of CSV, Wayback duplication, chimeric confabulation
- **Eliminated early** from metadata and evidence tasks

---

## 9. Key Methodological Insights

### Cross-Validation Does Not Guarantee Reality

Multiple LLM services can independently hallucinate the same non-existent tool. In verification testing, "archr" appeared in outputs from 2+ services but does not exist. This occurs because services share similar training data or naming pattern biases. **Human verification remains essential even for "cross-validated" discoveries.**

### Prompt Development

- Prompts evolved empirically through documented iteration (V1→V8)
- Evidence prompt: V1 (complex 15-column synthesis) → V5 (simple 5-column, one row per source) — radical simplification improved reliability
- Key guardrail: "ABOVE ALL ELSE, if you are unsure... do not make a claim"

### "Basin" Metaphor

Models fall into "attractor states" from training (e.g., report production, version history inclusion). Fighting basins is futile; "domestication" (channeling impulses into appropriate fields like History) works better.

### Two-Step CSV Pattern

Claude Research consistently required follow-up prompt to convert narrative report to CSV — workflow friction, not quality issue.

### Scope-Quality Relationship

Inverse relationship: narrower tasks → higher quality. Claude's self-aware scope limitation ("with 10 tools, you're going to get a shallow summary") proved accurate.

### Corruption Handling Principle

Critical distinction established during data correction: **LLM corruption = preserve as evidence; processing corruption = restore**. When LLM output contains errors (confabulations, version confusion), preserve the original for analysis. When downstream processing introduces artifacts (CSV column misalignment, encoding issues), restore the intended content.

### Quality Signals for Output Assessment

**Reliable negative indicators** (presence predicts problems):

- Empty metadata fields, especially Authors (NaN) — strongest single predictor
- Inconsistent or suspiciously sequential DOI patterns (joad.100, joad.101, joad.110...)
- Generic technology inclusion without domain justification
- Yield that seems too high for the source (fabrication) or too low (underextraction)

**Unreliable indicators** (do not guarantee quality):

- Real DOI format — can be hijacked with fabricated content
- Plausible tool names — can be confabulated
- Internal consistency — fabrications can be internally consistent
- Model asking clarifying questions — may still produce unreliable output
- Cross-validation across services — multiple services can hallucinate identically

---

## 10. Analysis Documents in Project

| Document | Purpose |
|----------|---------|
| `working_notes_section4.md` | Comprehensive notes, to-do lists, findings |
| `failure_analysis_comprehensive.md` | Complete failure taxonomy with examples |
| `success_analysis_comprehensive.md` | Patterns distinguishing successful runs |
| `disambiguation_failures_analysis.md` | Detailed analysis of 8 (now 7) metadata failures |
| `tool_origin_reconciliation.md` | Tracing 89 investigated tools to discovery pathways |
| `evidence_tool_pathway_trace.md` | Tracing 125 evidence tools to origins |
| `draft_section4_data_tasks.md` | Draft findings for data collection subsections |
| `section4_data_collection_drafts.md` | Enhanced subsections for OpenAI/Anthropic/Google |
| `slop_evaluation_detailed_report.md` | Full qualitative slop assessment |
| `questions_for_brian.md` | Outstanding questions (some resolved) |

---

## 11. Immediate Priorities for Claude Code

1. **Reconcile evidence numbers**: Check `03-tool-evidence.xlsx` to determine canonical counts (1,874/105 vs 1,179/125)

2. **Update failure taxonomy**: Integrate Bwigg reclassification (7 failures, not 8)

3. **Complete Section 4.2.3, 4.3.3, 4.4.3**: Data collection subsections need quantitative grounding from XLSX files

4. **Verify tool counts**: Cross-check discovery → metadata → evidence pipeline numbers

5. **Prepare for Brian's input**: Some questions can only be answered by Brian (Gemini Wayback details, session counts)

---

## 12. Style Notes

- **Australian spelling**: recognise, analyse, categorise, etc.
- **Formatting**: Minimal headers in prose; lists only when essential
- **Tone**: Academic clarity without obscurity; direct assertions with appropriate hedging
- **Cross-references**: "As observed with OpenAI's Deep Research..." to maintain parallel structure

---

*Handoff document prepared December 2025*
*Contact: Review `compact_message_draft.md` for session continuity context*
