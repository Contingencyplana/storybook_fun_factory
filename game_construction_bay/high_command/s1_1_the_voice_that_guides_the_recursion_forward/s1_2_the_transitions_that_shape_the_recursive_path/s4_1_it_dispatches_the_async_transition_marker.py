"""
Filename: s4_1_it_dispatches_the_async_transition_marker.py

Dispatches a marker representing an asynchronous recursion transition.
This marker can be later picked up by async receivers or systems awaiting off-thread recursion.

Fulfills Line 1 of Stanza 2 in Cycle 2: asynchronous_crosslayer_recursion/
"""

from pathlib import Path
import json
from datetime import datetime, UTC

TRANSITION_MARKER_FILENAME = "async_transition_marker.json"

def dispatch_async_transition_marker(destination: str, metadata: dict, output_dir: Path = None) -> Path:
    """
    Dispatches an asynchronous transition marker for a recursion shift that will occur out-of-phase.

    Parameters:
    - destination (str): The logical endpoint or next zone/system expected to receive this marker.
    - metadata (dict): A dictionary containing additional contextual data (e.g., transition_id, stanza, timestamp).
    - output_dir (Path): Optional path for where to write the marker file. Defaults to cwd() if not specified.

    Returns:
    - Path: The path to the created marker file.
    """
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)

    marker_data = {
        "destination": destination,
        "metadata": metadata,
        "dispatched_at": datetime.now(UTC).isoformat()
    }

    marker_path = output_dir / TRANSITION_MARKER_FILENAME

    with marker_path.open("w", encoding="utf-8") as f:
        json.dump(marker_data, f, indent=2)

    return marker_path
