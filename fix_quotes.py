#!/usr/bin/env python3
"""
A script to fix both opening and closing quotes in CSV description fields.
1. Adds a quote after the first comma if missing (opening quote)
2. Adds a quote before the GitHub URL or empty field pattern if missing (closing quote)

This version specifically handles the case where closing quotes are missing
and we can't rely on quote tracking to find field boundaries.
"""

import sys
import os
import re

def fix_quotes_in_csv(input_file, output_file, encoding='utf-8'):
    """
    Fix both opening and closing quotes in CSV description fields.
    Uses pattern matching instead of quote state tracking to handle missing quotes.
    
    Args:
        input_file (str): Path to the input CSV file
        output_file (str): Path to save the fixed CSV file
        encoding (str): File encoding to use (default: utf-8)
    
    Returns:
        tuple: (opening_quotes_fixed, closing_quotes_fixed)
    """
    print(f"Reading file: {input_file}")
    
    # Try to read with the specified encoding, fall back to latin-1 if needed
    try:
        with open(input_file, 'r', encoding=encoding) as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Error reading with {encoding} encoding, trying latin-1...")
        with open(input_file, 'r', encoding='latin-1') as f:
            content = f.read()
        encoding = 'latin-1'
    
    # Split into lines to process each row
    if '\r\n' in content:
        lines = content.split('\r\n')
        line_ending = '\r\n'
    else:
        lines = content.split('\n')
        line_ending = '\n'
    
    fixed_lines = []
    opening_quotes_fixed = 0
    closing_quotes_fixed = 0
    
    # Keep the header as is
    if lines:
        fixed_lines.append(lines[0])
    
    # Process each data row (skip header)
    for i, line in enumerate(lines[1:], 1):
        if not line.strip():  # Skip empty lines
            fixed_lines.append(line)
            continue
        
        fixed_this_row = False
        
        # Step 1: Fix missing opening quote after the first comma
        first_comma_idx = line.find(',')
        if first_comma_idx < 0:
            # No comma found, keep line as is
            fixed_lines.append(line)
            continue
        
        # Initialize the fixed line with the original
        fixed_line = line
        
        # Check if there's already a quote after the first comma
        if first_comma_idx + 1 < len(line) and line[first_comma_idx + 1] != '"':
            # Add a quote after the first comma
            fixed_line = line[:first_comma_idx + 1] + '"' + line[first_comma_idx + 1:]
            opening_quotes_fixed += 1
            fixed_this_row = True
        
        # Step 2: Fix missing closing quote 
        # Instead of counting commas while tracking quotes (which doesn't work with missing quotes),
        # we'll look for specific patterns that indicate where the GitHub column starts
        
        # Patterns to look for: 
        # 1. ,http - Beginning of a GitHub URL
        # 2. ,, - Empty GitHub field
        
        # Use regex to find the first occurrence of these patterns AFTER the first comma
        # but make sure we don't match patterns that already have a quote before them
        
        # If we've added an opening quote, we need to search from that position
        search_start = first_comma_idx + 2 if fixed_line[first_comma_idx + 1] == '"' else first_comma_idx + 1
        
        # Look for GitHub URL pattern
        github_match = re.search(r',\s*https?://', fixed_line[search_start:])
        empty_field_match = re.search(r',\s*,', fixed_line[search_start:])
        
        # Determine where to look for missing closing quote
        if github_match:
            # Found a GitHub URL
            pattern_pos = search_start + github_match.start()
            
            # Check if there's already a quote before this pattern
            char_before_pattern = fixed_line[pattern_pos - 1] if pattern_pos > 0 else ''
            
            if char_before_pattern != '"' and fixed_line[first_comma_idx + 1] == '"':
                # We have an opening quote but no closing quote before the GitHub URL
                # Add the closing quote
                fixed_line = fixed_line[:pattern_pos] + '"' + fixed_line[pattern_pos:]
                closing_quotes_fixed += 1
                fixed_this_row = True
                
        elif empty_field_match:
            # Found an empty field (,,)
            pattern_pos = search_start + empty_field_match.start()
            
            # Check if there's already a quote before this pattern
            char_before_pattern = fixed_line[pattern_pos - 1] if pattern_pos > 0 else ''
            
            if char_before_pattern != '"' and fixed_line[first_comma_idx + 1] == '"':
                # We have an opening quote but no closing quote before the empty field
                # Add the closing quote
                fixed_line = fixed_line[:pattern_pos] + '"' + fixed_line[pattern_pos:]
                closing_quotes_fixed += 1
                fixed_this_row = True
        
        # Show examples of fixes for the first few rows
        if fixed_this_row and i <= 5:
            print(f"\nFixed row {i+1}:")
            print(f"  Before: {line[:min(80, len(line))]}...")
            print(f"  After:  {fixed_line[:min(80, len(fixed_line))]}...")
        
        fixed_lines.append(fixed_line)
    
    # Join the lines back with original line endings
    fixed_content = line_ending.join(fixed_lines)
    
    print(f"\nWriting fixed file: {output_file}")
    with open(output_file, 'w', encoding=encoding) as f:
        f.write(fixed_content)
    
    print(f"Fixed {opening_quotes_fixed} missing opening quotes")
    print(f"Fixed {closing_quotes_fixed} missing closing quotes")
    
    return (opening_quotes_fixed, closing_quotes_fixed)

