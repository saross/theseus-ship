# Key Quantitative Findings: Complete Accounting

**Purpose**: Systematically account for every tool at every stage of the research pipeline, ensuring numbers reconcile across discovery → metadata → evidence phases.

**Created**: 2025-12-14
**Last Updated**: 2025-12-14 (JOSS runs fully verified, confabulation counts updated)
**Status**: Complete

---

## Pipeline Overview

```text
Raw Discovery → Filtered → Metadata → Evidence
     244      →    92    →    98    →   125
```

**Key insight**: The "92 tools filtered" represents tools selected through human curation from 244 raw discoveries. The 98 metadata tools includes 6 "spawned" tools discovered during investigation.

---

## 1. Tool Discovery Phase

### 1.1 Sources and Runs (from `01a-tool-discovery.xlsx`)

| Sheet Name | Articles | Tools With Mentions | Unique Tools | Model | Outcome |
|------------|----------|---------------------|--------------|-------|---------|
| IA-run2-success | 674 | 97 | 131 | ChatGPT DR | Success |
| JOSS-secondpass | 16 | 16 | 48 | ChatGPT DR | Success |
| JOAD-extreme fail | 40 | ~13 valid + 15 fabricated | 28 | ChatGPT DR | Extreme fail |
| JCAA-o3 | 45 | 45 | 19 | o3 | Mixed (generics) |
| JOSS-worthless-o3 | 29 | 29 | 29 | o3 | Unusable (all NaN authors) |
| IA-31-67 fail | 200 | 18 | 18 | ChatGPT DR | Failed (underextraction) |
| SoftwareX-run1 | 12 | 12 | ~10 | ChatGPT DR | Access failure |
| Perplexity-SyntheticPrompt | 9 | 9 | 9 | Perplexity | Sample/test |

### 1.2 Raw Discovery Summary (from `tool-discovery-summary.csv`)

- **Total unique standardised tools**: 244

**Hallucination Risk Distribution**:
| Risk Level | Count | Notes |
|------------|-------|-------|
| LOW | 158 | Verified or plausible |
| LOW (cross-validated) | 40 | Found by multiple services |
| MEDIUM | 31 | Requires verification |
| HIGH | 15 | Confirmed fabrications (all JOAD) |

**Run Quality Distribution** (tools can appear in multiple runs):
| Quality | Count | Notes |
|---------|-------|-------|
| success | 130 | Verified real tools |
| success-secondpass | 44 | Verified after re-run |
| fail-possible | 34 | Uncertain status |
| worthless | 29 | o3 JOSS run |
| standard | 19 | Operator runs |
| fail | 19 | Failed extraction |
| extreme fail | 15 | JOAD fabrications |
| access-fail | 13 | SoftwareX run processing failure |
| sample | 10 | Test runs |
| synthetic-prompt | 9 | Perplexity test |

### 1.3 Fabricated Tools (15 HIGH risk - all from JOAD)

1. 3DArq
2. ArtifactML
3. BigArq
4. CeramicNet
5. DataArq
6. DataMiner
7. DeepClass
8. FieldStream
9. GeoViz
10. ImageQuant
11. LandML
12. MapCrowd
13. Reconstructo
14. VRArchaeo
15. time2aoristic

### 1.4 Discovery → Metadata Filtering (Detailed Analysis)

**244 raw discoveries → 92 selected for metadata investigation**

The filtering was **human curation**, not mechanical exclusion. Discoveries were reviewed and rationalised into a focused investigation set.

#### Part A: Rationalisations (Consolidations)

Some metadata tools consolidated multiple discovery entries:

| Metadata Tool | Discovery Entries Consolidated |
|---------------|-------------------------------|
| ArchAIDE | ArchAIDE, ArchAIDE desktop application, ArchAIDE mobile application |
| FAIMS | FAIMS, FAIMS Mobile |
| FieldWorker | FieldWorker Advanced 2.3.5, FieldWorker Pro 0.91 |
| DepthmapX | Depthmap, DepthmapX |
| ArchaeoPhases | ArchaeoPhases, ArchaeoPhases (Archeofrag...) |
| bleiglas | bleiglas, Voro++ (bleiglas...) |
| kdedemo | kdedemo1, kdedemo2 |
| stratigraphr | Stratigraph, stratigraphr |
| KLRfome | KLRfome, KLRfome – Kernel Logistic Regression... |
| ArcGIS skeletal templates | ArcGIS, ArcGIS skeletal templates |
| Rhino for AutoCAD | AutoCAD, Rhino for AutoCAD |

