# Extracted ChatGPT Conversations (Official Export)

*Extracted: 8 December 2025*

This folder contains ChatGPT conversations from the official OpenAI data export, filtered to the "Theseus' Ship" project and the February–May 2025 date range.

## Extraction Summary

- **Source**: `bulk-exports/ChatGPT-data-2025-12-07/conversations.json`
- **Total conversations in export**: 227
- **Filtered by project (gizmo_id)**: 42 conversations
- **Filtered by date range (Feb–May 2025)**: 41 conversations
- **Extraction script**: `scripts/parse_chatgpt_export.py`

## Advantages Over Third-Party Exports

The official OpenAI export provides richer metadata than the third-party ChatGPT Exporter tool:

| Feature | Official Export | Third-Party Export |
|---------|----------------|-------------------|
| **Model per message** | Yes (e.g., `o3-mini-high`, `research`, `gpt-4-5`) | No |
| **Precise timestamps** | Per-message Unix timestamps | Conversation-level only |
| **Conversation ID** | Full UUID | Share link only |
| **Project ID** | gizmo_id for filtering | Not available |
| **Request IDs** | Available for debugging | Not available |

## Content Categories

### Literature Review & Conceptual Work (February 2025)

- `2025-02-09_bibtex-reference-completion.md`
- `2025-02-11_lit-review-research-software-sustainability.md`
- `2025-02-23_improve-resource-descriptions.md`
- `2025-02-23_tool-definition-assessment.md`
- `2025-02-23_research-tool-evidence-collection.md`

### V7 Metadata Collection (February 2025)

Multiple tool-specific metadata sessions using the V7 prompt:
- French tools: `v7-le-stratifiant`, `v7-chronophage`, `v7-seriographe`, `v7-explographe`
- R packages: `v7-ca`, `v7-osl-calibrationr`, `v7-artefact-morphor`
- Visualisation: `v7-rtibuilder`, `v7-rtiviewer`
- Analysis: `v7-unconstrainedclustering`, `v7-lisa-plc`, `v7-pointpattern`

### Model Comparison Tests (May 2025)

- `v1-metadata-faims-o3.md`, `v1-metadata-faims-dr.md`
- `v2-metadata-faims-o3.md`, `v3-metadata-faims-o3.md`
- `v7-faims-o3-2025-05.md`, `v7-faims-dr-2025-05.md`, `v7-faims-dr-2025-05-run2.md`

### LLM Methodology (April–May 2025)

- `2025-04-19_llms-in-agentic-systems.md`
- `2025-05-03_research-software-metadata-collection.md`

## Model Usage Observed

Based on extracted conversations, the following models were used:
- `o3-mini-high` — Primary reasoning model
- `research` — Deep Research mode
- `gpt-4-5` — Default conversation model

## Comparison with Third-Party Exports

The `extracted-chatgpt/` folder contains the same conversations exported via the third-party "ChatGPT Exporter" browser extension. The official exports in this folder are more complete and should be preferred for:
- Documenting which model was used for each response
- Precise timing analysis
- Audit trail purposes

The third-party exports may be easier to read due to their simpler structure.
