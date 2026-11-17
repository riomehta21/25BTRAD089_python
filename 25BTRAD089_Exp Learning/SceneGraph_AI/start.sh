#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/SceneGraph_Production"
exec ./start.sh "$@"
