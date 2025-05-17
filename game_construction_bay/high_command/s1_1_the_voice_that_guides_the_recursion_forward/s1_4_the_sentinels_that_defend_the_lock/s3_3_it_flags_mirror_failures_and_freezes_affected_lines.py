"""
s3_3_it_flags_mirror_failures_and_freezes_affected_lines.py

Flags stanza mirror failures (e.g., structure mismatch, trace divergence)
and logs the affected lines into a freeze file for downstream halting or inspection.

Each freeze log entry includes:
- filename
- stanza pair path
- reason
- timestamp

Example usage:
>>> from s3_3_it_flags_mirror_failures_and_freezes_affected_lines import freeze_failed_mirror_lines
>>> mismatches = [
...     {"file": "line1.py", "pair": {"left_stanza_path": "A", "right_stanza_path": "B"}, "reason": "Trace mismatch"}
... ]
>>> freeze_failed_mirror_lines(mismatches, "logs/freeze_log.jsonl")
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict


def _now_iso() -> str:
    return datetime.now().astimezone().isoformat()


def freeze_failed_mirror_lines(
    mismatches: List[Dict[str, str]],
    freeze_log_path: str,
) -> None:
    path = Path(freeze_log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as f:
        for entry in mismatches:
            frozen = {
                "file": entry.get("file"),
                "left_stanza_path": entry.get("pair", {}).get("left_stanza_path"),
                "right_stanza_path": entry.get("pair", {}).get("right_stanza_path"),
                "reason": entry.get("reason"),
                "timestamp": _now_iso(),
            }
            f.write(json.dumps(frozen) + "\n")
