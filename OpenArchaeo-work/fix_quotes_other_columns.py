#!/usr/bin/env python3
"""
Script to ensure all fields (except the description) that contain spaces or special characters
are properly quoted in a CSV file, without creating triple quotes.

This script handles cases where a field has only one quote (opening or closing).

This script assumes:
1. The description field (second column) is already properly quoted
2. No fields contain internal commas (commas are only column separators)
"""

import sys
import os
import csv
import time

def needs_quotes(field):
    """
    Determine if a field needs quotes based on its content.
    
    Args:
        field (str): Field value to check
        
    Returns:
        bool: True if the field needs quotes
    """
    # Check for spaces or special characters that would require quoting
    special_chars = ' -:/\\.,+&()[]{}=*#!?;\'`<>|'
    return any(char in field for char in special_chars)

def clean_and_quote_field(field):
    """
    Clean a field by removing any existing quotes, then add proper quotes if needed.
    Handles cases with single quotes or unmatched quotes.
    
    Args:
        field (str): Field to process
        
    Returns:
        str: Properly quoted field, and a boolean indicating if it was changed
    """
    original_field = field
    
    # Remove any quotes at the beginning
    while field.startswith('"'):
        field = field[1:]
    
    # Remove any quotes at the end
    while field.endswith('"'):
        field = field[:-1]
    
    # Now we have the clean content without any quotes
    
    # Add quotes if needed
    if needs_quotes(field):
        final_field = f'"{field}"'
    else:
        final_field = field
    
    # Return the fixed field and whether it changed
    return final_field, final_field != original_field

