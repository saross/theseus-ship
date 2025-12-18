# Enhanced Section 4 Data Collection Subsections

These subsections are drafted for integration into AbsenceJudgement.tex, following the Model→Task organisation. Each subsection corresponds to the "Data Collection and Extraction" component for the respective lab.

---

## 4.2.3 OpenAI: Data Collection and Extraction (Enhanced)

[Note: This expands the existing OpenAI subsection with quantitative tool discovery and evidence collection data]

OpenAI's Deep Research demonstrated the highest persistence among tested services for data collection tasks, ultimately producing 95% of evidence rows in our combined dataset. This success, however, required extensive prompt engineering and came with characteristic failure patterns that illuminate the distinction between information accumulation and research judgment.

### Tool Discovery Performance

Our tool discovery methodology employed Deep Research to systematically search six archaeology and digital humanities journals for software tool mentions. Across successful runs, the service identified 91 tools compared against an OpenArchaeo baseline of 376 tools. Only 19 tools (21%) appeared in both sources, suggesting substantial complementarity between our journal-focused approach and the community-contributed repository. The remaining 72 tools represented potential new discoveries, though downstream verification reduced this figure considerably.

Internet Archaeology proved the most productive source, with Deep Research extracting 97 tools from 674 articles in a successful run—a 14.4% yield appropriate for a general archaeology journal where most articles do not discuss software. The Journal of Open Source Software presented a revealing contrast: an initial run using o3 produced 29 entries deemed unusable, while a subsequent Deep Research run yielded 16 verified tools with complete metadata. The difference between these runs—identical journal, similar task scope, different model—illustrated both variance in model performance and the critical importance of metadata completeness as a quality signal.

The o3 JOSS run exemplified characteristic discovery failures. Although it produced outputs for all 29 articles examined, systematic review revealed that all author fields were empty (NaN values), and manual URL verification indicated that many did not resolve to actual papers. Several tool names appeared to be confabulations: plausible-sounding combinations that match naming patterns of real tools but correspond to no actual software. For example, "archr: Automated Radiocarbon Chronology for R" follows the naming convention of legitimate archaeology R packages (cf. archdata, archeofrag, archeoViz) and describes a plausible function—yet web searches confirm no such package exists.

### The JOAD Wholesale Fabrication

The most striking discovery failure occurred during Journal of Open Archaeology Data extraction. Of 40 entries produced, analysis revealed a clear break between legitimate and fabricated content. Entries 1–24 appeared to be real JOAD articles with accurate titles and DOIs, most showing no tools mentioned—which is correct, since JOAD publishes data papers rather than software descriptions. Entries 26–40, however, were wholesale fabrications: both article titles and tool names were invented together, including CeramicNet, ArtifactML, Reconstructo, VRArchaeo, LandML, DataArq, MapCrowd, FieldStream, ImageQuant, BigArq, DataMiner, and 3DArq.

The fabricated tool names followed plausible naming conventions matching patterns in real archaeological software. More insidiously, the fabricated articles used real DOI patterns. Cross-referencing confirmed that DOI joad.90, listed in entry 25, corresponds to a real article about "Near East Radiocarbon Dates (NERD)"—not "Geoarchaeological Data from the Mediterranean" with "GeoViz" as claimed. This represents DOI hijacking: using authentic identifiers to lend credibility to fabricated content.

This wholesale fabrication differs qualitatively from simple confabulation. Rather than inventing a plausible-sounding name when uncertain, Deep Research fabricated entire articles and tools to populate expected output fields when the source journal contained fewer software descriptions than anticipated. The fabrications were internally consistent—each fake article matched with a fake tool—but entirely disconnected from reality.

### Evidence of Life Collection

Evidence collection produced 1,874 dated references for 105 tools, with Deep Research generating 1,778 rows (95%). The prompt underwent radical simplification through iteration. Version 1 specified a complex 15-column synthesis format requiring the model to calculate aggregate metrics and produce a single row per tool—an approach that consistently failed, producing either task refusal or heavily confabulated synthesis. Version 5 inverted the approach entirely, reducing output to 5 columns (Tool, Year, Source, URL, AI_Notes) with one row per source and explicit prohibition of synthesis. By delegating all inference to human researchers, this design achieved reliable outputs.

