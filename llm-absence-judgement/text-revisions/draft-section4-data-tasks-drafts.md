# DRAFT: Section 4 Data Task Findings (UPDATED)

**Update Notes:**
- Bwigg reclassified from "insufficient documentation" to "verified real, minimal online footprint" (new failure category)
- Evidence numbers flagged for verification (discrepancy between spreadsheet versions)
- Failure taxonomy updated to reflect methodological limitations distinct from discovery errors

---

## 4.X Tool Discovery

Our tool discovery methodology identified 91 software tools through systematic journal searching, compared against an OpenArchaeo baseline of 376 tools. Only 19 tools (21%) appeared in both sources, suggesting substantial complementarity between our journal-focused approach and OpenArchaeo's community-contributed repository. The remaining 72 tools represent potential new discoveries not catalogued in the existing baseline, though verification of these additions required downstream metadata collection.

### Journal-by-Journal Performance

Internet Archaeology proved the most productive source, with 97 tools extracted from 674 articles in a successful Deep Research run. The Journal of Open Source Software presented a revealing contrast between model capabilities: an initial run using o3 produced 29 tool entries but was deemed unusable, while a subsequent Deep Research run yielded 16 verified tools with complete metadata.

[TABLE: Journal performance summary]
| Journal | Articles | Tools Found | Model | Outcome |
|---------|----------|-------------|-------|---------|
| Internet Archaeology (run 2) | 674 | 97 | Deep Research | Success |
| JOSS (secondpass) | 16 | 16 | Deep Research | Success |
| JOSS (initial) | 29 | 29 | o3 | Unusable |
| JOAD | 40 | 13 | Deep Research | Extreme fail (fabrication) |
| IA issues 31-67 | 200 | 18 | Deep Research | Failed |
| SoftwareX (run 1) | -- | -- | Deep Research | Access failure |

### Failure Modes in Discovery

The o3 JOSS run exemplifies characteristic discovery failures. Although it produced outputs for all 29 articles examined — a superficially impressive 100% hit rate — systematic review revealed fundamental problems. All author fields were empty (NaN values), and manual URL verification indicated that many did not resolve to actual JOSS papers. More concerning, several tool names appeared to be confabulations: plausible-sounding combinations that match the naming patterns of real tools but do not correspond to actual software.

For example, "archr: Automated Radiocarbon Chronology for R (pilot)" follows the naming convention of legitimate archaeology R packages (cf. archdata, archeofrag, archeoViz) and describes a plausible function — yet web searches confirm that no such package exists. Searching for "archr R package archaeology" returns ArchR (a bioinformatics package for single-cell analysis), archdata (archaeological datasets for R teaching), and archeofrag (fragmentation analysis) — but no "archr" for radiocarbon chronology. The model appears to have generated a statistically likely tool name by combining "arch" (archaeology) with "r" (the R language), complete with a realistic-sounding subtitle. This represents confabulation at the semantic level: not random noise but plausible-seeming outputs that lack correspondence to reality.

By contrast, the successful JOSS "secondpass" run using Deep Research produced 16 tools with verified author names (e.g., "Nicolas Frerebeau", "Sébastien Plutniak") and accurate URLs. The difference in output quality between these runs — identical journal, similar task scope, different model — illustrates both the variance in model performance and the critical importance of metadata completeness as a quality signal.

The Internet Archaeology issues 31-67 failure demonstrates a different pattern: the model produced outputs that included (a) issues with no tools listed, (b) no discrimination between domain-specific tools and generic technologies like ActiveX, and (c) apparent underextraction compared to the successful run. Where the earlier run found 97 tools in 674 articles, the failed run found only 18 tools in 200 articles despite covering issues known to discuss software extensively.

### The JOAD "Extreme Fail": Wholesale Fabrication

The Journal of Open Archaeology Data run provides the most striking example of discovery failure. Of 40 entries produced, analysis reveals a clear break between legitimate and fabricated content.

Entries 1-24 appear to be real JOAD articles with accurate titles and DOIs. Critically, most show no tools mentioned — which is **correct**, since JOAD is a data journal that publishes data papers rather than software descriptions. The model appropriately found few tools in early entries because few tools exist in JOAD's scope.

