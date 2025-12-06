# Disambiguation Failures: Detailed Characterisation (v2)

**v2 Note (3 Dec 2025)**: This version corrects the Bwigg classification. Original analysis characterised Bwigg as "origin unknown" / "no signal" / "possible confabulation". Re-checking `tool_discovery_granular.csv` reveals Bwigg was cross-validated (found by ChatGPT DR and Perplexity DR, 3 instances total) with a specific article citation. Bwigg is therefore a verified real tool that represents a methodological limit, not a discovery failure.

---

## Overview

These failures represent cases where the metadata prompt could not produce valid output, not due to prompt design flaws, but due to problems originating in the discovery phase (ChatGPT Deep Research) or genuine intractability. The analysis reveals distinct failure patterns with different implications for understanding LLM capabilities.

---

## Failure Type A: Real but Undocumented Tool

### PyCoCu

**What it actually is**: A Python script for spatial visualisation of archaeological data from the Combe-Cullier cave site. Name derived from **Py**thon + **Co**mbe-**Cu**llier.

**Source**: Mentioned in Sécher et al. 2020, cited in SEAHORS paper (Royer et al. 2023, Peer Community Journal): "PyCoCu for Combe-Cullier (Python script; Sécher et al. 2020)"

**Why discovery found it**: ChatGPT DR correctly identified a real tool mentioned in academic literature.

**Why metadata failed**: 
- Site-specific script, not a general-purpose tool
- No public repository, documentation, or web presence
- Not indexed in open-archaeo (548+ tools) or other catalogues
- Mentioned only in passing in academic papers

**Model behaviour**: Claude searched exhaustively, correctly concluded "no evidence that PyCoCu exists as an archaeological research software tool," identified similar-sounding tools in other domains (PyCoTools, PyCoCuMa), and provided alternatives.

**Implications**: Demonstrates ChatGPT DR's genuine literature-mining capability — it found a real but extremely obscure tool that exists only as a fleeting reference in academic papers. The metadata failure is appropriate: there's nothing *to* document.

---

## Failure Type B: Name Collision with Dominant Non-Archaeological Software

### FaceNet

**What Claude found**: Google's deep learning face recognition system (2015), widely documented.

**Why it failed**: If an archaeological FaceNet exists, it's completely overshadowed by Google's tool. No archaeological application was found.

**Status**: Likely a ChatGPT DR confabulation or misattribution — possibly conflated general ML/CV tools with archaeology-specific applications.

### Microware

**What Claude found**: Microware Systems Corporation's OS-9 real-time operating system (1977-2001).

**Why it failed**: The name is completely dominated by the operating system company. No archaeological software called "Microware" exists.

**Model behaviour**: Despite explicit instruction not to ask questions, Claude initially asked for clarification (showing the strength of the disambiguation basin). When redirected, it searched exhaustively and correctly reported non-existence.

**Status**: Likely a ChatGPT DR confabulation.

### pnuts

**What Claude found**: Two distinct software:
1. Pnuts — a Java scripting language (Sun Microsystems, ~1997-2005)
2. Yahoo! PNUTS — a distributed database system

**Why it failed**: Neither has any documented archaeological application. Claude correctly identified this and provided full metadata on the Java scripting language anyway, explicitly noting "has no documented applications in archaeology, history, or historical studies disciplines."

**Model behaviour**: Produced comprehensive metadata for the *actual* software found, while explicitly flagging the absence of archaeological use cases. Provided archaeological alternatives.

**Status**: Likely ChatGPT DR error — possibly misread a citation or conflated tools.

### Fountain

**What Claude found**: Fountain the screenplay markup language/software.

**Why it failed**: The name is dominated by the screenwriting tool. No archaeological "Fountain" exists.

**Model behaviour**: Asked for disambiguation despite instructions not to — the name collision created enough uncertainty that the model broke from instruction compliance. This is actually appropriate epistemic behaviour.

**Status**: Unclear source. Chat title suggests "need disambiguation" — the run was incomplete.

---

## Failure Type C: Insufficient Signal / Genuinely Undiscoverable

### Wcvt2Pov

**What Claude found**: Nothing directly. Identified POV-Ray ecosystem as related domain.

**Why it failed**: The name suggests a converter (Wcvt = "W convert"? to POV-Ray format), but no such specific tool exists in searchable sources.

**Model behaviour**: Correctly failed, but identified POV-Ray as the likely related tool. This led to POV-Ray being added to the dataset as a valid entry.

**Status**: Possibly a historical utility that was never formally released or documented. The pattern of "split from Wcvt2Pov" for POV-Ray in the spreadsheet shows the recovery pattern working.

---

## Failure Type D: Minimal Online Footprint (Verified Real) ← NEW CATEGORY

### Bwigg

**What it actually is**: A web-based facility for Bayesian radiocarbon wiggle-matching, published in Internet Archaeology issue 13 (2003) by J. Andrés Christen.

**Discovery status**: 
- Cross-validated: found by BOTH ChatGPT Deep Research AND Perplexity Deep Research
- 3 discovery instances total
- Specific article citation found: "Bwigg: An Internet facility for Bayesian radiocarbon wiggle-matching"
- URL: https://intarch.ac.uk/journal/issue13/2/index.html

