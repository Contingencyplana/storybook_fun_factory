# _1_4_and_left_a_mark_it_could_not_hide.py

"""
Registers permanent traces left behind by recursion errors—
ensuring that every deviation becomes part of poetic memory.
"""

from datetime import datetime
from pathlib import Path
import hashlib
import uuid

# Path to memory mark log
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
PERMANENT_TRACE_LOG = LOG_DIR / "permanent_trace_log.txt"

def create_permanent_trace(error_description: str) -> dict:
    """
    Creates a permanent trace record from a recursive error description.
    """
    timestamp = datetime.now().isoformat()
    mark_id = str(uuid.uuid4())
    content = f"{timestamp}::{error_description}::{mark_id}"
    signature = hashlib.sha256(content.encode()).hexdigest()
    return {
        "timestamp": timestamp,
        "description": error_description,
        "mark_id": mark_id,
        "signature": signature,
    }

def log_permanent_trace(trace: dict, override_path: Path = None):
    """
    Writes the permanent trace record to a symbolic memory log.
    """
    target_log = override_path or PERMANENT_TRACE_LOG
    entry = (
        f"[{trace['timestamp']}] "
        f"Trace: '{trace['description']}' "
        f"→ Mark ID: {trace['mark_id'][:8]} | Signature: {trace['signature'][:16]}..."
    )
    target_log.parent.mkdir(parents=True, exist_ok=True)
    with target_log.open("a", encoding="utf-8") as f:
        f.write(entry + "\n")

# Example execution
if __name__ == "__main__":
    sample_error = "Recursion slipped through an undefined state transition."
    trace = create_permanent_trace(sample_error)
    log_permanent_trace(trace)