Entries 26-40, however, are wholesale fabrications. Both article titles and tool names were invented:

| Entry | Fabricated Title | Fabricated Tool(s) |
|-------|------------------|-------------------|
| 26 | "Open Source Analysis of Ceramic Trade Networks" | CeramicNet |
| 27 | "Automated Artifact Classification Using Machine Learning" | ArtifactML; DeepClass |
| 28 | "Digital Reconstruction of Ancient Settlements" | Reconstructo |
| 29 | "Virtual Reality in Archaeology: Case Studies..." | VRArchaeo |
| 31 | "Integrating GIS and Machine Learning for Landscape Archaeology" | LandML |
| ... | ... | ... |

The fabricated tool names follow plausible naming conventions — CeramicNet, DataArq, MapCrowd, FieldStream, ImageQuant, BigArq, 3DArq — that match patterns in real archaeological software. More insidiously, the fabricated articles use real DOI patterns (joad.100, joad.101, joad.110...). Cross-referencing confirms that DOI joad.90, listed in entry 25, corresponds to a real article about "Near East Radiocarbon Dates (NERD)" — not "Geoarchaeological Data from the Mediterranean" with "GeoViz" as claimed.

This represents a qualitatively different failure mode from simple confabulation. Rather than inventing a plausible-sounding tool name when uncertain, the model fabricated entire articles and tools to populate expected output fields when it found that the source journal contained fewer software descriptions than anticipated. The fabrications are internally consistent — each fake article has a matching fake tool — but entirely disconnected from reality.

### Discovery Verification and Confabulation Rates

Cross-referencing discovered tools against metadata collection outcomes provides a verification rate for "new" discoveries. Of 71 tools discovered that did not appear in OpenArchaeo:
- 43 (61%) successfully passed metadata verification — confirmed real tools
- 28 (39%) did not pass verification

Of the 28 unverified tools, eight are documented failures from metadata collection:
- 4 name collisions (FaceNet, Fountain, Microware, pnuts)
- 1 insufficient documentation (Wcvt2Pov)
- 1 no online presence (PyCoCu)
- 1 confabulated name (Grid Machine → serendipitously led to ArchaeoGRID)
- 1 minimal online footprint (Bwigg — see methodological note below)

The remaining 20 tools (including Agisoft PhotoScan, Depthmap, GvSIG CE, VOSviewer) were either not prioritised for metadata collection or represent additional verification failures. Some may be legitimate tools that simply weren't investigated given resource constraints; others may represent confabulations or inappropriate inclusions (generic software like VOSviewer appearing in archaeological literature but not archaeology-specific).

This ~60% verification rate for "new" discoveries indicates that while the discovery process successfully identified many tools not in existing repositories, substantial human verification remains essential. The 8 documented failures represent clear model errors (confabulation, name collision) or methodological limitations (minimal online footprint), while the status of the remaining 20 would require further investigation to characterise.

### Chimeric Confabulation: The Perplexity SAGAscape Example

A distinct failure mode appeared in Perplexity Deep Research output: chimeric confabulation, where the model combined real facts from unrelated tools to produce a plausible but fabricated entry. When asked to collect metadata for SAGAscape, Perplexity produced:

| Field | Claimed Value | Reality |
|-------|---------------|---------|
| Earliest Mention | 2005 (Cologne) | 2022 (Belgium/Turkey collaboration) |
| Repository URL | gitlab.com/sagascape/sagascape-core | Does not exist |
| First Commit | 2006-09-01 | Impossible — tool created in 2022 |
| Latest Release | v8.3.2 | Appears to be SAGA GIS version number |

SAGAscape is real: it is an agent-based model published in the Journal of Computer Applications in Archaeology in 2022 by Boogers and Daems, written in NetLogo for simulating resource exploitation in the Sagalassos region of Turkey. However, Perplexity appears to have confused it with SAGA GIS (System for Automated Geoscientific Analyses), a general-purpose GIS platform established around 2004. The model combined characteristics from both tools — the name SAGAscape, Cologne associations from SAGA GIS, plausible but non-existent repository URLs, and version numbers from the unrelated software — into a single fabricated entry.

