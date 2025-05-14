"""
s3_3_it_watches_the_helpers_we_depend_on.py
(Watches helper files and critical imports)

This stanza line ensures that vital support files—dynamic import tools,
shared utilities, test scaffolds—are actively monitored by High Command.
It verifies existence, path stability, and import readiness across sessions.
"""

import os
from pathlib import Path
from typing import List


class HelperWatchdog:
    """
    Watches for the presence and readiness of critical helper files in the Storybook FUN Factory project.
    """

    def __init__(self, helper_root: Path = None):
        # Set root path for helper utilities
        self.helper_root = helper_root or Path.cwd() / "tests" / "test_helpers"

    def list_helpers(self) -> List[Path]:
        """
        Lists all Python files in the helper directory.
        """
        if not self.helper_root.exists():
            return []
        return [file for file in self.helper_root.glob("*.py") if file.is_file()]

    def file_exists(self, filename: str) -> bool:
        """
        Checks if a specific helper file exists.
        """
        return (self.helper_root / filename).exists()

    def check_import_ready(self, filename: str) -> bool:
        """
        Validates whether the helper file is syntactically importable (basic check).
        """
        filepath = self.helper_root / filename
        if not filepath.exists():
            return False
        try:
            with open(filepath, encoding="utf-8") as f:
                compile(f.read(), str(filepath), "exec")
            return True
        except Exception:
            return False
