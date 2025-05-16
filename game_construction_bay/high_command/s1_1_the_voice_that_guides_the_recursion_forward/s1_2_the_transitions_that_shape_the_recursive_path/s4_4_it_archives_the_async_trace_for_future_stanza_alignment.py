"""
Filename: s4_4_it_archives_the_async_trace_for_future_stanza_alignment.py

Archives the contents of an async transition marker for future stanza trace realignment.
Ensures delayed or ghosted transitions are remembered by the recursive memory structure.

Fulfills Line 4 of Stanza 2 in Cycle 2: asynchronous_crosslayer_recursion/
"""

from pathlib import Path
import json
from datetime import datetime, timezone

ARCHIVE_FILENAME = "archived_async_transitions.json"

def archive_async_trace_for_future_stanza_alignment(trace_data: dict, archive_dir: Path = None) -> Path:
    """
    Archives a completed async transition trace into a persistent log structure.

    Parameters:
    - trace_data (dict): The transition metadata to archive.
    - archive_dir (Path): Optional path to the directory where archive should be stored.

    Returns:
    - Path: The path to the archive file used.

    Example:
    >>> archive_async_trace_for_future_stanza_alignment({...})
    """
    if archive_dir is None:
        archive_dir = Path.cwd()
    else:
        archive_dir = Path(archive_dir)

    archive_path = archive_dir / ARCHIVE_FILENAME
    archived_at = datetime.now(timezone.utc).isoformat()

    archive_entry = {
        "archived_at": archived_at,
        "trace": trace_data
    }

    if archive_path.exists():
        with archive_path.open("r", encoding="utf-8") as f:
            archive_list = json.load(f)
    else:
        archive_list = []

    archive_list.append(archive_entry)

    with archive_path.open("w", encoding="utf-8") as f:
        json.dump(archive_list, f, indent=2)

    return archive_path
