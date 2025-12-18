# Verification Status Legend

This document describes the status codes used in `tool-discovery-granular.csv` to track the outcome of **each individual discovery event**.

Each row in the granular CSV represents one tool discovered by one LLM run. The same tool name may appear multiple times with different statuses if different runs produced different outcomes.

## Columns

The granular CSV includes two assessment columns:

1. **Verification_Status** - Was the discovered tool real and correctly attributed?
2. **Extraction_Completeness** - Did the discovery produce actionable source information?

---

## Extraction Completeness Codes

Assesses whether each discovery event produced sufficient information to locate and cite the source.

| Code | Description | Criteria |
|------|-------------|----------|
| `COMPLETE` | Full source reference | Tool name + article title + authors + URL/DOI + issue/journal |
| `PARTIAL` | Some source info but gaps | Missing one critical field (typically authors or URL) |
| `MINIMAL` | Insufficient to locate source | Tool name only, no article reference |

### Completeness Summary (2025-12-14)

| Status | Count | % | Notes |
|--------|-------|---|-------|
| COMPLETE | 299 | 85.4% | Actionable source references |
| PARTIAL | 46 | 13.1% | JOSS-worthless-o3 (29) + FullDetail sample (17) |
| MINIMAL | 5 | 1.4% | FullDetail sample run only |

**JOSS-worthless-o3**: All 29 entries have NaN authors (extraction failed to capture author metadata) but otherwise complete references.

**FullDetail sample run**: Early exploratory run that didn't produce structured article-level data.

---

## Tool Definition (Reference Standard)

Verification status is judged against the tool definition from the discovery prompt (`prompts-library-tools/01-tool-discovery.tex`):

> For our project, a software tool is any discrete piece of software—be it a program, script, or web application—that is **developed or substantially modified by researchers** to perform specific, **research-oriented computational tasks**. These tasks must involve **active data processing**, such as analysis, simulation, visualization, modeling, or automation, where input data is dynamically created, documented, transformed, or interpreted to generate meaningful results. In contrast, products whose primary function is to simply display, store, or promote static datasets—without offering mechanisms for active computational engagement—are excluded.
>
> A valid software tool for our purposes is one that not only **supports research in archaeology or historical sciences** but does so by actively collecting and/or processing data rather than merely serving as a generic data repository or static interface.

---

## Inclusion Criteria Decisions (Dec 2024)

During manual verification, several boundary cases required explicit decisions. These decisions refine the tool definition above for edge cases.

### Core Principle

**Research vs generic is the deciding factor, not commercial vs non-commercial.**

The tool definition emphasises software "developed or substantially modified by researchers" for "research-oriented computational tasks." Commercial software can meet this criterion if it has been **repurposed for research workflows** where researchers are actively using it for data processing in their domain.

### Specific Decisions

| Category | Decision | Rationale | Examples |
|----------|----------|-----------|----------|
| Commercial software repurposed for research | **INCLUDE** | We want to compare longevity of commercial vs non-commercial tools in research contexts | Vistapro, Pioneer, Truespace (3D landscape/modelling) |
| SfM/photogrammetry software | **INCLUDE** | "Research enough" - actively processes data for archaeological reconstruction | Agisoft PhotoScan/Metashape, Photomodeller |
| 3D modelling for archaeological visualisation | **INCLUDE** | Research-specific application even if commercial origin | Truespace, Pioneer Pro |
| Generic GIS platforms | **EXCLUDE** | Platform, not research tool | QGIS, ArcGIS, Arc/Info |
| Research-specific plugins to generic platforms | **INCLUDE** | Developed by/for researchers for specific research tasks | (Evaluate case-by-case) |
| Generic image editing software | **EXCLUDE** | Not research-specific | Paint Shop Pro, Photoshop |
| Generic surveying software | **EXCLUDE** | Not research-specific | Land Survey System |
| Format conversion utilities in research workflow | **INCLUDE** | Supporting research data processing pipeline | Wcvt2Pov (3D format converter) |
| Standards/formats | **EXCLUDE** | Specifications, not software tools | VRML |
| VRML authoring tools | **INCLUDE** | Software tools for creating 3D content | Fountain |

### Companion Programs and Plugins

Software companions, plugins, and extensions:
- May have different lifecycles than "main" software
- Should be tracked as separate discovery events
- Still valid discoveries if they meet the tool definition independently

### Secondary References

If a paper references another paper that mentions a tool, this is still a valid discovery event. This level of sensitivity is appropriate for the discovery phase - we are capturing *evidence of awareness* of tools in the literature, not just primary tool descriptions.

