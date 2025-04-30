#!/usr/bin/env python3
"""
A script to add quotes after ONLY the first comma in each row of a CSV file.
This ensures the description column (second column) is properly quoted.
"""

import sys
import os

def fix_first_comma_quotes(input_file, output_file, encoding='utf-8'):
    """
    Add quotes after the first comma in each row if not already present.
    Only affects the second column (description).
    
    Args:
        input_file (str): Path to the input CSV file
        output_file (str): Path to save the fixed CSV file
        encoding (str): File encoding to use (default: utf-8)
    
    Returns:
        int: Number of rows fixed
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
    fixes_made = 0
    
    # Keep the header as is (first line)
    if lines:
        fixed_lines.append(lines[0])
    
    # Process each data row (skip header)
    for i, line in enumerate(lines[1:], 1):
        if not line.strip():  # Skip empty lines
            fixed_lines.append(line)
            continue
        
        # Find the first comma
        first_comma_idx = line.find(',')
        if first_comma_idx < 0:
            # No comma found, keep line as is
            fixed_lines.append(line)
            continue
        
        # Check if there's already a quote after the first comma
        if first_comma_idx + 1 < len(line) and line[first_comma_idx + 1] != '"':
            # Add a quote after the first comma
            fixed_line = line[:first_comma_idx + 1] + '"' + line[first_comma_idx + 1:]
            fixed_lines.append(fixed_line)
            fixes_made += 1
            
            # Show examples of the fixes being made (for first few)
            if fixes_made <= 3:
                print(f"\nFixed row {i+1}:")
                print(f"  Before: {line[:min(60, len(line))]}...")
                print(f"  After:  {fixed_line[:min(60, len(fixed_line))]}...")
        else:
            # No fix needed
            fixed_lines.append(line)
    
    # Join the lines back with original line endings
    fixed_content = line_ending.join(fixed_lines)
    
    print(f"\nWriting fixed file: {output_file}")
    with open(output_file, 'w', encoding=encoding) as f:
        f.write(fixed_content)
    
    print(f"Made {fixes_made} replacements")
    return fixes_made

def check_file_differences(original_file, fixed_file, encoding='utf-8'):
    """
    Compare the first few differences between original and fixed files.
    This helps verify that only the first comma in each row was modified.
    
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
            if shown_diffs < 3:
                orig = original_lines[i].strip()
                fixed = fixed_lines[i].strip()
                
                # Find the first comma
                orig_comma = orig.find(',')
                fixed_comma = fixed.find(',')
                
                if orig_comma > 0 and fixed_comma > 0:
                    # Show the text around the first comma
                    print(f"\nLine {i+1} modified:")
                    print(f"  Original: ...{orig[max(0, orig_comma-5):orig_comma+20]}...")
                    print(f"  Fixed:    ...{fixed[max(0, fixed_comma-5):fixed_comma+20]}...")
                    
                    # Verify only the first comma was affected
                    if fixed[fixed_comma+1] == '"' and orig[orig_comma+1] != '"':
                        print("  ✓ Fix correctly added quote after first comma")
                    else:
                        print("  ⚠ Unexpected difference detected")
                
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
    fixes = fix_first_comma_quotes(input_file, output_file)
    
    # Verify the changes if any fixes were made
    if fixes > 0:
        check_file_differences(input_file, output_file)
        print(f"\nDone! Fixed CSV saved to: {output_file}")
    else:
        print("No issues found that needed fixing")