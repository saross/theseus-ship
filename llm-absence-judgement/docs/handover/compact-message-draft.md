# Compact Message Draft (for review)

## Project Context
Academic paper on LLM research capabilities in humanities/social sciences. Autoethnographic methodology assessing agency (persistence, goal-directedness) and judgment (epistemic humility, ampliative reasoning, correspondence with reality). Co-authors: Shawn and Brian. Target: journal submission within two weeks.

## Paper Status
- Sections 1-3: Penultimate state
- Section 4 (Findings): Partially drafted, needs revision
  - 4.1 Overview: Done
  - Literature discovery subsections: Done (all services)
  - Data collection subsections: OpenAI needs overhaul; Anthropic/Google more developed
- Sections 5-7: Need revision

## Pipeline Reconciliation (3 Dec 2025 Session)

**Two Independent Pathways Confirmed**:
1. **Discovery Pathway**: AI-assisted journal searches → 98 metadata investigations → 96 tools to evidence (965 rows)
2. **OpenArchaeo no-DVC Pathway**: Baseline tools without repos → direct to evidence (29 tools, 214 rows)

**Zero overlap** between pathways in evidence collection. Total: 125 tools, 1,179 evidence rows.

**Metadata Outcomes** (Discovery pathway only):
- 83 Success
- 6 Failure (Bwigg, FaceNet, Fountain (VRML tool), Microware, pnuts, PyCoCu)
- 4 New (spawned: ArchaeoGRID, OpenArchaeo semantic web, OpenGuide, Rhinoceros 3D)
- 2 Failure|Spawned New, 2 Success|Spawned New

**Key Anomaly**: 5/6 metadata failures still got evidence collected (FaceNet, Fountain (VRML tool), Microware, pnuts, PyCoCu). Reflects independent operation: metadata used Claude, evidence used ChatGPT DR.

**Bwigg Special Case**: Cross-validated real tool (3 discoveries, specific IA article from 2003: "Bwigg: An Internet facility for Bayesian radiocarbon wiggle-matching" by J. Andrés Christen) that failed BOTH metadata AND evidence. Only tool to fall through entire pipeline. Likely due to minimal online footprint for 20+ year old tool.

**Files Created**: `/mnt/user-data/outputs/evidence_tool_pathway_trace.md` - complete pipeline documentation

## Key Methodological Findings (Previous Sessions)

**Comparative Model Elimination**: Tested 4 configurations (ChatGPT o3, ChatGPT DR, Claude Research, Gemini Pro) across prompt versions V1-V8. Progressive elimination: DR dropped V2 (worst), Gemini dropped V5 (date errors, version confusion, hallucinated contributors), ChatGPT dropped V5 (factual errors, insufficient depth). Claude selected for superior accuracy and information density.

**Basin Metaphor**: Models fall into "attractor states" from training—e.g., report production, version history inclusion. Fighting basins is futile; "domestication" (channeling impulses into appropriate fields like History) works better.

**Prompt Evolution**: Metadata prompt grew from ~120 to ~310 lines (V1-V7), restructured to ~250 lines (V8). Each elaboration addressed documented failure. Key additions: cross-discipline emphasis, CSV reminders, version clarity section, word count targets. Prompting as empirical undertaking — iterate to get desired results, not theoretical prompt design.

**Two-Step Pattern**: CSV generation consistently required follow-up prompt ("please also produce the requested csv") — workflow friction, not quality issue. Final outputs were consistent and usable with all required fields filled.

## Failure Analysis Findings

