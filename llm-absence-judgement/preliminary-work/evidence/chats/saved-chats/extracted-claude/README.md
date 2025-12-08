# Extracted Claude Conversations

*Extracted: 8 December 2025*

This folder contains Claude.ai conversations related to the "Absence of Judgement" research project, extracted from a bulk export using `scripts/parse_claude_export.py`.

## Extraction Summary

- **Source**: `bulk-exports/Claude-data-2025-12-07-20-26-23-batch-0000/conversations.json`
- **Total conversations in export**: 610
- **Extracted (matching project UUIDs)**: 40
- **Date range**: February–May 2025

## Contents by Category

### Early Exploration (February 2025)

| File | Description |
|------|-------------|
| `2025-02-16_preserving-digital-humanities-research-data.md` | Initial exploration of research data preservation |
| `2025-02-21_evaluating-archaeology-software-dataset.md` | Early dataset evaluation work |

### Prompt Development and Testing (May 2025)

The bulk of the conversations document the V1→V8 prompt evolution for metadata collection:

| Version | Files | Key Developments |
|---------|-------|------------------|
| V1 | `v1-faims-metadata.md` | Initial prompt attempt |
| V2 | `v2-faims-metadata-and-prompt-improvement.md` (111KB) | Major prompt revision session |
| V3 | `v3-faims-metadata.md` | Refined prompt |
| V4 | `v4-ade4-metadata.md`, `v4-faims-metadata.md`, `v4-vosviewer-metadata.md` | Testing across multiple tools |
| V5 | `v5-ad4-metadata.md` | Continued refinement |
| V6 | `v6-ade4-metadata.md`, `v6-wsg-ade4-metadata.md` | Further testing |
| V7 | `v7-ade4-metadata.md`, `v7-agisoftphotoscan-metadata-and-prompt-improvemen.md` (62KB) | Major prompt improvement session |
| V8 | 22 files | Final prompt version, used for bulk metadata collection |

### Notable Conversations

- **`2025-05-01_defining-research-software-tools.md`** — Conceptual work on tool definitions
- **`2025-05-06_v8-bwigg-metadata-fail.md`** — Documented failure case (tool not found)
- **`2025-05-06_v8-depthmapx-metadata-nocsv.md`** / `v8-depthmapx-metadata-csv.md` — Paired files showing CSV generation requiring separate request

## Observations

1. **Prompt improvement chats are large**: The `v2-faims-metadata-and-prompt-improvement.md` (111KB) and `v7-agisoftphotoscan-metadata-and-prompt-improvemen.md` (62KB) files contain detailed discussions of prompt refinement.

2. **V8 was the production version**: 22 of 40 conversations use V8, indicating this was the final prompt used for bulk metadata collection.

3. **CSV generation was a consistent issue**: The paired depthmapx files and the documented "nocsv" suffix confirm the Google Chat observation that Claude required a separate request to produce CSV output.

4. **Failure cases were documented**: The `bwigg-metadata-fail.md` file shows a case where the tool couldn't be found.

## Usage Notes

Each file contains:
- Conversation UUID and URL for reference
- Timestamps for each message
- Full conversation thread in markdown format

Tool use blocks appear as placeholder text (e.g., "This block is not supported on your current device yet") due to limitations in the export format.
