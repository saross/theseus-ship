# Success Analysis: Characterising Effective AI Research Tool Outputs

## Executive Summary

Analysis of successful discovery, metadata, and evidence collection runs reveals consistent patterns that distinguish reliable outputs from failures. Success correlates strongly with: (1) complete metadata fields, (2) appropriate yield proportions, (3) diverse authoritative sources, and (4) model-task matching. Understanding these patterns provides practical guidance for deploying AI research tools effectively.

---

## 1. Discovery Success Patterns

### 1.1 Internet Archaeology Run 2: The Benchmark Success

**Metrics:**
- 674 articles examined
- 97 articles with tools (14.4% yield)
- 131 unique tools identified across 145 mentions
- 100% metadata field completeness

**What Made It Work:**

1. **Realistic Yield**: Only 14.4% of articles mentioned software tools â€” appropriate for a general archaeology journal. The model correctly identified that most articles don't discuss software, avoiding the temptation to fabricate tools to fill expected output slots.

2. **Complete Metadata**: Every row had Title, Authors, URL, Issue Number, Year, and Tools Mentioned (or explicit null). Zero NaN values in core fields.

3. **Appropriate Scope Discrimination**: The model correctly included:
   - Domain-specific tools: BCal, ArchEd, Stratigraph, FAIMS, Intrasis
   - Period-appropriate generic technologies: VRML, QuickTime VR (relevant for 1990s-2000s web archaeology articles)
   
4. **Multi-Tool Recognition**: Articles mentioning multiple tools had them correctly separated by semicolons (e.g., "Vistapro; Vistamorph; Photomodeller; Fountain (VRML tool); Pioneer; Pioneer Pro")

**Residual Issues Within Success:**
- Some generic technologies included (ActiveX, PowerPoint) â€” borderline but justifiable in historical context
- 14 potentially generic technologies among 131 tools (10.7%) â€” acceptable noise level

### 1.2 JOSS Secondpass: Quality Over Quantity

**Metrics:**
- 16 tools found (vs 29 in failed o3 run)
- 100% metadata completeness
- 100% verified real tools

**What Made It Work:**

1. **Rich Cross-Referencing**: Each entry included related tools mentioned in the paper, e.g.:
   - "aion" entry also listed: Bchron, rcarbon, Luminescence, ArchaeoPhases, shoredate, kairos
   - This demonstrates the model actually read and understood the papers

2. **Real Author Names**: Nicolas Frerebeau, SÃ©bastien Plutniak, Clemens Schmid â€” all verified researchers in computational archaeology

3. **Valid URLs**: All URLs resolved to actual JOSS papers with correct DOIs

4. **Appropriate Selectivity**: Found fewer tools than the failed run but with zero confabulations. The model exercised judgment about what counted as an archaeology/historical sciences tool.

**Key Contrast with Failure (JOSS-worthless-o3):**

| Metric | Success (secondpass) | Failure (o3) |
|--------|---------------------|--------------|
| Entries | 16 | 29 |
| Authors populated | 100% | 0% |
| Confabulated tools | 0 | â‰¥1 (archr confirmed) |
| Cross-references | Yes (related tools listed) | No |
| Model | Deep Research | o3 |

**Lesson**: Fewer entries with complete metadata > more entries with missing fields. Empty author fields signal broader quality problems.

### 1.3 SoftwareX Run 1: Success Despite "Access Fail" Label

**Metrics:**
- 12 tools found
- 100% metadata completeness
- Tools span 2015-2023

**What Made It Work:**

1. **Focused Domain Selection**: Every tool has clear archaeology/historical sciences relevance:
   - CAinterprTools (Correspondence Analysis in archaeology)
   - FAIMS Mobile (field data capture)
   - movecost (least-cost path analysis)
   - Cloud2FEM (heritage building point clouds)

2. **Contextual Notes**: Tools Mentioned field includes brief justifications:
   - "MICA (curve alignment software, used in dendrochronology for historical wood analysis)"
   - "ringR (R package for dendrochronology; relevant to historical sciences but lacks direct archaeology mention)"

