# Working Notes: Section 4 Findings — Comprehensive Update

## Document Status

Last updated: December 2025 (Verification #5 complete)
Status: Comprehensive analysis complete; awaiting Brian's input on specific questions

**Note**: This document contains detailed working analysis. For orientation and current decisions, see `HANDOFF_TO_CLAUDE_CODE_clean.md` first.

---

## 1. Quantitative Summary

### 1.1 Tool Discovery (Canonical figures from Verification #5)

- **91 tools discovered** across all successful runs (pre-spawning)
- **97 tools investigated** for metadata (91 + 6 spawned during investigation)
- **20 overlap with OpenArchaeo** (22% redundancy): 19 exact + 1 fuzzy (fellingdater↔fellingDateR)
- **71 unique discoveries** (91 − 20 overlap)
- **15 confirmed hallucinations** (all from JOAD "extreme fail" run)

### 1.2 Metadata Collection

- **97 tools investigated** for comprehensive metadata
- **89 successful** (92% success rate)
- **7 documented failures** — all attributable to upstream discovery issues or intractability
  - *(Reduced from 8 after Bwigg reclassification — see Section 3)*
- **100% prompt success rate** — no failures from metadata collection process itself
- **Claude Research selected** for production (superior accuracy, version awareness)

### 1.3 Evidence of Life Collection

- **~1,874 evidence rows** (or 1,179 — discrepancy needs verification against `03-tool-evidence.xlsx`)
- **105–125 unique tools** with evidence
- **849 rows from Brian** (alphabetically A→)
- **330 rows from Shawn** (alphabetically →Z)
- **95% of evidence from ChatGPT Deep Research**

---

## 2. Tool Source Tracing

### 2.1 Complete Tool Origin Reconciliation (89 Investigated Tools)

| Category | Count | % |
|----------|------:|--:|
| Discovery (direct match) | 62 | 69.7% |
| Discovery (name variant) | 19 | 21.3% |
| Discovery (bundled mention) | 1 | 1.1% |
| Split from discovered entry | 4 | 4.5% |
| Lead-following/serendipitous | 3 | 3.4% |
| OpenArchaeo without DVCS | 0 | 0% |
| **TOTAL** | **89** | **100%** |

### 2.2 Key Categories Explained

**Direct matches (62):** Tool name in discovery matches investigated tool name

**Name variants (19):** Standardised during metadata collection (e.g., "Depthmap" → "DepthmapX")

**Bundled mention (1):** htmltoc discovered in semicolon-separated list with htmlfig and pnuts

**Splits (4):**
- MASA Consortium → LogicistWriter, OpenArchaeo, OpenGuide
- Wcvt2Pov → POV-Ray

**Lead-following (3):**
- Grid Machine (confab) → ArchaeoGRID
- Rhino for AutoCAD → Rhinoceros 3D
- Stratigraphic tools investigation → StratiGraf

### 2.3 OpenArchaeo Overlap

- **20 tools** found in BOTH discovery AND OpenArchaeo (redundant)
- **71 tools** unique to discovery (genuine value-add)
- **9 OpenArchaeo no-DVCS tools** investigated for EVIDENCE (not metadata)

### 2.4 OpenArchaeo No-DVCS Tools Investigated (Evidence Only)

These tools were investigated for evidence but NOT added to Master List for metadata:

| Tool | Evidence Rows |
|------|--------------|
| ArboDat (+ variants) | 20 |
| ChronoLog | 26 |
| HumanOS | 18 |
| Sériation de matrice en présence/absence | 10 |
| Bonify | 10 |
| benmarwickopencontext.r | 6 |
| munsell-plot.R | 6 |
| tweet-edits-to-archaeology-articles.R | 6 |
| archaeology_on_wikipedia.R | 4 |

### 2.5 Pipeline Summary

```
91 discovered → 97 investigated for metadata
  + 6 spawned during investigation
  - 7 metadata failures
  = 89 with complete metadata
  + 9 OpenArchaeo no-DVCS (evidence only)
  = 105–125 unique tools in evidence spreadsheet
```

---

## 3. Documented Failures (7 Total)

**Note**: Reduced from 8 after Bwigg reclassification. Bwigg is a **verified real tool** (Bayesian wiggle-matching for radiocarbon calibration, Christen 2003) with minimal online footprint because it predates modern web presence conventions. This represents a methodological limitation, not a discovery error.

### 3.1 Name Collisions (4)

| Tool | Problem | Actual Result |
|------|---------|---------------|
| FaceNet | Google neural network | Wrong domain entirely |
| Fountain | Multiple software with this name | Ambiguous reference |
| Microware | Generic term | Multiple unrelated tools |
| pnuts | Yahoo platform | Wrong domain |

### 3.2 Minimal Online Footprint (1)

| Tool | Problem |
|------|---------|
| Bwigg | Real tool (Christen 2003) but insufficient web documentation for LLM-based research |

### 3.3 Insufficient Documentation (1)

| Tool | Problem |
|------|---------|
| Wcvt2Pov | Insufficient information for metadata (but led to POV-Ray recovery) |

### 3.4 No Online Presence (1)

| Tool | Problem |
|------|---------|
| PyCoCu | Site-specific Python script (Sécher et al. 2020); exists only as passing reference in literature |

**Note**: Grid Machine (previously counted as confabulation) led serendipitously to ArchaeoGRID discovery, so is now categorised as "productive failure" and excluded from the failure count.

---

## 4. Model-Specific Performance Patterns

### 4.1 ChatGPT Deep Research

**Strengths:**
- Highest persistence/longer time horizon
- Best for finding highest number of evidence pieces
- Eventually produced usable CSVs after iteration

**Weaknesses:**
- Required 55-line prompt to constrain output
- Random walk evidence accumulation
- Temporal blindness (ArboDat example)
- JOAD wholesale fabrication

### 4.2 Claude Research

**Strengths:**
- Excellent at "known tool → get more information"
- Rich, nuanced, version-aware metadata
- Superior prose quality
- Realistic scope assessment ("1 to 3 tools thoroughly")

**Weaknesses:**
- Persistent CSV refusal (always required follow-up prompt)
- Hyperbolic titles ("Revolutionary Digital Archaeology: The FAIMS Transformation")
- FAIMS fragmentation (4 separate entries in evidence)

### 4.3 Google Gemini 2.5 Pro

**Strengths:**
- DID produce CSVs (correction from earlier notes)
- Superior transcription capabilities

**Weaknesses:**
- Version confusion (mixed features across software versions)
- Couldn't keep version↔feature matches straight despite prompt refinement
- FAIMS examples: PostgreSQL vs SQLite/CouchDB confusion, Android-only vs cross-platform, false claims about server setup requirements
- **Eliminated early** from metadata and evidence tasks

### 4.4 o3 Model

**Weaknesses:**
- JOSS "worthless" run (29 entries, all NaN authors)
- archr confabulation (verified non-existent)
- Wholesale fabrication patterns

---

## 5. Failure Mode Taxonomy (Complete)

### 5.1 Content Fabrication

| Type | Description | Example |
|------|-------------|---------|
| Simple confabulation | Plausible names that don't exist | archr R package |
| Wholesale fabrication | Entire articles AND tools invented | JOAD entries 26–40 |
| Chimeric confabulation | Real facts from different tools combined | SAGAscape + SAGA GIS (Perplexity) |
| DOI hijacking | Real DOI with fabricated content | joad.90 → fake "GeoViz" |
| Multi-layered confabulation | Multiple simultaneous failures | ArchABM: fabricated title + hijacked DOI + name collision |
| Confabulation near-match | Plausible variant of real tool name | ChronoModelr (real: RChronoModel) |

### 5.2 Quality Degradation

| Type | Description | Example |
|------|-------------|---------|
| Underextraction | Finding fewer tools than exist | IA 31–67: 18 tools from 200 articles vs 97 from 674 |
| Underdiscrimination | Including generic technologies | JCAA-o3 included TensorFlow, Keras, ArcGIS |
| Version confusion | Mixing features across versions | Gemini on FAIMS |
| Metadata collapse | All entries missing critical fields | JOSS-worthless-o3: 29 entries, all NaN authors |

### 5.3 Process Failures

| Type | Description | Example |
|------|-------------|---------|
| Format non-compliance | Persistent refusal despite prompting | Claude CSV refusal |
| Vibes-based output | Producing output while acknowledging uncertainty | SoftwareX "Historical GIS Toolkit" |
| Temporal blindness | Finding but not understanding dates | ArboDat "developed since 1997" |

### 5.4 Concrete Example: Vibes-Based Output (SoftwareX Chat)

From the SoftwareX tool discovery chat transcript, the model:
- Produced CSV entry for "Historical GIS and Geo-Humanities Toolkit"
- Listed author as "Author Unknown (Not yet found in SoftwareX)"
- Explicitly stated: "Could not locate an explicit SoftwareX article. Might require citation tracking."
- **Yet still produced the entry** — demonstrating output generation despite acknowledged inability to verify

---

## 6. Quality Signals

### 6.1 Reliable Negative Indicators

- Empty metadata fields (especially Authors = NaN) → deeper problems likely
- Inconsistent or sequential DOI patterns (joad.100, joad.101...) → possible fabrication
- Generic technology inclusion → poor prompt adherence
- Yield too high for source → fabrication likely
- Yield too low for source → underextraction

### 6.2 Unreliable Indicators

- Real DOI format → doesn't guarantee real content (can be hijacked)
- Plausible tool names → can be fabricated
- Internal consistency → fabrications can be consistent
- Model asking clarifying questions → may still produce unreliable output
- Cross-validation across services → multiple services can hallucinate identically

---

## 7. Success Characterisation

### 7.1 Discovery Success Patterns

**IA-run2-success (Benchmark):**
- 674 articles examined, 97 with tools (14.4% yield)
- 131 unique tools across 145 mentions
- 100% metadata field completeness
- Appropriate yield: model correctly identified that 85.6% of articles don't discuss software
- Multi-tool recognition working (semicolon separation)

**JOSS-secondpass (Quality over Quantity):**
- 16 tools (vs 29 in failed o3 run) — but zero confabulations
- Rich cross-referencing: each entry lists related tools from the paper
- Real author names: Nicolas Frerebeau, Sébastien Plutniak, Clemens Schmid
- 100% URL validity

**Key differentiator: Fewer entries with complete metadata > more entries with missing fields**

### 7.2 Evidence Success Patterns

**Combined dataset characteristics:**
- Diverse authoritative sources: doi.org (165), cran.r-project.org (147), github.com (116), intarch.ac.uk (77)
- Appropriate evidence density: 4–106 rows per tool (reflects actual documentation availability)
- Temporal spread: 1996–2025, concentration in 2018–2024

**Residual issues within success:**
- 37% (698 entries) contain citation artifact markers (contentReference) — requires cleaning
- 14% (266 entries) marked "n.d." — appropriate for undated sources
- Some duplication across runs

### 7.3 Metadata Success Patterns

**Claude Research strengths:**
- Rich contextual detail (version-aware descriptions)
- Appropriate technical depth
- 89/97 investigated tools with complete fields

**Field completeness reflects reality:**
- DVCS-repo: 42% (not all tools have repositories)
- CRAN: 15.5% (only R packages)
- Core descriptive fields: 69% (complete for all investigated tools)

### 7.4 The Success/Failure Boundary

| Factor | Success Pattern | Failure Pattern |
|--------|-----------------|-----------------|
| Metadata completeness | 100% core fields | NaN in authors, URLs |
| Yield | Realistic proportions | Too many (fabrication) or too few (underextraction) |
| Tool types | Domain-specific with justified generics | Undiscriminated generic inclusion |
| Source diversity | Multiple authoritative domains | Single source or fabricated |
| Model selection | DR for discovery/evidence, Claude for metadata | o3 for discovery, any model for synthesis |

### 7.5 The Judgment Boundary

**Success occurs when tasks are structured to avoid requiring judgment.**

Models succeed at:
- Finding sources (given clear search terms)
- Extracting metadata (given specific fields)
- Reporting what was found (given simple output format)

Models fail when asked to:
- Evaluate source quality
- Synthesise across contradictory sources
- Decide what's relevant vs irrelevant
- Infer from absence

**Key insight:** The boundary between success and failure maps precisely onto the boundary between mechanical extraction and evaluative judgment. This supports the paper's argument that these tools provide genuine mundane utility when properly scoped, but lack judgment for autonomous research.

---

## 8. Practical Recommendations

### 8.1 Discovery Tasks

- Use Deep Research, not base models
- Accept realistic yield (not every article has tools)
- Check author field completeness as quality signal
- Expect 10–15% generic technology inclusion as acceptable noise

### 8.2 Evidence Tasks

- Use simple output format (≤5 columns)
- One row per source, no synthesis
- Include "if unsure, do not claim" instruction
- Budget for 37% citation artifact cleaning
- Expect 14% undated entries

### 8.3 Metadata Tasks

- Use Claude Research for depth
- Expect CSV conversion as separate step
- Provide specific metadata template
- Scope to 1–3 tools per prompt for quality

### 8.4 General Principles

- Match model to task type
- Structure tasks to avoid requiring judgment
- Use metadata completeness as quality signal
- Accept appropriate incompleteness (not everything has GitHub repo)
- Verify sample before trusting full output

---

## 9. Evidence Collection Specifics

### 9.1 Prompt Evolution

- V1 → V5 → V7: Complex 15-column synthesis → simple 5-column collection
- Final format: Tool, Year, Source, URL, AI_Notes
- Simplification improved reliability
- Key guardrail: "ABOVE ALL ELSE, if you are unsure... do not make a claim"

### 9.2 Model Testing on FAIMS (Ground Truth)

| Model | Issue |
|-------|-------|
| Claude | Fragmentation (4 separate entries: FAIMS, FAIMS Mobile Platform, FAIMS 3.0, Fieldmark) |
| Gemini | Wayback Machine snapshot duplication |
| ChatGPT DR with o3 | Highest-quality notes (explicit source classification, verification status) |

### 9.3 ArboDat Temporal Blindness

- Model found homepage stating "developed since 1997"
- Extracted page metadata date instead of development date
- Exemplifies inability to understand temporal significance

### 9.4 Coverage Split

- 849 rows (Brian) / 330 rows (Shawn)
- Split emerged organically
- Brian worked A→ alphabetically
- Shawn worked →Z alphabetically

---

## 10. Slop Assessment (Metadata Quality)

Using Shaib et al. (2025) "Measuring AI 'Slop' in Text" framework:

- **10 entries evaluated** (including FAIMS ground truth)
- **2 "None" / 8 "Minimal"** slop ratings
- **Mean 1.9 anchored claims per 100 words**
- **Mean 678 words per entry** (range 289–986)
- **0–3 generic phrases per entry**

No entries exhibited characteristic slop patterns: verbosity without information, hallucinated attributions, incoherent flow, or excessive promotional claims.

---

## 11. Questions Pending (For Brian)

### Priority 1: Essential for Paper

1. **Gemini Wayback behaviour** — What did the snapshot duplication look like during evidence collection?
2. **Claude vs ChatGPT DR evidence yield** — Any rough comparison of evidence rows returned?
3. **Deep Research session count** — Order of magnitude for evidence collection runs? (10s? 50s? 100s?)
4. **FAIMS fragmentation** — Was Claude producing 4 separate entries a single-prompt issue or persistent?

### Resolved

- ✓ JOAD "extreme fail" — wholesale fabrication of entries 26–40
- ✓ Coverage split — organic (Brian A→, Shawn →Z)
- ✓ Bwigg — verified real tool (Christen 2003)

---

## 12. Key Findings for Paper

### 12.1 Discovery Performance

- 91 tools discovered, 22% overlap with baseline
- 15 confirmed hallucinations (all from JOAD)
- Multiple distinct failure modes identified
- Model selection matters: different models excel at different tasks

### 12.2 Metadata Quality

- 92% success rate (89/97)
- 100% prompt success (all 7 failures from upstream discovery or intractability)
- Model-specific strengths: Claude for depth, OpenAI for structured output

### 12.3 Evidence Collection

- ChatGPT DR dominant (95% of evidence)
- Persistence/time horizon key differentiator
- Temporal blindness pattern documented
- 1,179–1,874 evidence rows for 105–125 tools

### 12.4 Theoretical Support

- Wholesale fabrication supports technoscholasticism thesis
- Vibes-based output demonstrates absence of genuine judgment
- Scope-confabulation relationship demonstrates fixed effort pattern
- Temporal blindness reflects absence of world model
- Cross-validation ≠ verification (multiple services can hallucinate identically)

---

## 13. Files and Resources

### Analysis Documents

| Document | Purpose |
|----------|---------|
| `HANDOFF_TO_CLAUDE_CODE_clean.md` | Authoritative orientation document |
| `DOCUMENT_RELATIONSHIP_GUIDE.md` | Guide to document hierarchy |
| `failure_analysis_comprehensive.md` | Complete failure taxonomy |
| `success_analysis_comprehensive.md` | Complete success characterisation |
| `draft_section4_data_tasks.md` | Draft findings sections |
| `questions_for_brian.md` | Outstanding questions |
| `slop_evaluation_detailed_report.md` | Full qualitative slop assessment |

### Source Spreadsheets

- `01a-tool-discovery.xlsx` — 12 sheets with discovery outputs
- `01b-tool-openarchaeo-work.xlsx` — 374 baseline tools
- `02-tool-metadata.xlsx` — V1–V8 tabs, 97 tools
- `03-tool-evidence.xlsx` — Evidence rows (count TBC)

### Web Verifications Conducted

- archr R package: **CONFIRMED NON-EXISTENT**
- ArchABM: **FALSE_POSITIVE** (wrong domain — indoor air quality, not archaeology)
- ChronoModelr: **CONFABULATED_NEAR_MATCH** (real package is RChronoModel)
- tidypaleo: Confirmed real (CRAN)
- SAGAscape: Confirmed real (JCAA 2022) but Perplexity data chimeric
- joad.90: Confirmed real DOI, content is "NERD" not "GeoViz"
- Bwigg: **VERIFIED REAL** (Christen 2003, minimal online footprint)

---

## 14. Gaps Identified for Section 4 Narrative (Claude Code Review, 6 Dec 2025)

This section documents gaps identified during Claude Code's review of handover materials. These represent information needed to complete the Section 4 findings narrative, particularly for the "scaffolding overcomes lack of judgment" theme.

### 14.1 Under-Documented: Segmentation Decisions

**Gap**: The handover documents don't clearly narrate *why* discovery and evidence collection had to be split into separate prompts.

**Questions to resolve**:
- What was the original combined discovery+evidence prompt attempting to do?
- What specific failures occurred that forced the split?
- How many iterations before abandoning the combined approach?
- What does this reveal about LLM agency limitations?

**Narrative significance**: This exemplifies how lack of agency was overcome through human-imposed task decomposition — a key point for the paper's argument.

### 14.2 Under-Documented: Batch Size Constraints

**Gap**: The operational necessity of processing "only a few journal issues at a time" for discovery and "only one tool at a time" for metadata/evidence isn't foregrounded.

**Questions to resolve**:
- What happened when larger batches were attempted?
- How was the optimal batch size determined (trial and error? explicit model guidance?)
- Does Claude's "1 to 3 tools" self-assessment match actual experience?

**Narrative significance**: Demonstrates that "agentic" capabilities require constant human chunking — the system cannot self-organise work.

### 14.3 Under-Documented: Model Elimination Sequence

**Gap**: The V1→V8 prompt evolution is documented, but the *model elimination story* isn't clear — which models were tried for metadata and why did they fail before Claude became "last model standing"?

**Known from paper/notes**:
- Gemini: Version confusion (FAIMS example), eliminated early
- DR: Tried for metadata (Table 1), outcome unclear
- o3: JOSS "worthless" run, JOAD failures

**Questions to resolve**:
- What was the sequence of model testing for metadata?
- Were there specific prompts/sessions where non-Claude models failed?
- What made Claude's failures (CSV refusal, hyperbolic titles) tolerable vs Gemini's failures (version confusion) intolerable?

### 14.4 Under-Documented: Persistent Annoyances Despite Success

**Gap**: Some weaknesses persisted despite extensive scaffolding. These are mentioned but not systematically catalogued.

**Known persistent issues**:
- CSV + report in single prompt: Never achieved (always required reprompting)
- Sensational titles: "Revolutionary Digital Archaeology: The FAIMS Transformation" despite templating
- History field contamination: Required creating dedicated History field to "channel" model's tendency

**Questions to resolve**:
- Were there other persistent annoyances that scaffolding couldn't eliminate?
- How much time was lost to these workarounds?
- Do these represent fundamental limits of prompt engineering?

### 14.5 Under-Documented: Evidence Prompt V1→V7 Evolution

**Gap**: The metadata prompt evolution (V1→V8) is well-documented, but evidence prompt changes (V1→V7) less so.

**Known**:
- V1: 122-line elaborate prompt
- V7: 56-line tightened version
- Shift from 15-column synthesis to 5-column collection

**Questions to resolve**:
- What specific failures drove each iteration?
- Was simplification always the solution, or were there failed attempts at more elaborate scaffolding?
- Which changes had the biggest impact on output quality?

### 14.6 Data Verification Needed

**Priority items**:
1. Evidence row count: Verify 1,874 vs 1,179 against `03-tool-evidence.xlsx`
2. Tool counts at each pipeline stage: Verify 91→97→89→125 flow
3. Prompt version inventory: Confirm V5 exists or if numbering skipped

---

## 15. Project Management: Outstanding Tasks

### Immediate (for Section 4 completion)

- [ ] Interview to fill gaps (Sections 14.1–14.5)
- [ ] Reconcile evidence row counts from spreadsheet
- [ ] Reconstruct model elimination sequence from chat logs/prompts
- [ ] Document persistent annoyances systematically

### Medium-term (for Discussion section)

- [ ] Questions for Brian (Section 11) — still pending
- [ ] Synthesise "scaffolding vs judgment" narrative from gap-filling interview

### Deferred

- [ ] Full prompt library review (all versions V1→V8)
- [ ] Cross-reference paper Section 4 with working notes for consistency

---

*Working notes maintained throughout December 2025 analysis sessions.*
*Last updated: 6 December 2025 — Claude Code review and gap identification*
