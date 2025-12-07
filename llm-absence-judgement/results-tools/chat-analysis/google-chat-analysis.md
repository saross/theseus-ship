# Google Chat History Analysis: Project Evolution and Key Observations

*Analysis conducted by Claude Code, 7 December 2025*
*Source: BBS-SAR-google-chat-history.md (February–May 2025)*

---

## Executive Summary

The Google Chat history provides a real-time record of methodological decisions, pivots, and learnings throughout the "Absence of Judgement" research project. This analysis documents key observations relevant to completing Section 4 of the paper.

---

## 1. Timeline and Major Phases

### Phase 1: Tool Discovery (11 Feb – 27 Feb 2025)
- Initial journal scanning using DR (Internet Archaeology first)
- Rapid discovery of batch size constraints
- Model comparison begins

### Phase 2: OpenArchaeo Enhancement (~21 Feb – 30 Apr 2025)
- Hugging Face script development for DR automation
- CSV formatting challenges requiring manual cleanup
- $200+ of OpenAI credits consumed

### Phase 3: Metadata Collection (1 May – ongoing)
- Prompt evolution from v3 to v8
- Model comparison: Claude Research emerges as preferred tool
- Persistent issues documented (CSV generation, sensational titles)

### Phase 4: Evidence Collection (parallel with Phase 3)
- Claude Research for tool reference finding
- Git scraper development for ground truth comparison

---

## 2. Segmentation Decisions (Gap 14.1 — ANSWERED)

**Original Combined Approach**: Discovery and evidence were NOT originally planned as one prompt. The Google Chat shows the workflow was always segmented by journal/source.

**Actual Segmentation Issue**: The constraint was **within** discovery:
- "I'm causing it to go in chunks of 10 issues" (Brian, 13 Feb)
- Each tool investigated in separate DR session
- "Each tool is in a new chat otherwise it'll confabulate (more)" (Brian, 25 Feb)

**Key Finding**: The batch size constraint was discovered empirically through trial and error, not from explicit model limitations.

---

## 3. Batch Size Constraints (Gap 14.2 — ANSWERED)

### What Happened When Larger Batches Were Attempted

**Journal-level batching** (13 Feb):
- DR processed Internet Archaeology in "chunks of 10 issues"
- Full journal scan was too broad; model got distracted

**JOSS failure** (20 Feb):
- "It just keeps getting distracted with tags, very bad at instruction following"
- Model couldn't filter to humanities-relevant software from broader catalogue
- "go look at this set of 46 libraries and identify if they're from the humanities? Just no"

**Context contamination** (25 Feb):
- Shawn: "I repeat the prompt, and it seems to do OK"
- Brian: "Each tool is in a new chat otherwise it'll confabulate (more)"
- Brian: "DR doesn't [remember], but the model does"
- Decision to segregate work to prevent cross-contamination

### How Optimal Batch Size Was Determined

Purely empirical:
- Started with journal-level → failed
- Moved to issue-level (10 at a time) → worked for IA
- Individual tools for metadata → required for quality
- "These take forever" (Brian, 14 Feb) — time cost acknowledged

---

## 4. Model Elimination Sequence (Gap 14.3 — ANSWERED)

### For Tool Discovery

| Model | Outcome | Date | Issue |
|-------|---------|------|-------|
| DR (OpenAI) | Primary tool | Feb 2025 | Worked but inconsistent, "seams showing" |
| Perplexity DR clone | "It's shit" | 16 Feb | Not specified |
| o3-mini-high with search | Could hit webpages DR couldn't | 20 Feb | Stopped after first result |
| Operator | "Fascinating to watch...slow" | 20 Feb | Returned one article with tool list |
| Computer Use (Anthropic) | $1 of tokens, failed | 19 Feb | "failure to click, failure to right click" |
| Elicit | Tried | 19 Feb | Outcome not documented in chat |

### For Metadata Collection (v3→v8 evolution, May 2025)

