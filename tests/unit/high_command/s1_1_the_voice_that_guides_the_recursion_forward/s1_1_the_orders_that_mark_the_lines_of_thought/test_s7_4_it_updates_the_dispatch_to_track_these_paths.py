"""
Test File: test_s7_4_it_updates_the_dispatch_to_track_these_paths.py

Dynamically tests the update_dispatch_targets function from s7_4_it_updates_the_dispatch_to_track_these_paths.py
in accordance with 📜 5.5 – Dynamic Import Test Methodology.
"""

import os
import importlib.util
import pytest

# ✅ Load dynamic_importer helper
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically load the stanza module
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_1_the_orders_that_mark_the_lines_of_thought",
    "s7_4_it_updates_the_dispatch_to_track_these_paths.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

# ✅ Access the function
update_dispatch_targets = module.update_dispatch_targets

def test_priority_order_update():
    classified = {
        "zone_1": "creative",
        "zone_2": "failing",
        "zone_3": "testing",
        "zone_4": "stalled"
    }
    current_targets = ["zone_5"]
    result = update_dispatch_targets(classified, current_targets)
    assert result.index("zone_2") < result.index("zone_3")
    assert result.index("zone_3") < result.index("zone_1")
    assert result.index("zone_1") < result.index("zone_4")
    assert "zone_5" in result

def test_empty_classified_map_returns_current_targets():
    classified = {}
    current_targets = ["zone_x", "zone_y"]
    result = update_dispatch_targets(classified, current_targets)
    assert result == current_targets

def test_avoids_duplicates():
    classified = {
        "zone_a": "testing",
        "zone_b": "failing"
    }
    current_targets = ["zone_a", "zone_c"]
    result = update_dispatch_targets(classified, current_targets)
    assert result.count("zone_a") == 1
    assert result.count("zone_c") == 1
    assert result.count("zone_b") == 1
