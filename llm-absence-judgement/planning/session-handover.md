# Session Handover: Discovery Event Verification

**Last updated:** 2025-12-18 (JOINT REVIEW COMPLETE)
**Task:** Manual verification of tool discovery events in `results-tools/tool-discovery-granular.csv`

---

## Current Progress

| Metric | Count |
|--------|-------|
| Total discovery events | 350 |
| Events with evidence notes | **350** |
| Events still needing evidence notes | **0** |
| **Status** | **COMPLETE - JOINT REVIEW FINISHED** |

**All 350 events have been verified, evidence notes added, and joint batch-by-batch review completed (Batches 1-35).**

### Final Verification Summary

| Status | Count | % |
|--------|-------|---|
| CONFIRMED | 230 | 65.7% |
| MISATTRIBUTED | 70 | 20.0% |
| CONFABULATED | 50 | 14.3% |

**Outcome:** 230 successes (65.7%), 120 failures (34.3%)

**Note:** DISCOVERY_ERROR merged into CONFABULATED. Sketchfab (2 events for same article) harmonised to CONFABULATED - source hallucination pattern.

---

## Verification Workflow

Working through entries in batches of 10:

1. Display 10 entries with full context (tool name, status, article, journal, URL)
2. Review each entry against source article
3. Confirm/correct verification status
4. Add evidence note documenting the verification
5. For duplicates: inherit status but confirm discovery metadata is accurate to that event

---

## Key Decisions (from Dec 14 session)

### Inclusion Criteria

1. **Commercial software repurposed for research = INCLUDE**
   - We want to capture repurposed commercial software to compare longevity of commercial vs non-commercial tools
   - The prompt could have been clearer; this is the *desired* outcome

2. **Research vs generic is the deciding factor, not commercial vs non-commercial**
   - Boundary case: Agisoft PhotoScan/Metashape - SfM/photogrammetry is "research enough" to include
   - Would NOT include: QGIS, ArcGIS (generic GIS platforms)
   - WOULD include: research-specific plugins/extensions to generic platforms
   - 3D modelling tools for archaeology = generally "in" as research tools

3. **Companion programs, plugins, extensions**
   - May not have same lifecycle as "main" software
   - Consider tracking separately
   - Still valid discovery events

4. **Secondary references are valid**
   - If a paper references another paper that mentions the tool, that's still a valid discovery event
   - Correct level of sensitivity for discovery phase

### Verification Status Categories

- **CONFIRMED**: Tool exists and is correctly identified as archaeological/research software
- **MISATTRIBUTED**: Tool exists but is generic software, not research-specific (e.g., Paint Shop Pro, WordPress)
- **CONFABULATED**: Tool does not exist, name is fabricated, OR tool exists but presence in source was fabricated (source hallucination)
- **UNCLEAR**: Cannot determine; needs further investigation

---

## Batch Progress Log

### Batch 1 (Lines 2-34) - COMPLETED Dec 14

- Reviewed sample run entries (lines 2-11)
- Reviewed IA-31-67 fail entries (lines 12-31)
- Reviewed start of IA-run2-success entries (lines 32-34)
- Key cases documented: ABCD (archaeobotanical database)

### Batch 2 (Lines 35-44) - COMPLETED Dec 15

All entries from article: "Sensuous and reflexive GIS: exploring visualisation and VRML" (IA issue 1, 1996)

| Line | Tool | Final Status | Evidence Note |
|------|------|--------------|---------------|
| 35 | Vistapro | CONFIRMED | Commercial landscape visualisation software repurposed for archaeological terrain modelling |
| 36 | Vistamorph | CONFIRMED | Commercial morphing/animation software used for archaeological visualisation sequences |
| 37 | Photomodeller | CONFIRMED | Photogrammetry software for 3D reconstruction - research-relevant (cf. Agisoft inclusion) |
| 38 | Fountain | CONFIRMED | VRML authoring tool used for archaeological 3D model creation |
| 39 | Pioneer | CONFIRMED | Commercial 3D landscape software repurposed for archaeological terrain visualisation |
| 40 | Pioneer Pro | CONFIRMED | Commercial 3D landscape software (enhanced version) repurposed for archaeological visualisation |
| 41 | Truespace | CONFIRMED | Commercial 3D modelling software repurposed for archaeological object/site reconstruction |
| 42 | Land Survey System | MISATTRIBUTED | Generic surveying software - not research-specific tooling |
| 43 | Paint Shop Pro | MISATTRIBUTED | Generic image editing software - not research-specific |
| 44 | Wcvt2Pov | CONFIRMED | Format conversion utility supporting archaeological 3D visualisation workflow |

**Status changes**: Pioneer, Pioneer Pro, Truespace changed from MISATTRIBUTED to CONFIRMED based on inclusion criteria decision that commercial 3D software repurposed for archaeological work counts as research tooling.