**Result**: 11 metadata tools consolidated 22 discovery entries (saving 11 duplicate investigations).

#### Part B: Problems Causing Exclusion

| Problem Category | Count | Description |
|-----------------|-------|-------------|
| **Fabrications** | 15 | JOAD extreme fail run - confirmed hallucinations |
| **Generic Tech** | 43 | Not archaeology-specific (ArcGIS variants, Excel, R, MATLAB, etc.) |
| **Databases/Platforms** | 27 | Infrastructure not tools (Open Context, tDAR, national systems) |
| **Worthless Run** | 20 | o3 JOSS run produced NaN/incomplete data - unverified R packages |
| **Run Processing Failure** | 13 | SoftwareX run failed to extract complete data |
| **Version Variants** | 4 | Consolidated into base tool |
| **Techniques/Standards** | 2 | Not software (RTI, data profiles) |
| **Deprioritised** | ~22 | Legitimate tools not selected for investigation |

#### Category Details

**Fabrications (15)** - All from JOAD "extreme fail" run:
- Confirmed wholesale hallucinations with fabricated names, article titles, and DOIs
- Listed in Section 3.1

**Generic Technologies (43)**:
- ESRI products: ArcGIS 10.5, ArcMap, ArcView, Arc/Info, ArcScene, Spatial Analyst
- Office/Stats: Excel, Microsoft Access, PowerPoint, MATLAB, Minitab
- Creative: Adobe Illustrator, Blender, Paint Shop Pro
- ML/Dev: TensorFlow, Keras, Jupyter, GitHub, Stable Diffusion
- Other: GRASS GIS, QGIS, GNU R, Unity 3D

**Databases/Platforms (27)**:
- National systems: ARCHIS, Askeladden, SIGEC
- Repositories: Open Context, tDAR, Archaeology Data Service
- Portals: HEIRPORT, AMCR-PAS, DB-HERITAGE, Heurist

**JOSS-worthless-o3 Run (29)** - now fully verified:

Despite having NaN authors and incomplete metadata (an **extraction completeness** issue), the 29 tools from this run have been manually verified:

| Status | Count | Examples |
|--------|-------|----------|
| CONFIRMED | 14 | tidypaleo, aRchaic, mapDamage, mortAAR, pyrho |
| CONFABULATED | 14 | archr, ArchABM, ChronoModelr, pastR, pyArchaeo |
| MISATTRIBUTED | 1 | MicroPasts (crowdsourcing platform, not research tool) |

**Key insight**: The "worthless" designation refers to extraction quality, not tool validity. Half were real tools.

**Run Processing Failure (13)** - SoftwareX run:

The SoftwareX run failed during LLM extraction. **Important**: SoftwareX is an open-access journal, so access/paywall was not the issue. The extraction partially succeeded but produced incomplete or corrupted data.

**Evidence of partial extraction** (from `01a-tool-discovery.xlsx`):

| Article | Tool Extracted | Issue |
|---------|----------------|-------|
| CAinterprTools: An R package... | CAinterprTools | ✓ Clean |
| tgcd: An R package... | tgcd | ✓ Clean |
| FAIMS Mobile... | FAIMS Mobile | ✓ Clean |
| MICA: Multiple interval-based... | MICA | ✓ Clean |
| CulSim: A simulator... | CulSim | ✓ Clean |
| movecost: An R package... | movecost | ✓ Clean |
| Cloud2FEM... | Cloud2FEM | HTML artifacts in data |
| Image2DEM... | Image2DEM | HTML artifacts in data |
| ArchaeoViz... | ArchaeoViz | ✓ Clean |
| Hyperspectral Image Analysis... | Toolbox | ✓ Clean |
| ringR... | ringR | ✓ Clean |
| SimLex... | SimLex | ✓ Clean |

**Observed problems**:
- Strange HTML artifacts in some entries (e.g., `&#8203;:contentReference[oaicite:4]{index=4}`)
- Possible missing author/metadata fields required by extraction schema
- Run may have terminated early before complete processing

**Result**: 13 tools from this run were excluded due to uncertainty about data completeness, despite the articles themselves being accessible

