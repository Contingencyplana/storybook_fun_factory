"""
get_project_root.py

Provides a utility function to determine the root directory of the project.
Useful for dynamically resolving paths across recursive stanza files.
"""

from pathlib import Path

def get_project_root() -> Path:
    """
    Returns the root path of the Storybook FUN Factory project.
    Assumes the 'src/storybook_fun_factory' structure.
    """
    return Path(__file__).resolve().parents[3]
