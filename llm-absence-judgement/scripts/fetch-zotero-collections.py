#!/usr/bin/env python3
"""
Fetch items from Zotero collections for literature review CSVs.

This script queries the Zotero API to retrieve bibliographic items from
specific collections (both valid sources and error categories) and outputs
them as CSV files for the literature discovery analysis.
"""

import csv
import json
import os
import urllib.request
from pathlib import Path

# Configuration
API_KEY = "3U1b9J6TiDdSRVGwtynB5iW8"
GROUP_ID = "5861859"
BASE_URL = f"https://api.zotero.org/groups/{GROUP_ID}"

# Collection IDs (from Zotero API)
COLLECTIONS = {
    # Valid sources (under Longevity-review)
    "valid": {
        "OpenAI-DR": "45QRRTJ2",
        "Manual": "JEB9RZSN",
        "Elicit": "XA53ZQKX",
        "Perplexity": "XWAQITL8",
    },
    # Error categories (top-level)
    "errors": {
        "Non-academic": "KNYZEC5Z",
        "Not-relevant": "KIAI3U3I",
        "Predatory": "4GGR8VLX",
        "Software-tool-publications": "5Z8L4HHG",
        "Unusable": "ZMEWJ866",
    },
}

OUTPUT_DIR = Path("/home/shawn/Code/theseus-ship/llm-absence-judgement/results/literature")


def fetch_collection_items(collection_key: str) -> list:
    """Fetch all items from a Zotero collection."""
    url = f"{BASE_URL}/collections/{collection_key}/items?limit=100"
    req = urllib.request.Request(url)
    req.add_header("Zotero-API-Key", API_KEY)

    with urllib.request.urlopen(req) as response:
        items = json.loads(response.read().decode())

    # Filter out attachments and notes
    return [
        item for item in items
        if item["data"].get("itemType") not in ("attachment", "note")
    ]


def format_creators(creators: list) -> str:
    """Format creator list as semicolon-separated string."""
    parts = []
    for c in creators:
        if "name" in c:
            parts.append(c["name"])
        elif "lastName" in c:
            name = c.get("firstName", "") + ", " + c["lastName"] if c.get("firstName") else c["lastName"]
            parts.append(name)
    return "; ".join(parts)


def item_to_row(item: dict, collection_name: str, validity_status: str) -> dict:
    """Convert Zotero item to CSV row."""
    data = item["data"]
    return {
        "zotero_key": item["key"],
        "item_type": data.get("itemType", ""),
        "title": data.get("title", ""),
        "creators": format_creators(data.get("creators", [])),
        "date": data.get("date", ""),
        "publication_title": data.get("publicationTitle", ""),
        "publisher": data.get("publisher", ""),
        "doi": data.get("DOI", ""),
        "url": data.get("url", ""),
        "abstract": data.get("abstractNote", ""),
        "all_tags": "; ".join(t.get("tag", "") for t in data.get("tags", [])),
        "all_collections": collection_name,
        "validity_status": validity_status,
        "is_valid": validity_status == "valid",
    }


def main():
    """Fetch all collections and write CSVs."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "zotero_key", "item_type", "title", "creators", "date",
        "publication_title", "publisher", "doi", "url", "abstract",
        "all_tags", "all_collections", "validity_status", "is_valid"
    ]

    all_valid = []
    all_errors = []

    # Fetch valid sources
    print("Fetching valid source collections...")
    for name, key in COLLECTIONS["valid"].items():
        print(f"  {name}: ", end="")
        items = fetch_collection_items(key)
        print(f"{len(items)} items")

        rows = [item_to_row(item, name, "valid") for item in items]
        all_valid.extend(rows)

        # Write individual CSV
        output_file = OUTPUT_DIR / f"source-{name.lower()}.csv"
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    # Fetch error categories
    print("\nFetching error category collections...")
    for name, key in COLLECTIONS["errors"].items():
        print(f"  {name}: ", end="")
        items = fetch_collection_items(key)
        print(f"{len(items)} items")

        rows = [item_to_row(item, name, name.lower()) for item in items]
        all_errors.extend(rows)

        # Write individual CSV
        output_file = OUTPUT_DIR / f"errors-{name.lower()}.csv"
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    # Write combined valid CSV
    combined_valid = OUTPUT_DIR / "literature-review-valid.csv"
    with open(combined_valid, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_valid)
    print(f"\nWrote combined valid: {len(all_valid)} items")

    # Write combined errors CSV
    combined_errors = OUTPUT_DIR / "literature-review-errors.csv"
    with open(combined_errors, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_errors)
    print(f"Wrote combined errors: {len(all_errors)} items")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Valid sources: {len(all_valid)}")
    print(f"Error items:   {len(all_errors)}")
    print(f"Total:         {len(all_valid) + len(all_errors)}")


if __name__ == "__main__":
    main()
