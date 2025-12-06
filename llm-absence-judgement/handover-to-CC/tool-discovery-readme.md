# Tool Discovery Dataset

## Overview

This dataset contains **all tools discovered** during the AI-assisted journal search phase of the research project, including both verified tools and potential hallucinations. The data was extracted from the `tool-discovery.xlsx` spreadsheet which contains the raw outputs from various LLM services and runs.

## Files

| File | Description |
|------|-------------|
| `tool_discovery_complete.xlsx` | Excel workbook with both sheets |
| `tool_discovery_summary.csv` | De-duplicated: one row per unique tool |
| `tool_discovery_granular.csv` | All instances: one row per discovery |

## Dataset Statistics

- **Total discovery instances**: 357 rows
- **Unique tools** (standardised): 246
- **Cross-validated tools** (found by 2+ services): 40
- **Hallucination risk distribution**:
  - LOW: 171 tools (from successful runs, single service)
  - LOW (cross-validated): 20 tools (found by multiple services)
  - MEDIUM: 40 tools (from failed/problematic runs)
  - HIGH: 15 tools (from "extreme fail" run - likely hallucinated)

---

## Sheet 1: Summary (De-duplicated)

One row per unique tool with aggregated information. Multi-valued fields use pipe (`|`) separators.

| Column | Description |
|--------|-------------|
| `Tool_Name_Standardised` | Canonical tool name (used for deduplication) |
| `Name_Variants` | All raw name variants found (pipe-separated) |
| `Discovery_Count` | Number of times this tool was discovered |
| `LLM_Services` | All LLM services that found this tool (pipe-separated) |
| `LLM_Services_Count` | Number of distinct services |
| `LLM_Models` | Specific models used (pipe-separated) |
| `Harnesses` | Interface types: Deep Research, Web chat, Operator, Perplexity (pipe-separated) |
| `Journals` | All source journals (pipe-separated) |
| `Journals_Count` | Number of distinct journals |
| `Run_Qualities` | Quality indicators from original runs (pipe-separated) |
| `Hallucination_Risk` | Risk assessment: HIGH, MEDIUM, LOW, LOW (cross-validated) |
| `Verification_Status` | To be filled: Verified, Hallucinated, Uncertain |
| `Sample_Article_Refs` | First 3 article titles where found |
| `Sample_URLs` | First 3 URLs/DOIs |
| `Notes` | Aggregated notes from all discoveries |

---

## Sheet 2: Granular (All Instances)

One row per discovery instance, preserving full provenance.

| Column | Description |
|--------|-------------|
| `Tool_Name_Raw` | Original tool name as extracted |
| `Tool_Name_Standardised` | Canonical name for joining to summary |
| `LLM_Service` | Which AI service discovered this tool |
| `LLM_Model` | Specific model (o3, Operator, Deep Research, etc.) |
| `Harness` | Interface type used |
| `Run_Quality` | Quality indicator from original spreadsheet |
| `Journal` | Source journal searched |
| `Article_Title` | Title of the article where tool was mentioned |
| `Article_Authors` | Authors of the source article |
| `Issue_Number` | Journal issue number |
| `Year` | Publication year |
| `URL_DOI` | Link to the source article |
| `Discovery_Context` | "Primary" (paper's subject) or "Mentioned" (passing reference) |
| `Sheet_Name` | Original spreadsheet sheet name |
| `Additional_Notes` | Notes about this specific discovery |

---

## LLM Services

| Service | Discoveries | Description |
|---------|-------------|-------------|
| ChatGPT Deep Research | 294 | OpenAI's Deep Research feature (web interface) |
| OpenAI o3 | 48 | OpenAI's o3 model via web chat |
| Perplexity Deep Research | 9 | Perplexity's research mode |
| OpenAI Operator | 6 | OpenAI's browser agent |

## Harnesses (Interfaces)

| Harness | Discoveries | Description |
|---------|-------------|-------------|
| Deep Research (web) | 294 | OpenAI's autonomous research mode |
| Web chat (o3) | 48 | Standard chat with o3 model |
| Perplexity (web) | 9 | Perplexity's web interface |
| Operator (browser agent) | 6 | Autonomous browser navigation |

## Journals Searched

| Journal | Discoveries |
|---------|-------------|
| Internet Archaeology | 165 |
| JOSS (Journal of Open Source Software) | 117 |
| JOAD (Journal of Open Archaeology Data) | 21 |
| JCAA (Journal of Computer Applications in Archaeology) | 19 |
| SoftwareX | 16 |
| Multiple (sample runs) | 19 |

## Run Quality Indicators

| Run Quality | Count | Risk Assessment |
|-------------|-------|-----------------|
| success | 145 | LOW |
| success-secondpass | 54 | LOW |
| fail-possible | 34 | MEDIUM |
| worthless | 29 | MEDIUM |
| standard | 22 | LOW |
| fail | 20 | MEDIUM |
| access-fail | 16 | MEDIUM |
| extreme fail | 15 | HIGH |
| sample | 10 | LOW |
| synthetic-prompt | 9 | LOW |

## Cross-Validation

Tools found by multiple LLM services have stronger evidence of being real:

**Found by 3 services (strongest evidence):**
- Arch-I-Scan: ChatGPT DR + o3 + Perplexity
- stratigraphr: ChatGPT DR + o3 + Perplexity
- SAGAscape: ChatGPT DR + o3 + Perplexity

**Found by 2 services (40 tools total):**
Including: ARCHIS, ArchAIDE, Gephi, ArcGIS, ArchaeoPhases, iDig, shoredate, tabula, Archeofrag, Bwigg, Mask R-CNN, PyLithics, aion, archeoViz, c14bazAAR, Heurist, TensorFlow, and others.

## HIGH RISK Tools (Likely Hallucinations)

The following 15 tools were discovered in the JOAD "extreme fail" run and have a HIGH likelihood of being hallucinated. All have suspiciously generic names:

1. time2aoristic
2. GeoViz
3. CeramicNet
4. ArtifactML
5. DeepClass
6. Reconstructo
7. VRArchaeo
8. LandML
9. DataArq
10. MapCrowd
11. FieldStream
12. ImageQuant
13. BigArq
14. DataMiner
15. 3DArq

These should be verified before inclusion in any analysis.

## Special Marker Entries

The granular dataset includes marker entries for:
- `[FALSE POSITIVE MARKER]` - Items marked as false positives in original data
- `[FALSE NEGATIVE MARKER]` - Items where tools were briefly mentioned but not captured
- `[DATA ARTICLE - tools unclear]` - Data articles where specific tools could not be identified

These markers are excluded from the summary sheet.

## Next Steps

1. **Verification**: Each tool needs to be verified as real or hallucinated
2. **Canonicalisation**: Review name variants and standardise (e.g., "Photomodeller" vs "Photomodeler")
3. **Cross-reference**: Compare with OpenArchaeo baseline to identify overlap and unique discoveries
4. **Update Verification_Status**: Fill in the empty column with verification results

## Source

Extracted from: `tool-discovery.xlsx`
Extraction date: December 2025