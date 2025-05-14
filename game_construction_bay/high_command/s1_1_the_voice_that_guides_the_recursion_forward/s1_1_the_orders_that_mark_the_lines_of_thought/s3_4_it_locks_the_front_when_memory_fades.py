"""
s3_4_it_locks_the_front_when_memory_fades.py
(Freezes active recursive focus when canonical memory becomes unreadable)

This safeguard system checks the integrity of critical memory files—such as the GDJ index and
test mapping registry—and prevents further updates to stanza focus if these structures are corrupted.
"""

import os
import json


class FrontLockProtocol:
    def __init__(self, gdj_index_path, test_map_path):
        self.gdj_index_path = gdj_index_path
        self.test_map_path = test_map_path
        self.locked = False
        self.status_report = {
            "gdj_index": None,
            "test_map": None,
            "locked": False,
            "errors": []
        }

    def verify_memory_file(self, file_path, label):
        """Try loading a JSON file; record whether it's valid."""
        if not os.path.exists(file_path):
            self.status_report[label] = "missing"
            self.status_report["errors"].append(f"{label} missing.")
            return False
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json.load(f)
            self.status_report[label] = "valid"
            return True
        except json.JSONDecodeError:
            self.status_report[label] = "corrupt"
            self.status_report["errors"].append(f"{label} corrupted.")
            return False

    def evaluate_lock(self):
        """Evaluate whether the system should be locked based on memory file integrity."""
        gdj_ok = self.verify_memory_file(self.gdj_index_path, "gdj_index")
        test_map_ok = self.verify_memory_file(self.test_map_path, "test_map")

        if not (gdj_ok and test_map_ok):
            self.locked = True
            self.status_report["locked"] = True
        return self.locked

    def get_status(self):
        """Return a full status report including lock condition and file validity."""
        return self.status_report
