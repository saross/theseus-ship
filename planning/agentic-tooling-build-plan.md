# Agentic tooling for the software-longevity tasks — producer/verifier loops (build plan)

**Status:** Proposed (build not started for the three research tasks; the
literature-discovery loop already exists and works).
**Created:** 2026-07-01.
**Owner:** Shawn.

## Purpose

Outline the approach to building producer/verifier agentic workflows for the
three core tasks of the software-longevity ("Theseus' Ship") study — **tool
discovery, tool documentation, and evidence-of-life gathering** — reusing the
2025 prompt lineage as the base. The tooling is deliberately over-determined:
it is at once

1. **standing operational infrastructure** — run on a weekly (or similar)
   schedule to re-scan for new research software, refresh metadata, and gather
   fresh evidence-of-life, feeding the longevity study its longitudinal
   tool-decay signal;
2. **the empirical substrate for a future paper** on agentic research
   workflows (extensive, at-scale validation — see boundaries below); and
3. **reviewer insurance** for the judgement paper (Paper B,
   `~/Code/2026-mq-llm-dh-judgement-paper-b`).

## Provenance (why this doc exists)

This came out of a Paper B submission-risk discussion (2026-07-01). Paper B
argues that reliability is a property of the human–AI system and that the locus
is the scaffolding — and prescribes an independent-context producer/verifier
architecture. The anticipated reviewer objection:

> You built a producer/verifier loop for **literature search**, but where is the
> loop — and the comparison — for the actual research tasks: **tool discovery,
> documentation, and evidence-gathering**?

The objection is fair and lands squarely on the 2025 case's three core stages
(Paper B §4.3–§4.5). The literature-discovery loop already answers it for one
task, and the 2025→2026 delta there is striking (automated, accurate Zotero
ingest and clean BibTeX where the 2025 commercial tools produced
confabulation-rife output that could not be reliably parsed at all) — but the
three research tasks proper are not yet looped.

**Decision (2026-07-01):** Paper B ships as-is — a conceptual, honestly-hedged
case study; Royal Society Open Science reviews for soundness, not for "do more
experiments". The tooling gets built on our own clock, not gated to Paper B's
submission. The empirical load stays out of Paper B. Full reasoning is in the
Paper B continuity beacon (`wiki/continuity.md`, START HERE, 2026-07-01) and its
session log.

## Strategic frame

The reviewer-demanded demonstration, the weekly operational tooling, and the
future paper's substrate **are the same artefact**. Build it once, for our own
reasons; let it double as insurance.

- **Paper B (judgement)** stays conceptual and cites this work as the natural
  next study. If a reviewer forces the issue, we add at most **one explicitly
  labelled proof-of-concept vignette** — feasibility, not validation.
- **Future paper (agentic workflows)** carries the empirical load: extensive
  runs, at scale, quantified comparison, ablations. Its contribution is the
  **validation and the operational findings**, never "we built it".
- **"Theseus' Ship" (longevity)** consumes the weekly runs as longitudinal data
  on tool survival, succession, and decay.

## Architecture: the paper's own three moves, instantiated

Each task is a **producer/verifier pair**:

- **Producer** — performs the task from decomposed, externalised prompts (the
  2025 lineage below). Narrow remit per call: the recurring 2025 lesson was that
  *narrowing* the model's task, not widening it, produced consistent output.
- **Verifier** — re-checks each atomic claim, and must embody the three
  properties Paper B argues give a guard its catching power:
  1. **Context independence** — a separate context, working from the *artefact*,
     not the producer's reasoning. (The 2025 o3 episode: a second model handed
     the first's output *in shared context* caught nothing, reproducing a
     fabricated list one-to-one. Independence of context, not a sterner
     instruction, is the lever.)
  2. **External re-grounding** — re-ground each claim against **independent
     external evidence** (registries, repositories, the tool's own homepage, the
     cited source itself), not against the producer's assertion. Agreement among
     sources of common origin is a cue, not a check.
  3. **Orthogonal framing** — change the question, not just the questioner:
     retrieve-then-assess rather than read-and-confirm.

