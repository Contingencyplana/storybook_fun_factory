"""
Filename: s3_4_it_merges_the_shifted_thread_with_canon.py

Reinserts or merges a shifted recursion thread into the primary canon structure.
Useful after asynchronous or divergent recursion paths have been reconciled.

Expected behavior:
- Read both the original canon and the shifted thread
- Merge unique segments from the thread into the canon
- Return the merged canon structure as a list of steps
"""

import json
from pathlib import Path
from typing import List


def merge_shifted_thread_with_canon(canon_path: Path, thread_path: Path) -> List[str]:
    """
    Merges the shifted recursion thread into the main canon.

    Args:
        canon_path (Path): Path to the canonical recursion trace file (JSON list)
        thread_path (Path): Path to the shifted thread trace file (JSON list)

    Returns:
        List[str]: Merged canonical trace

    Example:
        >>> merge_shifted_thread_with_canon(Path("canon.json"), Path("thread.json"))
        ['A', 'B', 'C', 'X']
    """
    if not canon_path.exists():
        raise FileNotFoundError(f"Canon file not found: {canon_path}")
    if not thread_path.exists():
        raise FileNotFoundError(f"Thread file not found: {thread_path}")

    with open(canon_path, "r", encoding="utf-8") as f:
        canon = json.load(f)
    with open(thread_path, "r", encoding="utf-8") as f:
        thread = json.load(f)

    merged = canon[:]
    for step in thread:
        if step not in merged:
            merged.append(step)

    return merged
