# LLM Defect Detection Analysis

This directory contains tools for analyzing the data from the LLM defect detection repository.

## Data Files

The original data files in the `llm-defect-detection` repository are quite large:

- `outputs/js/simple/data.json`: 4.4 MB
- `outputs/python/simple/data.json`: 3.1 MB
- `outputs/python/comprehension/data.json`: 400 KB
- `outputs/js/comprehension/data.json`: 392 KB
- `outputs/js/small_repo/data/data_p3.json`: 340 KB
- `outputs/js/small_repo/data/data_p1.json`: 268 KB

## Tools

The following tools have been created to help analyze this data:

1. `extract_model_stats.py` - Extracts statistics from comprehension datasets
2. `extract_data_compact.py` - Creates compact versions of the large data files
3. `analyze_compact_data.py` - Analyzes the compact data files for basic statistics

## Model ID Mapping

The model IDs likely correspond to:

- Model ID 1: Meta-Llama-3-70B
- Model ID 2: Mistral-7b-instruct-v0.2
- Model ID 6: Deepseek-coder-7b-instruct-v1.5
- Model ID 8: Phi-3-medium-128k-instruct or Nous-Hermes-2-Mixtral-8x7B-DPO
- Model ID 16: C4ai-command-r-plus
- Model ID 21: Related to one of the above

## Summary of Findings

### Python Comprehension Test Set
```
Model ID   Entries    Bugs(%)    FP(%)      Rating    
------------------------------------------------------------
2          37         37.84%      13.51%      4.41
16         37         40.54%      13.51%      4.46
1          37         40.54%      10.81%      4.54
21         37         43.24%      45.95%      3.76
8          37         29.73%      18.92%      4.00
6          37         21.62%      10.81%      4.03
```

### JavaScript Comprehension Test Set
```
Model ID   Entries    Bugs(%)    FP(%)      Rating    
------------------------------------------------------------
6          29         20.69%      31.03%      3.72
18         29         31.03%      24.14%      3.45
8          29         34.48%      10.34%      4.07
1          29         48.28%      27.59%      4.14
21         29         44.83%      13.79%      4.45
2          29         48.28%      17.24%      4.31
16         29         51.72%      13.79%      4.48
```

### Python Simple Test Set
```
Model ID   Entries    Bugs(%)    FP(%)      Rating    
------------------------------------------------------------
1          144        62.50%      0.00%      3.82
2          144        58.33%      0.00%      3.60
...
16         144        68.06%      0.00%      4.02
...
21         144        62.50%      0.00%      3.78
```

### JavaScript Simple Test Set
```
Model ID   Entries    Bugs(%)    FP(%)      Rating    
------------------------------------------------------------
1          192        61.98%      0.00%      4.00
2          187        56.15%      0.00%      3.74
6          188        67.02%      0.00%      3.97
8          187        53.48%      0.00%      3.41
...
16         186        54.30%      0.00%      3.47
...
21         186        52.15%      0.00%      3.54
```

Note that false positives (FP) are only recorded in the comprehension datasets. The simple datasets do not track false positives.
