"""
Test File: test_s8_1_it_detects_each_depth_and_marks_the_place.py

Tests the recursive stanza file detector in High Command Cycle 4, Stanza 1, Line 1.
Follows the dynamic import methodology (📜 5.5) and verifies proper detection of stanza lines.
"""

import os
import sys
import tempfile
import shutil
import importlib.util
from pathlib import Path
import pytest

# Load dynamic_importer
HELPER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py"))
spec = importlib.util.spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Dynamically load the target module
MODULE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../../game_construction_bay/high_command/s1_1_the_orders_that_mark_the_lines_of_thought/s8_1_it_detects_each_depth_and_marks_the_place.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
detect_layer5_stanza_files = module.detect_layer5_stanza_files

def test_detect_layer5_stanza_files():
    with tempfile.TemporaryDirectory() as tmpdirname:
        project_root = Path(tmpdirname)
        gc_bay = project_root / "game_construction_bay"
        gc_bay.mkdir()

        # Create mock components and stanza files
        for component in module.COMPONENTS:
            stanza_path = gc_bay / component / "s1_1_mock_stanza"
            stanza_path.mkdir(parents=True)
            (stanza_path / "s8_1_example.py").touch()
            (stanza_path / "s9_4_example.py").touch()

        result = detect_layer5_stanza_files(project_root)

        for component in module.COMPONENTS:
            assert component in result
            detected = result[component]
            assert any("s8_1_example.py" in f for f in detected)
            assert any("s9_4_example.py" in f for f in detected)
