# Section 4 Consistency Notes

**Created**: 2025-01-14
**Status**: To review after Tool Discovery editing complete

---

## Observation: Structure Mismatch Between 4.3 and 4.4

### Literature Discovery (4.3)
- ~70 lines prose across 5 subsubsections
- **Per-service structure**: ChatGPT DR (3 para), Perplexity (1 para), Elicit (1 para), Claude/Gemini (1 para)
- Detailed qualitative descriptions per service (output composition, specific error examples like "oil field decommissioning")
- Source Synthesis subsection
- Comparative Performance with 2 tables + 2 closing paragraphs

### Tool Discovery (4.4) after consolidation
- ~50 lines prose across 3 subsubsections
- **Consolidated structure**: Results (3 para + 2 tables), Confabulation Patterns (4 para), Verification Outcomes (1 para + 1 table)
- Tables do more of the per-service/per-journal work
- Detailed confabulation analysis (JOAD fabrication, DOI walking)

### Key Difference
- Lit Discovery: granular per-service prose
- Tool Discovery: consolidated with tables carrying per-service detail

### Note
Tool Discovery doesn't need per-service expansion since 95% of tools came from ChatGPT DR.

---

## Recommendation

Condense Literature Discovery to match Tool Discovery's table-centric approach:
- Reduce per-service prose
- Let tables speak for quantitative comparisons
- Keep qualitative observations (error examples, synthesis limitations) but consolidate

---

## To Do

- [x] Complete Tool Discovery section editing (Confabulation Patterns, Verification Outcomes) — 2025-01-14
- [x] Reconcile table data with source CSV (tool-discovery-granular.csv) — 2025-01-14
- [ ] Compare both sections in entirety
- [ ] Decide on consolidation approach for Literature Discovery

## Data Reconciliation Summary (2025-01-14)

Tables updated with correct counts from `tool-discovery-granular.csv`:
- **242 unique tools** (was incorrectly 203/230)
- **154 verified** (was 130/143)
- **52 misattributed** (was 54)
- **35 confabulated** (was 49/35)

Key finding: All 14 o3 confabulated tools were also confabulated by ChatGPT DR (shared confabulation modes).

Removed redundant Table 3 (tab:discovery-verification) — information now in Journal table.