### Batch 3 (Lines 45-54) - COMPLETED Dec 15

Articles in this batch:
- "Sensuous and reflexive GIS" (Gillings & Goodrick) - continuation
- "The archaeological use of Kernel Density Estimates" (Beardah & Baxter)
- Editorial (Vince) - IA issue 2
- "The need for solid modelling of structure in the archaeology of buildings" (Daniels)

| Line | Tool | Final Status | Evidence Note |
|------|------|--------------|---------------|
| 45 | Arc/Info | MISATTRIBUTED | Generic GIS platform - not research-specific (cf. ArcGIS exclusion) |
| 46 | MATLAB | MISATTRIBUTED | Generic scientific computing platform - not research-specific |
| 47 | kdedemo1 | CONFIRMED | Archaeological KDE demonstration tool by Beardah & Baxter |
| 48 | kdedemo2 | CONFIRMED | Archaeological KDE demonstration tool by Beardah & Baxter |
| 49 | pnuts | DISCOVERY_ERROR | Extracted from HTML template comments - not actual software |
| 50 | htmltoc | CONFIRMED | IA publication utility for generating tables of contents |
| 51 | htmlfig | CONFIRMED | IA publication utility for figure handling |
| 52 | AutoCAD | MISATTRIBUTED | Generic CAD platform - not research-specific |
| 53 | MicroStation | MISATTRIBUTED | Generic CAD platform - not research-specific |
| 54 | Rhino for AutoCAD | CONFIRMED | Research-specific 3D modelling plugin to generic CAD platform |

**Status changes**: Rhino for AutoCAD changed from MISATTRIBUTED to CONFIRMED (research-specific plugin heuristic).

**Cross-validation note**: Tools can be cross-checked against `02-tool-metadata.xlsx` - if a tool was investigated at the metadata collection phase, it met the tool definition at discovery.

### Batches 4-32 (Lines 55-351) - COMPLETED Dec 15

All remaining batches verified in extended session:

- **Batches 4-11 (Lines 55-134)**: IA articles - mix of CONFIRMED research tools and MISATTRIBUTED generic software
- **Batches 12-19 (Lines 135-214)**: IA articles continued, JOSS-worthless-o3 run (many confabulations), JCAA articles
- **Batches 20-26 (Lines 215-284)**: JCAA articles, JOAD-extreme fail run (all confabulations), JOSS-fail-possible run
- **Batches 27-30 (Lines 285-330)**: JOSS-secondpass (much better quality), Perplexity-SyntheticPrompt-DR
- **Batches 31-32 (Lines 331-351)**: Perplexity run, SoftwareX-run1-accessFail

**Key findings:**
- JOAD-extreme fail: Complete failure mode - articles, authors, and DOIs all fabricated
- JOSS-fail-possible: Mix of real packages and near-miss confabulations
- JOSS-secondpass: High quality run with mostly valid tools
- SoftwareX-run1-accessFail: Some DOI hijacking confabulations identified

---

## Files

- **Data file**: `results-tools/tool-discovery-granular.csv`
- **Status legend**: `results-tools/verification-status-legend.md`
- **This handover**: `planning/session-handover.md`

---

## Verification Complete

**All 350 discovery events have been verified and jointly reviewed (Batches 1-35).**

### Session Corrections (2025-12-18)

14 entries corrected from MISATTRIBUTED to CONFIRMED after cross-referencing with successful metadata evaluations in `02-tool-metadata.xlsx`:

- Gephi (5 occurrences: lines 8, 18, 113, 159, 336)
- Polynomial Texture Mapping (2 occurrences: lines 16, 111)
- MicroStation (line 53)
- TensorFlow (line 131)
- ade4 (line 328)
- SpadeR (line 329)
- vegan (line 330)
- WaveSurfer 1.8.8 → matched to WaveSurfer (line 130)
- Land Survey System → matched to LSS (line 42)

**Key decision:** Successful metadata collection always means CONFIRMED (tool met the definition at the metadata phase).

### Confabulation Verification (Batch 35)

Three confabulations in SoftwareX-run1-accessFail thoroughly verified using full protocol (GitHub, CRAN, PyPI, web search, DOI verification):

| Line | Claimed Tool | Actual DOI Owner | Pattern |
|------|--------------|------------------|---------|
| 349 | Hyperspectral Image Analysis Toolbox | XDrift (pesticide R pkg) | DOI hijacking |
| 350 | ringR | LyapXool (Lyapunov C++ program) | DOI hijacking + not on CRAN/GitHub |
| 351 | SimLex | FLBEIA (fisheries bio-econ) | DOI hijacking + author confusion |

### Manual Review Complete

All items in `verification-todo.md` have been resolved:
- Line 106: Virtual Amarna Project → MISATTRIBUTED (digital archive/dataset, not software tool)
