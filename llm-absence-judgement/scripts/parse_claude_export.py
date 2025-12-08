#!/usr/bin/env python3
"""
Claude.ai Export Parser for Prompt Development Corpus

This script extracts conversations from a Claude.ai JSON export, filtering to:
1. A specific project (identified by known conversation UUIDs)
2. A specific date range (February - May 2025)

Usage:
    python parse_claude_export.py <path_to_export.json> [output_directory]

The export can be obtained from Claude.ai:
    Settings → Privacy → Export data

Output:
    Individual markdown files for each conversation, named:
    YYYY-MM-DD_conversation-title-slug.md
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

# Known conversation UUIDs from this project (Feb-May 2025)
# Used as a whitelist to identify project conversations
PROJECT_CONVERSATION_UUIDS = {
    "f3023ec2-702f-4553-aa6c-9b9b7b7a8a34",
    "ecb39dda-ac13-44f2-b664-31874fe76dce",
    "21561146-3640-43d8-b645-20084703b462",
    "849d1e45-3fee-4aad-8500-56bc78e7b7d0",
    "2e210f3a-5152-4ef8-9cc0-f8ed2a7872f8",
    "b6592b63-0387-4d57-899b-64ef7a9deda3",
    "5d3c07ca-4fbf-4eae-bbc2-b8b5b6ac04e0",
    "17d43b38-bc37-4e2a-a762-6e610ddb9fa7",
    "da124a03-a346-4655-bb6c-80c61c0eb225",
    "a9305db4-28c8-490e-a9a1-b85c9a6ba2b2",
    "d59ad5f7-a2d3-4d6b-b314-57c7f2e5e753",
    "d9607165-6c5e-4649-baba-482fcea9d764",
    "48087fb6-3b26-4a4b-a8b9-e8c8a8e17ba4",
    "ffca9f05-ceb1-48e9-8e05-136906081303",
    "e58947d8-f5b1-4e05-bcac-ce2b1bfc5117",
    "9508de85-48a3-46da-99d8-5334e940260a",
    "70f47e62-6b6f-4f67-96e3-dd36cf19ce40",
    "415ed51b-513b-4bdc-bdbd-237ce56caeee",
    "4e37f132-88c2-4a3d-a699-e31eb3167dce",
    "6fe826fa-967c-4354-b08d-7c96a6540f9c",
    "a97ab597-66e0-4782-9e82-5dc3b6549eec",
    "e7e67938-e612-4751-a14e-e83e55ef608b",
    "d996a859-1fe1-4f27-9629-51fc1b10af32",
    "c318289d-9303-46bb-adb9-9ef6cde07fac",
    "7482d18e-17d8-423c-a8bf-0d768aece3b0",
    "bd5e93fc-9501-48b0-9345-01c4ed2b3572",
    "cf43507b-2e63-4705-ad5e-c60e2f5445ca",
    "014afb2b-4c6d-45d0-99b1-bc14b922ed1d",
    "ae006b56-7e59-4b75-98fc-bc41fdf63696",
    "6b48c966-5e7a-4e22-9e8b-9abf1e827ec0",
    "eca2e545-c48b-42c0-9364-3ae3f1f9f0c4",
    "0e78aa6d-455f-4f5d-a26c-9f539a7b1e85",
    "e9822bcc-9f6a-4ab0-9273-8d53aa3fdcfa",
    "e27036e6-2215-4fef-9ba4-5387b1a22c2d",
    "769af40d-b146-4b35-80d4-706c0774c148",
    "2ccacb91-cc14-475e-afe5-d3ab73716898",
    "1a24aafb-0a23-4260-92c1-7df9162e1c43",
    "ce31e610-3b81-420d-ad17-d8722daa8cb1",
    "282c6b6c-cf54-4e00-9147-17a5e0064845",
    "a6debb7d-80a1-4a5a-ac82-a5c1af646ad3",
}


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


def parse_datetime(dt_string: str) -> Optional[datetime]:
    """Parse datetime string in various formats."""
    formats = [
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
    ]
    
    # Handle timezone offset format (+00:00)
    dt_string = re.sub(r'\+00:00$', 'Z', dt_string)
    dt_string = dt_string.replace('+00:00', 'Z')
    
    for fmt in formats:
        try:
            dt = datetime.strptime(dt_string.replace('Z', ''), fmt.replace('Z', '').replace('%z', ''))
            return dt
        except ValueError:
            continue
    
    print(f"  Warning: Could not parse datetime: {dt_string}")
    return None


def extract_conversation_id(conversation: dict) -> Optional[str]:
    """Extract conversation UUID from various possible field names."""
    for field in ['uuid', 'id', 'conversation_id', 'chat_id']:
        if field in conversation:
            value = conversation[field]
            # Handle both string UUIDs and nested objects
            if isinstance(value, str):
                return value
            elif isinstance(value, dict) and 'uuid' in value:
                return value['uuid']
    return None


def extract_title(conversation: dict) -> str:
    """Extract conversation title with fallbacks."""
    for field in ['name', 'title', 'conversation_name']:
        if field in conversation and conversation[field]:
            return conversation[field]
    return "Untitled Conversation"


def extract_timestamp(conversation: dict) -> Optional[datetime]:
    """Extract conversation timestamp with fallbacks."""
    for field in ['updated_at', 'created_at', 'timestamp', 'date']:
        if field in conversation and conversation[field]:
            dt = parse_datetime(conversation[field])
            if dt:
                return dt
    return None


def extract_messages(conversation: dict) -> list:
    """Extract messages from conversation with various structure handling."""
    messages = []
    
    # Try different possible locations for messages
    message_sources = [
        conversation.get('chat_messages', []),
        conversation.get('messages', []),
        conversation.get('turns', []),
        conversation.get('conversation', {}).get('messages', []),
    ]
    
    for source in message_sources:
        if source:
            messages = source
            break
    
    return messages


def format_message_role(role: str) -> str:
    """Normalize message role to Human/Assistant."""
    role_lower = role.lower()
    if role_lower in ['human', 'user', 'h']:
        return "Human"
    elif role_lower in ['assistant', 'ai', 'a', 'claude']:
        return "Assistant"
    else:
        return role.title()


def extract_message_content(message: dict) -> str:
    """Extract text content from message with various structure handling."""
    # Direct text field
    if isinstance(message.get('text'), str):
        return message['text']
    
    # Content field (string or list)
    content = message.get('content', '')
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        # Handle content blocks (text, tool_use, etc.)
        text_parts = []
        for block in content:
            if isinstance(block, str):
                text_parts.append(block)
            elif isinstance(block, dict):
                if block.get('type') == 'text':
                    text_parts.append(block.get('text', ''))
                elif block.get('type') == 'tool_use':
                    tool_name = block.get('name', 'unknown_tool')
                    text_parts.append(f"\n[Tool Use: {tool_name}]\n")
                elif block.get('type') == 'tool_result':
                    text_parts.append(f"\n[Tool Result]\n")
        return '\n'.join(text_parts)
    
    # Message field (nested)
    if 'message' in message:
        return extract_message_content(message['message'])
    
    return str(message)


def conversation_to_markdown(conversation: dict, conv_id: str) -> str:
    """Convert a conversation to markdown format."""
    title = extract_title(conversation)
    timestamp = extract_timestamp(conversation)
    messages = extract_messages(conversation)
    
    # Build markdown
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("## Metadata")
    lines.append(f"- **UUID:** `{conv_id}`")
    lines.append(f"- **URL:** https://claude.ai/chat/{conv_id}")
    if timestamp:
        lines.append(f"- **Date:** {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Conversation")
    lines.append("")
    
    # Process messages
    for i, msg in enumerate(messages):
        # Extract role
        role = msg.get('sender', msg.get('role', msg.get('type', 'unknown')))
        role = format_message_role(role)
        
        # Extract content
        content = extract_message_content(msg)
        
        # Extract message timestamp if available
        msg_time = ""
        for time_field in ['created_at', 'timestamp']:
            if time_field in msg:
                dt = parse_datetime(msg[time_field])
                if dt:
                    msg_time = f" ({dt.strftime('%H:%M:%S')})"
                    break
        
        lines.append(f"### {role}{msg_time}")
        lines.append("")
        lines.append(content)
        lines.append("")
        lines.append("---")
        lines.append("")
    
    return '\n'.join(lines)


# =============================================================================
# Main Processing
# =============================================================================

def find_conversations(data: dict | list) -> list:
    """
    Find conversations in the export data structure.
    
    Claude exports may have various structures:
    - Direct list of conversations
    - {"conversations": [...]}
    - {"chats": [...]}
    - {"data": {"conversations": [...]}}
    """
    if isinstance(data, list):
        return data
    
    if isinstance(data, dict):
        # Try common container keys
        for key in ['conversations', 'chats', 'chat_conversations', 'data']:
            if key in data:
                result = find_conversations(data[key])
                if result:
                    return result
        
        # If the dict itself looks like a conversation, wrap it
        if 'chat_messages' in data or 'messages' in data:
            return [data]
    
    return []


def process_export(export_path: Path, output_dir: Path) -> None:
    """Process the Claude.ai export and extract filtered conversations."""
    
    print(f"Loading export from: {export_path}")
    
    # Load the export file
    with open(export_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Find conversations in the data structure
    conversations = find_conversations(data)
    print(f"Found {len(conversations)} total conversations in export")
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process and filter conversations
    extracted_count = 0
    skipped_not_in_project = 0
    skipped_out_of_range = 0
    
    for conv in conversations:
        conv_id = extract_conversation_id(conv)
        
        if not conv_id:
            print(f"  Warning: Could not extract ID from conversation, skipping")
            continue
        
        # Filter by project (UUID whitelist)
        if conv_id not in PROJECT_CONVERSATION_UUIDS:
            skipped_not_in_project += 1
            continue
        
        # Filter by date range
        timestamp = extract_timestamp(conv)
        if timestamp:
            if not (DATE_RANGE_START <= timestamp <= DATE_RANGE_END):
                skipped_out_of_range += 1
                continue
        
        # Extract and format
        title = extract_title(conv)
        date_str = timestamp.strftime('%Y-%m-%d') if timestamp else 'unknown-date'
        
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
        markdown = conversation_to_markdown(conv, conv_id)
        
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
    
    if extracted_count < len(PROJECT_CONVERSATION_UUIDS):
        missing = len(PROJECT_CONVERSATION_UUIDS) - extracted_count
        print(f"Note: {missing} expected conversations were not found in export.")
        print("This may indicate:")
        print("  - The export was run before those conversations occurred")
        print("  - The conversations are in a different export file")
        print("  - The export structure differs from expected")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nError: Please provide path to Claude.ai export JSON file")
        print("\nExample:")
        print("  python parse_claude_export.py ~/Downloads/claude_export.json")
        print("  python parse_claude_export.py export.json ./output_conversations")
        sys.exit(1)
    
    export_path = Path(sys.argv[1])
    
    if not export_path.exists():
        print(f"Error: Export file not found: {export_path}")
        sys.exit(1)
    
    # Output directory (default or specified)
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2])
    else:
        output_dir = Path("./prompt_development_corpus")
    
    process_export(export_path, output_dir)
    
    print("Done! You can now use these markdown files in Claude Code.")


if __name__ == "__main__":
    main()
