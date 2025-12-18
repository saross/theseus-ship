# Streamlined Questions for Brian

## Context
These questions emerged from systematic analysis of the discovery and evidence spreadsheets. Shawn is reviewing chat transcripts and communications to answer what he can; remaining questions are for Brian.

---

## Priority Questions (Essential for Paper)

### 1. JOAD Wholesale Fabrication
My analysis identified entries 26-40 in `JOAD-extreme fail` as wholesale fabrication - both article titles AND tool names invented (CeramicNet, ArtifactML, Reconstructo, VRArchaeo, LandML, etc.).

**Q: Does this match your recollection? Were any of these investigated before being identified as fake?**

### 2. IA 31-67 Failure
The failed run (200 articles â†’ 18 tools) contrasts sharply with the successful run (674 articles â†’ 97 tools).

**Q: What was different about the prompt or approach between these runs?**

### 3. Evidence Collection Model Comparison
The final dataset shows 95% from ChatGPT DR.

**Q: Can you give a rough sense of how Claude vs ChatGPT DR compared in evidence yield when you tested them? What made ChatGPT DR dominant?**

---

## Clarification Questions (Important for Accuracy)

### 4. JOSS o3 Red Highlighting
The `JOSS-worthless-o3` sheet shows red-highlighted entries.

**Q: Was this manual review highlighting (you marking problems) or something from the model output?**

### 5. FAIMS Fragmentation Pattern
Claude produced 4 separate entries for FAIMS (FAIMS, FAIMS Mobile Platform, FAIMS 3.0, Fieldmark).

**Q: Was this from a single prompt, or did it persist across multiple attempts? Did other tools with version history show similar fragmentation?**

### 6. Gemini Evidence Behaviour
You mentioned Gemini had Wayback Machine snapshot duplication issues.

**Q: Can you briefly describe what this looked like - multiple rows for the same snapshot, or something else?**

---

## Lower Priority (Nice to Have)

### 7. DR Session Count
For order-of-magnitude purposes:

**Q: Roughly how many ChatGPT Deep Research sessions were run for evidence collection? (10s? 50s? 100s?)**

### 8. Tool Verification Rate
Of the 29 tools in `JOSS-worthless-o3`, some appear verifiable (tidypaleo, archaeoviz) while others are confabulated (archr).

**Q: Do you recall what proportion ended up being verifiable vs fake?**

---

## Already Resolved

- **Coverage split (861/302)**: Emerged organically; Brian worked Aâ†’, Shawn worked â†Z
- **Gemini CSV issue**: Correction - Gemini DID produce CSVs; the problem was version confusion
- **Claude CSV refusal**: Happened during research phase; always required follow-up prompt

---

*Questions compiled from December 2025 analysis session. Please answer whatever you can recall - rough estimates are fine where exact numbers aren't available.*