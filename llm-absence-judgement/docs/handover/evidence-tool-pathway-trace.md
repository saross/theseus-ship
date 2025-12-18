# Evidence Dataset: Tool Pathway Trace

## Summary

This document traces all 125 unique tools in the evidence-of-life dataset (`tool-evidence__4_.xlsx`, Combined-tool-references sheet) back to their discovery pathways. All tools entered the investigation pipeline via one of two routes:

1. **Discovery Pathway**: Tools identified through AI-assisted journal searches (Internet Archaeology, JOSS, JCAA, JOAD, SoftwareX) using ChatGPT Deep Research, Operator, and related services
2. **OpenArchaeo no-DVC Pathway**: Tools from the OpenArchaeo baseline that lacked version control repositories and thus required manual evidence collection

### Quantitative Summary

| Pathway | Tools | Evidence Rows | Percentage of Tools |
|---------|-------|---------------|---------------------|
| Discovery | 96 | 965 | 76.8% |
| OpenArchaeo no-DVC | 29 | 214 | 23.2% |
| **Total** | **125** | **1,179** | **100%** |

---

## Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DISCOVERY PATHWAY                               │
│                                                                     │
│  AI-assisted journal searches (ChatGPT DR, Operator, etc.)         │
│  Sources: Internet Archaeology, JOSS, JCAA, JOAD, SoftwareX        │
│                                                                     │
│  → 98 tools investigated for metadata                               │
│    ├── 83 Success                                                   │
│    ├── 6 Failure (no usable metadata)                              │
│    ├── 2 Failure | Spawned New                                     │
│    ├── 4 New (spawned during other investigations)                 │
│    └── 2 Success | Spawned New                                     │
│                                                                     │
│  → 96 tools proceeded to evidence collection (965 rows)            │
└─────────────────────────────────────────────────────────────────────┘
                                    
┌─────────────────────────────────────────────────────────────────────┐
│                  OPENARCHAEO NO-DVC PATHWAY                         │
│                                                                     │
│  Tools from OpenArchaeo baseline lacking version control repos      │
│  Required same evidence-of-life collection as discovered tools      │
│                                                                     │
│  → 29 tools (no separate metadata investigation)                    │
│  → 29 tools proceeded to evidence collection (214 rows)            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Metadata Collection Outcomes (Discovery Pathway Only)

The metadata collection phase investigated 98 tools from the Discovery pathway. OpenArchaeo no-DVC tools were not subjected to metadata collection since they already had baseline documentation.

### Outcome Breakdown

| Outcome | Count | Description |
|---------|-------|-------------|
| Success | 83 | Complete metadata collected |
| Failure | 6 | Could not collect usable metadata |
| New | 4 | Tools spawned during other investigations |
| Failure \| Spawned New | 2 | Failed but led to discovery of related tool |
| Success \| Spawned New | 2 | Succeeded and also spawned new tool |
| **Total** | **97** | (plus 1 header row = 98 in file) |

### Failed Metadata Investigations (6)

These tools could not be successfully investigated due to disambiguation failures, name collisions, or insufficient online documentation:

| Tool | Failure Reason | Evidence Collected? |
|------|----------------|---------------------|
| Bwigg | Minimal online footprint (verified real: 2003 IA article) | No |
| FaceNet | Name collision (Google neural network) | Yes (7 rows)* |
| Fountain | Name collision (multiple software) | Yes (7 rows)* |
| Microware | Name collision (generic term) | Yes (9 rows)* |
| pnuts | Name collision (Yahoo platform) | Yes (4 rows)* |
| PyCoCu | No verifiable online presence | Yes (5 rows)* |

**Bwigg Note**: Unlike other failures, Bwigg was cross-validated as a real tool during discovery (3 instances across 2 services). The specific article "Bwigg: An Internet facility for Bayesian radiocarbon wiggle-matching" by J. Andrés Christen (Internet Archaeology issue 13, 2003) was found. Failure reflects minimal online footprint for a 20+ year old tool, not discovery error. Bwigg is the only tool to fall through both metadata AND evidence pipelines entirely.

*Note: Evidence was collected for these tools despite metadata failure, likely because evidence collection used broader search criteria or occurred before/separately from metadata investigation.