| Model | Outcome | Key Issue |
|-------|---------|-----------|
| o3 | "Less impressed" | Made up references, "lying liar who lies" |
| Gemini | "Sucks...just made a bunch of crap up" | Version confusion, fabrication |
| DR (metadata attempt) | "just...won't" | Couldn't be made to produce structured output |
| Claude Research | **Winner** | "good and mostly consistent...very happy with results" |

**Quote**: "I keep coming back to Claude for a lot of stuff, even though I keep hearing that Gemini and o3 are 'better'" (Shawn, 6 May)

**Key differentiation**: Claude's failures (CSV refusal, hyperbolic titles) were "tolerable annoyances" vs Gemini's failures (version confusion, fabrication) which corrupted the data.

---

## 5. Persistent Annoyances Despite Success (Gap 14.4 — ANSWERED)

### CSV Generation
- "Claude basically said 'no, you're not going to reproduce this via API'" (Shawn, 5 May)
- "always have to ask for the CSV, can't make it generate it from the initial prompt, always makes the report then stops" (Shawn, 6 May)
- Required explicit second request every time

### Sensational Titles
- "Claude just **won't** do a couple of things, no matter how I try. Australian English. Non-sensational report titles. Just no" (Shawn, 6 May)
- Small prompt adjustment helped temporarily but "relapsed"
- Titles like "Revolutionary Digital Archaeology: The FAIMS Transformation"

### Australian English
- "says 'always use Australian spelling and punctuation', and...no" (Shawn, 6 May)
- Remained a consistent failure despite system prompt instructions

### Follow-up Questions
- "I've mostly got it to stop asking follow-up questions" (Shawn, 6 May)
- Required prompt iteration

### Missing Columns
- "browbeat it into making sure it doesn't miss any columns in the CSV, which was a problem the first few runs" (Shawn, 6 May)

### Version Conflation
- "Had trouble getting it to not conflate various versions, shifted focus to 'recency' and put all historical info into 'history'" (Shawn, 2 May)
- Solution: Create dedicated History field to "channel" the model's tendency

---

## 6. Prompt Evolution Evidence

### Discovery Prompt
- Developed iteratively through Feb 2025
- "v7 is in overleaf" (Brian, 23 Feb)
- Focus on: tool definition, journal specificity, output format

### Metadata Prompt (v3→v8)
- v3: Initial attempt based on individual-tool prompt (2 May)
- v8: Final version with "domestication" strategies (4 May)
- Key changes: History field, recency focus, controlled vocabularies
- "have tried to up my prompting game, see v8 in the Overleaf document" (Shawn, 4 May)

### Evidence Collection
- Shared limitations with discovery
- Same batch constraints applied

---

## 7. Critical Insights for Section 4 Narrative

### "The Judgment Boundary"

All models shared the same fundamental limitations:
- "they all made the same kind of mistake" (Brian, 8 May)
- "do you see huge differences between the deep research products from the different labs?" / "In the margins, but not in the errors" (8 May exchange)

### What Scaffolding Could Fix
- Output format (with iteration)
- Field structure (with "domestication")
- Batch sizing (through segmentation)
- Cross-contamination (through session isolation)

### What Scaffolding Could NOT Fix
- Fabrication tendencies (only model selection helped)
- Citation accuracy ("vibes were fantastic...half the sources didn't exist")
- "Australian English. Non-sensational report titles. Just no"
- Temporal reasoning ("temporality blindness")

### Cost of Scaffolding
- 8 prompt versions for metadata
- ~$200 in API credits for OpenArchaeo enhancement
- "7 hours to get through the 20 [DR sessions], since it's 10min per with no notification" (Brian, 23 Feb)
- Human time for: batch management, output validation, reprompting

---

## 8. Model-Specific Observations

### OpenAI Deep Research
- "The seams are REALLY showing" (Brian, 13 Feb)
- Inconsistent outputs: "DR has just stopped putting the tool name in the first column of the CSV" despite same prompt (25 Feb)
- Rate limits: "100 DR uses/mo" (14 Feb), "20 a day" (23 Feb)
- "It simply WILL NOT follow URLs, it just starts searching instead" (19 Feb)
- Non-deterministic: different results on re-runs

