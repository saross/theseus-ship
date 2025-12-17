# Verification To-Do List

**Last updated:** 2025-12-18

Short-term to-do items for manual human review during tool discovery verification.

---

## Pending Manual Review

(None - all items completed)

---

## Completed Manual Reviews

### Line 106: Virtual Amarna Project - 2025-12-18
- **Article:** Developing a 3-D Digital Heritage Ecosystem (Limp et al., IA issue 30)
- **URL:** https://intarch.ac.uk/journal/issue30/limp_index.html
- **Original status:** CONFIRMED
- **Corrected to:** MISATTRIBUTED
- **Evidence:** Virtual Amarna Project is a digital archive/dataset of 3D scanned archaeological objects (ADS DOI: 10.5284/1011330), not a software tool. Primary function is to display and store static 3D models. Does not meet tool definition - excluded as dataset without active computational engagement.

### Line 49: pnuts - 2025-12-15
- **Original status:** DISCOVERY_ERROR
- **Corrected to:** CONFIRMED
- **Evidence:** Editorial describes "pnuts version four" as "Previous, Next, Up, Top and Search" navigation script (John Frank, WN server). IA publication utility similar to htmltoc/htmlfig.

### Line 81: Grid Machine 6.53 - 2025-12-15
- **Original status:** DISCOVERY_ERROR
- **Corrected to:** CONFIRMED
- **Evidence:** Found in §3: "The Extension Grid Machine Version 6.53 was used to convert each of the ADIs into a points theme." ArcView extension with archaeological applications.

### Line 109: Sketchfab - 2025-12-15
- **Original status:** DISCOVERY_ERROR
- **Verified as:** DISCOVERY_ERROR (correct)
- **Evidence:** Article uses Unity WebGL Player (Figure 16, /guild-chapel/index.html), NOT Sketchfab. Hallucination confirmed.

---

## Notes

- Items are added when web fetch cannot access full article content
- Items are added when there's ambiguity requiring human judgement
- Cross-reference tools against `02-tool-metadata.xlsx` - if listed on 'Tools' tab, tool is confirmed
- **Workflow improvement (2025-12-15):** Always check full article sections (not just summary/TOC) before classifying as DISCOVERY_ERROR
