# Prompt Development Corpus Index
## "An Absence of Judgment" Project — February to May 2025

This document serves as a finding aid for conversations documenting the iterative development of prompts for archaeological software tool metadata collection. These conversations represent primary source material for autoethnographic analysis of prompt engineering methodology.

---

## Overview

**Date Range:** 16 February 2025 – 7 May 2025  
**Total Conversations Indexed:** 40  
**Project Focus:** Development of prompts for AI-assisted metadata collection about archaeological research software tools

### Development Phases

| Phase | Period | Focus | Key Outputs |
|-------|--------|-------|-------------|
| Conceptual Foundation | Feb 2025 | Literature review, initial tool definition | Paper summaries, Open-Archaeo evaluation framework |
| Definition Refinement | Late Apr–1 May | Formalising "research software tool" definition | LaTeX definition document |
| Prompt Iteration | 2–5 May | Rapid iteration (v1–v8) with test tools | Metadata collection prompt, Writing Style Guide |
| Scaling Production | 5–7 May | Systematic collection, edge case refinements | Tool disambiguation, title conventions |

---

## Conversation Index

### Phase 1: Conceptual Foundation (February 2025)

#### 1. Preserving Digital Humanities Research Data
- **Date:** 16 February 2025
- **UUID:** `f3023ec2-702f-4553-aa6c-9b9b7b7a8a34`
- **URL:** https://claude.ai/chat/f3023ec2-702f-4553-aa6c-9b9b7b7a8a34
- **Synopsis:** Summary of "Fading Away... The challenge of sustainability in digital studies" paper. Established foundational understanding of digital preservation challenges in humanities research.
- **Key Themes:** Data sustainability, institutional challenges, preservation approaches, research tool obsolescence

#### 2. Evaluating Archaeology Software Dataset
- **Date:** 21 February 2025
- **UUID:** `ecb39dda-ac13-44f2-b664-31874fe76dce`
- **URL:** https://claude.ai/chat/ecb39dda-ac13-44f2-b664-31874fe76dce
- **Synopsis:** Evaluation of Open-Archaeo dataset entries against initial tool definition. First systematic application of tool classification criteria.
- **Key Themes:** Tool definition development, Open-Archaeo categories (Packages/Libraries, Products, Scripts, Standalone Software), screening methodology
- **Notable:** Contains early tool definition: "a software tool is any discrete piece of software—be it a program, script, or web application—that is developed or substantially modified by researchers to perform specific, research-oriented computational tasks"

---

### Phase 2: Definition Refinement (May 2025)

#### 3. Defining Research Software Tools
- **Date:** 1 May 2025
- **UUID:** `21561146-3640-43d8-b645-20084703b462`
- **URL:** https://claude.ai/chat/21561146-3640-43d8-b645-20084703b462
- **Synopsis:** Development of comprehensive "research software tool" definition drawing on Hettrick report. Produced LaTeX document with both concise and detailed definitions.
- **Key Themes:** Research software characteristics, distinguishing features, sustainability considerations, lifecycle variability
- **Notable:** Generated formal definition document integrating project knowledge with broader literature

---

### Phase 3: Prompt Iteration (2–5 May 2025)

#### 4. v1-FAIMS-metadata
- **Date:** 2 May 2025
- **UUID:** `849d1e45-3fee-4aad-8500-56bc78e7b7d0`
- **URL:** https://claude.ai/chat/849d1e45-3fee-4aad-8500-56bc78e7b7d0
- **Synopsis:** First attempt at FAIMS metadata collection. Established initial prompt structure with clarifying questions about focus and version history.
- **Key Themes:** Initial prompt testing, FAIMS as test case, version history considerations

#### 5. v3-FAIMS-metadata
- **Date:** 2 May 2025
- **UUID:** `2e210f3a-5152-4ef8-9cc0-f8ed2a7872f8`
- **URL:** https://claude.ai/chat/2e210f3a-5152-4ef8-9cc0-f8ed2a7872f8
- **Synopsis:** Refined FAIMS metadata collection with more structured prompt. CSV output generation introduced.
- **Key Themes:** CSV formatting, structured metadata fields, tool evaluation framework

