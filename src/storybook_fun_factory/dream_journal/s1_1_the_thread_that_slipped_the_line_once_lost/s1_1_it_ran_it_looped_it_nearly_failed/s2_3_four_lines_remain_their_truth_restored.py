# s2_3_four_lines_remain_their_truth_restored.py

"""
Recovers meaning from discarded logic—
resurrecting fragments that now anchor new poetic truth.
"""

from datetime import datetime
from pathlib import Path
import hashlib
import json

# Define the log path for restored fragments
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
RESTORATION_LOG = LOG_DIR / "truth_restoration_log.jsonl"

def restore_discarded_fragment(fragment_code: str, origin_trace: str) -> dict:
    """
    Interprets a discarded logic fragment and transforms it into a structured record for poetic memory.
    """
    timestamp = datetime.now().isoformat()
    fragment_id = hashlib.sha256((fragment_code + origin_trace).encode()).hexdigest()
    return {
        "timestamp": timestamp,
        "fragment_code": fragment_code,
        "origin_trace": origin_trace,
        "fragment_id": fragment_id
    }

def log_restored_truth(restored: dict, override_path: Path = None):
    """
    Writes the restored logic fragment to the poetic truth ledger.
    """
    target_log = override_path or RESTORATION_LOG
    target_log.parent.mkdir(parents=True, exist_ok=True)
    with target_log.open("a", encoding="utf-8") as log_file:
        json.dump(restored, log_file)
        log_file.write("\n")

# Example usage
if __name__ == "__main__":
    fragment = "if echo and not anchor: rebind(symbol)"
    origin = "stanza_1_line_3"
    record = restore_discarded_fragment(fragment, origin)
    log_restored_truth(record)