**No hallucinations in failure cases**. When tools didn't exist, Claude correctly identified this and produced helpful context. Failure types:
1. Name collision (FaceNet, Fountain (VRML tool), Microware, pnuts) — dominant non-archaeological software with same name
2. Real but undocumented (PyCoCu - site-specific script from Sécher et al. 2020)
3. Minimal online footprint (Bwigg - real 2003 tool, cross-validated discovery, but couldn't document further)
4. Discovery granularity: MASA → split into 3 component tools
5. Misidentification → recovery: STELLAR (wrong guess, but report contained correct tool)
6. Serendipitous: Rhino for AutoCAD → led to Rhinoceros 3D

**Bottom line**: Metadata prompt succeeded; failures were upstream (discovery) or genuinely intractable.

## Data Structure
- Metadata investigations: 98 tools (Discovery pathway)
- Evidence collection: 125 tools (96 Discovery + 29 OpenArchaeo no-DVC)
- Evidence rows: 1,179 total (965 Discovery + 214 OpenArchaeo)
- Metadata success rate: 85/98 = 86.7%
- Evidence coverage: 96/98 = 98% of metadata tools (only Bwigg dropped)

## Output Quality (Slop Evaluation)
- Framework: Shaib et al. (2025) "Measuring AI 'Slop' in Text" (arXiv:2509.19163)
- 10 entries evaluated: FAIMS (ground truth), archeoViz, Gephi, ARIADNE, PyLithics, SEAHORS, LifeForms, SASSA, SpadeR, kdedemo
- Results: 2 "None", 8 "Minimal"; 1.4-2.6 anchored claims per 100 words; 0-3 generic phrases
- Validated by domain expert: "very little triggers a 'slop' reaction"
- Files: slop_evaluation_results.csv, slop_evaluation_detailed_report.md, slop_evaluation_prompt.md, word_counts_all_entries.csv

## Files Available in /mnt/user-data/outputs/

| File | Size | Description |
|------|------|-------------|
| working_notes_section4_updated.md | 19K | **Most comprehensive** - all analysis, taxonomies, Bwigg correction |
| evidence_tool_pathway_trace.md | 12K | Complete pipeline tracing for 125 evidence tools |
| disambiguation_failures_analysis_v2.md | 12K | v2 with corrected Bwigg classification |
| failure_analysis_v2.md | 8K | v2 with corrected failure taxonomy |
| tool_verification_status_updated.csv | 5K | 37 corrections to verification status |
| compact_message_draft.md | 7K | This summary document |
| FILE_MANIFEST.md | 4K | Complete manifest with session-by-session changes |

**Verification Corrections Summary** (37 tools):
- 10 VERIFIED_REAL: ARCHIS, aRchaic, argus, Bwigg, FQC, KLRfome, mapDamage, MicroPasts, pyrho, SAGAscape
- 25 HALLUCINATED: 15 JOAD fabrications + 10 cross-validated confabulations
- 2 FALSE_POSITIVE: ArchABM (wrong domain), archCandy (wrong domain)

Note: Project files in /mnt/project/ are read-only with outdated Bwigg classification. Use v2 files.

## Outstanding Tasks
- [x] Failure analysis: complete with 6 types
- [x] Outcome counts: verified
- [x] Slop/quality evaluation: 10 entries evaluated using Shaib et al. (2025) framework
- [x] Word counts: all 89 successful entries (mean 678, range 289-986)
- [x] Pipeline reconciliation: Discovery vs OpenArchaeo no-DVC pathways traced
- [x] Bwigg status clarified: real tool, cross-validated, but minimal footprint
- [x] Documentation updated: v2 files created for read-only project files
- [ ] Draft Methods section on comparative elimination
- [ ] Revise Section 4.2 (OpenAI)
- [ ] Clarify Brian's process for signs-of-life prompt (V1→V5→V7)

## Key Quotes/Observations to Preserve
- "Advanced undergrad to beginning PhD RA, along a jagged frontier"
- Prompt development: "empirical, each started shorter and elaborated as problems emerged"
- Metadata prompt methodology is itself an *outcome* of the paper, not just a tool
- Metadata (Claude) and Evidence (ChatGPT DR) operated independently — different models, different success criteria
- Bwigg: only tool to fall through both downstream pipelines despite verified discovery
