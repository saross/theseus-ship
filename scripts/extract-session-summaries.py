#!/usr/bin/env python3
"""
Extract condensed summaries from archived CC sessions for metadata generation.

Reads each archived session's compressed JSONL and produces a compact
JSON summary containing the first few human and assistant messages,
tool usage patterns, and session statistics. This provides enough
context for an LLM to generate quality metadata (title, purpose, tags,
three_ps) without reading the full transcript.

Usage:
    # Extract summaries for all archived sessions
    python scripts/extract-session-summaries.py

    # Extract for specific session directories
    python scripts/extract-session-summaries.py --sessions \
        2026-01-13T06-50_179adf8a 2026-02-03T03-10_93e4d187

    # Output to a specific file
    python scripts/extract-session-summaries.py -o summaries.json

Created: 2026-02-03
"""

import argparse
import gzip
import json
from pathlib import Path
from typing import Any


# =============================================================================
# Configuration
# =============================================================================

ARCHIVE_DIR = Path(__file__).parent.parent / "archive" / "cc-sessions"

# Extraction limits — enough for metadata, not overwhelming
MAX_HUMAN_MESSAGES = 5
MAX_ASSISTANT_TEXTS = 3
HUMAN_MSG_TRUNCATE = 300  # chars
ASSISTANT_MSG_TRUNCATE = 200  # chars


# =============================================================================
# Extraction Logic
# =============================================================================

def extract_text_from_content(content: Any) -> str:
    """
    Extract plain text from a message's content field.

    Handles both string content and list-of-blocks content
    (common in CC JSONL format).

    Args:
        content: Message content — either a string or a list of
            content blocks (dicts with "type" and "text" fields).

    Returns:
        Concatenated text content.
    """
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        texts = []
        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text":
                    texts.append(block.get("text", ""))
                elif block.get("type") == "tool_result":
                    # Tool results in user messages (agent sessions)
                    result_content = block.get("content", "")
                    if isinstance(result_content, str):
                        texts.append(f"[tool_result: {result_content[:80]}]")
                    elif isinstance(result_content, list):
                        for sub in result_content:
                            if isinstance(sub, dict) and sub.get("type") == "text":
                                texts.append(
                                    f"[tool_result: {sub.get('text', '')[:80]}]"
                                )
            elif isinstance(block, str):
                texts.append(block)
        return " ".join(texts)

    return str(content)


