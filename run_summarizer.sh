#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate virtual environment
source "${SCRIPT_DIR}/.venv/bin/activate"

# Run the Python script
python3 "${SCRIPT_DIR}/obsidian-summarizer.py"

# Deactivate virtual environment
deactivate 