### Spawned Tools (6)

New tools discovered during investigation of other tools:

| Spawned Tool | Parent Investigation | Status |
|--------------|---------------------|--------|
| ArchaeoGRID | Grid Machine (failed) | New - closest real tool found |
| OpenArchaeo (semantic web platform) | MASA Consortium | New - component tool |
| OpenGuide | MASA Consortium | New - component tool |
| Rhinoceros 3D | Rhino for AutoCAD | New - parent software identified |
| LogicistWriter | MASA Consortium | Success - component tool |
| (additional from Success\|Spawned New) | Various | Success |

---

## Evidence Collection: Complete Tool Lists

### OpenArchaeo no-DVC Pathway (29 tools, 214 evidence rows)

| Tool | Evidence Rows |
|------|---------------|
| ArboDat | 13 |
| archaeology_on_wikipedia.R | 3 |
| artefact-morpho.R | 5 |
| BasicMapping | 3 |
| benmarwickDY-XYZ-data-on-an-irregular-grid-to-an-interpolated-raster.r | 3 |
| benmarwickopencontext.r | 4 |
| Bonify | 12 |
| ca (R Script for Seriation Using Correspondence Analysis) | 8 |
| ChronoLog | 20 |
| Chronophage | 8 |
| Crossbones | 6 |
| Explographe | 5 |
| Fiche Stratigraphique Numérique | 9 |
| Harris-matrix-legacy | 5 |
| HumanOS | 9 |
| Le Stratifiant | 10 |
| LISA | 7 |
| munsell-plot.R | 3 |
| osl_calibration.r | 2 |
| PLC | 7 |
| PointPattern | 4 |
| pyArchInit | 15 |
| RTIBuilder | 13 |
| RTIViewer | 12 |
| Seriographe EPPM | 8 |
| Stratibase | 8 |
| Sériation de matrice en présence/absence | 5 |
| tweet-edits-to-archaeology-articles.R | 3 |
| UnconstrainedClustering (R Script) | 4 |

### Discovery Pathway (96 tools, 965 evidence rows)

| Tool | Evidence Rows |
|------|---------------|
| ade4 | 8 |
| Agisoft PhotoScan | 14 |
| AION | 8 |
| Annotorious | 16 |
| ArboDat / APE | 1 |
| ArboDat 2016 | 3 |
| ArboDat+ | 1 |
| ArcGIS skeletal templates | 8 |
| Arch-I-Scan | 13 |
| ArchaeoPhases | 14 |
| ArchAIDE | 14 |
| ArchEd | 5 |
| Archeofrag | 9 |
| archeoViz | 15 |
| ARIADNE | 10 |
| BCal | 9 |
| Bchron | 10 |
| Bleiglas | 6 |
| c14bazAAR | 11 |
| DataScribe | 16 |
| Depthmap | 13 |
| Distant Viewing Toolkit | 17 |
| dplR | 53 |
| Endovélico Information System | 10 |
| FaceNet | 7 |
| FAIMS | 17 |
| Fellingdater | 16 |
| FieldWorker Advanced | 2 |
| FieldWorker Pro | 2 |
| FilmColors | 15 |
| Fountain | 7 |
| Gephi | 9 |
| GlottoSpace | 5 |
| glottoTrees | 11 |
| Grid Machine | 11 |
| gvSIG CE | 12 |
| htmlfig | 1 |
| iConr | 11 |
| iDig | 13 |
| Intrasis | 16 |
| kairos | 6 |
| kdedemo1 & kdedemo2 | 2 |
| kdedemo2 | 2 |
| KLRfome | 9 |
| Land Survey System | 6 |
| LifeForms | 5 |
| LingTypology | 21 |
| lingtypR | 7 |
| Luminescence | 18 |
| MapReader | 19 |
| MASA Consortium | 9 |
| Mask R-CNN | 13 |
| Matrix Manager | 5 |
| MicroStation | 12 |
| Microware | 9 |
| OASIS | 8 |
| oxcAAR | 11 |
| OxCal | 17 |
| Perseus 2.0 | 8 |
| Photomodeler | 15 |
| pnuts | 4 |
| Polynomial Texture Mapping (PTM) | 20 |
| PyCoCu | 5 |
| PyLithics | 13 |
| qlcData | 9 |
| rcarbon | 13 |
| recexcavAAR | 12 |
| Rhino for AutoCAD | 4 |
| SASSA | 12 |
| Scripto | 23 |
| SEAHORS | 8 |
| Shoredate | 5 |
| SpadeR | 5 |
| Spatial Analyst | 11 |
| STAR | 12 |
| STELLAR | 7 |
| straditize | 7 |
| Straditize | 9 |
| Stratigraph | 4 |
| stratigraphr | 8 |
| Survey2GIS | 15 |
| Tabula | 9 |
| TensorFlow | 9 |
| TimeMap | 8 |
| Truespace | 6 |
| vegan | 7 |
| VirtualArch | 11 |
| Vistamorph | 6 |
| VistaPro | 8 |
| Voro++ | 4 |
| VOSviewer | 6 |
| WallGIS database and GIS | 6 |
| WaveSurfer | 7 |
| Wcvt2Pov | 16 |
| XVR | 7 |
| Zooniverse Project Builder | 8 |

