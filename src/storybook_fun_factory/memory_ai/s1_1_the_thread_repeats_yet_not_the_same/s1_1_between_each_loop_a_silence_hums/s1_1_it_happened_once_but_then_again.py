"""
Filename: s1_1_it_happened_once_but_then_again.py

Detects repeated recursion signatures—looped behaviors or decisions
subtly altered over time. Compares current context hashes with previously
stored memory traces to identify meaningful recursions.

Enhancement: Now also stores reflection metadata when recursion is detected.
"""

# ✅ Ensure src/ is in sys.path first
import sys
import os
from pathlib import Path
import importlib.util

current_file = Path(__file__).resolve()
project_root = current_file.parents[5]
src_path = project_root / "src"

if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

# ✅ Dynamically import get_project_root from toolscape
tool_path = src_path / "storybook_fun_factory" / "toolscape" / "path_utils.py"
spec = importlib.util.spec_from_file_location("toolscape.path_utils", str(tool_path))
toolscape = importlib.util.module_from_spec(spec)
spec.loader.exec_module(toolscape)
get_project_root = toolscape.get_project_root

# ✅ Now it's safe to use standard libs
from hashlib import sha256
from datetime import datetime
import json


def get_memory_log_dir() -> Path:
    """Returns the path to the memory log directory."""
    return get_project_root() / "storybook_fun_factory" / "memory_ai" / "memory_chain" / "trace_logs"


def get_memory_log_file() -> Path:
    """Returns the full path to the memory log file."""
    return get_memory_log_dir() / "recursion_signatures.json"


def hash_context(context: dict) -> str:
    """Generate a SHA-256 hash from a dictionary representing a context snapshot."""
    serialized = json.dumps(context, sort_keys=True)
    return sha256(serialized.encode()).hexdigest()


def load_previous_records() -> dict:
    """Load stored hashes and metadata from memory log."""
    log_file = get_memory_log_file()
    if log_file.exists():
        with open(log_file, "r") as f:
            return json.load(f)
    return {}


def save_record(hash_val: str, context: dict) -> None:
    """Append a new context hash with timestamped metadata to the memory log."""
    records = load_previous_records()
    if hash_val not in records:
        records[hash_val] = {
            "first_seen": datetime.now().isoformat(),
            "context": context
        }
        log_file = get_memory_log_file()
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(log_file, "w") as f:
            json.dump(records, f, indent=2)


def detect_recursion_signature(current_context: dict) -> bool:
    """
    Returns True if the current context appears to be a repetition
    of a previously encountered recursion state.
    """
    current_hash = hash_context(current_context)
    previous_records = load_previous_records()

    if current_hash in previous_records:
        return True  # Recursion signature detected
    else:
        save_record(current_hash, current_context)
        return False


def example_run() -> None:
    """Optional callable entry point for manual testing."""
    example_context = {
        "timestamp": datetime.now().isoformat(),
        "component": "memory_ai",
        "action": "begin_layer_5_cycle",
        "stanza": "trace_intervals_first"
    }

    if detect_recursion_signature(example_context):
        print("🔁 Recursion detected: This path has looped before.")
    else:
        print("🆕 New path: Memory trace stored.")
