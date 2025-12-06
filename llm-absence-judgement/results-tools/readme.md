# Orientation to working results of our LLM-assisted software tool research

The files in this folder represent the working data for the discovery, documentation, and evidence-of-life gathering stages of research for the Theseus Ship project, which is exploring the lifecycle of digital tools in archaeology and adjacent disciplines.

## Source of truth: manually produced Excel spreadsheets

The four Excel Spreadsheets represent the source-of-truth for our results:

- **01a-tool-discovery.xlsx** contains various artefacts representing both successful and unsuccessful searches online in academic literature for mention or discussion of tools using LLMs to conduct the searches. This pathway of discovery is one of two we used. Includes 12 sheets from different runs (IA, JOSS, JCAA, JOAD, SoftwareX) with varying quality levels marked in sheet names (e.g., "success", "fail", "extreme fail").

- **01b-tool-openarchaeo-work.xlsx** contains tools found in the OpenArchaeo GitHub repo, the second pathway by which we discovered tools, ultimately split into those that utilise a DVCS (which allows straightforward assessment of the lifecycle) and those that do not. The ones without a DVCS were run through our pipeline like the tools we discovered ourselves, while investigation of those with a DVCS was deferred since that will involve a different approach (programmatic investigation of their GitHub/GitLab repos).

- **02-tool-metadata.xlsx** represents the second phase of our work, where discovered tools and tools from OpenArchaeo without DVCS were thoroughly documented, so as to capture metadata that might shed light on their lifecycle. Metadata was aligned with OpenArchaeo metadata but is much richer. Contains versioned tabs (V1–V8) showing prompt evolution.

- **03-tool-evidence.xlsx** represents the third stage of our research, where we used LLMs to search for 'evidence of life' for the tools, to document their lifespan/lifecycle. This spreadsheet contains both successes and failures, plus model comparison/elimination sheets.

### Pipeline Flow

01a (Discovery) + 01b (OpenArchaeo)
↓ verified tools
02 (Metadata collection)
↓ tools with complete metadata
03 (Evidence of life)

## LLM derivatives generated from source-of-truth files but not yet integreated

The other files:

- tool_discovery_granular.csv
- tool_discovery_summary.csv

are refinements / derivatives of the two tool-discovery pathways (our own discovery and OpenArchaeo) that were produced by Claude Opus 4.5 in the chat interface but not yet integrated into the source-of-truth documents above.

## Suggested mode-of-work

The Excel spreadsheets represent the results we built up, including successes and failures, as we initiated our research pipeline, but they are cumbersome to work with. I suggest that when we need to work with this data, we extract the sheet in question as a CSV, do the work on it, and then at the end of data / results analysis, we can re-integrate that CSV either by replacing the original sheet (if it represents relatively minor changes) or inserting it as a new sheet. I have copies of the originals online (as Google Sheets) and backed up locally. 