**Grounding via helper scripts.** Isolate mechanical retrieval from judgement, so
only the synthesis surface needs guarding — the pattern the existing
literature-discovery loop already uses (the `lit-scout` agent + its
`lit-search.py` helper wrapping the CrossRef, DataCite, and OpenAlex application
programming interfaces (APIs); in the `personal-assistant` repo). Generalise that
helper to wrap registry lookups, repository/homepage fetches, and web-archive
(Wayback) queries for the three loops.

## The three loops

The 2025 prompt lineage lives in **`~/Code/LLM-History-Paper/prompts/`** (migrated
out of this repo — theseus-ship's README still points at the old
`llm-absence-judgement/prompts-library-tools/` path, which is now stale). Each
loop reuses its lineage as the producer and guards the *documented* 2025 failure
mode with the verifier.

### 1. Tool discovery

- **Producer base:** `prompts/01-tool-discovery.tex` (+
  `prompts/openarchaeo-preliminary/v1–v3`).
- **2025 failure modes to guard (Paper B §4.3):** "DOI-sequence-walking"
  (inventing tools whose identifiers march through a journal's numbering space);
  silent mode-drop into "simulate a plausible list of articles"; confabulation
  that **tracked the journal, not the model**; plausible near-misses (e.g.
  ArchABM naming a real air-quality package).
- **Verifier:** for each candidate, retrieve the actual artefact (repository,
  homepage, registry record) and decide existence from *that*, not from the
  producer's claim. Orthogonal framing defeats DOI-walking: the invented
  identifier resolves to nothing retrievable.
- **Output:** verified tool list + rejected-candidate log (confabulation rate).

### 2. Tool documentation

- **Producer base:** `prompts/02-tool-metadata-v8.tex` (the 34-field schema at
  the end of the V2→V8 lineage in `prompts/tool-metadata/`). Carries the
  hard-won design moves — *domestication* (absorb a model's persistent tendency
  into the schema rather than forbidding it) and *working with the grain*
  (formalise spontaneously useful behaviour).
- **2025 failure modes to guard (Paper B §4.4):** the **binary failure mode** on
  familiar tools (a record is complete-and-accurate or it fails entirely, e.g. by
  writing an essay about the software *category*); version confusion; "spawning"
  related tools instead of documenting the one requested; classification
  instability resting on fabricated domain relevance.
- **Verifier:** re-check each field against independent ground truth; exploit the
  binary failure mode (errors announce themselves) so the verifier concentrates
  on real-vs-fabricated rather than auditing every field.
- **Output:** verified metadata records + failure taxonomy.

### 3. Evidence-of-life

- **Producer base:** `prompts/03-tool-evidence-v7.tex` (+
  `prompts/tool-evidence/v1,v5`). Keeps the **one-row-per-sighting** schema (the
  inversion from a brittle many-column synthesis format) and the conservative
  guardrail — *"if there is any doubt, there is no doubt"* — that suppresses
  confabulation at an acknowledged cost in recall; synthesis prohibited at
  source.
- **2025 failure modes to guard (Paper B §4.5):** event-level errors embedded in
  otherwise-sound output — fabricated attributions to real sources; the ArboDat
  case (a machine-readable "last updated" timestamp preferred over the
  human-readable sentence "developed since 1997" on the same page); same-name
  collisions across fields; the most-documented tool drawing the largest share
  of fabrication.
- **Verifier:** three checks per event, re-grounded against the **source itself**
  (correspondence, not mere retrieval): the source exists, it mentions the right
  tool, its stated year matches. Orthogonal framing (read what the source
  actually says) is what catches the timestamp-vs-text class.
- **Output:** verified evidence events + per-tool temporal footprint.

## Comparison design (the "where is your comparison?" answer)

The tooling must **log enough to support** the following comparisons. These are
the future paper's payload — build the instrumentation now, run the analysis
later.

- **Producer-only vs producer+verifier** — does the independent verifier catch
  what unaided output ships? (catch rate).
- **Independent-context vs shared-context verifier** — the central Paper B claim,
  turned into an ablation. The 2025 o3 episode predicts the shared-context arm
  catches ≈nothing; the future paper can measure the gap.
- **2026 agentic loop vs 2025 commercial-tool baseline** — a comparison against a
  *real historical baseline*: the 2025 outputs and their verification outcomes
  already exist (`~/Code/LLM-History-Paper/evidence/` and the tool/evidence
  datasets). This is where the striking delta is quantified.
- **Metrics:** confabulation/error rate, verifier catch rate, precision/recall
  against ground truth, human-correction burden, cost, and latency.
- **Ground truth:** FAIMS and other tools the authors built or maintain
  first-hand (the hard ground truth used in 2025), plus the OpenArchaeo
  catalogue.

## MVP scope vs full-validation scope

- **MVP (proof-of-concept / reviewer insurance, only if forced):** one loop per
  task, a small run over a known slice, showing the architecture instantiates and
  catches representative errors. Light; explicitly feasibility, not validation;
  clearly walled off from the future paper.
- **Full validation (future paper):** extensive runs at scale, the ablations
  above, quantified comparison to the 2025 baseline, and longitudinal weekly
  operation.

## Boundaries and guardrails

- **Keep the empirical load out of Paper B.** No rates, no benchmarks, no
  ablations in that manuscript. At most one labelled proof-of-concept vignette.
- **"We built it" is not a publishable contribution.** The future paper's worth
  is the validation and operational findings — protect that novelty by not
  spending it here.
- **API review gate.** Every batch large-language-model run needs model / count /
  cost sign-off before launch (standing rule). Note each conservative default
  (serial vs concurrent, sample vs full corpus) when scoping a run.

## Build phases

- [ ] **Phase 0 — inventory.** Confirm and read the 2025 lineage in
      `~/Code/LLM-History-Paper/prompts/` (discovery / metadata-v8 / evidence-v7)
      and the 2025 outputs + verification data in `.../evidence/`; locate the
      existing `lit-scout` / `lit-search.py` loop in `personal-assistant` as the
      pattern to generalise.
- [ ] **Phase 1 — skeleton.** Generalise the literature-discovery producer/
      verifier loop into a reusable per-task skeleton (producer agent,
      independent-context verifier agent, grounding helper, structured logging).
- [ ] **Phase 2 — discovery loop.**
- [ ] **Phase 3 — documentation loop.**
- [ ] **Phase 4 — evidence-of-life loop.**
- [ ] **Phase 5 — comparison harness.** Logging + config for producer-only vs
      +verifier, shared vs independent context, and the 2025 baseline.
- [ ] **Phase 6 — schedule.** Weekly (or similar) runs; wire outputs into the
      longevity dataset.

Each phase with a batch run passes the API review gate first.

## Open questions

- **Framework:** reuse Claude Code (the literature loop is already there) vs
  alternatives — default to reuse.
- **Corpus:** re-run the 2025 journals for a like-for-like baseline vs extend to
  new venues (probably both — baseline first).
- **Verifier model:** same family as producer (watch circularity) vs a
  deliberately different family for the independence arm.
- **Scheduling home:** cron/routine in `personal-assistant` vs this repo.

## Relationship to the papers and repos

- **Paper B — judgement** (`~/Code/2026-mq-llm-dh-judgement-paper-b`): conceptual;
  cites this as future work; stays hedged.
- **Future paper — agentic workflows:** the extensive-validation study built on
  this tooling.
- **"Theseus' Ship" — longevity** (this repo): the weekly runs feed its
  longitudinal tool-survival data.
- **Paper A — "Absence of Judgement"** (`~/Code/LLM-History-Paper`): source of the
  2025 prompt lineage and the empirical baseline reused here.
