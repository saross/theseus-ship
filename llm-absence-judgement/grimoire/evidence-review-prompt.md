# Evidence Review Prompt

A workflow for reviewing evidence-of-life events to verify tool lifecycle data.

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

### Step 1: Attempt All URLs

For each evidence event, attempt to verify via WebFetch:
- Follow redirects (DOIs often redirect to publisher sites)
- For PDFs, attempt to fetch and search for tool name
- Record: tool mentioned (yes/no), year matches (yes/no)

### Step 2: Handle Failures by Type

| Failure Type | Action |
|--------------|--------|
| **Accessible** | Mark CONFIRMED if tool mentioned, CONFABULATED if not |
| **404 (broken)** | Web search for moved resource; if not found, pass URL to user |
| **403 (paywalled)** | Check title/abstract (often visible); if tool mentioned, CONFIRMED; else pass citation to user |
| **PDF too large** | Pass URL to user for manual download |
| **Fetch error** | Retry once; if still failing, pass URL to user |

**Note on paywalled sources**: Titles and abstracts are typically visible even behind paywalls. Check these first - if the tool name appears in title or abstract, mark CONFIRMED without requiring full-text access.

### Step 3: Present to User

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
| Review_Status | CONFIRMED, CONFABULATED, EXCLUDED, UNVERIFIED |
| Review_Notes | Brief note explaining status |

### Status Definitions

| Status | Meaning |
|--------|---------|
| CONFIRMED | Source exists and mentions the tool correctly |
| CONFABULATED | Source exists but tool is NOT mentioned (fabricated reference) |
| EXCLUDED | Evidence is for a different tool (collision) |
| UNVERIFIED | Could not verify; awaiting user confirmation |

## Origin

Developed during evidence review for the Theseus Ship project, December 2025. Adapted from human-in-the-loop-review.md pattern.