---

## Verification Status Codes

| Code | Description | Example |
|------|-------------|---------|
| `CONFIRMED` | Tool exists, mentioned in source, meets tool definition | OxCal, York System, MODES |
| `UNCLEAR` | Insufficient detail to verify | Bwigg in FullDetail sample |
| `MISATTRIBUTED` | Real tool mentioned but **does not meet tool definition** | Internet Explorer 3, VRML, Twitter API |
| `CONFABULATED` | Fabrication - tool does not exist OR tool exists but presence in source was fabricated | PyCoCu, Bwigg (Perplexity), Sketchfab (source hallucination) |
| (empty) | Not yet verified | Pending verification |

**Note:** DISCOVERY_ERROR (tool not found in claimed source) was merged into CONFABULATED to avoid singleton categories. These "source hallucinations" are distinguished by evidence notes explaining that the tool exists but its presence in the cited article was fabricated.

### MISATTRIBUTED Subcategories

Tools marked MISATTRIBUTED fail the tool definition for one of these reasons:

| Subcategory | Description | Examples |
|-------------|-------------|----------|
| General-purpose software | Not developed by/for researchers | Internet Explorer 3, Jupyter Notebook |
| Hardware/platform | Not software | Microsoft HoloLens |
| Standard/format | Specification, not software tool | VRML |
| General API/service | Not research-specific | Twitter API |
| Citizen science platform | Generic platform, not research tool | (removed - see note below) |

**Note:** Zooniverse Project Builder was initially MISATTRIBUTED but corrected to CONFIRMED after cross-referencing with successful metadata evaluation (2025-12-18).

---

## Verification Summary

As of 2025-12-18 (all 350 events fully verified with evidence notes, updated after metadata cross-reference, manual review, and category merge):

| Status | Count | % | Description |
|--------|-------|---|-------------|
| CONFIRMED | 230 | 65.7% | Genuine research tools meeting definition |
| MISATTRIBUTED | 70 | 20.0% | Real tools but don't meet definition |
| CONFABULATED | 50 | 14.3% | Fabrications (tool or source) |
| UNCLEAR | 0 | 0.0% | Minimal extraction, cannot verify |

### Outcome Summary

| Category | Count | % |
|----------|-------|---|
| **Successes** (CONFIRMED) | 230 | 65.7% |
| **Failures** (MISATTRIBUTED + CONFABULATED) | 120 | 34.3% |
| **Uncertain** (UNCLEAR) | 0 | 0.0% |

### Metadata Cross-Reference Corrections (2025-12-18)

14 entries were corrected from MISATTRIBUTED to CONFIRMED after cross-referencing with successful metadata evaluations in `02-tool-metadata.xlsx`:

- Gephi (5 occurrences: lines 8, 18, 113, 159, 336)
- Polynomial Texture Mapping (2 occurrences: lines 16, 111)
- MicroStation (line 53)
- TensorFlow (line 131)
- ade4 (line 328)
- SpadeR (line 329)
- vegan (line 330)
- WaveSurfer 1.8.8 → matched to WaveSurfer (line 130)
- Land Survey System → matched to LSS (line 42)

## Source Hallucination Cases

These cases involve real tools where the LLM fabricated their presence in a specific source article. Now merged into CONFABULATED category.

### Sketchfab (Line 109)

- **LLM**: ChatGPT Deep Research
- **Run**: IA-run2-success
- **Claimed source**: "Visualising the Guild Chapel" (Giles et al., IA issue 32)
- **Verification**: Article uses Unity WebGL Player (Figure 16, /guild-chapel/index.html), NOT Sketchfab
- **Notes**: Sketchfab is a real 3D model sharing platform, but its presence in this article was hallucinated

### Historical Cases (Later Corrected to CONFIRMED)

These were initially flagged as source errors but later verified as present in the articles:

- **Grid Machine 6.53**: Found in §3 of Boldrini article - "Extension Grid Machine Version 6.53 was used to convert each of the ADIs into a points theme"
- **pnuts**: Found in IA issue 2 editorial - described as "Previous, Next, Up, Top and Search" navigation script by John Frank

## Confabulation Verification Protocol

When investigating suspected confabulations, **always check all of the following sources** before classifying a tool as CONFABULATED:

1. **Links in LLM output** - Check any URLs/DOIs provided in the discovery output
2. **GitHub** - Search `github.com` for exact tool name and variations
3. **GitLab** - Search `gitlab.com` for exact tool name and variations
4. **CRAN** - For R packages, check `cran.r-project.org/package=`
5. **PyPI** - For Python packages, check `pypi.org/project/`
6. **General web search** - Search for tool name + domain context (e.g., "archaeology", "R package")

