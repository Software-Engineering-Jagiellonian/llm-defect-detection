#!/usr/bin/env python3
import json
import sys
from collections import defaultdict

def extract_stats(file_path, output_prefix):
    """Extract statistics from a simple JSON data file"""
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
    
    # Create a simplified parser for the simple data format
    # Extract unique model IDs from the data
    model_results = defaultdict(lambda: {'total': 0, 'correct': 0})
    
    for entry in data:
        # Skip entries without both model and result fields
        if not isinstance(entry, dict) or 'model' not in entry or 'result' not in entry:
            continue
            
        model_name = entry['model']
        result = entry.get('result', {})
        
        # Increment counters
        model_results[model_name]['total'] += 1
        if result.get('correct', False):
            model_results[model_name]['correct'] += 1
    
    # Calculate percentages and format results
    formatted_results = {}
    for model, counts in model_results.items():
        total = counts['total']
        correct = counts['correct']
        percent = (correct / total * 100) if total > 0 else 0
        
        formatted_results[model] = {
            'total': total,
            'correct': correct,
            'percent_correct': percent
        }
    
    # Save the results
    output_file = f"{output_prefix}_stats.json"
    with open(output_file, 'w') as f:
        json.dump(formatted_results, f, indent=2)
    print(f"Saved statistics to {output_file}")
    
    # Print a summary to console
    print("\nModel Summary:")
    print("=" * 70)
    print(f"{'Model':<30} {'Total':<10} {'Correct':<10} {'Percent':<10}")
    print("-" * 70)
    
    for model, stats in formatted_results.items():
        print(f"{model:<30} {stats['total']:<10} {stats['correct']:<10} {stats['percent_correct']:.2f}%")
    
    print("=" * 70)

def main():
    if len(sys.argv) < 3:
        print("Usage: extract_model_stats_simple.py <json_file_path> <output_prefix>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    output_prefix = sys.argv[2]
    extract_stats(file_path, output_prefix)

if __name__ == "__main__":
    main()