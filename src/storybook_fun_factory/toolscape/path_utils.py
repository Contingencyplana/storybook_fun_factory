"""
Filename: path_utils.py

Provides utility functions for resolving Storybook FUN Factory project paths.
"""

import os
from pathlib import Path

def get_project_root() -> Path:
    """Return the root directory of the Storybook FUN Factory project."""
    current = Path(__file__).resolve()
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent
    raise FileNotFoundError("Could not locate pyproject.toml to determine project root.")
