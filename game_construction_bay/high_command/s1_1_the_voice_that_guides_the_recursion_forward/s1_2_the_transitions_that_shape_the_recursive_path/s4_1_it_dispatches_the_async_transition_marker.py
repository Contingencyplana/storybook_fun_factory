"""
Filename: s4_2_it_listens_for_crossphase_return_signals.py

Listens for a previously dispatched async recursion marker and retrieves its contents.
Designed for systems that await ghosted or delayed transition signals.

Fulfills Line 2 of Stanza 2 in Cycle 2: asynchronous_crosslayer_recursion/
"""

from pathlib import Path
import json

TRANSITION_MARKER_FILENAME = "async_transition_marker.json"

def listen_for_crossphase_return_signal(search_dir: Path = None) -> dict:
    """
    Listens for an existing async transition marker and returns its contents.

    Parameters:
    - search_dir (Path): Directory to look for the marker. Defaults to current working directory.

    Returns:
    - dict: Parsed contents of the marker file if found.

    Raises:
    - FileNotFoundError: If no marker file is found in the given directory.
    - json.JSONDecodeError: If the marker file exists but is not valid JSON.
    """
    if search_dir is None:
        search_dir = Path.cwd()
    else:
        search_dir = Path(search_dir)

    marker_path = search_dir / TRANSITION_MARKER_FILENAME

    if not marker_path.exists():
        raise FileNotFoundError(f"No async transition marker found at: {marker_path}")

    with marker_path.open("r", encoding="utf-8") as f:
        return json.load(f)
