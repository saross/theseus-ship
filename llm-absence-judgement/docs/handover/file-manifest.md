# File Manifest: Documentation Session (December 2025)

## Files in /mnt/user-data/outputs/

| File | Size | Description | Status |
|------|------|-------------|--------|
| `working_notes_section4.md` | 19K | Comprehensive working notes for Section 4 Findings. Contains all quantitative summaries, failure taxonomies, model performance patterns, pipeline reconciliation, and Bwigg methodological finding. **Most complete reference document.** | Complete |
| `evidence_tool_pathway_trace.md` | 12K | Traces all 125 tools in evidence dataset back to discovery pathways. Documents Discovery (96 tools) vs OpenArchaeo no-DVC (29 tools) split. | Complete |
| `disambiguation_failures_analysis_v2.md` | 12K | Detailed characterisation of 7 disambiguation failures. **v2 corrects Bwigg classification** from "no signal" to "verified real, minimal footprint". | Complete |
| `failure_analysis_v2.md` | 8K | Failure taxonomy with 6 types. **v2 corrects Bwigg** and adds Type 1d: Minimal Online Footprint. | Complete |
| `tool_verification_status_updated.csv` | 5K | Corrections to original verification status. Contains 37 tool updates (10 VERIFIED_REAL, 25 HALLUCINATED, 2 FALSE_POSITIVE). | Complete |
| `compact_message_draft.md` | 7K | Summary document for starting new chat sessions. Contains project context, current state, key findings, and task checklist. | Complete |
| `FILE_MANIFEST.md` | - | This file | - |

---

## Key Corrections Made Across Sessions

### Session #1 (LLM paper results verification #1)
- Initial comprehensive analysis
- Created slop evaluation framework using Shaib et al. (2025)
- Established failure taxonomies
- Documented 1,874 evidence rows for 105 tools

### Session #2 (LLM paper results verification #2)  
- Fixed merged ArchaeoPhases+Archeofrag entry
- Fixed orphaned ringR fragments
- Verified kdedemo1 as real MATLAB routine
- Removed "GIS" and "3D scanning..." as generic categories
- Reduced count from 244 to 240 unique tools

### Session #3 (LLM paper results verification #3)
- Established principle: LLM corruption = keep as evidence; processing corruption = restore
- KLRfome preserved as "CAPTURE_ERROR"
- **Bwigg verified as REAL** (2003 IA article by Christen)
- ChronCluster marked as likely hallucination
- ChronoModelr identified as confabulation (real tool is RChronoModel)

### Session #4 (LLM paper results verification #4)
- ChronoModelr reclassified as "CONFABULATED_NEAR_MATCH"
- **ArchABM revealed as sophisticated confabulation** with DOI hijacking (10.21105/joss.01201 → TraitDB)
- archr confirmed as hallucination
- Multiple JOAD "extreme fail" tools confirmed as fabrications

### This Session (Documentation Update)
- Created v2 versions of failure analysis files with Bwigg correction
- **Added Bwigg to tool_verification_status_updated.csv** (was missing)
- Documented Bwigg as methodological finding (real tool, but web-based research can't document early 2000s tools with minimal online footprint)

---

## Final Verification Counts

From `tool_verification_status_updated.csv` (37 corrections):
- **10 VERIFIED_REAL**: ARCHIS, aRchaic, argus, Bwigg, FQC, KLRfome, mapDamage, MicroPasts, pyrho, SAGAscape
- **25 HALLUCINATED**: 15 JOAD fabrications + archr, chora, ChronCluster, ChronoModelr, OpenEthnology, pastR, pyArchaeo, RACER, RChrono, rhip
- **2 FALSE_POSITIVE**: ArchABM (wrong domain), archCandy (wrong domain)

---

## Outstanding Work for Paper

- [ ] Draft Section 4 data task subsections using working notes
- [ ] Verify Brian's prompt evolution details (V1→V5→V7 for evidence)
- [ ] Confirm Gemini Wayback duplication specifics
- [ ] Final reconciliation of 244-tool master dataset with all corrections

---

## Read-Only Project Files (NOT Updated)

The following files in `/mnt/project/` contain **outdated Bwigg classification** (listed as "insufficient documentation" or "no signal"):
- `failure_analysis.md`
- `disambiguation_failures_analysis.md`
- `tool_verification_status.csv`

Use the v2 versions in `/mnt/user-data/outputs/` instead.

---

*Manifest created: December 2025*