### Claude Research
- Released mid-April 2025, accessible to Brian by 2 May
- "Anthropic's Research...is just fucking useful" (Brian, 6 May)
- "Claude research for writing code is **impressive**" (Brian, 6 May)
- Limitations: wouldn't produce CSV in single pass, ignored style preferences
- "Claude just gets on with the job" vs other models (Brian, 7 May)

### Gemini
- "Gemini is a fucking jerk" (Brian, 20 Apr)
- "it reflects their culture perfectly" (Brian, 20 Apr)
- Good for transcription: "I reach for it for transcription all of the time" (Brian, 20 Apr)
- Bad for research: "just made a bunch of crap up" (Shawn, 2 May)
- Version confusion: "Gemini still mixes things up" (Shawn, 2 May)

### o3
- "o3 is a lying liar who lies" (Brian, 7 May)
- Made up tool references by recombining real author names
- "o3... doesn't change my fundamental opinions" (Brian, 21 Apr)

### Computer Use / Operator
- Computer Use: "$1 of Claude 3.5 sonnet credits did not manage to get even a set of URLs from the library web page"
- "failure to click, failure to right click, failure to change apps between firefox and libreoffice"
- Operator: "fascinating to watch in action, slow though"

---

## 9. Methodological Insights for Paper

### Evidence for "Technoscholasticism" Thesis

1. **Authority over reality**: Models privilege textual sources over critical assessment
2. **Fabrication patterns**: "vibes were fantastic...half the sources didn't exist"
3. **Temporal blindness**: Unable to assess currency/validity of sources
4. **Lack of epistemic humility**: Confident assertions about fabricated content

### Evidence for "Scaffolding Overcomes but Doesn't Eliminate"

1. **V1→V8 evolution**: 8 versions to achieve reliable metadata output
2. **Session isolation**: Required to prevent confabulation
3. **Batch constraints**: Discovered empirically, imposed by humans
4. **Persistent failures**: CSV, titles, spelling despite extensive prompting

### Key Quote for Paper

"I quite like the following in o1... The second task is shockingly useful: getting the paper's argumentation is a wonderful way to see what the fuck they're claiming" (Brian, 20 Feb) — Shows models useful for synthesis but not judgment.

---

## 10. Open Questions for Interview

1. **February DR sessions**: Can you characterise what "seams showing" meant specifically? What behaviours indicated unreliability?

2. **Hugging Face ODR $200 run**: What was the quality vs cost trade-off? Were the enhanced descriptions usable?

3. **Evidence collection evolution**: What changes between V1 (122 lines) and V7 (56 lines) of the evidence prompt? What drove simplification?

4. **Temporal blindness examples**: Can you provide specific examples where models failed to assess recency appropriately?

5. **Model personality**: You both keep returning to Claude despite "hearing Gemini and o3 are better" — can you articulate what makes Claude's failures more tolerable?

---

## 11. Files Referenced in Chat (for follow-up)

### Shared Chat Links
- DR lit review: https://chatgpt.com/share/67aec308-c2d8-800c-a33b-a9b0024ca241
- Software Tool Extraction: https://chatgpt.com/share/67aee08c-6118-8004-9d58-94f36391bad0
- Abstract generator: https://claude.ai/share/3ed25401-2bd8-48a7-82ab-075cfbcd65a8
- Brian's paper transcript cleaning: PDF shared
- htmltoc check: https://chatgpt.com/share/6813dd01-0600-800c-acb7-73e85a8b45d4

### Spreadsheets
- llm-research-master: https://docs.google.com/spreadsheets/d/174a25huZWL2ttK...
- 02-tool-metadata: https://docs.google.com/spreadsheets/d/1GO1nBF3LC-lK5CqnyuzA8...
- tool-evidence: https://docs.google.com/spreadsheets/d/15Kn0BUSheDhcLN0osQ86d...

### Repositories
- open-deep-research-openarcheo-iterator: https://github.com/Denubis/open-deep-research-openarcheo-iterator
- GitHistoryToCSV: https://github.com/Denubis/GitHistoryToCSV

---

*This analysis covers approximately the first 4000 lines of the Google Chat history, Feb–May 2025.*
