"""
Filename: s7_1_it_logs_failed_restorations_for_manual_review.py

Poetic-Functional Description:
This stanza line captures all failed stanza restoration attempts, logging them
into a canonical failure registry for later assistant or human review.

Failure can stem from invalid codex structure, filename noncompliance,
conflicts between memory and archive data, or missing reconstruction data.

This stanza line does not halt execution or raise exceptions—it collects,
documents, and prepares unresolved failures for future cycles or manual
inspection.

Core Responsibilities:
- Accept a list of validated stanza results
- Identify those marked invalid (codex or filename)
- Log failure context to a structured file: failed_restorations/failed_log.txt

Example Usage:
>>> log_failed_stanzas(results)
# Output: ["failed_restorations/s6_2_broken_by_disagreement.log"]
"""

import os
from datetime import datetime, timezone

FAILED_LOG_DIR = "failed_restorations"
FAILED_LOG_FILE = os.path.join(FAILED_LOG_DIR, "failed_log.txt")

def log_failed_stanzas(validated_results):
    os.makedirs(FAILED_LOG_DIR, exist_ok=True)
    failures = []

    for entry in validated_results:
        if not entry.get("codex_valid") or not entry.get("filename_valid"):
            record = {
                "path": entry.get("path"),
                "source": entry.get("source"),
                "codex_valid": entry.get("codex_valid"),
                "filename_valid": entry.get("filename_valid"),
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "reason": {
                    "codex_reason": entry.get("codex_reason"),
                    "filename": entry.get("filename"),
                }
            }
            failures.append(record)

    if failures:
        with open(FAILED_LOG_FILE, "a", encoding="utf-8") as f:
            for record in failures:
                f.write(str(record) + "\n")
        return [FAILED_LOG_FILE]
    else:
        return []
