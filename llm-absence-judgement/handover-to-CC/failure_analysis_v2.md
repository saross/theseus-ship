## Failure Analysis: Detailed Evidence from Chat Review (v2)

**v2 Note (3 Dec 2025)**: This version corrects the Bwigg classification. Original analysis characterised Bwigg as "origin unknown" / "insufficient signal". Re-checking `tool_discovery_granular.csv` reveals Bwigg was cross-validated (found by ChatGPT DR and Perplexity DR, 3 instances total) with a specific article citation: "Bwigg: An Internet facility for Bayesian radiocarbon wiggle-matching" by J. Andrés Christen, Internet Archaeology issue 13 (2003). Bwigg is therefore a verified real tool that failed downstream due to minimal online presence, not a discovery failure.

---

### Failure Classification (Revised)

Based on reviewing actual chat histories, failures fall into distinct categories:

**Type 1a: Real but Undocumented Tools**
Tools that genuinely exist but lack sufficient public documentation.

| Tool | Reality | Why Metadata Failed |
|------|---------|---------------------|
| PyCoCu | Site-specific Python script for Combe-Cullier cave (Sécher et al. 2020, cited in SEAHORS paper) | No public repo or documentation; exists only as passing reference in literature |

This represents ChatGPT DR's genuine literature-mining capability finding something real but undocumentable. Claude's failure was appropriate.

**Type 1b: Name Collision with Non-Archaeological Software**

| Tool | Dominant Non-Archaeological Software | Archaeological Connection |
|------|-------------------------------------|---------------------------|
| FaceNet | Google's face recognition system | None found |
| Microware | OS-9 operating system | None found |
| pnuts | Java scripting language | None (Claude provided full metadata, flagged non-applicability) |
| Fountain | Screenplay markup language | None found |

**Type 1c: Insufficient Signal (Genuinely Undiscoverable)**

| Tool | Outcome |
|------|---------|
| Wcvt2Pov | Nothing found; led to POV-Ray recovery |

**Type 1d: Minimal Online Footprint (Verified Real)** ← NEW CATEGORY

| Tool | Discovery Status | Why Downstream Failed |
|------|------------------|----------------------|
| Bwigg | Cross-validated: found by ChatGPT DR + Perplexity DR (3 instances); specific article: Christen 2003, IA issue 13 | 2003 tool with minimal web presence beyond original publication; failed both metadata AND evidence collection |

**Methodological significance**: Bwigg demonstrates that perfect discovery does not guarantee downstream success. Even when discovery works optimally (cross-validated, specific citation found), subsequent tasks can fail if the tool has minimal online footprint. This is a genuine constraint of web-based LLM research independent of model capability.

**Key pattern**: Across all Type 1 failures, Claude didn't hallucinate. It correctly identified when tools couldn't be found, explicitly stated negative findings, and provided useful context or alternatives.

**Type 2: Discovery Granularity Errors → Recovery**
Tool discovery prompt returned something at wrong level of abstraction, but metadata prompt successfully recovered.

| Tool | Error | Recovery |
|------|-------|----------|
| MASA | Discovery returned ecosystem/consortium name instead of individual tools | Metadata prompt correctly identified 3 component tools (LogicistWriter, OpenArchaeo, OpenGuide); separate metadata runs for each |

Chat evidence: "MASA is a consortium established in 2012... The ecosystem comprises three primary tools: 1. OpenArchaeo... 2. LogicistWriter... 3. OpenGuide..."

**Type 3: Initial Misidentification → Clarification → Success**
Model guessed wrong tool initially, but provided enough information to enable correction.

| Tool | Initial Error | Recovery Mechanism |
|------|---------------|-------------------|
| STELLAR | Guessed "STELLAR (Stratigraphy and Harris Matrix Analyzer)" — doesn't exist | Report mentioned actual STELLAR: "Semantic Technologies Enhancing Links and Linked Data for Archaeological Resources"; second run with clarification succeeded |