**Deprioritised (~22)**:
- PixPlot, ExeGesIS, SAGAscape, Pioneer, SORAN, geoChronR, etc.
- Legitimate tools that weren't prioritised for metadata investigation

#### Key Insights

1. **Human curation**: The filtering represented deliberate selection based on relevance and scope
2. **Consolidation saved effort**: 11 metadata tools covered 22 discovery entries through name rationalisation
3. **Run failures created gaps**: 33 tools (worthless + SoftwareX) couldn't be verified due to extraction problems
4. **Hallucinations isolated**: All 15 fabrications came from one catastrophic JOAD run

---

## 2. Metadata Collection Phase

### 2.1 Tools Entering Metadata Phase

- **From discovery (filtered)**: 92 tools
- **Spawned during investigation**: 6 tools
  - ArchaeoGRID (from Grid Machine confab)
  - LogicistWriter (from MASA Consortium)
  - OpenArchaeo (from MASA Consortium)
  - OpenGuide (from MASA Consortium)
  - Rhinoceros 3D (from Rhino for AutoCAD)
  - POV-Ray (from Wcvt2Pov)
- **Total investigated**: 98 tools

### 2.2 Metadata Outcomes (from `02-tool-metadata.xlsx`, updated)

| Outcome Category | Count | Notes |
|------------------|-------|-------|
| Success | 82 | Complete metadata collected (includes FAIMS) |
| Success \| Spawned new | 2 | MASA Consortium, Rhino for AutoCAD |
| New (spawned) | 6 | Spawned tools that succeeded |
| Failure | 6 | Could not collect metadata |
| Failure \| Spawned new | 2 | Grid Machine, Wcvt2Pov |
| **Total** | **98** | |

**Calculated outcomes**:
- **Successful metadata**: 82 + 2 + 6 = **90** (92%)
- **Failed metadata**: 6 + 2 = **8**

### 2.3 Metadata Failures - Complete Attribution

All 8 metadata failures came from **successful discovery runs with LOW hallucination risk**. These are real tool names that couldn't be documented, not fabrications. The failures illustrate the boundary between what LLMs can find (popular, well-documented tools) versus what requires human expertise (obscure utilities, name-collision victims, pre-web-era software).

| Tool | Failure Type | Discovery Source | Run Quality | Root Cause |
|------|--------------|------------------|-------------|------------|
| FaceNet | Name collision | JOSS | success-secondpass | Name matched Google's neural network, not archaeological tool |
| Fountain (VRML tool) | Name collision | Internet Archaeology | success | Generic name matched multiple unrelated software |
| Microware | Name collision | Internet Archaeology | success | Generic term for dental microwear analysis software |
| pnuts | Name collision | Internet Archaeology | success | Matched Yahoo's distributed database platform |
| Bwigg | Minimal footprint | Multiple | cross-validated | Real tool (Christen 2003) predates web documentation conventions |
| Wcvt2Pov | Insufficient docs | Internet Archaeology | success | Minimal info available; spawned POV-Ray investigation |
| PyCoCu | No online presence | JOSS | success-secondpass | Site-specific Python script (Sécher et al. 2020) |
| Grid Machine | Confabulation → productive | Internet Archaeology | success | Led to ArchaeoGRID discovery |

#### Failure Type 1: Name Collision (4 tools)

These tool names exist in the archaeological literature but are obscured by more prominent software with the same name:

| Tool | What Claude Found Instead | Archaeological Context |
|------|---------------------------|------------------------|
| **FaceNet** | Google's neural network for face recognition | Mentioned in JOSS archaeological article, but search results overwhelmed by Google's 2015 facial recognition tool |
| **Fountain (VRML tool)** | Screenplay markup language | Claude asked for disambiguation—couldn't identify archaeology-specific version |
| **Microware** | OS-9 operating system by Microware Systems Corporation (1977-2001) | Possibly a generic reference to "microware analysis" software for dental microwear studies |
| **pnuts** | Yahoo's distributed database (PNUTS) or Java scripting language (Pnuts) | Real archaeological tool likely obscured by more prominent namesakes |

#### Failure Type 2: Minimal/No Documentation (3 tools)

These are real tools that lack sufficient online presence for LLM-based research:

| Tool | Claude's Verdict | Actual Status |
|------|------------------|---------------|
| **Bwigg** | "No evidence that 'Bwigg' exists as an archaeological research software tool" | Real tool from Christen 2003, but predates modern web documentation conventions—too obscure for LLM to find |
| **PyCoCu** | "Does not appear to exist" | Site-specific Python script (Sécher et al. 2020)—not distributed as standalone software |
| **Wcvt2Pov** | "No evidence found" in POV-Ray ecosystem | Very obscure utility for converting to POV-Ray format; investigation spawned POV-Ray as a successful metadata entry |

#### Failure Type 3: Productive Confabulation (1 tool)

| Tool | What Happened | Outcome |
|------|---------------|---------|
| **Grid Machine** | Claude couldn't find it, but mentioned "ArchaeoGRID" during search process | User followed up → Claude researched ArchaeoGRID → **spawned a successful metadata entry** for a real tool (University of Florence/UAB, 2004-2015) |

**Key insight**: None of the metadata failures were due to fabricated discoveries. All 8 were real mentions in real articles that couldn't be resolved to documentable tools. The Grid Machine failure was "productive"—it led to discovering a real related tool.

---

## 3. Hallucination Accounting

### 3.1 Confirmed Hallucinations (15 from JOAD)

All 15 HIGH-risk fabrications came from the JOAD "extreme fail" run. Each includes fabricated tool names, fake article titles, and plausible-looking DOIs:

| Tool | Claimed Type | Fabricated Article Title |
|------|--------------|--------------------------|
| 3DArq | 3D modelling tool | "Advancements in 3D Modelling for Archaeological Artifacts" |
| ArtifactML | R package | "Automated Artifact Classification Using Machine Learning" |
| BigArq | R script | "Leveraging Big Data in Archaeological Research" |
| CeramicNet | Python script | "Open Source Analysis of Ceramic Trade Networks" |
| DataArq | software tool | "An Open Platform for Archaeological Data Integration" |
| DataMiner | Python tool | "Leveraging Big Data in Archaeological Research" |
| DeepClass | Python tool | "Automated Artifact Classification Using Machine Learning" |
| FieldStream | data processing | "Enhancing Archaeological Fieldwork with Real-time Data Processing" |
| GeoViz | web application | "Geoarchaeological Data from the Mediterranean" |
| ImageQuant | software | "Digital Imaging Techniques in Artifact Analysis" |
| LandML | GIS plugin | "Integrating GIS and Machine Learning for Landscape Archaeology" |
| MapCrowd | mobile app | "Crowdsourcing Archaeological Site Mapping Using Mobile Apps" |
| Reconstructo | web application | "Digital Reconstruction of Ancient Settlements" |
| VRArchaeo | Unity-based | "Virtual Reality in Archaeology: Case Studies" |
| time2aoristic | R script | "Spatio-Temporal Distributions of Middle to Late Jomon Pithouses" |

**Pattern observed**: All fabrications followed a template of plausible tool names combining archaeological terms with technology buzzwords (ML, Net, VR, etc.).

### 3.2 JOSS Confabulations (14 tools, 28 events)

All 14 JOSS confabulations were "discovered" by both JOSS-worthless-o3 (o3) and Joss-fail-possible (ChatGPT DR) runs:

ArchABM, archCandy, archr, argus, ChronCluster, ChronoModelr, chora, FQC, OpenEthnology, pastR, pyArchaeo, RACER, RChrono, rhip

#### DOI Hijacking Pattern

Both o3 and ChatGPT Deep Research exhibited a systematic confabulation pattern:

1. **DOI sequence traversal**: Models walked through JOSS DOI sequences (10.21105/joss.00840, .01095, .01201, etc.)
2. **Archaeological name fabrication**: Generated plausible R package names combining "arch-" prefixes with common suffixes (-r, -ABM, -Chrono)
3. **False attribution**: Attached fabricated tool names to real DOIs from unrelated papers

**Verified DOI hijacking examples**:

