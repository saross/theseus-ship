#!/usr/bin/env python3
"""
A robust script to properly quote the description field in CSV files,
handling commas within the description.

The description field:
1. Is the second column (after the first comma)
2. May contain commas itself
3. Ends before the github column (which starts with https://github or is empty)
"""

import sys
import os
import re
import csv

def fix_description_quotes(input_file, output_file, encoding='utf-8'):
    """
    Fix quotes for the description field, handling commas within the description.
    
    Args:
        input_file (str): Path to the input CSV file
        output_file (str): Path to save the fixed CSV file
        encoding (str): File encoding to use
    """
    print(f"Reading file: {input_file}")
    
    # Try to read with the specified encoding, fall back to latin-1 if needed
    try:
        with open(input_file, 'r', encoding=encoding) as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print(f"Error reading with {encoding} encoding, trying latin-1...")
        with open(input_file, 'r', encoding='latin-1') as f:
            lines = f.readlines()
        encoding = 'latin-1'
    
    # Get the header
    header = lines[0].strip() if lines else ""
    
    # Analyze the header to find the position of the github column
    header_fields = header.split(',')
    github_column_index = None
    for i, field in enumerate(header_fields):
        if field.lower() == 'github':
            github_column_index = i
            break
    
    if github_column_index is None:
        print("Warning: Could not find 'github' column in header. Using default position (2).")
        github_column_index = 2
    
    print(f"GitHub column is at index {github_column_index} (0-based)")
    
    fixed_lines = [header]  # Keep header as is
    fixed_count = 0
    
    # Process each line (skip header)
    for i, line in enumerate(lines[1:], 1):
        line = line.strip()
        if not line:  # Skip empty lines
            fixed_lines.append("")
            continue
        
        # First, try to parse the CSV line properly
        reader = csv.reader([line])
        try:
            fields = next(reader)
            
            # If we have enough fields, we can extract the description
            if len(fields) > github_column_index:
                # Get the item_name (first column)
                item_name = fields[0]
                
                # Get the description (second column)
                description = fields[1]
                
                # Handle case where description field might already be quoted
                # If it has quotes, let's remove them for consistency
                description = description.strip('"')
                
                # Create a new fields list with the quoted description
                new_fields = fields.copy()
                new_fields[1] = f'"{description}"'
                
                # Check if we changed anything
                if new_fields[1] != fields[1]:
                    fixed_count += 1
                
                # Write the new fields back to a CSV line
                output = []
                writer = csv.writer(output, quoting=csv.QUOTE_NONE, escapechar='\\')
                writer.writerow(new_fields)
                fixed_line = output[0]
                
                # Remove any escaping of quotes that csv.writer might have added
                fixed_line = fixed_line.replace('\\"', '"')
                
                fixed_lines.append(fixed_line)
                
                # Show examples for the first few fixes
                if new_fields[1] != fields[1] and i <= 10:
                    print(f"\nRow {i}:")
                    print(f"  Original description: {fields[1]}")
                    print(f"  Fixed description: {new_fields[1]}")
            else:
                # Not enough fields - keep the line as is
                fixed_lines.append(line)
                print(f"Warning: Line {i+1} has fewer fields than expected ({len(fields)})")
        
        except Exception as e:
            # CSV parsing failed - the line is likely malformed
            # Let's use a more robust approach
            print(f"CSV parsing error on line {i+1}: {str(e)}")
            
            # Try a more manual approach for problematic lines
            fixed_line = fix_line_manually(line, github_column_index)
            fixed_lines.append(fixed_line)
            fixed_count += 1
    
    # Write the fixed file
    print(f"\nWriting fixed file to: {output_file}")
    with open(output_file, 'w', encoding=encoding) as f:
        f.write('\n'.join(fixed_lines))
    
    print(f"\nFixed {fixed_count} description fields.")
    return fixed_count

