# Evidence Review Workflow

**Purpose**: Systematic human-in-the-loop review of evidence-of-life events for tool lifecycle research.

**Created**: 2025-12-18

**Reusable prompt**: See `grimoire/evidence-review-prompt.md` for the generalised workflow template.

---

## Review Process

### Batch Structure
- One tool per batch (all evidence events for that tool reviewed together)
- Reviewer presents findings for each event
- User approves, asks follow-ups, or manually verifies

### Per-Event Investigation

For each evidence event, the reviewer should:

1. **Verify the source exists** — Check URL is accessible (or note if paywalled/archived)
2. **Confirm tool mention** — Verify the tool is actually mentioned/discussed in the source
3. **Validate the year** — Confirm the stated year matches the source's publication date
4. **Assess evidence quality** — Rate the strength of this evidence:
   - **Strong**: Peer-reviewed publication, official documentation, release announcement
   - **Moderate**: Blog post, conference presentation, tutorial, informal guide
   - **Weak**: Passing mention, tangential reference, secondary citation
5. **Flag issues** — Note any problems (broken URL, tool not actually mentioned, wrong year, etc.)

### Presentation Format

For each tool batch, present a summary table:

```
| # | Year | Source (truncated) | Quality | Issues |
|---|------|-------------------|---------|--------|
| 1 | 2020 | Journal of X... | Strong | None |
| 2 | n.d. | GitHub README | Moderate | Year unclear |
| 3 | 2018 | Blog post... | Weak | Tool only mentioned in passing |
```

Then provide detailed notes for any events with issues or that need discussion.

### User Response Options

- **Approve batch**: All events accepted as valid evidence
- **Follow-up questions**: Request clarification on specific events
- **Manual check**: User will verify specific events and report back
- **Flag for exclusion**: Mark specific events as invalid/unreliable

### Status Tracking

Add columns to CSV after review:
- `Review_Status`: CONFIRMED, EXCLUDED, NEEDS_VERIFICATION
- `Review_Notes`: Brief note on any issues
- `Evidence_Quality`: Strong, Moderate, Weak

---

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
- GitHub/GitLab repository metadata

### Weak Evidence
- Social media mentions
- Forum posts
- Passing mentions in unrelated work
- Secondary citations ("X used tool Y")
- Undated or poorly sourced references

---

## Notes

- 2025 dates are valid (runs conducted Feb–Apr 2025)
- HTML artifacts in AI_Notes are cosmetic, not errors
- Focus on whether evidence genuinely documents tool existence/usage at stated time