This chimeric confabulation differs from wholesale fabrication (inventing tools entirely) or simple confabulation (inventing plausible names). Here, the model assembled real facts into a false composite, producing output that superficially checks out — the tool name is real, the dates are plausible, the version number format is correct — while being fundamentally disconnected from the actual tool it purports to describe.

### Discovery Confabulation Taxonomy

The discovery failures documented above reveal four distinct confabulation types, each requiring different verification approaches:

| Type | Description | Example | Detection Method |
|------|-------------|---------|------------------|
| **Simple confabulation** | Plausible-sounding names that don't exist | archr R package | Web search, package registry check |
| **Wholesale fabrication** | Entire articles AND tools invented together | JOAD entries 26-40 (CeramicNet, ArtifactML) | DOI verification, journal issue checking |
| **Chimeric confabulation** | Real facts from unrelated tools combined | SAGAscape + SAGA GIS | Cross-reference with authoritative source |
| **DOI hijacking** | Real DOI with fabricated content | joad.90 → fake "GeoViz" | Direct DOI resolution |

The wholesale fabrication pattern is particularly concerning: it demonstrates that models may generate internally consistent outputs (each fake article matched with a fake tool) that satisfy format requirements while being entirely disconnected from reality. This supports the technoscholasticism thesis: models privilege the form of research outputs over correspondence with the world they purport to describe.

---

## 4.Y Metadata Collection

Metadata collection produced complete records for 89 of 97 tools investigated (92% success rate). All eight failures traced to upstream discovery issues or methodological limitations rather than metadata prompt failures, yielding a 100% success rate when given a documentable tool with adequate online presence.

### Failure Taxonomy

| Failure Type | Count | Examples | Attribution |
|--------------|-------|----------|-------------|
| Name collisions | 4 | FaceNet, Fountain, Microware, pnuts | Discovery error |
| Insufficient documentation | 1 | Wcvt2Pov | Discovery error |
| No online presence | 1 | PyCoCu | Discovery error |
| Confabulated tool name | 1 | Grid Machine → led to ArchaeoGRID | Discovery error |
| Minimal online footprint | 1 | Bwigg | Methodological limitation |
| **Total failures** | **8** | | |
| **Metadata prompt failures** | **0** | | |

**Methodological Note on Bwigg:** Unlike other failures, Bwigg represents a verified real tool — a Bayesian radiocarbon wiggle-matching program developed by J. Andrés Christen and published in *Radiocarbon* in 2003. The tool was cross-validated during discovery (found by 2 services across 3 instances in Internet Archaeology issue 13). However, both metadata AND evidence collection failed due to minimal online footprint beyond the original publication. This is not a model failure but a constraint of web-based LLM research for early 2000s tools that predate widespread version control adoption and online documentation practices. The tool exists but cannot be adequately documented through contemporary web search.

The name collision category proved particularly instructive. When asked to collect metadata for "FaceNet" (identified during tool discovery from an archaeological context), Claude Research returned detailed information about Google's facial recognition neural network — technically accurate but entirely wrong for the task. Similar collisions occurred with common words that happened to match software projects in other domains.

### Model Selection and Elimination

We tested three services for metadata collection: Claude Research, Google Gemini 2.5 Pro, and ChatGPT Deep Research. Claude Research was retained for production based on output quality.

**Gemini's version confusion**: When tested on FAIMS (a tool for which the authors possess ground truth), Gemini systematically conflated features across software versions. For example:
- Claimed PostgreSQL as the database backend (incorrect — old FAIMS used SQLite; new FAIMS uses CouchDB)
- Stated "Android-only client" (incorrect for new FAIMS, which is cross-platform)
- Claimed the software "requires server setup and maintenance" (incorrect for new FAIMS)
- Described CSV and JSON export capabilities mixing features from different versions without specifying which version was relevant

Many fields stated facts about either old FAIMS or new FAIMS without distinguishing between them, despite the prompt explicitly requesting information about FAIMS 3.0. Key personnel were partly confabulated. This version confusion persisted across multiple prompt refinements.

