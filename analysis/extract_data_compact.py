#!/usr/bin/env python3
import json
import sys
import os
from collections import defaultdict

def extract_compact_data(file_path, output_path):
    """Extract key information from large JSON data files into a smaller format"""
    print(f"Processing {file_path}...")
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file")
        return
    except FileNotFoundError:
        print(f"Error: {file_path} does not exist")
        return
    
    if not data:
        print(f"Warning: {file_path} contains no data")
        return
    
    # Extract just the key fields we care about
    compact_data = []
    for entry in data:
        # Skip entries that don't have model_id
        if 'model_id' not in entry:
            continue
            
        compact_entry = {
            'model_id': entry.get('model_id'),
            'bugs_identified': entry.get('bugs_identified', 0),
            'false_positives': entry.get('false_positives', 0),
            'purpose_identified': entry.get('purpose_identified', False),
            'code_analysis_rating': entry.get('code_analysis_rating', 0),
            'question_id': entry.get('question_id', 0),
            'dataset': entry.get('dataset', '')
        }
        compact_data.append(compact_entry)
    
    # Save compact data
    with open(output_path, 'w') as f:
        json.dump(compact_data, f, indent=2)
    
    orig_size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
    new_size = os.path.getsize(output_path) / (1024 * 1024)  # Size in MB
    
    print(f"Original size: {orig_size:.2f} MB")
    print(f"Compact size: {new_size:.2f} MB")
    print(f"Reduction: {(1 - new_size/orig_size) * 100:.2f}%")
    print(f"Saved compact data to {output_path}")

def main():
    if len(sys.argv) < 3:
        print("Usage: extract_data_compact.py <input_json_file> <output_json_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    extract_compact_data(input_file, output_file)

if __name__ == "__main__":
    main()