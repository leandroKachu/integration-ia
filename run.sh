#!/bin/bash
PROJECT_DIR="YOUR-PATH/gemini-cli"

# enter your dir

cd "$PROJECT_DIR" || exit 1

"$PROJECT_DIR/.venv/bin/python" "$PROJECT_DIR/gemini-ia.py"