"""
s1_1_it_applies_a_canon_lock_to_all_freshly_sealed_files.py

Applies an immutable canon lock to any file marked as freshly sealed.
This lock prevents further edits by converting file permissions to read-only
and embedding a lock marker in file metadata or inline content.

The canon lock ensures that once a stanza has passed validation and been
formally sealed by codex_builder, no mutation or overwrite is permitted.

Dependencies:
- pathlib
- hashlib
- os
- json

Expected lock format:
- Lock marker file named `.canon_lock` in same directory
- Contains JSON with filename, timestamp, hash

Example Usage:
>>> from s1_1_it_applies_a_canon_lock_to_all_freshly_sealed_files import apply_canon_lock
>>> apply_canon_lock("my_poem_line.py")

Result:
- my_poem_line.py is made read-only
- .canon_lock is created in same folder
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

LOCK_FILENAME = ".canon_lock"

def calculate_sha256(file_path: Path) -> str:
    """Returns the SHA-256 hash of the file."""
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def apply_canon_lock(file_path: str) -> dict:
    """
    Applies a canon lock to a given file by:
    1. Setting it to read-only.
    2. Recording metadata in a `.canon_lock` marker file.

    Args:
        file_path (str): Path to the freshly sealed stanza file.

    Returns:
        dict: Lock metadata including filename, timestamp, and hash.
    """
    file = Path(file_path).resolve()
    if not file.exists() or not file.is_file():
        raise FileNotFoundError(f"{file_path} does not exist.")

    # Lock metadata
    hash_digest = calculate_sha256(file)
    timestamp = datetime.now(timezone.utc).isoformat()
    metadata = {
        "filename": file.name,
        "timestamp": timestamp,
        "sha256": hash_digest
    }

    # Set file to read-only (Unix & Windows compatible)
    file.chmod(0o444)

    # Write or append to .canon_lock file in same directory
    lock_file = file.parent / LOCK_FILENAME
    if lock_file.exists():
        try:
            with lock_file.open("r", encoding="utf-8") as f:
                existing = json.load(f)
        except json.JSONDecodeError:
            existing = []
    else:
        existing = []

    existing.append(metadata)

    with lock_file.open("w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2)

    return metadata
