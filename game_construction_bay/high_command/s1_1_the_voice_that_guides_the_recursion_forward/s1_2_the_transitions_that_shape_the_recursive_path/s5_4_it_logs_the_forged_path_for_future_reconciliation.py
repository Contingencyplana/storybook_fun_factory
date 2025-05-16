"""
Filename: s5_4_it_logs_the_forged_path_for_future_reconciliation.py

Logs suspicious or failed recursive authenticity attempts for later review or narrative integration.

Fulfills Line 4 of Stanza 1 in Cycle 3: recursion_masking_and_identity_forgery/
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict

LOG_FILENAME = "forged_recursion_log.json"

def log_forged_path(
    origin: str, reason: str, metadata: Dict, output_dir: Path = None
) -> Path:
    """
    Appends an entry to the forged recursion log.

    Parameters:
    - origin (str): The claimed origin of the recursion path.
    - reason (str): The reason this path was flagged (e.g., signature mismatch, spoofing).
    - metadata (Dict): Additional context (e.g., timestamp, trace_id, system).
    - output_dir (Path): Optional directory to store the log; defaults to current working directory.

    Returns:
    - Path: The path to the updated log file.
    """
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)

    log_path = output_dir / LOG_FILENAME
    log_data = []

    if log_path.exists():
        try:
            with log_path.open("r", encoding="utf-8") as f:
                log_data = json.load(f)
        except json.JSONDecodeError:
            pass

    entry = {
        "timestamp": datetime.now().isoformat(),
        "origin": origin,
        "reason": reason,
        "metadata": metadata,
    }

    log_data.append(entry)

    with log_path.open("w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)

    return log_path
