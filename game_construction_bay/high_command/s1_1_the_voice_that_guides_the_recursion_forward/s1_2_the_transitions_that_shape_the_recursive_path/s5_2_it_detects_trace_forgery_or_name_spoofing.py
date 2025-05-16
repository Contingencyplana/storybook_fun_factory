"""
Filename: s5_2_it_detects_trace_forgery_or_name_spoofing.py

Flags falsified trace data or identity shifts in stanza transitions.

Fulfills Line 2 of Stanza 1 in Cycle 3: recursion_masking_and_identity_forgery/
"""

from pathlib import Path
import json
import hashlib

TRACE_FILENAME = "stanza_trace.json"

def is_trace_forged(trace_path: Path, expected_origin_hash: str) -> bool:
    """
    Checks whether the trace file at `trace_path` has been forged by
    comparing the stored origin hash to the expected one.

    Parameters:
    - trace_path (Path): Path to the stanza trace JSON file.
    - expected_origin_hash (str): The valid hash signature of the stanza's origin.

    Returns:
    - bool: True if the trace appears to be forged, False otherwise.
    """
    trace_path = Path(trace_path)

    if not trace_path.exists():
        return True  # Missing trace file is considered suspicious

    try:
        with trace_path.open("r", encoding="utf-8") as f:
            trace_data = json.load(f)

        actual_hash = trace_data.get("origin_hash", "")
        return actual_hash != expected_origin_hash

    except (json.JSONDecodeError, KeyError):
        return True  # Corrupt or incomplete trace = potentially forged

def compute_origin_hash(stanza_id: str, author: str, timestamp: str) -> str:
    """
    Computes a hash signature based on stanza ID, author, and timestamp.

    Parameters:
    - stanza_id (str): Unique identifier for the stanza.
    - author (str): Identity of the stanza's originator.
    - timestamp (str): ISO-format timestamp of creation.

    Returns:
    - str: A SHA-256 hash representing the stanza's origin.
    """
    base_string = f"{stanza_id}:{author}:{timestamp}"
    return hashlib.sha256(base_string.encode("utf-8")).hexdigest()
