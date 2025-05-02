"""
test_get_project_root.py

Tests the get_project_root function used to dynamically resolve project root paths.
"""

import os
from storybook_fun_factory.toolscape.get_project_root import get_project_root

def test_project_root_points_to_expected_folder():
    root = get_project_root()
    assert root.name == "storybook_fun_factory"
    assert os.path.isdir(root)