#### 6. v2-FAIMS-metadata and prompt-improvement
- **Date:** 3 May 2025
- **UUID:** `b6592b63-0387-4d57-899b-64ef7a9deda3`
- **URL:** https://claude.ai/chat/b6592b63-0387-4d57-899b-64ef7a9deda3
- **Synopsis:** Prompt refinement discussion including usage indicators, development timeline, and organisational context fields.
- **Key Themes:** Field consolidation, sustainability indicators, adoption metrics

#### 7. v4-FAIMS-metadata
- **Date:** 3 May 2025
- **UUID:** `5d3c07ca-4fbf-4eae-bbc2-b8b5b6ac04e0`
- **URL:** https://claude.ai/chat/5d3c07ca-4fbf-4eae-bbc2-b8b5b6ac04e0
- **Synopsis:** Further FAIMS testing with v4 prompt. Discussion of API access for batch processing.
- **Key Themes:** Batch processing considerations, API integration possibilities

#### 8. v4-VOSviewer-metadata
- **Date:** 3 May 2025
- **UUID:** `17d43b38-bc37-4e2a-a762-6e610ddb9fa7`
- **URL:** https://claude.ai/chat/17d43b38-bc37-4e2a-a762-6e610ddb9fa7
- **Synopsis:** Testing prompt with VOSviewer (bibliometric visualisation tool). First test with non-archaeology-specific tool.
- **Key Themes:** Cross-disciplinary tool evaluation, bibliometric software

#### 9. v5-ade4-metadata
- **Date:** 3 May 2025
- **UUID:** `da124a03-a346-4655-bb6c-80c61c0eb225`
- **URL:** https://claude.ai/chat/da124a03-a346-4655-bb6c-80c61c0eb225
- **Synopsis:** Testing with ade4 R package. Revealed need for handling tools from other disciplines applied to archaeology.
- **Key Themes:** Cross-disciplinary tools, ecological statistics in archaeology

#### 10. v4-ade4-metadata
- **Date:** 3 May 2025
- **UUID:** `a9305db4-28c8-490e-a9a1-b85c9a6ba2b2`
- **URL:** https://claude.ai/chat/a9305db4-28c8-490e-a9a1-b85c9a6ba2b2
- **Synopsis:** Prompt review revealing need for "Original-discipline" field and cross-disciplinary tool handling.
- **Key Themes:** Original-discipline field addition, evaluation criteria refinement
- **Notable:** Led to explicit instruction that "tools developed for other disciplines and repurposed for archaeology are to be expected and not disqualified"

#### 11. v6-ade4-metadata
- **Date:** 4 May 2025
- **UUID:** `d59ad5f7-a2d3-4d6b-b314-57c7f2e5e753`
- **URL:** https://claude.ai/chat/d59ad5f7-a2d3-4d6b-b314-57c7f2e5e753
- **Synopsis:** Writing style exploration. Attempted formal academic revision deemed "not quite so clear."
- **Key Themes:** Writing style balance, clarity vs formality trade-offs
- **Notable:** Led to decision to develop separate Writing Style Guide

#### 12. v6-WSG-ade4-metadata
- **Date:** 4 May 2025
- **UUID:** `d9607165-6c5e-4649-baba-482fcea9d764`
- **URL:** https://claude.ai/chat/d9607165-6c5e-4649-baba-482fcea9d764
- **Synopsis:** First integration of Writing Style Guide with metadata collection prompt.
- **Key Themes:** Australian English, academic clarity, style guide application

#### 13. v7-ade4-metadata
- **Date:** 4 May 2025
- **UUID:** `48087fb6-3b26-4a4b-a8b9-e8c8a8e17ba4`
- **URL:** https://claude.ai/chat/48087fb6-3b26-4a4b-a8b9-e8c8a8e17ba4
- **Synopsis:** Confirmed Writing Style Guide recognition. Addressed CSV generation consistency issue.
- **Key Themes:** Output consistency, CSV generation automation
- **Notable:** Resolved issue of needing separate prompt for CSV output