### Common Confabulation Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| DOI hijacking | Real DOI attached to fabricated tool name | archr → DOI belongs to PynPoint (astrophysics) |
| Domain confusion | Real tool exists in different domain | ArchABM exists for air quality, not archaeology |
| Near-miss | Similar name to real tool | ChronoModelr vs real RChronoModel |
| Method-to-tool | Method name converted to fabricated tool | aoristic method → "time2aoristic" tool |
| Name fabrication | Concept exists, tool name invented | "Advanced viewshed analysis" vs Visibility Analysis |
| Complete fabrication | Everything fabricated | JOAD-extreme fail tools with fake DOIs |

### Recording Evidence Notes

For CONFABULATED entries, the evidence note should document:
- Which sources were checked (GitHub, CRAN, PyPI, web search)
- Whether similar/related real tools were found (near-miss pattern)
- The specific confabulation pattern identified
- Any domain confusion cases (tool exists but for different purpose)

---

## Confabulation Details

### Confabulation Sources by Run

| Run | Count | Type |
|-----|-------|------|
| JOAD-extreme fail | 15 | Wholesale fabrications with fake DOIs |
| JOSS-worthless-o3 + Joss-fail-possible | 28 | Same 14 tools found by both runs |
| SoftwareX-run1-accessFail | 3 | DOI hijacking (ringR, Hyperspectral, SimLex) |
| JOSS-secondpass | 1 | PyCoCu |
| Perplexity-SyntheticPrompt-DR | 1 | Bwigg (fabricated Broad Institute tool) |

### JOAD Fabrications (15 tools)

All from the "extreme fail" JOAD run - wholesale fabrications with plausible names combining archaeological terms with technology buzzwords:

3DArq, ArtifactML, BigArq, CeramicNet, DataArq, DataMiner, DeepClass, FieldStream, GeoViz, ImageQuant, LandML, MapCrowd, Reconstructo, VRArchaeo, time2aoristic

### JOSS Confabulations (14 tools, 28 events)

All 14 confabulated tools were "discovered" by **both** the JOSS-worthless-o3 (o3) and Joss-fail-possible (ChatGPT DR) runs:

ArchABM, archCandy, archr, argus, ChronCluster, ChronoModelr, chora, FQC, OpenEthnology, pastR, pyArchaeo, RACER, RChrono, rhip

#### Key Examples (DOI Hijacking Pattern)