def fix_line_manually(line, github_column_index):
    """
    Fix a problematic line manually by looking for specific patterns.
    
    Args:
        line (str): The CSV line to fix
        github_column_index (int): The expected position of the github column
    
    Returns:
        str: The fixed line
    """
    # Find the first comma
    first_comma_idx = line.find(',')
    if first_comma_idx < 0:
        return line  # No comma, return as is
    
    # Get the item_name
    item_name = line[:first_comma_idx]
    rest_of_line = line[first_comma_idx+1:]
    
    # Check if the rest already starts with a quote
    has_opening_quote = rest_of_line.startswith('"')
    
    # Try to find patterns that indicate the end of the description
    # Look for github URL or consecutive commas
    github_pattern = r',\s*https?://github\.com/'
    github_match = re.search(github_pattern, rest_of_line)
    
    # Also look for consecutive commas that might indicate an empty github field
    empty_pattern = r',\s*,'
    empty_match = re.search(empty_pattern, rest_of_line)
    
    # Determine where the description ends
    end_pos = -1
    
    if has_opening_quote:
        # If there's an opening quote, try to find the matching closing quote
        # This is tricky because there might be escaped quotes inside
        pos = 1
        while pos < len(rest_of_line):
            next_quote = rest_of_line.find('"', pos)
            if next_quote < 0:
                break
            
            # Check if the next char after this quote is a comma (end of field)
            if next_quote + 1 < len(rest_of_line) and rest_of_line[next_quote+1] == ',':
                # This is likely the end of the quoted description
                end_pos = next_quote + 1
                break
            
            # Otherwise, this quote is part of the content; keep searching
            pos = next_quote + 1
    
    # If we couldn't find the end based on quotes, try pattern matching
    if end_pos < 0:
        if github_match:
            # Found a GitHub URL - likely indicates start of third column
            # The comma right before it is the end of the description
            end_pos = github_match.start()
        elif empty_match:
            # Found consecutive commas - the first one ends the description
            end_pos = empty_match.start()
    
    # If we still couldn't find the end, make a best guess
    # Try to find the expected number of commas
    if end_pos < 0:
        # Count commas to find the one that should end the description field
        count = 0
        for j, char in enumerate(rest_of_line):
            if char == ',':
                count += 1
                if count == github_column_index - 1:
                    end_pos = j
                    break
    
    # If we found where the description ends
    if end_pos >= 0:
        # Extract the description content
        description = rest_of_line[:end_pos]
        remainder = rest_of_line[end_pos:]
        
        # If the description was already quoted, unquote it first
        if has_opening_quote and description.endswith('"'):
            description = description[1:-1]
        elif has_opening_quote:
            description = description[1:]
        
        # Build the fixed line
        fixed_line = f'{item_name},"{description}"{remainder}'
        return fixed_line
    
    # If all else fails, just ensure the description is quoted
    if has_opening_quote:
        # It already has an opening quote, but might be missing the closing quote
        # Add a closing quote before the first comma (if any)
        next_comma = rest_of_line.find(',')
        if next_comma >= 0:
            fixed_line = f'{item_name},{rest_of_line[:next_comma]}"{rest_of_line[next_comma:]}'
        else:
            fixed_line = f'{item_name},{rest_of_line}"'
    else:
        # No opening quote, add both opening and closing quotes
        next_comma = rest_of_line.find(',')
        if next_comma >= 0:
            fixed_line = f'{item_name},"{rest_of_line[:next_comma]}"{rest_of_line[next_comma:]}'
        else:
            fixed_line = f'{item_name},"{rest_of_line}"'
    
    return fixed_line

def verify_csv_integrity(file_path, encoding='utf-8'):
    """
    Verify the integrity of a CSV file by checking field counts and parsing.
    
    Args:
        file_path (str): Path to the CSV file
        encoding (str): File encoding to use
    """
    print(f"\nVerifying CSV integrity: {file_path}")
    
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            reader = csv.reader(f)
            header = next(reader)
            expected_fields = len(header)
            
            print(f"Header has {expected_fields} fields")
            
            row_count = 0
            error_count = 0
            
            for i, row in enumerate(reader, 1):
                row_count += 1
                
                if len(row) != expected_fields:
                    print(f"Row {i+1}: Expected {expected_fields} fields, got {len(row)}")
                    error_count += 1
                    
                    if error_count <= 5:  # Limit the number of errors shown
                        print(f"  Item name: {row[0] if row else 'N/A'}")
                        print(f"  Fields: {len(row)}")
            
            if error_count == 0:
                print(f"CSV validated successfully! All {row_count} rows have {expected_fields} fields.")
            else:
                print(f"Found {error_count} rows with incorrect field counts out of {row_count} total rows.")
                
    except Exception as e:
        print(f"Error validating CSV: {str(e)}")

def check_description_quotes(file_path, encoding='utf-8'):
    """
    Check that description fields are properly quoted.
    
    Args:
        file_path (str): Path to the CSV file
        encoding (str): File encoding to use
    """
    print(f"\nChecking description quotes in: {file_path}")
    
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            reader = csv.reader(f)
            header = next(reader)
            
            row_count = 0
            unquoted_count = 0
            
            for i, row in enumerate(reader, 1):
                row_count += 1
                
                if len(row) > 1:
                    description = row[1]
                    # The raw field will include the quotes if they exist
                    if not (description.startswith('"') and description.endswith('"')):
                        unquoted_count += 1
                        if unquoted_count <= 5:
                            print(f"Row {i+1}: Description not properly quoted")
                            print(f"  Description: {description[:50]}...")
            
            if unquoted_count == 0:
                print(f"All {row_count} description fields are properly quoted!")
            else:
                print(f"Found {unquoted_count} description fields not properly quoted out of {row_count} rows.")
    
    except Exception as e:
        print(f"Error checking description quotes: {str(e)}")

if __name__ == "__main__":
    # Get input and output filenames from command line or use defaults
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'openarchaeoimproved.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'openarchaeoimproved_fixed.csv'
    
    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    # Fix the description quotes
    fixes = fix_description_quotes(input_file, output_file)
    
    # Verify the fixed file
    if fixes > 0:
        verify_csv_integrity(output_file)
        check_description_quotes(output_file)