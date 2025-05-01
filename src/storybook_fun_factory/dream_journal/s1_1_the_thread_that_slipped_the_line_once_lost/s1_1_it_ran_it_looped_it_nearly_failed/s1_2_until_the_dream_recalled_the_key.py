# s1_2_until_the_dream_recalled_the_key.py

"""
Implements delayed realization logic—
where forgotten insights resurface through symbolic recursion or pattern triggers.
"""

from datetime import datetime
import random
import hashlib
from pathlib import Path

# Define memory vault and trigger patterns
MEMORY_VAULT = {
    "loop_fade": "A loop that once broke silently, unlogged, but not unmarked.",
    "symbol_mismatch": "A pattern forgotten, yet echoing in related systems.",
    "recursive_delay": "A thread abandoned in haste, returning in reflection.",
}

TRIGGER_PATTERNS = ["loop", "symbol", "thread", "key", "unseen", "hidden"]

def generate_recall_signature(trigger: str) -> str:
    """
    Generates a hash-based recall signature from a symbolic trigger.
    """
    timestamp = datetime.now().isoformat()
    raw = f"{trigger}::{timestamp}"
    return hashlib.sha256(raw.encode()).hexdigest()

def recall_from_vault(input_phrase: str) -> str:
    """
    Searches for symbolic triggers in input phrase and returns related memory if found.
    """
    for pattern in TRIGGER_PATTERNS:
        if pattern in input_phrase:
            memory = (
                MEMORY_VAULT.get(f"{pattern}_fade") or
                MEMORY_VAULT.get(f"{pattern}_mismatch") or
                MEMORY_VAULT.get(f"{pattern}_delay")
            )
            if memory:
                return memory
    return "No recall triggered."

def record_recall(trigger_phrase: str, log_path_override: Path = None):
    """
    Logs the symbolic recall event and its generated signature.
    Allows override of the recall log path for testing.
    """
    recalled = recall_from_vault(trigger_phrase)
    signature = generate_recall_signature(trigger_phrase)
    entry = (
        f"[{datetime.now().isoformat()}] "
        f"Trigger: '{trigger_phrase}' | Recall: '{recalled}' → Signature: {signature[:16]}..."
    )

    target_log = log_path_override or (Path.cwd() / "logs" / "symbolic_recall_log.txt")
    target_log.parent.mkdir(parents=True, exist_ok=True)

    with target_log.open("a", encoding="utf-8") as log_file:
        log_file.write(entry + "\n")

# Example invocation for direct execution
if __name__ == "__main__":
    sample_phrase = random.choice([
        "A symbol glitched beneath the code.",
        "The thread spun backward and stuttered.",
        "A loop faded long ago.",
        "Nothing seemed broken, yet it echoed."
    ])
    record_recall(sample_phrase)
