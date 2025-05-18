"""
Filename: s6_1_it_quarantines_corrupted_stanza_groups_for_safety.py

Poetic-Functional Description:
This stanza line initiates the recovery process by scanning for stanza folders marked
as corrupted, tainted, or structurally suspect. Upon identification, it relocates the
entire stanza group into a designated quarantine zone within the recursive file system.
This ensures that no further recursion, repair, or assistant execution occurs against
potentially dangerous logic until explicit recovery or rollback is initiated.

It is the first and most important act of recursive containment—moving damage out of
reach without yet attempting restoration.

Core Responsibilities:
- Scan for corrupted stanza markers or flags.
- Move affected folders to the quarantine directory.
- Log the quarantine event with metadata (time, original path, reason).

Example Usage:
>>> quarantine_corrupted_stanza_groups("game_construction_bay")
[
  ("game_construction_bay/filename_ai/broken_stanza", "quarantine_zone/broken_stanza__20250518T041032Z"),
  ...
]
"""

import os
import shutil
from datetime import datetime, timezone

QUARANTINE_FOLDER = "quarantine_zone"
CORRUPTION_MARKERS = ["corrupted.stanza", "tainted.recursion", "quarantine.flag"]

def get_all_stanza_folders(base_path):
    for root, dirs, _ in os.walk(base_path):
        for d in dirs:
            yield os.path.join(root, d)

def is_folder_corrupted(folder_path):
    return any(os.path.exists(os.path.join(folder_path, marker)) for marker in CORRUPTION_MARKERS)

def quarantine_folder(folder_path, quarantine_root):
    os.makedirs(quarantine_root, exist_ok=True)

    folder_name = os.path.basename(folder_path)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    quarantine_path = os.path.join(quarantine_root, f"{folder_name}__{timestamp}")

    shutil.move(folder_path, quarantine_path)
    return quarantine_path

def log_quarantine_action(original_path, quarantine_path):
    log_dir = os.path.join(QUARANTINE_FOLDER, "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "quarantine_log.txt")
    log_entry = {
        "original_path": original_path,
        "quarantine_path": quarantine_path,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "quarantined"
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(str(log_entry) + "\n")

def quarantine_corrupted_stanza_groups(base_path="game_construction_bay"):
    quarantined = []
    for folder in get_all_stanza_folders(base_path):
        if is_folder_corrupted(folder):
            q_path = quarantine_folder(folder, QUARANTINE_FOLDER)
            log_quarantine_action(folder, q_path)
            quarantined.append((folder, q_path))
    return quarantined