**archr**
- **Claimed**: "Automated Radiocarbon Chronology for R" with DOI 10.21105/joss.00840
- **Reality**: Fabricated name + **DOI hijacking**
- **Actual DOI owner**: [PynPoint](https://joss.theoj.org/papers/10.21105/joss.00840) - exoplanet imaging (astrophysics)

**ArchABM**
- **Claimed**: "Agent-based modeling of ancient societies in R" with DOI 10.21105/joss.01201
- **Reality**: Multi-layered confabulation + **DOI hijacking**
- **Actual DOI owner**: [TraitDB](https://joss.theoj.org/papers/10.21105/joss.01201) - phenotypic trait database
- **Notes**: A real "ArchABM" Python package exists but for architecture/COVID modelling, not archaeology

**ChronoModelr**
- **Claimed**: "A wrapper for ChronoModel" with DOI 10.21105/joss.01095
- **Reality**: Near-match confabulation + **DOI hijacking**
- **Actual DOI owner**: [pyam](https://joss.theoj.org/papers/10.21105/joss.01095) - climate/energy model analysis
- **Real tool**: [RChronoModel](https://cran.r-project.org/package=RChronoModel) (note different name) - real CRAN package for ChronoModel post-processing

### DOI Hijacking Pattern

Both o3 and ChatGPT DR exhibited the same confabulation pattern:
1. Traversed JOSS DOI sequences (10.21105/joss.00840, .01095, .01201, etc.)
2. Fabricated plausible archaeological tool names
3. Attached fabricated names to real DOIs from unrelated papers

This explains why multiple models "found" the same 14 tools - they're both traversing the same DOI sequence and confabulating archaeological contexts. **This is not true cross-validation.**

### SoftwareX Confabulations (3 tools)

From the SoftwareX-run1-accessFail run - DOI hijacking with fabricated heritage/archaeology tools attached to real SoftwareX DOIs:

**ringR**
- **Claimed**: "R package for analyzing and modeling tree-ring growth" with DOI 10.1016/j.softx.2019.100325
- **Verification**: No R package "ringR" exists. The main dendrochronology package is [dplR](https://cran.r-project.org/package=dplR)
- **DOI status**: Unverified (may be hijacked or may be a plausible-looking fabricated DOI)

**Hyperspectral Image Analysis Toolbox**
- **Claimed**: "Cultural Heritage Applications" tool by Carcagnì et al. with DOI 10.1016/j.softx.2020.100610
- **Reality**: DOI hijacking
- **Actual DOI owner**: [XDrift](https://www.sciencedirect.com/science/article/pii/S235271102030323X) - pesticide spray-drift R package by Bub et al.

**SimLex**
- **Claimed**: "Computational model for simulating lexical change" by Dellert & Jäger with DOI 10.1016/j.softx.2017.06.001
- **Reality**: DOI hijacking
- **Actual DOI owner**: [FLBEIA](https://www.sciencedirect.com/science/article/pii/S2352711017300171) - fisheries bio-economic modelling
- **Notes**: Dellert & Jäger did create NorthEuraLex (lexical database), but not "SimLex" software. SimLex-999 is a separate word similarity dataset by Hill et al.

### PyCoCu

- **LLM**: ChatGPT Deep Research
- **Run**: JOSS-secondpass
- **Verification**: No evidence this tool exists
- **Metadata run result**: "Does not appear to exist as a standalone software package"

### Bwigg (Perplexity run)

- **LLM**: Perplexity
- **Run**: Perplexity-SyntheticPrompt-DR
- **Claimed tool**: "Bwigg" - Broad Institute genomics tool
- **Reality**: Complete fabrication. The real Bwigg is Christen 2003 Bayesian wiggle-matching software, which the IA-run2 correctly identified.

## Misattribution Details

### FaceNet

- **LLM**: ChatGPT Deep Research
- **Run**: JOSS-secondpass
- **Reality**: Google's face recognition neural network
- **Issue**: Mentioned as citation, not as archaeological tool
- **Notes**: Name collision with prominent unrelated software

## Bwigg Case Study: Same Name, Different Outcomes

This case illustrates why per-event tracking matters. Three runs discovered "Bwigg" but with completely different outcomes:

| Run | LLM | Status | What was found |
|-----|-----|--------|----------------|
| IA-run2-success | ChatGPT DR | CONFIRMED | Real Bwigg (Christen 2003 Bayesian wiggle-matching) |
| FullDetail Sample | ChatGPT DR | UNCLEAR | Vague description, cannot verify |
| Perplexity-SyntheticPrompt | Perplexity | CONFABULATED | Fabricated Broad Institute genomics tool |

Cross-validation counts in `tool-discovery-summary.csv` can be misleading when different runs confabulate different tools with the same name.

---

## JOSS Run Overlap Analysis

Two separate JOSS discovery runs produced overlapping results:

| Run | Model | Tools Found | Status |
|-----|-------|-------------|--------|
| JOSS-worthless-o3 | OpenAI o3 | 29 | "Worthless" - NaN authors, incomplete data |
| Joss-fail-possible | ChatGPT DR | 34 | "Fail-possible" - uncertain status |

**Overlap**: 29 tools appear in both runs (the o3 run is a subset).

### Key Findings

1. **Both runs found the same confabulations**: archr, ArchABM, ChronoModelr appear in both runs, indicating these are systematic LLM confabulations rather than random hallucinations.

2. **The o3 run extracted URLs but had NaN metadata**: Despite being labeled "worthless", the o3 run captured DOI URLs (e.g., `https://joss.theoj.org/papers/10.21105/joss.00840`).

3. **The DR run extracted article titles but lacked URLs**: The "fail-possible" run captured article descriptions but marked URLs as "TODO".

4. **Different extraction quality, same underlying reality**: When the same tool is discovered by both runs, one run's extraction may have better URL data while the other has better descriptive metadata.

### Implications for Verification

Both JOSS runs have been fully verified:
- **JOSS-worthless-o3**: 14 CONFIRMED, 14 CONFABULATED, 1 MISATTRIBUTED (29 total)
- **Joss-fail-possible**: 18 CONFIRMED, 14 CONFABULATED, 2 MISATTRIBUTED (34 total)

The "worthless" designation refers to **extraction completeness** (NaN authors, incomplete metadata), not verification status. A run can have poor extraction quality but still discover real tools.

This illustrates why per-event tracking matters: extraction completeness and verification status are independent assessments.
