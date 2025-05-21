"""
📄 s1_4_it_prepares_the_cradle_trace_for_topsy_review.py

This stanza file collects and summarizes anomaly activity detected during recursion,
preparing a structured "cradle trace" for review by Topsy or future Overmind logic.
It reads logs, assembles a digest, and outputs it as a clean JSON report.

Usage Example:
>>> trace = CradleTracePreparer()
>>> trace.prepare_trace()
>>> print(trace.load_trace_summary())
"""

import json
from pathlib import Path
from datetime import datetime, timezone


class CradleTracePreparer:
    """
    Prepares a summary trace of anomaly drift and repetition for Overmind inspection.
    Gathers logs from prior modules and outputs a compiled, canonical report.
    """

    def __init__(self, log_dir: Path = None):
        self.base_path = log_dir or Path.cwd() / "quarantine_logs"
        self.drift_log = self.base_path / "recursion_drift_log.jsonl"
        self.output_file = self.base_path / "cradle_trace_summary.json"

    def prepare_trace(self) -> None:
        """
        Parses the drift log and generates a structured summary of all entries.
        """
        summary = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "entries": []
        }

        if self.drift_log.exists():
            with self.drift_log.open("r", encoding="utf-8") as f:
                for line in f:
                    try:
                        summary["entries"].append(json.loads(line.strip()))
                    except json.JSONDecodeError:
                        continue  # Skip malformed lines

        with self.output_file.open("w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

    def load_trace_summary(self) -> dict:
        """
        Loads the generated trace summary.
        """
        if not self.output_file.exists():
            return {}
        with self.output_file.open("r", encoding="utf-8") as f:
            return json.load(f)