**ChatGPT Deep Research limitations**: Outputs showed less detail than Claude and exhibited similar version confusion. For example, on FAIMS:
- Claude produced: "Fully operational offline functionality allowing work in remote areas without connectivity; Multi-user synchronization capability enabling team collaboration; Comprehensive customization options through a web-based notebook designer; Strong focus on data integrity and provenance tracking..."
- ChatGPT DR produced: "Offline-first design; highly customisable notebook designer; cross-platform builds; strong audit trail; permissive code reuse"

While technically accurate, ChatGPT's outputs lacked the depth required for comprehensive metadata records. No discussion of evolution appeared in the technical-discussion field, where Claude provided version history context.

**Claude's CSV limitation**: Despite numerous prompt refinements, Claude Research never produced CSV output within the research phase, always requiring a follow-up prompt to convert its narrative report into structured data. This introduced an additional manual step into every metadata collection run and represents a persistent format compliance failure that could not be resolved through prompt engineering.

### Output Quality Assessment

We assessed metadata quality using the slop taxonomy from Shaib et al. (2025). A sample of ten entries including expert-validated ground truth showed:
- 2 entries with "None" (no detectable slop)  
- 8 entries with "Minimal" slop
- 0 entries with "Moderate" or higher slop levels
- Mean information density: 1.9 anchored claims per 100 words
- Mean word count: 678 words per entry

The high information density and low slop levels indicate that when metadata collection succeeded, outputs were substantive rather than padded. The 8/10 "Minimal" slop entries typically contained one or two generic phrases ("continues to be developed") without specific attribution rather than systematic quality problems.

---

## 4.Z Evidence of Life Collection

**[VERIFICATION NEEDED: Evidence numbers]** Two versions of the evidence dataset exist with different totals:
- Earlier version (tool-evidence__1_.xlsx): 1,874 rows, 105 tools
- Reconciled version (tool-evidence__4_.xlsx): 1,179 rows, 125 tools

The reconciled version (125 tools, 1,179 rows) appears to be the deduplicated dataset combining Discovery pathway (96 tools, 965 rows) and OpenArchaeo no-DVC pathway (29 tools, 214 rows). The following uses these reconciled figures pending final verification.

Evidence collection produced 1,179 dated references for 125 tools, documenting the temporal footprint of each software tool through citations, releases, commits, and other datable mentions. ChatGPT Deep Research generated the majority of evidence rows, with separate collection runs for Discovery pathway tools and OpenArchaeo tools lacking version control repositories.

### Prompt Evolution

The evidence prompt underwent radical simplification between versions. Version 1 specified a complex 15-column synthesis format requiring the model to calculate aggregate metrics (commit counts, contributor numbers, release tags) and produce a single row per tool. This approach consistently failed: models either refused the task or produced heavily confabulated synthesis.