3. **Appropriate Uncertainty Flagging**: Entry 10 notes: "Hyperspectral Image Analysis Toolbox (used for historic document analysis, but archaeological applications unclear)"

**Note on Label**: The "accessFail" likely refers to access issues during the run (ScienceDirect paywall?), not output quality. The data itself is high quality.

---

## 2. Evidence Collection Success Patterns

### 2.1 Combined Evidence Dataset

**Metrics:**
- 1,874 evidence rows
- 105 unique tools
- 95% from OpenAI Deep Research
- 95.1% AI_Notes completeness

**Source Distribution (Top Domains):**

| Domain | Count | Source Type |
|--------|-------|-------------|
| doi.org | 165 | Peer-reviewed publications |
| cran.r-project.org | 147 | R package repository |
| github.com | 116 | Version control |
| intarch.ac.uk | 77 | Journal archive |
| joss.theoj.org | 36 | Software journal |
| zenodo.org | 20 | Data/software repository |

**What Made It Work:**

1. **Diverse Authoritative Sources**: Evidence drawn from academic publications (doi.org), code repositories (GitHub, CRAN), institutional sites (cambridge.org, historicengland.org.uk), and specialised archives (archaeologydataservice.ac.uk)

2. **Appropriate Evidence Density**: Well-documented tools have 20-106 evidence rows; obscure tools have 2-4. This reflects reality rather than artificial padding.

3. **Temporal Spread**: Evidence spans 1996-2025, with appropriate concentration in recent years (2018-2024 = ~45% of rows)

4. **Explicit Dating in Notes**: High-quality entries include explicit temporal markers:
   - "Earliest archived version in CRAN. Date from CRAN archive"
   - "Official UNSW news release announcing the FAIMS project (Published 24 Jul 2012)"

**Residual Issues Within Success:**

1. **Citation Artifact Leakage**: 698 entries (37%) contain `contentReference[oaicite` markers â€” the AI citation artifacts that leaked despite prompt instructions. These don't invalidate the data but require cleaning.

2. **Duplicate Entries**: FAIMS 2012 and 2013 entries appear twice (likely from overlapping runs). Deduplication needed.

3. **Non-Standard Years**: 266 entries (14%) marked "n.d." for no date â€” appropriate for undated web pages but requires handling.

### 2.2 Evidence Quality by Tool Type

**Well-Documented Tools (dplR example â€” 106 rows):**
- CRAN archive releases tracked granularly (1.0.1, 1.0.2, 1.0.3...)
- Academic citations from multiple venues
- GitHub activity documented
- Clear version history

**Ground Truth Tool (FAIMS â€” 34 rows):**
- Correct identification of key dates (2012 launch, 2018 SoftwareX paper)
- Multiple source types (news releases, conference papers, project websites)
- Minor duplication issue but core facts accurate

**Minimal Evidence Tools (htmlfig â€” 2 rows):**
- Both from 1997 Internet Archaeology
- Notes are NaN (no additional context)
- Represents legitimate obscurity rather than collection failure

---

## 3. Metadata Collection Success Patterns

### 3.1 Tool Master List

**Metrics:**
- 129 total entries
- 97 tools with complete metadata
- 89 with full description/history fields (69%)

**What Made Claude Research Work:**

1. **Rich Contextual Detail**: FAIMS entry included:
   - "Fully operational offline functionality allowing work in remote areas without connectivity"
   - "Multi-user synchronization capability enabling team collaboration"
   - "Comprehensive customization options through a web-based notebook designer"
   
2. **Version-Aware History**: History fields distinguish between major versions and their capabilities

3. **Appropriate Technical Depth**: Technical-discussion fields include:
   - Database backends
   - Platform requirements
   - Integration capabilities

**Field Completeness Analysis:**

| Field Category | Completeness | Notes |
|---------------|--------------|-------|
| Core descriptive (Description, History) | 69% | Complete for all investigated tools |
| Technical (DVCS-repo, CRAN, PyPi) | 4-42% | Appropriately sparse â€” not all tools have these |
| Analytical (Strengths, Weaknesses, Survivability) | ~69% | Present for investigated tools |

