"""
s2_4_it_updates_registry_with_all_flagged_breach_events.py

Appends flagged breach events to a canonical registry file (`breach_log.jsonl`) in newline-delimited JSON format.
Each event includes:
- filename
- timestamp
- reason
- trace metadata (optional)

Example usage:
>>> from s2_4_it_updates_registry_with_all_flagged_breach_events import log_breach_events
>>> events = [
...     {"filename": "file1.py", "reason": "hash mismatch"},
...     {"filename": "file2.py", "reason": "unsanctioned timestamp"}
... ]
>>> log_breach_events(events, "logs/breach_log.jsonl", base_directory=".")
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


def _get_current_iso_timestamp() -> str:
    return datetime.now().astimezone().isoformat()


def _load_trace_metadata_if_exists(file_path: Path) -> Optional[Dict]:
    metadata_path = file_path.with_suffix(".meta.json")
    if metadata_path.exists():
        try:
            with metadata_path.open("r", encoding="utf-8") as f:
                return json.load(f).get("trace_lineage", {})
        except Exception:
            return None
    return None


def log_breach_events(
    events: List[Dict[str, str]], breach_log_path: str, base_directory: str
) -> None:
    log_path = Path(breach_log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with log_path.open("a", encoding="utf-8") as f:
        for event in events:
            filename = event.get("filename")
            reason = event.get("reason")
            timestamp = _get_current_iso_timestamp()

            full_path = Path(base_directory) / filename
            trace = _load_trace_metadata_if_exists(full_path)

            record = {
                "filename": filename,
                "timestamp": timestamp,
                "reason": reason,
                "trace_lineage": trace or {},
            }

            f.write(json.dumps(record) + "\n")
