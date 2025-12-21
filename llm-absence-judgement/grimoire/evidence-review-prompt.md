# Evidence Review Prompt

A workflow for reviewing evidence-of-life events to verify tool lifecycle data.

## Critical Distinction: QA on Existing Data Only

**This workflow verifies EXISTING evidence-events from the source data (03-tool-evidence.xlsx).** The task is to confirm that each specific source listed in our dataset actually mentions the tool as claimed.

**This is NOT**:
- Finding new evidence or new sightings of tools
- Confirming a tool exists by finding it mentioned elsewhere
- Searching for alternative sources that mention the tool

**A valid confirmation requires**: The SPECIFIC source listed in the evidence-event explicitly mentions the tool. Finding the same tool mentioned in a different source does not confirm the event.

## Context

Use this approach when:

- You have evidence events (references, mentions, citations) for research tools
- Each event needs verification that the source exists and mentions the tool
- Quality assessment is needed (strong/moderate/weak evidence)
- Tool name collisions may exist (same name, different software)

## Invocation

```text
Review evidence for [TOOL NAME] ([N] events) from tool-evidence-granular.csv.

For each event:
1. Verify the source exists (check URL accessibility)
2. Confirm the tool is actually mentioned in the source
3. Validate the year matches the source's publication date
4. Assess evidence quality (Strong/Moderate/Weak)
5. Flag any issues (broken URL, wrong tool, collision, etc.)

Present results in a summary table, then we'll discuss any issues.
```

## Per-Event Investigation

For each evidence event, check:

| Check | Description |
|-------|-------------|
| Source exists | URL accessible, or note if paywalled/archived |
| Tool mentioned | Tool actually discussed in source (not just similar name) |
| Year correct | Publication date matches stated year |
| Quality rating | Strong (peer-reviewed), Moderate (blog/tutorial), Weak (passing mention) |
| Issues | Broken URL, collision, wrong year, etc. |

## Quality Criteria

### Strong Evidence
- Peer-reviewed journal articles
- Official software documentation
- Release notes/changelogs
- Conference proceedings (published)
- Academic books/chapters

### Moderate Evidence
- Preprints (arXiv, OSF, etc.)
- Blog posts from developers/maintainers
- Conference presentations (slides/abstracts)
- Tutorials and how-to guides
- Repository metadata (GitHub, CRAN, PyPI)

### Weak Evidence
- Social media mentions
- Forum posts
- Passing mentions in unrelated work
- Secondary citations ("X used tool Y")
- Undated or poorly sourced references

## Presentation Format

```markdown
## [Tool Name] Review: [N] events

| # | Year | Source | Quality | Issues |
|---|------|--------|---------|--------|
| 1 | 2020 | Journal of X... | Strong | None |
| 2 | n.d. | GitHub README | Moderate | Year unclear |
| 3 | 2018 | Blog post... | Weak | Passing mention only |

### Issues requiring discussion

**Event 3**: [Detailed notes on the issue]
```

## User Response Options

After reviewing the summary:

- **Approve batch**: All events accepted, update CSV with CONFIRMED status
- **Follow-up questions**: Request clarification on specific events
- **Manual check**: User will verify specific events themselves
- **Exclude events**: Mark specific events as EXCLUDED with reason

## Verification Workflow

**Goal**: Resolve all URLs autonomously, then present unresolvable items to user.

### Step 1: Title/Abstract Verification via Web Search

**When you cannot access a full PDF**, use web search to check if the tool appears in the title or abstract of THE SPECIFIC SOURCE listed in the evidence-event. This is a workaround for inaccessible full-text, not a way to find alternative evidence.

**Key principle**: You are verifying the SPECIFIC source in our dataset, not finding other sources that mention the tool.

1. **Search for the specific source**: `"[Source Title]" [author] [year]`
2. **Check if tool appears in title/abstract**: Search results often show titles and abstract snippets
3. **Only mark CONFIRMED if**: The tool name appears explicitly in the title or abstract of THAT source
4. **If tool not visible in title/abstract**: Mark UNVERIFIED (requires full-text access)

**Example - VALID confirmation**:
- Event claims: "SASSA mentioned in EGU 2007 abstract by Smith"
- Search: `"SASSA" EGU 2007 Smith`
- Result shows: Abstract title "SASSA: A Support System for Archaeological Survey"
- Action: CONFIRMED - tool explicitly in title of the specific source

**Example - INVALID confirmation**:
- Event claims: "straditize mentioned in Journal of Ecology 2019 paper"
- Search: `straditize "Journal of Ecology" 2019`
- Result shows: straditize exists (JOSS paper), but no evidence THIS specific J.Ecology paper mentions it
- Action: UNVERIFIED - cannot confirm the specific source without full-text access

