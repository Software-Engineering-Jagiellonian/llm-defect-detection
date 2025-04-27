#!/usr/bin/env python3
import json
import sys
import os
from collections import defaultdict

def extract_stats(file_path, output_prefix):
    """Extract statistics from a large JSON data file"""
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
    
    # Group data by model_id
    model_data = defaultdict(list)
    for entry in data:
        model_id = entry.get('model_id')
        if model_id is not None:
            model_data[model_id].append(entry)
    
    # Create a summary for each model
    model_stats = {}
    for model_id, entries in model_data.items():
        # Count entries, bugs identified, false positives
        total = len(entries)
        bugs_identified = sum(1 for e in entries if e.get('bugs_identified', 0) > 0)
        false_positives = sum(1 for e in entries if e.get('false_positives', 0) > 0)
        purpose_identified = sum(1 for e in entries if e.get('purpose_identified', False))
        
        # Calculate average code analysis rating
        ratings = [e.get('code_analysis_rating', 0) for e in entries]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        
        model_stats[model_id] = {
            'total_entries': total,
            'bugs_identified': bugs_identified,
            'bugs_identified_percent': (bugs_identified / total) * 100 if total else 0,
            'false_positives': false_positives,
            'false_positives_percent': (false_positives / total) * 100 if total else 0,
            'purpose_identified': purpose_identified,
            'purpose_identified_percent': (purpose_identified / total) * 100 if total else 0,
            'avg_code_analysis_rating': avg_rating
        }
    
    # Save the summaries to separate files
    output_file = f"{output_prefix}_model_stats.json"
    with open(output_file, 'w') as f:
        json.dump(model_stats, f, indent=2)
    print(f"Saved model statistics to {output_file}")
    
    # Create a table-friendly summary for quick viewing
    table_data = []
    for model_id, stats in model_stats.items():
        row = {
            'model_id': model_id,
            'total_entries': stats['total_entries'],
            'bugs_identified_percent': round(stats['bugs_identified_percent'], 2),
            'false_positives_percent': round(stats['false_positives_percent'], 2),
            'avg_code_analysis_rating': round(stats['avg_code_analysis_rating'], 2)
        }
        table_data.append(row)
    
    # Save the table data
    table_file = f"{output_prefix}_table.json"
    with open(table_file, 'w') as f:
        json.dump(table_data, f, indent=2)
    print(f"Saved table-friendly data to {table_file}")
    
    # Print a simple summary to console
    print("\nModel Summary:")
    print("=" * 60)
    print(f"{'Model ID':<10} {'Entries':<10} {'Bugs(%)':<10} {'FP(%)':<10} {'Rating':<10}")
    print("-" * 60)
    for model_id, stats in model_stats.items():
        print(f"{model_id:<10} {stats['total_entries']:<10} "
              f"{stats['bugs_identified_percent']:.2f}%{'':5} "
              f"{stats['false_positives_percent']:.2f}%{'':5} "
              f"{stats['avg_code_analysis_rating']:.2f}")
    print("=" * 60)

def main():
    if len(sys.argv) < 3:
        print("Usage: extract_model_stats.py <json_file_path> <output_prefix>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    output_prefix = sys.argv[2]
    extract_stats(file_path, output_prefix)

if __name__ == "__main__":
    main()