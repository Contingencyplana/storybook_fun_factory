"""
s3_2_it_marks_which_tests_guard_the_line.py
(Indexes test files associated with stanza line files)

This module maps main stanza line files to their corresponding test files,
enabling high_command to track which parts of the system are protected by tests
and which lines remain unguarded. This aids test coverage visibility, auditing,
and strategic test generation.
"""

import os
import fnmatch
from pathlib import Path
from typing import Dict, List, Optional


class TestCoverageIndex:
    def __init__(self, tests_root: Path, file_prefix: str = "test_", file_suffix: str = ".py"):
        self.tests_root = Path(tests_root)
        self.file_prefix = file_prefix
        self.file_suffix = file_suffix
        self.index: Dict[str, str] = {}  # Maps stanza line filenames to test file paths
        self.build_index()

    def build_index(self) -> None:
        """
        Walk the test suite directory and build a mapping from stanza filenames
        to test file paths (relative to tests_root).
        """
        for root, _, files in os.walk(self.tests_root):
            for name in files:
                if name.startswith(self.file_prefix) and name.endswith(self.file_suffix):
                    stanza_filename = self._extract_main_filename(name)
                    rel_path = os.path.relpath(os.path.join(root, name), self.tests_root)
                    self.index[stanza_filename] = rel_path.replace(os.sep, "/")

    def _extract_main_filename(self, test_filename: str) -> str:
        """
        Convert a test filename (e.g., test_s1_1_it_marks_the_front.py)
        to its corresponding main stanza filename (e.g., s1_1_it_marks_the_front.py).
        """
        if test_filename.startswith(self.file_prefix):
            return test_filename[len(self.file_prefix):]
        return test_filename

    def get_test_for_stanza(self, stanza_filename: str) -> Optional[str]:
        """
        Return the relative path to the test file guarding the given stanza file.
        Returns None if no test is found.
        """
        return self.index.get(stanza_filename)

    def list_unguarded_stanza_files(self, stanza_dir: Path) -> List[str]:
        """
        Scan the given stanza folder for .py files and list those without corresponding tests.
        Returns a list of stanza filenames (e.g., s2_3_the_threads.py) with no matching test.
        """
        stanza_files = fnmatch.filter(os.listdir(stanza_dir), "*.py")
        unguarded = [f for f in stanza_files if f not in self.index]
        return sorted(unguarded)

    def list_all_mapped_tests(self) -> List[tuple]:
        """
        Return all stanza→test file mappings as a sorted list of tuples.
        """
        return sorted(self.index.items())
