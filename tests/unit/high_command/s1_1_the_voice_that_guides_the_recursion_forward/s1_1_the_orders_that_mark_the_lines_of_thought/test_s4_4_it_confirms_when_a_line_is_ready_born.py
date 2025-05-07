"""
Filename: test_s4_4_it_confirms_when_a_line_is_ready_born.py

Tests the readiness validation logic defined in s4_4_it_confirms_when_a_line_is_ready_born.py
using dynamic import methodology as established in 📜 5.5.
"""

import os
import importlib.util
import pytest

# ✅ Load the dynamic importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically import the stanza file to be tested
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
target_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_1_the_orders_that_mark_the_lines_of_thought",
    "s4_4_it_confirms_when_a_line_is_ready_born.py"
)
module = dynamic_importer.dynamic_import_module(target_path)

# ✅ Access the target functions
get_ready_lines = module.get_ready_lines
all_lines_ready = module.all_lines_ready


def test_get_ready_lines_extracts_only_successful():
    status_map = {
        "line_1.py": "[✅ Success!]",
        "line_2.py": "[⏳ In progress]",
        "line_3.py": "[✅ Success!]",
        "line_4.py": "[🔜 Not started]",
    }
    result = get_ready_lines(status_map)
    assert result == ["line_1.py", "line_3.py"]


def test_all_lines_ready_true_if_all_success():
    status_map = {
        "line_1.py": "[✅ Success!]",
        "line_2.py": "[✅ Success!]",
        "line_3.py": "[✅ Success!]",
    }
    assert all_lines_ready(status_map) is True


def test_all_lines_ready_false_if_any_incomplete():
    status_map = {
        "line_1.py": "[✅ Success!]",
        "line_2.py": "[⏳ In progress]",
    }
    assert all_lines_ready(status_map) is False