| Confabulated Tool | Claimed DOI | Actual Paper at DOI |
|-------------------|-------------|---------------------|
| archr | 10.21105/joss.00840 | [PynPoint](https://joss.theoj.org/papers/10.21105/joss.00840) - exoplanet imaging |
| ArchABM | 10.21105/joss.01201 | [TraitDB](https://joss.theoj.org/papers/10.21105/joss.01201) - phenotypic trait database |
| ChronoModelr | 10.21105/joss.01095 | [pyam](https://joss.theoj.org/papers/10.21105/joss.01095) - climate/energy analysis |

**Critical insight**: The fact that **both models confabulated the same 14 tools** is not cross-validation—it demonstrates shared failure modes. Both models likely:

- Learned the JOSS DOI structure from training data
- Associated "arch-" naming patterns with archaeology
- Failed to verify that DOIs actually correspond to the claimed tools

This pattern explains why "cross-validation" (multiple LLMs finding the same tool) can be misleading for fabrication detection.

### 3.3 Discovery Errors

| Tool | Type | Notes |
|------|------|-------|
| Grid Machine | Discovery error → productive | Not confabulation; led to ArchaeoGRID discovery |
| Microware | Technique misread | Article discusses "microwear", not "Microware" software |
| pnuts | Template artifact | Extracted from HTML comments, not article content |

### 3.4 Hallucination vs Metadata Failure

**Critical distinction**:

- The 15 JOAD hallucinations were never investigated for metadata (excluded at discovery)
- The 8 metadata failures were real discoveries that couldn't be documented (see Section 2.3 for detailed breakdown)

---

## 4. OpenArchaeo Baseline Comparison

### 4.1 Baseline Composition (from `01b-tool-openarchaeo-work.xlsx`)

- **OpenArchaeo total**: 374 tools
- **With DVCS repository**: 345 tools (92%)
- **Without DVCS repository**: 29 tools (8%)

The 29 no-DVC tools were selected for evidence collection alongside discovery pathway tools.

### 4.2 Overlap Analysis

From `combined-tool-list` sheet (445 rows analysed):

- **Exact matches**: 19 tools
- **Fuzzy matches**: 8 (low: 6, medium: 1, high: 1)
- **Human-validated overlap**: ~20 tools after manual review

**Result**:
- **Discovery ∩ OpenArchaeo**: 20 tools
- **Unique to discovery**: 71 tools (91 - 20)
- **Unique to OpenArchaeo**: 354 tools (374 - 20)

---

## 5. Evidence Collection Phase

### 5.1 Final Evidence Counts (from `03-tool-evidence.xlsx`)

| Pathway | Unique Tools | Evidence Rows | Notes |
|---------|--------------|---------------|-------|
| Discovery pathway | 96 | 965 | Tools from journal scanning |
| OpenArchaeo (no DVC) | 29 | 214 | Tools without repositories |
| **Total** | **125** | **1,179** | No overlap between pathways |

Note: 2 rows have missing data (NaN values), so actual valid rows = 1,179.

### 5.2 Evidence Collection Attribution

| Contributor | Total Rows | Discovery | OpenArchaeo |
|-------------|------------|-----------|-------------|
| BBS (Brian) | 849 (72%) | 804 | 45 |
| SAR (Shawn) | 330 (28%) | 161 | 169 |

### 5.3 Metadata → Evidence Reconciliation

**Question**: Why do 89 successful metadata tools become 96 discovery pathway evidence tools?

**Analysis** (comparing `02-tool-metadata.xlsx` to `03-tool-evidence.xlsx`):

- Tools in both: 58
- Only in metadata (not in evidence): 33
- Only in evidence (not in metadata): 38

**Key finding**: The discrepancy is primarily due to **naming inconsistencies**, not missing tools:

| Metadata Name | Evidence Name |
|---------------|---------------|
| Agisoft PhotoScan/Metashape | Agisoft PhotoScan |
| bleiglas | Bleiglas |
| ArcheoFrag | Archeofrag |
| Endovélico | Endovélico Information System |
| FieldWorker | FieldWorker Advanced, FieldWorker Pro |
| Perseus Digital Library | Perseus 2.0 |

**Also notable**: Metadata failures (FaceNet, Fountain (VRML tool), Microware, pnuts, Grid Machine, Wcvt2Pov, PyCoCu) appear in evidence because evidence was collected for all discovered tools, regardless of metadata success.

---

## 6. Complete Pipeline Reconciliation

### 6.1 Flow Diagram (Verified)

```text
RAW DISCOVERY (244 unique tools)
│
├── HUMAN CURATION
│   │
│   ├── Excluded (152 tools):
│   │   ├── Fabrications: 15 (JOAD extreme fail)
│   │   ├── Generic tech: 43 (ArcGIS, Excel, R, etc.)
│   │   ├── Databases/platforms: 27 (Open Context, tDAR, etc.)
│   │   ├── Worthless run: 20 (o3 JOSS extraction failure)
│   │   ├── Run processing failure: 13 (SoftwareX)
│   │   ├── Version variants: 4 (consolidated)
│   │   ├── Techniques/standards: 2 (not software)
│   │   └── Deprioritised: ~28 (legitimate but not selected)
│   │
│   └── Consolidated (11 metadata tools ← 22 discovery entries):
│       ArchAIDE ← 3, FAIMS ← 2, FieldWorker ← 2, etc.
│
└── SELECTED FOR METADATA: 92 tools

METADATA PHASE (98 tools)
├── From discovery: 92
├── Spawned during investigation: +6
│   ├── ArchaeoGRID (from Grid Machine confab)
│   ├── LogicistWriter (from MASA Consortium)
│   ├── OpenArchaeo (from MASA Consortium)
│   ├── OpenGuide (from MASA Consortium)
│   ├── Rhinoceros 3D (from Rhino for AutoCAD)
│   └── POV-Ray (from Wcvt2Pov)
│
├── Successful: 90 (92%)
│   ├── Success: 82 (includes FAIMS)
│   ├── Success|Spawned: 2
│   └── New (spawned): 6
│
└── Failed: 8
    ├── Name collision: 4 (FaceNet, Fountain (VRML tool), Microware, pnuts)
    ├── Minimal footprint: 1 (Bwigg)
    ├── Insufficient docs: 1 (Wcvt2Pov - spawned POV-Ray)
    ├── No online presence: 1 (PyCoCu)
    └── Productive confab: 1 (Grid Machine - spawned ArchaeoGRID)

EVIDENCE PHASE (125 tools, 1,179 rows)
├── Discovery pathway: 96 tools, 965 rows
│   ├── Includes metadata successes
│   ├── Includes metadata failures (still discovered)
│   └── Naming variants create apparent discrepancy
│
├── OpenArchaeo no-DVC: 29 tools, 214 rows
│   └── Separate pathway, no overlap with discovery
│
└── Contributors: BBS 849 rows (72%), SAR 330 rows (28%)
```

### 6.2 Resolved Questions

| Question | Resolution |
|----------|------------|
| How do 90 metadata become 96 discovery evidence? | Naming inconsistencies + metadata failures still collected |
| 6 spawned tools verified? | ✓ All 6 confirmed in metadata spreadsheet |
| JOAD hallucination count? | ✓ 15 confirmed (all HIGH risk) |
| Evidence row discrepancy? | ✓ 1,179 valid rows + 2 NaN = 1,181 total |
| SoftwareX "access fail"? | ✓ Run processing failure, not paywall (open access journal) |

### 6.3 Key Pipeline Insights

1. **Confabulation rate**: 31 unique fabricated tools across all runs:
   - JOAD: 15 (wholesale fabrications with fake DOIs)
   - JOSS runs: 14 (DOI hijacking pattern - same tools in both runs)
   - JOSS-secondpass: 1 (PyCoCu)
   - Perplexity: 1 (Bwigg fabrication)
2. **Metadata success rate**: 90/98 = 92% (8 failures, none due to fabrications)
3. **Curation yield**: 92 tools selected from 244 discoveries through human review
4. **Evidence coverage**: 125 tools with 1,179 evidence rows (avg 9.4 rows/tool)

---

## 7. Summary Statistics

| Metric | Value |
|--------|-------|
| Raw discoveries | 244 |
| After curation | 92 |
| After spawning | 98 |
| Successful metadata | 90 (92%) |
| Metadata failures | 8 |
| Unique fabrications | 31 (JOAD: 15, JOSS: 14, other: 2) |
| Consolidations | 11 (from 22 entries) |
| Evidence tools | 125 |
| Evidence rows | 1,179 |
| OpenArchaeo baseline | 374 |
| Discovery ∩ OpenArchaeo | 20 |

### Verification Status Summary (350 discovery events)

| Status | Count | % |
|--------|-------|---|
| CONFIRMED | 171 | 48.9% |
| MISATTRIBUTED | 98 | 28.0% |
| CONFABULATED | 45 | 12.9% |
| UNCLEAR | 33 | 9.4% |
| DISCOVERY_ERROR | 3 | 0.9% |

---

**Document status**: Complete (2025-12-14, updated with JOSS verification results)
