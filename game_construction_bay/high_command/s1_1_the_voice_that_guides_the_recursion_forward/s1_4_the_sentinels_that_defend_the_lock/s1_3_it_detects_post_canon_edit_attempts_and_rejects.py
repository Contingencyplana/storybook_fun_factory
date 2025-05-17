"""
s1_3_it_detects_post_canon_edit_attempts_and_rejects.py

This enforcement layer detects post-canon tampering by recalculating the SHA-256
hash of a locked file and comparing it against the recorded value in `.canon_lock`.

If any deviation is detected—whether from content corruption, unauthorized overwrite,
or hash mismatch—the function will return False and may trigger rejection logic.

Expected `.canon_lock` format (in same folder as locked file):
[
  {
    "filename": "my_file.py",
    "timestamp": "...",
    "sha256": "..."
  }
]

Example Usage:
>>> from s1_3_it_detects_post_canon_edit_attempts_and_rejects import verify_canon_integrity
>>> verify_canon_integrity("my_file.py")
True  # if unchanged
False # if modified
"""

import json
import hashlib
from pathlib import Path

LOCK_FILENAME = ".canon_lock"

def calculate_sha256(file_path: Path) -> str:
    """Returns the SHA-256 hash of the file."""
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_canon_integrity(file_path: str) -> bool:
    """
    Checks if the file matches its stored SHA-256 hash in the .canon_lock.

    Args:
        file_path (str): Path to the canon-locked file.

    Returns:
        bool: True if file hash matches the lock; False otherwise.
    """
    file = Path(file_path).resolve()
    lock_file = file.parent / LOCK_FILENAME

    if not file.exists():
        raise FileNotFoundError(f"{file} does not exist.")
    if not lock_file.exists():
        raise FileNotFoundError(f"{LOCK_FILENAME} not found in {file.parent}")

    with lock_file.open("r", encoding="utf-8") as f:
        entries = json.load(f)

    expected_hash = None
    for entry in entries:
        if entry.get("filename") == file.name:
            expected_hash = entry.get("sha256")
            break

    if expected_hash is None:
        return False  # No record of this file in the lock

    current_hash = calculate_sha256(file)
    return current_hash == expected_hash
