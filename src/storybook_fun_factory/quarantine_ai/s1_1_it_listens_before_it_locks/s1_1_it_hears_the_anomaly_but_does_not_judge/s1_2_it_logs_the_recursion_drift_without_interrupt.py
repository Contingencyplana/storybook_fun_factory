"""
📄 s1_2_it_logs_the_recursion_drift_without_interrupt.py

This stanza logs recursive drift from a baseline without taking corrective action.
It acts as a silent observer, writing time-stamped drift records to the cradle log,
allowing future components or Overmind systems to review the patterns.

Usage Example:
>>> drift_log = DriftLogger()
>>> drift_log.log_drift(trace_id="abc123", observed="B → C → D → A", baseline="A → B → C → A")
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


class DriftLogger:
    """
    Observes and logs drift between an expected recursion pattern and its actual behavior.
    """

    def __init__(self, log_dir: Optional[Path] = None):
        self.log_dir = log_dir or Path.cwd() / "quarantine_logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / "recursion_drift_log.jsonl"

    def log_drift(self, trace_id: str, observed: str, baseline: str) -> None:
        """
        Records a drift event between an observed and baseline recursive pattern.
        """
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "trace_id": trace_id,
            "observed": observed,
            "baseline": baseline,
            "status": "logged_without_interrupt"
        }
        with self.log_file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