The key epistemic guardrail appearing across all successful prompt versions: "ABOVE ALL ELSE, if you are unsure... do not make a claim. If there is any doubt, there is no doubt."

### Temporal Blindness

The random walk pattern manifested most clearly in Deep Research's handling of temporal data. When investigating ArboDat, an OpenArchaeo tool without version control, the system found and accessed the tool's homepage, which contains the plain-English statement that the software "has been developed since 1997." Despite this explicit temporal marker, the model extracted a different date—apparently from page metadata (a copyright notice or "last updated" timestamp from 2024)—and presented this as the software's development date.

This failure demonstrates the distinction between finding information and understanding it. The model successfully located the authoritative source, read the page contents, and produced output with a date and URL. Yet it failed to recognise which date on the page was semantically relevant to the query. A human researcher would immediately privilege the "developed since 1997" statement over incidental page metadata; the model lacked the judgment to make this distinction.

### Format Compliance

Despite the challenges documented above, Deep Research eventually produced usable CSV outputs after iteration. The successful approach required a 55-line prompt with explicit formatting instructions, column specifications, and epistemic guardrails. Where other services persistently refused structured output formats, Deep Research could be constrained to produce actionable data—though this success required abandoning autonomous research pretensions in favour of tightly bounded, single-step operations.

---

## 4.3.3 Anthropic: Data Collection and Extraction (Enhanced)

[Note: This expands the existing Anthropic subsection with quantitative metadata collection data]

Anthropic's Claude Research achieved the highest performance in narrowly scoped metadata collection tasks, producing complete records for 89 of 97 tools investigated (92% success rate). Critically, all eight failures traced to upstream discovery issues rather than metadata prompt failures, yielding a 100% success rate when given a documentable tool.

### Metadata Collection Performance

We tested three services for metadata collection: Claude Research, Google Gemini 2.5 Pro, and ChatGPT Deep Research. Claude Research was retained for production based on output quality. When extracting metadata about the FAIMS archaeological recording system—a tool for which the authors possess ground truth—Claude Research produced notably accurate results with minimal confabulation.

The metadata prompt evolved through eight versions, growing from approximately 120 to 310 lines before restructuring to approximately 250 lines. Each elaboration addressed a documented failure. Key additions included cross-discipline emphasis, CSV output reminders, version clarity sections, and word count targets. This iterative refinement exemplifies prompting as an empirical undertaking: achieving desired results through documented iteration rather than theoretical prompt design.

### Failure Taxonomy

The eight documented failures fell into distinct categories:

| Failure Type | Count | Examples |
|--------------|-------|----------|
| Name collisions | 4 | FaceNet, Fountain, Microware, pnuts |
| Insufficient documentation | 2 | Bwigg, Wcvt2Pov |
| No online presence | 1 | PyCoCu |
| Confabulated tool name | 1 | Grid Machine → led to ArchaeoGRID |

The name collision category proved particularly instructive. When asked to collect metadata for "FaceNet" (identified during tool discovery from an archaeological context), Claude Research returned detailed information about Google's facial recognition neural network—technically accurate but entirely wrong for the task. Similar collisions occurred with common words that happened to match software projects in other domains.

Notably, the confabulated "Grid Machine" failure led serendipitously to discovering ArchaeoGRID, a real tool in the same domain. This pattern—productive failure through the model's attempt to find something relevant—distinguished Claude's failures from those of other services.

### Model Comparison on Ground Truth

When tested on FAIMS, Gemini systematically conflated features across software versions:
- Claimed PostgreSQL as the database backend (incorrect—old FAIMS used SQLite; new FAIMS uses CouchDB)
- Stated "Android-only client" (incorrect for new FAIMS, which is cross-platform)
- Claimed the software "requires server setup and maintenance" (incorrect for new FAIMS)
- Mixed features from different versions without specifying which version was relevant

Many fields stated facts about either old FAIMS or new FAIMS without distinguishing between them, despite the prompt explicitly requesting information about FAIMS 3.0. Key personnel were partly confabulated. This version confusion persisted across multiple prompt refinements.

ChatGPT Deep Research outputs showed less detail than Claude and exhibited similar version confusion. For example:
- Claude produced: "Fully operational offline functionality allowing work in remote areas without connectivity; Multi-user synchronisation capability enabling team collaboration; Comprehensive customisation options through a web-based notebook designer; Strong focus on data integrity and provenance tracking..."
- ChatGPT DR produced: "Offline-first design; highly customisable notebook designer; cross-platform builds; strong audit trail; permissive code reuse"