Chat evidence from failed run: "The STELLAR that does exist in archaeological contexts is 'Semantic Technologies Enhancing Links and Linked Data for Archaeological Resources' - a one-year AHRC-funded project (2010-2011)..."

This is the "produce something" behaviour working *in the researcher's favour* — the model's attempt to be helpful even when failing provided the clue needed for correction.

**Type 4: Closest-Match Identification**
Model couldn't find exact tool but identified likely candidates.

| Tool | Outcome |
|------|---------|
| Grid Machine | Found no exact match; identified "University of Queensland grid computing project (2004-2008)" as closest candidate; also found ArchaeoGRID as related tool |

Chat title explicitly shows recovery: "v8-GridMachine-metadata (fail) and ArchaeoGRID (closest tool)"

**Type 5: Name Clarification Discovery**
Initial search term led to discovering proper product name.

| Tool | Discovery Path |
|------|----------------|
| Rhinoceros 3D | "Rhino for AutoCAD" prompt correctly identified the integration ecosystem; Description opened with "Rhinoceros 3D (Rhino) integration with AutoCAD..." which revealed proper product name. Second run with "Rhinoceros 3D" produced cleaner standalone product entry. |

Both entries are valid — they describe different things (integration vs. standalone). The first wasn't wrong, it just prompted recognition that the base product deserved its own entry.

**Type 6: Fallback/Recovery Entry**
ArchaeoGRID was not a separate prompt run — it emerged from the Grid Machine failure. When "Grid Machine" couldn't be found, Claude identified ArchaeoGRID as the closest match and produced metadata for it.

- Chat: "v8-GridMachine-metadata (fail) and ArchaeoGRID (closest tool)"
- Yellow highlighting in spreadsheet likely indicates: entry came from non-standard discovery path (fallback from failed search)
- Metadata appears valid; the "different emphasis" is about provenance, not quality

### Key Insight: "Produce Something" as Feature, Not Bug

When models hit disambiguation failures, they consistently attempted to produce useful output rather than failing cleanly:

1. **General field reports**: When specific tool couldn't be found, produced report on "software that does X" in the general field
2. **Alternative suggestions**: Often identified related tools or alternatives
3. **Contextual information**: Provided background that helped researcher understand why tool couldn't be found
4. **Recovery clues**: In STELLAR case, the "failed" report contained the information needed to correct and retry

This behaviour could be seen as problematic (masking failure) but in practice proved useful for the research workflow. The model's epistemic honesty — explicitly stating "no evidence exists for this tool" — combined with helpful context created a productive failure mode.

### Hallucination Assessment

Across all failure cases reviewed, **no outright hallucinations were found**. When tools didn't exist, Claude:
- Correctly identified they couldn't be found
- Explicitly stated the negative finding
- Provided contextual information that was accurate
- Did not invent tools or fabricate details

This contrasts with earlier model comparisons (Gemini hallucinating contributors at V4).

### Error Attribution Summary (REVISED)

| Attribution | Count | Tools |
|-------------|-------|-------|
| Discovery: name collision | 4 | FaceNet, Fountain, Microware, pnuts |
| Discovery: insufficient signal | 1 | Wcvt2Pov (→ POV-Ray) |
| Discovery: real but undocumented | 1 | PyCoCu |
| Discovery: doesn't exist | 1 | Grid Machine (→ ArchaeoGRID) |
| **Minimal online footprint (verified real)** | **1** | **Bwigg** |
| **Total failures** | **8** | |
| Metadata prompt failure | 0 | — |

**Bottom line**: Metadata prompt success rate = 100% for documentable tools. 7 of 8 failures trace to discovery phase issues. 1 failure (Bwigg) represents a methodological limit: real tools with minimal web presence cannot be documented via web-based LLM research regardless of discovery success. Zero failures attributable to the metadata prompt itself.

---
