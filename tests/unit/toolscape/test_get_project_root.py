"""
Filename: test_get_project_root.py

Tests the get_project_root utility function from toolscape.

Ensures that it reliably locates the project root directory.
"""

import os
import sys
import pytest

# 🛠️ Manually inject 'src/' into sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ✅ Now imports work as expected
from storybook_fun_factory.toolscape.get_project_root import get_project_root


def test_get_project_root_points_to_storybook_fun_factory_root():
    root = get_project_root()
    assert root.name == "storybook_fun_factory"
    assert (root / "pyproject.toml").exists()
