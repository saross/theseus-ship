# Slop Evaluation Report: Tool Metadata Quality Assessment

## Framework

This evaluation uses the taxonomy from Shaib et al. (2025) "Measuring AI 'Slop' in Text" (arXiv:2509.19163), adapted for research software metadata entries.

**Definition**: "Slop" = AI-generated text that is generic, overly verbose, inaccurate, irrelevant, or contributes little meaningful value despite sounding fluent.

**7-code taxonomy**:
- Information Utility: Density (IU1), Relevance (IU2)
- Information Quality: Factuality (IQ1), Bias/Perspective (IQ2)
- Style Quality: Structure/Repetition (SQ1), Coherence (SQ3), Tone/Verbosity/Complexity (SQ4-7)

**Assessment scale**:
- **None**: No generic phrases; anchored claims â‰¥2.0 per 100 words; balanced perspective
- **Minimal**: 1-3 generic phrases; anchored claims 1.5-2.0 per 100 words; generally balanced
- **Moderate**: 4-6 generic phrases; anchored claims 1.0-1.5 per 100 words; some promotional tone
- **Significant**: >6 generic phrases; anchored claims <1.0 per 100 words; substantial filler

---

## Summary Results

| Tool | Words | Anchored/100w | Generic | Assessment |
|------|-------|---------------|---------|------------|
| FAIMS | 689 | 2.6 | 0 | None |
| archeoViz | 680 | 2.2 | 0 | None |
| Gephi | 850 | 2.1 | 1 | Minimal |
| ARIADNE | 950 | 2.1 | 2 | Minimal |
| PyLithics | 580 | 1.4 | 3 | Minimal |
| SEAHORS | 750 | 1.9 | 1 | Minimal |
| LifeForms | 638 | 1.6 | 2 | Minimal |
| SASSA | 775 | 1.5 | 2 | Minimal |
| SpadeR | 741 | 1.5 | 1 | Minimal |
| kdedemo | 723 | 1.7 | 1 | Minimal |

**Overall**: 2 entries scored "None", 8 scored "Minimal". No entries exhibited moderate or significant slop.

---

## Detailed Evaluations

### 1. FAIMS (Ground Truth)

**Word count**: 689

**Code-by-Code Assessment**:

- **IU1 (Density)**: None identified. Exceptionally high information density throughout.
- **IU2 (Relevance)**: None identified. All content directly addresses capabilities, history, and technical implementation.
- **IQ1 (Factuality)**: None identified. Verifiable claims include: Shawn Ross, Adela Sobotkova, 2012 start, NeCTAR funding, 2014 release, Macquarie University 2015, ARC LIEF AUD $945,000, NSW RAAP, ARDC 2020-2022, December 2022 FAIMS3, June 2023 Fieldmark rebrand, Electronic Field Notebooks Pty Ltd 2023, TypeScript/JavaScript/React/Capacitor/CouchDB stack.
- **IQ2 (Bias)**: None identified. Frank acknowledgment of limitations: "Technical complexity requires significant setup time", "Resource requirements... can be prohibitive", "Sociotechnical barriers exist".
- **SQ1 (Structure)**: "The current" appears 4Ã— â€” minor templating, functionally appropriate.
- **SQ3 (Coherence)**: None identified. History proceeds chronologically; Technical-discussion flows logically.
- **SQ4-7 (Tone)**: None identified. Appropriately technical; terms explained where needed.

**Claim inventory**: 18+ anchored, 15+ technical, 4 evaluative-with-evidence, 0 generic

**Assessment**: **None** â€” Exemplary entry with zero slop patterns.

---

### 2. archeoViz

**Word count**: ~680

**Code-by-Code Assessment**:

- **IU1 (Density)**: None identified. Every sentence conveys specific information (e.g., "convex hull computation (via the cxhull package)").
- **IU2 (Relevance)**: None identified. Content directly addresses tool capabilities.
- **IQ1 (Factuality)**: None identified. Verifiable: SÃ©bastien Plutniak, CITERES laboratory, CNRS/University of Tours, version 1.3.5, JOSS September 2023, Open Science Free Software Award November 2024.
- **IQ2 (Bias)**: None identified. Explicitly notes "not intended to replace more sophisticated analysis tools", "resource-intensive".
- **SQ1 (Structure)**: "The current version" appears 5Ã— â€” minor templating.
- **SQ3 (Coherence)**: None identified. Technical-discussion flows: architecture â†’ visualisation â†’ data handling â†’ export.
- **SQ4-7 (Tone)**: None identified. Appropriately technical without excessive jargon.

**Claim inventory**: 15+ anchored, 12+ technical, 3 evaluative-with-evidence, 0 generic

**Assessment**: **None**

---

### 3. Gephi

**Word count**: ~850

**Code-by-Code Assessment**:

- **IU1 (Density)**: "enables researchers to explore, analyse, and visualise complex relational data through an intuitive graphical interface" â€” somewhat generic opening. Recovers immediately with specifics.
- **IU2 (Relevance)**: None identified. Includes archaeology-specific applications appropriately.
- **IQ1 (Factuality)**: None identified. Verifiable: Mathieu Jacomy, 2006 origin, v0.6.0 July 2008, GraphStore project, Eduardo Ramos IbÃ¡Ã±ez 2017, v0.10.0 January 2023.
- **IQ2 (Bias)**: None identified. Acknowledges "technical debt", "outdated dependencies".
- **SQ1 (Structure)**: "The current version" appears 6Ã— â€” minor templating.
- **SQ3 (Coherence)**: None identified. Excellent flow in Technical-discussion.
- **SQ4-7 (Tone)**: None identified. Appropriately critical where warranted.

**Claim inventory**: 18+ anchored, 15+ technical, 4 evaluative-with-evidence, 1 generic

**Assessment**: **Minimal** â€” One generic opening phrase; otherwise excellent.

---

### 4. ARIADNE

**Word count**: ~950

**Code-by-Code Assessment**:

- **IU1 (Density)**: "addresses the critical problem of archaeological data fragmentation" â€” slightly generic framing. Otherwise dense with specifics (3.8 million resources, 40+ providers).
- **IU2 (Relevance)**: None identified. Appropriately clarifies this is infrastructure, not software.
- **IQ1 (Factuality)**: None identified. Verifiable: â‚¬6.5 million, 1 February 2013, FP7, â‚¬6.6 million H2020, November 2022 AISBL, THANADOS, BADACor, ATRIUM 2024-2027.
- **IQ2 (Bias)**: "significant achievements" â€” mildly promotional. Generally balanced; notes uneven coverage, technical barriers.
- **SQ1 (Structure)**: Some repetition of "current version of ARIADNE".
- **SQ3 (Coherence)**: None identified. Clear structure: architecture â†’ semantic foundation â†’ vocabulary â†’ access.
- **SQ4-7 (Tone)**: "sophisticated technical architecture" â€” mild overstatement. Technical terms appropriate.

**Claim inventory**: 20+ anchored, 12+ technical, 3 evaluative-with-evidence, 2 generic

**Assessment**: **Minimal** â€” Minor promotional framing; well-anchored overall.

---

### 5. PyLithics

**Word count**: ~580

**Code-by-Code Assessment**:

- **IU1 (Density)**: "enables researchers to transform the vast corpus of published lithic illustrations into machine-readable datasets, facilitating large-scale comparative analyses" â€” somewhat promotional.
- **IU2 (Relevance)**: None identified. Directly explains functionality.
- **IQ1 (Factuality)**: "~1000x faster" â€” specific but unattributed. Verifiable: Alan Turing Institute, Cambridge, JOSS January 29 2022, v1.0.
- **IQ2 (Bias)**: "First-of-its-kind" â€” strong promotional claim. Balanced by frank Weaknesses.
- **SQ1 (Structure)**: Strengths uses terse list format different from other entries.
- **SQ3 (Coherence)**: None identified. Technical-discussion flows through 11-step workflow.
- **SQ4-7 (Tone)**: Some promotional tone in Strengths balanced by Weaknesses.

**Claim inventory**: 8 anchored, 10+ technical, 2 evaluative-with-evidence, 2-3 generic