**Why metadata failed**: 
- 2003 tool with minimal web presence beyond original publication
- No repository, no recent citations, no active development footprint
- Original web facility may no longer be operational

**Why evidence failed**:
- Bwigg is the ONLY tool to fail both metadata AND evidence collection
- Even ChatGPT Deep Research (which found it during discovery) could not locate sufficient evidence for the evidence-of-life prompt

**Model behaviour**: Claude correctly reported inability to find documentation. This is appropriate given the minimal online footprint.

**Methodological significance**: 
This case demonstrates that **perfect discovery does not guarantee downstream success**. Even when discovery works optimally:
- Cross-validated across 2 independent services
- 3 separate discovery instances  
- Specific article citation found

...subsequent tasks can still fail if the tool has minimal online presence beyond its original publication. This is a genuine constraint of web-based LLM research that is **independent of model capability**. Tools from the early 2000s that were never widely adopted may simply not have enough online footprint for LLM-based research to document.

**Status**: VERIFIED REAL. Not a confabulation, not a discovery error, but a methodological limit.

---

## Summary Table (REVISED)

| Tool | Failure Type | What Exists | Archaeological Connection | Model Behaviour |
|------|--------------|-------------|---------------------------|-----------------|
| PyCoCu | A: Real but undocumented | Site-specific Python script | Yes (Combe-Cullier) | Correct failure, good alternatives |
| FaceNet | B: Name collision | Google's face recognition | None found | Correct failure |
| Microware | B: Name collision | OS-9 operating system | None found | Correct failure after redirection |
| pnuts | B: Name collision | Java scripting language | None found | Full metadata + explicit non-applicability |
| Fountain | B: Name collision | Screenplay markup | None found | Requested disambiguation |
| Wcvt2Pov | C: No signal | Nothing (POV-Ray related) | N/A | Correct failure, identified related tool |
| **Bwigg** | **D: Minimal footprint (verified real)** | **2003 IA article** | **Yes (radiocarbon)** | **Correct failure — methodological limit** |

---

## Key Findings (REVISED)

### 1. No Hallucinations in Failure Cases

Across all seven cases, Claude:
- Did not invent tools that don't exist
- Explicitly stated when tools couldn't be found
- Provided accurate context about what *was* found
- Suggested relevant alternatives

### 2. "Produce Something" Behaviour Was Helpful

When unable to find the requested tool, Claude consistently:
- Provided context about the general domain
- Identified related or alternative tools
- In the pnuts case, provided full metadata for the actual software found while flagging non-applicability

### 3. Discovery Prompt (ChatGPT DR) Was the Source of Most Errors

Six of seven failures trace back to the discovery phase:
- **PyCoCu**: Real but undocumentable (legitimate but niche)
- **Name collisions**: Likely misattributions or conflations
- **No signal**: Wcvt2Pov — possible historical utility

### 4. One Failure Represents a Methodological Limit (NEW)

**Bwigg** is NOT a discovery failure:
- Cross-validated discovery (2 services, 3 instances)
- Specific article citation found
- Verified real tool (2003 publication)

It failed downstream because **minimal online footprint makes documentation impossible via web-based methods**, regardless of model capability. This is an important finding about the limits of LLM-based research tools.

### 5. Disambiguation Requests Were Appropriate

When Claude broke from "don't ask questions" instructions (Fountain, Microware), it was responding to genuine ambiguity where proceeding would produce meaningless results. This shows appropriate judgment — prioritising accuracy over instruction compliance.

---

## Implications for Paper (REVISED)

1. **Error Attribution**: Six of seven failures should not count against the metadata prompt methodology. They demonstrate appropriate failure modes — the prompt correctly identified that it couldn't produce valid metadata.

2. **Discovery vs. Metadata**: The division of labour between prompts is working as designed. Discovery casts a wide net (with some false positives); metadata filters for documentable tools.

3. **ChatGPT DR Limitations**: The discovery prompt's failures reveal:
   - Tendency to surface obscure but real tools (PyCoCu, Bwigg)
   - Tendency to misattribute or conflate names (Microware, pnuts, Fountain)

4. **Epistemic Honesty**: Claude's consistent pattern of stating "I could not find this" rather than inventing plausible-sounding content is a significant positive finding for research applications.

5. **Methodological Limits** (NEW): The Bwigg case demonstrates that web-based LLM research has genuine constraints independent of model capability. Tools with minimal online presence — particularly older tools that were never widely adopted — may be undocumentable regardless of how well discovery performs. This should be acknowledged as a limitation of the methodology, not a model failure.

---

## Correction Log

| Original Claim | Correction | Evidence |
|----------------|------------|----------|
| "Bwigg: origin unknown" | Bwigg is a verified 2003 tool | tool_discovery_granular.csv: 3 instances, 2 services |
| "Bwigg: possible confabulation" | Specific article citation exists | IA issue 13, Christen 2003 |
| "Bwigg: Type C (no signal)" | Reclassified as Type D (minimal footprint, verified real) | Cross-validation confirms real tool |
