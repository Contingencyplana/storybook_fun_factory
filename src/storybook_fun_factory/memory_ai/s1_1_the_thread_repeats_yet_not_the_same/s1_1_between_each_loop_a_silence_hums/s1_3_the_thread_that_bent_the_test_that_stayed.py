"""
_1_3_the_thread_that_bent_the_test_that_stayed.py

Logs persistent deviations or tests that altered future recursion—
marking branching points in memory. Records decision signatures and
compares them to expected paths, flagging unexpected but lasting changes.
"""

from pathlib import Path
import json
from datetime import datetime
from hashlib import sha256

# Deviation log directory and file
DEVIATION_LOG_DIR = Path.cwd() / "memory_ai" / "memory_chain" / "trace_logs"
DEVIATION_LOG_FILE = DEVIATION_LOG_DIR / "branching_points.json"

# Ensure log directory exists
DEVIATION_LOG_DIR.mkdir(parents=True, exist_ok=True)

def hash_decision_path(path_signature: list[str]) -> str:
    """Hashes a list of stringified decisions to produce a stable signature."""
    serialized = "|".join(path_signature)
    return sha256(serialized.encode()).hexdigest()

def load_branching_points() -> dict:
    """Load previously stored branching point data."""
    if DEVIATION_LOG_FILE.exists():
        with open(DEVIATION_LOG_FILE, "r") as f:
            return json.load(f)
    return {}

def record_branch_point(path_signature: list[str], result_state: str) -> str:
    """
    Logs a persistent test or decision path that resulted in
    an unexpected but lasting change in recursive memory.
    Returns a message indicating whether this branch is new or previously seen.
    """
    hashed = hash_decision_path(path_signature)
    branch_data = load_branching_points()

    if hashed in branch_data:
        return "↩️ Branch previously recorded. No new divergence."
    else:
        branch_data[hashed] = {
            "path_signature": path_signature,
            "result_state": result_state,
            "timestamp": datetime.now().isoformat()
        }
        with open(DEVIATION_LOG_FILE, "w") as f:
            json.dump(branch_data, f, indent=2)
        return "🌱 New branch recorded: Recursion deviation captured."

# Example usage
if __name__ == "__main__":
    path = ["start", "observe", "pause", "invert"]
    result = "unexpected_calm_loop"

    msg = record_branch_point(path, result)
    print(msg)
