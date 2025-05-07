"""
Filename: test_s4_1_it_reads_the_lines_that_wait_to_be.py

Tests the functionality of s4_1_it_reads_the_lines_that_wait_to_be.py using dynamic import,
following the canonical methodology defined in 📜 5.5.
"""

import os
import importlib.util
import pytest

# ✅ Load the dynamic importer helper module
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)

spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Construct absolute path to the main stanza file to test
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
target_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_1_the_orders_that_mark_the_lines_of_thought",
    "s4_1_it_reads_the_lines_that_wait_to_be.py"
)

# ✅ Dynamically import the target module
module = dynamic_importer.dynamic_import_module(target_path)

# ✅ Access functions to test
read_pending_lines = module.read_pending_lines


def test_read_pending_lines_returns_correct_files():
    mock_status = {
        "line_1.py": "[🔜 Not started]",
        "line_2.py": "[✅ Success!]",
        "line_3.py": "[🔜 Not started]",
        "line_4.py": "[⏳ In progress]",
    }

    result = read_pending_lines(mock_status)
    assert result == ["line_1.py", "line_3.py"]


def test_read_pending_lines_empty_result():
    mock_status = {
        "line_1.py": "[✅ Success!]",
        "line_2.py": "[⏳ In progress]",
    }

    result = read_pending_lines(mock_status)
    assert result == []


def test_read_pending_lines_custom_marker():
    mock_status = {
        "line_1.py": "[WAITING]",
        "line_2.py": "[✅ Success!]",
        "line_3.py": "[WAITING]",
    }

    result = read_pending_lines(mock_status, marker="[WAITING]")
    assert result == ["line_1.py", "line_3.py"]
