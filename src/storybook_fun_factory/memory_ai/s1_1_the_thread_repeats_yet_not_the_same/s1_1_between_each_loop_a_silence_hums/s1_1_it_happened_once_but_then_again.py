"""
Filename: s1_1_it_happened_once_but_then_again.py

Detects repeated recursion signatures—looped behaviors or decisions
subtly altered over time. Compares current context hashes with previously
stored memory traces to identify meaningful recursions.
"""

from hashlib import sha256
from datetime import datetime
from pathlib import Path
import json
from storybook_fun_factory.toolscape.path_utils import get_project_root  # ✅ FIXED IMPORT


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


def load_previous_hashes() -> list:
    """Load stored hashes from memory log."""
    log_file = get_memory_log_file()
    if log_file.exists():
        with open(log_file, "r") as f:
            return json.load(f)
    return []


def save_hash(hash_val: str) -> None:
    """Append a new context hash to the memory log."""
    previous = load_previous_hashes()
    if hash_val not in previous:
        previous.append(hash_val)
        log_file = get_memory_log_file()
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(log_file, "w") as f:
            json.dump(previous, f, indent=2)


def detect_recursion_signature(current_context: dict) -> bool:
    """
    Returns True if the current context appears to be a repetition
    of a previously encountered recursion state.
    """
    current_hash = hash_context(current_context)
    previous_hashes = load_previous_hashes()

    if current_hash in previous_hashes:
        return True  # Recursion signature detected
    else:
        save_hash(current_hash)
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
