"""
s3_4_it_logs_mirrored_enforcement_status_and_source_pairs.py

Logs the final outcome of mirror stanza verification for each pair.
Outputs to a newline-delimited `.jsonl` file including:
- Pair paths (left and right)
- Status ("passed" or "failed")
- Timestamp
- Optional failure notes or metadata

Example usage:
>>> from s3_4_it_logs_mirrored_enforcement_status_and_source_pairs import log_mirror_status
>>> results = [
...     {"pair": {"left": "A", "right": "B"}, "status": "passed"},
...     {"pair": {"left": "X", "right": "Y"}, "status": "failed", "notes": "Trace mismatch"}
... ]
>>> log_mirror_status(results, "logs/mirror_status_log.jsonl")
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict


def _timestamp() -> str:
    return datetime.now().astimezone().isoformat()


def log_mirror_status(
    summary: List[Dict[str, str]],
    output_path: str
) -> None:
    log_path = Path(output_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with log_path.open("a", encoding="utf-8") as f:
        for result in summary:
            line = {
                "left_stanza_path": result["pair"]["left"],
                "right_stanza_path": result["pair"]["right"],
                "status": result["status"],
                "timestamp": _timestamp(),
            }
            if "notes" in result:
                line["notes"] = result["notes"]
            f.write(json.dumps(line) + "\n")