def quote_other_fields(input_file, output_file, encoding='utf-8'):
    """
    Ensure all fields (except description) containing spaces or special characters are quoted.
    
    Args:
        input_file (str): Path to the input CSV file
        output_file (str): Path to save the fixed CSV file
        encoding (str): File encoding to use
    
    Returns:
        tuple: (fields_fixed, rows_with_fixes, total_rows_processed)
    """
    print(f"✓ Reading file: {input_file}")
    
    # Try to read with the specified encoding, fall back to latin-1 if needed
    try:
        with open(input_file, 'r', encoding=encoding) as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print(f"ℹ️ Error reading with {encoding} encoding, trying latin-1...")
        with open(input_file, 'r', encoding='latin-1') as f:
            lines = f.readlines()
        encoding = 'latin-1'
    
    fixed_lines = []
    total_fields_fixed = 0
    rows_with_fixes = 0
    total_rows = len(lines) - 1  # Excluding header
    
    # Keep header as is
    if lines:
        fixed_lines.append(lines[0].rstrip())
    
    print(f"ℹ️ Processing {total_rows} data rows...")
    
    # Process data rows with a progress counter
    for i, line in enumerate(lines[1:], 1):
        # Show progress for larger files
        if i % 100 == 0 or i == total_rows:
            progress = (i / total_rows) * 100
            print(f"ℹ️ Progress: {i}/{total_rows} rows ({progress:.1f}%)")
        
        line = line.rstrip()
        if not line.strip():  # Skip empty lines
            fixed_lines.append("")
            continue
        
        # Parse the line with csv reader to handle complex cases
        fields_fixed_in_row = 0
        try:
            # Try using the CSV reader first
            reader = csv.reader([line])
            fields = next(reader)
            fixed_fields = []
            
            for j, field in enumerate(fields):
                # Skip the description field (index 1) which should already be fixed
                if j == 1:
                    fixed_fields.append(field)
                    continue
                
                # Fix quotes in this field
                fixed_field, was_fixed = clean_and_quote_field(field)
                
                if was_fixed:
                    fields_fixed_in_row += 1
                
                fixed_fields.append(fixed_field)
            
            # Rebuild the line
            output = []
            writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fixed_fields)
            fixed_line = output[0].rstrip()
            
            # Just to be sure, clean up any triple quotes that might still exist
            if '"""' in fixed_line:
                fixed_line = fixed_line.replace('"""', '"')
                print(f"ℹ️ Row {i}: Removed triple quotes")
            
            # Update counters
            total_fields_fixed += fields_fixed_in_row
            
            # Show examples of fixes
            if fields_fixed_in_row > 0:
                rows_with_fixes += 1
                if i <= 5:  # Only show the first 5 examples
                    print(f"\n✓ Row {i}:")
                    print(f"  Before: {line[:100]}...")
                    print(f"  After:  {fixed_line[:100]}...")
                    print(f"  Fixed {fields_fixed_in_row} fields in this row")
        
        except Exception as e:
            # If CSV reader fails (possibly due to malformed quotes),
            # use a more manual approach
            print(f"⚠️ CSV parsing error on row {i}: {str(e)}")
            print("  Using manual field extraction...")
            
            # Split the line by commas, but keep the description field intact
            # First find the first comma
            first_comma_idx = line.find(',')
            if first_comma_idx > 0:
                # Extract the item_name
                item_name = line[:first_comma_idx]
                
                # Find the second comma that's not inside the description
                # This is tricky if the description has quotes...
                # For simplicity, we'll try to parse smartly
                
                # Check if the description starts with a quote
                rest_of_line = line[first_comma_idx+1:]
                if rest_of_line.startswith('"'):
                    # Find the matching end quote
                    end_quote_idx = rest_of_line.find('",', 1)
                    if end_quote_idx > 0:
                        # Found the end of the description
                        description = rest_of_line[:end_quote_idx+1]
                        remainder = rest_of_line[end_quote_idx+2:]
                        
                        # Now process the remaining fields
                        remainder_fields = remainder.split(',')
                        fixed_remainder_fields = []
                        remainder_fixes = 0
                        
                        for field in remainder_fields:
                            fixed_field, was_fixed = clean_and_quote_field(field)
                            fixed_remainder_fields.append(fixed_field)
                            if was_fixed:
                                remainder_fixes += 1
                        
                        # Reconstruct the line
                        fixed_line = item_name + ',' + description + ',' + ','.join(fixed_remainder_fields)
                        fields_fixed_in_row = remainder_fixes
                    else:
                        # Couldn't find the end of the description
                        fixed_line = line
                else:
                    # Description doesn't start with a quote - harder to parse
                    # For safety, keep the line as is
                    fixed_line = line
            else:
                # No comma found - unlikely but handle it
                fixed_line = line
            
            # Show the manual fix
            if fields_fixed_in_row > 0:
                rows_with_fixes += 1
                if i <= 5:  # Only show the first 5 examples
                    print(f"  Manual fix results:")
                    print(f"  Before: {line[:100]}...")
                    print(f"  After:  {fixed_line[:100]}...")
                
                # Update the total counter
                total_fields_fixed += fields_fixed_in_row
            
            # Just to be sure, clean up any triple quotes
            if '"""' in fixed_line:
                fixed_line = fixed_line.replace('"""', '"')
        
        fixed_lines.append(fixed_line)
    
    # Write the fixed file
    print(f"\n✓ Writing fixed file to: {output_file}")
    with open(output_file, 'w', encoding=encoding) as f:
        f.write('\n'.join(fixed_lines))
    
    return total_fields_fixed, rows_with_fixes, total_rows

def check_for_unbalanced_quotes(file_path, encoding='utf-8'):
    """
    Check if there are any fields with unbalanced quotes in the file.
    
    Args:
        file_path (str): Path to the CSV file
        encoding (str): File encoding to use
    """
    print(f"\nVerifying quote balance in: {file_path}")
    
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            reader = csv.reader(f)
            header = next(reader)
            
            unbalanced_count = 0
            row_count = 0
            
            for i, row in enumerate(reader, 1):
                row_count += 1
                
                for j, field in enumerate(row):
                    # Check for fields that start with a quote but don't end with one, or vice versa
                    if (field.startswith('"') and not field.endswith('"')) or \
                       (field.endswith('"') and not field.startswith('"')):
                        unbalanced_count += 1
                        if unbalanced_count <= 5:  # Limit to first 5 examples
                            print(f"⚠️ Row {i}, Column {j+1}: Unbalanced quotes - '{field[:30]}...'")
            
            if unbalanced_count == 0:
                print(f"✓ All quotes are balanced across {row_count} rows!")
            else:
                print(f"⚠️ Found {unbalanced_count} fields with unbalanced quotes.")
                
    except Exception as e:
        print(f"⚠️ Error checking for unbalanced quotes: {str(e)}")
        # If CSV reader fails, it might be due to unbalanced quotes
        print("  CSV parsing error suggests there might be unbalanced quotes.")

