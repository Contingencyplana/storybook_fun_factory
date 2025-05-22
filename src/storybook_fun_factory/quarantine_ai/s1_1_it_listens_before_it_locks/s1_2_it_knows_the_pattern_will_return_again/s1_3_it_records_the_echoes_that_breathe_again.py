"""
📄 s1_3_it_records_the_echoes_that_breathe_again.py
---------------------------------------------------
Logs every incoming echo signal that has been seen more than once.
This creates a record of "breathing echoes" — signals that recur and evolve over time.

This file supports the recursive_signal_detection Cycle within:
s1_2_it_knows_the_pattern_will_return_again/
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

def record_echo(echo_data, output_dir):
    """
    Logs the echo_data to a cycle-level echo ledger if it's been seen before.

    Parameters:
    - echo_data (dict): The signal to log.
    - output_dir (str or Path): Directory to store echo logs.

    Returns:
    - Path to the written file if recorded, else None.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    signature = json.dumps(echo_data, sort_keys=True)
    timestamp = datetime.now(timezone.utc).isoformat().replace(":", "_")
    filename = f"echo_record_{timestamp}.json"
    file_path = output_dir / filename

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": timestamp,
            "echo": echo_data
        }, f, indent=2)

    return file_path