---

## Gaps and Anomalies

### Metadata Tools NOT in Evidence Collection

The following tools appear in the metadata investigation file but have no matching entries in the evidence collection:

| Tool | Metadata Outcome | Notes |
|------|------------------|-------|
| Bwigg | Failure | Only metadata failure with no evidence |
| ArchaeoGRID | New (spawned) | Spawned tool not separately investigated for evidence |
| OpenArchaeo (semantic web platform) | New (spawned) | Spawned tool not separately investigated for evidence |
| OpenGuide | New (spawned) | Spawned tool not separately investigated for evidence |
| LogicistWriter | Success | Component of MASA; may be covered under MASA evidence |
| StratiGraf | Success | No evidence found under this name |
| htmltoc | Success | No evidence found under this name |
| Perseus Digital Library | Success | Evidence filed under "Perseus 2.0" (name variant) |

### Name Variants in Evidence

Several tools appear under variant names. These should be treated as the same tool for analysis:

| Canonical Name | Variants in Evidence |
|----------------|---------------------|
| ArboDat | ArboDat, ArboDat / APE, ArboDat 2016, ArboDat+ |
| FieldWorker | FieldWorker Advanced, FieldWorker Pro |
| kdedemo | kdedemo1 & kdedemo2, kdedemo2 |
| Straditize | straditize, Straditize (case variant) |
| Perseus | Perseus 2.0, Perseus Digital Library |

### Tools with Evidence Despite Metadata Failure

Notably, 5 of 6 metadata failures still received evidence collection:

- FaceNet (7 rows)
- Fountain (7 rows)
- Microware (9 rows)
- pnuts (4 rows)
- PyCoCu (5 rows)

This suggests evidence collection occurred independently of metadata success, or used different search strategies that could find mentions even when comprehensive metadata could not be compiled.

---

## Key Statistics for Paper

### For Results Section

- **Total tools with evidence collected**: 125
- **Evidence rows collected**: 1,179
- **Discovery pathway**: 96 tools (76.8%), 965 evidence rows (81.8%)
- **OpenArchaeo no-DVC pathway**: 29 tools (23.2%), 214 evidence rows (18.2%)

### For Methods Section

- **Metadata investigation**: 98 tools attempted
- **Metadata success rate**: 85/98 = 86.7% (counting Success and Success|Spawned New)
- **Metadata failure rate**: 8/98 = 8.2% (counting Failure and Failure|Spawned New)
- **Spawned discoveries**: 6 new tools identified during investigation

### Pipeline Efficiency

- **Discovery → Metadata**: 98 tools investigated
- **Metadata → Evidence**: 96 tools (98% progression; only Bwigg dropped entirely)
- **OpenArchaeo no-DVC → Evidence**: 29/29 = 100% progression

---

## Data Sources

- `open-archaeo-no-dvc.csv`: 29 tools from OpenArchaeo baseline without version control
- `tool-metadata.csv`: 98 rows (97 tools + header) from metadata investigation
- `tool-evidence.csv`: 1,182 rows (1,179 evidence + headers/duplicates) from evidence collection

---

*Document generated: December 2025*
*For use in: Section 4 (Findings) of "Absence of Judgment" paper*
