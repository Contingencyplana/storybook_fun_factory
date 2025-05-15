"""
Filename: s4_3_it_resolves_pending_recursions_from_other_layers.py

Processes and resolves pending recursion threads that originated from other layers,
but have not yet been reintegrated into the active canonical stanza chain.

Fulfills Line 3 of Stanza 2 in Cycle 2: asynchronous_crosslayer_recursion/
"""

from pathlib import Path
import json

PENDING_RECURSIONS_FILENAME = "pending_recursions.json"

def resolve_pending_recursions_from_other_layers(source_dir: Path = None) -> list:
    """
    Processes pending recursion transitions that were deferred or originated from other layers.

    Parameters:
    - source_dir (Path): Path to the directory containing the pending_recursions.json file.
                         Defaults to the current working directory.

    Returns:
    - list: A list of resolved recursion transition data (dicts).

    Raises:
    - FileNotFoundError: If no pending_recursions.json is found in the given directory.
    - json.JSONDecodeError: If the file is malformed.
    """
    if source_dir is None:
        source_dir = Path.cwd()
    else:
        source_dir = Path(source_dir)

    pending_file = source_dir / PENDING_RECURSIONS_FILENAME

    if not pending_file.exists():
        raise FileNotFoundError(f"No pending_recursions.json found at: {pending_file}")

    with pending_file.open("r", encoding="utf-8") as f:
        pending_list = json.load(f)

    # Placeholder resolution logic: return as-is for now
    return pending_list