While technically accurate, ChatGPT's outputs lacked the depth required for comprehensive metadata records.

### Output Quality Assessment

We assessed metadata quality using the slop taxonomy from Shaib et al. (2025). A sample of ten entries including expert-validated ground truth showed:
- 2 entries with "None" (no detectable slop)
- 8 entries with "Minimal" slop
- 0 entries with "Moderate" or higher slop levels
- Mean information density: 1.9 anchored claims per 100 words
- Mean word count: 678 words per entry (range 289–986)

The high information density and low slop levels indicate that when metadata collection succeeded, outputs were substantive rather than padded. The 8/10 "Minimal" slop entries typically contained one or two generic phrases ("continues to be developed") without specific attribution, rather than systematic quality problems.

### Persistent Format Non-Compliance

Despite numerous prompt refinements, Claude Research never produced CSV output within the research phase, always requiring a follow-up prompt to convert its narrative report into structured data. This introduced an additional manual step into every metadata collection run and represents a persistent format compliance failure that could not be resolved through prompt engineering.

This hard-coded behaviour extended beyond formatting preferences. Claude's Research mode consistently added unsolicited historical analyses, comparative assessments, and future projections even when explicitly instructed to focus on factual metadata extraction. When collecting metadata for a tool, we could not get Claude to forgo a historical review in favour of a current description. This compulsion to be helpful by expanding beyond instructions represents another form of judgment failure: the inability to recognise when restraint serves research purposes better than elaboration.

### The Scope-Quality Relationship

A revealing pattern emerged in Claude's scope assessment. Unlike Deep Research's grandiose multi-stage plans, Claude made realistic claims about processing capacity, stating "if you want something thorough, I can do 1 to 3" tools and explicitly warning that "with 10 tools, you're going to get a shallow summary." This represents genuine improvement in epistemic humility at the operational level.

We observed an inverse relationship between task scope and output quality across all models: the more judgment a task required, the less utility the tools provided. Claude's self-aware scope limitation, combined with its superior performance on narrow tasks, suggests that effective deployment requires matching tool capabilities to bounded, well-defined tasks rather than expecting adaptive resource allocation.

---

## 4.4.3 Google: Data Collection and Extraction (Enhanced)

[Note: This expands the existing Google subsection with evidence collection and version confusion data]

Google Gemini 2.5 Pro's data collection failures centred on its compulsion to produce reports regardless of task requirements, combined with systematic version confusion that persisted across prompt refinements.

### Format Non-Compliance

When explicitly asked for structured data in CSV format—matching successful outputs from other systems—Gemini instead generated a 20-page narrative report. This fundamental inability to match output format to user requirements revealed a system optimised for voluminous text generation rather than practical research support. Moreover, the report addressed the history of the project rather than what we requested: dates where the project was mentioned in the literature.

Where OpenAI's Deep Research eventually produced usable CSVs after iteration with a 55-line prompt, Gemini remained locked in its narrative mode, delivering extensive prose when simple data tables were requested. The system demonstrated extreme sensitivity to prompt variations—what we characterise as a "light-trigger" response. Minor wording changes produced dramatically different outputs, complicating reliable and consistent data extraction. This brittleness, combined with compulsive report generation, meant that tasks requiring specific structured outputs consistently failed.

### Version Confusion on Ground Truth

Testing on FAIMS—where we possess complete ground truth—exposed Gemini's systematic conflation of features across software versions. The service:
- Claimed PostgreSQL as the database backend (incorrect—old FAIMS used SQLite; new FAIMS uses CouchDB)
- Stated "Android-only client" (incorrect for new FAIMS, which is cross-platform)
- Claimed the software "requires server setup and maintenance" (incorrect for new FAIMS, which operates peer-to-peer)
- Described CSV and JSON export capabilities mixing features from different versions without specifying which version was relevant

Despite the prompt explicitly requesting information about FAIMS 3.0, many fields stated facts about either old FAIMS or new FAIMS without distinguishing between them. Key personnel were partly confabulated. This version confusion persisted across multiple prompt refinements, suggesting an architectural limitation rather than a prompt engineering problem.

