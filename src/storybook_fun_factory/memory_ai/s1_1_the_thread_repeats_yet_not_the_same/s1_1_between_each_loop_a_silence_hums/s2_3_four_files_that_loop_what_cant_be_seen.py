"""
s2_3_four_files_that_loop_what_cant_be_seen.py

Implements deeper memory linking logic—tracing influence across Lines
and simulating hidden recursive cycles. Identifies correlations between
independent memory events and maps them into inferred memory loops.
"""

from pathlib import Path
from typing import List, Dict, Optional
import json
from hashlib import sha256

# Memory trace path shared across memory_ai
TRACE_DIR = Path.cwd() / "memory_ai" / "memory_chain" / "trace_logs"
TRACE_FILE = TRACE_DIR / "recursion_signatures.json"

# Ensure trace directory exists
TRACE_DIR.mkdir(parents=True, exist_ok=True)

def load_all_traces() -> List[Dict]:
    """Load the full list of previously stored memory events."""
    if TRACE_FILE.exists():
        with open(TRACE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def generate_trace_signature(trace: Dict) -> str:
    """
    Generates a simple fingerprint of a trace using component and action,
    allowing lightweight correlation detection.
    """
    raw = f"{trace.get('component', '')}|{trace.get('action', '')}"
    return sha256(raw.encode()).hexdigest()

def detect_loop_clusters(traces: Optional[List[Dict]] = None) -> Dict[str, int]:
    """
    Scans memory events to identify repeated fingerprints—indicative of looping behavior.
    Returns a dictionary mapping trace signatures to their recurrence count.
    """
    traces = traces if traces is not None else load_all_traces()
    fingerprints = {}

    for trace in traces:
        sig = generate_trace_signature(trace)
        fingerprints[sig] = fingerprints.get(sig, 0) + 1

    return {sig: count for sig, count in fingerprints.items() if count > 1}

# Example usage
if __name__ == "__main__":
    loops = detect_loop_clusters()

    if not loops:
        print("🌀 No looping behavior detected across traces.")
    else:
        print("♻️ Loop patterns found:")
        for sig, count in loops.items():
            print(f"  • {sig[:12]}... → {count} recurrences")
