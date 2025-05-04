"""
Filename: test_get_project_root.py

Tests the get_project_root utility function from toolscape.

Uses Dynamic Import Methodology (📜 5.5: May 3, 4:05 – Canonizing the Dynamic Import Test Methodology)
"""

import os
import sys
import importlib.util
import pytest
from pathlib import Path

# ✅ Ensure src/ is in sys.path before anything else
project_root = os.path.abspath(os.getcwd())
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# ✅ Load the dynamic_importer helper
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically load the module to test
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        src_path,
        "storybook_fun_factory",
        "toolscape",
        "get_project_root.py",
    )
)

# ✅ Access the function from the dynamically imported module
get_project_root = module.get_project_root

def test_get_project_root_points_to_storybook_fun_factory_root():
    root = get_project_root()
    assert root.name == "storybook_fun_factory"
    assert (root / "pyproject.toml").exists()