#### 14. v7-AgisoftPhotoscan-metadata and prompt improvement
- **Date:** 4 May 2025
- **UUID:** `ffca9f05-ceb1-48e9-8e05-136906081303`
- **URL:** https://claude.ai/chat/ffca9f05-ceb1-48e9-8e05-136906081303
- **Synopsis:** Testing with Agisoft PhotoScan/Metashape. Research depth and field length guidance developed.
- **Key Themes:** Research depth requirements, field length guidance (200-250 words target)

#### 15. v8-FAIMS-metadata and prompt improvement
- **Date:** 4 May 2025
- **UUID:** `e58947d8-f5b1-4e05-bcac-ce2b1bfc5117`
- **URL:** https://claude.ai/chat/e58947d8-f5b1-4e05-bcac-ce2b1bfc5117
- **Synopsis:** Version clarity guidelines development for tools with multiple versions (FAIMS → Fieldmark).
- **Key Themes:** Version disambiguation, temporal markers, current vs previous version handling
- **Notable:** Produced Version Clarity Guidelines section for prompt

#### 16. v8-ade4-metadata
- **Date:** 4 May 2025
- **UUID:** `9508de85-48a3-46da-99d8-5334e940260a`
- **URL:** https://claude.ai/chat/9508de85-48a3-46da-99d8-5334e940260a
- **Synopsis:** Clean v8 test run with ade4. Validated prompt improvements.
- **Key Themes:** Prompt validation, R package metadata

#### 17. v8-Agisoft-metadata
- **Date:** 4 May 2025
- **UUID:** `70f47e62-6b6f-4f67-96e3-dd36cf19ce40`
- **URL:** https://claude.ai/chat/70f47e62-6b6f-4f67-96e3-dd36cf19ce40
- **Synopsis:** Clean v8 test with Agisoft PhotoScan. Validated photogrammetry tool handling.
- **Key Themes:** Commercial software handling, photogrammetry tools

---

### Phase 4: Scaling Production (5–7 May 2025)

#### 18. v8-aion-metadata
- **Date:** 5 May 2025
- **UUID:** `415ed51b-513b-4bdc-bdbd-237ce56caeee`
- **URL:** https://claude.ai/chat/415ed51b-513b-4bdc-bdbd-237ce56caeee
- **Synopsis:** Aion metadata collection. Tool disambiguation guidance developed.
- **Key Themes:** Ambiguous tool names, archaeological application priority
- **Notable:** Produced Tool Disambiguation section: "When encountering tools with ambiguous names, always prioritize the archaeological/historical research application version"

#### 19. v8-ArcGISSkeletalTemplates-metadata
- **Date:** 5 May 2025
- **UUID:** `4e37f132-88c2-4a3d-a699-e31eb3167dce`
- **URL:** https://claude.ai/chat/4e37f132-88c2-4a3d-a699-e31eb3167dce
- **Synopsis:** ArcGIS skeletal templates metadata. Revealed categorisation issues for plugins/extensions.
- **Key Themes:** Category definitions, platform dependencies, CSV validation
- **Notable:** Led to enhanced category definitions and structured validation checklist

#### 20. v8-ArchIScan-metadata
- **Date:** 5 May 2025
- **UUID:** `6fe826fa-967c-4354-b08d-7c96a6540f9c`
- **URL:** https://claude.ai/chat/6fe826fa-967c-4354-b08d-7c96a6540f9c
- **Synopsis:** Arch-I-Scan metadata collection. Title conventions refined.
- **Key Themes:** Academic tone in titles, avoiding sensationalism
- **Notable:** Produced Title Conventions section with format "[Tool Name]: [Primary Function] for [Application Domain]"

#### 21. v8-Annotorious-metadata
- **Date:** 5 May 2025
- **UUID:** `a97ab597-66e0-4782-9e82-5dc3b6549eec`
- **URL:** https://claude.ai/chat/a97ab597-66e0-4782-9e82-5dc3b6549eec
- **Synopsis:** Annotorious (image annotation tool) metadata collection.
- **Key Themes:** Digital humanities tools, annotation software, W3C standards

#### 22. v8-ArchaeoPhases-metadata
- **Date:** 5 May 2025
- **UUID:** `e7e67938-e612-4751-a14e-e83e55ef608b`
- **URL:** https://claude.ai/chat/e7e67938-e612-4751-a14e-e83e55ef608b
- **Synopsis:** ArchaeoPhases R package metadata. Chronological modelling focus.
- **Key Themes:** Bayesian chronology, R packages, MCMC post-processing

