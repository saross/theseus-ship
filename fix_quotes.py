#!/usr/bin/env python3
"""
A script to fix both opening and closing quotes in CSV description fields.
1. Adds a quote after the first comma if missing (opening quote)
2. Adds a quote before the next non-description field ONLY if the field isn't already
   properly quoted.

This version fixes issues with:
- Multiple empty columns
- Descriptions with commas
- Already properly quoted fields
"""

import sys
import os
import re

def fix_quotes_in_csv(input_file, output_file, encoding='utf-8'):
    """
    Fix missing quotes in CSV description fields.
    Properly checks if fields are already correctly quoted.
    
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
        
        # Step 2: ONLY fix missing closing quotes if needed
        # First determine if the description field is already properly quoted
        
        # Check if there's an opening quote (either originally or after our fix)
        has_opening_quote = (fixed_line[first_comma_idx + 1] == '"')
        
        if has_opening_quote:
            # Look for a matching closing quote by counting quotes after the opening quote
            # If there's an odd number of quotes after the opening, we need to add one
            
            # Extract the rest of the line after the opening quote
            rest_of_line = fixed_line[first_comma_idx + 2:]
            
            # First check if there are any quotes at all in the rest of the line
            if '"' in rest_of_line:
                # There's at least one quote, but we need to determine if it's the matching one
                # Find the position of what *might* be the matching quote
                quote_pos = rest_of_line.find('"')
                
                # What comes after this quote?
                after_quote = rest_of_line[quote_pos + 1:].lstrip()
                
                # If the character after the quote is a comma or end of line, this is likely a closing quote
                if after_quote and after_quote[0] == ',':
                    # This field is likely already properly quoted, skip the closing quote fix
                    fixed_lines.append(fixed_line)
                    continue
            
            # If we get here, we need to add a closing quote
            
            # Search for patterns that indicate where the description field ends
            search_start = first_comma_idx + 2  # Start after the opening quote
            
            # Look for GitHub URL pattern or consecutive commas
            github_match = re.search(r',\s*https?://', fixed_line[search_start:])
            empty_match = re.search(r',\s*,', fixed_line[search_start:])
            
            pattern_pos = -1
            
            if github_match:
                # Found a GitHub URL
                pattern_pos = search_start + github_match.start()
            elif empty_match:
                # Found empty fields (consecutive commas)
                pattern_pos = search_start + empty_match.start()
            
            # If we found a pattern, add a closing quote if needed
            if pattern_pos > 0:
                # Check if there's already a quote before this pattern
                char_before_pattern = fixed_line[pattern_pos - 1] if pattern_pos > 0 else ''
                
                if char_before_pattern != '"':
                    # Add the closing quote before the pattern
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
    
    # Final sanity check - scan for instances of triple quotes which shouldn't happen
    if '"""' in fixed_content:
        print("WARNING: Found triple quotes in output, which may indicate a bug in the script.")
        triple_quote_lines = [j+1 for j, line in enumerate(fixed_content.split('\n')) if '"""' in line]
        print(f"Triple quotes found on lines: {triple_quote_lines[:10]}...")
    
    print(f"\nWriting fixed file: {output_file}")
    with open(output_file, 'w', encoding=encoding) as f:
        f.write(fixed_content)
    
    print(f"Fixed {opening_quotes_fixed} missing opening quotes")
    print(f"Fixed {closing_quotes_fixed} missing closing quotes")
    
    return (opening_quotes_fixed, closing_quotes_fixed)