---

## 4. Cross-Cutting Success Factors

### 4.1 Complete Metadata as Quality Signal

Across all successful runs, core metadata fields were 100% populated. Missing fields (particularly Authors in discovery, AI_Notes in evidence) reliably predicted other quality problems.

**Practical Implication**: Check metadata completeness before trusting content. If Authors=NaN, investigate further before using.

### 4.2 Appropriate Yield Proportions

Successful runs showed realistic extraction rates:
- IA discovery: 14.4% of articles had tools (realistic for general journal)
- JOSS secondpass: 16 tools (quality-filtered from larger potential set)
- Evidence: 4-106 rows per tool (reflecting actual documentation availability)

**Contrast with Failures**: JOAD fabrication occurred when model tried to populate expected output slots for a journal with fewer relevant articles than expected.

### 4.3 Model-Task Matching

| Task | Best Model | Key Strength |
|------|-----------|--------------|
| Discovery | Deep Research | Persistent web searching, handles large corpus |
| Metadata | Claude Research | Rich contextual detail, version awareness |
| Evidence | ChatGPT DR + o3 | Explicit source classification, temporal markers |

No single model excelled at all tasks. Success required matching model capabilities to task demands.

### 4.4 Prompt Constraints

Evidence collection success required:
- Simple output format (5 columns, not 15)
- One row per source (not synthesised)
- Explicit prohibition of synthesis
- "If unsure, do not make a claim" epistemic guardrail

Discovery success worked with relatively standard prompts but required iteration to achieve appropriate selectivity.

---

## 5. The Success/Failure Boundary

### 5.1 What Distinguishes Success from Failure

| Factor | Success Pattern | Failure Pattern |
|--------|-----------------|-----------------|
| Metadata completeness | 100% core fields | NaN in authors, URLs |
| Yield | Realistic proportions | Either too many (fabrication) or too few (underextraction) |
| Tool types | Domain-specific with justified generics | Undiscriminated generic inclusion |
| Source diversity | Multiple authoritative domains | Single source or fabricated |
| Model selection | Deep Research for discovery/evidence, Claude for metadata | o3 for discovery, any model for synthesis tasks |

### 5.2 The Judgment Boundary

Even successful runs show judgment limitations:
- Cannot distinguish "appropriate generic technology in historical context" from "inappropriate generic inclusion"
- Cannot synthesise across sources (attempts produce confabulation)
- Cannot exercise taste in source selection (includes all found sources rather than most authoritative)

**Key Insight**: Success occurs when tasks are structured to avoid requiring judgment. The model succeeds at:
- Finding sources (given clear search terms)
- Extracting metadata (given specific fields)
- Reporting what it found (given simple output format)

The model fails when asked to:
- Evaluate source quality
- Synthesise across contradictory sources
- Decide what's relevant vs irrelevant
- Infer from absence

---

## 6. Practical Recommendations from Success Patterns

### 6.1 Discovery Tasks
- Use Deep Research, not base models
- Accept realistic yield (not every article has tools)
- Check author field completeness as quality signal
- Expect 10-15% generic technology inclusion as acceptable noise

### 6.2 Evidence Tasks
- Use simple output format (â‰¤5 columns)
- One row per source, no synthesis
- Include "if unsure, do not claim" instruction
- Budget for 37% citation artifact cleaning
- Expect 14% undated entries

### 6.3 Metadata Tasks
- Use Claude Research for depth
- Expect CSV conversion as separate step
- Provide specific metadata template
- Scope to 1-3 tools per prompt for quality

### 6.4 General Principles
- Match model to task type
- Structure tasks to avoid requiring judgment
- Use metadata completeness as quality signal
- Accept appropriate incompleteness (not everything has a GitHub repo)
- Verify a sample before trusting full output

---

*Analysis based on systematic examination of tool-discovery.xlsx and tool-evidence__1_.xlsx success sheets. Compiled December 2025.*