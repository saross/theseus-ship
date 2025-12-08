#!/usr/bin/env python3
"""
ChatGPT Official Export Parser for Prompt Development Corpus

This script extracts conversations from an official ChatGPT JSON export, filtering to:
1. A specific project (identified by gizmo_id)
2. A specific date range (February - May 2025)

Usage:
    python parse_chatgpt_export.py <path_to_conversations.json> [output_directory]

The export can be obtained from ChatGPT:
    Settings → Data controls → Export data (takes ~24 hours)

Output:
    Individual markdown files for each conversation, named:
    YYYY-MM-DD_conversation-title-slug.md

Advantages over third-party exports:
    - Exact model information (model_slug) per message
    - Precise timestamps per message
    - Full conversation tree structure
    - Request IDs for debugging
    - Complete metadata
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


# =============================================================================
# Configuration
# =============================================================================

# Date range for filtering (inclusive)
DATE_RANGE_START = datetime(2025, 2, 1)
DATE_RANGE_END = datetime(2025, 5, 31, 23, 59, 59)

# Project gizmo ID (identifies the "Theseus' Ship" project in ChatGPT)
# This is the equivalent of filtering by project in the ChatGPT interface
PROJECT_GIZMO_ID = "g-p-682fbda4eb1c819180b176f6de9d9cd8"


# =============================================================================
# Helper Functions
# =============================================================================

def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:50]


def timestamp_to_datetime(ts: float) -> Optional[datetime]:
    """Convert Unix timestamp to datetime."""
    if ts is None:
        return None
    try:
        return datetime.fromtimestamp(ts)
    except (ValueError, OSError):
        return None


def format_role(role: str) -> str:
    """Normalise message role to Human/Assistant/System."""
    role_map = {
        'user': 'Human',
        'assistant': 'Assistant',
        'system': 'System',
        'tool': 'Tool',
    }
    return role_map.get(role.lower(), role.title())


def extract_messages_from_mapping(mapping: dict) -> list:
    """
    Extract messages from the conversation mapping in chronological order.

    The mapping is a tree structure with parent/children relationships.
    We traverse it to get messages in order.
    """
    messages = []

    # Build a lookup and find the root
    nodes = {}
    root_id = None

    for node_id, node in mapping.items():
        nodes[node_id] = node
        if node.get('parent') is None:
            root_id = node_id

    if not root_id:
        # Fallback: look for 'client-created-root' or similar
        for node_id in mapping:
            if 'root' in node_id.lower():
                root_id = node_id
                break

    if not root_id:
        return messages

    # Traverse the tree depth-first, following children
    def traverse(node_id: str):
        if node_id not in nodes:
            return

        node = nodes[node_id]
        msg = node.get('message')

        if msg and msg.get('content'):
            content = msg.get('content', {})
            parts = content.get('parts', [])

            # Skip empty messages
            if parts and any(p for p in parts if p):
                messages.append({
                    'id': msg.get('id'),
                    'role': msg.get('author', {}).get('role', 'unknown'),
                    'content': parts,
                    'create_time': msg.get('create_time'),
                    'model_slug': msg.get('metadata', {}).get('model_slug'),
                    'status': msg.get('status'),
                })

        # Follow children (usually just one, but could branch)
        for child_id in node.get('children', []):
            traverse(child_id)

    traverse(root_id)
    return messages


def format_message_content(parts: list) -> str:
    """Format message content parts into readable text."""
    text_parts = []

    for part in parts:
        if isinstance(part, str):
            text_parts.append(part)
        elif isinstance(part, dict):
            # Handle different content types
            content_type = part.get('content_type', '')
            if content_type == 'image_asset_pointer':
                text_parts.append('[Image]')
            elif content_type == 'code':
                code = part.get('text', '')
                lang = part.get('language', '')
                text_parts.append(f"```{lang}\n{code}\n```")
            else:
                # Generic fallback
                text_parts.append(str(part))

    return '\n'.join(text_parts)


def conversation_to_markdown(conversation: dict) -> str:
    """Convert a conversation to markdown format."""
    title = conversation.get('title', 'Untitled')
    conv_id = conversation.get('conversation_id', conversation.get('id', 'unknown'))
    create_time = timestamp_to_datetime(conversation.get('create_time'))
    update_time = timestamp_to_datetime(conversation.get('update_time'))
    model_slug = conversation.get('default_model_slug', 'unknown')
    gizmo_id = conversation.get('gizmo_id', '')

    # Extract messages
    mapping = conversation.get('mapping', {})
    messages = extract_messages_from_mapping(mapping)

    # Build markdown
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("## Metadata")
    lines.append(f"- **Conversation ID:** `{conv_id}`")
    if create_time:
        lines.append(f"- **Created:** {create_time.strftime('%Y-%m-%d %H:%M:%S')}")
    if update_time:
        lines.append(f"- **Updated:** {update_time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- **Default Model:** `{model_slug}`")
    if gizmo_id:
        lines.append(f"- **Project ID:** `{gizmo_id}`")
    lines.append(f"- **Source:** Official ChatGPT Export")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Conversation")
    lines.append("")

    # Process messages
    for msg in messages:
        role = format_role(msg['role'])

        # Skip system messages (usually just context setup)
        if role == 'System':
            continue

        # Format timestamp
        msg_time = ""
        if msg['create_time']:
            dt = timestamp_to_datetime(msg['create_time'])
            if dt:
                msg_time = f" ({dt.strftime('%H:%M:%S')})"

        # Format model info for assistant messages
        model_info = ""
        if role == 'Assistant' and msg.get('model_slug'):
            model_info = f" [Model: {msg['model_slug']}]"

        lines.append(f"### {role}{msg_time}{model_info}")
        lines.append("")

        # Format content
        content = format_message_content(msg['content'])
        lines.append(content)
        lines.append("")
        lines.append("---")
        lines.append("")

    return '\n'.join(lines)


# =============================================================================
# Main Processing
# =============================================================================

def process_export(export_path: Path, output_dir: Path) -> None:
    """Process the ChatGPT export and extract filtered conversations."""

    print(f"Loading export from: {export_path}")

    # Load the export file
    with open(export_path, 'r', encoding='utf-8') as f:
        conversations = json.load(f)

    print(f"Found {len(conversations)} total conversations in export")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process and filter conversations
    extracted_count = 0
    skipped_not_in_project = 0
    skipped_out_of_range = 0

    for conv in conversations:
        conv_id = conv.get('conversation_id', conv.get('id', ''))
        gizmo_id = conv.get('gizmo_id', '')

        # Filter by project (gizmo_id)
        if gizmo_id != PROJECT_GIZMO_ID:
            skipped_not_in_project += 1
            continue

        # Filter by date range
        create_time = conv.get('create_time')
        if create_time:
            dt = timestamp_to_datetime(create_time)
            if dt and not (DATE_RANGE_START <= dt <= DATE_RANGE_END):
                skipped_out_of_range += 1
                continue

        # Extract and format
        title = conv.get('title', 'Untitled')
        dt = timestamp_to_datetime(create_time) if create_time else None
        date_str = dt.strftime('%Y-%m-%d') if dt else 'unknown-date'

        # Generate filename
        title_slug = slugify(title)
        filename = f"{date_str}_{title_slug}.md"
        filepath = output_dir / filename

        # Handle duplicate filenames
        counter = 1
        while filepath.exists():
            filename = f"{date_str}_{title_slug}_{counter}.md"
            filepath = output_dir / filename
            counter += 1

        # Convert to markdown and save
        markdown = conversation_to_markdown(conv)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  Extracted: {filename}")
        extracted_count += 1

    # Summary
    print("")
    print("=" * 60)
    print("EXTRACTION SUMMARY")
    print("=" * 60)
    print(f"Total conversations in export:     {len(conversations)}")
    print(f"Skipped (not in project):          {skipped_not_in_project}")
    print(f"Skipped (outside date range):      {skipped_out_of_range}")
    print(f"Extracted to markdown:             {extracted_count}")
    print(f"Output directory:                  {output_dir}")
    print("")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nError: Please provide path to ChatGPT conversations.json file")
        print("\nExample:")
        print("  python parse_chatgpt_export.py ~/Downloads/ChatGPT-data/conversations.json")
        print("  python parse_chatgpt_export.py conversations.json ./output_conversations")
        sys.exit(1)

    export_path = Path(sys.argv[1])

    if not export_path.exists():
        print(f"Error: Export file not found: {export_path}")
        sys.exit(1)

    # Output directory (default or specified)
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2])
    else:
        output_dir = Path("./chatgpt_extracted")

    process_export(export_path, output_dir)

    print("Done! You can now use these markdown files for analysis.")


if __name__ == "__main__":
    main()