def check_file_differences(original_file, fixed_file, encoding='utf-8'):
    """
    Compare the first few differences between original and fixed files.
    
    Args:
        original_file (str): Path to the original CSV file
        fixed_file (str): Path to the fixed CSV file
        encoding (str): File encoding to use
    """
    print(f"\nVerifying fixes between {original_file} and {fixed_file}...")
    
    try:
        with open(original_file, 'r', encoding=encoding) as f:
            original_lines = f.readlines()
        with open(fixed_file, 'r', encoding=encoding) as f:
            fixed_lines = f.readlines()
    except UnicodeDecodeError:
        with open(original_file, 'r', encoding='latin-1') as f:
            original_lines = f.readlines()
        with open(fixed_file, 'r', encoding='latin-1') as f:
            fixed_lines = f.readlines()
    
    # Count lines with differences
    differences = 0
    shown_diffs = 0
    
    for i in range(min(len(original_lines), len(fixed_lines))):
        if original_lines[i] != fixed_lines[i]:
            differences += 1
            
            # Show details for first few differences
            if shown_diffs < 5:
                orig = original_lines[i].strip()
                fixed = fixed_lines[i].strip()
                
                # First find the first comma
                first_comma_idx = orig.find(',')
                
                if first_comma_idx > 0:
                    # Show truncated version focusing on key differences
                    print(f"\nLine {i+1} modified:")
                    
                    # Check for opening quote fix
                    if first_comma_idx + 1 < len(orig) and first_comma_idx + 1 < len(fixed):
                        if orig[first_comma_idx + 1] != fixed[first_comma_idx + 1]:
                            print(f"  Opening quote area:")
                            print(f"    Original: {orig[first_comma_idx:first_comma_idx+20]}...")
                            print(f"    Fixed:    {fixed[first_comma_idx:first_comma_idx+20]}...")
                    
                    # Check for closing quote fix by looking for URL or empty field pattern
                    github_idx = orig.find(',http', first_comma_idx)
                    empty_idx = orig.find(',,', first_comma_idx)
                    
                    if github_idx > 0:
                        print(f"  Closing quote area (GitHub URL):")
                        print(f"    Original: ...{orig[max(0, github_idx-5):github_idx+15]}...")
                        print(f"    Fixed:    ...{fixed[max(0, github_idx-5):github_idx+15]}...")
                    elif empty_idx > 0:
                        print(f"  Closing quote area (empty field):")
                        print(f"    Original: ...{orig[max(0, empty_idx-5):empty_idx+5]}...")
                        print(f"    Fixed:    ...{fixed[max(0, empty_idx-5):empty_idx+5]}...")
                
                shown_diffs += 1
    
    print(f"\nTotal lines modified: {differences}")

if __name__ == "__main__":
    # Get input and output filenames from command line or use defaults
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'openarchaeoimproved.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'openarchaeoimproved_fixed.csv'
    
    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    # Fix the CSV file
    print(f"Fixing CSV file: {input_file} -> {output_file}")
    opening_fixes, closing_fixes = fix_quotes_in_csv(input_file, output_file)
    
    # Verify the changes if any fixes were made
    if opening_fixes > 0 or closing_fixes > 0:
        check_file_differences(input_file, output_file)
        print(f"\nDone! Fixed CSV saved to: {output_file}")
        print(f"Total fixes: {opening_fixes + closing_fixes}")
    else:
        print("No issues found that needed fixing")