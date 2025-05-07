# File: s5_2_if_focus_breaks_it_restores_the_flow.py

"""
s5_2_if_focus_breaks_it_restores_the_flow.py

Realigns recursive progression by detecting logical breaks in stanza continuity.
Restores focus by identifying which stanza line should be revisited or continued
based on recent activity and file status across a component.
"""

import os
from datetime import datetime
from pathlib import Path

def find_last_modified_file(directory: str) -> str | None:
    """
    Returns the most recently modified .py file (excluding test files) in the given directory tree.
    """
    latest_time = 0
    latest_file = None

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and not file.startswith("test_"):
                path = os.path.join(root, file)
                mod_time = os.path.getmtime(path)
                if mod_time > latest_time:
                    latest_time = mod_time
                    latest_file = path

    return latest_file

def recommend_focus_file(directory: str) -> str | None:
    """
    Suggests which file should be the current focus of recursive continuation.
    If a file was recently updated but its neighbors were not, this may indicate
    a break in stanza flow.
    """
    stanza_files = []

    for root, _, files in os.walk(directory):
        for file in sorted(files):
            if file.endswith(".py") and not file.startswith("test_"):
                full_path = os.path.join(root, file)
                stanza_files.append((full_path, os.path.getmtime(full_path)))

    if not stanza_files:
        return None

    # Detect outlier: latest-modified file where the next in sequence is untouched
    stanza_files.sort(key=lambda tup: tup[0])  # sort by name (stanza order)
    for i in range(len(stanza_files) - 1):
        current_file, current_mtime = stanza_files[i]
        next_file, next_mtime = stanza_files[i + 1]

        if current_mtime > next_mtime + 1800:  # 30 minutes stale gap
            return next_file

    return stanza_files[-1]  # Default to last file if no clear gap found
