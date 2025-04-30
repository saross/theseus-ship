#!/usr/bin/env python
# Script to fix Archive.org URLs in the internetarchive column of a CSV file

import csv
import re
import os

def fix_internetarchive_column(input_file, output_file):
    """
    Fixes a CSV file by ensuring all archive.org URLs appear in the 'internetarchive' column
    while preserving all original quotation marks.
    
    Args:
        input_file: Path to the input CSV file
        output_file: Path to write the corrected CSV file
    """
    # First pass - determine the column index of 'internetarchive'
    with open(input_file, 'r', encoding='utf-8') as file:
        # Read header line
        header_line = file.readline().strip()
        
        # Split the header using our custom function that preserves quotation
        header_fields = split_csv_preserving_quotes(header_line)
        
        # Find the index of the 'internetarchive' column
        internetarchive_index = -1
        for i, field in enumerate(header_fields):
            if field.strip('"') == 'internetarchive':
                internetarchive_index = i
                break
        
        if internetarchive_index == -1:
            raise ValueError("Could not find 'internetarchive' column in header")
        
        print(f"'internetarchive' column found at index {internetarchive_index} (column {internetarchive_index + 1})")
        
        # Get total expected columns
        expected_columns = len(header_fields)
        print(f"Header has {expected_columns} columns")
        
        # Read the rest of the file
        lines = [header_line] + [line.strip() for line in file]
    
    # Second pass - process each line and fix URLs
    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        # Write header as-is
        file.write(lines[0] + '\n')
        
        # Process each data row
        for line_num, line in enumerate(lines[1:], 2):
            # Find if this line has an archive.org URL
            archive_url_match = re.search(r'https://archive\.org/[^,"]*', line)
            
            if not archive_url_match:
                file.write(line + '\n')
                print(f"Line {line_num}: No archive.org URL found, writing as-is")
                continue
            
            archive_url = archive_url_match.group(0)
            print(f"Line {line_num}: Found archive.org URL: {archive_url}")
            
            # Split the line preserving quoted fields
            raw_fields = split_csv_preserving_quotes(line)
            
            # Check if we have the correct number of fields
            if len(raw_fields) != expected_columns:
                print(f"Line {line_num}: Warning - Found {len(raw_fields)} fields instead of {expected_columns}")
                
                # Adjust field count while preserving content
                if len(raw_fields) < expected_columns:
                    # Too few fields - add empty fields
                    raw_fields.extend([''] * (expected_columns - len(raw_fields)))
                elif len(raw_fields) > expected_columns:
                    # Too many fields - consolidate excess fields
                    excess = ' '.join(raw_fields[expected_columns:])
                    raw_fields = raw_fields[:expected_columns-1] + [raw_fields[expected_columns-1] + ' ' + excess]
            
            # Check which field contains the archive.org URL
            url_field_index = None
            for i, field in enumerate(raw_fields):
                if archive_url in field:
                    url_field_index = i
                    break
            
            # If we found the URL field
            if url_field_index is not None:
                print(f"Line {line_num}: URL found in field {url_field_index+1} of {len(raw_fields)}")
                
                # Remove the URL from its current position
                # Be careful not to modify quotation marks
                if url_field_index != internetarchive_index:
                    raw_fields[url_field_index] = raw_fields[url_field_index].replace(archive_url, '').strip()
                    
                    # Format the URL with a single set of quotation marks
                    # The quoting should mirror the existing pattern in the file
                    if not raw_fields[internetarchive_index].strip():
                        # If empty, use the standard format with quotes
                        raw_fields[internetarchive_index] = f'"{archive_url}"'
                    else:
                        # If there's already something there, append with correct quoting
                        # This shouldn't happen if URL should be the only thing in this column
                        current = raw_fields[internetarchive_index].strip('"')
                        raw_fields[internetarchive_index] = f'"{current} {archive_url}"'
                
                # Rejoin the fields into a CSV line, carefully preserving quotes
                output_line = ','.join(raw_fields)
                file.write(output_line + '\n')
                print(f"Line {line_num}: Fixed - archive.org URL positioned in the internetarchive column")
            else:
                # This shouldn't happen if we found the URL with regex
                print(f"Line {line_num}: Error - Found URL with regex but couldn't locate it in fields")
                file.write(line + '\n')
    
    print(f"\nProcessing complete! Fixed CSV written to {output_file}")

def split_csv_preserving_quotes(line):
    """
    Split a CSV line into fields while preserving all quotation marks exactly as they are.
    This handles quoted fields containing commas properly.
    """
    fields = []
    current_field = ""
    in_quotes = False
    
    for char in line:
        if char == '"':
            in_quotes = not in_quotes
            current_field += char
        elif char == ',' and not in_quotes:
            fields.append(current_field)
            current_field = ""
        else:
            current_field += char
    
    # Don't forget the last field
    fields.append(current_field)
    return fields

if __name__ == "__main__":
    input_file = "open-archaeo-improved-1_fixed_all.csv"
    output_file = "open-archaeo-improved-1_fixed_final.csv"
    
    print(f"Starting to process {input_file}...")
    fix_internetarchive_column(input_file, output_file)
    
    # Verify all URLs are in the internetarchive column
    print("\nVerifying URL placement...")
    with open(output_file, 'r', encoding='utf-8') as file:
        # Get header and find internetarchive column index
        header = file.readline().strip()
        header_fields = split_csv_preserving_quotes(header)
        internetarchive_index = -1
        for i, field in enumerate(header_fields):
            if field.strip('"') == 'internetarchive':
                internetarchive_index = i
                break
        
        # Check each data row
        incorrect_placements = 0
        for i, line in enumerate(file, 2):
            fields = split_csv_preserving_quotes(line.strip())
            # Check if archive.org URL appears in any column other than internetarchive
            for j, field in enumerate(fields):
                if j != internetarchive_index and 'archive.org' in field:
                    print(f"Error: Line {i} has archive.org URL in column {j+1} (should be in column {internetarchive_index+1})")
                    incorrect_placements += 1
                    break
        
        if incorrect_placements == 0:
            print(f"✅ All archive.org URLs are correctly positioned in the internetarchive column")
        else:
            print(f"❌ Found {incorrect_placements} rows with incorrectly positioned archive.org URLs")


if __name__ == "__main__":
    input_file = "open-archaeo-improved-1_fixed_all.csv"
    output_file = "open-archaeo-improved-1_fixed_final.csv"
    
    print(f"Starting to process {input_file}...")
    fix_internetarchive_column(input_file, output_file)
    
    # Verify column counts match between input and output
    if os.path.exists(output_file):
        with open(input_file, 'r', encoding='utf-8') as infile:
            input_header = infile.readline().strip()
            input_columns = input_header.count(',') + 1
        
        with open(output_file, 'r', encoding='utf-8') as outfile:
            output_header = outfile.readline().strip()
            output_columns = output_header.count(',') + 1
        
        print(f"Verification: Input has {input_columns} columns, output has {output_columns} columns")
        if input_columns == output_columns:
            print("✅ Column count matches between input and output files")
        else:
            print("⚠️ Column count mismatch between input and output files")