**Do NOT mark CONFIRMED just because**:
- The tool exists and is used in that field
- Other papers in the same journal use the tool
- The paper topic seems related to the tool's function

### Step 2: Attempt URLs for Remaining Events

For events not resolved via title/abstract search, attempt to verify via WebFetch:
- Follow redirects (DOIs often redirect to publisher sites)
- For PDFs, attempt to fetch and search for tool name
- Record: tool mentioned (yes/no), year matches (yes/no)

### Step 3: Handle Failures by Type

| Failure Type | Action |
|--------------|--------|
| **Accessible** | Mark CONFIRMED if tool mentioned, CONFABULATED if not |
| **404 (broken)** | Web search for moved resource; if found, verify; if not found, mark UNVERIFIED |
| **403 (paywalled)** | Check title/abstract (often visible); if tool mentioned, CONFIRMED; else pass citation to user |
| **PDF too large** | Pass URL to user for manual search (see PDF verification protocol below) |
| **Fetch error** | Retry once; if still failing, pass URL to user |
| **Site blocked** | Note for user verification (e.g., StackExchange, Wikipedia) |

**Note on paywalled sources**: Titles and abstracts are typically visible even behind paywalls. Check these first - if the tool name appears in title or abstract, mark CONFIRMED without requiring full-text access.

**Note on 404s**: URLs that were valid during the original LLM run may have since broken. If web search cannot locate a moved copy, mark UNVERIFIED rather than CONFABULATED - absence of evidence is not evidence of fabrication.

**Note on user downloads**: When the user downloads a PDF for verification, they place it in `bibliography/`. Read the file from there to check for tool mentions.

### PDF Verification Protocol

When a PDF is too large to fetch or parse:

1. **Provide the URL** to the user with the tool name to search for
2. **User searches with Ctrl+F** - if they find the reference, they confirm and provide the relevant text
3. **If user cannot find it**, they download the PDF to `bibliography/` for Claude to verify
4. **Mark accordingly**: CONFIRMED if user finds mention, proceed to step 3 if not found

This minimises unnecessary file transfers while maintaining verification rigour.

### Step 4: Present to User

After autonomous verification, present:

1. **Summary table** with all events and their status
2. **Paywalled citations** (author, title, DOI) for user to verify via institutional access
3. **Unresolved URLs** for user to check manually

User confirms items, then update CSV accordingly.

### Zenodo/Repository Errors

If Zenodo or similar repositories consistently fail, consider setting up API access for batch verification.

## Handling Collisions

When evidence refers to a different tool with the same name:

1. Check metadata (`02-tool-metadata.xlsx`) to identify which tool we investigated
2. Evidence matching our metadata → CONFIRMED
3. Evidence for different tool → EXCLUDED with collision note
4. Add colliding tool to `planning/tools-for-later-investigation.md`

## CSV Updates

After review, update `tool-evidence-granular.csv` with:

| Column | Values |
|--------|--------|
| Review_Status | CONFIRMED, CONFABULATED, COLLISION, UNVERIFIED |
| Review_Notes | Brief note explaining status |

### Status Definitions

| Status | Meaning |
|--------|---------|
| CONFIRMED | Source exists and mentions the correct tool |
| CONFABULATED | Source exists but does NOT mention the tool (fabricated reference) |
| COLLISION | Source mentions a different tool with the same name |
| UNVERIFIED | Could not verify yet (PDF inaccessible, URL broken, awaiting user check) |

## Batch Processing Strategy

For large-scale verification:

### Recommended Approach

**Parallel URL fetching**: Fetch 4-6 URLs simultaneously to maximise throughput while staying within rate limits.

**Batch by tool**: Process all events for one tool before moving to the next. This keeps context coherent and makes collision detection easier.

**Present results incrementally**: After each tool batch, present summary and get user confirmation before proceeding. This catches workflow issues early.

### Batch Sizes

| Dataset Size | Recommended Batch |
|--------------|-------------------|
| < 20 events | Single batch, all tools |
| 20-100 events | 3-5 tools per batch |
| 100+ events | 1 tool per batch, parallel URL fetches |

### Progress Tracking

Use TodoWrite to track:
- Tools pending review
- Current tool in progress
- Tools completed with issue counts

This provides visibility to user and prevents losing track during long sessions.

## Origin

Developed during evidence review for the Theseus Ship project, December 2025. Adapted from human-in-the-loop-review.md pattern.
