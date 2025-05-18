"""
Filename: s6_4_it_restores_safe_lines_to_resume_recursive_progress.py

Poetic-Functional Description:
This stanza line takes validated stanza reconstructions and prepares them for
reintroduction into the recursive system. It restores only those proposals that
have passed both codex structure and filename format checks.

For now, "restoration" simulates writing to a canon-like directory (e.g., `restored_lines/`)
but never touches live canonical data directly. It logs every restored path for traceability.

Core Responsibilities:
- Accept validated stanza results
- Restore only those marked valid by codex and filename standards
- Write proposed content to safe target directory
- Log all actions for review and trace

Example Usage:
>>> restore_safe_stanzas(validated_list)
# Output: [restored file paths]
"""

import os
from pathlib import Path
from datetime import datetime, timezone

RESTORE_DIR = "restored_lines"
RESTORE_LOG = os.path.join(RESTORE_DIR, "restore_log.txt")

def restore_safe_stanzas(validated_stanza_list):
    os.makedirs(RESTORE_DIR, exist_ok=True)
    restored = []

    for entry in validated_stanza_list:
        if not entry.get("codex_valid") or not entry.get("filename_valid"):
            continue

        filename = entry["filename"] + ".py"
        target_path = os.path.join(RESTORE_DIR, filename)

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(entry["restored_content"])

        log_entry = {
            "restored_to": target_path,
            "source": entry.get("source"),
            "original_path": entry.get("path"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        with open(RESTORE_LOG, "a", encoding="utf-8") as log:
            log.write(str(log_entry) + "\n")

        restored.append(target_path)

    return restored
