# Tool Origin Reconciliation: Tracing 89 Investigated Tools

## Summary

Of the 129 entries in the Tool Master List, **89 tools have complete metadata** (Description + History). This document traces the origin of each investigated tool.

---

## Category Breakdown

| Category | Count | Percentage |
|----------|------:|----------:|
| Discovery (direct match) | 62 | 69.7% |
| Discovery (name variant) | 19 | 21.3% |
| Discovery (bundled mention) | 1 | 1.1% |
| Split from discovered entry | 4 | 4.5% |
| Lead-following/serendipitous | 3 | 3.4% |
| OpenArchaeo without DVCS | 0 | 0% |
| **TOTAL** | **89** | **100%** |

---

## 1. From Discovery (Direct Match) â€” 62 tools

These tools were found during discovery runs and match directly (case-insensitive) with the investigated tool name.

| Tool |
|------|
| AION |
| ARIADNE |
| Annotorious |
| ArcGIS skeletal templates |
| Arch-I-Scan |
| ArchAIDE |
| ArchEd |
| ArchaeoPhases |
| ArcheoFrag |
| BCal |
| Bchron |
| DataScribe |
| Distant Viewing Toolkit |
| Gephi |
| HTMLfig |
| Intrasis |
| KLRfome |
| Kairos |
| LifeForms |
| Luminescence |
| MASA Consortium |
| MapReader |
| Mask R-CNN |
| Matrix Manager |
| MicroStation |
| OASIS |
| OxCal |
| Polynomial Texture Mapping (PTM) |
| PyLithics |
| Rhino for AutoCAD |
| SEAHORS |
| STAR |
| STELLAR |
| Scripto |
| Shoredate |
| SpadeR |
| Survey2GIS |
| Tabula |
| TensorFlow |
| TimeMap |
| Vistamorph |
| Voro++ |
| XVR |
| Zooniverse Project Builder |
| ade4 |
| archeoViz |
| bleiglas |
| c14bazAAR |
| dplR |
| glottoTrees |
| glottospace |
| iDig |
| iconr |
| lingtypR |
| lingtypology |
| oxcAAR |
| qlcData |
| rcarbon |
| recexcavAAR |
| straditize |
| stratigraphr |
| vegan |

---

## 2. From Discovery (Name Variant) â€” 19 tools

These tools were discovered under a different name and standardised during metadata collection.

| Investigated Tool | Discovered As |
|-------------------|---------------|
| Agisoft PhotoScan/Metashape | Agisoft PhotoScan |
| ArcGIS Spatial Analyst | Spatial Analyst 2.0 |
| DepthmapX | Depthmap |
| EndovÃ©lico | EndovÃ©lico information system |
| FellingDater | fellingdater |
| FieldWorker | FieldWorker Advanced 2.3.5 / FieldWorker Pro 0.91 |
| FilmColors (VIAN) | FilmColors |
| LSS (Land Survey System) | Land Survey System |
| Perseus Digital Library | Perseus 2.0 |
| PhotoModeler | Photomodeller |
| SASSA | SASSA (web-based system) |
| TrueSpace | Truespace |
| VOSviewer | VOSviewer (bibliometric mapping software) |
| VirtualArch | VirtualArch project platform |
| VistaPro | Vistapro |
| WallGIS | WallGIS database and GIS |
| WaveSurfer | WaveSurfer 1.8.8 (audio analysis software) |
| gvSIG | gvSIG CE |
| kdedemo | kdedemo1 / kdedemo2 |

---

## 3. From Discovery (Bundled Mention) â€” 1 tool

Tools discovered as semicolon-separated mentions within an article discussing multiple tools.

| Tool | Source Article | Bundled With |
|------|----------------|--------------|
| htmltoc | IA Editorial | pnuts; htmlfig |

---

## 4. Split from Discovered Entry â€” 4 tools

Single discovered entries that revealed multiple distinct tools upon investigation.

| Investigated Tool | Split From |
|-------------------|------------|
| LogicistWriter | MASA Consortium |
| OpenArchaeo (semantic web platform) | MASA Consortium |
| OpenGuide | MASA Consortium |
| POV-Ray | Wcvt2Pov |

**Note:** MASA Consortium was discovered as a single entry but investigation revealed it encompasses three distinct tools.

---

## 5. Lead-Following / Serendipitous â€” 3 tools

Tools discovered during investigation of other tools, either as suggested alternatives or as related tools in the same domain.

| Investigated Tool | Lead From | Relationship |
|-------------------|-----------|--------------|
| ArchaeoGRID | Grid Machine (confabulation) | Found while investigating the non-existent "Grid Machine" |
| Rhinoceros 3D | Rhino for AutoCAD | Suggested as the parent software |
| StratiGraf | Matrix Manager / ArchEd / stratigraphic tools | Discovered during investigation of stratigraphic software domain |

---

## 6. OpenArchaeo without DVCS â€” 9 tools (evidence only)

**These tools were investigated for evidence but NOT added to the Master List for metadata collection.**

| Tool | Evidence Rows | Notes |
|------|--------------|-------|
| ArboDat | 20 (across 4 variants) | ArboDat, ArboDat / APE, ArboDat 2016, ArboDat+ |
| ChronoLog | 26 | |
| HumanOS | 18 | |
| SÃ©riation de matrice en prÃ©sence/absence | 10 | |
| Bonify | 10 | |
| benmarwickopencontext.r | 6 | |
| munsell-plot.R | 6 | |
| tweet-edits-to-archaeology-articles.R | 6 | |
| archaeology_on_wikipedia.R | 4 | |