#### 23. v8-ArchAIDE-metadata
- **Date:** 5 May 2025
- **UUID:** `d996a859-1fe1-4f27-9629-51fc1b10af32`
- **URL:** https://claude.ai/chat/d996a859-1fe1-4f27-9629-51fc1b10af32
- **Synopsis:** ArchAIDE (ceramic identification AI) metadata. First "no follow-up questions" instruction.
- **Key Themes:** AI/ML tools, ceramic classification, EU-funded projects

#### 24. v8-ArchED-metadata
- **Date:** 5 May 2025
- **UUID:** `c318289d-9303-46bb-adb9-9ef6cde07fac`
- **URL:** https://claude.ai/chat/c318289d-9303-46bb-adb9-9ef6cde07fac
- **Synopsis:** ArchEd (Harris matrix software) metadata collection.
- **Key Themes:** Stratigraphic analysis, abandoned software, legacy tools

#### 25. v8-Archaefrag-metadata
- **Date:** 5 May 2025
- **UUID:** `7482d18e-17d8-423c-a8bf-0d768aece3b0`
- **URL:** https://claude.ai/chat/7482d18e-17d8-423c-a8bf-0d768aece3b0
- **Synopsis:** ArcheoFrag (refitting analysis) metadata. Title convention enforcement.
- **Key Themes:** Fragment refitting, network analysis, R packages

#### 26. v8-archeoViz-metadata
- **Date:** 5 May 2025
- **UUID:** `bd5e93fc-9501-48b0-9345-01c4ed2b3572`
- **URL:** https://claude.ai/chat/bd5e93fc-9501-48b0-9345-01c4ed2b3572
- **Synopsis:** archeoViz (spatial visualisation) metadata collection.
- **Key Themes:** R Shiny applications, intra-site spatial analysis, CNRS tools

#### 27. v8-ARIADNE-metadata
- **Date:** 6 May 2025
- **UUID:** `cf43507b-2e63-4705-ad5e-c60e2f5445ca`
- **URL:** https://claude.ai/chat/cf43507b-2e63-4705-ad5e-c60e2f5445ca
- **Synopsis:** ARIADNE infrastructure metadata. Handling of data infrastructures vs tools.
- **Key Themes:** Research infrastructure classification, EU projects, data aggregation

#### 28. v8-BCal-metadata
- **Date:** 6 May 2025
- **UUID:** `014afb2b-4c6d-45d0-99b1-bc14b922ed1d`
- **URL:** https://claude.ai/chat/014afb2b-4c6d-45d0-99b1-bc14b922ed1d
- **Synopsis:** BCal (Bayesian calibration) metadata. Abandoned tool documentation.
- **Key Themes:** Web-based tools, abandoned software, chronological modelling

#### 29. v8-Bchron-metadata
- **Date:** 6 May 2025
- **UUID:** `ae006b56-7e59-4b75-98fc-bc41fdf63696`
- **URL:** https://claude.ai/chat/ae006b56-7e59-4b75-98fc-bc41fdf63696
- **Synopsis:** Bchron (chronology modelling) metadata collection.
- **Key Themes:** R packages, age-depth modelling, palaeoenvironmental tools

#### 30. v8-bleiglas-metadata
- **Date:** 6 May 2025
- **UUID:** `6b48c966-5e7a-4e22-9e8b-9abf1e827ec0`
- **URL:** https://claude.ai/chat/6b48c966-5e7a-4e22-9e8b-9abf1e827ec0
- **Synopsis:** bleiglas (3D tessellation) metadata. Niche tool handling.
- **Key Themes:** Spatiotemporal analysis, Voronoi tessellation, Max Planck tools

#### 31. v8-Bwigg-metadata-fail
- **Date:** 6 May 2025
- **UUID:** `eca2e545-c48b-42c0-9364-3ae3f1f9f0c4`
- **URL:** https://claude.ai/chat/eca2e545-c48b-42c0-9364-3ae3f1f9f0c4
- **Synopsis:** Bwigg search failure. Tool not found despite research efforts.
- **Key Themes:** Research failure handling, insufficient information scenarios

