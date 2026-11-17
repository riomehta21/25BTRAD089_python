#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

# Create virtual environment if missing or if it's an incompatible Windows venv
if [ ! -f ".venv/bin/activate" ]; then
    echo "Creating clean virtual environment for macOS..."
    rm -rf .venv
    if command -v python3.12 &>/dev/null; then
        python3.12 -m venv .venv
    elif command -v python3.13 &>/dev/null; then
        python3.13 -m venv .venv
    else
        python3 -m venv .venv
    fi
fi

source .venv/bin/activate

# Install requirements if dependencies are missing
if ! python -c "import uvicorn, fastapi" 2>/dev/null; then
    echo "Installing required Python dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

python start.py "$@"
