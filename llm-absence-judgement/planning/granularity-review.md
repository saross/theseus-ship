# Granularity Review: Tools That May Not Be Tools

**Created**: 2025-12-21

The metadata investigation phase identified several items that were extracted as "tools" during discovery but may not meet the definition of a software tool. This document is for user review to confirm classification.

---

## Classification Categories

- **GRANULARITY_ERROR**: Item is a project, infrastructure, or service—not a software tool
- **NOT_ARCHAEOLOGICAL**: Legitimate software but no evidence of archaeological use
- **BORDERLINE**: Partially meets criteria; requires judgement call
- **TOOL**: Confirms item is a legitimate software tool (no action needed)

---

## Items Requiring Review

### 1. VirtualArch

**Current status**: GRANULARITY_ERROR (already applied)

**Summary**: EU Interreg Central Europe project (2017-2020) that developed site-specific VR/AR applications for 8 archaeological sites. Received €2.1 million funding across 10 partner institutions.

**Why it may not be a tool**: "The project did not develop a unified software platform but instead created multiple applications using existing tools and technologies." No public code repositories, no standardised distribution, no provisions for reuse. Applications were deployed as on-site museum installations rather than distributable software.

**Metadata verdict**: "VirtualArch fails to meet essential criteria for research software classification."

- [x] GRANULARITY_ERROR (already confirmed)
- [ ] TOOL

**Notes**: _Already marked as granularity error in discovery files._

---

### 2. ARIADNE

**Current status**: CONFIRMED (in discovery files)

**Summary**: Advanced Research Infrastructure for Archaeological Dataset Networking in Europe. Unified portal providing integrated access to over 3.8 million archaeological resources from 40+ data providers.

**Why it may not be a tool**: "ARIADNE is not software that researchers install locally, but rather a comprehensive infrastructure with both a web portal for discovery and search, and specialized tools for data management and sharing."

**Metadata verdict**: Described as an infrastructure/portal, not a software tool.

- [ ] GRANULARITY_ERROR (infrastructure, not software)
- [ ] TOOL (the portal/infrastructure itself counts as a research tool)

**Notes**:

---

### 3. TrueSpace

**Current status**: CONFIRMED (in discovery files)

**Summary**: 3D modelling and animation software developed by Caligari Corporation (1994-2009), acquired and discontinued by Microsoft. Available as freeware with community support.

**Why it may not be a tool (for archaeology)**: "TrueSpace does not qualify as research software for archaeology despite its theoretical potential... No documented usage in archaeological contexts can be found in academic literature, archaeological publications, or community forums, indicating a complete lack of adoption within the research community."

**Metadata verdict**: Legitimate 3D software, but "entirely bypassed by the archaeological community."

- [ ] NOT_ARCHAEOLOGICAL (real software, but no archaeological adoption)
- [ ] TOOL (general-purpose tool that could be used in archaeology)

**Notes**:

---

### 4. LSS (Land Survey System)

**Current status**: CONFIRMED (in discovery files)

**Summary**: Digital terrain modelling (DTM) system by McCarthy Taylor Systems for survey data processing, used in civil engineering, mining, and other industries.

**Why it may not be a tool (for archaeology)**: "LSS does not qualify as archaeological research software because it lacks the essential criterion of methodological alignment with recognised archaeological research practices... no evidence was found of actual usage in archaeological research projects, suggesting the archaeological community has not adopted this tool."

**Metadata verdict**: Legitimate survey software, but no evidence of archaeological adoption.

- [ ] NOT_ARCHAEOLOGICAL (real software, but no archaeological adoption)
- [ ] TOOL (general-purpose tool mentioned in archaeological contexts)

**Notes**:

---

### 5. WallGIS

**Current status**: CONFIRMED (in discovery files)

**Summary**: Geodatabase and GIS for Hadrian's Wall developed through WallCAP project, distributed via Archaeology Data Service.

**Why it may not be a tool**: "Rather than functioning as standalone software, WallGIS operates as a data product distributed through the Archaeology Data Service, with users accessing the data through web interfaces or downloading in multiple formats."

**Metadata verdict**: Data product, not software. Uses ESRI ArcGIS geodatabase architecture but is accessed as data, not installed as software.

- [ ] GRANULARITY_ERROR (data product, not software)
- [ ] TOOL (the geodatabase/GIS constitutes a research tool)

**Notes**:

---

### 6. LogicistWriter

**Current status**: Not yet in evidence files (may be discovery-only)

**Summary**: Web-based application for constructing archaeological reasoning structures using logicist methodology. Hosted on France's Huma-Num infrastructure.

**Why it may not be a tool**: "Unlike typical open source archaeological software, LogicistWriter operates as a service rather than distributable code."

**Metadata verdict**: Service-based, not distributable software.

- [ ] GRANULARITY_ERROR (service, not distributable software)
- [ ] TOOL (web applications count as software tools)

**Notes**:

---

### 7. Endovélico

**Current status**: Not yet reviewed

**Summary**: Portuguese national archaeological site inventory and management system.

**Why it may be borderline**: "As primarily an inventory and management system rather than analytical research software, it occupies a borderline position." Meets research data engagement but "primary purpose was administrative rather than research-focused."

**Metadata verdict**: Borderline—inventory system rather than research software.

- [ ] BORDERLINE (keep as tool but note limitations)
- [ ] GRANULARITY_ERROR (administrative system, not research software)
- [ ] TOOL

**Notes**:

---

### 8. ArchaeoGRID

**Current status**: Not yet reviewed

**Summary**: Conceptual framework and prototype for distributed archaeological data management using grid computing.

**Why it may be borderline**: "Its limited implementation beyond conceptual and prototype stages, lack of evidence for widespread adoption in actual archaeological projects, and apparent discontinuation make its classification as a fully developed research software tool questionable."

**Metadata verdict**: "Remains in a borderline category."

- [ ] BORDERLINE (conceptual/prototype, not production software)
- [ ] GRANULARITY_ERROR (never fully implemented)
- [ ] TOOL

**Notes**:

---

## Summary of Potential Reclassifications

| Item | Current Status | Suggested Status | Reason |
|------|---------------|------------------|--------|
| VirtualArch | GRANULARITY_ERROR | GRANULARITY_ERROR | Project, not tool |
| ARIADNE | CONFIRMED | ? | Infrastructure/portal |
| TrueSpace | CONFIRMED | ? | No archaeological adoption |
| LSS | CONFIRMED | ? | No archaeological adoption |
| WallGIS | CONFIRMED | ? | Data product, not software |
| LogicistWriter | ? | ? | Service, not distributable |
| Endovélico | ? | ? | Administrative system |
| ArchaeoGRID | ? | ? | Prototype only |

---

## User Decisions

After review, update the relevant discovery and evidence files with confirmed classifications.
