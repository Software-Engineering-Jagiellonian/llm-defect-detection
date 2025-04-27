# LLM Defect Detection

This repository contains datasets and evaluation scripts for using Large Language Models (LLMs) for static code analysis and defect detection. The project is organized as part of academic research focused on investigating LLMs for identifying code defects.

## Repository Structure

```
llm-defect-detection/
├── outputs/
│   ├── js/                 # JavaScript code examples
│   │   ├── big_repo/       # Large codebase examples
│   │   ├── comprehension/  # Code understanding examples
│   │   ├── simple/         # Simple defect examples
│   │   └── small_repo/     # Small codebase examples
│   └── python/             # Python code examples (same structure)
└── LICENSE
└── README.md
```

## Dataset Description

The repository contains code examples in JavaScript and Python, organized into different categories:

### 1. Simple Defects (`simple/`)

Simple code snippets with common programming errors and vulnerabilities such as:
- API misuse (e.g., deprecated functions)
- Security vulnerabilities
- Coding anti-patterns
- Basic syntax and logic errors

Each example includes:
- An ID
- A name/description
- Correctness flag (True/False)
- Issue description
- External reference link (when available)
- Code snippet
- Fix (when available)

### 2. Code Comprehension (`comprehension/`)

More complex code examples that require deeper understanding of programming concepts such as:
- Function composition
- Recursion
- Higher-order functions
- Event handling
- Data processing

Each example includes paired correct and incorrect versions of the same code with documented issues.

### 3. Small and Big Repositories (`small_repo/` and `big_repo/`)

Code examples simulating real-world repositories with:
- Multiple files and components
- Data files structured in JSON format
- Issues documented in Python scripts

## Usage

This dataset is designed for evaluating and training LLMs on code defect detection. Researchers can use these examples to:

1. Test an LLM's ability to identify defects in code
2. Compare performance across different programming languages
3. Evaluate comprehension of different types of coding errors
4. Benchmark LLM performance on progressively more complex code examples

## Academic Research

This repository is part of an academic research project investigating Large Language Models for static code analysis and defect detection conducted at Jagiellonian University, Poland.\
The authors of the study are:
- Ewa Woźny (main contributor)
- Jarek Hryszko (corresponding author -- jaroslaw dot hryszko at uj dot edu dot pl)
- Adam Roman
