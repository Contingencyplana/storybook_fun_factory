# Filename: s2_1_the_echo_stayed_within_the_thread.py

"""
Preserves dormant signals that lingered in the recursive weave—
subtle echoes ignored but never erased.
"""

from datetime import datetime
from pathlib import Path
import hashlib
import uuid

# Define echo storage log path
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
ECHO_LOG = LOG_DIR / "resonant_echo_log.txt"

def capture_dormant_echo(source_event: str, layer_id: str) -> dict:
    """
    Generates and returns a symbolic echo record tied to a past event and logic layer.
    """
    timestamp = datetime.now().isoformat()
    echo_id = str(uuid.uuid4())
    content = f"{timestamp}::{source_event}::{layer_id}::{echo_id}"
    signature = hashlib.sha256(content.encode()).hexdigest()
    return {
        "timestamp": timestamp,
        "source_event": source_event,
        "layer_id": layer_id,
        "echo_id": echo_id,
        "signature": signature
    }

def log_dormant_echo(echo: dict, override_path: Path = None):
    """
    Logs a dormant echo into a symbolic memory register.
    """
    target_log = override_path or ECHO_LOG
    entry = (
        f"[{echo['timestamp']}] "
        f"Echo: '{echo['source_event']}' @ Layer: {echo['layer_id']} "
        f"→ Echo ID: {echo['echo_id'][:8]} | Signature: {echo['signature'][:16]}..."
    )
    target_log.parent.mkdir(parents=True, exist_ok=True)
    with target_log.open("a", encoding="utf-8") as f:
        f.write(entry + "\n")

# Example usage
if __name__ == "__main__":
    example_event = "Unacknowledged loop edge during path stitching."
    example_layer = "memory-to-dream"
    echo = capture_dormant_echo(example_event, example_layer)
    log_dormant_echo(echo)
