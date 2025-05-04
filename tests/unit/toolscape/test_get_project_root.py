"""
Filename: test_get_project_root.py

Tests the get_project_root utility function from toolscape.

Follows the Dynamic Import Methodology (📜 5.5) for compatibility with recursive test structure.
"""

import os
import sys
import importlib.util
import pytest

# ✅ Inject src/ into sys.path before loading anything
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# ✅ Dynamic importer from the correct helper path
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Load the target module dynamically
module = dynamic_importer.dynamic_import_module(
    os.path.join(src_path, "storybook_fun_factory", "toolscape", "get_project_root.py")
)

# ✅ Access the function to test
get_project_root = module.get_project_root

def test_get_project_root_points_to_storybook_fun_factory_root():
    root = get_project_root()
    assert root.name == "storybook_fun_factory"
    assert (root / "pyproject.toml").exists()
