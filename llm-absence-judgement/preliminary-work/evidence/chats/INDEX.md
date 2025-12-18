# Chat Evidence Index

This directory contains LLM conversation transcripts used as evidence in the Absence of Judgement research project.

## Directory Structure

```text
chats/
├── bulk-exports/              # Raw exports from LLM platforms
│   ├── Claude-data-*/         # Claude conversation exports
│   └── chatgpt-exports/       # ChatGPT conversation exports
│
├── saved-chats/               # Organised conversation files
│   ├── Brian-*.pdf            # Brian's exported conversations (PDF)
│   ├── extracted-chatgpt-shawn/  # Shawn's ChatGPT exports (markdown)
│   ├── extracted-claude-brian/   # Brian's Claude exports
│   ├── extracted-claude-brian-md/# Brian's Claude exports (markdown)
│   └── extracted-claude-shawn/   # Shawn's Claude exports
│
├── BBS-SAR-google-chat-history.md  # Google chat coordination log
├── claude_prompt_development_corpus_index.md  # Prompt development index
└── Shawn-chat-links.tex       # LaTeX file with chat references
```

## Bulk Exports

### Claude Exports

Located in `bulk-exports/Claude-data-*/`:

- Full conversation exports from Claude web interface
- Contains `conversations.json`, `projects.json`
- Includes complete message history and metadata

### ChatGPT Exports

Located in `bulk-exports/chatgpt-exports/`:

- Official ChatGPT data export format
- Contains conversation history in JSON format

## Extracted Conversations

Conversations have been extracted and organised by contributor:

### Brian's Conversations

- `Brian-*.pdf` — PDF exports of key Claude sessions
- `extracted-claude-brian/` — Extracted Claude transcripts
- `extracted-claude-brian-md/` — Markdown versions

### Shawn's Conversations

- `extracted-chatgpt-shawn/` — ChatGPT conversation extracts
- `extracted-claude-shawn/` — Claude conversation extracts

## Naming Convention

Extracted conversations follow the pattern:

```text
YYYY-MM-DD_description.md
```

Examples:

- `2025-02-16_preserving-digital-humanities-research-data.md`
- `2025-05-02_v7-faims-metadata.md`

## Extraction Scripts

Conversations were extracted using scripts in `scripts/`:

- `find_missing_conversations.py` — Identify gaps in conversation coverage

## Key Conversation Categories

1. **Prompt Development** — Iterating on discovery/metadata/evidence prompts
2. **Tool Metadata Collection** — v1-v8 metadata prompt runs
3. **Evidence Collection** — Evidence of life gathering sessions
4. **Analysis Sessions** — Working with Claude Code on data analysis

## Notes

- Some bulk exports are excluded from git (large files, privacy)
- See `.gitignore` for exclusion patterns
- Extracted markdown files preserve key research conversations
