# Absence of Judgment: Project Data Manifest

Generated: December 2025

---

## Core Quantitative Data Files

### Tool Discovery Data

| File | Rows | Size | Purpose |
|------|------|------|---------|
| `tool-discovery-summary.csv` | 244 | 72K | **De-duplicated tool list**: One row per unique tool with aggregated discovery metadata (services, journals, hallucination risk) |
| `tool-discovery-granular.csv` | 351 | 121K | **All discovery instances**: One row per discovery event, preserving full provenance (which service found what, in which journal, from which run) |
| `tool_discovery_complete.xlsx` | — | 75K | Excel workbook containing both summary and granular sheets |

**Key columns in summary**: Tool_Name_Standardised, Discovery_Count, LLM_Services, Hallucination_Risk
**Key columns in granular**: Tool_Name_Raw, Tool_Name_Standardised, LLM_Service, LLM_Model, Harness, Run_Quality, Journal

### Tool Verification Data

| File | Rows | Size | Purpose |
|------|------|------|---------|
| `tool_verification_status_final.csv` | 242 | 21K | **Canonical verification status**: Each discovered tool's reality status (verified, hallucinated, false positive, etc.) |
| `tool_verification_status.csv` | 244 | 20K | *Superseded* — older version without Notes column |
| `tool_verification_summary.txt` | — | 512B | Quick text summary of verification counts |

**Key columns**: Tool, Verification_Status, Hallucination_Risk, Status_Simple, Notes

**Status values**:
- VERIFIED / LIKELY_REAL: Confirmed real tools
- HALLUCINATED / LIKELY_HALLUCINATED: Fabricated by LLM
- FALSE_POSITIVE: Real but not a tool (e.g., technology category)
- AMBIGUOUS / UNCERTAIN: Requires further investigation

### Metadata Quality Assessment

| File | Rows | Size | Purpose |
|------|------|------|---------|
| `slop_evaluation_results.csv` | 10 | 1.4K | Quantitative slop metrics for 10 sampled tool metadata entries |
| `word_counts_all_entries.csv` | 89 | 3.6K | Word counts by field (Description, History, Technical, Strengths, Weaknesses) for all successful metadata entries |
| `slop_evaluation_detailed_report.md` | — | 16K | Full qualitative slop evaluation using Shaib et al. (2025) framework |
| `slop_evaluation_prompt.md` | — | 10K | The prompt/framework used for slop evaluation |

**Key metrics**: Anchored claims per 100 words, generic phrase count, overall slop assessment (None/Minimal/Moderate/Significant)

---

## Analysis Documents

### Failure Analysis

| File | Purpose |
|------|---------|
| `failure_analysis.md` | Initial failure taxonomy (6 types) |
| `failure_analysis_comprehensive.md` | Complete failure analysis across discovery and evidence tasks |
| `disambiguation_failures_analysis.md` | Detailed characterisation of the 8 documented metadata failures |

### Success Analysis

| File | Purpose |
|------|---------|
| `success_analysis_comprehensive.md` | Patterns distinguishing successful from failed runs |
| `tool_origin_reconciliation.md` | Tracing all 89 investigated tools back to discovery pathways |
| `evidence_tool_pathway_trace.md` | Tracing all 125 evidence dataset tools to their origins |

### Working Documents

| File | Purpose |
|------|---------|
| `working_notes_section4.md` | Comprehensive notes for Section 4 (Findings) |
| `draft_section4_data_tasks.md` | Draft findings for tool discovery, metadata, and evidence subsections |
| `section4_data_collection_drafts.md` | Enhanced data collection subsections for OpenAI/Anthropic/Google |
| `compact_message_draft.md` | Condensed session continuity document |
| `questions_for_brian.md` | Outstanding questions for co-author |

---

## Key Quantitative Findings (Quick Reference)

### Tool Discovery
- **91 tools discovered** across successful journal searches
- **19 overlap** with OpenArchaeo baseline (376 tools)
- **15 confirmed hallucinations** (all from JOAD "extreme fail" run)
- **Cross-validation**: 3 tools found by 3 services; 40 tools found by 2+ services

### Metadata Collection
- **97 tools investigated** for comprehensive metadata
- **89 successful** (92% success rate)
- **8 documented failures** — all attributable to upstream discovery issues
- **100% prompt success rate** for documentable tools

### Evidence Collection
- **1,874 evidence rows** in combined dataset
- **105 unique tools** with evidence
- **95% from ChatGPT Deep Research**

### Output Quality (Slop Assessment)
- **2 "None" / 8 "Minimal"** across 10 sampled entries
- **Mean: 1.9 anchored claims per 100 words**
- **Mean word count: 678 words** (range 289–986)

---

## File Relationships

```
tool-discovery-granular.csv (351 instances)
        │
        ▼ de-duplicate by Tool_Name_Standardised
tool-discovery-summary.csv (244 unique tools)
        │
        ▼ verify each tool
tool_verification_status_final.csv (242 tools with status)
        │
        ├─► 204 VERIFIED/LIKELY_REAL → metadata collection
        ├─► 15 HALLUCINATED → excluded
        ├─► 2 FALSE_POSITIVE → excluded
        └─► remainder: uncertain/capture error

word_counts_all_entries.csv (89 successful metadata entries)
        │
        ▼ sample 10 entries
slop_evaluation_results.csv (quality metrics)
```

---

## Source Spreadsheets (Not in Project Directory)

These are referenced in analysis documents but stored separately:
- `tool-discovery.xlsx` — Raw discovery outputs (12 sheets)
- `Tool_master_list.xlsx` — Master list with metadata (97 tools)
- `tool-evidence__1_.xlsx` / `tool-evidence__4_.xlsx` — Evidence of life data (1,874 rows)
- `Openarchaeo-work.xlsx` — OpenArchaeo baseline comparison (445 rows)

---

## Document References

| Document | Purpose |
|----------|---------|
| `AbsenceJudgement.tex` | Main paper manuscript |
| `Writing_style_guide` | Style conventions for paper |
| `Context_for_Dataset_Creation_and_Description_Sections.md` | Background for Section 4 work |
| `tool_discovery_README.md` | Documentation for discovery dataset |
| `SoftwareXevidencechat.pdf` | Chat transcript showing vibes-based output pattern |

---

*Manifest generated for transition to Claude Code environment*