Version 5 inverted the approach entirely, reducing output to 5 columns (Tool, Year, Source, URL, AI Notes) with one row per source and explicit prohibition of synthesis. By delegating all inference to human researchers, this design achieved reliable outputs. Version 7 added instructions to exclude AI citation artifacts (the【deep research】and contentReference[oaicite markers that sometimes leaked into outputs).

The key epistemic guardrail appearing across all successful versions: "ABOVE ALL ELSE, if you are unsure... do not make a claim. If there is any doubt, there is no doubt."

### Model Testing and Selection

Model testing on FAIMS, where authors possessed complete ground truth, revealed characteristic failure patterns across services:

**Claude Research** fragmented FAIMS into four separate tool entries: FAIMS, FAIMS Mobile Platform, FAIMS 3.0, and Fieldmark. While each entry contained accurate information, the fragmentation broke data aggregation — a researcher could not easily determine the complete evidence history for the tool without manual reconciliation. Similar naming fragmentation occurred with other tools exhibiting version variants.

**Gemini** treated Wayback Machine snapshots as separate annual "sources," producing inflated row counts that mostly duplicated the same webpage across different capture years. This inflated evidence counts without providing new information. **[ASK BRIAN: Specific row count from Wayback duplication?]**

**ChatGPT Deep Research** with o3 produced the highest-quality notes, explicitly classifying source types (e.g., "academic paper", "GitHub repository", "project website") and noting verification status. This service was selected for production based on evidence yield: Claude and other services simply returned fewer valid evidence rows for the same tool sets.

### The ArboDat Temporal Blindness Example

A revealing failure occurred during evidence collection for ArboDat, an OpenArchaeo tool without version control. The model found and accessed the tool's homepage, which contains the plain-English statement that the software "has been developed since 1997." Despite this explicit temporal marker, the model extracted a different date — apparently from page metadata (a copyright notice or "last updated" timestamp from 2024) — and presented this as the software's development date.

This failure demonstrates the distinction between finding information and understanding it. The model successfully located the authoritative source, read the page contents, and produced an output with a date and URL. Yet it failed to recognise which date on the page was semantically relevant to the query. A human researcher would immediately privilege the "developed since 1997" statement over incidental page metadata; the model lacked the judgment to make this distinction.

### Coverage and Limitations

The evidence collection spans 125 tools across two pathways:
- **Discovery pathway**: 96 tools, 965 evidence rows
- **OpenArchaeo no-DVC pathway**: 29 tools, 214 evidence rows

Tools with active GitHub repositories typically produced 20-30 evidence rows spanning commits, releases, and academic citations. Tools without version control relied on literature searching, typically producing 5-10 evidence rows.

Division of labour emerged organically: Brian worked alphabetically from A→, Shawn worked ←Z, with the split reflecting different tool familiarity and availability during the collection period. **[VERIFY: Contribution counts against reconciled dataset]**

---

## Cross-Task Synthesis [FOR DISCUSSION SECTION]

[Note: The following patterns should move to Discussion, not Findings]

The three data tasks reveal consistent patterns in model capabilities and limitations:

1. **Scope-quality tradeoff**: Narrow, well-bounded tasks (single tool metadata, single-source evidence) succeeded; broad tasks (journal-wide discovery, synthesised timelines) failed or produced unreliable outputs.

2. **Format compliance as quality signal**: Missing metadata (NaN authors in JOSS o3), format refusal (Claude's narrative-not-CSV), and structural violations consistently indicated deeper quality problems.

3. **Production service differentiation**: Despite testing multiple services, each task converged on a different production model — ChatGPT DR for discovery and evidence, Claude Research for metadata — suggesting no single model excels across research task types.

4. **Upstream vs downstream failures**: Metadata and evidence failures primarily traced to discovery-phase problems (confabulated or collision tool names), not to failures in the metadata/evidence prompts themselves. The Bwigg case reveals a distinct category: real tools that cannot be documented through web-based methods due to minimal online footprint.

---

## Questions Requiring Clarification

### For Brian:
1. ~~Why was JOAD labelled "extreme fail" — what specifically failed?~~ **RESOLVED**: Wholesale fabrication of entries 26-40
2. Gemini snapshot count: how many rows from Wayback duplication?
3. Claude evidence elimination: roughly how many fewer rows vs ChatGPT DR?
4. Deep Research session count: total runs for evidence collection (order of magnitude)?
5. ~~861/302 row split — deliberate division or organic?~~ **RESOLVED**: Organic; Brian worked A→, Shawn worked ←Z
6. **NEW**: Which evidence spreadsheet version is canonical? (1,874/105 vs 1,179/125)

### Resolved Through Analysis:
- ~~Cross-reference 72 "new" tools against metadata results~~ **DONE**: 61% verification rate (43/71)
- ~~Confirm SoftwareX chat transcript findings~~ **DONE**: Vibes-based output pattern confirmed
- ~~Bwigg classification~~ **RESOLVED**: Verified real (Christen 2003), minimal online footprint — methodological limitation, not discovery error

---

## Change Log

**December 2025 Update:**
1. Bwigg reclassified from "insufficient documentation" (implying discovery error) to "minimal online footprint" (methodological limitation of web-based LLM research)
2. Added new failure category in taxonomy: "Minimal online footprint" distinct from discovery errors
3. Added methodological note explaining Bwigg as verified real tool (Bayesian wiggle-matching, Christen 2003) that cannot be documented through contemporary web search
4. Flagged evidence number discrepancy for verification (1,874/105 vs 1,179/125)
5. Updated JOAD row to reflect "Extreme fail (fabrication)" outcome
6. Added question about canonical evidence spreadsheet version
