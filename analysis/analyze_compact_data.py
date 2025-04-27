#!/usr/bin/env python3
import json
import sys
from collections import defaultdict

def analyze_data(file_path):
    """Analyze compact data files and generate statistics"""
    print(f"Analyzing {file_path}...")
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file")
        return
    except FileNotFoundError:
        print(f"Error: {file_path} does not exist")
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
    
    # Print a simple summary to console
    print("\nModel Summary:")
    print("=" * 60)
    print(f"{'Model ID':<10} {'Entries':<10} {'Bugs(%)':<10} {'FP(%)':<10} {'Rating':<10}")
    print("-" * 60)
    
    for model_id in sorted(model_stats.keys()):
        stats = model_stats[model_id]
        print(f"{model_id:<10} {stats['total_entries']:<10} "
              f"{stats['bugs_identified_percent']:.2f}%{'':5} "
              f"{stats['false_positives_percent']:.2f}%{'':5} "
              f"{stats['avg_code_analysis_rating']:.2f}")
    
    print("=" * 60)
    return model_stats

def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_compact_data.py <json_file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    analyze_data(file_path)

if __name__ == "__main__":
    main()