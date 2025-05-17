"""
s2_1_it_checks_for_unapproved_file_deltas_by_hash.py

Compares current file hashes within the project against a stored canonical hash registry.
Raises an alert if any file has been altered post-canonization.

This is a defensive enforcement tool in Cycle 1 of the recursive_enforcement_protocols/
for s1_4_the_sentinels_that_defend_the_lock/.

Expected registry format:
{
    "relative/path/to/file.py": "sha256:abc123...",
    ...
}

Example usage:
>>> from s2_1_it_checks_for_unapproved_file_deltas_by_hash import detect_unapproved_hash_deltas
>>> alert_files = detect_unapproved_hash_deltas("path/to/hash_registry.json", "base/project/dir")
>>> if alert_files:
...     print("Unauthorized edits detected:", alert_files)
"""

import hashlib
import json
from pathlib import Path
from typing import Dict, List


def compute_file_hash(file_path: Path) -> str:
    hasher = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return f"sha256:{hasher.hexdigest()}"


def detect_unapproved_hash_deltas(
    registry_path: str, base_directory: str
) -> List[str]:
    registry = _load_hash_registry(Path(registry_path))
    flagged_files = []

    for rel_path, stored_hash in registry.items():
        file_path = Path(base_directory) / rel_path
        if not file_path.exists():
            flagged_files.append(rel_path)
            continue
        current_hash = compute_file_hash(file_path)
        if current_hash != stored_hash:
            flagged_files.append(rel_path)

    return flagged_files


def _load_hash_registry(registry_path: Path) -> Dict[str, str]:
    with registry_path.open("r", encoding="utf-8") as f:
        return json.load(f)
