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

## Derived CSV Files

### Discovery Data

- **tool-discovery-granular.csv** — 350 discovery events with full provenance (which LLM found what, in which journal, from which run)
- **tool-discovery-summary.csv** — 244 unique tools (de-duplicated) with aggregated discovery metadata

### OpenArchaeo Data

- **tool-openarchaeo-granular.csv** — 513 items from OpenArchaeo export tracked through the classification and investigation pipeline

#### Column definitions

| Column | Description |
|--------|-------------|
| Tool | Item name from OpenArchaeo |
| Has-DVCS | Whether tool has a full DVCS repository (GitHub, GitLab, Bitbucket, etc.) — excludes Gists |
| Gist-only | Whether the only code hosting is a GitHub Gist (no full repository) |
| AI-classification | LLM classification against tool definition (yes/no) |
| Human-review | Human review outcome (Yes = accepted as tool) |
| In-final-list | Whether tool made it to the final OpenArchaeo tool list |
| Discovery-overlap | Whether tool also appeared in LLM Discovery pathway |
| Unique-to-OpenArchaeo | Tool is in final list but NOT in Discovery pathway |
| Metadata-investigated | Whether metadata was collected (yes only for Discovery overlap tools) |
| Evidence-investigated | Whether evidence-of-life was collected (Discovery overlap OR no-DVCS tools) |

#### Note on DVCS vs Gist distinction

GitHub Gists are excluded from the "Has-DVCS" column because:

- **Gists are lightweight code snippets**, not full repositories
- **No collaborative infrastructure** — no issues, pull requests, or discussions
- **No versioning workflow** — no releases, tags, or meaningful commit history
- **Typically "fire and forget"** — created to share code once, rarely maintained

For lifecycle analysis, a Gist provides only a single data point (existence), whereas a full repository allows reconstruction of the tool's development history through commits, releases, and activity patterns.

#### Pipeline summary

| Stage | Count |
|-------|-------|
| Raw OpenArchaeo export | 513 |
| With full DVCS | 452 |
| Without DVCS (incl. Gist-only) | 61 |
| AI classified as tool | 341 |
| Human-reviewed as tool | 375 (372 unique*) |
| In final tool list | 375 (372 unique*) |
| — With DVCS | 343 |
| — Without DVCS | 32 (of which 7 Gist-only) |
| Overlap with Discovery | 20 |
| Unique to OpenArchaeo | 355 |
| Metadata investigated | 20 (all from Discovery overlap) |
| Evidence investigated | 43 (20 Discovery overlap + 23 no-DVCS unique) |
| Not investigated at all | 332 (unique to OpenArchaeo, with DVCS) |

*3 case-insensitive duplicates: harris-matrix (×2), outliner/outlineR, seriation/Seriation

### Verification Data

- **verification-status-legend.md** — Detailed documentation of verification status codes and criteria
- **verification-sample.csv** — Sample verification data

### Final Verification Summary (2025-12-18)

All 350 discovery events have been manually verified:

| Status | Count | % |
|--------|-------|---|
| CONFIRMED | 230 | 65.7% |
| MISATTRIBUTED | 70 | 20.0% |
| CONFABULATED | 50 | 14.3% |

**Outcome**: 230 successes (65.7%), 120 failures (34.3%)

Summary-level verification (244 unique tools):

| Status | Count |
|--------|-------|
| VERIFIED | 156 |
| MISATTRIBUTED | 52 |
| CONFABULATED | 36 |

## Suggested Mode of Work

The Excel spreadsheets represent the results we built up, including successes and failures, as we initiated our research pipeline, but they are cumbersome to work with. I suggest that when we need to work with this data, we extract the sheet in question as a CSV, do the work on it, and then at the end of data/results analysis, we can re-integrate that CSV either by replacing the original sheet (if it represents relatively minor changes) or inserting it as a new sheet. I have copies of the originals online (as Google Sheets) and backed up locally. 