def extract_session_summary(session_dir: Path) -> dict[str, Any]:
    """
    Extract a condensed summary from an archived session.

    Reads the compressed JSONL and the existing session.meta.json
    to produce a compact representation suitable for metadata
    generation.

    Args:
        session_dir: Path to the session archive directory
            (containing session.jsonl.gz and session.meta.json).

    Returns:
        Dictionary with condensed session information.
    """
    meta_path = session_dir / "session.meta.json"
    gz_path = session_dir / "session.jsonl.gz"
    jsonl_path = session_dir / "session.jsonl"

    # Load existing metadata for stats context
    metadata = {}
    if meta_path.exists():
        try:
            metadata = json.loads(meta_path.read_text())
        except json.JSONDecodeError:
            pass

    session_info = metadata.get("session", {})
    stats = metadata.get("statistics", {})
    archive_info = metadata.get("archive", {})

    # Determine session type
    session_id = session_info.get("id", session_dir.name)
    is_agent = session_id.startswith("agent-")

    # Extract messages from JSONL
    human_messages: list[str] = []
    assistant_texts: list[str] = []
    tool_names_used: list[str] = []

    # Choose the right file and opener
    if gz_path.exists():
        open_fn = gzip.open
        source_path = gz_path
    elif jsonl_path.exists():
        open_fn = open
        source_path = jsonl_path
    else:
        # No JSONL file found
        return _build_summary(
            session_dir, session_id, is_agent, metadata,
            human_messages, assistant_texts, tool_names_used
        )

    with open_fn(source_path, 'rt', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            # Skip non-message entries
            if entry.get("type") == "file-history-snapshot":
                continue

            message = entry.get("message", {})
            role = message.get("role", entry.get("type", ""))
            content = message.get("content", "")

            if role == "user":
                if len(human_messages) < MAX_HUMAN_MESSAGES:
                    text = extract_text_from_content(content)
                    if text.strip():
                        truncated = text.strip()[:HUMAN_MSG_TRUNCATE]
                        human_messages.append(truncated)

            elif role == "assistant":
                # Extract text blocks (skip tool_use, thinking)
                if len(assistant_texts) < MAX_ASSISTANT_TEXTS:
                    text = extract_text_from_content(content)
                    if text.strip():
                        truncated = text.strip()[:ASSISTANT_MSG_TRUNCATE]
                        assistant_texts.append(truncated)

                # Track tool names
                if isinstance(content, list):
                    for block in content:
                        if (isinstance(block, dict)
                                and block.get("type") == "tool_use"):
                            tool_name = block.get("name", "unknown")
                            if tool_name not in tool_names_used:
                                tool_names_used.append(tool_name)

    return _build_summary(
        session_dir, session_id, is_agent, metadata,
        human_messages, assistant_texts, tool_names_used
    )


def _build_summary(
    session_dir: Path,
    session_id: str,
    is_agent: bool,
    metadata: dict[str, Any],
    human_messages: list[str],
    assistant_texts: list[str],
    tool_names_used: list[str]
) -> dict[str, Any]:
    """
    Build the final summary dictionary.

    Args:
        session_dir: Path to the session archive directory.
        session_id: Session identifier string.
        is_agent: Whether this is an agent sub-session.
        metadata: Loaded session.meta.json contents.
        human_messages: Extracted human message texts.
        assistant_texts: Extracted assistant text blocks.
        tool_names_used: Ordered list of unique tool names.

    Returns:
        Condensed summary dictionary.
    """
    session_info = metadata.get("session", {})
    stats = metadata.get("statistics", {})
    archive_info = metadata.get("archive", {})
    artifacts = metadata.get("artifacts", {})

    # Compressed file size
    gz_path = session_dir / "session.jsonl.gz"
    gz_bytes = gz_path.stat().st_size if gz_path.exists() else 0

    return {
        "dir_name": session_dir.name,
        "session_id": session_id,
        "is_agent": is_agent,
        "started_at": session_info.get("started_at"),
        "duration_minutes": session_info.get("duration_minutes", 0),
        "turns": stats.get("turns", 0),
        "human_messages": stats.get("human_messages", 0),
        "assistant_messages": stats.get("assistant_messages", 0),
        "thinking_blocks": stats.get("thinking_blocks", 0),
        "model": metadata.get("model", {}).get("model_id", "unknown"),
        "tool_calls": stats.get("tool_calls", {}),
        "gz_bytes": gz_bytes,
        "uncompressed_bytes": archive_info.get(
            "jsonl_bytes_uncompressed",
            archive_info.get("jsonl_bytes", 0)
        ),
        "artifacts_created": len(artifacts.get("created", [])),
        "artifacts_modified": len(artifacts.get("modified", [])),
        "artifacts_referenced": len(artifacts.get("referenced", [])),
        "first_human_messages": human_messages,
        "first_assistant_texts": assistant_texts,
        "tool_names_used": tool_names_used,
    }


# =============================================================================
# Session Discovery
# =============================================================================

def find_session_dirs(
    filter_sessions: list[str] | None = None
) -> list[Path]:
    """
    Find all session directories in the archive.

    Scans all project subdirectories (e.g., theseus-ship/, llm-history-paper/)
    for session directories containing session.meta.json.

    Args:
        filter_sessions: Optional list of directory names to include.
            If None, all sessions are included.

    Returns:
        Sorted list of session directory paths.
    """
    session_dirs = []

    for project_dir in ARCHIVE_DIR.iterdir():
        if not project_dir.is_dir():
            continue
        # Skip non-session directories
        if project_dir.name in ("queries",):
            continue

        for session_dir in project_dir.iterdir():
            if not session_dir.is_dir():
                continue
            if not (session_dir / "session.meta.json").exists():
                continue

            if filter_sessions:
                if session_dir.name not in filter_sessions:
                    continue

            session_dirs.append(session_dir)

    return sorted(session_dirs, key=lambda p: p.name)


# =============================================================================
# Main
# =============================================================================

def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Extract condensed session summaries for metadata generation"
    )
    parser.add_argument(
        "--sessions", "-s",
        nargs="+",
        help="Specific session directory names to extract (default: all)"
    )
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="Output JSON file path (default: stdout)"
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output"
    )

    args = parser.parse_args()

    # Find sessions
    session_dirs = find_session_dirs(args.sessions)

    if not session_dirs:
        print("No sessions found.", flush=True)
        return

    print(f"Extracting summaries from {len(session_dirs)} session(s)...",
          flush=True)

    # Extract summaries
    summaries = []
    for session_dir in session_dirs:
        print(f"  {session_dir.name}...", flush=True)
        summary = extract_session_summary(session_dir)
        summaries.append(summary)

    # Output
    indent = 2 if args.pretty else None
    output_json = json.dumps(summaries, indent=indent, ensure_ascii=False)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_json)
        print(f"Wrote {len(summaries)} summaries to {output_path}")
    else:
        print(output_json)

    print("Done!", flush=True)


if __name__ == "__main__":
    main()