def check_specific_examples(original_file, fixed_file, examples, encoding='utf-8'):
    """
    Check specific examples to verify the fixes.
    
    Args:
        original_file (str): Path to the original CSV file
        fixed_file (str): Path to the fixed CSV file
        examples (list): List of strings to search for in rows
        encoding (str): File encoding to use
    """
    print(f"\nChecking specific examples in {fixed_file}...")
    
    try:
        with open(original_file, 'r', encoding=encoding) as f:
            original_content = f.read()
        with open(fixed_file, 'r', encoding=encoding) as f:
            fixed_content = f.read()
    except UnicodeDecodeError:
        with open(original_file, 'r', encoding='latin-1') as f:
            original_content = f.read()
        with open(fixed_file, 'r', encoding='latin-1') as f:
            fixed_content = f.read()
    
    # Split into lines
    original_lines = original_content.split('\n')
    fixed_lines = fixed_content.split('\n')
    
    for example in examples:
        # Find lines containing the example in both files
        original_match = None
        fixed_match = None
        
        for line in original_lines:
            if example in line:
                original_match = line
                break
        
        for line in fixed_lines:
            if example in line:
                fixed_match = line
                break
        
        if original_match and fixed_match:
            print(f"\nExample containing '{example}':")
            print(f"  Original: {original_match[:100]}...")
            print(f"  Fixed:    {fixed_match[:100]}...")
            
            # Count the quotes in the description field
            first_comma_orig = original_match.find(',')
            first_comma_fixed = fixed_match.find(',')
            
            if first_comma_orig > 0 and first_comma_fixed > 0:
                # Count quotes after the first comma
                rest_orig = original_match[first_comma_orig+1:]
                rest_fixed = fixed_match[first_comma_fixed+1:]
                
                quotes_orig = rest_orig.count('"')
                quotes_fixed = rest_fixed.count('"')
                
                print(f"  Quotes in description (original): {quotes_orig}")
                print(f"  Quotes in description (fixed): {quotes_fixed}")
                
                if quotes_orig != quotes_fixed:
                    print(f"  ✓ Quote structure was modified")
                else:
                    print(f"  ℹ Quote structure was unchanged")

def check_problematic_examples(input_file, output_file, problematic_examples, encoding='utf-8'):
    """
    Check specifically problematic examples to verify they weren't incorrectly modified.
    
    Args:
        input_file (str): Path to the input CSV file
        output_file (str): Path to the fixed CSV file
        problematic_examples (list): List of strings to search for in rows
        encoding (str): File encoding to use
    """
    print(f"\nChecking problematic examples...")
    
    try:
        with open(input_file, 'r', encoding=encoding) as f:
            original_lines = f.readlines()
        with open(output_file, 'r', encoding=encoding) as f:
            fixed_lines = f.readlines()
    except UnicodeDecodeError:
        with open(input_file, 'r', encoding='latin-1') as f:
            original_lines = f.readlines()
        with open(output_file, 'r', encoding='latin-1') as f:
            fixed_lines = f.readlines()
    
    for example in problematic_examples:
        found = False
        for i in range(min(len(original_lines), len(fixed_lines))):
            if example in original_lines[i]:
                found = True
                if original_lines[i] != fixed_lines[i]:
                    print(f"\nProblematic example '{example}' was modified:")
                    print(f"  Original: {original_lines[i][:100]}...")
                    print(f"  Fixed:    {fixed_lines[i][:100]}...")
                    
                    # Find quotes and highlight the differences
                    orig = original_lines[i].strip()
                    fixed = fixed_lines[i].strip()
                    
                    # Find positions of all quotes in both strings
                    orig_quotes = [j for j, char in enumerate(orig) if char == '"']
                    fixed_quotes = [j for j, char in enumerate(fixed) if char == '"']
                    
                    print(f"  Original quotes at positions: {orig_quotes}")
                    print(f"  Fixed quotes at positions: {fixed_quotes}")
                    
                    if len(fixed_quotes) > len(orig_quotes):
                        print("  ⚠ Added quotes where they might not be needed!")
                else:
                    print(f"\nProblematic example '{example}' was correctly left unchanged")
                break
        
        if not found:
            print(f"Example '{example}' not found in files")

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
    
    # Check problematic examples
    check_problematic_examples(input_file, output_file, ["PLC"])
    
    # Summary
    if opening_fixes > 0 or closing_fixes > 0:
        print(f"\nDone! Fixed CSV saved to: {output_file}")
        print(f"Total fixes: {opening_fixes + closing_fixes}")
    else:
        print("No issues found that needed fixing")