**Implication:** Evidence collection was more comprehensive than metadata collection. These 9 tools have evidence (1,874 total rows dataset) but no formal metadata entry.

---

## Revised Category Breakdown

| Category | Count | Percentage |
|----------|------:|----------:|
| Discovery (direct match) | 62 | 69.7% |
| Discovery (name variant) | 19 | 21.3% |
| Discovery (bundled mention) | 1 | 1.1% |
| Split from discovered entry | 4 | 4.5% |
| Lead-following/serendipitous | 3 | 3.4% |
| **Subtotal: Tools with metadata** | **89** | **100%** |
| | | |
| OpenArchaeo no-DVCS (evidence only) | 9 | â€” |
| **Total tools investigated (any capacity)** | **98** | â€” |

---

## OpenArchaeo Overlap Analysis

**20 tools** were found in BOTH the discovery phase AND OpenArchaeo (with DVCS):

| Tool | Match Type |
|------|------------|
| aion | exact |
| ArchaeoPhases | exact |
| ArchAIDE | exact |
| Archeofrag | exact |
| archeoViz | exact |
| Bchron | exact |
| bleiglas | exact |
| c14bazAAR | exact |
| dplR | exact |
| fellingdater/FellingDater | high |
| iconr | exact |
| kairos | exact |
| Luminescence | exact |
| oxcAAR | exact |
| rcarbon | exact |
| recexcavAAR | exact |
| SEAHORS | exact |
| shoredate | exact |
| stratigraphr | exact |
| tabula | exact |

This 20-tool overlap represents **redundant discovery** â€” these tools would have been found from OpenArchaeo alone. The **71 tools unique to discovery** represent the genuine value-add of the AI-assisted discovery process.

---

## Documented Failures (8 tools â€” not investigated)

These tools were discovered but could not be successfully investigated:

| Tool | Failure Reason |
|------|----------------|
| Bwigg | Insufficient documentation online |
| FaceNet | Name collision (Google neural network) |
| Fountain (VRML tool) | Name collision (multiple software) |
| Grid Machine | Confabulation â€” does not exist |
| Microware | Name collision (generic term) |
| PyCoCu | No verifiable online presence |
| Wcvt2Pov | Insufficient information (but led to POV-Ray discovery) |
| pnuts | Name collision (Yahoo platform) |

---

## Notes on Methodology

1. **Name variations count as successes** â€” per project convention, tools discovered under variant names (e.g., "Depthmap" â†’ "DepthmapX") are categorised as successful discoveries with name standardisation during metadata collection.

2. **Splits and serendipitous discoveries are separate categories** â€” these represent tools that emerged during the investigation process rather than directly from discovery prompts.

3. **The discovery â†’ investigation pipeline** shows 91 discovered â†’ 89 investigated (accounting for 8 failures + bundled mentions + splits).

---

## Pipeline Summary

```
DISCOVERY PHASE
â”œâ”€â”€ 91 tools discovered
â”‚   â”œâ”€â”€ 62 direct matches â†’ investigated (metadata)
â”‚   â”œâ”€â”€ 19 name variants â†’ investigated (metadata)
â”‚   â”œâ”€â”€ 1 bundled mention (htmltoc) â†’ investigated (metadata)
â”‚   â”œâ”€â”€ 1 split source (MASA) â†’ 3 tools investigated (metadata)
â”‚   â”œâ”€â”€ 1 split source (Wcvt2Pov) â†’ 1 tool investigated (metadata)
â”‚   â””â”€â”€ 8 failures â†’ evidence only, no metadata
â”‚
â”œâ”€â”€ Lead-following during investigation
â”‚   â””â”€â”€ 3 additional tools discovered (ArchaeoGRID, Rhinoceros 3D, StratiGraf)
â”‚
â”œâ”€â”€ OpenArchaeo no-DVCS tools
â”‚   â””â”€â”€ 9 tools investigated for evidence only (not added to Master List)
â”‚
â””â”€â”€ INVESTIGATION TOTALS:
    â”œâ”€â”€ 89 tools with complete metadata (Description + History)
    â”œâ”€â”€ 8 documented failures (evidence collected, metadata failed)
    â”œâ”€â”€ 9 OpenArchaeo no-DVCS (evidence only)
    â””â”€â”€ 105 unique tools in evidence spreadsheet
```

---

## Evidence vs Metadata Discrepancy

The evidence spreadsheet contains **105 unique tools**, while the Master List has **89 tools with metadata**. The 16-tool difference comprises:

| Category | Count |
|----------|------:|
| Name variants (same tool, different name in evidence) | 14 |
| Documented failures (evidence but no metadata) | 8* |
| OpenArchaeo no-DVCS (evidence only) | 9 |
| Split parents (MASA Consortium) | 1 |
| Special cases (FAIMS ground truth, Stratigraph) | 2 |

*Note: 7 failures are in Master List without descriptions; some overlap with evidence name variants.

The overlap explains why 105 evidence tools + adjustments = 89 metadata tools + 9 evidence-only + 8 failures - name variants and special cases.

---