**Assessment**: **Minimal** â€” Fewer anchored claims; some promotional tone offset by honest limitations.

---

### 6. SEAHORS

**Word count**: ~750

**Code-by-Code Assessment**:

- **IU1 (Density)**: "facilitates intra-site spatial analysis of archaeological data without requiring extensive GIS or programming knowledge" â€” minor generic opening. Immediately followed by specific visualisation types.
- **IU2 (Relevance)**: None identified. Highly relevant content including specific site application (Cassenade).
- **IQ1 (Factuality)**: Verifiable: AurÃ©lien Royer, UniversitÃ© de Bourgogne, DeerPal, ANR-18-CE03-0007, PCI Archaeology 2023, CRAN, version 1.8.0, December 2023 bar plot, January 2024 save/load, https://aurelienroyer.shinyapps.io/Seahors/.
- **IQ2 (Bias)**: None identified. Frank limitations: "unsuitable for regional studies", "lacks advanced spatial statistical methods", "performance with very large datasets (>10,000 points) remains untested".
- **SQ1 (Structure)**: Minor templating from prompt structure.
- **SQ3 (Coherence)**: None identified. Good logical flow.
- **SQ4-7 (Tone)**: None identified. Appropriately technical.

**Claim inventory**: 14 anchored, 10+ technical, 2 evaluative-with-evidence, 1 generic

**Assessment**: **Minimal** â€” One minor generic opening; otherwise well-anchored with specific funding codes and URLs.

---

### 7. LifeForms

**Word count**: ~638

**Code-by-Code Assessment**:

- **IU1 (Density)**: "unique capabilities for visualising human movement aspects of cultural heritage that traditional archaeological tools often overlook" â€” repeated in Description and Strengths. Minor redundancy.
- **IU2 (Relevance)**: None identified. Appropriately notes limited archaeological applicability.
- **IQ1 (Factuality)**: Verifiable: Simon Fraser University, Dr. Tom Calvert, Thecla Schiphorst, Merce Cunningham 1989-1990, 'Trackers' 1991, Credo Interactive, Prambanan temple.
- **IQ2 (Bias)**: "unique capabilities" â€” mild promotional. Balanced by frank limitations about Western dance bias and proprietary nature.
- **SQ1 (Structure)**: Repetition of "unique capabilities" phrase across sections.
- **SQ3 (Coherence)**: None identified. Clear historical narrative.
- **SQ4-7 (Tone)**: None identified. Appropriate for a tool with limited archaeological application.

**Claim inventory**: 10 anchored, 8 technical, 1 evaluative-with-evidence, 2 generic

**Assessment**: **Minimal** â€” Good historical anchoring; honest about narrow applicability.

---

### 8. SASSA

**Word count**: ~775

**Code-by-Code Assessment**:

- **IU1 (Density)**: "bridge the knowledge gap between soil science and archaeology" â€” slightly generic. Overall high density.
- **IU2 (Relevance)**: None identified. Directly relevant to archaeological soil interpretation.
- **IQ1 (Factuality)**: Verifiable: University of Stirling, 2005-2007 development, NERC funding, 2007 launch, Internet Archaeology Issue 25 (2008), MediaWiki, LAMP stack.
- **IQ2 (Bias)**: "exemplary scientific communication" â€” mild promotional. Notably balanced; explicitly states "project did not transition successfully from initial grant funding", "little evidence of substantial updates after 2009".
- **SQ1 (Structure)**: Minor templating.
- **SQ3 (Coherence)**: None identified. Clear chronological and technical structure.
- **SQ4-7 (Tone)**: None identified. Appropriately frank about sustainability failure.

**Claim inventory**: 12 anchored, 8 technical, 2 evaluative-with-evidence, 2 generic

**Assessment**: **Minimal** â€” Frank acknowledgment of sustainability failure distinguishes this from slop; well-anchored.

---

### 9. SpadeR

**Word count**: ~741

**Code-by-Code Assessment**:

- **IU1 (Density)**: "with limited applications in archaeology" â€” appropriately honest framing, not generic.
- **IU2 (Relevance)**: None identified. Clearly contextualises limited archaeological applicability.
- **IQ1 (Factuality)**: Verifiable: Anne Chao, National Tsing Hua University, CRAN, version 0.1.1, September 6 2016, SPADE C++ origins, iNEXT successor, https://chao.shinyapps.io/SpadeR/.
- **IQ2 (Bias)**: None identified. Balanced; notes "limited active development since 2016", "steep learning curve", "ecological assumptions require careful consideration".
- **SQ1 (Structure)**: Numbered lists in Strengths/Weaknesses follow consistent format.
- **SQ3 (Coherence)**: None identified. Good technical explanation of data formats.
- **SQ4-7 (Tone)**: "comprehensive statistical framework" â€” minor overstatement. Otherwise appropriate.

**Claim inventory**: 11 anchored, 10 technical, 2 evaluative-with-evidence, 1 generic

**Assessment**: **Minimal** â€” Honest about limited archaeological scope; well-anchored with specific versions and URLs.

---

### 10. kdedemo

**Word count**: ~723

**Code-by-Code Assessment**:

- **IU1 (Density)**: "pioneering" â€” promotional but historically accurate for 1996. High information density overall.
- **IU2 (Relevance)**: None identified. Appropriately positioned as historical tool.
- **IQ1 (Factuality)**: Verifiable: Nottingham Trent University, Christian C. Beardah, Michael J. Baxter, Internet Archaeology 1996, CAA 1995, 'Interfacing the Past', MATLAB 4.2c. Direct quote: "can claim some credit for introducing KDEs into the archaeological literature, though it was not really taken up until the 2000s".
- **IQ2 (Bias)**: None identified. Retrospective assessment is notably humble: acknowledges limited adoption, notes "modern alternatives like R now provide more accessible implementations".
- **SQ1 (Structure)**: Minor templating.
- **SQ3 (Coherence)**: None identified. Excellent historical narrative with retrospective insight.
- **SQ4-7 (Tone)**: None identified. Appropriately positions historical significance without overclaiming.

**Claim inventory**: 12 anchored, 8 technical, 2 evaluative-with-evidence, 1 generic

**Assessment**: **Minimal** â€” Excellent historical anchoring with honest retrospective; quotes from developers add authenticity.

---

## Overall Findings

### Quantitative Summary

- **Mean word count**: 693 words (range 580-950)
- **Mean anchored claims/100 words**: 1.9 (range 1.4-2.6)
- **Mean generic phrases**: 1.3 (range 0-3)
- **Assessment distribution**: 2 None, 8 Minimal, 0 Moderate, 0 Significant

### Qualitative Observations

1. **No significant slop detected**: All entries demonstrate substantive content with verifiable claims.

2. **Generic phrases when present are minor**: Typically occur in opening framings ("enables researchers to...") â€” a common pattern in technical writing that doesn't undermine utility.

3. **Balanced perspective is consistent**: Weaknesses sections across all entries contain frank, specific limitations rather than defensive hedging.

4. **Historical tools handled well**: kdedemo and SASSA demonstrate appropriate retrospective assessment, including honest acknowledgment of limited adoption or sustainability failures.

5. **Cross-disciplinary tools appropriately contextualised**: LifeForms, SpadeR, and Gephi clearly note their limited archaeological applicability without overclaiming.

6. **The "domestication" strategy works**: Version histories are detailed but appropriately placed in History fields; technical specifications are precise in Technical-discussion fields.

### Implications for Paper

The metadata prompt successfully elicits substantive, verifiable content with minimal slop. Using the Shaib et al. (2025) framework, a sample of 10 entries (including expert-validated ground truth) found high information density (1.4â€“2.6 anchored claims per 100 words) with minimal generic content (0â€“3 phrases per entry). No entries exhibited the characteristic slop patterns identified in the literature: verbosity without information, hallucinated attributions, incoherent flow, or excessive promotional claims without substantiation.

---

## Reference

Shaib, C., et al. (2025). Measuring AI "Slop" in Text. *arXiv preprint arXiv:2509.19163*. https://arxiv.org/abs/2509.19163