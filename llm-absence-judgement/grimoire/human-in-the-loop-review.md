# Human-in-the-Loop Review

A workflow for efficiently reviewing large candidate sets where relevance criteria are difficult to specify upfront but become clear through examples.

## Context

Use this approach when:

- You have a large corpus (hundreds to thousands of items) to filter
- Relevance criteria are subjective or context-dependent
- You'll recognise relevant/irrelevant items when you see them, but can't fully specify rules in advance
- False positives are acceptable in initial filtering; false negatives are costly

**Examples:**

- Reviewing conversation exports for project-relevant chats
- Filtering search results for literature review
- Triaging issue backlogs or email archives
- Identifying relevant documents in a large collection

## Workflow

### Phase 1: Automated Initial Filtering

Generate a scored candidate list using keyword/pattern matching.

**Purpose:** Reduce the corpus to a manageable size while minimising false negatives.

**Output:** Candidates organised by relevance score (HIGH/MEDIUM/LOW/NONE), with enough context to assess each item (title, date, preview, identifier).

### Phase 2: Calibration Sampling

User reviews a representative sample (~20-30% of HIGH relevance items).

**Purpose:** Identify exclusion patterns and edge cases that weren't anticipated.

**User actions:**

- Mark clear inclusions/exclusions
- Note categories of false positives (e.g., "all RAiD items are unrelated")
- Flag uncertain items for discussion

**Key insight:** The user often can't articulate exclusion rules upfront but can identify them when seeing concrete examples.

### Phase 3: Pattern Extraction

AI explicitly identifies learned rules from user feedback.

**Present to user for confirmation:**

```text
Based on your review, I've identified these patterns:

EXCLUDE:
- All items mentioning [X] (seen in items 3, 7, 12)
- Items from [date range] about [topic]

INCLUDE:
- Items matching [pattern] even if [apparent contradiction]

UNCERTAIN:
- Items about [topic] - could be relevant, need case-by-case review

Should I apply these rules to the remaining items?
```

### Phase 4: Assisted Completion

AI pre-fills decisions for remaining items with confidence indicators.

**Format:**

```markdown
- [x] Include *(HIGH confidence: matches [inclusion pattern])*
- [x] Exclude *(HIGH confidence: [exclusion category])*
- [ ] Uncertain *(LOW confidence: could be [X] or [Y], needs review)*
```

**User reviews:**

- All UNCERTAIN items
- Spot-check of HIGH confidence decisions
- Any items they want to override

### Phase 5: Execution

Apply final decisions (extract, tag, move, etc.) and document the filtering criteria used for reproducibility.

## Model Prompt

Use this prompt to invoke the workflow:

```text
I need to review [CORPUS DESCRIPTION] to identify items relevant to [PURPOSE].

Please help me using a human-in-the-loop review approach:

1. **Initial filtering**: Search/filter the corpus using keyword patterns related to [RELEVANCE CRITERIA]. Generate a candidate list organised by relevance score with enough context to assess each item.

2. **Calibration**: Present the results. I'll review a sample and provide feedback on false positives/negatives.

3. **Pattern extraction**: Based on my feedback, explicitly state the inclusion/exclusion rules you've learned. Ask me to confirm before proceeding.

4. **Assisted completion**: Pre-fill decisions for remaining items with confidence indicators. I'll review uncertain items and spot-check your decisions.

5. **Execution**: Apply final decisions and document the filtering criteria.

Let's start with phase 1.
```

## Variations

### Active Learning Variant

Instead of sequential review, present the most ambiguous items first:

1. Initial filtering (same)
2. AI identifies items where classification is uncertain
3. User reviews ambiguous items first (maximum learning per item reviewed)
4. AI applies learned patterns to clear-cut items
5. User spot-checks

**Trade-off:** More efficient learning, but user doesn't see the "shape" of the full candidate set early.

### Clustering Variant

For very large corpora or when keyword matching is insufficient:

1. Semantic clustering of items (group by topic similarity)
2. User reviews cluster summaries, approves/rejects entire clusters
3. AI presents edge cases that don't fit cleanly into clusters
4. User reviews edge cases
5. Apply decisions

**Trade-off:** Faster for homogeneous clusters, but risks missing outliers.

### Iterative Refinement Variant

For ongoing/repeated filtering tasks:

1. Initial filtering with current rules
2. User reviews sample, provides feedback
3. Rules updated and documented
4. Next batch uses refined rules
5. Periodic recalibration as patterns shift

**Trade-off:** Rules improve over time, but requires tracking rule evolution.

## Anti-patterns

- **Skipping calibration**: Applying AI judgement without user feedback leads to systematic errors
- **Over-specifying upfront**: Trying to define all rules before seeing data wastes effort on irrelevant distinctions
- **Treating AI decisions as final**: Always preserve user override capability
- **No audit trail**: Decisions without reasoning can't be reviewed or learned from

## Origin

Developed during review of Claude.ai conversation exports for the Theseus Ship project, December 2024. Initial corpus: ~200 conversations. Time to review: ~45 minutes (vs estimated 2+ hours for manual review).