#### 32. v8-c14bazAAR-metadata
- **Date:** 6 May 2025
- **UUID:** `0e78aa6d-455f-4f5d-a26c-9f539a7b1e85`
- **URL:** https://claude.ai/chat/0e78aa6d-455f-4f5d-a26c-9f539a7b1e85
- **Synopsis:** c14bazAAR (radiocarbon database aggregator) metadata.
- **Key Themes:** Data aggregation tools, radiocarbon dating, rOpenSci

#### 33. v8-DataScribe-metadata
- **Date:** 6 May 2025
- **UUID:** `e9822bcc-9f6a-4ab0-9273-8d53aa3fdcfa`
- **URL:** https://claude.ai/chat/e9822bcc-9f6a-4ab0-9273-8d53aa3fdcfa
- **Synopsis:** DataScribe (historical transcription) metadata collection.
- **Key Themes:** Omeka S modules, historical data entry, structured transcription

#### 34. v8-DepthmapX-metadata-CSV
- **Date:** 6 May 2025
- **UUID:** `e27036e6-2215-4fef-9ba4-5387b1a22c2d`
- **URL:** https://claude.ai/chat/e27036e6-2215-4fef-9ba4-5387b1a22c2d
- **Synopsis:** DepthmapX (space syntax analysis) metadata with CSV output.
- **Key Themes:** Space syntax, visibility analysis, UCL tools

#### 35. v8-DepthmapX-metadata-noCSV
- **Date:** 6 May 2025
- **UUID:** `769af40d-b146-4b35-80d4-706c0774c148`
- **URL:** https://claude.ai/chat/769af40d-b146-4b35-80d4-706c0774c148
- **Synopsis:** DepthmapX metadata without CSV (parallel test run).
- **Key Themes:** Output consistency testing

#### 36. v8-DistantViewingToolkit-metadata
- **Date:** 6 May 2025
- **UUID:** `2ccacb91-cc14-475e-afe5-d3ab73716898`
- **URL:** https://claude.ai/chat/2ccacb91-cc14-475e-afe5-d3ab73716898
- **Synopsis:** Distant Viewing Toolkit (visual analysis) metadata.
- **Key Themes:** Computer vision, digital humanities, moving image analysis

#### 37. v8-dplR-metadata
- **Date:** 6 May 2025
- **UUID:** `1a24aafb-0a23-4260-92c1-7df9162e1c43`
- **URL:** https://claude.ai/chat/1a24aafb-0a23-4260-92c1-7df9162e1c43
- **Synopsis:** dplR (dendrochronology) metadata collection.
- **Key Themes:** Tree-ring analysis, R packages, OpenDendro initiative

#### 38. v8-Endovélico-metadata
- **Date:** 6 May 2025
- **UUID:** `ce31e610-3b81-420d-ad17-d8722daa8cb1`
- **URL:** https://claude.ai/chat/ce31e610-3b81-420d-ad17-d8722daa8cb1
- **Synopsis:** Endovélico (Portuguese archaeological database) metadata.
- **Key Themes:** National databases, heritage management systems, government tools

#### 39. v8-fellingdater-metadata
- **Date:** 6 May 2025
- **UUID:** `282c6b6c-cf54-4e00-9147-17a5e0064845`
- **URL:** https://claude.ai/chat/282c6b6c-cf54-4e00-9147-17a5e0064845
- **Synopsis:** FellingDater (dendrochronology) metadata collection.
- **Key Themes:** Tree-ring dating, timber analysis, heritage applications

#### 40. v8-FieldworkerAdvanced-metadata
- **Date:** 7 May 2025
- **UUID:** `a6debb7d-80a1-4a5a-ac82-a5c1af646ad3`
- **URL:** https://claude.ai/chat/a6debb7d-80a1-4a5a-ac82-a5c1af646ad3
- **Synopsis:** FieldWorker Advanced (mobile data collection) metadata. Title convention correction.
- **Key Themes:** Legacy software, mobile data collection, Palm OS era tools
- **Notable:** Required title regeneration to match "[Tool Name]: [Primary Function] for [Application Domain]" convention

