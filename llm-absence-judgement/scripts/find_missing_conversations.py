#!/usr/bin/env python3
"""
Find Potentially Missed Conversations for Software Tool Longevity Research

This script analyses the Claude bulk export to find conversations from Feb-May 2025
that weren't already extracted, and assesses their potential relevance to the research
project on software tool longevity.

Relevance criteria:
- Tool metadata searches
- Evidence collection for tools
- Prompt development / metaprompting
- Bibliography searches
- Questions about Claude's capabilities for research
- Ideation, writing, revision of the paper
"""

import json
import re
from datetime import datetime
from pathlib import Path


# =============================================================================
# Configuration
# =============================================================================

EXPORT_PATH = Path(
    "/home/shawn/Code/theseus-ship/llm-absence-judgement/preliminary-work/"
    "evidence/chats/bulk-exports/Claude-data-2025-12-07-20-26-23-batch-0000/"
    "conversations.json"
)

OUTPUT_PATH = Path(
    "/home/shawn/Code/theseus-ship/llm-absence-judgement/planning/"
    "candidate-conversations-review.md"
)

# Date range for filtering (inclusive)
DATE_RANGE_START = datetime(2025, 2, 1)
DATE_RANGE_END = datetime(2025, 5, 31, 23, 59, 59)

# Already extracted conversation UUIDs (from parse_claude_export.py)
ALREADY_EXTRACTED = {
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

# Keywords that suggest relevance to the research project
RELEVANCE_KEYWORDS = [
    # Tool/software research
    r'\bsoftware\s+tool',
    r'\bresearch\s+tool',
    r'\barchaeolog',
    r'\bdigital\s+humanities',
    r'\bmetadata',
    r'\blongevity',
    r'\bsustainab',
    r'\bmaintenance',
    r'\babandoned',
    r'\bdeprecated',
    r'\bversion',
    r'\bgithub',
    r'\brepository',
    r'\bopen\s+source',
    r'\bCRAN',
    r'\bPyPI',
    r'\bR\s+package',
    r'\bPython\s+package',

    # Specific tools mentioned in the project
    r'\bFAIMS',
    r'\bade4',
    r'\bVOSviewer',
    r'\bArchaeoPhases',
    r'\bBchron',
    r'\bOxCal',
    r'\bstratigraph',

    # Research/writing activities
    r'\bprompt',
    r'\bmetaprompt',
    r'\bsystem\s+prompt',
    r'\bbibliograph',
    r'\bcitation',
    r'\bbibtex',
    r'\breference',
    r'\bliterature\s+review',
    r'\bpaper\s+section',
    r'\bmanuscript',
    r'\bwriting',
    r'\brevision',
    r'\bediting',
    r'\bdraft',

    # Methodology
    r'\bevidence',
    r'\bassessment',
    r'\bevaluation',
    r'\bcriteria',
    r'\bframework',
    r'\bmethodolog',

    # Ship of Theseus / identity
    r'\bship\s+of\s+theseus',
    r'\btheseus',
    r'\bidentity',
    r'\bcontinuity',
    r'\bsoftware\s+evolution',
]


# =============================================================================
# Helper Functions
# =============================================================================

def parse_datetime(dt_string: str) -> datetime | None:
    """Parse datetime string in various formats."""
    if not dt_string:
        return None

    formats = [
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
    ]

    # Normalise timezone format
    dt_string = re.sub(r'\+00:00$', 'Z', dt_string)
    dt_string = dt_string.replace('+00:00', 'Z')

    for fmt in formats:
        try:
            dt = datetime.strptime(
                dt_string.replace('Z', ''),
                fmt.replace('Z', '').replace('%z', '')
            )
            return dt
        except ValueError:
            continue

    return None


def extract_text_content(messages: list) -> str:
    """Extract all text content from messages for keyword searching."""
    text_parts = []

    for msg in messages:
        # Try different content structures
        text = msg.get('text', '')
        if text:
            text_parts.append(text)
            continue

        content = msg.get('content', '')
        if isinstance(content, str):
            text_parts.append(content)
        elif isinstance(content, list):
            for block in content:
                if isinstance(block, str):
                    text_parts.append(block)
                elif isinstance(block, dict) and block.get('type') == 'text':
                    text_parts.append(block.get('text', ''))

    return '\n'.join(text_parts)


def get_first_human_message(messages: list) -> str:
    """Get the first human message for context."""
    for msg in messages:
        sender = msg.get('sender', msg.get('role', '')).lower()
        if sender in ['human', 'user']:
            text = msg.get('text', '')
            if text:
                return text[:500]  # First 500 chars

            content = msg.get('content', '')
            if isinstance(content, str):
                return content[:500]
            elif isinstance(content, list):
                for block in content:
                    if isinstance(block, str):
                        return block[:500]
                    elif isinstance(block, dict) and block.get('type') == 'text':
                        return block.get('text', '')[:500]

    return "(No human message found)"


def calculate_relevance_score(text: str) -> tuple[int, list[str]]:
    """
    Calculate relevance score based on keyword matches.

    Returns (score, list of matched keywords).
    """
    text_lower = text.lower()
    matches = []

    for pattern in RELEVANCE_KEYWORDS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            matches.append(pattern)

    return len(matches), matches


def categorise_relevance(score: int) -> str:
    """Categorise relevance level based on score."""
    if score >= 5:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    elif score >= 1:
        return "LOW"
    else:
        return "NONE"


# =============================================================================
# Main Processing
# =============================================================================

def main():
    print("Loading Claude export...")

    with open(EXPORT_PATH, 'r', encoding='utf-8') as f:
        conversations = json.load(f)

    print(f"Found {len(conversations)} total conversations in export")

    # Filter and analyse
    candidates = []
    stats = {
        'total': len(conversations),
        'in_date_range': 0,
        'already_extracted': 0,
        'new_candidates': 0,
    }

    for conv in conversations:
        # Extract UUID
        conv_id = conv.get('uuid', conv.get('id', ''))
        if not conv_id:
            continue

        # Check date range
        timestamp_str = conv.get('updated_at', conv.get('created_at', ''))
        timestamp = parse_datetime(timestamp_str)

        if not timestamp:
            continue

        if not (DATE_RANGE_START <= timestamp <= DATE_RANGE_END):
            continue

        stats['in_date_range'] += 1

        # Skip already extracted
        if conv_id in ALREADY_EXTRACTED:
            stats['already_extracted'] += 1
            continue

        # Analyse content for relevance
        title = conv.get('name', 'Untitled')
        messages = conv.get('chat_messages', [])
        full_text = f"{title}\n{extract_text_content(messages)}"

        score, matches = calculate_relevance_score(full_text)
        relevance = categorise_relevance(score)

        first_msg = get_first_human_message(messages)

        candidates.append({
            'uuid': conv_id,
            'title': title,
            'date': timestamp.strftime('%Y-%m-%d'),
            'timestamp': timestamp,
            'score': score,
            'relevance': relevance,
            'matches': matches,
            'first_message': first_msg,
            'message_count': len(messages),
        })

        stats['new_candidates'] += 1

    # Sort by relevance score (descending) then date
    candidates.sort(key=lambda x: (-x['score'], x['timestamp']))

    # Generate markdown report
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Candidate Conversations for Review")
    lines.append("")
    lines.append("Conversations from Feb-May 2025 not yet extracted, assessed for")
    lines.append("relevance to the software tool longevity research project.")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## Summary Statistics")
    lines.append("")
    lines.append(f"- Total conversations in export: {stats['total']}")
    lines.append(f"- Conversations in date range (Feb-May 2025): {stats['in_date_range']}")
    lines.append(f"- Already extracted: {stats['already_extracted']}")
    lines.append(f"- New candidates to review: {stats['new_candidates']}")
    lines.append("")

    # Group by relevance
    high = [c for c in candidates if c['relevance'] == 'HIGH']
    medium = [c for c in candidates if c['relevance'] == 'MEDIUM']
    low = [c for c in candidates if c['relevance'] == 'LOW']
    none = [c for c in candidates if c['relevance'] == 'NONE']

    lines.append("## Relevance Breakdown")
    lines.append("")
    lines.append(f"- HIGH relevance: {len(high)}")
    lines.append(f"- MEDIUM relevance: {len(medium)}")
    lines.append(f"- LOW relevance: {len(low)}")
    lines.append(f"- No keyword matches: {len(none)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Separate v8-metadata from other HIGH relevance
    v8_metadata = [c for c in high if 'v8-' in c['title'].lower() or 'v7-' in c['title'].lower()
                   or 'v6-' in c['title'].lower() or 'v5-' in c['title'].lower()
                   or 'v4-' in c['title'].lower() or 'v3-' in c['title'].lower()
                   or 'v2-' in c['title'].lower() or 'v1-' in c['title'].lower()
                   or 'test' in c['title'].lower()]
    other_high = [c for c in high if c not in v8_metadata]

    # Other HIGH relevance (non-metadata) - review first
    if other_high:
        lines.append("## PRIORITY REVIEW: Non-Metadata High Relevance")
        lines.append("")
        lines.append("These conversations have high keyword scores but are NOT tool metadata")
        lines.append("collection. Review these first for prompt development, writing, ideation, etc.")
        lines.append("")

        for c in other_high:
            lines.append(f"### {c['title']}")
            lines.append("")
            lines.append(f"- **UUID:** `{c['uuid']}`")
            lines.append(f"- **Date:** {c['date']}")
            lines.append(f"- **Messages:** {c['message_count']}")
            lines.append(f"- **Relevance Score:** {c['score']}")
            lines.append("")
            lines.append("**First human message:**")
            lines.append("")
            lines.append(f"> {c['first_message'][:400]}...")
            lines.append("")
            lines.append(f"**URL:** https://claude.ai/chat/{c['uuid']}")
            lines.append("")
            lines.append("- [ ] Include in extraction")
            lines.append("- [ ] Not relevant")
            lines.append("")
            lines.append("---")
            lines.append("")

    # v8-metadata section
    if v8_metadata:
        lines.append("## Tool Metadata Collection Conversations")
        lines.append("")
        lines.append(f"Found {len(v8_metadata)} tool metadata conversations (v1-v8 naming pattern).")
        lines.append("These are tool investigation chats that appear to have been missed from")
        lines.append("the original extraction. Listed in table format for quick review.")
        lines.append("")
        lines.append("| Date | Tool Name | Messages | Score | UUID |")
        lines.append("|------|-----------|----------|-------|------|")

        for c in v8_metadata:
            title_short = c['title'][:35] + "..." if len(c['title']) > 35 else c['title']
            lines.append(
                f"| {c['date']} | {title_short} | {c['message_count']} | "
                f"{c['score']} | `{c['uuid'][:8]}...` |"
            )

        lines.append("")
        lines.append("### Full UUIDs for extraction")
        lines.append("")
        lines.append("```python")
        lines.append("ADDITIONAL_METADATA_UUIDS = {")
        for c in v8_metadata:
            lines.append(f'    "{c["uuid"]}",  # {c["title"]}')
        lines.append("}")
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Original HIGH section - skip since we've handled it above
    if False and high:
        lines.append("## HIGH Relevance Candidates")
        lines.append("")
        lines.append("These conversations have 5+ keyword matches and are likely relevant.")
        lines.append("")

        for c in high:
            lines.append(f"### {c['title']}")
            lines.append("")
            lines.append(f"- **UUID:** `{c['uuid']}`")
            lines.append(f"- **Date:** {c['date']}")
            lines.append(f"- **Messages:** {c['message_count']}")
            lines.append(f"- **Relevance Score:** {c['score']}")
            lines.append(f"- **Matched Keywords:** {len(c['matches'])}")
            lines.append("")
            lines.append("**First human message:**")
            lines.append("")
            lines.append(f"> {c['first_message'][:300]}...")
            lines.append("")
            lines.append(f"**URL:** https://claude.ai/chat/{c['uuid']}")
            lines.append("")
            lines.append("- [ ] Include in extraction")
            lines.append("- [ ] Not relevant")
            lines.append("")
            lines.append("---")
            lines.append("")

    # MEDIUM relevance section
    if medium:
        lines.append("## MEDIUM Relevance Candidates")
        lines.append("")
        lines.append("These conversations have 3-4 keyword matches and may be relevant.")
        lines.append("")

        for c in medium:
            lines.append(f"### {c['title']}")
            lines.append("")
            lines.append(f"- **UUID:** `{c['uuid']}`")
            lines.append(f"- **Date:** {c['date']}")
            lines.append(f"- **Messages:** {c['message_count']}")
            lines.append(f"- **Relevance Score:** {c['score']}")
            lines.append("")
            lines.append("**First human message:**")
            lines.append("")
            lines.append(f"> {c['first_message'][:200]}...")
            lines.append("")
            lines.append(f"**URL:** https://claude.ai/chat/{c['uuid']}")
            lines.append("")
            lines.append("- [ ] Include in extraction")
            lines.append("- [ ] Not relevant")
            lines.append("")
            lines.append("---")
            lines.append("")

    # LOW relevance section (condensed)
    if low:
        lines.append("## LOW Relevance Candidates")
        lines.append("")
        lines.append("These conversations have 1-2 keyword matches. Quick review recommended.")
        lines.append("")
        lines.append("| Date | Title | Messages | Score | UUID |")
        lines.append("|------|-------|----------|-------|------|")

        for c in low:
            title_short = c['title'][:40] + "..." if len(c['title']) > 40 else c['title']
            lines.append(
                f"| {c['date']} | {title_short} | {c['message_count']} | "
                f"{c['score']} | `{c['uuid'][:8]}...` |"
            )

        lines.append("")
        lines.append("---")
        lines.append("")

    # NO relevance section (very condensed)
    if none:
        lines.append("## No Keyword Matches")
        lines.append("")
        lines.append(f"{len(none)} conversations had no keyword matches. Listed here for")
        lines.append("completeness - these are unlikely to be relevant but titles are shown")
        lines.append("in case any were missed by the keyword approach.")
        lines.append("")
        lines.append("<details>")
        lines.append("<summary>Click to expand ({} conversations)</summary>".format(len(none)))
        lines.append("")

        for c in none:
            lines.append(f"- {c['date']}: {c['title']}")

        lines.append("")
        lines.append("</details>")
        lines.append("")

    # Write output
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print("")
    print("=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"Candidates found: {stats['new_candidates']}")
    print(f"  - HIGH relevance: {len(high)}")
    print(f"  - MEDIUM relevance: {len(medium)}")
    print(f"  - LOW relevance: {len(low)}")
    print(f"  - No matches: {len(none)}")
    print("")
    print(f"Output written to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
