"""
s1_4_it_confirms_and_logs_lock_state_for_recursive_trace.py

After a canon lock has been applied, this enforcement line logs the final state
of the lock action—success or failure—to a recursive trace log. This ensures
auditability, rollback alignment, and multi-cycle trust continuity.

The trace file is a structured JSONL file (`.lock_trace.jsonl`) with one log
entry per enforcement action, including status, hash, path, timestamp, and source.

Example Output (per line in .lock_trace.jsonl):
{
  "filename": "s1_1_the_orders_that_mark_the_lines_of_thought.py",
  "status": "locked",
  "sha256": "...",
  "path": ".../high_command/...",
  "timestamp": "2025-05-17T12:00:00Z",
  "source": "canon_enforcement_protocol"
}

Example Usage:
>>> from s1_4_it_confirms_and_logs_lock_state_for_recursive_trace import log_lock_status
>>> log_lock_status("locked_file.py", True, "abc123...")
"""

import json
from datetime import datetime, timezone
from pathlib import Path

TRACE_FILE = ".lock_trace.jsonl"

def log_lock_status(file_path: str, success: bool, hash_value: str, source: str = "canon_enforcement_protocol") -> dict:
    """
    Logs the lock state of a file to the recursive trace log.

    Args:
        file_path (str): Path to the locked file.
        success (bool): True if locking succeeded, False if failed.
        hash_value (str): SHA-256 of the file (or attempted value).
        source (str): Caller or protocol source of the enforcement.

    Returns:
        dict: The logged entry.
    """
    file = Path(file_path).resolve()
    entry = {
        "filename": file.name,
        "status": "locked" if success else "failed",
        "sha256": hash_value,
        "path": str(file),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": source
    }

    with Path(TRACE_FILE).open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    return entry
