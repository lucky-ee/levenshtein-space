# levenshtein-space

A high-performance interactive command-line spell-checker built with Python.
It organizes words into a discrete metric space and uses the Levenshtein distance and a BK-Tree search algorithm to instantly find autocomplete matches without brute-forcing the entire dictionary.

## Project Structure

`engine.py` - Runs the interactive search loop and handles terminal arguments
`bktree.py` - Contains the BKNode and BKTree data structures
`test_engine.py` - Automated unit tests for metric axioms and tree logic
`README.md` - Project documentation

## Features

* Custom Levenshtein distance metric
* BK-Tree implementation for optimal search clustering
* Triangle inequality optimization to instantly prune mathematical dead-ends
* Interactive command-line loop
* Built-in argument parsing for quick terminal queries
* Automated unit testing

## Getting Started

### Prerequisites

* Python 3.x
* A standard dictionary text file (built-in on Mac/Linux at `/usr/share/dict/words`)

### Installation

Clone the repository:
```bash
git clone [https://github.com/YOUR-USERNAME/metric-spell-checker.git](https://github.com/YOUR-USERNAME/metric-spell-checker.git)
cd metric-spell-checker
```

### Development

Start the interactive engine:
```bash
python3 engine.py
```

When the tree builds successfully, the terminal will show that it is ready.
In the terminal, enter a misspelled word and your desired tolerance level. 

You can also test the metric axioms and tree logic by running:
```bash
python3 test_engine.py
```

## CLI Commands

`python3 engine.py`                  Launch the interactive loop
`python3 engine.py [word]`           Search for a specific word directly
`python3 engine.py [word] -t 3`      Search with a custom tolerance level (e.g., 3)
`python3 engine.py [word] -d [path]` Search using a custom dictionary text file
`python3 engine.py --help`           Display the available commands

## Git Ignore

The following files should be included in `.gitignore`:
```text
# Python-generated files
__pycache__/
*.pyc

# macOS-generated files
.DS_Store
```

## Team

Built by Hayley (lucky-ee).

```bash
metric-spell-checker/
├── engine.py
├── bktree.py
├── test_engine.py
├── .gitignore
└── README.md
```