---

## Key Prompt Evolution Milestones

| Date | Conversation | Change Introduced |
|------|--------------|-------------------|
| 21 Feb | #2 | Initial tool definition |
| 1 May | #3 | Formal research software tool definition |
| 3 May | #10 | Original-discipline field; cross-disciplinary handling |
| 4 May | #11-12 | Writing Style Guide development |
| 4 May | #15 | Version Clarity Guidelines |
| 5 May | #18 | Tool Disambiguation guidance |
| 5 May | #19 | Category definitions; CSV validation checklist |
| 5 May | #20 | Title Conventions |
| 5 May | #23 | "No follow-up questions" instruction for consistency |

---

## Conversation UUIDs for Export Filtering

The following UUIDs identify all conversations in this project within the Feb–May 2025 date range. Use these for filtering the JSON export:

```
f3023ec2-702f-4553-aa6c-9b9b7b7a8a34
ecb39dda-ac13-44f2-b664-31874fe76dce
21561146-3640-43d8-b645-20084703b462
849d1e45-3fee-4aad-8500-56bc78e7b7d0
2e210f3a-5152-4ef8-9cc0-f8ed2a7872f8
b6592b63-0387-4d57-899b-64ef7a9deda3
5d3c07ca-4fbf-4eae-bbc2-b8b5b6ac04e0
17d43b38-bc37-4e2a-a762-6e610ddb9fa7
da124a03-a346-4655-bb6c-80c61c0eb225
a9305db4-28c8-490e-a9a1-b85c9a6ba2b2
d59ad5f7-a2d3-4d6b-b314-57c7f2e5e753
d9607165-6c5e-4649-baba-482fcea9d764
48087fb6-3b26-4a4b-a8b9-e8c8a8e17ba4
ffca9f05-ceb1-48e9-8e05-136906081303
e58947d8-f5b1-4e05-bcac-ce2b1bfc5117
9508de85-48a3-46da-99d8-5334e940260a
70f47e62-6b6f-4f67-96e3-dd36cf19ce40
415ed51b-513b-4bdc-bdbd-237ce56caeee
4e37f132-88c2-4a3d-a699-e31eb3167dce
6fe826fa-967c-4354-b08d-7c96a6540f9c
a97ab597-66e0-4782-9e82-5dc3b6549eec
e7e67938-e612-4751-a14e-e83e55ef608b
d996a859-1fe1-4f27-9629-51fc1b10af32
c318289d-9303-46bb-adb9-9ef6cde07fac
7482d18e-17d8-423c-a8bf-0d768aece3b0
bd5e93fc-9501-48b0-9345-01c4ed2b3572
cf43507b-2e63-4705-ad5e-c60e2f5445ca
014afb2b-4c6d-45d0-99b1-bc14b922ed1d
ae006b56-7e59-4b75-98fc-bc41fdf63696
6b48c966-5e7a-4e22-9e8b-9abf1e827ec0
eca2e545-c48b-42c0-9364-3ae3f1f9f0c4
0e78aa6d-455f-4f5d-a26c-9f539a7b1e85
e9822bcc-9f6a-4ab0-9273-8d53aa3fdcfa
e27036e6-2215-4fef-9ba4-5387b1a22c2d
769af40d-b146-4b35-80d4-706c0774c148
2ccacb91-cc14-475e-afe5-d3ab73716898
1a24aafb-0a23-4260-92c1-7df9162e1c43
ce31e610-3b81-420d-ad17-d8722daa8cb1
282c6b6c-cf54-4e00-9147-17a5e0064845
a6debb7d-80a1-4a5a-ac82-a5c1af646ad3
```

---

## Notes on Corpus Limitations

1. **Excerpts Only:** The synopses above are based on truncated conversation snippets retrieved via the `recent_chats` tool, not complete transcripts.

2. **Possible Missing Conversations:** If additional conversations exist in this project outside the retrieved set, they would not appear in this index.

3. **Project Identification:** These conversations were retrieved as belonging to the current project scope. The JSON export will need to be filtered using either the UUIDs above or project metadata if available in the export structure.

---

*Index generated: December 2025*
*Source: Claude past chats retrieval within project scope*
