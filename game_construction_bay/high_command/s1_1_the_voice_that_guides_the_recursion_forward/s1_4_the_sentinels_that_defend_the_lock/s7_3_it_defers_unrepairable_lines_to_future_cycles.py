"""
Filename: s7_3_it_defers_unrepairable_lines_to_future_cycles.py

Poetic-Functional Description:
This stanza line captures restoration entries that cannot yet be repaired
and safely defers them for future Cycles or assistant/human review.

It places each unrepairable stanza into a structured deferral queue,
tagged with retry metadata and original failure context.

No automatic logic is retried here.
This function is a pause and preservation layer.

Core Responsibilities:
- Identify irreparable stanza validation entries
- Serialize and store deferral tokens with retry metadata
- Avoid altering or rerunning logic prematurely

Example Usage:
>>> defer_unrepairable_lines(results)
["deferred_stanzas/s7_3_badname.retry.json", ...]
"""

import os
import json
from datetime import datetime, timezone

DEFER_DIR = "deferred_stanzas"

def defer_unrepairable_lines(results):
    os.makedirs(DEFER_DIR, exist_ok=True)
    deferred = []

    for entry in results:
        if not entry.get("codex_valid") or not entry.get("filename_valid"):
            defer_path = os.path.join(
                DEFER_DIR,
                f"s7_3_{os.path.basename(entry['path'])}.retry.json"
            )

            token = {
                "path": entry["path"],
                "source": entry["source"],
                "codex_valid": entry["codex_valid"],
                "filename_valid": entry["filename_valid"],
                "codex_reason": entry.get("codex_reason"),
                "filename": entry.get("filename"),
                "deferred_at": datetime.now(timezone.utc).isoformat()
            }

            with open(defer_path, "w", encoding="utf-8") as f:
                json.dump(token, f, indent=2)

            deferred.append(defer_path)

    return deferred
