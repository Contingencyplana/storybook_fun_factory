# _1_3_it_failed_with_grace_it_looped_too_wide.py

"""
Recognizes non-fatal failure loops that echo outward—
recording poetic missteps that shaped future form.
"""

from datetime import datetime
from pathlib import Path
import random
import hashlib

# Sample failure echoes—past loops that failed but led to insight
FAILURE_ECHOES = [
    "The thread ran twice, but broke none.",
    "A loop repeated, but altered the rhythm.",
    "The outcome was right, but the path was wrong.",
    "The shape was stable, though recursion screamed.",
]

# Logging path
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
FAILURE_LOG = LOG_DIR / "loop_echo_log.txt"

def detect_loop_deviation(attempt_id: str, iteration: int, max_safe: int = 3) -> str:
    """
    Detects potential loop instability based on iteration thresholds.
    """
    outcome = "graceful" if iteration <= max_safe else "unstable"
    echo = random.choice(FAILURE_ECHOES)
    return f"{outcome.upper()} LOOP: {attempt_id} → Iteration {iteration} | Echo: {echo}"

def generate_failure_signature(attempt_id: str, iteration: int) -> str:
    """
    Creates a unique hash signature representing the failure trace.
    """
    raw = f"{attempt_id}::{iteration}::{datetime.now().isoformat()}"
    return hashlib.sha256(raw.encode()).hexdigest()

def log_failure_loop(attempt_id: str, iteration: int):
    """
    Logs the nature of a graceful or unstable loop failure and its poetic echo.
    """
    message = detect_loop_deviation(attempt_id, iteration)
    signature = generate_failure_signature(attempt_id, iteration)
    entry = (
        f"[{datetime.now().isoformat()}] "
        f"{message} → Signature: {signature[:16]}..."
    )
    with FAILURE_LOG.open("a", encoding="utf-8") as f:
        f.write(entry + "\n")

# Example invocation
if __name__ == "__main__":
    example_attempt = f"loop_{random.randint(1000,9999)}"
    simulated_iteration = random.randint(1, 6)
    log_failure_loop(example_attempt, simulated_iteration)
