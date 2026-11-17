=#!/usr/bin/env python3
"""Root launcher forwarding to SceneGraph_Production/start.py."""
import os
import shutil
import subprocess
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent / "SceneGraph_Production"
if sys.platform == "win32":
    venv_py = APP_DIR / ".venv" / "Scripts" / "python.exe"
else:
    venv_py = APP_DIR / ".venv" / "bin" / "python"

if venv_py.is_file():
    py_bin = str(venv_py)
else:
    py_bin = (
        shutil.which("python3.12")
        or shutil.which("python3.13")
        or shutil.which("python3")
        or sys.executable
    )

raise SystemExit(subprocess.call([py_bin, str(APP_DIR / "start.py"), *sys.argv[1:]], cwd=str(APP_DIR)))
