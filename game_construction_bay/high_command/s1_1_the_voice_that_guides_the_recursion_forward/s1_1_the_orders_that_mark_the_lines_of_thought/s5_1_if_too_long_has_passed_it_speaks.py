# File: s5_1_if_too_long_has_passed_it_speaks.py

"""
s5_1_if_too_long_has_passed_it_speaks.py

Detects when a file has remained untouched beyond an acceptable threshold,
and issues a prompt for review or action if necessary. Ensures no stanza line
is silently forgotten or stalled in recursive progression.
"""

import os
import time

def file_has_been_idle_too_long(file_path: str, max_idle_seconds: int = 3600) -> bool:
    if not os.path.exists(file_path):
        return False
    last_modified_time = os.path.getmtime(file_path)
    current_time = time.time()
    return (current_time - last_modified_time) > max_idle_seconds

def list_stale_files(directory: str, max_idle_seconds: int = 3600) -> list[str]:
    stale_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and not file.startswith("test_"):
                full_path = os.path.join(root, file)
                if file_has_been_idle_too_long(full_path, max_idle_seconds):
                    stale_files.append(full_path)
    return stale_files