def check_for_triple_quotes(file_path, encoding='utf-8'):
    """
    Check if there are any triple quotes in the file.
    
    Args:
        file_path (str): Path to the CSV file
        encoding (str): File encoding to use
    
    Returns:
        int: Number of fields with triple quotes
    """
    print(f"\nChecking for triple quotes in: {file_path}")
    
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()
        
        triple_count = content.count('"""')
        
        if triple_count > 0:
            print(f"⚠️ Found {triple_count} instances of triple quotes")
            
            # Try to locate the triple quotes
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if '"""' in line:
                    print(f"  Triple quotes found in row {i+1}")
                    if i < 5:  # Show the first few problematic lines
                        print(f"  Line preview: {line[:50]}...")
        else:
            print("✓ No triple quotes found - quoting is correct!")
        
        return triple_count
    
    except Exception as e:
        print(f"⚠️ Error checking for triple quotes: {str(e)}")
        return -1

def verify_field_quotes(file_path, encoding='utf-8'):
    """
    Verify that all fields that need quotes have them.
    
    Args:
        file_path (str): Path to the CSV file to check
        encoding (str): File encoding to use
    """
    print(f"\nVerifying quotes in fields: {file_path}")
    
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            reader = csv.reader(f)
            header = next(reader)
            
            unquoted_count = 0
            row_count = 0
            field_count = 0
            
            for i, row in enumerate(reader, 1):
                row_count += 1
                
                for j, field in enumerate(row):
                    # Skip the description field (index 1)
                    if j == 1:
                        continue
                    
                    field_count += 1
                    
                    # Check if field needs quotes but doesn't have them
                    stripped_field = field.strip('"')
                    
                    if needs_quotes(stripped_field) and not (field.startswith('"') and field.endswith('"')):
                        unquoted_count += 1
                        if unquoted_count <= 5:  # Limit to first 5 examples
                            shortened = stripped_field[:20] + "..." if len(stripped_field) > 20 else stripped_field
                            print(f"⚠️ Row {i}, Column {j+1}: Missing quotes - '{shortened}'")
            
            if unquoted_count == 0:
                print(f"✓ All {field_count} fields that need quotes have them! ({row_count} rows checked)")
            else:
                percentage = (unquoted_count / field_count) * 100 if field_count > 0 else 0
                print(f"⚠️ Found {unquoted_count} fields missing quotes ({percentage:.1f}% of all fields)")
    
    except Exception as e:
        print(f"⚠️ Error verifying quotes: {str(e)}")

if __name__ == "__main__":
    print("\n=== CSV Quote Fixer ===")
    
    # Get input and output filenames from command line or use defaults
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'openarchaeoimproved_desc_fixed.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'openarchaeoimproved_all_fixed.csv'
    
    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"⚠️ Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    # Start timing
    start_time = time.time()
    
    # Fix quotes in other fields
    print("\n-- Fixing Quotes in Fields --")
    fields_fixed, rows_fixed, total_rows = quote_other_fields(input_file, output_file)
    
    # End timing
    end_time = time.time()
    processing_time = end_time - start_time
    
    # Verify the fixed file
    if fields_fixed > 0 or rows_fixed > 0:
        check_for_triple_quotes(output_file)
        check_for_unbalanced_quotes(output_file)
        verify_field_quotes(output_file)
        
        # Summary report
        print("\n-- Summary --")
        print(f"✓ Total fields fixed: {fields_fixed}")
        print(f"✓ Rows with fixes: {rows_fixed} out of {total_rows} ({(rows_fixed/total_rows*100):.1f}%)")
        print(f"✓ Processing time: {processing_time:.2f} seconds")
        print(f"✓ Fixed file saved to: {output_file}")
    else:
        print("\n-- Summary --")
        print(f"ℹ️ No fields needed fixing. The CSV appears to be already properly quoted.")
        print(f"ℹ️ Processing time: {processing_time:.2f} seconds")