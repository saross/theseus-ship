# Document Relationship Guide for Claude Code

## Overview

This project includes multiple analysis documents created during verification sessions. This guide explains how they relate and when to consult each.

---

## Primary Documents

### `HANDOFF_TO_CLAUDE_CODE_clean.md` — START HERE

This is the **authoritative orientation document**. Always read this first.

**Contents:**
- Canonical numbers and key decisions (verified, reconciled)
- What's been decided and what's outstanding
- Priorities and immediate tasks
- Key patterns and principles (distilled)
- Style notes and cross-references

**Characteristics:**
- ~300 lines, structured for quick reference
- Fully updated with latest corrections (7 failures, not 8)
- Clean encoding (no mojibake)
- Designed for efficient onboarding

---

### `working_notes_section4_clean.md` — DEEP REFERENCE

Consult this document when you need **granular detail** beyond what's in the handoff.

**Contents:**
- Complete analysis trail with intermediate findings
- Full tool origin reconciliation (89 tools traced individually)
- Detailed examples and concrete metrics
- Practical recommendations by task type
- Extended failure and success characterisation

**Characteristics:**
- ~500+ lines with extensive working detail
- Clean encoding (corrected from original)
- Fully updated with Verification #5 corrections (7 failures, Bwigg reclassification)
- Designed as audit trail and reference

**Note:** The original `working_notes_section4.md` may still exist in the project but is superseded by the clean version.

---

## Key Differences

| Aspect | Handoff | Working Notes (Clean) |
|--------|---------|----------------------|
| Purpose | Orientation + action | Reference + audit trail |
| Currency | Fully updated | Fully updated |
| Detail level | Distilled principles | Full examples and metrics |
| Length | ~300 lines | ~500+ lines |
| Encoding | Clean | Clean |
| When to use | First, always | When you need specifics |

---

## Conflict Resolution

**Both documents are now current and should be consistent.** If any discrepancy is found, the handoff document is authoritative.

Key figures that should match across documents:
- Failure count: **7 failures** (after Bwigg reclassification)
- Evidence attribution: **849 rows (BBS) / 330 rows (SAR)**
- Tool discovery: **91 discovered → 97 investigated → 89 successful**

The evidence row discrepancy (**1,874 vs 1,179 total rows**) remains unresolved and needs verification against `03-tool-evidence.xlsx`.

---

## Supporting Analysis Documents

These documents provide detailed analysis on specific topics. Consult as needed:

| Document | Purpose | When to Use |
|----------|---------|-------------|
| `working_notes_section4_clean.md` | Comprehensive working notes (clean) | Granular detail, full reconciliation tables |
| `success_analysis_comprehensive.md` | Patterns distinguishing successful runs | Understanding what worked and why |
| `failure_analysis_comprehensive.md` | Complete failure taxonomy with examples | Detailed failure mode examples |
| `disambiguation_failures_analysis.md` | Detailed analysis of 7 metadata failures | Specific failure case studies |
| `tool_origin_reconciliation.md` | Tracing 89 tools to discovery pathways | Pipeline verification |
| `evidence_tool_pathway_trace.md` | Tracing 125 evidence tools to origins | Evidence collection verification |
| `draft_section4_data_tasks.md` | Draft findings for data subsections | Starting point for Section 4 completion |
| `section4_data_collection_drafts.md` | Enhanced subsections for OpenAI/Anthropic/Google | More developed draft text |
| `slop_evaluation_detailed_report.md` | Full qualitative slop assessment | Output quality methodology |
| `questions_for_brian.md` | Outstanding questions for co-author | Items requiring Brian's input |

---

## Recommended Workflow

1. **Read `HANDOFF_TO_CLAUDE_CODE_clean.md` completely** — this orients you to current state
2. **Check Section 11 (Immediate Priorities)** — this tells you what to do first
3. **Consult `working_notes_section4_clean.md`** when you need:
   - Specific tool-by-tool reconciliation data
   - Detailed examples for paper text
   - Full metrics and counts
   - Practical recommendations by task type
4. **Consult supporting documents** for deep dives on specific topics

---

## Notes on Data Currency

The verification sessions occurred in sequence (#1 through #5), with later sessions correcting earlier findings:

- **Verification #1**: Initial analysis, failure taxonomy, slop evaluation
- **Verification #2**: Data correction (some errors made)
- **Verification #3**: Corrected #2 errors, established corruption handling principle, Bwigg reclassification
- **Verification #4**: ArchABM multi-layered confabulation, archr confirmation, ChronoModelr
- **Verification #5**: Canonical tool counts, pipeline reconciliation

**Document consolidation (December 2025):** Both the handoff document and working notes have been cleaned and updated to integrate all corrections from the verification sessions. The original `working_notes_section4.md` (with encoding issues) may still exist but is superseded by `working_notes_section4_clean.md`.

---

*Guide prepared December 2025*
