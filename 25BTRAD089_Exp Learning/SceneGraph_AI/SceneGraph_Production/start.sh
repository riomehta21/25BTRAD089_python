#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

# If .venv/bin/python is missing or broken (e.g. from Windows), run setup first
if [ ! -f ".venv/bin/python" ]; then
    exec ./run_mac.sh "$@"
fi

exec .venv/bin/python start.py "$@"