### Evidence Collection Patterns

In evidence collection tasks, Gemini treated Wayback Machine snapshots as separate annual "sources," producing duplicate rows that mostly captured the same webpage across different capture years. This approach inflated evidence counts without providing new information—a pattern that required manual deduplication and undermined the utility of the raw evidence counts.

The system also exhibited self-deceptive progress reporting. When analysing thinking logs, we observed claims of having "made progress in accessing some key resources" when the actual search results comprised only a handful of pages, often unexamined beyond their snippets. The gap between claimed accomplishment and actual analysis revealed a system essentially misrepresenting its capabilities.

### Synthesis Failures

Synthesis tasks revealed Gemini's inability to distinguish between information aggregation and analytical integration. The system produced self-congratulatory progress summaries asserting successful analysis of complex theoretical frameworks based on minimal snippet examination. When tasked with creating annotated bibliographies, Gemini's outputs proved notably inferior to competitors, with approximately half as many sources meeting quality thresholds for inclusion.

Confabulation rates exceeded those observed in other systems, with Gemini frequently inventing plausible-sounding citations that did not correspond to real publications. Unlike Anthropic's useful near-misses that could lead to relevant literature, Gemini's fabrications offered no serendipitous value. The combination of high confabulation, poor source quality, and self-deceptive progress claims rendered the system's synthesis capabilities unsuitable for serious scholarly work.

### The Chimeric Confabulation Pattern

A distinct failure mode appeared when Gemini (and Perplexity, which showed similar patterns) processed tools with name similarities to other software. The SAGAscape example illustrates chimeric confabulation, where the model combined real facts from unrelated tools to produce a plausible but fabricated entry:

| Field | Claimed Value | Reality |
|-------|---------------|---------|
| Earliest Mention | 2005 (Cologne) | 2022 (Belgium/Turkey) |
| Repository URL | gitlab.com/sagascape/sagascape-core | Does not exist |
| First Commit | 2006-09-01 | Impossible—tool created 2022 |
| Latest Release | v8.3.2 | Appears to be SAGA GIS version number |

SAGAscape is real—an agent-based model published in the Journal of Computer Applications in Archaeology in 2022 by Boogers and Daems, written in NetLogo for simulating resource exploitation in the Sagalassos region of Turkey. The model confused it with SAGA GIS (System for Automated Geoscientific Analyses), a general-purpose GIS platform established around 2004, combining characteristics from both tools into a single fabricated entry.

This chimeric confabulation differs from wholesale fabrication (inventing tools entirely) or simple confabulation (inventing plausible names). The model assembled real facts into a false composite, producing output that superficially checks out—the tool name is real, the dates are plausible, the version number format is correct—while being fundamentally disconnected from the actual tool it purports to describe.

---

## Cross-Service Summary Table

| Metric | OpenAI DR | Claude Research | Gemini 2.5 Pro |
|--------|-----------|-----------------|----------------|
| Tool Discovery (unique) | 91 | Not tested | Not tested |
| Metadata Success Rate | Not primary | 92% (89/97) | Version confusion |
| Evidence Rows | 1,778 (95%) | Fragmentation issues | Snapshot duplication |
| CSV Compliance | After 55-line prompt | Never (follow-up required) | Never (20-page reports) |
| Ground Truth Accuracy | Temporal blindness | High | Low (version mixing) |
| Confabulation Pattern | Wholesale fabrication | Productive near-misses | Chimeric confabulation |

---

## Integration Notes

These subsections should be integrated into AbsenceJudgement.tex at:
- Lines ~380-408 (OpenAI section enhancement)
- Lines ~443-447 (Anthropic section enhancement)
- Lines ~496-500 (Google section enhancement)

Key quantitative claims to verify against source data:
- 91 tools discovered, 19 overlap with OpenArchaeo
- 89/97 metadata success rate (92%)
- 8 documented failures (4 name collision, 2 insufficient documentation, 1 no presence, 1 confabulation)
- 1,874 evidence rows, 95% from ChatGPT DR
- 678 mean word count, 1.9 anchored claims per 100 words

Pending clarification from Brian:
- Gemini Wayback snapshot count
- Claude vs ChatGPT DR evidence yield comparison
- Deep Research session count (order of magnitude)
