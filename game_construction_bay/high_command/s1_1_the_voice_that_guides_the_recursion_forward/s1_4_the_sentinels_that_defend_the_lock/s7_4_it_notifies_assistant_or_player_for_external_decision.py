"""
Filename: s7_4_it_notifies_assistant_or_player_for_external_decision.py

Poetic-Functional Description:
This stanza line represents the final step of the recovery failure path.
It surfaces unresolved or conflicting reconstruction decisions for
human or assistant review—inviting manual input before resumption.

This notification system logs each deferral, includes trace data,
and prepares a human-readable summary to be dispatched via UI or console.

Core Responsibilities:
- Scan deferral directory for deferred stanza entries.
- Log each entry with metadata and review rationale.
- Output a summary list of deferred items for assistant/player action.

Example Usage:
>>> notify_external_review("quarantine_zone/deferred/")
['Awaiting review: stanza at /quarantine_zone/deferred/component_xyz']
"""

import os
import json
from datetime import datetime, timezone

def notify_external_review(deferred_dir="quarantine_zone/deferred"):
    """
    Notifies the assistant or player that certain stanza groups
    require manual inspection due to unrecoverable state.

    Returns a summary list of pending reviews.
    """
    if not os.path.exists(deferred_dir):
        return []

    summary = []
    for file in os.listdir(deferred_dir):
        full_path = os.path.join(deferred_dir, file)
        if file.endswith(".json"):
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    summary_line = f"Awaiting review: stanza at {data.get('path', full_path)}"
                    summary.append(summary_line)

                    log_dir = os.path.join(deferred_dir, "logs")
                    os.makedirs(log_dir, exist_ok=True)
                    log_path = os.path.join(log_dir, "review_log.txt")
                    with open(log_path, "a", encoding="utf-8") as log:
                        log.write(json.dumps({
                            "timestamp": datetime.now(timezone.utc).isoformat(),
                            "path": data.get("path", full_path),
                            "source": data.get("source", "unknown"),
                            "reason": data.get("reason", "unspecified"),
                            "status": "awaiting_review"
                        }) + "\n")
            except Exception as e:
                summary.append(f"Failed to parse {file}: {str(e)}")

    return summary
