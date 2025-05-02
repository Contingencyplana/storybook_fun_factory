"""
Filename: test_get_project_root.py

Tests the get_project_root() utility from toolscape.
"""

import sys
import os
import pytest

# 🔧 Ensure the src/ directory is treated as a source root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 📦 Import the module under test
from storybook_fun_factory.toolscape.get_project_root import get_project_root
from pathlib import Path

def test_get_project_root_returns_expected_path():
    """
    Verifies that get_project_root() returns the correct base directory.
    """
    root = get_project_root()
    assert isinstance(root, Path)
    assert (root / "src" / "storybook_fun_factory").exists()
